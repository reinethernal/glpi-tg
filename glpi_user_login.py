import requests
from config import GLPI_API_URL

def authenticate_user(username: str, password: str) -> str:
    """
    Authenticates the user with the GLPI API using their username and password.
    Returns the user's session token.
    """
    endpoint = f"{GLPI_API_URL}/initSession"
    data = {"login_name": username, "login_password": password}
    response = requests.post(endpoint, json=data)
    if response.status_code == 200:
        session_token = response.json()["session_token"]
        return session_token
    else:
        raise Exception("Failed to authenticate user with GLPI API.")