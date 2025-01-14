tasks=[]  #Inititalizing list of tasks



def add_to_list():   #add to list function                                                            
    global tasks
    x = input('what tasks need to be done? ')
    tasks.append(x)
    g = (str(input(f'{x} has been added to the list would you like to continue y/n? ')))
    while g == 'y':
         y = input('what tasks need to be done?')
         tasks.append(y)
         g = input(f'Would you like to add more tasks? ')
    else:
        print('Have a nice day')
        
def check_list():    # Check list function
    if not tasks:
        print('list is empty')
    else:
        for i, task in enumerate(tasks):
            print(f'{i+1}.{task}')
            


def check_off_list():     # checkl off list function
    global tasks
    x = 'y'
    if not tasks:
        print('list is empty')
    else:
        while x == 'y':
            check_list()
            index = int(input('what task would you like to remove? '))-1
            if 0 <= index <= len(tasks):
                tasks.pop(index)
                print('The task has been completed')
                if not tasks:
                    print('list is empty')
                    x ='n'
                else:
                    x = input('Would you like to remove another task? y/n? ')
        else:
            print('Have a nice day!')
            

def home():         # Main fuction, Loops through function working as a hub for the program.
    
    choice = 1
    while choice in (1, 2, 3):
        print(f'welcome to your Check List {name}')
        print("""
        1. Check List
        2. Add to List
        3. Check Off List
        """)
        choice = int(input('Which would you like to do today! '))
        if choice == 1:
            check_list()
        elif choice == 2:
            add_to_list()
        elif choice == 3:
            check_off_list()  

        
name = input('What is your name? ')

home()
 