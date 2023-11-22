def display_todo_list(todo_list):
    if not todo_list:
        print("your to-do list is empty.")
    else:
        print("your to-do list:")
        for index,task in enumerate(todo_list,start=1):
            print(f"{index}.{task}")
            #function to add a task to the to-do list
            def add_task(todo_list,task):
                todo_list.append(task)
                print(f"Task'{task}' added to the to-do list.")
                def remove_task(todo_task,task_index):
                    if 1 <= task_index <= len(todo_list):
                        removed_task=todo_list.pop(task_index-1)
                        print(f"Task'{removed_task}'removed from the to-do list.")
                    else:
                        print("invalid task index.")
                        #Main function
                        def main():
                            todo_list=[]
                            while True:
                                print("\n options:")
                                print("1.display to-do list")
                                print("2.add a task")
                                print("3.remove a task")
                                print("4.quit")
                                choice=input("enter your choice(1-4):")
                                if choice=="1":
                                    display_todo_list(todo_list)
                                elif choice=="2":
                                    task=input("enter the task:")
                                    display_todo_list(todo_list)
                                elif choice=="3":
                                    task_index=int(input("enter the task index to remove:"))
                                    remove_task(todo_list,task_index)
                                elif choice=="4":
                                    print("quitting the to-do list program.bye!")
                                    break
                                else:
                                    print("invalid choice.Please enter a no. between 1 and 4.")
                                    if __name__=="__main__":
                                        main()

