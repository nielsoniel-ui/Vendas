# 📊 Sistema de Gestão & Análise de Vendas (MUV Documents)

Dashboard interativo, análise de rentabilidade e processamento de dados de vendas de produtos informáticos e periféricos em Moçambique (Maputo, Matola e Boane).

## 🚀 Funcionalidades

- **Dashboard Interativo em HTML/JS (`index.html`)**:
  - Gráficos interativos com **Chart.js** com suporte a **filtro cruzado** (clicar nas barras ou fatias filtra todo o painel).
  - Análise de rentabilidade: **Receita Bruta vs Lucro Líquido Estimado** por produto.
  - Alternador de métricas dinâmico (Receita / Lucro / Quantidade) e exportação de gráficos em **PNG**.
  - Rankings de clientes por valor gasto e por volume de unidades.
  - Registo de novas vendas através de modal moderno com cálculo em tempo real.
  - Exportação direta da base de dados para ficheiro **CSV**.
  - Pesquisa instantânea e filtros por cidade, produto e cliente.

- **Módulo de Análise em Python (`vendas.py`)**:
  - Relatório completo via terminal com rankings, totais e gráficos em texto (ASCII).
  - Funções de consulta e agregações (`total_vendas`, `receita_total`, `perfil_cliente`, etc.).

- **Servidor Web & API Nativa (`servidor.py`)**:
  - Servidor HTTP leve em Python nativo (**zero dependências externas / pip**).
  - Endpoints REST para consulta (`/api/vendas`, `/api/metricas`) e persistência (`POST /api/vendas`) direto no CSV.

- **Base de Dados (`vendas.csv`)**:
  - Registo de 100 transações cobrindo 10 produtos diferentes ao longo de 2026.

## 📦 Como Usar

### 1. Visualizar o Dashboard no Navegador:
Basta abrir diretamente o ficheiro `index.html` em qualquer navegador web.

### 2. Iniciar o Servidor Web e API (Opcional):
```bash
python servidor.py
```
Acesse no navegador: `http://localhost:8000`

### 3. Executar o Relatório Python no Terminal:
```bash
python vendas.py
```
