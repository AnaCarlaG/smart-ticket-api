import httpx
import csv
import time

tickets = [
    "Meu computador não liga depois que caiu no chão",
    "Preciso de acesso ao sistema de RH urgente",
    "A impressora do setor financeiro está sem papel e toner",
    "Esqueci minha senha do e-mail corporativo",
    "O sistema de ponto eletrônico está fora do ar",
    "Meu notebook está superaquecendo e desligando sozinho",
    "Não consigo acessar a VPN de casa",
    "O monitor está com listras na tela",
    "Preciso instalar o pacote Office na minha máquina",
    "O Wi-Fi do escritório está muito lento hoje",
    "Recebi um e-mail suspeito com link pedindo minha senha",
    "O HD externo não está sendo reconhecido pelo Windows",
    "Preciso de permissão para acessar a pasta do projeto X",
    "O sistema de vendas travou durante um fechamento importante",
    "Meu teclado está com várias teclas paradas de funcionar",
    "Não consigo abrir arquivos PDF no meu computador",
    "O servidor de arquivos está inacessível para toda a equipe",
    "Preciso urgente redefinir minha senha do sistema ERP",
    "A webcam não está funcionando para reuniões no Teams",
    "Suspeito que meu computador está com vírus",
]

results = []

print(f"Processando {len(tickets)} tickets...\n")

for i, description in enumerate(tickets, 1):
    try:
        response = httpx.post(
            "http://localhost:8000/api/tickets/analyze",
            json={"description": description},
            timeout=30
        )
        data = response.json()
        results.append({
            "id": i,
            "description": description,
            "title": data.get("title", ""),
            "category": data.get("category", ""),
            "priority": data.get("priority", ""),
            "summary": data.get("summary", ""),
        })
        print(
            f"[{i}/{len(tickets)}] OK - {data.get('category')} | {data.get('priority')}")
        time.sleep(1)
    except Exception as e:
        print(f"[{i}] ERRO: {e}")

with open("analysis/tickets_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f, fieldnames=["id", "description", "title", "category", "priority", "summary"])
    writer.writeheader()
    writer.writerows(results)

print(f"\nPronto! {len(results)} tickets salvos em analysis/tickets_data.csv")
