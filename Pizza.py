######### per aspera ad astra #########



# importing libraries
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from PIL import Image  
import csv   
import customtkinter as ctk
import random
from datetime import datetime
from tkinter import ttk
from tkinter import CENTER



# some basic setting for GUI
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")
body = ctk.CTk()
body.geometry("1000x500")
body.title("Pizza Delivery Project")


# importing customers.csv
customersdf = pd.read_csv("customers.csv")

# importing orders.csv
ordersdf = pd.read_csv("orders.csv")

# importing Menu.txt
file = open("Menu.txt", "r" ,encoding="utf-8")
menu = file.read()

# defining prices and contain dicts
prices = {"classic":30, "margherita":40, "turkish":50, "simple":20, "olive":4, "mushroom":10, "goat cheese":7, "meat":15, "onion":4, "corn":6}
contain = {"classic":"tomatoes, mozzarella and basil.", "margherita":"tomatoes, mozzarella, basil, olive oil and salt.", 
           "turkish":"sausage, bacon, pepper, and mushroom.", "simple":"tomatoes and mozzarella cheese."}



# defining the Pizza class
class Pizza:
    def __init__(self, base, sauce):
        self.base = base
        self.sauce = sauce
    

    # defining the get_description function
    def get_description(self):
        description = "Your {} pizza with {} is being prepared...\nYour pizza contains {}".format(self.base, self.sauce, contain[self.base])
        return description

    
    # defining the get_cost function
    def get_cost(self):
        cost = prices[self.base] + prices[self.sauce]
        cost = "cost: {}₺".format(cost)
        return cost



# defining the variables that we will use in Pizza Delivery Project
log_control = tk.BooleanVar(body, value=False)
remember_control = tk.BooleanVar(body, value=False)

username_entry = tk.StringVar(body)
password_entry = tk.StringVar(body)

username_signup_entry = tk.StringVar(body)
password_signup_entry = tk.StringVar(body)

pizza_choice = tk.StringVar(body, value="no_cho_pizza")
sauce_choice = tk.StringVar(body, value="no_cho_sauce")

credit_card_number_tk = tk.StringVar(body)
credit_card_security_code_tk = tk.StringVar(body)
credit_card_expire_tk = tk.StringVar(body)
address_tk = tk.StringVar(body)
note_tk = tk.StringVar(body)



# function to destroy all widgets and clear the screen
def remove_widgets():
    for widget in body.winfo_children():
        widget.destroy()


# funtion page to get login or signup to system
def Login():
    remove_widgets()
    login_page_space = ctk.CTkLabel(body, text="").pack()

    loginlbl = ctk.CTkLabel(body, text="You are welcome again! Login to your account.", font=("Times",30)).pack()

    login_page_space = ctk.CTkLabel(body, text="").pack()
    login_page_space = ctk.CTkLabel(body, text="").pack()

    # username and password entries to login to the system
    usernamelbl = ctk.CTkLabel(body, text="Username", font=("System",15)).pack()
    username_ent = ctk.CTkEntry(body, textvariable=username_entry, width=200).pack()
    passwordlbl = ctk.CTkLabel(body, text="Password", font=("System",15)).pack()
    password_ent = ctk.CTkEntry(body, textvariable=password_entry, width=200).pack()
    login_page_space = ctk.CTkLabel(body, text="").pack()
    login_page_space = ctk.CTkLabel(body, text="").pack()
    login_button = ctk.CTkButton(body, text='Login', font=("System",15), command=LoginCheck).pack()
    login_page_space = ctk.CTkLabel(body, text="").pack()
    login_page_space = ctk.CTkLabel(body, text="").pack()
    login_page_space = ctk.CTkLabel(body, text="").pack()


    # redirect to the SignUp page to create a new registration if not registered in the system
    create_acc = ctk.CTkLabel(body, text="Don't have an account yet? Create one.", font=("Times",15)).pack()
    signup_button = ctk.CTkButton(body, text='Sign up', command=SignUp, font=("System",15)).pack()



# function page to check the accuracy of the information from Login()
def LoginCheck():
    # importing customers.csv again to check username and password after sign up 
    customersdf = pd.read_csv("customers.csv")

    # check if the entered username and password are in customersdf if they matched then redirect to Home page with login
    for i in range(customersdf.shape[0]):
        if(customersdf.loc[i,"username"]==username_entry.get() and customersdf.loc[i,"password"]==password_entry.get()):
            log_control.set(True)
            remove_widgets()
            messagebox.showinfo("welcome", "login successful")
            HomeLogin()
            break

    # if username or password incorrect then system gives a warning
    if(log_control.get()==False):
        messagebox.showerror("login failed", "your username or password is incorrect")
        Login()


# function page to save information of new users
def SignUp():
    remove_widgets()

    signup_page_space = ctk.CTkLabel(body, text="").pack()
    signup_page_space = ctk.CTkLabel(body, text="").pack()
    signup_page_space = ctk.CTkLabel(body, text="").pack()
    signup_page_space = ctk.CTkLabel(body, text="").pack()

    signlbl = ctk.CTkLabel(body, text="You are welcome!", font=("Times",30)).pack()

    signup_page_space = ctk.CTkLabel(body, text="").pack()
    signup_page_space = ctk.CTkLabel(body, text="").pack()
    signup_page_space = ctk.CTkLabel(body, text="").pack()

    # username and password entries to register to the system
    username_signup_lbl = ctk.CTkLabel(body, text="username", font=("System",15)).pack()
    username_signup_ent = ctk.CTkEntry(body, textvariable=username_entry, width=200).pack()
    password_signup_lbl = ctk.CTkLabel(body, text="password", font=("System",15)).pack()
    password_signup_ent = ctk.CTkEntry(body, textvariable=password_entry, width=200).pack()
    signup_page_space = ctk.CTkLabel(body, text="").pack()
    signup_button = ctk.CTkButton(body, text="Sign Up", font=("System",15), command=SignUpCheck).pack()
    

# function page to write the username, password and user_Id of new users on customers.csv
def SignUpCheck():
    username_signup_entry = username_entry.get()
    password_signup_entry = password_entry.get()

    
    # produce new random user_Id
    user_id = random.randint(100000, 999999)

    # open and append username, password and user_Id to customers.csv
    fields = {username_signup_entry:"username", password_signup_entry:"password", user_id:"user_Id"}
    with open("customers.csv", 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        f.close()

    # redirect to Login() page
    Login()

    

# function to display previous orders
def Previous_Orders():
    remove_widgets()

    if(log_control.get()==True):

        ordersdf = pd.read_csv("orders.csv")
        prev_order_page_space = ctk.CTkLabel(body, text="").pack()
        loginlbl = ctk.CTkLabel(body, text="{0}'s previous orders".format(username_entry.get()), font=("Times", 30), text_color="magenta").pack()
        prev_order_page_space = ctk.CTkLabel(body, text="").pack()
    
        tree = ttk.Treeview(body, column=("ordered_pizza", "ordered_sauce", "total_amount", "order_datetime", "order_note"), show='headings', height=20)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="ordered_pizza")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="ordered_sauce")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="total_amount")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="order_datetime")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="order_note")


        prev_order = ordersdf[ordersdf["username"].str.contains(username_entry.get())].reset_index(drop=True)

        # insert the data in Treeview 
        for i in range(len(prev_order)):
            tree.insert('', 'end', text="{0}".format(i), values=(prev_order.loc[i,"ordered_pizza"], 
                                                                prev_order.loc[i,"ordered_sauce"], 
                                                                prev_order.loc[i,"total_amount"], 
                                                                prev_order.loc[i,"order_datetime"],
                                                                prev_order.loc[i,"order_note"]))


        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Times", 20))
        style.configure("Treeview", font=("Times", 13))
        style.configure("Treeview", background="black", foreground="violet")

        tree.pack()
        prev_order_page_space = ctk.CTkLabel(body, text="").pack()
        back_to_home = ctk.CTkButton(body, text="Home Page", command=HomeLogin).pack()


    elif(log_control.get()==False):
        messagebox.showerror(title="You are not logged in yet", message="Please log in or sign up")
        Login()


# page to display communication channels
def Contact_Us():
    remove_widgets()
    contact_page_space = ctk.CTkLabel(body, text="").pack()
    contact_page_space = ctk.CTkLabel(body, text="").pack()
    contact_page_space = ctk.CTkLabel(body, text="").pack()
    contact_page_space = ctk.CTkLabel(body, text="").pack()
    contact_page_space = ctk.CTkLabel(body, text="").pack()
    mail_lbl = ctk.CTkLabel(body, width=200, height=40, text="ahmetguner7649@gmail.com", font=("Times", 30), text_color="magenta").pack()
    contact_page_space = ctk.CTkLabel(body, text="").pack()
    contact_page_space = ctk.CTkLabel(body, text="").pack()

    back_to_home = ctk.CTkButton(body, text="Home Page", command=Contact_Check).pack()


def Contact_Check():
    # check if logged in redirect to Order() page else display error and redirect to Login() page
    if (log_control.get() == True):
        HomeLogin()
    elif(log_control.get() == False):
        Home()
    


# Home page without login
def Home():
    remove_widgets()


    ######################################### menubar #########################################
    main_menu = tk.Menu(body)

    # profile menu
    profile_menu = tk.Menu(main_menu, tearoff=0)
    profile_menu.add_command(label='Login', font=("Merriweather Bold",11), command=Login)
    profile_menu.add_separator()
    profile_menu.add_command(label='Sign Up', font=("Merriweather Bold",11), command=SignUp)

    # help menu
    help_menu = tk.Menu(main_menu, tearoff=0)
    help_menu.add_command(label="previous orders", font=("Merriweather Bold",11), command=Previous_Orders)
    help_menu.add_command(label="contact us", font=("Merriweather Bold",11), command=Contact_Us)


    main_menu.add_cascade(label='Profile', menu=profile_menu)
    main_menu.add_cascade(label='Help', menu=help_menu)

    body.config(menu=main_menu)


    ##################################### images of pizzas #####################################
    # image of classic pizza
    img = Image.open("images/classic.png")
    img = ctk.CTkImage(img, size=(120,120))
    panel = ctk.CTkLabel(body, image = img, text="", width=30, height=10).place(x=80, y=20)
    classic_pizza = ctk.CTkLabel(body, text="classic pizza", text_color="magenta").place(x=105, y=140)

    # image of margherita pizza
    img = Image.open("images/margherita.png")
    img = ctk.CTkImage(img, size=(120,120))
    panel = ctk.CTkLabel(body, image = img, text="", width=30, height=10).place(x=310, y=20)
    margherita_pizza = ctk.CTkLabel(body, text="margherita pizza", text_color="magenta").place(x=325, y=140)

    # image of turkish pizza
    img = Image.open("images/turkish.png")
    img = ctk.CTkImage(img, size=(120,120))
    panel = ctk.CTkLabel(body, image = img, text="", width=30, height=10).place(x=540, y=20)
    turkish_pizza = ctk.CTkLabel(body, text="turkish pizza", text_color="magenta").place(x=565, y=140)

    # image of simple pizza
    img = Image.open("images/simple.png")
    img = ctk.CTkImage(img, size=(120,120))
    panel = ctk.CTkLabel(body, image = img, text="", width=30, height=10).place(x=770, y=20)
    simple_pizza = ctk.CTkLabel(body, text="simple pizza", text_color="magenta").place(x=795, y=140)


    ########################################## orders ##########################################
    # Which pizza would you like?
    which_pizza_label = ctk.CTkLabel(body, text="   Which pizza would you like?   ", bg_color="darkslateblue", text_color="aquamarine").place(x=80, y=195)
    pizza_radio_1 = ctk.CTkRadioButton(body, text="classic", variable= pizza_choice, value="classic").place(x=80, y=230)
    pizza_radio_2 = ctk.CTkRadioButton(body, text="margherita", variable= pizza_choice, value="margherita").place(x=80, y=255)
    pizza_radio_3 = ctk.CTkRadioButton(body, text="turkish", variable= pizza_choice, value="turkish").place(x=80, y=280)
    pizza_radio_4 = ctk.CTkRadioButton(body, text="simple", variable= pizza_choice, value="simple").place(x=80, y=305)

    # What sauce would you like to add?
    which_pizza_label = ctk.CTkLabel(body, text="   What sauce would you like to add?   ", bg_color="darkslateblue", text_color="aquamarine").place(x=300, y=195)
    pizza_radio_1 = ctk.CTkRadioButton(body, text="olive", variable= sauce_choice, value="olive").place(x=300, y=230)
    pizza_radio_2 = ctk.CTkRadioButton(body, text="mushroom", variable= sauce_choice, value="mushroom").place(x=300, y=255)
    pizza_radio_3 = ctk.CTkRadioButton(body, text="goat cheese", variable= sauce_choice, value="goat cheese").place(x=300, y=280)
    pizza_radio_4 = ctk.CTkRadioButton(body, text="meat", variable= sauce_choice, value="meat").place(x=300, y=305)
    pizza_radio_4 = ctk.CTkRadioButton(body, text="onion", variable= sauce_choice, value="onion").place(x=300, y=330)
    pizza_radio_4 = ctk.CTkRadioButton(body, text="corn", variable= sauce_choice, value="corn").place(x=300, y=355)

    # printing Menu.txt on screen
    menu_label = ctk.CTkLabel(body, text=menu, font=("Times", 15), text_color="mediumaquamarine").place(x=640, y=200)

    # button to Buy() funtion
    buy_button = ctk.CTkButton(body, text="Buy", command=Buy, width=435, height=50, font=("Times", 30)).place(x=80, y=400)



# Home page with login
def HomeLogin():
    remove_widgets()


    ######################################### menubar #########################################
    main_menu = tk.Menu(body)

    # profile menu
    profile_menu = tk.Menu(main_menu, tearoff=0)
    profile_menu.add_command(label=username_entry.get(), font=("Merriweather Bold",11), command=Profile)
    profile_menu.add_separator()
    profile_menu.add_command(label="log out", font=("Merriweather Bold",11), command=LogOut)

    # information menu
    help_menu = tk.Menu(main_menu, tearoff=0)
    help_menu.add_command(label="previous orders", font=("Merriweather Bold",11), command=Previous_Orders)
    help_menu.add_command(label="contact us", font=("Merriweather Bold",11), command=Contact_Us)

    main_menu.add_cascade(label='Profile', menu=profile_menu)
    main_menu.add_cascade(label='Help', menu=help_menu)

    body.config(menu=main_menu)


    ##################################### images of pizzas #####################################
    # image of classic pizza
    classicimg = Image.open("images/classic.png")
    classicimg = ctk.CTkImage(classicimg, size=(120,120))
    panel = ctk.CTkLabel(body, image = classicimg, text="", width=30, height=10).place(x=80, y=20)
    classic_pizza = ctk.CTkLabel(body, text="classic pizza", text_color="magenta").place(x=105, y=140)

    # image of margherita pizza
    margheritaimg = Image.open("images/margherita.png")
    margheritaimg = ctk.CTkImage(margheritaimg, size=(120,120))
    panel = ctk.CTkLabel(body, image = margheritaimg, text="", width=30, height=10).place(x=310, y=20)
    margherita_pizza = ctk.CTkLabel(body, text="margherita pizza", text_color="magenta").place(x=325, y=140)

    # image of turkish pizza
    turkishimg = Image.open("images/turkish.png")
    turkishimg = ctk.CTkImage(turkishimg, size=(120,120))
    panel = ctk.CTkLabel(body, image = turkishimg, text="", width=30, height=10).place(x=540, y=20)
    turkish_pizza = ctk.CTkLabel(body, text="turkish pizza", text_color="magenta").place(x=565, y=140)

    # image of simple pizza
    simpleimg = Image.open("images/simple.png")
    simpleimg = ctk.CTkImage(simpleimg, size=(120,120))
    panel = ctk.CTkLabel(body, image = simpleimg, text="", width=30, height=10).place(x=770, y=20)
    simple_pizza = ctk.CTkLabel(body, text="simple pizza", text_color="magenta").place(x=795, y=140)


     ########################################## orders ##########################################
    # Which pizza would you like?
    which_pizza_label = ctk.CTkLabel(body, text="   Which pizza would you like?   ", bg_color="darkslateblue", text_color="aquamarine").place(x=80, y=195)
    pizza_radio_1 = ctk.CTkRadioButton(body, text="classic", variable= pizza_choice, value="classic").place(x=80, y=230)
    pizza_radio_2 = ctk.CTkRadioButton(body, text="margherita", variable= pizza_choice, value="margherita").place(x=80, y=255)
    pizza_radio_3 = ctk.CTkRadioButton(body, text="turkish", variable= pizza_choice, value="turkish").place(x=80, y=280)
    pizza_radio_4 = ctk.CTkRadioButton(body, text="simple", variable= pizza_choice, value="simple").place(x=80, y=305)

    # What sauce would you like to add?
    which_pizza_label = ctk.CTkLabel(body, text="   What sauce would you like to add?   ", bg_color="darkslateblue", text_color="aquamarine").place(x=300, y=195)
    pizza_radio_1 = ctk.CTkRadioButton(body, text="olive", variable= sauce_choice, value="olive").place(x=300, y=230)
    pizza_radio_2 = ctk.CTkRadioButton(body, text="mushroom", variable= sauce_choice, value="mushroom").place(x=300, y=255)
    pizza_radio_3 = ctk.CTkRadioButton(body, text="goat cheese", variable= sauce_choice, value="goat cheese").place(x=300, y=280)
    pizza_radio_4 = ctk.CTkRadioButton(body, text="meat", variable= sauce_choice, value="meat").place(x=300, y=305)
    pizza_radio_4 = ctk.CTkRadioButton(body, text="onion", variable= sauce_choice, value="onion").place(x=300, y=330)
    pizza_radio_4 = ctk.CTkRadioButton(body, text="corn", variable= sauce_choice, value="corn").place(x=300, y=355)

    # printing Menu.txt on screen
    menu_label = ctk.CTkLabel(body, text=menu, font=("Times", 15), text_color="mediumaquamarine").place(x=640, y=200)

    # button to Buy() funtion
    buy_button = ctk.CTkButton(body, text="Buy", command=Buy, width=435, height=50, font=("Times", 30)).place(x=80, y=400)


# function to log out
def LogOut():
    # set the log_control False and display info then redirect to Home page without login
    log_control.set(False)
    messagebox.showinfo(title="You logged out", message="Successfully logged out")
    Home()



# function to buy and check if logged in
def Buy():
    # check if logged in redirect to Order() page else display error and redirect to Login() page
    if (log_control.get() == True):
        if(pizza_choice.get()=="no_cho_pizza" and sauce_choice.get()=="no_cho_sauce"):
            messagebox.showerror(title="error", message="you didn't choose the pizza or sauce")
            HomeLogin()
        else:
            global pizza
            pizza = Pizza(pizza_choice.get(), sauce_choice.get())
            Order()
    elif(log_control.get() == False):
        messagebox.showerror(title="You are not logged in yet", message="Please log in or sign up")
        Login()



# function page to get order information
def Order():
    remove_widgets()
    getinf = ctk.CTkLabel(body, text="Fill in the information below to order pizza.", font=("Times", 20), text_color="magenta").place(x=200, y=20)

    orderimgpath = "images/{0}.png".format(pizza_choice.get())
    orderimg = Image.open(orderimgpath)
    orderimg = ctk.CTkImage(orderimg, size=(250,250))
    orderimgpanel = ctk.CTkLabel(body, image = orderimg, text="", width=30, height=10).place(x=585, y=20)
    order_description = ctk.CTkLabel(body, text = pizza.get_description(), text_color="magenta").place(x=550, y=285)
    order_total_amount = ctk.CTkLabel(body, text=pizza.get_cost(), text_color="magenta", font=("Times",30)).place(x=650, y=350)


    credit_card_number_lbl = ctk.CTkLabel(body, text="enter your credit card number", font=("System",15)).place(x=200, y=60)
    credit_card_number_entry = ctk.CTkEntry(body,textvariable = credit_card_number_tk, width=310).place(x=200, y=90)

    credit_card_security_code_lbl = ctk.CTkLabel(body, text="enter your credit card security code", font=("System",15)).place(x=200, y=140)
    credit_card_security_code_entry = ctk.CTkEntry(body,textvariable = credit_card_security_code_tk, width=310).place(x=200, y=170)

    credit_card_expire_lbl = ctk.CTkLabel(body, text="enter your credit card expire date", font=("System",15)).place(x=200, y=220)
    credit_card_expire_entry = ctk.CTkEntry(body,textvariable = credit_card_expire_tk, width=310).place(x=200, y=250)

    address_card_number_lbl = ctk.CTkLabel(body, text="enter your address", font=("System",15)).place(x=200, y=300)
    address_entry = ctk.CTkEntry(body,textvariable = address_tk, width=310).place(x=200, y=330)

    note_lbl = ctk.CTkLabel(body, text="write note if you want to specify about your order", font=("System",15)).place(x=200, y=390)
    note_entry = ctk.CTkEntry(body,textvariable = note_tk, height=70, width=310).place(x=200, y=420)

    order_button = ctk.CTkButton(body, text="Order", font=("System",15), command=OrderCheck, height=70, width=150).place(x=630, y=420)



# function page that processes the entered information into customers.csv and orders.csv
def OrderCheck():

    # importing customers.csv again to refresh
    customersdf = pd.read_csv("customers.csv")

    username = username_entry.get()
    
    # get order date time
    current_date_time = datetime.now()
    current_date_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S")

    # processing data into customers.csv
    customersdf.loc[customersdf.username == username, "credit_card_number"] = credit_card_number_tk.get()
    customersdf.loc[customersdf.username == username, "credit_card_security_code"] = credit_card_security_code_tk.get()
    customersdf.loc[customersdf.username == username, "credit_card_expire"] = credit_card_expire_tk.get()
    customersdf.loc[customersdf.username == username, "address"] = address_tk.get()
    customersdf.to_csv("customers.csv", index=False)

    # processing data into orders.csv
    orders_fields = {username_entry.get():"username", address_tk.get():"address", pizza_choice.get():"ordered_pizza", 
                    sauce_choice.get():"ordered_sauce", pizza.get_cost()[-3:]:"total_amount", current_date_time:"order_datetime",
                    note_tk.get():"order_note"}
    with open("orders.csv", 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(orders_fields)
        f.close()

    # reported that the order was successful
    messagebox.showinfo(title="Bon appetit!", message="your order has been received successfully")

    # return to Home page with login
    HomeLogin()



# Profile page that shows information of current user
def Profile():
    remove_widgets()

    loginlbl = ctk.CTkLabel(body, text="You are welcome {0}!".format(username_entry.get()), font=("Times", 30)).place(x=350, y=80)
    back_to_home = ctk.CTkButton(body, text="Home Page", command=HomeLogin).place(x=430, y=120)


    

if __name__ == "__main__":
    Home()
    body.mainloop()




######### per aspera ad astra #########