import pandas as pd

from utils import generate_date_column

######## BR - São Paulo

br_checkin = pd.read_csv("br_checkin.csv")

print(br_checkin.groupby(["City"]).count()["UserID"].sort_values(ascending = False)[:5])

sp_checkin = br_checkin[br_checkin["City"] == 'Sao Paulo']
sp_checkin = sp_checkin.reset_index(drop = True)

time_info  = [1, 2, 5] ## 1 month, 2 day, 5 year
sp_checkin = generate_date_column(sp_checkin, time_info)

print("\n--- Brasil: São Paulo")
print("{} days, {} users, and {} places".format(len(set(sp_checkin["Date"])), len(set(sp_checkin["UserID"])),
                                                len(set(zip(sp_checkin["Latitude"], sp_checkin["Longitude"])))))


######## US - New York

us_checkin = pd.read_csv("us_checkin.csv")

print(us_checkin.groupby(["City"]).count()["UserID"].sort_values(ascending = False)[:5])

nyc_checkin = us_checkin[us_checkin["City"] == 'New York']
nyc_checkin = nyc_checkin.reset_index(drop = True)

time_info   = [1, 2, 5] ## 1 month, 2 day, 5 year
nyc_checkin = generate_date_column(nyc_checkin, time_info)

print("\n--- EUA: New York")
print("{} days, {} users, and {} places".format(len(set(nyc_checkin["Date"])), len(set(nyc_checkin["UserID"])),
                                                len(set(zip(nyc_checkin["Latitude"], nyc_checkin["Longitude"])))))


######## JP - Tokyo

jp_checkin = pd.read_csv("jp_checkin.csv")

print(jp_checkin.groupby(["City"]).count()["UserID"].sort_values(ascending = False)[:5])

tk_checkin = jp_checkin[jp_checkin["City"] == 'Tokyo']
tk_checkin = tk_checkin.reset_index(drop = True)

time_info   = [1, 2, 5] ## 1 month, 2 day, 5 year
tk_checkin = generate_date_column(tk_checkin, time_info)

print("\n--- Japan: Tokyo")
print("{} days, {} users, and {} places".format(len(set(tk_checkin["Date"])), len(set(tk_checkin["UserID"])),
                                                len(set(zip(tk_checkin["Latitude"], tk_checkin["Longitude"])))))