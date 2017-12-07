#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

print("You must click on search bar and press enter to take you to your desired")
food = input("Enter a food place in that area:")
webbrowser.open('https://www.google.com/maps/place/' + address + ', ' + food)