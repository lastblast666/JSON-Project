from py2neo import Graph, Node, Relationship
import os
import pandas as pd

URL = os.environ.get("http://localhost:7474/")
connect = Graph(URL)
connect.delete_all()

Chemin = 'C:/Krasicki_Alexandre_Hitema/JSON Project/movies_rated_tagged.json'
data = pd.read_json(Chemin)

data = data.drop_duplicates(subset=['title'])

for film in data['title']:
    print("Send {} into node".format(film))
    node_Title = Node('Titre film', name=film)
    connect.create(node_Title)

unique_year_list = []
for year in data['year']:
    if year not in unique_year_list:
        unique_year_list.append(year)
        print("Send {} into node".format(year))
        node_Title = Node('Année film', name=year)
        connect.create(node_Title)


#film_years = Relationship(film, "KNOWS", year)
#graph.create(film_years)
