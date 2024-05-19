import json
from os import path

from src.core.parse_raw_ward_data import parse_raw_ward_data


def get_example_member():
    base_path = path.dirname(__file__)
    file_path = path.abspath(path.join(base_path, "..", "example_data", "member.json"))
    f = open(file_path)
    data = json.load(f)
    f.close()
    return data


def test_parse_raw_ward_data_includes_phone_number():
    test_data = get_example_member()
    result = parse_raw_ward_data(test_data)
    assert result[0].phone_number == '1234567890'


def test_parse_raw_ward_data_includes_first_name():
    data = get_example_member()
    result = parse_raw_ward_data(data)
    assert result[0].first_name == data[0]['nameFormats']['givenPreferredLocal']


def test_parse_raw_ward_data_includes_last_name():
    data = get_example_member()
    result = parse_raw_ward_data(data)
    assert result[0].last_name == data[0]['nameFormats']['familyPreferredLocal']


def test_parse_raw_ward_data_works_for_multiple_members():
    member_one = get_example_member()[0]
    member_two = get_example_member()[0]
    member_two['nameFormats']['givenPreferredLocal'] = "John"
    member_two['nameFormats']['familyPreferredLocal'] = "Doe"

    result = parse_raw_ward_data([member_one, member_two])

    assert result[0].phone_number == '1234567890'
    assert result[0].first_name == member_one['nameFormats']['givenPreferredLocal']
    assert result[0].last_name == member_one['nameFormats']['familyPreferredLocal']

    assert result[1].phone_number == '1234567890'
    assert result[1].first_name == member_two['nameFormats']['givenPreferredLocal']
    assert result[1].last_name == member_two['nameFormats']['familyPreferredLocal']


def test_parse_raw_ward_data_adds_note_for_elder_or_sister():
    test_member = get_example_member()[0]

    result = parse_raw_ward_data([test_member])

    assert result[0].note == "Elders Quorum"


def test_if_no_numbers_exist_skip_the_person():
    member_with_no_number = get_example_member()[0]
    member_with_no_number['phoneNumber'] = None

    results = parse_raw_ward_data([member_with_no_number])

    assert results == []


def test_strips_all_non_nums_from_phone_number():
    malformed_number = get_example_member()[0]
    malformed_number['phoneNumber'] = '+1 444-444-4444 (his)'

    results = parse_raw_ward_data([malformed_number])

    assert results[0].phone_number == "14444444444"


def test_ignores_members_with_missing_first_or_last_name():
    missing_first_name = get_example_member()[0]
    missing_first_name['nameFormats']['givenPreferredLocal'] = None

    missing_last_name = get_example_member()[0]
    missing_last_name['nameFormats']['familyPreferredLocal'] = None

    results = parse_raw_ward_data([missing_first_name, missing_last_name])

    assert results == []
