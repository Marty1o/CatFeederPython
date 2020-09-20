from Motor import *
import schedule
import time


def initialization():
    motor = Motor()

    schedule.every().day.at('07:00').do(Motor.runMotor)
    schedule.every().day.at('18:00').do(Motor.runMotor)


def main():
    # Call initilization function
    Motor.runMotor()
    initialization()

    # will loop forever and check if there are any pending tasks.
    while True:
        schedule.run_pending()
        time.sleep(1)


# Call main function
if __name__ == "__main__":
    main()
