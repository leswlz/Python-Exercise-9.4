import pickle
import time

f_name = "notebook.dat"
data = []

try:
    f = open(f_name,"rb")
    f.close()
except IOError:
    f = open(f_name,"wb")
    print("No default notebook was found, created one.")
    f.close()

try:
    with open(f_name, 'rb') as f:
        data = pickle.load(f)
except Exception:
    with open(f_name, 'wb') as f:
        pickle.dump(data, f)
    with open(f_name, 'rb') as f:
        data = pickle.load(f)

keep_going = True

while keep_going:
    print("(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit")
    action_number = input("\nPlease select one: ")
    if action_number == "1":
        for i in data:
            print(i)
        continue
    if action_number == "2":
        added_text = input("Write a new note: ")
        added_text = added_text + ":::" + time.strftime("%X %x")
        data.append(added_text)
        continue
    if action_number == "3":
        print("The list has ",len(data)," notes.")
        changed_string = int(input("Which of them will be changed?: "))
        if changed_string >= 0 and changed_string < len(data):
            print(data[changed_string])
            new_string = input("Give the new note: ")
            data[changed_string] = new_string + ":::" + time.strftime("%X %x")
        else:
            print("Incorrect selection.")
        continue
    if action_number == "4":
        print("The list has ",len(data)," notes.")
        deleted_string = int(input("Which of them will be deleted?: "))
        if deleted_string >= 0 and deleted_string < len(data):
            print("Deleted note",data[deleted_string])
            data.pop(deleted_string)
        else:
            print("Incorrect selection.")
        continue
    if action_number == "5":
        print("Notebook shutting down, thank you.")
        with open(f_name, 'wb') as f:
            pickle.dump(data, f)
        break
    else:
        print("Incorrect selection")
        continue
