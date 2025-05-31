# Importing necessary libraries
import streamlit as st 
from classes.data.dataset import df
from classes.ui.logo import Logo
from classes.ui.pages import Page
from classes.ui.textelements import TextElement

# Home page
homePage = Page(name="TributoSmart Analytics", icon="📊", pageLayout='wide')
Logo(imagePath='assets/teamLogo.png')

# Page's content
TextElement('# 🏢 TributoSmart Analytics')
TextElement('---')
st.dataframe(df)

# Simplified analysis
TextElement('''
           Os dados representam a recuperação tributária ao longo dos meses do ano, detalhando os tributos pagos e devidos, além dos créditos recuperados e da correção pela taxa SELIC.

            - Tributos Pagos VS Tributos Devidos: Observamos que em todos os meses os tributos pagos foram superiores aos tributos devidos. Essa diferença pode representar impostos pagos indevidamente ou antecipadamente, gerando oportunidade de recuperação tributária.

            - Créditos Recuperados e Correção SELIC: Os créditos recuperados variam ao longo dos meses, com valores mais expressivos em Fevereiro, Março e Outubro, indicando períodos de maior restituição fiscal. A correção pela SELIC é relativamente baixa e não influencia de forma significativa no total recuperado.

            - Total Recuperado: Os meses de Fevereiro, Março e Outubro tiveram os maiores valores recuperados, o que pode indicar períodos de maior revisão fiscal ou compensação de créditos tributários.          
            ''')

# Hiding humburguer menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Footer
footer = """
<style>
    .footer {
        width: 100%;
        text-align: center;
        padding: 10px;
        font-weight: bold;
    }
</style>
<div class="footer">
    &copy; Team Contabilidade - All rights reserved
</div>
"""

# Exibindo o footer no app
st.markdown(footer, unsafe_allow_html=True)