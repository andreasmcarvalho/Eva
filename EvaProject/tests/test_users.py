import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.users import cadastrar_usuario, obter_usuario

def testar_usuario():
    user_id = "123456789"
    nome = "Andreas"

    cadastrar_usuario(user_id, nome)
    resultado = obter_usuario(user_id)

    if resultado:
        print(f"Usuário encontrado: {resultado}")
    else:
        print("Usuário não encontrado.")

if __name__ == "__main__":
    testar_usuario()
