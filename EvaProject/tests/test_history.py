import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.history import salvar_historico_email, obter_historico_emails


def testar_historico():
    user_id = "123456789"
    email_data = {
        "destinatario": "João",
        "mensagem": "Compareça à reunião às 14h.",
        "acao": "enviar e-mail"
    }

    salvar_historico_email(user_id, email_data)
    print("E-mail salvo no histórico.")

    historico = obter_historico_emails(user_id)
    print("Histórico do usuário:")
    for item in historico:
        print(item)

if __name__ == "__main__":
    testar_historico()
