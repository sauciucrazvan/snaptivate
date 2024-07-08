import requests, os, re

from dialogs import error
from processes import search
from configuration import configuration as config

def start() -> None:
    file = os.path.join(os.path.expanduser('~'), 'Documents', 'Snaptivate', 'latest.jpg')

    if not os.path.exists(file):
        error.show_error_dialog("File not found at: {}".format(file))
        return

    upload_url = "https://api.imgbb.com/1/upload"
    params = {
        "key": config.getValue("api_key"),
        "expiration": 300
    }
    files = {"image": open(file, "rb")}

    try:
        response = requests.post(upload_url, params = params, files = files)
        json_response = response.json()

        if response.status_code == 200 and json_response["success"]:
            search.start(json_response["data"]["url"])
        else:
            config_file_location = f"{os.path.expanduser('~').replace('\\', '/')}/Documents/Snaptivate"
            error.show_error_dialog(f"Couldn't access the ImgBB API! Make sure you've provided the correct API key.\n\nProvide your API key in the configuration.yaml file, located in:\n{config_file_location}")
    except requests.ConnectionError as exception:
        exception_message = re.sub(r'key=[^&]*&?', '', str(exception))
        error.show_error_dialog(f"An error occured! Make sure you're connected to the internet.\n\nException:\n{exception_message}")