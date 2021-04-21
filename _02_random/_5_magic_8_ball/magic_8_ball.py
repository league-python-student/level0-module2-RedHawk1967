import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    q = simpledialog.askstring(title="",prompt="Ask a yes or no question?")
    # Make a variable and initialize it to a random number between 0 and 3
    random_number = random.randint(0, 3)
    # If the random number is 0
    if random_number == 0:
        messagebox.showinfo(title="",message="Yes")
        # tell the user "Yes"

    # If the random number is 1
    if random_number == 1:
        messagebox.showinfo(title="",message="No")
        # tell the user "No"

    # If the random number is 2
    if random_number == 2:
        messagebox.showinfo(title="",message="Maybe you should ask Google?")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if random_number == 3:
        messagebox.showinfo(title="",message="I don;t know really know the answer to that")
        # write your own answer
