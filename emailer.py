def prompt_user_name():
    """Prompt the user to input their name."""
    return input("Please enter your name: ")

def read_items_from_file(input_file):
    """Read the list of items from the input text file."""
    with open(input_file, 'r') as file:
        items = file.readlines()
    # Strip newline characters from each item
    items = [item.strip() for item in items]
    return items

def prompt_for_quantities(items):
    """Prompt the user for quantities of each item."""
    quantities = {}
    for item in items:
        while True:
            try:
                quantity = int(input(f"How many of {item} do you need? "))
                quantities[item] = quantity
                break
            except ValueError:
                print("Please enter a valid number.")
    return quantities

def format_email_message(user_name, quantities):
    """Format the email message with the user's name and list of items with quantities."""
    message = f"Hello,\n\nHere are the items I need:\n"
    for item, quantity in quantities.items():
        message += f"- {item}: {quantity}x\n"
    message += f"\nBest regards,\n{user_name}"
    return message

def write_message_to_file(output_file, message):
    """Write the formatted message to the output text file."""
    with open(output_file, 'w') as file:
        file.write(message)

def main(input_file):
    """Main function to read items, prompt for quantities, format the message, and overwrite the file."""
    user_name = prompt_user_name()
    items = read_items_from_file(input_file)
    quantities = prompt_for_quantities(items)
    email_message = format_email_message(user_name, quantities)
    write_message_to_file(input_file, email_message)

# Example 
input_file = 'items.txt'

main(input_file)
