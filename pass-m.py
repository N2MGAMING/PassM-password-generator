from random import *
from tkinter import *
from time import strftime, localtime
import string
import os


def generator():
    def save(password):
        num = 0
        pasword = []
        source = "log.txt"
        file = open(source, 'a')
        datetiime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        for i in password:
            pasword.append(i)
            num += 1
            if num == 499999:
                pasword.append("\n")
                num = 0
        log = "\n*** " + datetiime + " password ***\n" + "".join(pasword)
        file.write(log)
        file.close()
    
    def lenghtt(lengh):
        char = string.ascii_letters + string.digits +string.punctuation
        password_part5 = choices(char, k=lengh - 4)
        password_part1 = choice(string.ascii_lowercase)
        password_part2 = choice(string.ascii_uppercase)
        password_part3 = choice(string.digits)
        password_part4 = choice(string.punctuation)
        index_choosen1 = choice(range(lengh - 4))
        index_choosen2 = choice(range(lengh - 4))
        index_choosen3 = choice(range(lengh - 4))
        index_choosen4 = choice(range(lengh - 4))
        password_part5.insert(index_choosen1, password_part1)
        password_part5.insert(index_choosen2, password_part2)
        password_part5.insert(index_choosen3, password_part3)
        password_part5.insert(index_choosen4, password_part4)
        password = ''.join(password_part5)
        password_entry.insert("1.0", password)
        return password
    
    password_entry.delete("1.0", END)
    
    if variable.get()=="...":
        def get_user():
            lenght_basic = user_entry.get("1.0", END)
            user_number.destroy()
            password = lenghtt(lengh=int(lenght_basic))
            save(password=password)
            

        user_number = Tk()

        user_number.title("Write the number of characters")
        user_number.maxsize(480, 240)
        user_number.minsize(480, 240)
        user_number.focus()
        user_number.config(bg="white")
        user_entry = Text(user_number, font=("Arial", 20), bd=0, exportselection=1,height=5, width=28)
        user_button = Button(user_number, text="Confirm", font=("Ubuntu", 20), bg="white", fg="black", border=0, activeforeground='black', activebackground='#b3b6b7', anchor=N, command=get_user)

        user_entry.pack(expand=YES)
        user_button.pack(expand=YES)
        user_number.mainloop()
    else:
        lenght = int(variable.get())
        password = lenghtt(lengh=lenght)
        save(password=password)

def clear_log():
    source = "log.txt"
    file = open(source, 'w')
    file.write("")
    file.close

def open_log():
    os.system("featherpad log.txt")

app = Tk()

app.title("Password generator")
app.maxsize(800, 480)
app.minsize(800, 480)
app.iconphoto(True, PhotoImage(file='asset/icon.png'))
app.config(bg="white")

generator_frame = Frame(app, bg="white")
button_frame = Frame(generator_frame, bg="white")
log_frame = Frame(button_frame, bg="white")
canvas = Canvas(app, bg="white", highlightthickness=False)
password_entry = Text(generator_frame, font=("Arial", 20), bd=0, exportselection=1,height=6, width=30)
generator_button = Button(button_frame, text="Generate", font=("Ubuntu", 20), bg="white", fg="black", border=0, activeforeground='black', activebackground='#b3b6b7', anchor=N, command=generator)
log_button = Button(log_frame, text="clear log", font=("Ubuntu", 20), bg="white", fg="black", border=0, activeforeground='black', activebackground='#b3b6b7', anchor=N, command=clear_log)
open_log_button = Button(log_frame, text="open log file", font=("Ubuntu", 20), bg="white", fg="black", border=0, activeforeground='black', activebackground='#b3b6b7', anchor=N, command=open_log)
lenght_frame = Frame(generator_frame, bg="white")
lenght_label = Label(lenght_frame, text="Number of characters :", font=("Ubuntu", 15), bg="white")
OptionList = ["8", "16", "24", "..."]
variable = StringVar()
variable.set(OptionList[0])
opt = OptionMenu(lenght_frame, variable, *OptionList)
opt.config(highlightthickness=False)
image = PhotoImage(file="asset/shield.png")
canvas.create_image(160, 133, image=image)

generator_frame.pack(side=RIGHT)
lenght_label.pack(side=LEFT)
opt.pack(padx=20)
lenght_frame.pack(anchor= W, padx=50)
password_entry.pack(expand=True, padx=50, pady=30)
button_frame.pack(expand=True)
generator_button.pack(side=TOP)
log_frame.pack(side=BOTTOM, pady=10)
log_button.pack(side=LEFT)
open_log_button.pack(side=RIGHT)
canvas.pack(side=LEFT)

app.mainloop()
