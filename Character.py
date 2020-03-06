

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
        name = character.name[self.name]
        role = character.role[self.role]
        profession = character.profession[self.profession]
        age = character.age[self.age]
        return str(name + role + profession + age)


