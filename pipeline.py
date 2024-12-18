from etl import extrair_dados, salvar_csv
from datetime import datetime
path = 'data'
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
data_consolidada = extrair_dados(path)
salvarcsv = salvar_csv(data_consolidada, f"data/vendas_consolidadas_{timestamp}.csv")