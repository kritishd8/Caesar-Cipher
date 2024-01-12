alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
exit_message = '\nThanks for using the program, goodbye!'
again_message = "\nWould you like to encrypt or decrypt another message? (y/n): "
action_message = '\nWould you like to encrypt (e) or decrypt (d) ?: '

#? Welcome Message
def welcome():
    '''
    Prints the welcome message
        
            Parameters:
                    None
            
            Returns:
                    None
    '''

    print('\nWelcome to the Caesar Cipher.\nThis program encrypts and decrypts text with the Caesar Cipher.')

#? Take inputs
def enter_message(action):   
    '''
    Returns a tuple containing user selected mode, user input message, and shift number

            Parameters:
                    action (str): A single alphabet
            
            Returns:
                    a tuple like: (action, message, shift)
    '''

    if action == 'e':
        message = input('\nWhat message would you like to encrypt: ')
        message = message.upper()
        shift = int(input('What is the shift number: '))

    elif action == 'd':
        message = input('\nWhat message would you like to decrypt: ')
        message = message.upper()
        shift = int(input('What is the shift number: '))

    else:
        print('\nInvalid Mode!! Please select "e" or "d". ')

    return (action, message, shift)

#? Function to encrypt the message
def encrypt(message, shift):
    '''
    Returns encrypted version of the given message using given shift

            Parameters:
                    message (str): The message to encrypt
                    shift (int): An integer
            
            Returns:
                    String containing the encrypted message
    '''

    encrypted = ''

    for letter in message:
        if letter == ' ' or letter == '' or letter == '\n':
            encrypted += letter
        else:
            index = alphabets.index(letter) + shift
            encrypted += alphabets[index]
    
    return f"\n{encrypted}"

#? Function to decrypt the message
def decrypt(message, shift):
    '''
    Returns decrypted version of the given message using given shift

            Parameters:
                    message (str): The message to decrypt
                    shift (int): An integer
            
            Returns:
                    String containing the decrypted message
    '''

    decrypted = ''

    for letter in message:
        if letter == ' ' or letter == '' or letter == '\n':
            decrypted += letter
        else:
            index = alphabets.index(letter) - shift
            decrypted += alphabets[index] 
    
    return f"\n{decrypted}"

#? Take the file and read line by line and encrypt it and store it in a list
def process_file(filename, action):
    '''
    Returns a list after performing the given action on each line with the shift

            Parameters:
                    filename (str): Name of the file
                    action (int): An alphabet
            
            Returns:
                    List containing encrypted/decrypted version of every line from file
    '''

    shift = int(input('What is the shift number: '))
    actioned_list = []
    
    with open(filename) as file:
        length = len(file.readlines())        

    with open(filename) as file:
        for i in range(length):
            if action == 'e':
                actioned_list.append(encrypt(file.readline().upper(), shift))
            elif action == 'd':
                actioned_list.append(decrypt(file.readline().upper(), shift))
    
    return actioned_list

#? Checks if a file exists
def is_file(filename):
    '''
    Returns True if file exists and False if it doesnt exist

            Parameters:
                    filename (str): Name of the file
            
            Returns:
                    Returns a boolean based on if the file exist or not
    '''

    try:
        with open(filename) as f:
            pass
        return True
    except: return False

#? Write encrypted message to a new file
def write_messages(message_list):
    '''
    Writes all the data from the given list to a file name results.txt (creates the file if it doesnt exist)

            Parameters:
                    message_list: The list containing all the content to write to the file
            
            Returns:
                    None
    '''

    if is_file('results.txt'):
        with open('results.txt', 'a') as file:
            for items in message_list:
                file.write(f'{items}\n')
    else:
        with open('results.txt', 'x') as file:
            for items in message_list:
                file.write(f'{items}\n')

#? Console mode or File mode, do appropriate action
def message_or_file():
    '''
    Takes user input for if they want to enter console mode or file mode.

            Parameters:
                    None
            
            Returns:
                    None
    '''

    while 1:
        action = input(action_message).lower()
        if action in ('e', 'd'):
            console = input('\nDo you want to process messages using console or file? (c for console, f for file) ')

            if console == 'f':
                filename = input('\nEnter file name with it\'s extension: ')
                if is_file(filename):
                    try:
                        write_messages(process_file(filename, action))
                        print('\nAction completed successfully.')
                    except: print('\nSome error occured!')
                    break
                else:
                    print('\nFile not found!!\nTry Again!\n')

            elif console == 'c':
                values = enter_message(action)
                return values
                break

            else:
                print('\nInvalid Choice. Please choose "f" or "c"!')
        else:
            print('Invalid Choice. Please choose "e" or "d"!')

def print_result(values):
    '''
    Prints the encrypted/decrypted message

            Parameters:
                    values (str): The tuple containing action, message and shift number
            
            Returns:
                    None
    '''

    if values != None:
        if values[0] == 'e':
            print(encrypt(values[1], values[2]))
        elif values[0] == 'd':
            print(decrypt(values[1], values[2]))

        try_again = input(again_message)
        if try_again == 'n':
            print(exit_message)
        else:
            main()

#? Main function to start the program
def main():
    '''
    Main function to run all other functions in order

            Parameters:
                    None
            
            Returns:
                    None
    '''

    welcome()
    values = message_or_file()
    print_result(values)


#? Start
main()