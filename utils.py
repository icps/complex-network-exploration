import numpy as np
import pandas as pd
import networkx as nx
from tqdm.notebook import tqdm


def get_dates(df, year):

    lyear = []
    
    all_date = list(set(df["Date"]))

    for date in all_date:
        if year in date:
            lyear.append(date)
            
    return lyear


def generate_date_column(df, info):
    
    cols = list(df.columns)
    days = []
    
    for time in df["Time"]:
        day = ' '.join([time.split(" ")[i] for i in info])
        days.append(day)
    
    df["Date"] = days
    
    cols.remove('Unnamed: 0')
    cols.remove("Time")
    cols.remove("Timezone")
    
    cols = cols + ["Date"]

    df = df[cols]
    
    return df


def get_encounter_edges(data, remove_selfloop = False):
    
    edges = []
    
    latlong = set(zip(data["Latitude"], data["Longitude"]))

    for lat, long in latlong:

        possible_edges = data[(data["Latitude"] == lat) & (data["Longitude"] == long)]

        if len(possible_edges) > 1:
            current_id = []

            for e in range(len(possible_edges) - 1):
                node1 = possible_edges["UserID"].iloc[e]
                node2 = possible_edges["UserID"].iloc[e + 1]

                if remove_selfloop == True:
                    if node1 != node2:                        
                        this_edge = (node1, node2)
                        current_id.append(this_edge)
                else:
                    this_edge = (node1, node2)
                    current_id.append(this_edge)

            edges.extend(current_id)
    
    return edges



def get_place_frequency_edges(data, remove_selfloop = False):
    
    edges = []
    
    users = set(data["UserID"])

    for user in users:
        possible_edges = data[data["UserID"] == user]

        if len(possible_edges) > 1:
            current_id = []

            for e in range(len(possible_edges) - 1):
                node1 = possible_edges["VenueID"].iloc[e]
                node2 = possible_edges["VenueID"].iloc[e + 1]

                if remove_selfloop == True:
                    if node1 != node2:                        
                        this_edge = (node1, node2)
                        current_id.append(this_edge)
                else:
                    this_edge = (node1, node2)
                    current_id.append(this_edge)

            edges.extend(current_id)
    
    return edges


def create_graph(nodes, edges, remove_isolates = False):
    
    G = nx.Graph() # make a directed graph (digraph)

    G.add_nodes_from(list(set(nodes))) # add nodes

    for e in edges:
        e1, e2 = e
        if G.has_edge(e1, e2):
            # we added this one before, just increase the weight by one
            G[e1][e2]['weight'] = G[e1][e2]['weight'] + 1
        else:
            # new edge. add with weight=1
            G.add_edge(e1, e2, weight = 1)
            
    if remove_isolates == True:
        G.remove_nodes_from(list(nx.isolates(G)))
            
    return G


def get_features(G):
    
    degree_sequence   = nf.degree_sequence(G)
    max_degree        = max(degree_sequence)
    min_degree        = min(degree_sequence)
    std_degree        = np.std(degree_sequence)
    mean_degree       = np.mean(degree_sequence)
    
    density           = nf.density(G)
    
    n_nodes           = nf.nodes(G)
    
    n_edges           = nf.edges(G)
    
    n_subgraphs       = nf.subgraphs(G)
    biggest_component = len(nf.biggest_component(G))
    
    clustering        = nf.clustering(G)
    max_clustering    = max(clustering)
    min_clustering    = min(clustering)
    std_clustering    = np.std(clustering)
    mean_clustering   = np.mean(clustering)
    
    closeness         = nf.closeness(G)
    max_closeness     = max(closeness)
    min_closeness     = min(closeness)
    std_closeness     = np.std(closeness)
    mean_closeness    = np.mean(closeness)
    
    assortativity     = nf.assortativity(G)
    
    diameter          = nf.diameter(G)
    
    eccentricity      = nf.eccentricity(G)
    max_eccentricity  = max(eccentricity)
    min_eccentricity  = min(eccentricity)
    std_eccentricity  = np.std(eccentricity)
    mean_eccentricity = np.mean(eccentricity)
    
    betweenness       = nf.betweenness(G)
    max_betweenness   = max(betweenness)
    min_betweenness   = min(betweenness)
    std_betweenness   = np.std(betweenness)
    mean_betweenness  = np.mean(betweenness)
    
    eigenvector       = nf.eigenvector(G)
    max_eigenvector   = max(eigenvector)
    min_eigenvector   = min(eigenvector)
    std_eigenvector   = np.std(eigenvector)
    mean_eigenvector  = np.mean(eigenvector)
    
        
    features = [n_nodes, n_edges, density, n_subgraphs, biggest_component, assortativity, diameter,
                max_degree, min_degree, mean_degree, std_degree, 
                max_clustering, min_clustering, mean_clustering, std_clustering, 
                max_closeness, min_closeness, mean_closeness, std_closeness, 
                max_eccentricity, min_eccentricity, mean_eccentricity, std_eccentricity,
                max_betweenness, min_betweenness, mean_betweenness, std_betweenness,
                max_eigenvector, min_eigenvector, mean_eigenvector, std_eigenvector]
    
    return features


def get_subset(dataset, city, time = "diary"):
    
    subset = dataset[dataset["City"] == city]
    subset = subset.reset_index(drop = True)
    
    if time == "diary":
        time_info = [1, 2, 5] ## 1 month, 2 day, 5 year
        
    elif time == "monthly":
        time_info = [1, 5] ## 1 month, 2 day, 5 year       
 
    subset   = generate_date_column(subset, time_info)
    
    return subset


def get_network(data, year, features = True, contact = False, remove_selfloop = True, remove_isolates = False):

    selected_dates      = get_dates(data, year)
    extracted_features  = pd.DataFrame()
    calculated_networks = []
    
    without_data = []
    for date in tqdm(selected_dates):
        df_dates = data[data["Date"] == date]
        
        if contact == False:
            edges = get_place_frequency_edges(df_dates, remove_selfloop)
            graph = create_graph(df_dates["VenueID"], edges, remove_isolates)
            
        else:
            edges = get_encounter_edges(df_dates, remove_selfloop)
            graph = create_graph(df_dates["UserID"], edges, remove_isolates)
            
        calculated_networks.append((date, graph))
        
        if features == True:
    
            try:
                gfeat              = get_features(graph)
                extracted_features = extracted_features.append(pd.Series(gfeat), ignore_index = True)
            except:
                print(date)
                without_data.append(date)
                pass
            
    if features == True:  
    
        for rm in without_data:
            selected_dates.remove(rm)


        features = ["nodes", "edges", "density", "subgraphs", "biggest_component", "assortativity", "diameter",
                    "max_degree", "min_degree", "std_degree", "mean_degree",
                    "max_clustering", "min_clustering", "mean_clustering", "std_clustering", 
                    "max_closeness", "min_closeness", "mean_closeness", "std_closeness", 
                    "max_eccentricity", "min_eccentricity", "mean_eccentricity", "std_eccentricity",
                    "max_betweenness", "min_betweenness", "mean_betweenness", "std_betweenness",
                    "max_eigenvector", "min_eigenvector", "mean_eigenvector", "std_eigenvector"]

        extracted_features.columns = features
        extracted_features.index   = selected_dates
        extracted_features.index   = pd.to_datetime(extracted_features.index)

        extracted_features.sort_index(inplace = True)

        return calculated_networks, extracted_features
    
    else:
        return calculated_networks



