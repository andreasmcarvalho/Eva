from .firebase_service import db

def cadastrar_usuario(user_id: str, nome: str):
    db.collection("usuarios").document(str(user_id)).set({
        "nome": nome
    })

def obter_usuario(user_id: str):
    doc = db.collection("usuarios").document(str(user_id)).get()
    if doc.exists:
        return doc.to_dict()
    return None
