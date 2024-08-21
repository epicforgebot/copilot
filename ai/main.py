import os
from fastapi import FastAPI, HTTPException, Depends
import requests
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

app = FastAPI()

SAP_AI_CORE_URL = os.getenv('SAP_AI_CORE_URL')
XSUAA_URL = os.getenv('XSUAA_URL')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

@app.get('/')
def read_root():
    """
    Root endpoint for health check.
    Returns a JSON response with a greeting message.
    """
    return {'Hello': 'World'}

@app.post('/ai/predict')
def predict(input_data: dict, token: str = Depends(oauth2_scheme)):
    """
    Endpoint to send a POST request to the SAP AI Core service for prediction.

    Args:
        input_data (dict): The input data for prediction.
        token (str): The authorization token.

    Returns:
        dict: The prediction result.

    Raises:
        HTTPException: If the response status code is not 200.
    """
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(f'{SAP_AI_CORE_URL}/predict', =input_data, headers=headers)
    if response.status_code == 200:
        return response.()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)
