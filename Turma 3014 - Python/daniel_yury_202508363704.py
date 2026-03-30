import pandas as pd
import random
import os

nome_arquivo = './base_alunos.xlsx'


# Carrega o arquivo Excel para o dataframe.
dataframe = pd.read_excel(nome_arquivo)

# Calculo da media, o cálculo é 'Nota 1' + 'Nota 2 ' / 2
dataframe['media'] = (dataframe['Nota 1'] + dataframe['Nota 2']) / 2

# Itera por cada linha do dataframe e realiza a validação da nota do Aluno através da coluna 'media', se a média 
# for maior ou igual à 6 a atribui a situação como 'Aprovado' se for menor que 6 irá atribuir como 'Reprovado'
dataframe['situacao'] = ( dataframe['media'] >= 6 ).map({True: 'Aprovado', False: 'Reprovado'})

print(dataframe)