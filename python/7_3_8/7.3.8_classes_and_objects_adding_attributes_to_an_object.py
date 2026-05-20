class User():
    name = 'IDK'
    age = 0

    def output_info(self):
        print("Hi, I am " + self.name + " and I am " + str(self.age))


'''
when you change an object, be it add remove or edit it, those changes
only apply to that one object, it does not affect the other objects 
or the template class that it was originally created from
'''
user_andres = User()
user_andres.name = "Andres"
user_andres.age = 22
user_andres.country = "Costa Rica"


user_celeste = User()
user_celeste.name = "Celeste"
user_celeste.age = 19
user_celeste.country = "Costa Rica"

print(user_andres.country)
print(user_celeste.country)
