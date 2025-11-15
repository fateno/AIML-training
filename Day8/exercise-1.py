class invalidMark(Exception):
    pass


def check_mark(mark):
    if (mark<=0):
        raise invalidMark('Mark should not be less than 0')
    # elif (mark<50):
    #     raise invalidMark('Mark should be in between 0 and 50')
    elif (mark>=50):
        raise invalidMark('Mark should be in between 0 and 50')
    else: 
        print(f'Mark {mark} is valid')

while True: 
    try: 
        input_mark=int(input('Enter your mark: '))
        check_mark(input_mark)
    except invalidMark as e: 
        print ('Invalid Mark: ',e)
    except Exception as ex: 
        print ("Error: ",ex)

    choice=input('Do you want to continue checking?')
    if (choice != 'y'):
        print ('Bye')
        break

