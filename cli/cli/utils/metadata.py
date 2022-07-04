import json
import os

BIGDRIVE_FOLDER_ENV_KEY = "BIGDRIVE_FOLDER"
HOME_DIRECTORY = os.path.expanduser("~")
BIGDRIVE_FOLDER = os.environ.get(BIGDRIVE_FOLDER_ENV_KEY, ".bd")

METADATA_FILE_NAME = "config.json"
METADATA_FOLDER_PATH = os.path.join(HOME_DIRECTORY, BIGDRIVE_FOLDER)
METADATA_FILE_PATH = os.path.join(METADATA_FOLDER_PATH, METADATA_FILE_NAME)

_config = {}


def get_config():
    return _config


def load_config():
    global _config

    os.makedirs(METADATA_FOLDER_PATH, exist_ok=True)

    try:
        with open(METADATA_FILE_PATH, mode="r") as config_file:
            _config = json.loads(config_file.read())
    except FileNotFoundError:
        dump_config()


def dump_config():
    with open(METADATA_FILE_PATH, mode="w+") as config_file:
        config_file.write(json.dumps(_config))


def update_auth_config_from_sign_in(token, email, password):
    _config["id_token"] = token
    _config["email"] = email
    _config["password"] = password


def update_auth_config_token(new_token):
    _config["id_token"] = new_token
