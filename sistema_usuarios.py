import json # Módulo para manipulação de ficheiros JSON
import os # Módulo para verificar a existência de ficheiros

# Ficheiro onde os dados serão guardados no computador
ARQUIVO_BANCO = "usuarios.json" # Arquivo JSON para armazenar os dados dos utilizadores

def carregar_dados(): # Arquivo de dados
    """Lê os dados guardados no ficheiro JSON se ele existir."""
    if os.path.exists(ARQUIVO_BANCO): # Verifica se o ficheiro existe
        with open(ARQUIVO_BANCO, "r", encoding="utf-8") as f: # Abre o ficheiro para leitura
            return json.load(f) #
    return [] # Retorna uma lista vazia se o ficheiro não existir

def salvar_dados(lista_usuarios):  # Arquivo de dados
    """Escreve a lista atualizada de utilizadores no ficheiro JSON."""
    with open(ARQUIVO_BANCO, "w", encoding="utf-8") as f: # Abre o ficheiro para escrita
        json.dump(lista_usuarios, f, indent=4, ensure_ascii=False) # Escreve os dados no ficheiro

def cadastrar_usuario(lista_usuarios): # Arquivo de dados
    """Coleta dados e adiciona um novo cliente à lista."""
    print("\n--- NOVO CADASTRO ---") # Exibe o título do cadastro
    nome = input("Nome completo: ").strip() # Coleta o nome completo
    email = input("E-mail: ").strip().lower() # Coleta o e-mail e converte para minúsculas
    tipo_conta = input("Tipo (Cliente / Restaurante): ").strip().capitalize() # Coleta o tipo de conta

    usuario = {     # Dados do novo utilizador
        "id": len(lista_usuarios) + 1, # Atribui um ID único
        "nome": nome, # Atribui o nome 
        "email": email, # Atribui o e-mail
        "tipo": tipo_conta # Atribui o tipo de conta
    }
    
    lista_usuarios.append(usuario)
    salvar_dados(lista_usuarios)
    print(f"✅ Utilizador '{nome}' cadastrado com sucesso!")

def listar_usuarios(lista_usuarios):
    """Exibe todos os utilizadores guardados."""
    print("\n--- LISTA DE UTILIZADORES CADASTRADOS ---")
    if not lista_usuarios:
        print("Nenhum utilizador cadastrado até ao momento.")
        return

    for u in lista_usuarios:
        print(f"ID: {u['id']} | Nome: {u['nome']} | E-mail: {u['email']} | Tipo: {u['tipo']}")

# --- LOOP PRINCIPAL DO SISTEMA ---
def main():
    usuarios = carregar_dados()
    
    while True:
        print("\n=== GERENCIADOR DE CADASTROS ===")
        print("1 - Cadastrar novo utilizador")
        print("2 - Listar utilizadores cadastrados")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            listar_usuarios(usuarios)
        elif opcao == "3":
            print("A encerrar o sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()