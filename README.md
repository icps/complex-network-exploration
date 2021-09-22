# Complex Network Exploration

Work made for the Complex Network class in my PhD course (2020).

## Abstract 

Mobility is one of the most important phenomenon in human life, being linked with our existence since the beginning of time. 
In this work, we use data collected from location-based social networks, specifically Foursquare, in order to unveil the dynamics of cities through people's mobility. 
The analysis is made by the Complex Network perspective. 
We build two types of networks: the contact data for people's encounters in a city, and the commute data, for people's trajectories.
We investigated data from New York and Tokyo to understand how the cultural distance impact people's behavior and, consequently, the dynamics of cities.

---

We used the following dataset: https://sites.google.com/site/yangdingqi/home/foursquare-dataset

Please, do not forget to cite their work if using it.

---

The extracted check-ins: https://drive.google.com/drive/folders/1XgK_Wc_Hc65v9iV10WITnsY6orjverdy?usp=sharing

We calculated the cities in a very naive way, be careful.

## Usage 

* Run ```get-country-data.py``` to extract raw check-in information (including cities). We saved this information as ```***_checkin.csv```
* Run ```extract-network-features.py``` to extract network features from commute and contact network
* To check information such as how many days, users, and places are in city data, run ```check-information.py```
* Run the notebooks ```Understanding mobility - *** Network.ipynb``` to see the information about the networks

The pdf ```report``` contains a little report about this work (which I used in my class).


