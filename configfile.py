from configparser import ConfigParser
from pathlib import Path


def get_config_details(config_file_path: Path=Path(__file__).parent, file_name: str='config.cfg', config_name: str='default', settings: list=[]) -> dict:
    config = ConfigParser()
    config.read(config_file_path / file_name)
    
    config_settings = {}
    for setting in settings:
        key = setting
        value = config[config_name][setting]
        config_settings
        config_settings.update({key: value})

    return  config_settings