"""
=============================================================
  SISTEMA DE VENDAS - MUV Documents
  Ficheiro: vendas.py
  Descrição: Registo e análise de vendas de produtos
=============================================================
"""

import csv
import os
from datetime import datetime

# ─────────────────────────────────────────────
#  DADOS DE VENDAS
# ─────────────────────────────────────────────

vendas = [
    {"data": "2026-01-03", "cliente": "Carlos Machava",    "produto": "Headphones",   "cidade": "Maputo", "quantidade":  3, "preco_unitario":  3500, "valor_venda":  10500},
    {"data": "2026-01-05", "cliente": "Ana Cossa",         "produto": "Laptop",       "cidade": "Maputo", "quantidade":  2, "preco_unitario": 45000, "valor_venda":  90000},
    {"data": "2026-01-08", "cliente": "João Sitoe",        "produto": "Monitor",      "cidade": "Matola", "quantidade":  3, "preco_unitario": 15000, "valor_venda":  45000},
    {"data": "2026-01-12", "cliente": "Beatriz Langa",     "produto": "Teclado",      "cidade": "Maputo", "quantidade":  8, "preco_unitario":  1800, "valor_venda":  14400},
    {"data": "2026-01-15", "cliente": "Pedro Nhantumbo",   "produto": "Tablet",       "cidade": "Boane",  "quantidade":  1, "preco_unitario": 28000, "valor_venda":  28000},
    {"data": "2026-01-18", "cliente": "Fátima Cumbe",      "produto": "Rato",         "cidade": "Boane",  "quantidade": 10, "preco_unitario":   900, "valor_venda":   9000},
    {"data": "2026-01-22", "cliente": "Manuel Chaúque",    "produto": "SSD Externo",  "cidade": "Matola", "quantidade":  2, "preco_unitario":  8500, "valor_venda":  17000},
    {"data": "2026-01-25", "cliente": "Ana Cossa",         "produto": "Laptop",       "cidade": "Matola", "quantidade":  1, "preco_unitario": 45000, "valor_venda":  45000},
    {"data": "2026-01-29", "cliente": "Sofia Guambe",      "produto": "Cadeira Gamer","cidade": "Maputo", "quantidade":  1, "preco_unitario": 18000, "valor_venda":  18000},
    {"data": "2026-02-03", "cliente": "Carlos Machava",    "produto": "Monitor",      "cidade": "Maputo", "quantidade":  4, "preco_unitario": 15000, "valor_venda":  60000},
    {"data": "2026-02-06", "cliente": "João Sitoe",        "produto": "Headphones",   "cidade": "Matola", "quantidade":  4, "preco_unitario":  3500, "valor_venda":  14000},
    {"data": "2026-02-09", "cliente": "Fátima Cumbe",      "produto": "Teclado",      "cidade": "Boane",  "quantidade": 12, "preco_unitario":  1800, "valor_venda":  21600},
    {"data": "2026-02-12", "cliente": "Rui Tembe",         "produto": "Tablet",       "cidade": "Maputo", "quantidade":  2, "preco_unitario": 28000, "valor_venda":  56000},
    {"data": "2026-02-14", "cliente": "Beatriz Langa",     "produto": "Rato",         "cidade": "Matola", "quantidade": 15, "preco_unitario":   900, "valor_venda":  13500},
    {"data": "2026-02-18", "cliente": "Pedro Nhantumbo",   "produto": "SSD Externo",  "cidade": "Boane",  "quantidade":  3, "preco_unitario":  8500, "valor_venda":  25500},
    {"data": "2026-02-20", "cliente": "Luciana Bila",      "produto": "Impressora",   "cidade": "Maputo", "quantidade":  2, "preco_unitario": 12500, "valor_venda":  25000},
    {"data": "2026-02-25", "cliente": "Manuel Chaúque",    "produto": "Cadeira Gamer","cidade": "Matola", "quantidade":  1, "preco_unitario": 18000, "valor_venda":  18000},
    {"data": "2026-02-27", "cliente": "Ana Cossa",         "produto": "Laptop",       "cidade": "Boane",  "quantidade":  2, "preco_unitario": 45000, "valor_venda":  90000},
    {"data": "2026-03-02", "cliente": "Carlos Machava",    "produto": "Headphones",   "cidade": "Boane",  "quantidade":  6, "preco_unitario":  3500, "valor_venda":  21000},
    {"data": "2026-03-04", "cliente": "João Sitoe",        "produto": "Monitor",      "cidade": "Matola", "quantidade":  5, "preco_unitario": 15000, "valor_venda":  75000},
    {"data": "2026-03-08", "cliente": "Rui Tembe",         "produto": "Tablet",       "cidade": "Matola", "quantidade":  1, "preco_unitario": 28000, "valor_venda":  28000},
    {"data": "2026-03-10", "cliente": "Sofia Guambe",      "produto": "Teclado",      "cidade": "Maputo", "quantidade": 10, "preco_unitario":  1800, "valor_venda":  18000},
    {"data": "2026-03-14", "cliente": "Beatriz Langa",     "produto": "SSD Externo",  "cidade": "Maputo", "quantidade":  4, "preco_unitario":  8500, "valor_venda":  34000},
    {"data": "2026-03-16", "cliente": "Fátima Cumbe",      "produto": "Rato",         "cidade": "Boane",  "quantidade": 20, "preco_unitario":   900, "valor_venda":  18000},
    {"data": "2026-03-20", "cliente": "Pedro Nhantumbo",   "produto": "Cadeira Gamer","cidade": "Boane",  "quantidade":  2, "preco_unitario": 18000, "valor_venda":  36000},
    {"data": "2026-03-22", "cliente": "Luciana Bila",      "produto": "Impressora",   "cidade": "Matola", "quantidade":  3, "preco_unitario": 12500, "valor_venda":  37500},
    {"data": "2026-03-26", "cliente": "Carlos Machava",    "produto": "Webcam",       "cidade": "Maputo", "quantidade":  3, "preco_unitario":  4200, "valor_venda":  12600},
    {"data": "2026-03-29", "cliente": "Ana Cossa",         "produto": "Laptop",       "cidade": "Maputo", "quantidade":  3, "preco_unitario": 45000, "valor_venda": 135000},
    {"data": "2026-04-01", "cliente": "Rui Tembe",         "produto": "Headphones",   "cidade": "Maputo", "quantidade":  9, "preco_unitario":  3500, "valor_venda":  31500},
    {"data": "2026-04-06", "cliente": "João Sitoe",        "produto": "Monitor",      "cidade": "Boane",  "quantidade":  4, "preco_unitario": 15000, "valor_venda":  60000},
    {"data": "2026-04-08", "cliente": "Sofia Guambe",      "produto": "Tablet",       "cidade": "Boane",  "quantidade":  3, "preco_unitario": 28000, "valor_venda":  84000},
    {"data": "2026-04-11", "cliente": "Beatriz Langa",     "produto": "Teclado",      "cidade": "Matola", "quantidade": 15, "preco_unitario":  1800, "valor_venda":  27000},
    {"data": "2026-04-14", "cliente": "Manuel Chaúque",    "produto": "SSD Externo",  "cidade": "Matola", "quantidade":  5, "preco_unitario":  8500, "valor_venda":  42500},
    {"data": "2026-04-17", "cliente": "Fátima Cumbe",      "produto": "Rato",         "cidade": "Maputo", "quantidade": 18, "preco_unitario":   900, "valor_venda":  16200},
    {"data": "2026-04-20", "cliente": "Carlos Machava",    "produto": "Cadeira Gamer","cidade": "Maputo", "quantidade":  2, "preco_unitario": 18000, "valor_venda":  36000},
    {"data": "2026-04-23", "cliente": "Luciana Bila",      "produto": "Impressora",   "cidade": "Boane",  "quantidade":  2, "preco_unitario": 12500, "valor_venda":  25000},
    {"data": "2026-04-26", "cliente": "Pedro Nhantumbo",   "produto": "Webcam",       "cidade": "Boane",  "quantidade":  4, "preco_unitario":  4200, "valor_venda":  16800},
    {"data": "2026-04-28", "cliente": "Ana Cossa",         "produto": "Laptop",       "cidade": "Matola", "quantidade":  2, "preco_unitario": 45000, "valor_venda":  90000},
    {"data": "2026-05-02", "cliente": "Rui Tembe",         "produto": "Headphones",   "cidade": "Maputo", "quantidade":  5, "preco_unitario":  3500, "valor_venda":  17500},
    {"data": "2026-05-04", "cliente": "João Sitoe",        "produto": "Monitor",      "cidade": "Boane",  "quantidade":  4, "preco_unitario": 15000, "valor_venda":  60000},
    {"data": "2026-05-07", "cliente": "Manuel Chaúque",    "produto": "Impressora",   "cidade": "Matola", "quantidade":  4, "preco_unitario": 12500, "valor_venda":  50000},
    {"data": "2026-05-10", "cliente": "Sofia Guambe",      "produto": "Webcam",       "cidade": "Boane",  "quantidade":  3, "preco_unitario":  4200, "valor_venda":  12600},
    {"data": "2026-05-12", "cliente": "Beatriz Langa",     "produto": "Rato",         "cidade": "Matola", "quantidade": 22, "preco_unitario":   900, "valor_venda":  19800},
    {"data": "2026-05-14", "cliente": "Carlos Machava",    "produto": "Monitor",      "cidade": "Maputo", "quantidade":  6, "preco_unitario": 15000, "valor_venda":  90000},
    {"data": "2026-05-16", "cliente": "Luciana Bila",      "produto": "Impressora",   "cidade": "Boane",  "quantidade":  3, "preco_unitario": 12500, "valor_venda":  37500},
    {"data": "2026-05-18", "cliente": "João Sitoe",        "produto": "Headphones",   "cidade": "Matola", "quantidade":  8, "preco_unitario":  3500, "valor_venda":  28000},
    {"data": "2026-05-22", "cliente": "Rui Tembe",         "produto": "Tablet",       "cidade": "Maputo", "quantidade":  2, "preco_unitario": 28000, "valor_venda":  56000},
    {"data": "2026-05-24", "cliente": "Ana Cossa",         "produto": "Laptop",       "cidade": "Maputo", "quantidade":  2, "preco_unitario": 45000, "valor_venda":  90000},
    {"data": "2026-05-26", "cliente": "Fátima Cumbe",      "produto": "Teclado",      "cidade": "Boane",  "quantidade": 20, "preco_unitario":  1800, "valor_venda":  36000},
    {"data": "2026-05-30", "cliente": "Pedro Nhantumbo",   "produto": "Webcam",       "cidade": "Matola", "quantidade":  5, "preco_unitario":  4200, "valor_venda":  21000},
    {"data": "2026-06-02", "cliente": "Beatriz Langa",     "produto": "Teclado",      "cidade": "Matola", "quantidade": 14, "preco_unitario":  1800, "valor_venda":  25200},
    {"data": "2026-06-03", "cliente": "Ana Cossa",         "produto": "Laptop",       "cidade": "Boane",  "quantidade":  1, "preco_unitario": 45000, "valor_venda":  45000},
    {"data": "2026-06-06", "cliente": "Sofia Guambe",      "produto": "Tablet",       "cidade": "Matola", "quantidade":  3, "preco_unitario": 28000, "valor_venda":  84000},
    {"data": "2026-06-08", "cliente": "Fátima Cumbe",      "produto": "Rato",         "cidade": "Boane",  "quantidade": 28, "preco_unitario":   900, "valor_venda":  25200},
    {"data": "2026-06-10", "cliente": "Carlos Machava",    "produto": "Rato",         "cidade": "Maputo", "quantidade": 25, "preco_unitario":   900, "valor_venda":  22500},
    {"data": "2026-06-13", "cliente": "Rui Tembe",         "produto": "Headphones",   "cidade": "Boane",  "quantidade": 10, "preco_unitario":  3500, "valor_venda":  35000},
    {"data": "2026-06-15", "cliente": "João Sitoe",        "produto": "Monitor",      "cidade": "Maputo", "quantidade":  5, "preco_unitario": 15000, "valor_venda":  75000},
    {"data": "2026-06-17", "cliente": "Manuel Chaúque",    "produto": "SSD Externo",  "cidade": "Maputo", "quantidade":  4, "preco_unitario":  8500, "valor_venda":  34000},
    {"data": "2026-06-21", "cliente": "Pedro Nhantumbo",   "produto": "Webcam",       "cidade": "Boane",  "quantidade":  6, "preco_unitario":  4200, "valor_venda":  25200},
    {"data": "2026-06-22", "cliente": "Luciana Bila",      "produto": "Impressora",   "cidade": "Matola", "quantidade":  2, "preco_unitario": 12500, "valor_venda":  25000},
    {"data": "2026-06-24", "cliente": "João Sitoe",        "produto": "Monitor",      "cidade": "Matola", "quantidade":  3, "preco_unitario": 15000, "valor_venda":  45000},
    {"data": "2026-06-28", "cliente": "Sofia Guambe",      "produto": "Tablet",       "cidade": "Boane",  "quantidade":  2, "preco_unitario": 28000, "valor_venda":  56000},
    {"data": "2026-07-01", "cliente": "Ana Cossa",         "produto": "Laptop",       "cidade": "Boane",  "quantidade":  1, "preco_unitario": 45000, "valor_venda":  45000},
    {"data": "2026-07-02", "cliente": "Manuel Chaúque",    "produto": "SSD Externo",  "cidade": "Matola", "quantidade":  5, "preco_unitario":  8500, "valor_venda":  42500},
    {"data": "2026-07-05", "cliente": "Carlos Machava",    "produto": "Teclado",      "cidade": "Maputo", "quantidade": 18, "preco_unitario":  1800, "valor_venda":  32400},
    {"data": "2026-07-08", "cliente": "Fátima Cumbe",      "produto": "Teclado",      "cidade": "Boane",  "quantidade": 16, "preco_unitario":  1800, "valor_venda":  28800},
    {"data": "2026-07-09", "cliente": "Rui Tembe",         "produto": "Headphones",   "cidade": "Maputo", "quantidade": 12, "preco_unitario":  3500, "valor_venda":  42000},
    {"data": "2026-07-13", "cliente": "Ana Cossa",         "produto": "Laptop",       "cidade": "Matola", "quantidade":  2, "preco_unitario": 45000, "valor_venda":  90000},
    {"data": "2026-07-15", "cliente": "Beatriz Langa",     "produto": "Rato",         "cidade": "Maputo", "quantidade": 32, "preco_unitario":   900, "valor_venda":  28800},
    {"data": "2026-07-17", "cliente": "Luciana Bila",      "produto": "Impressora",   "cidade": "Maputo", "quantidade":  3, "preco_unitario": 12500, "valor_venda":  37500},
    {"data": "2026-07-21", "cliente": "Manuel Chaúque",    "produto": "SSD Externo",  "cidade": "Boane",  "quantidade":  6, "preco_unitario":  8500, "valor_venda":  51000},
    {"data": "2026-07-22", "cliente": "João Sitoe",        "produto": "Monitor",      "cidade": "Matola", "quantidade":  4, "preco_unitario": 15000, "valor_venda":  60000},
    {"data": "2026-07-25", "cliente": "Beatriz Langa",     "produto": "Rato",         "cidade": "Matola", "quantidade": 30, "preco_unitario":   900, "valor_venda":  27000},
    {"data": "2026-07-28", "cliente": "Luciana Bila",      "produto": "Impressora",   "cidade": "Boane",  "quantidade":  3, "preco_unitario": 12500, "valor_venda":  37500},
    {"data": "2026-07-29", "cliente": "Sofia Guambe",      "produto": "Webcam",       "cidade": "Maputo", "quantidade":  4, "preco_unitario":  4200, "valor_venda":  16800},
    {"data": "2026-08-02", "cliente": "Rui Tembe",         "produto": "Tablet",       "cidade": "Maputo", "quantidade":  4, "preco_unitario": 28000, "valor_venda": 112000},
    {"data": "2026-08-05", "cliente": "João Sitoe",        "produto": "Monitor",      "cidade": "Boane",  "quantidade":  5, "preco_unitario": 15000, "valor_venda":  75000},
    {"data": "2026-08-09", "cliente": "Carlos Machava",    "produto": "Headphones",   "cidade": "Matola", "quantidade":  7, "preco_unitario":  3500, "valor_venda":  24500},
    {"data": "2026-08-13", "cliente": "Sofia Guambe",      "produto": "Cadeira Gamer","cidade": "Maputo", "quantidade":  2, "preco_unitario": 18000, "valor_venda":  36000},
    {"data": "2026-08-17", "cliente": "Ana Cossa",         "produto": "Laptop",       "cidade": "Boane",  "quantidade":  3, "preco_unitario": 45000, "valor_venda": 135000},
    {"data": "2026-08-21", "cliente": "Manuel Chaúque",    "produto": "SSD Externo",  "cidade": "Matola", "quantidade":  8, "preco_unitario":  8500, "valor_venda":  68000},
    {"data": "2026-08-25", "cliente": "Pedro Nhantumbo",   "produto": "Cadeira Gamer","cidade": "Matola", "quantidade":  1, "preco_unitario": 18000, "valor_venda":  18000},
    {"data": "2026-08-28", "cliente": "Fátima Cumbe",      "produto": "Teclado",      "cidade": "Boane",  "quantidade": 22, "preco_unitario":  1800, "valor_venda":  39600},
    {"data": "2026-09-01", "cliente": "Beatriz Langa",     "produto": "Rato",         "cidade": "Maputo", "quantidade": 35, "preco_unitario":   900, "valor_venda":  31500},
    {"data": "2026-09-05", "cliente": "Pedro Nhantumbo",   "produto": "Webcam",       "cidade": "Matola", "quantidade":  7, "preco_unitario":  4200, "valor_venda":  29400},
    {"data": "2026-09-09", "cliente": "Carlos Machava",    "produto": "Cadeira Gamer","cidade": "Boane",  "quantidade":  2, "preco_unitario": 18000, "valor_venda":  36000},
    {"data": "2026-09-12", "cliente": "Rui Tembe",         "produto": "Monitor",      "cidade": "Maputo", "quantidade":  7, "preco_unitario": 15000, "valor_venda": 105000},
    {"data": "2026-09-16", "cliente": "Sofia Guambe",      "produto": "Tablet",       "cidade": "Matola", "quantidade":  3, "preco_unitario": 28000, "valor_venda":  84000},
    {"data": "2026-09-20", "cliente": "Luciana Bila",      "produto": "Impressora",   "cidade": "Boane",  "quantidade":  4, "preco_unitario": 12500, "valor_venda":  50000},
    {"data": "2026-09-24", "cliente": "Manuel Chaúque",    "produto": "SSD Externo",  "cidade": "Maputo", "quantidade": 10, "preco_unitario":  8500, "valor_venda":  85000},
    {"data": "2026-09-28", "cliente": "João Sitoe",        "produto": "Headphones",   "cidade": "Boane",  "quantidade": 14, "preco_unitario":  3500, "valor_venda":  49000},
    {"data": "2026-10-02", "cliente": "Ana Cossa",         "produto": "Laptop",       "cidade": "Maputo", "quantidade":  4, "preco_unitario": 45000, "valor_venda": 180000},
    {"data": "2026-10-05", "cliente": "Carlos Machava",    "produto": "Cadeira Gamer","cidade": "Maputo", "quantidade":  3, "preco_unitario": 18000, "valor_venda":  54000},
    {"data": "2026-10-08", "cliente": "Fátima Cumbe",      "produto": "Rato",         "cidade": "Boane",  "quantidade": 40, "preco_unitario":   900, "valor_venda":  36000},
    {"data": "2026-10-11", "cliente": "Beatriz Langa",     "produto": "Teclado",      "cidade": "Matola", "quantidade": 25, "preco_unitario":  1800, "valor_venda":  45000},
    {"data": "2026-10-14", "cliente": "Rui Tembe",         "produto": "Webcam",       "cidade": "Maputo", "quantidade":  9, "preco_unitario":  4200, "valor_venda":  37800},
    {"data": "2026-10-17", "cliente": "João Sitoe",        "produto": "Monitor",      "cidade": "Boane",  "quantidade":  6, "preco_unitario": 15000, "valor_venda":  90000},
    {"data": "2026-10-20", "cliente": "Manuel Chaúque",    "produto": "SSD Externo",  "cidade": "Matola", "quantidade":  7, "preco_unitario":  8500, "valor_venda":  59500},
    {"data": "2026-10-23", "cliente": "Sofia Guambe",      "produto": "Tablet",       "cidade": "Boane",  "quantidade":  5, "preco_unitario": 28000, "valor_venda": 140000},
    {"data": "2026-10-26", "cliente": "Pedro Nhantumbo",   "produto": "Cadeira Gamer","cidade": "Matola", "quantidade":  2, "preco_unitario": 18000, "valor_venda":  36000},
]

# ─────────────────────────────────────────────
#  FUNÇÕES DE ANÁLISE
# ─────────────────────────────────────────────

def total_vendas():
    """Retorna o número total de registos de vendas."""
    return len(vendas)


def receita_total():
    """Retorna a receita total acumulada de todas as vendas."""
    return sum(v["valor_venda"] for v in vendas)


def vendas_por_produto():
    """Retorna um dicionário com receita total agrupada por produto."""
    resultado = {}
    for v in vendas:
        produto = v["produto"]
        resultado[produto] = resultado.get(produto, 0) + v["valor_venda"]
    return dict(sorted(resultado.items(), key=lambda x: x[1], reverse=True))


def vendas_por_cidade():
    """Retorna um dicionário com receita total agrupada por cidade."""
    resultado = {}
    for v in vendas:
        cidade = v["cidade"]
        resultado[cidade] = resultado.get(cidade, 0) + v["valor_venda"]
    return dict(sorted(resultado.items(), key=lambda x: x[1], reverse=True))


def vendas_por_mes():
    """Retorna um dicionário com receita total agrupada por mês."""
    resultado = {}
    meses = {
        "01": "Janeiro", "02": "Fevereiro", "03": "Março",    "04": "Abril",
        "05": "Maio",    "06": "Junho",     "07": "Julho",    "08": "Agosto",
        "09": "Setembro","10": "Outubro",   "11": "Novembro", "12": "Dezembro"
    }
    for v in vendas:
        mes_num = v["data"][5:7]
        mes = meses[mes_num]
        resultado[mes] = resultado.get(mes, 0) + v["valor_venda"]
    return resultado


def produto_mais_vendido():
    """Retorna o produto com maior receita total."""
    por_produto = vendas_por_produto()
    produto = max(por_produto, key=por_produto.get)
    return produto, por_produto[produto]


def cidade_mais_vendas():
    """Retorna a cidade com maior receita total."""
    por_cidade = vendas_por_cidade()
    cidade = max(por_cidade, key=por_cidade.get)
    return cidade, por_cidade[cidade]


def filtrar_por_produto(nome_produto):
    """Filtra e retorna todas as vendas de um produto específico."""
    return [v for v in vendas if v["produto"].lower() == nome_produto.lower()]


def filtrar_por_cidade(nome_cidade):
    """Filtra e retorna todas as vendas de uma cidade específica."""
    return [v for v in vendas if v["cidade"].lower() == nome_cidade.lower()]


def filtrar_por_cliente(nome_cliente):
    """Filtra e retorna todas as vendas de um cliente específico."""
    return [v for v in vendas if v["cliente"].lower() == nome_cliente.lower()]


def ranking_clientes_por_valor():
    """Retorna ranking de clientes ordenado por valor total gasto (desc)."""
    resultado = {}
    for v in vendas:
        cliente = v["cliente"]
        resultado[cliente] = resultado.get(cliente, 0) + v["valor_venda"]
    return dict(sorted(resultado.items(), key=lambda x: x[1], reverse=True))


def ranking_clientes_por_quantidade():
    """Retorna ranking de clientes ordenado por quantidade total comprada (desc)."""
    resultado = {}
    for v in vendas:
        cliente = v["cliente"]
        resultado[cliente] = resultado.get(cliente, 0) + v["quantidade"]
    return dict(sorted(resultado.items(), key=lambda x: x[1], reverse=True))


def perfil_cliente(nome_cliente):
    """Retorna um resumo completo do perfil de um cliente."""
    compras = filtrar_por_cliente(nome_cliente)
    if not compras:
        return None
    total_gasto   = sum(v["valor_venda"]  for v in compras)
    total_itens   = sum(v["quantidade"]   for v in compras)
    num_compras   = len(compras)
    ticket_medio  = total_gasto / num_compras
    produtos      = list({v["produto"] for v in compras})
    return {
        "cliente":       nome_cliente,
        "num_compras":   num_compras,
        "total_itens":   total_itens,
        "total_gasto":   total_gasto,
        "ticket_medio":  ticket_medio,
        "produtos":      produtos,
    }


def exportar_csv(caminho=None):
    """Exporta os dados de vendas para um ficheiro CSV."""
    if caminho is None:
        caminho = os.path.join(os.path.dirname(__file__), "vendas_exportado.csv")
    campos = ["data", "produto", "cidade", "quantidade", "preco_unitario", "valor_venda"]
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(vendas)
    print(f"✅ Exportado com sucesso para: {caminho}")


# ─────────────────────────────────────────────
#  RELATÓRIO GERAL
# ─────────────────────────────────────────────

def imprimir_relatorio():
    """Imprime um relatório completo de vendas no terminal."""
    separador = "=" * 55

    print(separador)
    print("       📊 RELATÓRIO DE VENDAS — MUV Documents")
    print(separador)

    print(f"\n📦 Total de registos de vendas : {total_vendas()}")
    print(f"💰 Receita total               : {receita_total():,.0f} MT")

    # Produto mais vendido
    prod, val = produto_mais_vendido()
    print(f"🏆 Produto top                 : {prod} ({val:,.0f} MT)")

    # Cidade com mais vendas
    cid, val_cid = cidade_mais_vendas()
    print(f"📍 Cidade top                  : {cid} ({val_cid:,.0f} MT)")

    # Por produto
    print(f"\n{separador}")
    print("  RECEITA POR PRODUTO")
    print(separador)
    for produto, total in vendas_por_produto().items():
        barra = "█" * (total // 20000)
        print(f"  {produto:<15} {total:>10,.0f} MT  {barra}")

    # Por cidade
    print(f"\n{separador}")
    print("  RECEITA POR CIDADE")
    print(separador)
    for cidade, total in vendas_por_cidade().items():
        barra = "█" * (total // 30000)
        print(f"  {cidade:<15} {total:>10,.0f} MT  {barra}")

    # Por mês
    print(f"\n{separador}")
    print("  RECEITA POR MÊS")
    print(separador)
    for mes, total in vendas_por_mes().items():
        barra = "█" * (total // 20000)
        print(f"  {mes:<12} {total:>10,.0f} MT  {barra}")

    # Ranking de clientes por valor
    print(f"\n{separador}")
    print("  🏅 TOP CLIENTES — POR VALOR GASTO")
    print(separador)
    for i, (cliente, total) in enumerate(ranking_clientes_por_valor().items(), 1):
        medalha = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f" {i}.")
        print(f"  {medalha} {cliente:<20} {total:>10,.0f} MT")

    # Ranking de clientes por quantidade
    print(f"\n{separador}")
    print("  🏅 TOP CLIENTES — POR UNIDADES COMPRADAS")
    print(separador)
    for i, (cliente, qtd) in enumerate(ranking_clientes_por_quantidade().items(), 1):
        medalha = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f" {i}.")
        print(f"  {medalha} {cliente:<20} {qtd:>6} unidades")

    print(f"\n{separador}\n")


# ─────────────────────────────────────────────
#  PONTO DE ENTRADA
# ─────────────────────────────────────────────

if __name__ == "__main__":
    imprimir_relatorio()

    # Perfil detalhado do cliente top
    print("👤 PERFIL DO CLIENTE TOP:")
    top_cliente = list(ranking_clientes_por_valor().keys())[0]
    perfil = perfil_cliente(top_cliente)
    print(f"   Nome         : {perfil['cliente']}")
    print(f"   Nº compras   : {perfil['num_compras']}")
    print(f"   Total itens  : {perfil['total_itens']} unidades")
    print(f"   Total gasto  : {perfil['total_gasto']:,.0f} MT")
    print(f"   Ticket médio : {perfil['ticket_medio']:,.0f} MT")
    print(f"   Produtos      : {', '.join(perfil['produtos'])}")

    # Descomente a linha abaixo para exportar CSV:
    # exportar_csv()
