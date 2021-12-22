import json


class User(object):

    def __init__(self, username, password, email, date_of_birth=None, status=None, city=None, country=None,
    phone_number=None):
        
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
    
    # def __iter__(self):
    #     for key in self
    
    @staticmethod
    def from_dict(source):
        return json.loads(json.dumps(source), object_hook=User)
    
    def to_dict(self):
        return self.__dict__
    