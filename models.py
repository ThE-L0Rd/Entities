class Memeber:
    """This class for info about member such as : age, name ."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Post:
    """This class for info about post such as : title, body ."""
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body   
