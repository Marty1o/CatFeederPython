# from Email import *
from Motor import *
import schedule
import time


def initialization():
    motor = Motor()

    schedule.every(1).minute.do(Motor.runMotor)

    '''print("Auto-Cat initializing")
    email = Email(465, 'catfeederprojectpie@gmail.com', 'none at the moment')
    # motor = Motor(21, 50, 5)
    # schedule.every(1).minutes.do(email.sendEmail,'martin.c.842@gmail.com','This is a test')
    email.sendEmail('martin.c.842@gmail.com', 'This is a test!!')
    # schedule.every(1).minutes.do(motor.feed, 10, 5)
    # Add any other initializing components here
    print("Auto-Cat initializing complete")'''

def helloWorld():
    print("hi hi hi")

def main():
    # Call initilization function
    initialization()

    # will loop forever and check if there are any pending tasks.
    while True:
        print('System is running')
        schedule.run_pending()
        time.sleep(1)


# Call main function
if __name__ == "__main__":
    main()
