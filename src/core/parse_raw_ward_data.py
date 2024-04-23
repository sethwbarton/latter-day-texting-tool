def parse_raw_ward_data(json_data):
    members = []
    for raw in json_data:
        members.append(parse_ward_member(raw))
    return members


def parse_ward_member(raw):
    member = WardMember()
    WardMember.phone_number = raw['phoneNumber']
    WardMember.first_name = raw['nameFormats']['givenPreferredLocal']
    WardMember.last_name = raw['nameFormats']['familyPreferredLocal']
    return member


class WardMember:
    phone_number = None
    first_name = None
    last_name = None
