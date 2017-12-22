import pickle
running = True



phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 15, "phone_number": "+380501234567", "city": "Odessa"},
              {"name": "Ivan", "surname": "Ivanov", "age": 50, "phone_number": "+380507654321", "city": "Kiev"},
              {"name": "Daria", "surname": "Domanina", "age": 18, "phone_number": "+380507885397", "city": "Odessa"}
             ]


def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    print ("| City:    %20s |" % entry["city"])
    print ()


def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()
    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1



def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number   = input("    Enter phone num.: ")
    city = input("    Enter city: ")


    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    entry["city"] = city
    phone_book.append(entry)





def printError(message):
    print ("ERROR: %s" % message)


def printInfo(message):
    print ("INFO: %s" % message)


def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


def find_entry_age_phonebook():
    age = int(input("   Enter age: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


def delete_entry_name_phonebook():
    name = str(input("Enter name which you want to delete from your phone - book: "))
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            phone_book.remove(entry)
            found = True
    if not found:
        printError("Not found!!")


def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))


def print_phonebook_by_age():
    print("by age")
    for i in range(len(phone_book) - 1):
        if phone_book[i]["age"] < phone_book[i + 1]["age"]:
            temp = phone_book[i+1]
            phone_book[i + 1] = phone_book[i]
            phone_book[i] = temp
    print_phonebook()


def increase_age():
    value_of_years = int(input("Enter value of years that you want to plus: "))
    for entry in phone_book:
        entry["age"] += value_of_years
    print_phonebook()


def avr_age_of_all_persons():
    sum_of_all_ages = 0
    value_of_persons = 0
    for entry in phone_book:
        sum_of_all_ages += entry["age"]
        value_of_persons += 1
    average_age = round(sum_of_all_ages / value_of_persons, 1)
    print(average_age)


def print_entry_by_city_and_value_of_people_in_town():
    your_town = str(input("Enter town from which you want to find people: "))
    found = False
    idx = 1
    value_of_people = 0
    for entry in phone_book:
        if entry["city"] == your_town:
            value_of_people += 1
            print_entry(idx, entry)
            idx += 1
            found = True
    print("Value of people in %s = %d" %(your_town, value_of_people))
    if not found:
        printError("Not found!!!")


def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


def exit():
      global running
      running = False


def print_prompt():
      print()
      print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1 - Print phonebook entries")
      print("     2 - Print phonebook entries (by age)")
      print("     3 - Add new entry")
      print("     4 - Find entry by name")
      print("     5 - Find entry by age")
      print("     6 - Delete entry by name")
      print("     7 - The number of entries in the phonebook")
      print("     8 - Avr. age of all persons")
      print("     9 - Increase age by num. of years")
      print("     10 - Find entry by city and value of people in town")
      print("-----------------------------")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


def main():
    while running:
        try:
            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,
                  '10': print_entry_by_city_and_value_of_people_in_town,

                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }



            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()
        except Exception as ex:
            printError("Something went wrong. Try again...")




if __name__ == '__main__':
    main()