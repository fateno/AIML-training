from ourpack import welcome

username = input('Please enter your name:')
print (welcome.display(username))
msg = welcome.display(username)
print ('Message for you: ', msg)