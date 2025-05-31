# Importing necessary modules
import streamlit as st 
from classes.data.dataset import df

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