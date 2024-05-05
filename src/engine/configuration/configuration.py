import yaml, os

defaultConfig = """# Snaptivate configuration.yaml file

# Provide the API key that you'll get when you access the following link:
# https://api.imgbb.com/
# Make sure that you are logged in first! Example:
# api_key: \"abcdefghjkl\"
api_key: \"\"

"""

def getValue(value: str) -> object:
    # Creates the directory if it's not already
    directory = os.path.join(os.path.expanduser('~'), 'Documents', 'Snaptivate')
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Check if the file exists, if not, creates it with the default configuration
    file_path = os.path.join(directory, 'configuration.yaml')
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(defaultConfig)
    
    # Reads the configuration.yaml file and returns the value requested.
    file_path = os.path.join(directory, 'configuration.yaml')
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data[value]
    