import os
from fastapi import FastAPI, HTTPException
import requests
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

app = FastAPI()

SAP_AI_CORE_URL = os.getenv('SAP_AI_CORE_URL')
XSUAA_URL = os.getenv('XSUAA_URL')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.post('/ai/predict')
def predict(input_data: dict, token: str = Depends(oauth2_scheme)):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(f'{SAP_AI_CORE_URL}/predict', =input_data, headers=headers)
    if response.status_code == 200:
        return response.()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)
