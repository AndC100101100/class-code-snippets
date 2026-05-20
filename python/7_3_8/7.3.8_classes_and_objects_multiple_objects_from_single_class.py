class User():
    name = 'IDK'
    age = 0

    def output_info(self):
        print("Hi, I am " + self.name + " and I am " + str(self.age))



user_andres = User()
user_andres.name = "Andres"
user_andres.age = 22
user_andres.output_info()


user_celeste = User()
user_celeste.name = "Celeste"
user_celeste.age = 19
user_celeste.output_info()

if (user_andres.age > user_celeste.age):
    print("Andres is older than Celeste")
else:
    print("Andres is younger than Celeste")
