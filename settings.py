from pathlib import Path
import json
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Google
    g_project_id: str = ''
    g_client_email: str = ''
    g_private_key_id: str = ''
    g_private_key: str = ''
    g_client_id: str = ''
    g_auth_uri: str = 'https://accounts.google.com/o/oauth2/auth'
    g_token_uri: str = 'https://oauth2.googleapis.com/token'
    g_auth_provider_x509_cert_url: str = 'https://www.googleapis.com/oauth2/v1/certs'
    g_client_x509_cert_url: str = ''

    # OpenAi
    openai_org_id: str = ''
    openai_project_id: str = ''
    openai_api_key: str = ''

    # Firebase Creds
    @property
    def firebase_credentials(self):
        return {
            'type': 'service_account',
            'project_id': self.g_project_id,
            'private_key_id': self.g_private_key_id,
            'private_key': self.g_private_key.replace('\\n', '\n'),
            'client_email': self.g_client_email,
            'client_id': self.g_client_id,
            'auth_uri': self.g_auth_uri,
            'token_uri': self.g_token_uri,
            'auth_provider_x509_cert_url': self.g_auth_provider_x509_cert_url,
            'client_x509_cert_url': self.g_client_x509_cert_url,
        }

    def load_service_account(self, file_path: str):
        service_account_path = Path(file_path)
        if service_account_path.is_file():
            with service_account_path.open() as f:
                data = json.load(f)
                self.g_project_id = data.get('project_id', '')
                self.g_client_email = data.get('client_email', '')
                self.g_private_key_id = data.get('private_key_id', '')
                self.g_private_key = data.get('private_key', '')
                self.g_client_id = data.get('client_id', '')
                self.g_auth_uri = data.get('auth_uri', 'https://accounts.google.com/o/oauth2/auth')
                self.g_token_uri = data.get('token_uri', 'https://oauth2.googleapis.com/token')
                self.g_auth_provider_x509_cert_url = data.get('auth_provider_x509_cert_url',
                                                              'https://www.googleapis.com/oauth2/v1/certs')
                self.g_client_x509_cert_url = data.get('client_x509_cert_url', '')

    model_config = SettingsConfigDict(env_file='.env', extra='allow')


# Usage
settings = Settings()
settings.load_service_account('service-account.json')
