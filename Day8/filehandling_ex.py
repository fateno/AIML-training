import os

#curpath = r"/Users/fateno/Desktop/AIML//Day8/ourfiles"
curpath = os.getcwd()
print (curpath)
filename= input("Please input file name with .txt: \t")
file_path= os.path.join(curpath,filename)
print (file_path)

#curpath="/Users/fateno/Desktop/AIML/Day8/ourfiles/sample.txt"

#def read(file_path):

def append (file_path):
    edit=input("Do you want to edit the file (y/n): \t")
    if (input!= 'y'): 
        file = open(file_path,'a')
        content = input("Enter text to add in file")
        file.write(content)
        file.close()
    else: 
        print ("Bye")




if (os.path.exists(file_path)):
    file=open(file_path,'r')
    content=file.read()
    print("File Content as follows: \n")
    print (content)
    append(file_path)

    #file = open(file_path,'a')
    #content = input("Enter text to add in file")
    #file.write(content)
    #file.close()
else: 
    print ("f{file_path} is not available")
    file = open(file_path, 'w')
    print (f"{file_path} is created.")
    content = input("Enter text to write in file: ")
    file.write(content)
    file.close()
