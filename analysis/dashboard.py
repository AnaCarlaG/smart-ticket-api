import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

st.set_page_config(page_title="Smart Ticket Dashboard",
                   page_icon="🎫", layout="wide")

st.title("🎫 Smart Ticket API")
st.caption("Dashboard de análise de chamados de TI com Inteligência Artificial")

df = pd.read_csv("analysis/tickets_data.csv")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Chamados", len(df))
col2.metric("Prioridade Alta", len(df[df["priority"] == "ALTA"]))
col3.metric("Prioridade Crítica", len(df[df["priority"] == "CRÍTICA"]))
col4.metric("Categorias", df["category"].nunique())

st.divider()

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Chamados por Categoria")
    cat_counts = df["category"].value_counts()

    category_colors = ["#6366f1", "#f97316", "#22c55e",
                       "#ef4444", "#3b82f6", "#a855f7", "#eab308"]
    colors_cat = [category_colors[i %
                                  len(category_colors)] for i in range(len(cat_counts))]

    fig_a, ax_a = plt.subplots(figsize=(6, 4))
    bars_a = ax_a.bar(cat_counts.index, cat_counts.values,
                      color=colors_cat, width=0.5)

    for bar, val in zip(bars_a, cat_counts.values):
        ax_a.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.1,
            str(val),
            ha="center", va="bottom", fontweight="bold"
        )

    ax_a.set_xlabel("Categoria")
    ax_a.set_ylabel("Quantidade")
    ax_a.set_ylim(0, cat_counts.max() + 2)
    ax_a.spines["top"].set_visible(False)
    ax_a.spines["right"].set_visible(False)

    st.pyplot(fig_a)
    plt.close(fig_a)

with col_b:
    st.subheader("Distribuição por Prioridade")
    pri_counts = df["priority"].value_counts()

    priority_colors = {
        "CRÍTICA": "#ef4444",
        "ALTA":    "#f97316",
        "MÉDIA":   "#3b82f6",
        "BAIXA":   "#22c55e"
    }

    colors_pri = [priority_colors.get(p, "#94a3b8") for p in pri_counts.index]

    fig_b, ax_b = plt.subplots(figsize=(6, 4))
    bars_b = ax_b.barh(pri_counts.index, pri_counts.values,
                       color=colors_pri, height=0.5)

    for bar, val in zip(bars_b, pri_counts.values):
        ax_b.text(
            bar.get_width() + 0.1,
            bar.get_y() + bar.get_height() / 2,
            str(val),
            ha="left", va="center", fontweight="bold"
        )

    ax_b.set_xlabel("Quantidade")
    ax_b.set_ylabel("Prioridade")
    ax_b.set_xlim(0, pri_counts.max() + 2)
    ax_b.spines["top"].set_visible(False)
    ax_b.spines["right"].set_visible(False)

    st.pyplot(fig_b)
    plt.close(fig_b)

st.divider()

st.subheader("Tickets Analisados")

priority_filter = st.multiselect(
    "Filtrar por prioridade:",
    options=df["priority"].unique(),
    default=df["priority"].unique()
)

filtered = df[df["priority"].isin(priority_filter)]
st.dataframe(
    filtered[["id", "title", "category", "priority", "summary"]],
    use_container_width=True,
    hide_index=True
)
