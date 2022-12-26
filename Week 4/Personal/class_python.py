from bs4 import BeautifulSoup

var = 1 

class Animal: 

    def __init__(self, name: str, age: int ) -> None:
        self.name = name
        self.age = age
    
    def display(self): 
        print(f"My name is {self.name} and my age is {self.age}")

    def can_fly(self): 
        if self.name == 'Babu': 
            return True
        return False

kaley = Animal("kaley", 16)
babu = Animal("Babu", 6)
fucchu = Animal("Fucchu", 8)

print(kaley.display(), kaley.can_fly())
print(babu.display(), babu.can_fly())
print(fucchu.display(), fucchu.can_fly())