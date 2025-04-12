from .firebase_service import db

def salvar_historico_email(user_id: str, email_data: dict):
    db.collection("historico_emails").add({
        "user_id": user_id,
        **email_data
    })

def obter_historico_emails(user_id: str):
    docs = db.collection("historico_emails").where("user_id", "==", user_id).stream()
    return [doc.to_dict() for doc in docs]
