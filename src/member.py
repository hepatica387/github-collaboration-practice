members = []

MAX_MEMBER_COUNT = 100

def add_member(name, age):
    member = {
        "name": name,
        "age": age
    }

    members.append(member)

    return member
