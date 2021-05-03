#This program is intended to help a small business manage the tasks assigned to each team member.
#Admin will be able to register new users, generate reports, and view task statistics.
#All users (including admin) will be able to log in with a username and password, add tasks, view all tasks, view their tasks,
#and edit tasks (mark tasks complete, change task due dates, and assign tasks to a different user).


#Functions:

#1.) "login_screen()" logs users into the system.
#    Variables "username", "password", and "valid" are assigned global values, otherwise they cannot be used outside this function.
#    (W3schools.com, 2021, Python - Global Variables, t.ly/LSBj).
#    The user is requested to enter their username and password (stored as "username" and "password").
#    Text file "user.txt" is read and its contents stored as "content" (Hyperiondev, 2021, Working with External Data Sources - Input, p.4).
#    If the username-password string is found in "content", "valid" becomes true, and user enters to the main menu (see main program below).
#    (Note: f-string is used - Hyperiondev, 2021, The String Data Type, p.2 & p.4).
#    Else, while "valid" is false, an error message is displayed, and the user is requested to reenter their login details.
#    If the reentered user input is in "content", "valid" becomes true:

def login_screen():
    
    global username
    global password
    global valid
    
    print("\nPlease enter your details to log in.\n")
    username = input("Username:\n")
    password = input("\nPassword:\n")
    
    f = open("user.txt", "r+")
    content = f.read()
    f.close()
    
    if f"{username}, {password}" in content:
        valid = True
    else:
        while not valid:
            print("\nSorry, incorrect username or password entered.\nPlease reenter your details to log in.\n")
            username = input("Username:\n")
            password = input("\nPassword:\n")
            if f"{username}, {password}" in content:
                valid = True
                

#2.) "reg_user()" allows admin to register new users to the system.
#    Admin is requested to enter the new user's username and password (stored as "username_r" and "password_r").
#    Text file "user.txt" is read, its contents stored as "content", and Boolean control "valid_r" declared false.
#    If the new username is not in "content", "valid_r" becomes true, and the new username and password are written to "user.txt"
#    (Hyperiondev, 2021, Working with External Data Sources - Output, p.2-3).
#    If the new username is in "content", while "valid_r" is false, an error message is displayed, and the user is requested to enter another username.
#    If the reentered username is not present in "user.txt", "valid_r" becomes true, and the new username and password are written to "user.txt":

def reg_user():
    
    print("\nPlease enter a new username and password.\n")       
    username_r = input("Username:\n")
    password_r = input("\nPassword:\n")
    
    f = open("user.txt", "r+")
    content = f.read()    
    valid_r = False
    
    if username_r not in content:
        valid_r = True
        f.write(f"\n{username_r}, {password_r}")
        f.close()
        
    if username_r in content:
        while not valid_r:
            print("\nSorry, this username is already registered.\nPlease enter another username.\n")
            username_r = input("Username:\n")
            password_r = input("\nPassword:\n")
            if username_r not in content:
                valid_r = True
                f.write(f"\n{username_r}, {password_r}")
                f.close()

               
#3.) "add_task()" allows users to add a new task to the system.
#    Variable "current" is assigned its global value (i.e. the current date and year - see main program below).
#    The user is requested to enter task details (the user the task is to be assigned to, the task title, task description, due date, and completion status - 
#    stored as "username_a", "title", "describe", "due", and "complete" respectively).
#    All task details are written to text file "tasks.txt":

def add_task():
    
    global current
    
    username_a = input("\nPlease enter the username of the person you wish to assign the task to:\n")
    title = input("\nPlease enter the task title:\n")
    describe = input("\nPlease enter the task description:\n")
    due = input("\nPlease enter the task due date:\n")
    complete = "No"
    
    f = open("tasks.txt", "r+")
    f.read()
    f.write(f"\n{username_a}, {title}, {describe}, {current}, {due}, {complete}")
    f.close()


#4.) "view_all()" allows users to view all tasks currently on the system.
#    A Notification message is displayed, text file "tasks.txt" is opened, and read line for line (Hyperiondev, 2021, Working with External Data Sources - Input, p.3).
#    For each line (i.e. task) in "tasks.txt", that line is split into a list of details "line_list" (commas and spaces removed -  Hyperiondev, 2021, String Handling, p.3).
#    Using list indexing (Hyperiondev, 2021, The String Data Type, p.5-6), each detail in "line_list" is stored as a "va" variable,
#    and then displayed using triple quotations to make writing/formatting easier (Hyperiondev, 2021, The String Data Type, p.2):

def view_all():
    
    print("\n\nHere is a summary of all tasks:")
    
    with open("tasks.txt", "r+") as f:
        for line in f:
            line_list = line.split(", ")
            username_va = line_list[0]
            task_va = line_list[1]
            describe_va = line_list[2]
            assigned_va = line_list[3]
            due_va = line_list[4]
            complete_va = line_list[5].strip("\n")

            print(f"""-----------------------------------------------------------------------------

Task:\t\t\t\t\t{task_va}
Assigned to:\t\t\t\t{username_va}
Date assigned:\t\t\t\t{assigned_va}
Due date:\t\t\t\t{due_va}
Task Complete?\t\t\t\t{complete_va}
Task Description:
  {describe_va}

-----------------------------------------------------------------------------""")

#(Note: the triple quotation string above appears to be incorrectly indented, but is not. This is because a triple-quotation string will display exactly as it is written,
#i.e. indenting the body of the string will indent it on the display. We want it left-aligned on the display, thus we should align it left in the code.
#The position of the "print" funtion should still be properly indented though - in this case inside the "for line in f:" statement.)


#5.) "view_mine()" allows a user to view all the tasks assigned to them. 
#    Global variables "menu", "edit_gate", "username", "task_list", and "number_list", are used.
#    Text file "tasks.txt" is read and its content stored as "content"
#    If "username" (the username the user used to log in) is in "content" (i.e. if the user has tasks assigned to them),
#    a notification is displayed, and two empty lists created ("task_list" and "number_list").
#    For every line (i.e. task) in "tasks.txt", that line is split into list "line_list" (commas and spaces are removed).
#    If the task is assigned to the user (username equals the first index of "line_list"),
#    the last index of "line_list" is stripped of its new-line character (Hyperiondev, 2021, String Handling, p.3),
#    and the entire "line_list" added to list of lists "task_list" (Hyperiondev, 2021, Beginner Data Structures - The List, p.4):

def view_mine():
    
    global menu
    global edit_gate
    global username
    global task_list
    global number_list
        
    f = open("tasks.txt", "r+")
    content = f.read()
    f.close()
    
    if username in content:
        print("""\n\nHere is a summary of all your tasks.""")
        task_list = []
        number_list = []
        with open("tasks.txt", "r+") as f:
            for line in f:
                line_list = line.split(", ")                  
                if username in line_list[0]:
                    line_list[5] = line_list[5].strip("\n")
                    task_list.append(line_list)
                    
#    After iterating through the lines, "task_list" is enumerated (starting at number "1") (Agrawal, 2020, Geeksforgeeks.org, Enumerate() in Python, t.ly/XGPM).
#    For each number and task in enumerated "task_list", the number is added to "number_list",
#    and each task's number and details are displayed using indexing, f-string, and triple quotations.
#    Last, Boolean "edit_gate" becomes true ("edit_gate" gives access to "edit_gate_func()" in the main program below).
#    (Note: we cant store "enumerate(task_list, 1)" as a variable, hence "number_list" is required to store the numbers which will be used in "edit_gate_func()"):

        for num,task in enumerate(task_list, 1):  
            number_list.append(str(num))
            
            print(f"""-----------------------------------------------------------------------------

Task {num}:\t\t\t\t\t{task[1]}
Assigned to:\t\t\t\t{task[0]}
Date assigned:\t\t\t\t{task[3]}
Due date:\t\t\t\t{task[4]}
Task Complete?\t\t\t\t{task[5]}
Task Description:
  {task[2]}

-----------------------------------------------------------------------------""")
        edit_gate = True

#   If the user's username is not in "content" (i.e. the user has no tasks), a notification is displayed,
#   and the user is asked whether they would like to go back to the main menu ("-1") or quit ("e")(input stored as "notask_choice").
#   If the user selects "-1", "menu" becomes true, and the main program loops back to the main menu.
#   if the user selects "e", the program is exited:

    if username not in content:
            
        print(f"""\n-----------------------------------------------------------------------------
You have no current tasks.
-----------------------------------------------------------------------------""")

        notask_choice = input("Please enter '-1' to go back to the main menu, or press 'e' to exit.\n")
        if notask_choice in ("-1"):
            menu = True
        if notask_choice in ("e", "E"):
            exit()
        

#6.) "edit_gate_func()" allows the user to choose a task they wish to edit, and prevents them from editing a task that has already been completed.
#    Global variables "menu", "edit_gate", "edit", "task_list", "number_list", and "chosen task" are used.
#    While "edit_gate" is true: the user requested to enter the number of the task they wish to edit, or press "-1" to go back to the main menu (input stored as "edit_vm").
#    If "edit_vm" does not equal "-1" or a number stored in "number_list", an error message is displayed, and the user requested again.
#    If "edit_vm" equals "-1", "edit_gate" becomes false, "menu" becomes true, and the main program loops back to the main menu.
#    If "edit_vm" equals a number in "number_list", "task_list" is enumerated and looped through again,
#    and if "edit_vm" equals the task number, that task is stored as "chosen_task".
#    If the chosen task has already been completed (its last index == "Yes"), a notification is displayed, and the user can choose "-1" to go back to the main menu,
#    or "y" to choose another task ("edit_gate" then loops back to its start)(note: we don't need "if "y"" because it is the only option excluded by the other two if statements).
#    If neither "-1" or "y" are entered, "edit_gate" becomes false and "invalid_command" becomes true.
#    While "invalid_command" is true, an error message is displayed, and the user can enter "-1" to go back to the main menu, or "y" to go back to the start of the "edit_gate" loop.
#    If the chosen task has not been completed (its last index == "No"), "edit_gate" becomes false (loop is exited), and "edit" becomes true.
#    The main program will then run "edit_task()" function:

def edit_gate_func():
    
    global menu
    global edit_gate
    global edit
    global task_list
    global number_list  
    global chosen_task
    
    while edit_gate:
        edit_vm = input("""\nPlease enter the number of the task you wish to edit,
or enter '-1' to go back to the main menu.\n""")
        
        if edit_vm != "-1" and edit_vm not in number_list:            
            print("\nError - invalid task number.")
        if edit_vm == "-1":            
            edit_gate = False
            menu = True
            
        if edit_vm in number_list:
            for num,task in enumerate(task_list, 1):
                if num == int(edit_vm):
                    chosen_task = task
                    
                    if chosen_task[5] == "Yes":                        
                        edit_vm_again = input("""\nThis task has already been completed.                   
Please enter 'y' to edit another task, or enter '-1' to go back to the main menu.\n""")
                        if edit_vm_again == "-1":
                            edit_gate = False
                            menu = True                          
                        if edit_vm_again != "-1" and edit_vm_again not in ("y", "Y"):
                            edit_gate = False
                            invalid_command = True
                            
                            while invalid_command:
                                edit_vm_again = input("""Error - invalid command.
Please enter 'y' to edit another task, or enter '-1' to go back to the main menu.""")
                                if edit_vm_again == "-1":
                                    invalid_command = False
                                    menu = True
                                if edit_vm_again in ("y", "Y"):
                                    invalid_command = False
                                    edit_gate = True

                    if chosen_task[5] == "No":
                        edit_gate = False
                        edit = True


#7.) "edit_task()" allows users to mark a task as complete, to change the user the task is assigned to, or to change the due date of the task.
#    Parameters "x" and "y" are used, where "x" equals the index number (i.e. task detail) of "chosen_task" (global "chosen_task"),
#    and "y" equals the value that index "x" is to be replaced by. 
#    The list "chosen_task" is joined into a string "task_string" (commas and spaces inserted between elements)(Hyperiondev, 2021, String Handling, p.3)
#    "chosen_task" index "x" is replaced by "y", and joined into string "new_line" (again commas and spaces are inserted).
#    Text file "tasks.txt" is opened, read, and contents stored as a list of lines "lines" (W3Schools.com, 2021, Python File readlines() Method, t.ly/IVic)
#    For every line (i.e. task) in list "lines", if the line stripped of its new-line character equals "task_string" (i.e. if the task equals the chosen task),
#    the list index of that line is found and stored as "indx" (Striver, 2020, Geeksforgeeks.com,  Python list | index(), t.ly/X95u).
#    If the line is the last line in "lines" (index -1), the line at index "indx" is replaced by the "new_line" string (no "\n" needed - these are added when adding new tasks).
#    Else, the line at index "indx" is replaced by the "new_line" string and a new-line character (to keep lines seperated when overwriting to the text file).
#    Last, "tasks.txt" is opened again and "lines" written to file (W3schools.com, 2021, Python File writelines() Method, t.ly/qqow):

def edit_task(x, y):
    
    global chosen_task

    task_string = (", ".join(chosen_task))
    chosen_task[x] = y
    new_line = (", ".join(chosen_task))
    
    with open("tasks.txt", "r+") as f:
        lines = f.readlines()                            
        for line in lines:
            if line.strip("\n") == task_string:
                indx = lines.index(line)               
                if line == lines[-1]:
                    lines[indx] = new_line
                else:
                    lines[indx] = new_line + "\n"
                                            
    f = open("tasks.txt", "w")
    f.writelines(lines)
    f.close()

       
#8.) "gen_rep()" allows admin to generate reports about user and tasks statistics, which are written to two separate text files.
#    Global "x" is used ("x" equals the current date and year), as well  as counter variables "taskcounter", "complt_tasks", "incomplt_tasks", and "incomplt_ovrdue" - all set to zero)
#    Text file "tasks.txt" is opened. For every line (i.e. task), "taskcounter" increases by one,
#    and the line is split into list "line_list" (commas and spaces removed). If the task is complete ("line_list" index 5 == "Yes"), "complt_tasks" increases by one.
#    If the task is incomplete ("line_list" index 5 == "No"), "incomplt_tasks" increases by one, and the due date is checked:
#    "line_list" index 4 (i.e. the due date) is converted to a datetime object and stored as "due_date" (Tutorialspoint.com, 2021, Python time strptime() Method, t.ly/9yoE).
#    If current date "x" is greater than "due_date", the task is overdue (iharshwardhan, 2018, Geeksforgeeks.com, Comparing dates in Python, t.ly/JiiD),
#    and "incomplt_ovrdue" increases by one.
#    The percentage of incomplete and overdue tasks are found (stored as "perct_incomplt" and "perct_ovrdue"), and rounded off to two decimals.
#    Finally, "task_overview.txt" is opened (or created if it doesn't exist), and the statistics written to file:

def gen_rep():
    
    global x 
    taskcounter = 0
    complt_tasks = 0
    incomplt_tasks = 0
    incomplt_ovrdue = 0
    
    with open("tasks.txt", "r+") as f:
        for line in f:
            taskcounter += 1
            line_list = line.split(", ")
            
            if line_list[5].strip("\n") == "Yes":
                complt_tasks += 1
            if line_list[5].strip("\n") == "No":
                incomplt_tasks += 1
                due_date = datetime.datetime.strptime(line_list[4], "%d %b %Y")  
                if x > due_date: 
                    incomplt_ovrdue += 1
                    
    perct_incomplt = round((incomplt_tasks/taskcounter)*100 ,2)
    perct_ovrdue = round((incomplt_ovrdue/taskcounter)*100, 2)
    
    with open("task_overview.txt", "w") as f:
        f.write(f"""Total tasks:\t\t\t\t\t\t{taskcounter}
Complete tasks:\t\t\t\t\t\t{complt_tasks}
Incomplete tasks:\t\t\t\t\t{incomplt_tasks}
Incomplete overdue tasks:\t\t\t\t{incomplt_ovrdue}
Percentage incomplete tasks:\t\t\t\t{perct_incomplt} %
Percentage incomplete overdue tasks:\t\t\t{perct_ovrdue} %""")
        
#    For user statistics, "usercounter" is set to zero and empty list "user_data_list" created.
#    Text file "user.txt" is opened and for every line (i.e. user), one is added to "usercounter",
#    and counter variables, "user_tasks", "user_complt_tasks", "user_incomplt_tasks", and "user_incomplt_ovrdue" are set to zero (they will thus be set to zero again for each user).
#    The line is split into a list "line_list", and "tasks.txt" is opened. For every line (i.e. task) in "tasks.txt":
#    the line is split into a list "line_list_2", and if "line_list_2" index 0 equals "line_list" index 0 (i.e. the task is assigned to the user), one is added to "user_tasks"
#    If the task has been completed ("line_list_2" index 5 == "Yes"), "user_complt_tasks" increases by one.
#    If the task has not been completed ("line_list_2" index 5 == "No"), "user_incomplt_tasks" increases by one.
#    If the current date "x" is larger than the due date of the incomplete task, "user_incomplt_ovrdue" increases by one:

    usercounter = 0
    user_data_list = []
    
    with open("user.txt", "r+") as f:
        for line in f:
            usercounter += 1
            user_tasks = 0
            user_complt_tasks = 0
            user_incomplt_tasks = 0
            user_incomplt_ovrdue = 0
            line_list = line.split(", ")
            
            with open("tasks.txt", "r+") as f2:
                for line in f2:
                    line_list_2 = line.split(", ")
                    
                    if line_list_2[0] == line_list[0]:
                        user_tasks += 1
                        
                        if line_list_2[5].strip("\n") == "Yes":
                            user_complt_tasks += 1
                        if line_list_2[5].strip("\n") == "No":
                            user_incomplt_tasks += 1
                            due_date = datetime.datetime.strptime(line_list_2[4], "%d %b %Y")  
                            if x > due_date: 
                                user_incomplt_ovrdue += 1

#    If, after iterating through "tasks.txt", "user_tasks" is zero (i.e. the user has no tasks), the statistics are added to "user_data_list".
#    Else, the percentage of the total tasks assigned to the user, and the percentage of completed, incomplete, and overdue user tasks are calculated, rounded of to two decimals
#    (stored as "user_perct_tasks", "user_perct_complt", "user_perct_incomplt", and "user_perct_incomplt_ovrdue" respectively), and added to "user_data_list":

            if user_tasks == 0:
                user_data_list.append(f"""------------------------------------------------------------------
User:\t\t\t\t\t\t\t{line_list[0]}
Total tasks:\t\t\t\t\t\t{user_tasks}
------------------------------------------------------------------\n""")
            else:
                user_perct_tasks = round((user_tasks/taskcounter)*100, 2)
                user_perct_complt = round((user_complt_tasks/user_tasks)*100, 2)
                user_perct_incomplt = round((user_incomplt_tasks/user_tasks)*100, 2)
                user_perct_incomplt_ovrdue = round((user_incomplt_ovrdue/user_tasks)*100, 2)
                
                user_data_list.append(f"""------------------------------------------------------------------
User:\t\t\t\t\t\t\t{line_list[0]}
Total tasks:\t\t\t\t\t\t{user_tasks}
Percentage of all tasks:\t\t\t\t{user_perct_tasks} %
Percentage of user tasks completed:\t\t\t{user_perct_complt} %
Percentage of user tasks incomplete:\t\t\t{user_perct_incomplt} %
Percentage of user tasks incomplete & overdue:\t\t{user_perct_incomplt_ovrdue} %
------------------------------------------------------------------\n""")            

#    After iterating through all the users in "user.txt", "user_overview.txt" is opened (or created if it doesn't exist),
#    and the total number of users and tasks ("usercounter" and "taskcounter"), as well as every user in "user_data_list", written to "user_overview.txt":
                 
    with open("user.overview.txt", "w") as f:
        f.write(f"""Total users:\t\t\t\t\t\t{usercounter}
Total tasks:\t\t\t\t\t\t{taskcounter}\n""")
        for user in user_data_list:
            f.write(user)


#9.) "view_stats()" allows admin to display the stats generated via "gen_rep()" on screen.
#    Text file "task_overview.txt" is opened, read, and content stored as list "lines".
#    Using list indexing, the total number of tasks  ("lines" index 0), and task statistics  ("lines" indexes 1 to 5, joined as string without seperators),
#    are found and stored as "total_tasks" and "task_stat_string" respectively.
#    Similarly, "user_overview" is openend, read, and stored as "lines2".
#    The total number of users ("lines2" index 0), and individual users statistics ("lines2" indexes 2 to last, joined as a string without seperators),
#    are found and stored as "total_users" and "user_stat_string" respectively.
#    Finally, the new variable values are displayed:

def view_stats():
    
    f = open("task_overview.txt", "r+")
    lines = f.readlines()
    total_tasks = lines[0].strip("\n")
    task_stat_string = ("".join(lines[1:6]))
    f.close()
    
    f2 = open("user.overview.txt", "r+")
    lines2 = f2.readlines()
    total_users = lines2[0].strip("\n")
    user_stat_string = ("".join(lines2[2:]))
    f2.close()
    
    print(f"""\n
{total_users}
{total_tasks}
{task_stat_string}\n
{user_stat_string}""")





#Main program:

#Datetime module is imported and current date and time "x" stored (W3schools.com, 2021, Python Datetime, t.ly/TDG4)
#"strftime" is used to convert datetime object "x" to string "current" which stores the current day, month (abbreviated) and year (PsPranav, 2019, Stackoverflow.com, t.ly/Cic4):
    
import datetime
x = datetime.datetime.now()
current = (x.strftime("%d") + " " + x.strftime("%b") + " " + x.strftime("%Y"))

#Control variables are set to their default values:

valid = False
menu = False
edit_gate = False
edit = False
username = ""
password = ""
choice = ""
edit_choice = ""
edit_choice2 = ""
task_list = []
number_list = []
chosen_task = []


#Login screen() funciton is called. If the login details are valid ("valid" == True), "menu" becomes true.
#While menu is true, if the user is an admin, the admin main menu is displayed (admin selection stored as "choice")
#Else (if the user is not an admin), the normal main menu is displayed (user selection also stored as "choice"):

login_screen()
if valid:
    menu = True
    while menu:
        if username in ("admin", "Admin", "ADMIN"):
            
            choice = input(f"""\nPlease select one of the following options:
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    gr - generate reports
    vs - view stats    
    e - exit\n""")
        else:
            choice = input(f"""\nPlease select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit\n""")

#For all user choices, "menu" changes to false (to exit the loop), and depending on the choice, the corresponding function is called:
            
        if choice in ("r","R"):
            menu = False
            reg_user()            
        if choice in ("a", "A"):
            menu = False
            add_task()            
        if choice in ("va", "Va", "VA"):
            menu = False
            view_all()            
        if choice in ("vm", "Vm", "VM"):
            menu = False
            view_mine()
            
#If the user chooses to view their own tasks ("choice" in "vm") and they have tasks assigned to them, "edit_gate" becomes true and "edit_gate_func()" is called.
#If the task the user wants to edit (selected in "edit_gate_func()") is incomplete, "edit" becomes true, and the user can choose to mark the task complete ("mc") or edit the task ("et").
#If the user selects "et", an edit submenu is displayed and the user can choose to change the username the task is assigned to ("cu"), or change the task due date ("cd").
#In all three options "mc", "cu", and "cd", the same function "edit_task()" is called, but using different parameters (each time a different task element is changed):
            
            if edit_gate:
                edit_gate_func()  
            if edit:
                edit_choice = input("""\nPlease select an option below:
mc - mark the task as complete
et - edit the task\n""")
                if edit_choice in ("mc", "Mc", "MC"):
                    edit_task(5, "Yes")
                if edit_choice in ("et", "Et", "ET"):
                    edit_choice_2 = input("""\nPlease select an edit option below:
    cu - change username 
    cd - change due date\n""")
                    if edit_choice_2 in ("cu", "Cu", "CU"):
                        edit_task(0, input("\nPlease enter a new username to assign the task to:\n"))
                    if edit_choice_2 in ("cd", "Cd", "CD"):
                        edit_task(4, input("\nPlease enter a new due date:\n"))

        if choice in ("gr", "Gr", "GR"):
            menu = False
            gen_rep()                                       
        if choice in ("vs", "Vs", "VS"):
            menu = False
            gen_rep()
            view_stats()
        if choice in ("e", "E"):
            menu = False
            exit()

#Note: The stats displayed when the user chooses "vs" are read from the reports generated via "gen_rep()" when the user chose "gr".
#In case the user wants to view stats, but the reports are not generated yet (i.e. user has not selected "gr" first), the "gen_rep()" function is called first.
#This is a much simpler solution than trying to programatically find the Dropbox shared folder path on a remote computer using JSON files, or searching the entire file system
#(c00kiemonster, 2012, Stackoverflow.com, How to determine the Dropbox folder location programmatically?, t.ly/OjRT).





############################ THE END ###############################




          
            
    
