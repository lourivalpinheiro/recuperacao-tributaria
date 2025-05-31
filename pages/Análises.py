# Importing necessary libraries
import streamlit as st
from classes.ui.logo import Logo
from classes.ui.pages import Page
from classes.ui.textelements import TextElement
from classes.data.plots import paidTaxesFig, ownedTaxesFig, recoveredCreditFig, selicCorrectionFig, totalRecoveredFig

# Page's main configuration
analysisPage = Page(name="Análises", icon="📊", pageLayout='wide')
Logo(imagePath='assets/teamLogo.png')

# Page's content
TextElement('# 📊 Análises')
TextElement('---')

paidTaxesColumn, ownedTaxesColumn = st.columns(2, gap='small')
with paidTaxesColumn:
    # Paid taxes by month
    with st.container(height=520):
        st.plotly_chart(paidTaxesFig, use_container_width=True)

with ownedTaxesColumn:
    # Owned taxes by month
    with st.container(height=520):
        st.plotly_chart(ownedTaxesFig, use_container_width=True)

recoveredCreditColumn, recoveredSum = st.columns(2, gap='small')
with recoveredCreditColumn:
    # Recovered credit by month
    with st.container(height=490):
        st.plotly_chart(recoveredCreditFig, use_container_width=True)

with recoveredSum:
    # SELIC correction by month
    with st.container(height=490):
        st.plotly_chart(selicCorrectionFig, use_container_width=True)

with st.container(height=490):
    st.plotly_chart(totalRecoveredFig, use_container_width=True)

# Detailed analysis
TextElement('''
            # Análise Detalhada dos Dados  

            ## 1️⃣ Tributos Pagos
            ---
            Esta métrica representa o total de tributos efetivamente pagos em cada mês. Os meses com maiores pagamentos foram dezembro (24699,10) e fevereiro (24507,14), enquanto os menores ocorreram em novembro (15205,84) e julho (15580,84).  
            
            ### O que analisar no gráfico?  
            ---
            - A tendência dos pagamentos ao longo do ano.  
            - Identificação de picos sazonais nos pagamentos de tributos.  
            - Possíveis padrões de pagamento vinculados a faturamento ou estratégias fiscais da empresa.  

            ## 2️⃣ Tributos Devidos
            ---
            Os tributos devidos representam as obrigações fiscais calculadas conforme a legislação vigente. Em muitos meses, os tributos pagos superaram os valores devidos, indicando possíveis antecipações ou pagamentos excedentes. O menor valor devido ocorreu em novembro (11754,66), enquanto o maior foi registrado em dezembro (19551,57).  
            
            ### O que analisar no gráfico?  
            ---
            - Diferença entre tributos pagos e devidos.  
            - Identificação de oportunidades de recuperação tributária.  
            - Avaliação do impacto de estratégias de compensação de crédito.  

            ## 3️⃣ Créditos Recuperados
            ---
            Os créditos recuperados representam valores restituídos à empresa por pagamentos indevidos ou compensações fiscais. Os maiores montantes de recuperação foram registrados em fevereiro (6051,19) e outubro (5854,19), enquanto os menores ocorreram em junho (2795,50) e setembro (3089,41).  
            
            ### O que analisar no gráfico?  
            ---
            - Meses em que a recuperação tributária foi mais expressiva.  
            - Comparação dos valores recuperados com os tributos pagos.  
            - Estratégias de maximização de recuperação fiscal.  

            ## 4️⃣ Correção SELIC
            ---
            A correção SELIC reflete a atualização monetária dos valores recuperáveis conforme a taxa de juros aplicada pelo governo. Os valores de correção são relativamente baixos em relação aos tributos pagos e créditos recuperados. O maior ajuste foi registrado em fevereiro (699,93) e o menor em dezembro (51,48).  
            
            ### O que analisar no gráfico?  
            ---
            - Impacto da correção SELIC na recuperação tributária.  
            - Tendência dos valores corrigidos ao longo dos meses.  
            - Estratégias para otimizar compensações fiscais e minimizar perdas monetárias.  

            ## 5️⃣ Total Recuperado
            ---
            Esta métrica corresponde à soma dos créditos recuperados e da correção SELIC, representando o valor total restituído à empresa. Os meses com maiores recuperações foram fevereiro (6751,12) e outubro (6031,58), evidenciando a importância da análise desses períodos. 
             
            ### O que analisar no gráfico?  
            ---
            - Evolução do total recuperado ao longo do ano.  
            - Correlação entre tributos pagos e valores recuperados.  
            - Análise de períodos mais vantajosos para ajustes tributários.  

            ---

            # 📝 Conclusão e Insights  
            ---
            A análise desses dados permite uma visão estratégica sobre a gestão tributária da empresa. Ao acompanhar os gráficos e tendências, os gestores podem identificar oportunidades de recuperação fiscal, reduzir pagamentos indevidos e melhorar o planejamento financeiro.  

            ### Principais pontos de atenção
            --- 
            - Identificar meses de maior impacto na recuperação tributária.  
            - Avaliar padrões sazonais nos tributos pagos e devidos.  
            - Investigar formas de otimizar compensações e minimizar perdas financeiras.  

            Essa seção do dashboard proporcionará insights valiosos para a tomada de decisões estratégicas.
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