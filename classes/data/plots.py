# Importing necessary libraries
import plotly.express as px
from data import paidTaxes, ownedTaxes, recoveredCredit, selicCorrection, totalRecovered

# Total paid taxes by month
paidTaxesFig = px.bar(paidTaxes, x='Mês', y='Tributos Pagos (R$)', color_discrete_sequence=["red"], title='Tributos pagos por mês')

# Owned taxes by month
ownedTaxesFig = px.bar(ownedTaxes, x='Mês', y='Tributos Devidos (R$)', color_discrete_sequence=["red"], title='Tributos devidos por mês')

# Recovered credit by month
recoveredCreditFig = px.line(recoveredCredit, x='Mês', y="Créditos Recuperados (R$)", color_discrete_sequence=["red"], title='Crédito recuperado por mês')

# SELIC Correction by month
selicCorrectionFig = px.line(selicCorrection, x='Mês', y='Correção SELIC (R$)', color_discrete_sequence=["red"], title='Correção SELIC por mês')

# Total recovered by month
totalRecoveredFig = px.area(totalRecovered, x='Mês', y='Total Recuperado (R$)', color_discrete_sequence=["red"], title='Total recuperado por mês')