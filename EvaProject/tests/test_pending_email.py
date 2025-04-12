import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.pending_emails import registrar_email_pendente, obter_email_pendente, excluir_email_pendente

def testar_email():

    user_id = "123456789"
    email_data = {
        "destinatario": "gabrielle@email.com",
        "mensagem": "Compareça à faculdade às 10h, por favor.",
        "acao": "enviar e-mail"
    }

    registrar_email_pendente(user_id, email_data)
    print("E-mail pendente registrado.")

    recuperado = obter_email_pendente(user_id)
    print(f"E-mail recuperado: {recuperado}")

    excluir_email_pendente(user_id)
    print("E-mail pendente excluído.")

if __name__ == "__main__":
    testar_email()
