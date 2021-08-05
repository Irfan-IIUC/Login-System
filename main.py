from tkinter import *
from tkinter import messagebox

from PIL import ImageTk


class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Frame")
        self.root.geometry("1000x600+150+200")
        self.root.resizable(False, False)

        # === image ===

        self.bg = ImageTk.PhotoImage(file="image/dest1.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        f1 = Frame(self.root, bg="white")
        f1.place(x=430, y=65, height=340, width=500)

        l1 = Label(f1, text="Login Here", bg="white", fg="Blue", pady="18", font=("times new roman", 35, "bold")).pack()
        l3 = Label(f1, text="Username", bg="white", fg="Black", font=("times new roman", 20, "bold")).place(x=70, y=100)

        self.txtuser = Entry(f1, text="", font=("times new roman", 15), bg="lightgray", fg="red")
        self.txtuser.place(x=75, y=140, height=30, width=350)

        l4 = Label(f1, text="Password", bg="white", fg="Black", font=("times new roman", 20, "bold")).place(x=70, y=180)

        self.txtpass = Entry(f1, text="", font=("times new roman", 15), bg="lightgray", fg="red")
        self.txtpass.place(x=75, y=220, height=30, width=350)

        forgot = Button(f1, text="Forget Password?", cursor="hand2", bd=0, font=("times new roman", 12), fg="white", bg="blue").place(
            x=75, y=265)
        b1 = Button(self.root, text="Login", cursor="hand2", command=self.login_function, font=("times new roman", 20), fg="white",
                    bg="red").place(x=600, y=385, height=40, width=180)

    def login_function(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required !", parent=self.root)
        elif self.txtuser.get() != 'admin' or self.txtpass.get() != '12345':
            messagebox.showerror("Error", "Invalid username/password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.txtuser.get()}\nYour password {self.txtpass.get()}",
                                parent=self.root)


root = Tk()
ob = login(root)

root.mainloop()
