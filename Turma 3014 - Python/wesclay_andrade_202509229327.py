import pandas as pd 
#as permite dar uma apelido ao pandas
dados_excel = pd.read_excel("notas_py2.xlsx",  engine="openpyxl")
# solicitei a leitura do arquivo excel que contem as notas pd.read_excel("nome do arquivo exato.xlsx")
# o header sinaliza qual linha deve começar minha leitura, precisei mudar devido uma linha mesclada que tava dando erro
print(dados_excel) 
print(dados_excel.columns)
#esse print me permite saber o que a primeira coluna do meu arquivo diz 

#solicitado a impressão dos dados do arquivo

dados_excel['Média'] = (dados_excel['Nota 1 '] + dados_excel['Nota 2']) / 2 
#solicitado o calculo de média, atenção a escrita literal que esta na tabela

dados_excel['situação'] = ['Aprovado' if nota >= 6 else 'Reprovado'for nota in dados_excel['Média']] 
#condição para situação final de aprovado ou não 

print(dados_excel)

