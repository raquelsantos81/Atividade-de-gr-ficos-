import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Preferência de Cores", layout="centered")
st.title("🎨 Preferência de Cores nas Roupas do Armário")
st.markdown("Veja quais são as cores mais presentes no seu guarda-roupa!")


arquivo = st.file_uploader("📁 Envie seu arquivo CSV de preferências de cores:", type=["csv"])

if arquivo is not None:
    df = pd.read_csv(arquivo)
    st.write("📊 Dados carregados:")
    st.dataframe(df)

    
    fig, ax = plt.subplots()
    cores = plt.cm.Paired.colors  # Cores bonitas e distintas
    ax.pie(
        df["Peças no Armário"], 
        labels=df["Cor"], 
        autopct="%1.1f%%", 
        startangle=140,
        colors=cores,
        wedgeprops={"edgecolor": "black", "linewidth": 1}
    )
    ax.set_title("Distribuição das Cores no Armário", fontsize=14)
    st.pyplot(fig)

else:
    st.warning("Por favor, envie o arquivo `preferencia_cores.csv`.")
