
def show_welcome_message(name):
    print(f"Welcome to {name}")
    
def greet_reader(name):
    print(f"Hello {name}. How can I help you today?")

def show_main_menu(options_list):

    option_num = 0
    for option in options_list:
        option_num += 1
        print(f"{option_num}. {option}")