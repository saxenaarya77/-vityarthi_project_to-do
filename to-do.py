t = []
# t is a list
def show() :
    print("\n-- To do list --")
    print("1. add a task ")
    print("2. view tasks ")
    print("3. remove a task ")
    print("4. exit ")
#we will define a function
def add() :
    ta = input("Enter the task: ")
    t.append(ta)
    print("Task added !")

def view() :
    if len(t) == 0:
        print("No task added yet. ")
    else :
        print("\nYour task :")
        i = 0
        while i < len(t) :
            print(str(i+1) + ". " + t[i])
            i += 1

def rem() :
    if len(t) == 0 :
        print("No task to remove.")
    else :
        view()
        n = int(input("Enter the task number to remove : "))
        if n >= 1 and n <= len(t) :
            removed = t.pop(n-1)
            print("Removed:", removed)
        else:
            print("Invalid task number!")

while True :
    show()
    ch = input("Enter your choice (1-4) : ")

    if ch == "1" :
        add()
    elif ch == "2" :
        view()
    elif ch == "3" :
        rem()
    elif ch == "4" :
        print("Exiting..... goodbye! ")
        break
    else:
        print("Invalid choice .! Please enter 1–4.")