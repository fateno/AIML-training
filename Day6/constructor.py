
class Emp: 
    def __init__(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=qual 

    def display(self):
        print('ID: ',self.id)
        print('Name: ',self.name)
        print('Qual: ',self.qual)

class Dev(Emp):
    def __init__(self, id, name, qual, domain, project):
        super().__init__(id, name, qual)
        self.domain=domain
        self.project=project 
    
    def display(self):
        super().display()
        print('Domain: ',self.domain)
        print('Project: ',self.project)
    

e=Emp(1,'John','MCA')
e.display()
devl=Dev(3, 'Ravi', 'MTech', 'e-shopping', 'dotnet')
print('Developer details as follows:')
devl.display()
print('Employee details as follows: ')
e.display()


