from urllib.parse import quote
import webbrowser
import time
import os

# Caminhos
pasta = os.path.dirname(os.path.abspath(__file__))
arquivo_numeros = os.path.join(pasta, "numeros.txt")

# Verificar se o arquivo numeros.txt existe
if not os.path.exists(arquivo_numeros):
    print(f"Erro: '{arquivo_numeros}' não encontrado!")
    input("Pressione Enter para sair...")
    exit()

# Ler números (tel1;tel2;nome;especialidade)
with open(arquivo_numeros, "r", encoding="utf-8") as f:
    linhas = [linha.strip().split(";") for linha in f if linha.strip()]

# Pedir datas no terminal
data_inicio = input("Digite a data de início (ex: 30/09/2025): ")
data_fim = input("Digite a data de fim (ex: 03/10/2025): ")

# Mensagem base
modelo = """Olá, {nome}!

Sua consulta em {especialidade} foi agendada.
Para retirar o comprovante de agendamento, você precisa comparecer à nossa unidade com o pedido médico de referência, no Setor de Regulação, que funciona de segunda a sexta-feira, das 8h às 17h.

O comprovante estará disponível entre os dias {inicio} e {fim}."""

# Abrir links no navegador
for i, (tel1, tel2, nome, especialidade) in enumerate(linhas, start=1):
    mensagem = modelo.format(nome=nome, especialidade=especialidade, inicio=data_inicio, fim=data_fim)
    mensagem_url = quote(mensagem)

    for tel in (tel1, tel2):
        url = f"https://wa.me/{tel}?text={mensagem_url}"
        webbrowser.open(url)
        print(f"[{i}] Mensagem para {nome} ({especialidade}) enviada para {tel}: {url}")
        time.sleep(10)  # intervalo entre os envios

print("\n✅ Todos os links foram abertos no navegador!")
input("Pressione Enter para finalizar...")