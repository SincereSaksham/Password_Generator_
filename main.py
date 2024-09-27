from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#improve it , use try and except only when there is use of it otherwise if else works the best
def search():
    with open("Password_data.json") as data_file:
        data = json.load(data_file)
        searchinput = wbinput.get()
        try:
            messagebox.showinfo(title=f"{searchinput}", message=f"Email: {data[searchinput]['USER']} \n"
                                                                    f"Password: {data[searchinput]['PASSCODE']}")
            print(data[searchinput]["USER"])

        except KeyError:
            messagebox.showerror(title="Error", message="Website not present in database\nEnter again")



def generate_passwords():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    pas = "".join(password_list)
    passinput.insert(0, pas)
    pyperclip.copy(pas)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = wbinput.get()
    use_email = eminput.get()
    word = passinput.get()
    new_data = {web: {
        "USER": use_email,
        "PASSCODE": word
    }
    }

    if len(web) == 0 or len(use_email) == 0 or len(word) == 0:
        messagebox.showwarning(message="You have left some fields")
    else:
        try:
            with open("Password_data.json", "r") as pw_data:
                data = json.load(pw_data)
                data.update(new_data)
        except FileNotFoundError:
            with open("Password_data.json", "w") as pw_data:
                json.dump(new_data, pw_data)
                wbinput.delete(0, END)
                passinput.delete(0, END)

        else:
            with open("Password_data.json", "w") as sw_data:
                json.dump(data, sw_data, indent=4)

        finally:
            wbinput.delete(0, END)
            passinput.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(480,400)
window.config(pady=50, padx=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# label : website
website = Label(text="Website:")
website.grid(column=0, row=1)
wbinput = Entry(width=28)
wbinput.focus()
wbinput.place(x=140, y= 205)

em = Label(text="Email / Username:")
em.grid(column=0, row=2)
eminput = Entry(width=28)
eminput.place(x=140, y=230)

password = Label(text="Password:")
password.grid(column=0, row=3)
passinput = Entry(width=28)
passinput.place(x=140, y=255)

gen_pass_button = Button(text="Gen.Password", command=generate_passwords)
gen_pass_button.place(x=318 , y =253 )

add = Button(text="Add", width=35, command=save_password , bg="lightgreen")
add.place(x=140, y=280)

search_button = Button(text="Search", width=10, command=search)
search_button.place(x= 320, y=200)

window.mainloop()
