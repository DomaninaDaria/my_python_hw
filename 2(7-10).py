print("--------------------------------------------------------")
print("7.1")
print("We have the date in american format is: 07.22.2017")
current_date = "07.22.2017"
lst = current_date.split(".")
lst[0], lst[1] = lst[1], lst[0]
eu_date = ".".join(lst)
print("The date in european format is: ",  eu_date)
print("---------------------------------------------------------")

print("7.2")
lst = current_date.split(".")
print("The date in european format is:  %s.%s.%s  " % (lst[1], lst[0], lst[2]))
print("---------------------------------------------------------")

print("---------------------------------------------------------")
print("8.")
print("We have the  person`s name in this way: Daria Domanina")
current_name = "Daria Domanina"
lst = current_name.split(" ")
print("Now, we have the person`s name in another way: %s %s" % (lst[1], lst[0]))
print("---------------------------------------------------------")

print("---------------------------------------------------------")
print("9.")
print("We have a word in  the snake_style format: life_is_fight")
current_style = "life_is_fight"
lst = current_style.split("_")
another_style = lst[0].title() + lst[1].title() + lst[2].title()
print("Now, we have this word in the CamelizedStyle format: ", another_style)
print("---------------------------------------------------------")


print("---------------------------------------------------------")
print("10.")
print("We have a string: Aleksandr Pushkin*1799-06-06*1837-02-10")
current_string = "Aleksandr Pushkin*1799-06-06*1837-02-10"
lst = current_string.split("*")
name = lst[0]
date_of_birth = lst[1]
date_of_death = lst[2]
lst1 = date_of_birth.split("-")
year_of_birth = lst1[0]
lst2 = date_of_death.split("-")
year_of_death = lst2[0]
age = int(year_of_death) - int(year_of_birth)
print("The information about person is: %s,%d years old" % (name, age))
print("---------------------------------------------------------")


