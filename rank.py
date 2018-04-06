import pandas as pd
import csv


mod = int(input("Para saber o ranking especifique a modalidade:\n1 - Hip Hop\n2 - Balé Clásico\n3 - Dança de Salão\n"))
if mod == 1:
    cat = int(input("Categoria:\n1 - Infantil\n2 - Infanto-juvenil\n3 - Adulto"))
    ## no teste a modalidade n tem todas as categorias, verificar se haverá todas as cat no real
    if cat == 1:
        modalidade = "Hip Hop"
        categoria= "Infantil"
        dados = pd.read_csv("rank.csv", encoding='utf-8')
        dados = dados[dados["Modalidade"]==modalidade]
        dados = dados[dados["Categoria:"]==categoria]


        print(dados.sort_values(by = "Nota da apresentação",ascending=False))

    elif cat == 2:
        modalidade = "Hip Hop"
        categoria= "Infanto-juvenil"
        dados = pd.read_csv("rank.csv", encoding='utf-8')
        dados = dados[dados["Modalidade"]==modalidade]
        dados = dados[dados["Categoria:"]==categoria]


        print(dados.sort_values(by = "Nota da apresentação",ascending=False))

    elif cat == 3:
        modalidade = "Hip Hop"
        categoria= "Adulto"
        dados = pd.read_csv("rank.csv", encoding='utf-8')
        dados = dados[dados["Modalidade"]==modalidade]
        dados = dados[dados["Categoria:"]==categoria]


        print(dados.sort_values(by = "Nota da apresentação",ascending=False))

elif mod == 2:
    cat = int(input("Categoria:\n1 - Infantil\n2 - Infanto-juvenil\n3 - Adulto"))
    ## no teste a modalidade n tem todas as categorias, verificar se haverá todas as cat no real
    if cat == 1:
        modalidade = "Balé Clássico"
        categoria= "Infantil"
        dados = pd.read_csv("rank.csv", encoding='utf-8')
        dados = dados[dados["Modalidade"]==modalidade]
        dados = dados[dados["Categoria:"]==categoria]


        print(dados.sort_values(by = "Nota da apresentação",ascending=False))

    elif cat == 2:
        modalidade = "Balé Clássico"
        categoria= "Infanto-juvenil"
        dados = pd.read_csv("rank.csv", encoding='utf-8')
        dados = dados[dados["Modalidade"]==modalidade]
        dados = dados[dados["Categoria:"]==categoria]


        print(dados.sort_values(by = "Nota da apresentação",ascending=False))

    elif cat == 3:
        modalidade = "Balé Clássico"
        categoria= "Adulto"
        dados = pd.read_csv("rank.csv", encoding='utf-8')
        dados = dados[dados["Modalidade"]==modalidade]
        dados = dados[dados["Categoria:"]==categoria]


        print(dados.sort_values(by = "Nota da apresentação",ascending=False))
        
elif mod == 3:
    
    cat = int(input("Categoria:\n1 - Infantil\n2 - Infanto-juvenil\n3 - Adulto"))
    ## no teste a modalidade n tem todas as categorias, verificar se haverá todas as cat no real
    if cat == 1:
        modalidade = "Dança de Salão"
        categoria= "Infantil"
        dados = pd.read_csv("rank.csv", encoding='utf-8')
        dados = dados[dados["Modalidade"]==modalidade]
        dados = dados[dados["Categoria:"]==categoria]


        print(dados.sort_values(by = "Nota da apresentação",ascending=False))

    elif cat == 2:
        modalidade = "Dança de Salão"
        categoria= "Infanto-juvenil"
        dados = pd.read_csv("rank.csv", encoding='utf-8')
        dados = dados[dados["Modalidade"]==modalidade]
        dados = dados[dados["Categoria:"]==categoria]


        print(dados.sort_values(by = "Nota da apresentação",ascending=False))

    elif cat == 3:
        modalidade = "Dança de Salão"
        categoria= "Adulto"
        dados = pd.read_csv("rank.csv", encoding='utf-8')
        dados = dados[dados["Modalidade"]==modalidade]
        dados = dados[dados["Categoria:"]==categoria]


        print(dados.sort_values(by = "Nota da apresentação",ascending=False))




