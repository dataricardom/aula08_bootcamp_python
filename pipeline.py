from etl import extrair_dados, salvar_csv, calcular_kpi_de_total_de_vendas
from datetime import datetime
import os
path = 'data'
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
dado_consolidada = extrair_dados(path)
dado_transformado = calcular_kpi_de_total_de_vendas(dado_consolidada)
salvarcsv = salvar_csv(dado_transformado, f"data/vendas_consolidadas_{timestamp}.csv")