# ReadMe for AddMin.py

## Run the program

Just enter `python AddMin.py` from the command line.

## Using the program

Enter your job duration in the format of hours:minutes. For example, if the job says it completes in 15h and 12 minutes, enter `15:12` at the prompt.
The calculated job delivery time is then copied to your computer's clipboard so you can paste it into the application of your choice.

## Creating the Executable

Use the following command:

`pyinstaller AddMin.py --onefile`

## Dependencies

This program uses pyperclip to enable the clipboard interaction. You may need to install that library to your computer first:
Please see: https://pypi.org/project/pyperclip/