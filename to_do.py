
'''
Create a to-do list
'''
if __name__ == '__main__':
    tasks = []

    while True:
        print("To do list:\n1. Add\n2. View\n3. Remove\n4. Exit")
        choice = input("Choose ad option: ")

        match choice:
            case "1":
                task = input("\nWhat you want to add? ").strip()
                tasks.append(task)
            case "2":
                if not tasks: 
                    print("\nSorry, you've not tasks\n")
                else:
                    counter = 1
                    print("\nTo-do list:")
                    for i in tasks:
                        print(str(counter) +". " + i + "\n")
                        counter+=1
            case "3":
                if not tasks:
                    print("\nSorry, you've not tasks\n")
                else:
                    counter = 1
                    print("\nTo-do list:")
                    for i in tasks:
                        print(str(counter) +". " + i + "\n")
                        counter+=1
                    rm_task = input("What task you wanto to remove? ").strip()
                    tasks.pop(int(rm_task)-1)
            case "4":
                print("Ok Bye!")
                break
                
            
                    

