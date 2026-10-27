"""
=============================================================
  MUV Documents — Servidor Web & API de Vendas
  Ficheiro: servidor.py
  Descrição: Servidor HTTP nativo em Python (sem dependências)
             para gerir o dashboard e persistir vendas no CSV.
=============================================================
"""

import http.server
import socketserver
import json
import csv
import os
import urllib.parse
from datetime import datetime

PORTA = 8000
DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_CSV = os.path.join(DIRETORIO_BASE, "vendas.csv")

# Tabela de custos de aquisição estimados para análise de lucro líquido
CUSTOS_PRODUTO = {
    "Laptop":        31500,  # Preço de venda: 45.000 MT (Lucro: 13.500 MT/un)
    "Monitor":        9800,  # Preço de venda: 15.000 MT (Lucro:  5.200 MT/un)
    "Tablet":        19500,  # Preço de venda: 28.000 MT (Lucro:  8.500 MT/un)
    "SSD Externo":    5500,  # Preço de venda:  8.500 MT (Lucro:  3.000 MT/un)
    "Impressora":     8200,  # Preço de venda: 12.500 MT (Lucro:  4.300 MT/un)
    "Teclado":        1100,  # Preço de venda:  1.800 MT (Lucro:    700 MT/un)
    "Cadeira Gamer": 12000,  # Preço de venda: 18.000 MT (Lucro:  6.000 MT/un)
    "Headphones":     2200,  # Preço de venda:  3.500 MT (Lucro:  1.300 MT/un)
    "Rato":            500,  # Preço de venda:    900 MT (Lucro:    400 MT/un)
    "Webcam":         2800,  # Preço de venda:  4.200 MT (Lucro:  1.400 MT/un)
}

def carregar_vendas_csv():
    vendas = []
    if not os.path.exists(ARQUIVO_CSV):
        return vendas

    with open(ARQUIVO_CSV, mode="r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            try:
                venda = {
                    "data": linha.get("data", "").strip(),
                    "cliente": linha.get("cliente", "").strip(),
                    "produto": linha.get("produto", "").strip(),
                    "cidade": linha.get("cidade", "").strip(),
                    "quantidade": int(linha.get("quantidade", 1)),
                    "preco_unitario": float(linha.get("preco_unitario", 0)),
                    "valor_venda": float(linha.get("valor_venda", 0))
                }
                # Adicionar métricas de custo e lucro estimado
                custo_unit = CUSTOS_PRODUTO.get(venda["produto"], venda["preco_unitario"] * 0.65)
                venda["custo_unitario"] = custo_unit
                venda["custo_total"] = custo_unit * venda["quantidade"]
                venda["lucro_estimado"] = venda["valor_venda"] - venda["custo_total"]
                vendas.append(venda)
            except Exception as e:
                continue
    return vendas

def salvar_nova_venda_csv(venda):
    campos = ["data", "cliente", "produto", "cidade", "quantidade", "preco_unitario", "valor_venda"]
    existe = os.path.exists(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        if not existe:
            escritor.writeheader()
        escritor.writerow({
            "data": venda["data"],
            "cliente": venda["cliente"],
            "produto": venda["produto"],
            "cidade": venda["cidade"],
            "quantidade": venda["quantidade"],
            "preco_unitario": venda["preco_unitario"],
            "valor_venda": venda["valor_venda"]
        })

class ServidorVendasHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRETORIO_BASE, **kwargs)

    def do_GET(self):
        url_parsed = urllib.parse.urlparse(self.path)
        caminho = url_parsed.path

        if caminho == "/api/vendas":
            vendas = carregar_vendas_csv()
            self.enviar_json(200, {"sucesso": True, "total": len(vendas), "vendas": vendas})
            return

        elif caminho == "/api/metricas":
            vendas = carregar_vendas_csv()
            total_receita = sum(v["valor_venda"] for v in vendas)
            total_lucro = sum(v["lucro_estimado"] for v in vendas)
            total_itens = sum(v["quantidade"] for v in vendas)

            # Lucro e receita por produto
            produtos_lucro = {}
            for v in vendas:
                p = v["produto"]
                if p not in produtos_lucro:
                    produtos_lucro[p] = {"receita": 0, "lucro": 0, "quantidade": 0}
                produtos_lucro[p]["receita"] += v["valor_venda"]
                produtos_lucro[p]["lucro"] += v["lucro_estimado"]
                produtos_lucro[p]["quantidade"] += v["quantidade"]

            ranking_lucro = sorted(produtos_lucro.items(), key=lambda x: x[1]["lucro"], reverse=True)
            mais_lucrativo = ranking_lucro[0] if ranking_lucro else ("N/A", {"lucro": 0})
            menos_lucrativo = ranking_lucro[-1] if ranking_lucro else ("N/A", {"lucro": 0})

            resposta = {
                "total_registos": len(vendas),
                "total_receita": total_receita,
                "total_lucro_estimado": total_lucro,
                "margem_media": (total_lucro / total_receita * 100) if total_receita else 0,
                "total_itens_vendidos": total_itens,
                "produto_mais_lucrativo": {
                    "produto": mais_lucrativo[0],
                    "lucro": mais_lucrativo[1]["lucro"],
                    "receita": mais_lucrativo[1]["receita"]
                },
                "produto_menos_lucrativo": {
                    "produto": menos_lucrativo[0],
                    "lucro": menos_lucrativo[1]["lucro"],
                    "receita": menos_lucrativo[1]["receita"]
                }
            }
            self.enviar_json(200, resposta)
            return

        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/vendas":
            tamanho = int(self.headers.get("Content-Length", 0))
            corpo = self.rfile.read(tamanho).decode("utf-8")
            try:
                dados = json.loads(corpo)
                campos_obrigatorios = ["data", "cliente", "produto", "cidade", "quantidade", "preco_unitario"]
                for c in campos_obrigatorios:
                    if c not in dados or str(dados[c]).strip() == "":
                        self.enviar_json(400, {"sucesso": False, "erro": f"Campo obrigatório em falta: {c}"})
                        return

                dados["quantidade"] = int(dados["quantidade"])
                dados["preco_unitario"] = float(dados["preco_unitario"])
                dados["valor_venda"] = float(dados.get("valor_venda", dados["quantidade"] * dados["preco_unitario"]))

                salvar_nova_venda_csv(dados)

                self.enviar_json(201, {
                    "sucesso": True,
                    "mensagem": "Venda registada com sucesso!",
                    "venda": dados
                })
            except Exception as e:
                self.enviar_json(500, {"sucesso": False, "erro": str(e)})
            return

        self.enviar_json(404, {"erro": "Rota não encontrada"})

    def enviar_json(self, status, payload):
        conteudo = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(conteudo)))
        self.end_headers()
        self.wfile.write(conteudo)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

def iniciar_servidor():
    with socketserver.TCPServer(("", PORTA), ServidorVendasHandler) as httpd:
        print(f"🚀 Servidor MUV Vendas rodando em: http://localhost:{PORTA}")
        print("Pressione Ctrl+C para encerrar.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor finalizado com sucesso.")

if __name__ == "__main__":
    iniciar_servidor()
