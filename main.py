# Dicionários para armazenar pedidos e avaliações
orders = {
    'paulo': ['Pizza', 'Coca', 'Hamburguer'],
    'gustavo': ['Sushi', 'Lasanha', 'Sorvete'],
    'carla': ['Macarronada', 'Suco', 'Salada']
}

reviews = {}

def orders_history(client_name): 
    client_name = client_name.lower()

    if client_name in orders:
        print(f'\nÚltimos pedidos de {client_name.capitalize()}:')
        for orders_num, order in enumerate(orders[client_name], 1):
            print(f'[{orders_num}] {order}')
    else:
        print('Cliente inexistente!')

def restaurant_reviews():
    user_name = input("\nDigite seu nome: ").strip()
    
    if not user_name:
        print('Comentários sobre o restaurante disponíveis apenas com o nome do usuário!')
        return
    
    restaurant_name = input("\nDigite o nome do restaurante: ").strip()
    
    if not restaurant_name:
        print('Comentários disponíveis apenas com o nome do restaurante!')
        return
    
    while True:
        try:
            note = float(input("Digite sua nota de 0 a 5: "))
            if 0 <= note <= 5:
                break
            else:
                print("Por favor, digite uma nota entre 0 e 5!")
        except ValueError:
            print("Entrada inválida! Digite um número.")

    review = input("Deixe um comentário (opcional): ").strip()
    
    if restaurant_name not in reviews:
        reviews[restaurant_name] = []

    reviews[restaurant_name].append({
        "usuario": user_name,
        "nota": note,
        "comentario": review
    })

    print(f"\nObrigado, {user_name}! Você avaliou o restaurante {restaurant_name} com nota {note:.1f}.")
    if note >= 4:
        print("Que bom que você gostou!")
    elif note <= 2:
        print("😢 Sentimos muito pela experiência ruim.")

def show_reviews():
    if not reviews:
        print("\nSem comentários registrados!")
        return
    
    print("\nComentários registrados:")
    for restaurant, comments in reviews.items():
        print(f"\n📍 Restaurante: {restaurant}")
        for review in comments:
            print(f"Usuário: {review['usuario']} - Nota: {review['nota']:.1f}")  # Usando 'usuario' e 'nota'
            if review["comentario"]:
                print(f"Comentário: {review['comentario']}")  # Usando 'comentario'
            print("-" * 30)


def menu():
    while True:
        print("\n=== 🍽️ SISTEMA DE RESTAURANTE ===")
        print("[1] Ver histórico de pedidos")
        print("[2] Avaliar restaurante")
        print("[3] Ver avaliações registradas")
        print("[4] Sair")
        
        options = input("\nEscolha uma opção: ").strip()
        
        if options == "1":
            client_name = input('\nDigite o nome do cliente: ').strip()
            orders_history(client_name)
        elif options == "2":
            restaurant_reviews()
        elif options == "3":
            show_reviews()
        elif options == "4":
            print("\nObrigado por usar nosso sistema! Até mais! 👋")
            break
        else:
            print("\nOpção inválida! Por favor, escolha 1, 2, 3 ou 4.")

if __name__ == "__main__":
    menu()
