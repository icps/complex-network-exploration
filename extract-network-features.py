import collections
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm

from utils import get_subset, get_network
import network_features as nf
    
    
###############
##### Load Data
###############
    
br_checkin = pd.read_csv("br_checkin.csv")
sp_days    = get_subset(br_checkin, "Sao Paulo", time = "diary")
sp_months  = get_subset(br_checkin, "Sao Paulo", time = "monthly")

us_checkin = pd.read_csv("us_checkin.csv")
tk_days    = get_subset(jp_checkin, "Tokyo", time = "diary")
tk_months  = get_subset(jp_checkin, "Tokyo", time = "monthly")

jp_checkin = pd.read_csv("jp_checkin.csv")
nyc_days   = get_subset(us_checkin, "New York", time = "diary")
nyc_months = get_subset(us_checkin, "New York", time = "monthly")


###############
##### Extract Commute Network Features
###############

print("Extracting commute network features")

######## BR - São Paulo
sp_gdays2012, sp_fdays2012 = get_network(sp_days, "2012", features = True)
sp_fdays2012.to_csv("commute_features/SP_network_features2012_isolates_days.csv")

sp_gdays2013, sp_fdays2013 = get_network(sp_days, "2013", features = True)
sp_fdays2013.to_csv("commute_features/SP_network_features2013_isolates_days.csv")

sp_gmonths2012, sp_fmonths2012 = get_network(sp_months, "2012", features = True)
sp_fmonths2012.to_csv("commute_features/SP_network_features2012_isolates_months.csv")

sp_gmonths2013, sp_fmonths2013 = get_network(sp_months, "2013", features = True)
sp_fmonths2013.to_csv("commute_features/SP_network_features2013_isolates_months.csv")


######## JP - Tokyo
tk_gdays2012, tk_fdays2012     = get_network(tk_days, "2012", features = True)
tk_fdays2012.to_csv("commute_features/TK_network_features2012_isolates_days.csv")

tk_gdays2013, tk_fdays2013     = get_network(tk_days, "2013", features = True)
tk_fdays2013.to_csv("commute_features/TK_network_features2013_isolates_days.csv")

tk_gmonths2012, tk_fmonths2012 = get_network(tk_months, "2012", features = True)
tk_fmonths2012.to_csv("commute_features/TK_network_features2012_isolates_months.csv")

tk_gmonths2013, tk_fmonths2013 = get_network(tk_months, "2013", features = True)
tk_fmonths2013.to_csv("commute_features/TK_network_features2013_isolates_months.csv")


######## US - New York
nyc_gdays2012, nyc_fdays2012     = get_network(nyc_days, "2012", features = True)
nyc_fdays2012.to_csv("commute_features/NYC_network_features2012_isolates_days.csv")

nyc_gdays2013, nyc_fdays2013     = get_network(nyc_days, "2013", features = True)
nyc_fdays2013.to_csv("commute_features/NYC_network_features2013_isolates_days.csv")

nyc_gmonths2012, nyc_fmonths2012 = get_network(nyc_months, "2012", features = True)
nyc_fmonths2012.to_csv("commute_features/NYC_network_features2012_isolates_months.csv")

nyc_gmonths2013, nyc_fmonths2013 = get_network(nyc_months, "2013", features = True)
nyc_fmonths2013.to_csv("commute_features/NYC_network_features2013_isolates_months.csv")


###############
##### Extract Contact Network Features
###############

print("Extracting contact network features")

######## BR - São Paulo
sp_gdays2012, sp_fdays2012 = get_network(sp_days, "2012", features = True, contact = True)
sp_fdays2012.to_csv("contact_features/SP_network_features2012_isolates_days.csv")

sp_gdays2013, sp_fdays2013 = get_network(sp_days, "2013", features = True, contact = True)
sp_fdays2013.to_csv("contact_features/SP_network_features2013_isolates_days.csv")

sp_gmonths2012, sp_fmonths2012 = get_network(sp_months, "2012", features = True, contact = True)
sp_fmonths2012.to_csv("contact_features/SP_network_features2012_isolates_months.csv")

sp_gmonths2013, sp_fmonths2013 = get_network(sp_months, "2013", features = True, contact = True)
sp_fmonths2013.to_csv("contact_features/SP_network_features2013_isolates_months.csv")


######## JP - Tokyo
tk_gdays2012, tk_fdays2012 = get_network(tk_days, "2012", features = True, contact = True)
tk_fdays2012.to_csv("contact_features/TK_network_features2012_isolates_days.csv")

tk_gdays2013, tk_fdays2013 = get_network(tk_days, "2013", features = True, contact = True)
tk_fdays2013.to_csv("contact_features/TK_network_features2013_isolates_days.csv")

tk_gmonths2012, tk_fmonths2012 = get_network(tk_months, "2012", features = True, contact = True)
tk_fmonths2012.to_csv("contact_features/TK_network_features2012_isolates_months.csv")

tk_gmonths2013, tk_fmonths2013 = get_network(tk_months, "2013", features = True, contact = True)
tk_fmonths2013.to_csv("contact_features/TK_network_features2013_isolates_months.csv")


######## US - New York
nyc_gdays2012, nyc_fdays2012 = get_network(nyc_days, "2012", features = True, contact = True)
nyc_fdays2012.to_csv("contact_features/NYC_network_features2012_isolates_days.csv")

nyc_gdays2013, nyc_fdays2013 = get_network(nyc_days, "2013", features = True, contact = True)
nyc_fdays2013.to_csv("contact_features/NYC_network_features2013_isolates_days.csv")

nyc_gmonths2012, nyc_fmonths2012 = get_network(nyc_months, "2012", features = True, contact = True)
nyc_fmonths2012.to_csv("contact_features/NYC_network_features2012_isolates_months.csv")

nyc_gmonths2013, nyc_fmonths2013 = get_network(nyc_months, "2013", features = True, contact = True)
nyc_fmonths2013.to_csv("contact_features/NYC_network_features2013_isolates_months.csv")
