
#Created start function to better organize the code
def start():
    #greeted user and collected name and age
    print("Hello User!, I am the Elite 101 Chat Bot")
    name = input("What is your name? ----> ")
    age = int(input("How old are you? ----->"))
    #communicated with user by using name and age
    print(f'Hey {name}, how awesome is it to be {age}')
    #asked user to choose an option
    print("How can I help you? Please choose an option")
    #displayed the options using the options function
    options()
    #gathered the user's choice
    option = int(input())
    #good bye message to the user
    print(f'Thank you {name} for using this program!')

def options():
    #printed the options using \n
    print("1. Blank Option\n2. Blank Option\n3. Blank Option\n4. Exit Conversation")
#called start command to begin code
start()