#
#           Name: main.py
#           Author: Stephen Coyne
#

#Splash Screen Execution
exec(open("splashscreen.py").read())

while True:
    #Loops Player Entry Screen till F5 is pressed
    exec(open("player-entry.py").read())

    #Once 30 second countdown timer is completed, Player Action screen is called
    exec(open("player-action.py").read())

    #DEBUG
    break
