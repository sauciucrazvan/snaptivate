import sys, webbrowser

def start(file_url) -> None:
    # Opening the browser with the requested image.
    search_url = f"https://lens.google.com/uploadbyurl?url={file_url}"
    webbrowser.open(search_url)

    # Quitting the application's engine as it is not needed anymore.
    sys.exit()
