class Base:
    def __init__(self,name):
        self.name = name

class inher(Base):
    def __init__(self,name,age):
        self.age = age
        super().__init__(name)

a = inher('sagar',23)
print(a.name)