import networkx as nx



def degree_sequence(G):
    return [d for n, d in G.degree(weight = 'weight')]


def eigenvector(G):
    return list(nx.eigenvector_centrality_numpy(G, weight = 'weight').values())


def density(G):
    return nx.density(G)


def nodes(G):
    return G.number_of_nodes()


def edges(G):
    return G.number_of_edges()


def subgraphs(G):
    return len(list(nx.connected_components(G)))


def clustering(G):
    return list(nx.clustering(G, weight = 'weight').values())


def closeness(G):
    return list(nx.closeness_centrality(G, distance = 'weight').values())


def assortativity(G):
    return nx.degree_assortativity_coefficient(G, weight = 'weight')


def biggest_component(G):
    
    bcomponent      = {}
    connected_nodes = list(nx.connected_components(G))

    b = 0
    for component in connected_nodes:
        if len(component) > b:
            b = len(component)
            bcomponent = component
            
    return bcomponent
    
    
def diameter(G):
    
    bcomponent = biggest_component(G)
    bgraph     = G.subgraph(bcomponent)
    
    return nx.diameter(bgraph)


def eccentricity(G):
    
    bcomponent = biggest_component(G)
    bgraph     = G.subgraph(bcomponent)
    
    return list(nx.eccentricity(bgraph).values())


def betweenness(G):
    
    bcomponent = biggest_component(G)
    bgraph     = G.subgraph(bcomponent)
    
    return list(nx.betweenness_centrality(bgraph).values())