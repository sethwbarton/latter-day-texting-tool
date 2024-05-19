def parse_raw_ward_data(json_data):
    members = []
    for raw in json_data:
        members.append(parse_ward_member(raw))
    return [i for i in members if i is not None]


def parse_ward_member(raw):
    phone_number = raw['phoneNumber']
    first_name = raw['nameFormats']['givenPreferredLocal']
    last_name = raw['nameFormats']['familyPreferredLocal']
    if not phone_number or not first_name or not last_name:
        return None
    member = WardMember(phone_number=filter_numeric(phone_number),
                        first_name=first_name,
                        last_name=last_name,
                        note=get_note(raw))
    return member


def filter_numeric(input_string):
    numeric_filtered = ''.join([char for char in input_string if char.isdigit()])
    return numeric_filtered


def get_note(raw):
    if raw['sex'] == 'M':
        return 'Elders Quorum'
    return 'Relief Society'


class WardMember:
    def __init__(self, phone_number=None, first_name=None, last_name=None, note=None):
        self.last_name = last_name
        self.phone_number = phone_number
        self.first_name = first_name
        self.note = note

    def to_csv_row(self):
        phone_number = self.phone_number
        first_name = self.first_name
        last_name = self.last_name

        return f'{last_name},{first_name},{phone_number},Elders Quorum\n'
