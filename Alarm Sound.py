import time
import winsound

def alarm():
    frequency = 2500 
    duration = 2000 
    winsound.Beep(frequency, duration)

def stopwatch():
    start_time = time.time()
    print("Stopwatch has been started")
    print("Press 'Enter' to stop.")
    input()
    
    end_time = time.time()
    stop_time = end_time - start_time
    
    print("Stop time: {:.2f} seconds".format(stop_time))
    alarm()

def display_current_time():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print("Current time:", current_time)

def set_alarm():
    alarm_time = input("Set the alarm time (format: HH:MM:SS): ")
    
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        
        if current_time == alarm_time:
            print("Alarm time reached!")
            alarm()
            break

while True:
    print("\n1. Start Stopwatch")
    print("2. Display Current Time")
    print("3. Set Alarm")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        stopwatch()
    elif choice == "2":
        display_current_time()
    elif choice == "3":
        set_alarm()
    elif choice == "4":
        print("Exiting the program...")
        alarm()
        break
    else:
        print("Invalid choice. Please try again.")
