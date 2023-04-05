import requests
from config import GLPI_API_URL, GLPI_API_APP_TOKEN

def get_user_requests(user_token):
    """
    Retrieves all requests for the user with the given token from the GLPI API.

    Args:
        user_token (str): The token for the user making the request.

    Returns:
        list: A list of dicts representing the user's requests.
    """
    headers = {"App-Token": GLPI_API_APP_TOKEN, "Session-Token": user_token}
    response = requests.get(f"{GLPI_API_URL}/Ticket", headers=headers)
    response.raise_for_status()

    return response.json()["data"]

def create_user_request(user_token, title, description):
    """
    Creates a new request in the GLPI API on behalf of the user with the given token.

    Args:
        user_token (str): The token for the user making the request.
        title (str): The title of the request.
        description (str): The description of the request.

    Returns:
        dict: A dict representing the newly created request.
    """
    headers = {"App-Token": GLPI_API_APP_TOKEN, "Session-Token": user_token}
    data = {"name": title, "content": description}
    response = requests.post(f"{GLPI_API_URL}/Ticket", headers=headers, json=data)
    response.raise_for_status()

    return response.json()

def update_user_request(user_token, request_id, status):
    """
    Updates the status of the request with the given ID in the GLPI API on behalf of the user with the given token.

    Args:
        user_token (str): The token for the user making the request.
        request_id (int): The ID of the request to update.
        status (int): The new status code for the request.

    Returns:
        dict: A dict representing the updated request.
    """
    headers = {"App-Token": GLPI_API_APP_TOKEN, "Session-Token": user_token}
    data = {"input": {"status": status}}
    response = requests.put(f"{GLPI_API_URL}/Ticket/{request_id}", headers=headers, json=data)
    response.raise_for_status()

    return response.json()