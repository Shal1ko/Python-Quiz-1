import random
import time

id = 0

class TaskManager:
    
    taskList = []
    identifierList = []
    completedTasks = 0
    
    def __init__(self):
        pass
    
    
    def logger(func):
        def wrapper(task):
            start = time.time()
            print(f"Executing function {func.__name__}...")
            func(task)
            curr = time.time() - start
            print(f"Function {func.__name__} comlleted in {curr} seconds")
        return wrapper
            
            
            
    @logger
    @staticmethod
    def addTask(task):
        if task.identifier in TaskManager.identifierList:
            print("Task with this identifier already exists or has already been completed.")
            return
        TaskManager.identifierList.append(task.identifier)
        TaskManager.taskList.append(task)
        
    @logger
    @staticmethod
    def completeTask(task):
        TaskManager.completedTasks += 1
        TaskManager.taskList.remove(task)
        
    @logger
    @staticmethod
    def removeTask(task):
        TaskManager.identifierList.remove(task.identifier)
        TaskManager.taskList.remove(task)
        
        
    @staticmethod
    def taskGen(x):
        global id
        for i in range(x):
            yield task(id, "F", "Waiting", random.randint(1, 5), "IDK")
            id += 1
            
        
        
        
        
    
    


class task:
    def __init__(self, identidier, name, status, priority, dueDate):
        self.__identifier = identidier
        self.__name = name
        self.__status = status
        self.__priority = priority
        self.__dueDate = dueDate
        
    @property
    def identifier(self):
        return self.__identifier
    @identifier.setter
    def identifier(self, x):
        self.__identifier = x
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, x):
        self.__name = x
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, x):
        self.__status = x
    @property
    def priority(self):
        return self.__priority
    @priority.setter
    def priority(self, x):
        self.__priority = x
    @property
    def dueDate(self):
        return self.__dueDate
    @dueDate.setter
    def dueDate(self, x):
        self.__dueDate = x
        
    def __str__(self):
        return f"Identifier: {self.__identifier} name: {self.__name} Status: {self.__status} priority: {self.__priority} dueDate = {self.__dueDate} \n"


def generate(x):
    for i in TaskManager.taskGen(x):
        TaskManager.addTask(i)
        

generate(6)

    
while True:
    print("choose an action")
    print("1. task list     2. complete first high priority task    3. add some tasks   4. remove a task by id      5. close")
    try:
        choice = int(input())
    except ValueError:
        print("choose corretly")
        continue
    
    if choice == 1:
        print(*TaskManager.taskList)
        
    elif choice==2:
        firsthighest = 0
        for index, obj in enumerate(TaskManager.taskList):
            if TaskManager.taskList[index].priority > TaskManager.taskList[firsthighest].priority:
                firsthighest = index
        TaskManager.completeTask(TaskManager.taskList[firsthighest])
        
    elif choice == 3:
        print("how many tasks do you want to add?")
        try:
            num = int(input())
        except ValueError:
            print("choose correctly")
            continue
        generate(num)
        
    elif choice == 4:
        print("enterthe id of a task you want to remove")
        try:
            id = int(input())
        except ValueError:
            print("choose correctly")
            continue
        for i in TaskManager.taskList:
            if i.identifier == id:
                TaskManager.removeTask(i)
                break
            
    elif choice == 5:
        print("exiting...")
        break
    else:
        print("choose correctly")