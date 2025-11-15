#class is template/object factory/blueprint to create object 

#methods are functions defined inside a class 
#describe behavior of objects 

#object constructor (__init__)
# --> run automatically when you create object of the class

'''
class Emp: 
    def display(self): #method #self-->
        print ("Display of Employee Class")

obj = Emp()
obj.display()
e=Emp()
e.display()
'''

class Emp: 
    def reg(self,eid,ename):
        self.eid=eid
        self.ename=ename

    def display(self):
        print("Employee details as follows:")
        print("Employee id:",self.eid)
        print('Employee Name:',self.ename)
    
e1=Emp()
e2=Emp()
e1.reg(1,'Faten')
e1.display()
e2.reg(2,"Sofea")
e2.display()
#staff={""}