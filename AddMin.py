# AddMin.py
# Author: Jeff Davies
# License: CC0 - No attribution required
import pyperclip
from datetime import datetime, timedelta

def time_to_minutes():
    # Prompt the user for input
    time_input = input("Enter the job time in hh:mm format: ")
    
    # Split the input into hours and minutes
    hours, minutes = map(int, time_input.split(':'))
    
    # Convert hours to minutes and add the minutes
    total_minutes = hours * 60 + minutes
    
    return total_minutes

def show_help():
    print("**********************************************")
    print("* Enter the job duration to get the date and *")
    print("* time the job completes.                    *")
    print("* Use the format hh:mm. For example: 15:12   *")
    print("* Enter the time as 0:0 to quit the program. *")
    print("**********************************************\n")

total_minutes = 1
show_help()

while total_minutes > 0:
    # Call the function and print the result
    total_minutes = time_to_minutes()

    if total_minutes > 0:
        # Get the current datetime
        current_datetime = datetime.now()

        # Add the specified number of minutes to the current datetime
        new_datetime = current_datetime + timedelta(minutes=total_minutes)
        formatted_date_time = new_datetime.strftime("%Y-%m-%d %H:%M")

        pyperclip.copy(formatted_date_time)

        # Display the result
        # print("Current datetime:", current_datetime)
        print(f"Job completes: {formatted_date_time}")
        print("Copied to clipboard!")
print("Done!")
