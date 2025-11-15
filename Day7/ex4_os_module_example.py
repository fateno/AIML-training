#import os 

#print ('Current directory: ',os.getcwd())

#Create a folder directory inside current directory using Python
import os
import sys

cdir=os.getcwd()
#os.system(f"chmod -R 777 {cdir}")
folder_name=input("Enter folder name: ")
folder_path=os.path.join(cdir,folder_name)
if (os.path.exists(folder_path)):
    print ("Folder exists")
    new_folder_name=input("Enter new name: ")
    os.rename(folder_path, new_folder_name)
    new_folder_path=os.path.join(cdir,new_folder_name)
    #print (new_folder_path)
    #sys.exit()
    if os.path.exists(new_folder_path):
        print (f"{folder_path} has been renamed to {new_folder_path}")
else: 
    os.makedirs(folder_path, exist_ok=True)
    print (f'{folder_name} created at {folder_path}')