class User():
    __name = 'Unknown' # double underscore signifies private variable, can only be used within the class, and cannot be referenced outside 

    def set_name(self, provided_name):
        if ("Mr" in provided_name):
            print(">> Error, no titles can be included in the name")
        else:
            self.__name = provided_name

    def get_name(self):
        return self.__name


user_andres = User()
user_andres.set_name("Andres Castro") # we use the setter to set the name
print(user_andres.get_name()) # we get the name with our getter

user_celeste = User()
user_celeste.__name = "Celeste Elizondo" # we are trying to set a private attribute in our obj, we cant, returns te original value
print(user_celeste.get_name())

user_li = User()
user_li.set_name("Mr. Li Zhang") # uses the getter and setter but is caught by our conditional
print(user_li.get_name()) # will return the original value as the name was caught in the exception
