#import libraries
import osmnx as ox
import networkx as nx

#call overpass api to retrieve the motorway network of the Netherlands and store in a graph G
place_name=['South Holland, Netherlands',{'state':'Utrecht', 'country':'Netherlands'},'North Brabant, Netherlands', 'Limburg, Netherlands','Gelderland, Netherlands', 'Overijssel, Netherlands','Drenthe, Netherlands', {'state':'Groningen', 'country':'Netherlands'}, 'Friesland, Netherlands', 'Flevoland, Netherlands', 'North Holland, Netherlands']
G = ox.graph_from_place(place_name, network_type='none', infrastructure='way["highway"~"motorway|motorway_links"]')
