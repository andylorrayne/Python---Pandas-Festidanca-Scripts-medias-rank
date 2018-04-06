import pandas as pd
import csv

dados = pd.read_csv("respostaFestdanca.csv", encoding='utf-8')
grupos = dados.groupby(["Modalidade","Categoria:","Grupo de Dança:"]).mean().to_csv("rank.csv")
    
print(dados.describe())
