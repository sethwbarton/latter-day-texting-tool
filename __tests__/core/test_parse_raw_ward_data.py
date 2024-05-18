import json
from os import path

from src.core.parse_raw_ward_data import parse_raw_ward_data


def get_example_member():
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "example_data", "member.json"))
    f = open(filepath)
    data = json.load(f)
    f.close()
    return data


def test_parse_raw_ward_data_includes_phone_number():
    test_data = get_example_member()
    result = parse_raw_ward_data(test_data)
    assert result[0].phone_number == test_data[0]['phoneNumber']


def test_parse_raw_ward_data_includes_first_name():
    data = get_example_member()
    result = parse_raw_ward_data(data)
    assert result[0].first_name == data[0]['nameFormats']['givenPreferredLocal']


def test_parse_raw_ward_data_includes_last_name():
    data = get_example_member()
    result = parse_raw_ward_data(data)
    assert result[0].last_name == data[0]['nameFormats']['familyPreferredLocal']