import pandas as pd
from py2neo import Graph, Node, Relationship
import os


URL = os.environ.get("http://localhost:7474/")
connect = Graph(URL)
connect.delete_all()


Chemin = 'C:\Krasicki_Alexandre_Hitema\Repo_G8_Dataset_1_House\Dataset_1_house.csv'
data = pd.read_csv(Chemin, sep='|')

print(data)