from items import stock  # Importing the `stock` variable from an external module `items`
from nrclex import NRCLex  # Importing the NRCLex library for text-based emotion analysis
import nltk  # Importing nltk for natural language processing tasks
nltk.download('punkt_tab')  # Downloading the 'punkt_tab' tokenizer (for tokenizing text into sentences/words)

# Created start function to better organize the code
def start(stock):
    """
    Main function to greet the user, interact with them, and handle their menu choices.
    :param stock: A list of stock items representing the inventory.
    """
    # Greeted user and collected name and age
    print("Hello User!, I am the Elite 101 Chat Bot")
    name = input("What is your name? ----> ")  # Collect user's name
    age = int(input("How old are you? ----->"))  # Collect user's age
    # Communicated with user by using name and age
    print(f'Hey {name}, how awesome is it to be {age}')
    # Asked user to choose an option
    print("How can I help you? Please choose an option")
    # Displayed the options using the options function

    # Gathered the user's choice
    option = 0  # Initialize option to enter the loop
    while option != 5:  # Continue until user selects "Exit the Program"
        options()  # Display menu options
        option = int(input())  # Gather user input for the chosen option
        if option == 1:
            instructions()  # Display program instructions
        elif option == 2:
            customer_return(stock)  # Handle item return
        elif option == 3:
            customer_exchange(stock)  # Handle item exchange
        elif option == 4:
            write_review()  # Allow the user to write a review
        else:
            break  # Exit the loop when option 5 is selected
    print(f'Thank you {name} for using this program!')  # Thank the user on exit

def options():
    """
    Function to display program menu options.
    """
    # Printed the options using \n for better formatting
    print("1. Program Instructions\n2. Return\n3. Exchange\n4. Review\n5. Exit the Program")

def instructions():
    """
    Function to display program instructions to the user.
    """
    print("For this program you can return an item by providing the type and price, "
          "you can also exchange your item for an item of less or equal price.")

def customer_return(stock):
    """
    Handles the return of an item by the customer.
    :param stock: A list representing the inventory of items.
    """
    print("Hey! Thank you for returning your item")
    # Gather details about the returned item
    item_type = input("Please input the type of clothing being returned: ")
    item_price = float(input("Please input the price of your item: "))
    # Create a dictionary representing the item
    item = {"name": item_type, "id": 0, "price": item_price}
    item_return(item, stock)  # Add the returned item to the inventory
    print("Your Item has been Returned!")
    print(stock)  # Print the updated stock for verification

def customer_exchange(stock):
    """
    Handles the exchange of an item by the customer.
    :param stock: A list representing the inventory of items.
    """
    print("Hey! Thank you for exchanging your item")
    # Gather details about the exchanged item
    item_type = input("Please input the type of clothing being Exchanged: ")
    item_price = float(input("Please input the price of your item: "))
    item = {"name": item_type, "id": 0, "price": item_price}
    exchangable_items = item_exchange(item, stock)  # Get items eligible for exchange
    if len(exchangable_items) > 0:
        print("Here are the items you can exchange")
        # Display exchangeable items
        for i in range(len(exchangable_items)):
            print(f"{i + 1}. {exchangable_items[i]['name']}")
        item_num = int(input("Please choose an item to exchange for: "))
        # Remove the selected item and add the returned item to stock
        remove_item(exchangable_items[item_num - 1], stock)
        item_return(item, stock)
        print("Your item has been exchanged!")
        print(stock)  # Print updated stock
    else:
        print("There are no items you can exchange for :(")  # Handle no exchangeable items

def item_return(item, stock):
    """
    Adds a returned item to the stock inventory.
    :param item: A dictionary representing the item details.
    :param stock: A list representing the inventory of items.
    """
    item['id'] = stock[len(stock) - 1]["id"] + 1  # Assign a new ID based on the last item's ID
    stock.append(item)  # Append the item to the stock

def item_exchange(item, stock):
    """
    Finds items in the stock eligible for exchange.
    :param item: A dictionary representing the exchanged item's details.
    :param stock: A list representing the inventory of items.
    :return: A list of items eligible for exchange.
    """
    exchangable_items = []
    for i in range(len(stock)):
        if stock[i]["price"] <= item["price"]:  # Check if item's price is less than or equal
            exchangable_items.append(stock[i])  # Add eligible items to the list
    return exchangable_items

def remove_item(item, stock):
    """
    Removes an item from the stock inventory.
    :param item: A dictionary representing the item's details to remove.
    :param stock: A list representing the inventory of items.
    """
    for i in range(len(stock)):
        if stock[i]["id"] == item["id"]:  # Match item by its unique ID
            stock.pop(i)  # Remove the item from stock
            break

def write_review():
    """
    Allows the user to write a review and analyzes the emotion using NRCLex.
    """
    review = input("Hey! Please input your review: ")
    text_object = NRCLex(review)  # Analyze the review for emotions
    emotions = text_object.top_emotions  # Extract the top emotions
    print("Thanks for writing a review")
    print(emotions)  # Display the detected emotions
    return emotions

# Called start command to begin code execution
start(stock)
