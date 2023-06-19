import pandas as pd

def read_json(file_path='config.json') -> pd.DataFrame:
    data = pd.read_json(file_path)
    return data

def get_topics(device: str) -> dict:
    data = read_json()
    try:
        data_dict = data[device]['Topics']
    except KeyError:
        return {'error': 'Device not found'}
    return data_dict


def get_config(device: str, param: str) -> str:
    data = read_json()
    try:
        value = data[device][param]
    except KeyError:
        return 'not_found_error'
    return value


def get_components() -> list:
    data = read_json()
    try:
        data_dict = list(data.columns)
    except KeyError:
        return ['error']
    return data_dict
