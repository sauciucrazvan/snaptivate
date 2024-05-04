import sys, webbrowser

def start(file_url):
    print("Debug: Started searching with Google Lens...")

    search_url = f"https://lens.google.com/uploadbyurl?url={file_url}"
    webbrowser.open(search_url)

    sys.exit()
