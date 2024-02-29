print("Write ' help ' to start the program")
command = ""
started = False
while True:
        command = input("> ").lower()
        if command == "start":
            if started:
               print("Car already started")
            else:
                started = True
                print("Car Engine Started")
        elif command == "stop":
            if not started:
                print("Car is already stopped")
            else:
                started = False
                print("Car Engine Stop")
        elif command == "help":
            print("""
            start -- car start
            stop -- car stop
            quit -- end program
            """)
        elif command == "quit":
            break
        else:
            print("Sorry! I don't understand that...!")
