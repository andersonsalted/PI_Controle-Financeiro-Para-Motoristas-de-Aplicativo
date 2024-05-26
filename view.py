# Importando Sqlite
import sqlite3 as lite
import pandas as pd

# Criando conexão
con = lite.connect('dados.db')

# Funções de inclusão 
# Inserir Categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query,i)
    
# Inserir Receita
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query,i)

# Inserir Gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query,i)

# Funções de exclusão

#Deletar Receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)

#Deletar Gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, i)

# Funções para ver dados

# Ver Categorias
def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# Ver Receitas
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# Ver Gastos
def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens


def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista

# Função para dados do grafico dde Barra
def bar_valores():
    #Receitas Total
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receitas_total = sum(receitas_lista)

    #Dispesas Total
    gastos = ver_gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    gastos_total = sum(gastos_lista)

    #Saldo Total
    saldo_total = receitas_total - gastos_total
    
    return [receitas_total, gastos_total, saldo_total]


#Função Grafico Pie
def pie_valores():
    gastos = ver_gastos()
    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista, columns=['id','Categoria', 'Data', 'Valor'])
    dataframe = dataframe.groupby('Categoria')['Valor'].sum()

    lista_quantias = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return([lista_categorias, lista_quantias])


# Função para dados do grafico dde Barra
def porcentagem_valor():
    #Receitas Total
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receitas_total = sum(receitas_lista)

    #Dispesas Total
    gastos = ver_gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    gastos_total = sum(gastos_lista)

    #Porcentagem Total
    total = ((receitas_total - gastos_total) / receitas_total) * 100
    
    return [total]