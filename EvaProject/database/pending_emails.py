from .firebase_service import db

def registrar_email_pendente(user_id: str, email_data: dict):
    db.collection("emails_pendentes").document(str(user_id)).set(email_data)

def obter_email_pendente(user_id: str):
    doc = db.collection("emails_pendentes").document(str(user_id)).get()
    if doc.exists:
        return doc.to_dict()
    return None

def excluir_email_pendente(user_id: str):
    db.collection("emails_pendentes").document(str(user_id)).delete()
