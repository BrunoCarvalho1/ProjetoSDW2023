# Etapa de Extração (dados de exemplo)
source_data = [
    {'id': 1, 'nome': 'Alice', 'idade': 30},
    {'id': 2, 'nome': 'Bob', 'idade': 25},
    {'id': 3, 'nome': 'Carol', 'idade': 35},
]

# Etapa de Transformação (Neste exemplo, apenas uma transformação simples)
def transform_data(data):
    for item in data:
        item['idade'] *= 2  # Multiplica a idade por 2

# Etapa de Carga (usando uma lista como destino)
destination_data = []

def load_data(data):
    destination_data.extend(data)

if __name__ == "__main__":
    # Executando o pipeline ETL
    transform_data(source_data)
    load_data(source_data)
    
    # Exibindo os dados transformados
    print("Dados transformados:")
    for item in destination_data:
        print(item)

