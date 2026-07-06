library_name = "Bailey's Books and Bargains"
librarian = "Anthony"
book_count = 20
is_open = True

print(f"Welcome to {library_name}")
reader_name = input("What is your name? ")
formatted_name = reader_name.strip().title()

print(f"Hello {formatted_name}.")

view_selection = input("Would you like to view our book selection? ")
cleaned_selection_response = view_selection.strip().lower()

if cleaned_selection_response == "yes":
    print("Ok, great.")
    requested_books = input("How many books would you like to check out? ")
    requested_books = int(requested_books)

    if requested_books > 3:
        print("Sorry, you can check out no more than 3 books.")
    else:
        print("Perfect. Let's get you fixed up.")
        
elif cleaned_selection_response == "no":
    print("No worries. Have a nice day!")
else:
    print("Please type yes or no.")

