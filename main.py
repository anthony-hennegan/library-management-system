library_name = "Bailey's Books and Bargains"
librarian = "Anthony"
book_count = 20
is_open = True

print(f"Welcome to {library_name}")
reader_name = input("What is your name? ")
print(f"Hello {reader_name}.")
view_selection = input("Would you like to view our book selection? ")

if view_selection == "yes":
    print("Ok, here is what we have.")
elif view_selection == "no":
    print("No worries. Have a nice day!")
else:
    print("Please type yes or no.")
