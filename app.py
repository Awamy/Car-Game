co_help = 'help'
co_start = 'start'
co_stop = 'stop'
co_exit = 'exit'
counter = 0

while counter == 0:
    command = input('>')
    if command.lower() == co_help:
        print('''start - to start the car
stop - to stop the car
exit - to quit game''')
    elif command.lower() == co_start:
        print("car started")
    elif command.lower() == co_stop:
        print("Car Stopped")
    elif command.lower() == co_exit:
        break
    else:
        print("i can't understand")