import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    random_number0 = random.randint(1, 100)
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    random_number3 = random.randint(1, 100)
    random_number4 = random.randint(1, 100)
    random_number5 = random.randint(1, 100)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title="",message=str(random_number0)+" "+ str(random_number1) +" " + str(random_number2)+ " " + str(random_number3)+ " "+ str(random_number4)+" "+str(random_number5))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
