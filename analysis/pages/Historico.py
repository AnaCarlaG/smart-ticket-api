import streamlit as st
import pandas as pd

st.set_page_config(page_title="Histórico", page_icon="📂", layout="wide")

st.title("📂 Histórico de Chamados")
st.caption("Todos os tickets analisados pela IA")

try:
    df = pd.read_csv("analysis/tickets_data.csv")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total", len(df))
    col2.metric("Categorias", df["category"].nunique())
    col3.metric("Prioridade Alta ou Crítica", len(
        df[df["priority"].isin(["ALTA", "CRÍTICA"])]))

    st.divider()

    col_a, col_b = st.columns(2)
    with col_a:
        priority_filter = st.multiselect(
            "Filtrar por prioridade:",
            options=df["priority"].unique(),
            default=df["priority"].unique()
        )
    with col_b:
        category_filter = st.multiselect(
            "Filtrar por categoria:",
            options=df["category"].unique(),
            default=df["category"].unique()
        )

    filtered = df[
        df["priority"].isin(priority_filter) &
        df["category"].isin(category_filter)
    ]

    st.dataframe(
        filtered[["id", "title", "category", "priority", "summary"]],
        use_container_width=True,
        hide_index=True
    )

    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Exportar CSV",
        data=csv,
        file_name="tickets_filtrados.csv",
        mime="text/csv"
    )

except FileNotFoundError:
    st.warning(
        "Nenhum ticket encontrado. Analise chamados primeiro na página 'Analisar Ticket'.")
