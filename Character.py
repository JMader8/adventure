

class character(object):
    name = ""
    role = ""
    profession = ""
    age = "0"

    def __init__(self, name, role, profession, age):
        self.name = name
        self.role = role
        self.profession = profession
        self.age = age

    def __str__(self):
        name = str(character.name)
        role = character.role
        profession = character.profession
        age = character.age

        return (f"{name} + {role} + {profession} + {age}")


