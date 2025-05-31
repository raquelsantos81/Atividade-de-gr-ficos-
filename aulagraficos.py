import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard de Estilo", layout="wide")


st.title("👗 Dashboard: Preferências de Cores no Armário")
st.markdown("Este painel mostra a distribuição das cores de roupas no armário.")


df = pd.read_csv("preferencia_cores.csv")


col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Tabela de Dados")
    st.dataframe(df)

with col2:
    st.subheader("🎨 Gráfico de Pizza")
    fig, ax = plt.subplots()
    cores = plt.cm.Paired.colors
    ax.pie(
        df["Peças no Armário"],
        labels=df["Cor"],
        autopct="%1.1f%%",
        startangle=140,
        colors=cores,
        wedgeprops={"edgecolor": "black"}
    )
    ax.set_title("Distribuição das Cores no Armário")
    st.pyplot(fig)


st.markdown("---")
st.subheader("📈 Estatísticas")
st.write(f"**Total de peças:** {df['Peças no Armário'].sum()}")
st.write(f"**Cor mais presente:** {df.loc[df['Peças no Armário'].idxmax(), 'Cor']}")
st.write(f"**Cor menos presente:** {df.loc[df['Peças no Armário'].idxmin(), 'Cor']}")
