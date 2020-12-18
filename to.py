import datetime
import os
import sys
import argparse

taskList = []
cc=[]
taskList1=[]

def mainLoop(n):
    if(n==3):
        action=sys.argv[2]
    elif(n==4):
        action=sys.argv[2]
        cc.append(sys.argv[3])
        dd=sys.argv[3]
        print(action)
    try:
        if (action in performAction):
            
            if(action=="delete"):
                    a_file = open("todo.txt", "r")
                    lines = a_file.readlines()
                    
                    d=int(dd)
                    del lines[d]
                    new_file = open("todo.txt", "w+")
                    for line in lines:
                        new_file.write(line)

                    new_file.close()
                    print ("Task deleted")
            elif(action=="new"):
                    print ("")
                    newTaskName = cc
    
                    taskList.append(newTaskName)
                    print(str(newTaskName)+str(" added ")+"todo")
                    with open('todo.txt', 'a') as the_file:
                        the_file.write(str(newTaskName[0])+"\n")
            elif(action=="ls"):
                for line in open('todo.txt','r').readlines():
                    taskList.append(line.strip())
                for i in range(len(taskList)):
                    print ("["+str(i)+"]", end = " ")
                    print (taskList[i])
                
            elif(action=="help"):
                        print("usage")
                        list = ['ref        #Refresh', 'new        #New job/task(add todo items)', 'delete      #Delete job/task(delete todo items)','ls          #show all todo task/items/jobs','exit        #Exit','help         #to show usage','do          #to do the task/jobs','report      #report to get the details of jobs/task']
                        print(*list, sep = "\n")
                    
            elif(action=="ref"):
                input("Done !!!Press enter to continue")
            elif(action=="do"):
                    
                    a_file = open("todo.txt", "r")
                    lines = a_file.readlines()
                    x = datetime.datetime.now()
                    
                    d=int(dd)
                    
                    line1 = lines[d]
                    print(line1)
                    new_file1 = open("report.txt", "a")
                    new_file1.write("["+str(x)+"]"+str(line1))
                    new_file1.close()


                    del lines[d]

                    new_file = open("todo.txt", "w+")
                    for line in lines:
                        new_file.write(line)

                    new_file.close()
                    print ("Task done")
            elif(action=="report"):
                for line in open('report.txt','r').readlines():
                    taskList1.append(line.strip())
                for i in range(len(taskList1)):
                    print ("\n["+str("Task done")+"]", end = " ")
                    print (taskList1[i])
                    
                for line in open('todo.txt','r').readlines():
                    taskList.append(line.strip())
                print("\n[Remaining task]")
                for i in range(len(taskList)):
                    print ("["+str(i)+"]", end = " ")
                    print (taskList[i])
        elif(action == "exit"):
            print("end")
            sys.exit()
        else:
            print("tumble weed")
    except ValueError:
        print ('value error')
        input("Press enter to continue")
        
performAction = {
    "ref",
    "new",
    "delete",
    "ls",
    "help",
    "do",
    "report"
    
}
n=len(sys.argv)
if(n==2):
    if(sys.argv[1]=='./todo'):
        print("usage")
        list = ['ref        #Refresh', 'new        #New job/task(add todo items)', 'delete      #Delete job/task(delete todo items)','ls          #show all todo task/items/jobs','exit        #Exit','help         #to show usage','do          #to do the task/jobs','report      #report to get the details of jobs/task']
        print(*list, sep = "\n")
    else:
        print("please enter correct command   -->   ./todo  command")    
elif(n==3):
    if(sys.argv[1]=='./todo'):
        mainLoop(n)
    else:
        print("please enter correct command   -->   ./todo  command")
elif(n==4):
    if(sys.argv[1]=='./todo'):
        mainLoop(n)
    else:
        print("please enter correct command   -->   ./todo  command")
else:
        print("please enter correct command   -->   ./todo  command")
