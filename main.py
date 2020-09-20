# from Email import *
from Motor import *
import time
import schedule


def initialization():
    motor = Motor()
    motor.runMotor()

    '''print("Auto-Cat initializing")
    email = Email(465, 'catfeederprojectpie@gmail.com', 'AutoCatProject')
    # motor = Motor(21, 50, 5)
    # schedule.every(1).minutes.do(email.sendEmail,'martin.c.842@gmail.com','This is a test')
    email.sendEmail('martin.c.842@gmail.com', 'This is a test!!')
    # schedule.every(1).minutes.do(motor.feed, 10, 5)
    # Add any other initializing components here
    print("Auto-Cat initializing complete")'''


def main():
    # Call initilization function
    initialization()


# Call main function
if __name__ == "__main__":
    main()
