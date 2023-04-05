import requests
from config import GLPI_API_URL, GLPI_API_APP_TOKEN

def authenticate_operator(api_key: str) -> str:
    """
    Authenticates the operator with the GLPI API using their API key.
    Returns the operator's session token.
    """
    endpoint = f"{GLPI_API_URL}/initSession"
    headers = {"App-Token": GLPI_API_APP_TOKEN, "Authorization": f"key {api_key}"}
    response = requests.post(endpoint, headers=headers)
    if response.status_code == 200:
        session_token = response.json()["session_token"]
        return session_token
    else:
        raise Exception("Failed to authenticate operator with GLPI API.")