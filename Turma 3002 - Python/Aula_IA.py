# -----------------------------------------------------------
# AULA DE INTELIGÊNCIA ARTIFICIAL
# Exemplo simples de Machine Learning em Python
# Classificação: aluno aprovado ou reprovado
# -----------------------------------------------------------

# Importando bibliotecas
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# -----------------------------------------------------------
# 1. Criando um conjunto de dados simples
# -----------------------------------------------------------

# Horas de estudo e número de faltas
dados = {
    "horas_estudo": [2, 3, 5, 7, 1, 4, 6, 8],
    "faltas": [8, 6, 2, 1, 10, 5, 2, 0],
    "resultado": ["Reprovado", "Reprovado", "Aprovado", "Aprovado",
                  "Reprovado", "Reprovado", "Aprovado", "Aprovado"]
}

# Transformando em DataFrame
df = pd.DataFrame(dados)

print("Base de dados utilizada:")
print(df)

# -----------------------------------------------------------
# 2. Separando variáveis de entrada e saída
# -----------------------------------------------------------

X = df[["horas_estudo", "faltas"]]  # variáveis de entrada
y = df["resultado"]                 # variável alvo

# -----------------------------------------------------------
# 3. Criando o modelo de Inteligência Artificial
# -----------------------------------------------------------

modelo = DecisionTreeClassifier()

# Treinando o modelo
modelo.fit(X, y)

# -----------------------------------------------------------
# 4. Fazendo uma previsão
# -----------------------------------------------------------

# Novo aluno para prever resultado
novo_aluno = [[4, 3]]  # 4 horas de estudo e 3 faltas

previsao = modelo.predict(novo_aluno)

print("\nPrevisão da IA para o novo aluno:")
print(previsao[0])

# -----------------------------------------------------------
# 5. Testando vários alunos
# -----------------------------------------------------------

novos_alunos = [
    [2, 9],
    [6, 2],
    [5, 1]
]

resultado = modelo.predict(novos_alunos)

print("\nResultados previstos pela IA:")

for i, r in enumerate(resultado):
    print(f"Aluno {i+1}: {r}")