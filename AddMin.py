# AddMin.py
# Author: Jeff Davies
# License: CC0 - No attribution required

from datetime import datetime, timedelta

def time_to_minutes():
    # Prompt the user for input
    time_input = input("Enter the job time in hh:mm format: ")
    
    # Split the input into hours and minutes
    hours, minutes = map(int, time_input.split(':'))
    
    # Convert hours to minutes and add the minutes
    total_minutes = hours * 60 + minutes
    
    return total_minutes

total_minutes = 1

while total_minutes > 0:
    # Call the function and print the result
    total_minutes = time_to_minutes()
    print(f"The total number of minutes is: {total_minutes}")


    if total_minutes > 0:
        # Get the current datetime
        current_datetime = datetime.now()

        # Add the specified number of minutes to the current datetime
        new_datetime = current_datetime + timedelta(minutes=total_minutes)
        formatted_date_time = new_datetime.strftime("%Y-%m-%d %H:%M")

        # Display the result
        # print("Current datetime:", current_datetime)
        print("Job completes:", formatted_date_time)
print("Done!")
