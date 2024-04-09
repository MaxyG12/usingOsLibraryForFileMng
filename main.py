import os,time,random

def clear():
  os.system("clear")

toDoList = []

#f = open("toDoList.txt","r")
#toDoList = eval(f.read())
#f.close()

print("ToDo List Manager")
print()
def printList():
  print()
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("Do you want to view, add, or edit your to do list?: ")
  if menu == "view":
    printList()
  elif menu == "add":
    item = input("What do you want to add?: ")
    toDoList.append(item)
  elif menu == "edit":
    item = input("What do you want to remove?: ")
    if item in toDoList:
      confirmation = input("Are you sure you want to remove this?: ")
      if confirmation == "yes":
        toDoList.remove(item)
      else:
        print("Okay, we won't remove it")
    else:
      print(f"{item} was not in the list")
  else:
    print("That is not a valid option")
  time.sleep(1)
  clear()
  delete = input("Do you want to delete the list?: ")
  if delete == "yes":
    toDoList = []
  else:
    continue

  os.mkdir = ("backup")
  name = f"backup{random.randint(1,1000000000)}.txt"
  os.popen(f"cp toDoList.txt backup/{name}")
  
  f = open("toDoList.txt","w")
  f.write(str(toDoList))
  f.close()
clear()


