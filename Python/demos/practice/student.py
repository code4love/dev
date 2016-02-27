class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def desc(self):
        print("name:%s, age:%d"%(self.name,self.age))

    def name(self):
        return self.name

    def age(self):
        return self.age