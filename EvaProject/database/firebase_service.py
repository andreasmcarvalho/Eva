import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Inicializa o Firebase apenas uma vez
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Exporta cliente do Firestore
db = firestore.client()
