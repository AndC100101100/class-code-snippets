class User():
    name = 'IDK'
    age = 0

    def output_info(self):
        print("Hi, I am " + self.name + " and I am " + str(self.age))



user_andres = User()
user_andres.name = "Andres"
user_andres.age = 22
user_andres.output_info()


