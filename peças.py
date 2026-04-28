import pandas as pd
from faker import Faker
import random

fake = Faker('pt_BR')

def gerar_estoque_scario(total_itens=20000):
    pecas = ["Amortecedor", "Pastilha de Freio", "Filtro de Óleo", "Correia Dentada", "Vela de Ignição", 
             "Bateria 60Ah", "Radiador", "Bomba d'Água", "Disco de Freio", "Pivô de Suspensão", 
             "Junta Homocinética", "Cabo de Vela", "Lâmpada H4", "Sensor de Oxigênio", "Palheta"]
    
    marcas = ["Bosch", "Magneti Marelli", "Cofap", "Nakata", "Monroe", "NGK", "Fram", "Moura"]
    
    modelos = ["Gol G5", "Onix", "HB20", "Corolla", "Civic", "Fiat Uno", "Palio", "Hilux", "Compass"]

    dados = []

    print(f"Gerando {total_itens} peças... Aguarde.")

    for i in range(total_itens):
        peca = random.choice(pecas)
        marca = random.choice(marcas)
        modelo = random.choice(modelos)
        
        # Estrutura: Nome da Peça + Marca + Compatibilidade
        nome_completo = f"{peca} {marca} - {modelo}"
        
        # Gerando SKU único (Ex: SCR-82319-X)
        sku = f"SCR-{random.randint(10000, 99999)}-{random.choice(['A', 'B', 'X'])}"
        
        item = {
            "codigo_sku": sku,
            "nome_peca": nome_completo,
            "fabricante": marca,
            "quantidade_estoque": random.randint(0, 150),
            "localizacao_corredor": f"COR-{random.randint(1, 20)}-{random.choice(['A', 'B', 'C'])}",
            "preco_venda": round(random.uniform(15.0, 1200.0), 2)
        }
        dados.append(item)

    df = pd.DataFrame(dados)
    df.to_csv("estoque_20k_scario.csv", index=False, encoding='utf-8')
    print("Sucesso! Arquivo 'estoque_20k_scario.csv' gerado.")

if __name__ == "__main__":
    gerar_estoque_scario()