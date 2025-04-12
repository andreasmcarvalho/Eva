import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..database.firebase_service import db

def testar_conexao():
    try:
        usuarios = db.collection("usuarios").stream()
        print("Conexão bem-sucedida com o Firebase!")
        for user in usuarios:
            print(f"Usuário encontrado: {user.id} -> {user.to_dict()}")
    except Exception as e:
        print(f"Erro ao conectar com o Firebase: {e}")

if __name__ == "__main__":
    testar_conexao()
