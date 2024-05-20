Group 14 Ground Rules

We will use Microsoft Teams as our main method of day-to-day communication and will expect replies within 24 hours unless unavailability has been previously discussed. 
For any group work, we can assign tasks to each member to ensure work is being evenly divided among ourselves. 
Respectful communication, speaking respectfully and being open-minded
Effective collaboration, contributing fairly, meeting deadlines, and management of time effectively.
Clear communication, staying positive, supportive, and civil 
Give any constructive feedback/suggestions with nonjudgmental language 
If a team member is confused about a task, communicate to clear confusion and ask questions to have a better understanding.

Requesting Data from the Microservice

To programmatically request data from the microservice, you need to call the main function with the path to the input text file containing the list of items. The list of items need to be put into the list with each item in a separate line. 
For example:
IV bags
Gauze
Gloves
The main function will prompt the user for their name and the quantities of each item, then overwrite the input file with th3e formatted email message.

Example Code:

input_file = 'items.txt' 
main(input_file)

Receiving Data from the Microservice

After calling the microservice and providing the necessary inputs, the service will process the data and write the formatted email message back into the same input text file. 

Example Code:
with open('items.txt', 'r') as file:
    formatted_message = file.read()
    print(formatted_message)

