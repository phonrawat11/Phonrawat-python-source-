class pub_mod:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        print("Age:", self.age)
obj = pub_mod("John", 30)
obj1 = pub_mod("Alice", 25)        
print("Name:", obj.name);
print("Name:", obj1.name);