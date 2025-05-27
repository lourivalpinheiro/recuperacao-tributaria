# Importing necessary libraries
import pandas as pd 

# Criando o dicionário com os dados
dados = {
    "Mês": [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ],
    "Tributos Pagos (R$)": [
        18745.4, 24507.14, 22319.94, 20986.58, 16560.19, 16559.95,
        15580.84, 23661.76, 21011.15, 22080.73, 15205.84, 24699.1
    ],
    "Tributos Devidos (R$)": [
        17022.9, 18455.95, 16638.54, 15652.86, 12851.71, 13764.45,
        12589.1, 18285.98, 17921.74, 16226.54, 11754.66, 19551.57
    ],
    "Créditos Recuperados (R$)": [
        1722.5, 6051.19, 5681.4, 5333.72, 3708.48, 2795.5,
        2991.74, 5375.78, 3089.41, 5854.19, 3451.18, 5147.53
    ],
    "Correção SELIC (R$)": [
        218.46, 699.93, 594.4, 499.69, 307.27, 201.65,
        184.05, 274.22, 125.44, 177.39, 69.37, 51.48
    ],
    "Total Recuperado (R$)": [
        1940.96, 6751.12, 6275.8, 5833.41, 4015.75, 2997.15,
        3175.79, 5650.0, 3214.85, 6031.58, 3520.55, 5199.01
    ]
}

# Criando o DataFrame
df = pd.DataFrame(dados)
df.head()

# Total paid taxes by month
paidTaxes = df[['Mês', 'Tributos Pagos (R$)']]

# Total owned taxes by month
ownedTaxes = df[['Mês', 'Tributos Devidos (R$)']]

# Recovered credit by month
recoveredCredit = df[['Mês', 'Créditos Recuperados (R$)']]

# Selic correction by month
selicCorrection = df[['Mês', 'Correção SELIC (R$)']]

# Total recovered by month
totalRecovered = df[['Mês', 'Total Recuperado (R$)']]