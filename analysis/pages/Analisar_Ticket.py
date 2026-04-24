import streamlit as st
import httpx
import csv
import os

st.set_page_config(page_title="Analisar Ticket", page_icon="🔍", layout="wide")

st.title("🔍 Analisar Novo Chamado")
st.caption("Digite a descrição do problema e a IA irá classificar automaticamente")

with st.form("ticket_form"):
    description = st.text_area(
        "Descrição do chamado",
        placeholder="Ex: Meu computador não liga depois que caiu no chão...",
        height=150
    )
    submitted = st.form_submit_button(
        "🚀 Analisar com IA", use_container_width=True)

if submitted:
    if not description.strip():
        st.warning("Digite a descrição do chamado antes de enviar.")
    else:
        with st.spinner("Analisando com IA..."):
            try:
                response = httpx.post(
                    "http://localhost:8000/api/tickets/analyze",
                    json={"description": description},
                    timeout=30
                )
                data = response.json()

                st.success("Chamado analisado com sucesso!")
                st.divider()

                col1, col2 = st.columns(2)
                col1.metric("Categoria", data.get("category", "-"))
                col2.metric("Prioridade", data.get("priority", "-"))

                st.subheader("📝 Título sugerido")
                st.info(data.get("title", "-"))

                st.subheader("📋 Resumo")
                st.write(data.get("summary", "-"))

                st.subheader("💬 Sugestão de resposta")
                st.success(data.get("suggested_response",
                           data.get("response", "-")))

                csv_path = "analysis/tickets_data.csv"
                file_exists = os.path.exists(csv_path)
                with open(csv_path, "a", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(
                        f, fieldnames=["id", "description", "title", "category", "priority", "summary"])
                    if not file_exists:
                        writer.writeheader()
                    import pandas as pd
                    df = pd.read_csv(
                        csv_path) if file_exists else pd.DataFrame()
                    new_id = len(df) + 1 if not df.empty else 1
                    writer.writerow({
                        "id": new_id,
                        "description": description,
                        "title": data.get("title", ""),
                        "category": data.get("category", ""),
                        "priority": data.get("priority", ""),
                        "summary": data.get("summary", ""),
                    })
                st.caption("✅ Ticket salvo no histórico automaticamente.")

            except Exception as e:
                st.error(f"Erro ao conectar com a API: {e}")
                st.info(
                    "Verifique se a API está rodando com: uvicorn app.main:app --reload")
