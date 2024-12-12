from dotenv import load_dotenv

from settings import Settings

load_dotenv()

settings = Settings()
settings.load_service_account('service-account.json')
print(settings.firebase_credentials)