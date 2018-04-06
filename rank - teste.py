import pandas as pd
import csv


dados = pd.read_csv("rank.csv", encoding='utf-8')

grupo = dados.groupby(by = ["Modalidade", "Categoria:"])
f = lambda x:x.sort_values(by = "Nota da apresentação", ascending=False)

print(grupo.apply(f))




