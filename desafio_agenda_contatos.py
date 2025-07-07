"""
App de agenda de contatos, onde pode-se adicionar, remover, editar, 
favoritar e listar os contatos.
"""

import os

contacts_list = [
    {"name": "João Silva", "phone": "11 - 99999-9999", "email": "joao@example.com", "favorite": False},
    {"name": "Amanda Paes", "phone": "15 - 99841 - 9831", "email": "amanda@example.com", "favorite": True}
]

def list_contacts(contacts_list):
    """
    Lista todos os contatos na agenda.
    """
    if not contacts_list:
        print("Nenhum contato encontrado.")
        return
    print("Lista de Contatos:")
    for index, contact in enumerate(contacts_list, start=1):
        favorite_mark = "⭐" if contact.get("favorite") else ""
        print(f"{index}. Nome: {contact['name']} - Telefone: {contact['phone']} - E-mail: {contact['email']} {favorite_mark}")
    return

def add_contact(contacts_list):
    """
    Adiciona um novo contato à agenda.
    """
    name = input("\nDigite o nome do contato: ")
    phone = input("\nDigite o telefone (DDD - (XX) ou pressione 'Enter' para pular): ").strip()
    while phone and len(phone) != 11:
        print("\nTelefone inválido. Deve conter 11 dígitos.")
        phone = input("\nDigite o telefone (DDD - (XX) ou pressione 'Enter' para pular): ").strip()
        if not phone:
            phone = " "
            break
    email = input("\nDigite o e-mail do contato ou pressione 'Enter' para pular: ").strip()
    is_favorite = bool(input("\nDeseja adicionar este contato como favorito? (Digite 's' ou 'sim' para favoritar" \
    "ou pressione 'Enter' para pular): ").strip().lower())
    contacts_list.append({"name": name, "phone": phone, "email": email, "favorite": is_favorite})
    print(f"Contato {name} adicionado com sucesso!")
    return

def edit_contact(contacts_list):
    """
    Edita as informações de um contato existente na agenda.
    """ 
    if not contacts_list:
        print("Nenhum contato encontrado.")
        return
    list_contacts(contacts_list)
    index = int(input("Digite o número do contato que deseja editar: ")) - 1
    if 0 <= index < len(contacts_list):
        field = input("Qual informação deseja editar? (Digite 'nome', 'telefone', 'email' ou 'favorito'): ").strip().lower()
        match field:
            case "nome":
                new_name = input("Digite o nome: ")
                contacts_list[index]["name"] = new_name
            case "telefone":
                new_phone = input("Digite o telefone (DDD - (XX): ")
                contacts_list[index]["phone"] = new_phone
            case "email":
                new_email = input("Digite o e-mail: ")
                contacts_list[index]["email"] = new_email
    else:
        print("Contato não encontrado.")
    return

def favorite_or_unfavorite_contact(contacts_list):
    """
    Favorita ou desfavorita um contato existente na agenda.
    """
    if not contacts_list:
        print("Nenhum contato encontrado.")
        return
    list_contacts(contacts_list)
    index = int(input("Digite o número do contato que deseja favoritar ou desfavoritar: ")) - 1
    if 0 <= index < len(contacts_list):
        contacts_list[index]["favorite"] = not contacts_list[index]["favorite"]
        action = "favoritado" if contacts_list[index]["favorite"] else "desfavoritado"
        print(f"Contato {contacts_list[index]['name']} {action} com sucesso!")
    else:
        print("Contato não encontrado.")

def remove_contact(contacts_list):
    """
    Remove um contato existente da agenda.
    """
    if not contacts_list:
        print("Nenhum contato encontrado.")
        return
    list_contacts(contacts_list)
    index = int(input("Digite o número do contato que deseja remover: ")) - 1
    if 0 <= index < len(contacts_list):
        if contacts_list[index].get("favorite"):
            confirm = input("Esse contato está como favorito. Deseja realmente removê-lo? (s/n): ").strip().lower()
            if confirm == "s" or confirm == "sim":
                removed_contact = contacts_list.pop(index)
                print(f"Contato {removed_contact['name']} removido com sucesso!")
            else:
                print("Remoção cancelada.")
        else:
            removed_contact = contacts_list.pop(index)
            print(f"Contato {removed_contact['name']} removido com sucesso!")
    else:
        print("Contato não encontrado.")
    return

print("Bem-vindo à Agenda de Contatos!")
while True:
    print("Você pode:")
    print("1. Listar contatos")
    print("2. Adicionar contato")
    print("3. Editar contato")
    print("4. Favoritar/Desfavoritar contato")
    print("5. Remover contato")
    print("6. Sair do programa")

    choice = input("\nDigite o número da opção desejada: ").strip()
    match choice:
        case "1":
            list_contacts(contacts_list)
            input("Pressione Enter para continuar...")

        case "2":
            add_contact(contacts_list)
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        case "3":
            edit_contact(contacts_list)
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        case "4":
            favorite_or_unfavorite_contact(contacts_list)
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        case "5":
            remove_contact(contacts_list)
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        case "6":
            print("\nEncerrando o programa!")
            print("\n")
            exit()
