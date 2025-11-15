class Emp:
    def reg(self,id,name):
        self.id=id
        self.name=name

    def display(self,id, name):
        print ('Id: ',{id})
        print ('Name: ',{name})

class Dev(Emp):
    def welcome():
        print('Welcome to Developer')

d=Dev()
d.welcome()
d.reg(1,'Sam')
d.display()