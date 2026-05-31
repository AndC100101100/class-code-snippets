import types

class User():
    name = 'IDK'
    age = 0
    
    def set_name(self, provided_name):
        self.name = provided_name

    def get_name(self):
        return self.name

    def set_age(self, provided_age):
        self.age = provided_age

    def get_age(self):
        return self.age
        
    def output_info(self):
        print("Hi, I am " + self.get_name() + " and I am " + str(self.get_age()))






user_andres = User()
user_andres.set_name("Andres")
user_andres.set_age(22)
user_andres.output_info()



