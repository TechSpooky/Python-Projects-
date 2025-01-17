class Task():
    def __init__(self,description):
        self.description = description
        self.complete = False

    def complete_task(self):
        self.complete = True 
    
    def __str__(self):
            if self.complete is False:
                return (f'{self.description} - Not Complete')
            else:
                 return (f'{self.description} - Complete')
        
    def __len__(self):
        return len(self.tasks)    
    



    
class Tasks():
    def __init__(self):
        self.tasks = []


    def add_task(self,task):
        self.tasks.append(task)
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task number")
    
    def __str__(self):
        if not self.tasks:
            return ('list is empty')
        else:
            x = ""
            for i, task in enumerate(self.tasks):
               x += (f'{i+1}.{task}\n')
        return x

def Home():
    to_do_list = Tasks()
    name = input('whats your name?')
    print(f'Welcome to your To-Do-List {name}')
    
    choice = 1
    while choice in (1, 2, 3):
        choice = int(input('Which would you like to do today! '))
        if choice == 1:
            print(to_do_list)

        elif choice == 2:
            x = input('what task needs to be done')
            to_do = Task(x)
            to_do_list.add_task(to_do.description)
            print(f'{ to_do.description} has been added to the list')

        elif choice == 3:
            print(to_do_list)
            index = int(input('what task do I remove?')) - 1
            to_do_list.remove_task(index)

Home()