from py2neo import Graph, Node, Relationship
import os
import pandas as pd

URL = os.environ.get("http://localhost:7474/")
connect = Graph(URL)
connect.delete_all()

Chemin = 'C:/Krasicki_Alexandre_Hitema/JSON Project/movies_rated_tagged.json'
data = pd.read_json(Chemin)

data = data.drop_duplicates(subset=['title'])

data_genre_doc = data.iloc[:,3:4]
data_genre_others = data.iloc[:,6:24]
data_category = pd.concat([data_genre_doc, data_genre_others], axis = 1)
data_titre = data['title']

cpt=0
cat_node_unique = []
for title in data['title']:
    titre = Node("Titre du film", name=title)
    for cat in data_category:
        if data[cat].iloc[cpt] == 1:
            #if cat not in cat_node_unique:
            catego = Node("Categorie de film", name=cat)
                #cat_node_unique.append(cat)
            res = Relationship(titre, "KNOWS", catego)
            connect.create(res)

            #elif cat in cat_node_unique:

                #res = Relationship(titre, "KNOWS", catego)
                #connect.create(res)

    cpt = cpt+1

list_title_film = []
for film in data['title']:
    print("Send {} into node".format(film))
    node_Title = Node('Titre film', name=film)
    list_title_film.append(node_Title)
    connect.create(node_Title)

unique_year_list = []
list_year = []
for year in data['year']:
    if year not in unique_year_list:
        unique_year_list.append(year)
        print("Send {} into node".format(year))
        node_year = Node('Année film', name=year)
        list_year.append(node_year)
        connect.create(node_year)

#film_years = Relationship(node_Title, "KNOWS", node_year)
#graph.create(film_years)
