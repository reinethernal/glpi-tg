import requests
from config import GLPI_API_URL, GLPI_API_APP_TOKEN

def get_ticket(ticket_id: int) -> dict:
    """Retrieve information about a ticket by its ID."""
    endpoint = f"{GLPI_API_URL}/Ticket/{ticket_id}"
    response = requests.get(endpoint, headers={"App-Token": GLPI_API_APP_TOKEN})
    if response.ok:
        return response.json()["data"]
    else:
        response.raise_for_status()

def get_tickets_assigned_to_operator(operator_id: int) -> list:
    """Retrieve a list of tickets assigned to the specified operator."""
    endpoint = f"{GLPI_API_URL}/Ticket"
    params = {
        "criteria[0][field]": "12",
        "criteria[0][value]": operator_id,
        "criteria[1][link]": "AND",
        "criteria[1][field]": "status",
        "criteria[1][searchtype]": "equals",
        "criteria[1][value]": "2",
        "forcedisplay[0]": "1",
        "forcedisplay[1]": "2",
        "forcedisplay[2]": "9",
        "forcedisplay[3]": "12",
    }
    response = requests.get(
        endpoint, headers={"App-Token": GLPI_API_APP_TOKEN}, params=params
    )
    if response.ok:
        return response.json()["data"]
    else:
        response.raise_for_status()

def assign_ticket_to_operator(ticket_id: int, operator_id: int) -> dict:
    """Assign the specified ticket to the specified operator."""
    endpoint = f"{GLPI_API_URL}/Ticket/{ticket_id}"
    data = {"input": {"12": operator_id}}
    response = requests.put(
        endpoint, headers={"App-Token": GLPI_API_APP_TOKEN}, json=data
    )
    if response.ok:
        return response.json()
    else:
        response.raise_for_status()

def update_ticket_status(ticket_id: int, status_id: int) -> dict:
    """Update the status of the specified ticket."""
    endpoint = f"{GLPI_API_URL}/Ticket/{ticket_id}"
    data = {"input": {"status": status_id}}
    response = requests.put(
        endpoint, headers={"App-Token": GLPI_API_APP_TOKEN}, json=data
    )
    if response.ok:
        return response.json()
    else:
        response.raise_for_status()

def create_ticket(title: str, description: str, operator_id: int) -> dict:
    """Create a new ticket with the specified title, description, and assigned operator."""
    endpoint = f"{GLPI_API_URL}/Ticket"
    data = {
        "input": {
            "name": title,
            "content": description,
            "type": "2",
            "status": "2",
            "urgency": "3",
            "itilcategories_id": "2",
            "user_id": operator_id,
        }
    }
    response = requests.post(
        endpoint, headers={"App-Token": GLPI_API_APP_TOKEN}, json=data
    )
    if response.ok:
        return response.json()["data"]
    else:
        response.raise_for_status()