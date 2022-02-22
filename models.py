import json


class User(object):

    def __init__(self, first_name, last_name, username, password, email, date_of_birth=None, status=None, city=None, country=None,
    phone_number=None):

        self.first_name = first_name
        self.last_name = last_name   
        self.username = username
        self.password = password
        self.email = email
        self.date_of_birth = date_of_birth
        self.status = status
        self.country = country
        self.city = city
        self.phone_number = phone_number

    def __init__(self, user_dict):
        self.__dict__.update(user_dict)
    
    @staticmethod
    def from_dict(source):
        return json.loads(json.dumps(source), object_hook=User)
    
    def to_dict(self):
        return self.__dict__
    