class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return self.__dict__

    @classmethod
    def dict_to(cls,d):
        return cls(d["name"], d["email"], d["password"])

