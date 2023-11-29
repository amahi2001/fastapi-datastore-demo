import os
from google.cloud.datastore import Client as Dsclient
from pydantic_settings import BaseSettings
from google.oauth2 import service_account

class Settings(BaseSettings):
    '''Settings Class'''
    LOCAL: bool = os.environ.get('PRODUCTION', 'false') == 'false'

settings = Settings()

#datastore creds
DS_CREDS = service_account.Credentials.from_service_account_file("./gcp-service-account.json")
DS_CLIENT = Dsclient(credentials=DS_CREDS)
