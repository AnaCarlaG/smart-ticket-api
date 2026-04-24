import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

df = pd.read_csv("analysis/tickets_data.csv")

print(f"Total de tickets analisados: {len(df)}")
print("\nDistribuição por categoria:")
print(df["category"].value_counts())
print("\nDistribuição por prioridade:")
print(df["priority"].value_counts())

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Smart Ticket API - Análise de Chamados",
             fontsize=16, fontweight="bold")

category_counts = df["category"].value_counts()
axes[0].bar(category_counts.index, category_counts.values, color=[
            "#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"])
axes[0].set_title("Chamados por Categoria")
axes[0].set_xlabel("Categoria")
axes[0].set_ylabel("Quantidade")
axes[0].tick_params(axis="x", rotation=30)

priority_order = ["CRÍTICA", "ALTA", "MÉDIA", "BAIXA"]
priority_counts = df["priority"].value_counts().reindex(
    priority_order).dropna()
colors = ["#C44E52", "#DD8452", "#4C72B0", "#55A868"]
axes[1].pie(
    priority_counts.values,
    labels=priority_counts.index,
    autopct="%1.1f%%",
    colors=colors,
    startangle=90
)
axes[1].set_title("Distribuição por Prioridade")

plt.tight_layout()
plt.savefig("analysis/dashboard.png", dpi=150, bbox_inches="tight")
print("\nGráfico salvo em analysis/dashboard.png")
