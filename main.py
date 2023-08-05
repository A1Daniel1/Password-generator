import password as p

def show_commands():
    welcome_message = "Welcome to your password manager!"
    command_info = "Select the command [gc] to create a password.\n" \
                   "Select the command [oc] to get one of your passwords. \n" \
                    "Select the command [exit] to exit the program."
    separator = "-" * 50
    print(f"{welcome_message}\n{separator}\n{command_info}")

def ask(user_input):
    if user_input in ["gc", "oc"]:
        master_key = input("key Master?\n")
        service = input("Name of the service?\n")
        
        if user_input == "gc":
            print(f"The password created to {service.capitalize()} is:\n{p.add_password(service, master_key)}")
        else:
            print(f"Your password to {service.capitalize()} is:\n{p.get_password(master_key, service)}")

def main():
    show_commands()
    while True:
        command = input("select a command ->")

        if command == "exit":
            break
        else:
            ask(command)

main()