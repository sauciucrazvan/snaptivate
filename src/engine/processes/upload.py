import requests, os, sys, time

from processes import search
from configuration import configuration as config
from dialogs import error

def start() -> None:
    file = os.path.join(os.path.expanduser('~'), 'Documents', 'Snaptivate', 'latest.jpg')

    upload_url = "https://api.imgbb.com/1/upload"
    params = {
        "key": config.getValue("IMGBB_API_KEY"),
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
            error.show_error_dialog(f"Couldn't access the ImgBB API; make sure you've provided the correct API key.\n\nProvide your API key in the configuration.yaml file, located in:\n{config_file_location}")
    except requests.ConnectionError as exception:
        error.show_error_dialog(f"An error occured! Make sure you're connected to the internet.\n\nDetails:\n{exception}")