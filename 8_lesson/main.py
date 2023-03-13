from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
        return all_data


def show_all():
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")


def add_new_contact():
    global id
    array['surname', 'name', 'surname_2', 'phone_number']
    string = ''
    for i in array:
        string += input(f'enter {i} ') + ' '
    id += 1

    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f"{id} {string}\n")



def delete_record():
    global all_data
    show_all()
    num = input("enter id: ")
    all_data = [i for i in all_data if i[0] != num]
    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f"{symbol.join(all_data)}\n")



def change_record(old_string, new_string):
    global all_data
    show_all()
    old_string = input("enter the data you want to change: ")
    new_string = input("enter new data: ")
    with open(file_base, encoding="utf-8") as f:
        s = f.read()
    with open(file_base, 'w', encoding="utf-8") as f:
        print(f"Changing {old_string} to {new_string} in {file_base}".format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)   
    

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Delete\n"
                       "4. Change\n"
                       "5. Exit\n")
    match answer:
        case "1":
            show_all()
        case "2":
            add_new_contact()
        case "3":
            delete_record()
        case "4":
            change_record(old_string, new_string)
        case "5":
            play = False
        case _:
            print("Try again!\n")


main_menu()