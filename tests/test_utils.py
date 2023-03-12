import json


def load_test_fixture_data(file_path: str):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["results"]
