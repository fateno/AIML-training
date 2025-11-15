class Player: 
    def __init__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team 
    
    def display(self):
        print(f"Id:{self.id}")
        print(f"Name:{self.name}")
        print (f"Team: {self.team}")

    def __str__(self):
        return f'{self.id}{self.name}{self.team}'

p1=Player(1,'MSD','India')
p2=Player(2,'R.Khan','Afghanistan')
p3=Player(3,'Moin Ali','England')


p1.display()
p2.display()
p3.display()

print(p1)