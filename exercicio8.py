produtos = [
    {"nome": "Camiseta", "preco": 39.90},
    {"nome": "Calça Jeans", "preco": 89.90},
    {"nome": "Tênis", "preco": 120.00}
]
for produto in produtos:
    if produto["preco"] > 50.00:
        
        print(produto["nome"])
