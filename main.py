library_name = "Bailey's Books and Bargains"
librarian = "Anthony"
book_count = 20
is_open = True
checkout_limit = 3

print(f"Welcome to {library_name}")
reader_name = input("What is your name? ")
formatted_name = reader_name.strip().title()

print(f"Hello {formatted_name}.")

if not is_open:
    print("The library is closed.")
    
view_selection = input("Would you like to view our book selection? ")
cleaned_selection_response = view_selection.strip().lower()

if cleaned_selection_response == "yes" or cleaned_selection_response == "y":
    print("Ok, great.")
    requested_books = input("How many books would you like to check out? ")
    requested_books = int(requested_books.strip())

    if requested_books <= checkout_limit and is_open:
        print("Perfect. Let's get you fixed up.")
    else:
        print("Checkout is not available.")
        
        
elif cleaned_selection_response == "no" or cleaned_selection_response == "n":
    print("No worries. Have a nice day!")
else:
    print("Please type yes or no.")

