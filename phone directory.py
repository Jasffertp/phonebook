#Author: Jasffer T. Padigdig
#Date: October 14, 2020
#Assignment: Phonebook code
#Description: The code is executes the CRUD using hashing
#References: 

def linearprobing(A, location):
    counter = 0
    #if the counter is greater than the length of the list then it means the phone book is already full
    while counter < len(A):
        val = (location + 1)%len(A)
        
        if A[val] == None:
            return val
        
        #increase the location by 1 until we reach an empty location
        location += 1
        counter += 1
    
    #return false since it's already full
    return False

def create(A):
    account = []
    #getting the user info
    userid = int(input('input user ID: '))
    account.append(userid)
    name = input('input user name: ')
    account.append(name)
    tel = int(input('input telephone number: '))
    account.append(tel)
    
    #hashing the location of the information
    location = tel%len(A)
    
    
    #if hashed location isn't empty insert the user information
    if A[location] == None:
        A[location] = account
        print('data has been added.')
    
    #if location isn't empty, check if the telephone number matches with the input
    else:
        if A[location][2] == tel:
            print('That telephone number already exists!')
            return
        else:
            checker = linearprobing(A, location)
            if checker:
                A[checker] = account
                print('data has been added')
            else:
                print('The phonebook is already full!')

    return A

def read(A):
    print('')
    print('1 - you want to read the whole phonebook         2 - read a specific part of the phonebook')
    choice = input('>>>> ')
    
    if choice == '1':
        print('')
        print('ID           Name            Telephone')
        
        for i in range(len(A)):
            if A[i] != None:
                print(f'{A[i][0]}            {A[i][1]}             {A[i][2]}')
        
    elif choice == '2':
        print('')
        i = int(input('what is the telephone number you want to search for? '))
        location = i%(len(A))
        
        if  A[location] != None and A[location][2] == i:
            print(f'ID: {A[location][0]}          Username: {A[location][1]}          Telephone: {A[location][2]}')
        else:
            counter = 0
            while counter < len(A):
                checker = (location + 1)%len(A)
                if A[checker] != None and A[checker][2] == i:
                    print(f'ID: {A[checker][0]}          Username: {A[checker][1]}          Telephone: {A[checker][2]}')
                    return
                location += 1
                counter += 1
            print('the value does not exist!')
        
    else:
        print('invalid syntax')
        return

def update(A):
    print('')
    i = int(input('what is the telephone number you want to update? '))
    location = i%(len(A))
    
    if  A[location] != None and A[location][2] == i:
            update = []
            #getting the user info
            userid = int(input('input user ID: '))
            update.append(userid)
            name = input('input user name: ')
            update.append(name)
            tel = int(input('input telephone number: '))
            update.append(tel)
            
            A[location] = update
            
            print('')
            print('user has been updated, new values:')
            print(f'ID: {A[location][0]}            Username: {A[location][1]}             Telephone: {A[location][2]}')
    else:
        counter = 0
        while counter < len(A):
            checker = (location + 1)%len(A)
            if A[checker] != None and A[checker][2] == i:
                update = []
                #getting the user info
                userid = int(input('input user ID: '))
                update.append(userid)
                name = input('input user name: ')
                update.append(name)
                tel = int(input('input telephone number: '))
                update.append(tel)
                
                A[checker] = update
                
                print('')
                print('user has been updated, new values:')
                print(f'ID: {A[checker][0]}            Username: {A[checker][1]}             Telephone: {A[checker][2]}')
                return
            location += 1
            counter += 1
        print('data does not exist!')

def delete(A):
    print('')
    i = int(input('what is the telephone number you want to delete? '))
    location = i%(len(A))
    
    if  A[location] != None and A[location][2] == i:
        A[location] = None
    else:
        counter = 0
        while counter < len(A):
            checker = (location + 1)%len(A)
            if A[checker] != None and A[checker][2] == i:
                A[checker] = None
                print('The data has been deleted.')
                return
            location += 1
            counter += 1
            
        print('data does not exist!')

A = [None] * 10
end = True

while end:
    print('what do you want to do?')
    print('1 - Create new Account           2 - Read an account')
    print('3 - Update existing account      4 - delete existing account')
    print('')
    choice = input('>>>> ')
    
    if choice == '1':
         create(A)
    elif choice == '2':
        read(A)
    elif choice == '3':
        update(A)
    elif choice == '4':
        delete(A)
    else:
        end = False
    
    print('')    
print('the program has ended')
print('')
print('final phonebook:')
print('ID           Name            Telephone')

for i in range(len(A)):
    if A[i] != None:
        print(f'{A[i][0]}            {A[i][1]}             {A[i][2]}')