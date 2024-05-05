import requests, os, sys, time

from processes import search
from configuration import configuration

def start() -> None:
    file = os.path.join(os.path.expanduser('~'), 'Documents', 'Snaptivate', 'latest.jpg')

    upload_url = "https://api.imgbb.com/1/upload"
    params = {
        "key": configuration.getConfigurationValue("IMGBB_API_KEY"),
        "expiration": 300
    }
    files = {"image": open(file, "rb")}

    response = requests.post(upload_url, params = params, files = files)
    json_response = response.json()

    if response.status_code == 200 and json_response["success"]:
        search.start(json_response["data"]["url"])
    else:
        print("Error: Couldn't access the ImgBB API; make sure you've provided the correct API key.")
        print("Provide your API key in the configuration.yaml file, located in:", f'{os.path.expanduser('~').replace('\\', '/')}/Documents/Snaptivate')
        print("The application is closing in 5 seconds...")

        time.sleep(5)
        sys.exit()