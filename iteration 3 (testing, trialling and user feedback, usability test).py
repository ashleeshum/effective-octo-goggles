"""ITERATION 3
author: Ashlee Shum
description: fixing code (functions within functions), pep8 testing,
usability testing/user feedback
"""


import tkinter as tk
from tkinter import *

class BentoBowl:
    def __init__(self):
        self.mainslist = ["rice","brown rice", "noodles"]
        self.vegeslist = ["stirfry", "salad", "beetroot", "edamame beans"]
        self.meatslist = ["chicken karage", "chicken karage (spicy)", "chicken katsu"]
        self.meatslist2 = ["tempura", "salmon", "teriyaki chicken"]
        self.sauceslist = ["teriyaki chicken sauce", "bbq sauce", "kewpie mayo"]

    def return_lists(self):
        #passing self through so that the lists above can be accessed and thus returned
        #returning all the lists with ingredients so that they can be passed through to another class and used.
        return [self.mainslist, self.vegeslist, self.meatslist, self.meatslist2, self.sauceslist]


class Submit:
    def __init__(self, layout):
        """creating variable so that the root created from layout
        class can be accessed within this submit class.
        """
        self.root = layout.root
        
    #making order show up on screen
    def show_order(self, name, phoneno, popup, sauce_retr, meats_retr, veges_retr, main_retr):
        user_name=name.get("1.0","end-1c")
        user_phone=phoneno.get("1.0","end-1c")
        order_details = ""

        #checking if valid name and phone number has been entered
        if user_phone.isnumeric() and user_name != "":
            popup.destroy()
            printed_order=Toplevel(self.root, bg="#FDFDFB")
            printed_order.geometry("500x300")
            printed_order.title("Your order:")
            printed_order.resizable(False, False)

            all_veges = ""
            for idx, vege in enumerate(veges_retr):
                if vege.get() != "":  
                    all_veges += vege.get()
                    if idx < len(veges_retr) - 1:
                        all_veges += ", "

            all_meats = ""
            for idx, meat in enumerate(meats_retr):
                if meat.get() != "":
                    all_meats += (meat.get() + ", ")
                    if idx == 2:
                        all_meats += "\n"
            #removing comma and space
            all_meats = all_meats[:-2]

            #calculating price of bento bowl based on options user selected
            self.value=14
            for vege in veges_retr:
                if vege.get() != "":
                    self.value += 2 
            for meat in meats_retr:
                if meat.get() != "":
                    self.value += 2                

            #printing order on popup
            order_details = "Mains choice: " + main_retr + "\n"
            order_details = order_details + "Vegetables choice: " + all_veges + "\n"
            order_details = order_details + "Meats choice: " + all_meats + "\n"
            order_details = order_details + "Sauce choice: " +sauce_retr + "\n"
            order_details = order_details + "Order for " +user_name + "\n\n"
            order_details = order_details + "Phone number: " +user_phone +"\n"
            order_details = order_details + "Cost: $" +str(self.value) +"\n\n"
            order_details = order_details + "We will text you when your order is ready for pick up!\nHave a good day :)"
            
            users_order_label=tk.Label(
                master=printed_order,
                text="Here is your order:",
                anchor="w",
                font=("Lucinds, 15"),
                padx = 10,
                pady=5,
                width = 50,
                bg="#B24C63"
                )
            users_order_label.grid(row=0, column=0, sticky="we")

            users_order = tk.Label(
                master=printed_order,
                text=order_details,
                font=("Lucinds, 13"),
                anchor="w",
                justify = "left",
                padx = 10,
                pady=10,
                bg="#FDFDFB"
                )
            users_order.grid(row=1, column=0, sticky="w")
                
        #checking if phone number has been entered but no name
        elif user_phone.isnumeric() and user_name == "":
            error_popup= Toplevel(popup)
            error_popup.geometry("200x100")
            error_popup.title("error:")
            error_popup.resizable(False, False)
            error_label = tk.Label(
                master=error_popup,
                text="please enter a \n name", 
                font = ("Lucinds, 10"),
                anchor="center"
            )
            error_label.grid(row=0, column=0, sticky="news")

        elif user_phone == "" and user_name != "":
            error_popup= Toplevel(popup)
            error_popup.geometry("200x100")
            error_popup.title("error:")
            error_popup.resizable(False, False)
            error_label = tk.Label(
                master=error_popup,
                text="please enter a \n phone number", 
                font = ("Lucinds, 10"),
                anchor="center"
            )
            error_label.grid(row=0, column=0, sticky="news")

        elif not user_phone.isnumeric() and user_name != "":
            error_popup= Toplevel(popup)
            error_popup.geometry("200x100")
            error_popup.title("error:")
            error_popup.resizable(False, False)
            error_label = tk.Label(
                master=error_popup,
                text="please enter a \n valid phone number", 
                font = ("Lucinds, 10"),
                anchor="center"
            )
            error_label.grid(row=0, column=0, sticky="news")
            
        else:
            error_popup= Toplevel(popup)
            error_popup.geometry("200x100")
            error_popup.title("error:")
            error_popup.resizable(False, False)
            error_label = tk.Label(
                master=error_popup,
                text="please enter a \n phone number and name", 
                font = ("Lucinds, 10"),
                anchor="center"
            )
            error_label.grid(row=0, column=0, sticky="news")

    #method for if no options have been selected in the ordering section
    def not_entered_error(self):
        order_error_popup=Toplevel(self.root)
        order_error_popup.geometry("200x100")
        order_error_popup.title("error")
        order_error_popup.resizable(False, False)
        #making text for not entered sections
        order_error_label = tk.Label(
            master=order_error_popup,
            text="Please fill in all sections \nbefore ordering",
            anchor="center",
            font=("Lucinds, 10")
            )
        order_error_label.grid(row=0, column=0, sticky="news")
    
    #only need to pass throguh self as variables are in the same class thus don't need to pass every single thing
    def popup(self, frm_sauces, sauce_retr, meats_retr, veges_retr, main_retr):
        frm_sauces.grid_remove()

        #getting vege and meat options selected into a list bc they are checkbuttons
        is_vege_selected = ""
        for vege in veges_retr:
            is_vege_selected += vege.get()

        is_meat_selected = ""
        for meat in meats_retr:
            is_meat_selected += meat.get()

        #checking if user has entered anything in the sections
        if main_retr == "0":
            self.not_entered_error()
        elif is_vege_selected == "":
            self.not_entered_error()
        elif is_meat_selected == "":
            self.not_entered_error()
        elif sauce_retr == "0":
            self.not_entered_error()
        else:
            #make popup where user enters name and phone number then print order
            popup= Toplevel(self.root)
            popup.geometry("400x200")
            popup.title("Finalising order:")
            popup.resizable(False, False)
        
            #remove everything on popup then print order has been submitted displaying their order
            #creating label for instructions
            frame_instruct = tk.Frame(popup)
            frame_instruct.grid(row=0, column=0, sticky="w")
            popup_instructions = tk.Label(
                master=frame_instruct,
                text = "Please enter your details below:",
                font=("Lucinds, 15"),
                padx=10,
                pady=10)
            popup_instructions.grid(row = 0, column=0, sticky="w")
            
            #creating text box for name
            frame_enter_name = tk.Frame(popup)
            frame_enter_name.grid(row=1, column=0, columnspan=2, sticky="w")
            enter_name = tk.Text(
                master=frame_enter_name,
                height = 1,
                font=("Lucinds, 10"),
                width = 20)
            enter_name.grid(row=1, column=1, sticky="w")

            #creating label for name
            lbl_name = tk.Label(
                master=frame_enter_name,
                text="Name:",
                font=("Lucinds, 15"),
                anchor="w",
                justify = "left",
                padx=20
                )
            lbl_name.grid(row=1, column=0, sticky="w")

            #making text box for phone number
            frame_enter_phoneno=tk.Frame(popup)
            frame_enter_phoneno.grid(row=2, column=0, columnspan=2, sticky="w")
            enter_phoneno = tk.Text(
                master=frame_enter_phoneno,
                height = 1,
                font=("Lucinds, 10"),
                width = 20)
            enter_phoneno.grid(row=2, column=1)

            #creating text box for phone number
            lbl_phoneno = tk.Label(
                master=frame_enter_phoneno,
                text="Phone number:",
                font=("Lucinds, 15"),
                anchor="w",
                padx=20
                )
            lbl_phoneno.grid(row=2, column=0, sticky="w", pady=20)

            #make order button
            order_btn = tk.Button(
                master=popup,
                text="order",
                font=("Lucinds, 13"),
                command=lambda: self.show_order(enter_name, enter_phoneno, popup, sauce_retr, meats_retr, veges_retr, main_retr)
                )
            order_btn.grid(row=3, column=1, sticky="e")



class Commands:
    def __init__(self, ingredients, layout):
        #variables for collecting the values (users choices)
        self.mainsvar = tk.StringVar(value=0)
        self.vegesvar = []
        self.meatsvar = []
        self.saucesvar = tk.StringVar(value=0)

        #assigning the parameters to a class variable so it can be accessed in other methods, not just innit
        self.ingredients = ingredients
        #making it layout.frame_header to pass through the frame_header from the layout class
        self.frame_header = layout.frame_header
        self.frame_mains_section = tk.Frame(self.frame_header, bg="#FDFDFB")
        self.frame_meats_section = tk.Frame(self.frame_header, bg="#FDFDFB")
        self.frame_vege_section = tk.Frame(self.frame_header, bg="#FDFDFB")
        self.submit = Submit(layout)
    
    #next button from step 3 wll open up step 4 collapsible section
    def step_4(self):
        self.frame_meats_section.destroy()
        frame_sauces_section = tk.Frame(self.frame_header, bg="#FDFDFB")
        label_sauces_section = tk.Label(
            master=frame_sauces_section,
            width=100,
            height=10,
            bg="#FDFDFB",
            highlightcolor = "#eee9e1"
        )
        label_sauces_section.grid(row=9, column=0, columnspan=4)
        frame_sauces_section.grid(row=9, column=0, columnspan=4, sticky="we")


        self.saucesvar = tk.StringVar()
        #making selecting options for sauces
        column = 0
        for text in self.ingredients[4]:
            self.sauce = tk.Radiobutton(
                master = label_sauces_section,
                text=text,
                bg="#FDFDFB",
                variable = self.saucesvar,
                value=text,
                font=("Lucinds, 13"),
                padx = 40,
                pady = 20
            )
            self.sauce.grid(row=0, column=column, sticky="w")
            column += 1
        self.saucesvar.set(0)

        #making button for siracha
        self.sauce = tk.Radiobutton(
            master = label_sauces_section,
            text="siracha",
            bg="#FDFDFB",
            variable = self.saucesvar,
            value="siracha",
            font=("Lucinds, 13"),
            padx = 40,
            pady = 20
        )
        self.sauce.grid(row=1, column=0, sticky="w")
            
        #going to the popup function
        finish_button = tk.Button(
            master=frame_sauces_section,
            text= "finish",
            bg="white",
            width=10,
            height=1,
            font=("Lucinds, 10"),
            command = lambda : self.submit.popup(frame_sauces_section, self.saucesvar.get(), self.meatsvar, self.vegesvar, self.mainsvar.get())
        )
        finish_button.grid(row=9, column=0, columnspan=4, sticky="se", pady=10, padx=10)

        

    #next button from step 2 wll open up step 3 collapsible section
    def step_3(self):
        self.frame_vege_section.destroy()
        self.frame_meats_section = tk.Frame(self.frame_header, bg="#FDFDFB")
        label_meats_section = tk.Label(
            master=self.frame_meats_section,
            width=100,
            height=10,
            bg="#FDFDFB"
        )
        label_meats_section.grid(row=0, column=0, columnspan=4)
        self.frame_meats_section.grid(row=7, column=0, columnspan=4, sticky="we")

        
        #making selecting options for meats first row
        column = 0
        self.meatsvar=[]
        for text in self.ingredients[3]:
            check_button_choice = tk.StringVar()
            self.meatsvar.append(check_button_choice)
            self.meats = tk.Checkbutton(
                master = label_meats_section,
                text=text,
                bg="#FDFDFB",
                variable = check_button_choice,
                onvalue=text,
                offvalue= "",
                font=("Lucinds, 13"),
                padx = 40,
                pady = 20
            )
            self.meats.grid(row=0, column=column, sticky="w")
            column += 1

        #making selecting options for meats second row
        column = 0
        for text in self.ingredients[2]:
            check_button_choice = tk.StringVar()
            self.meatsvar.append(check_button_choice)
            #self.meatsvar = tk.StringVar()
            self.meats = tk.Checkbutton(
                master = label_meats_section,
                text=text,
                bg="#FDFDFB",
                variable = check_button_choice,
                onvalue=text,
                offvalue= "",
                font=("Lucinds, 13"),
                padx = 40,
                pady = 20
            )
            self.meats.grid(row=1, column=column, sticky="w")
            column += 1
        
        #next button
        next_button_step3 = tk.Button(
                master=self.frame_meats_section,
                text= "next",
                bg="white",
                width=10,
                height=1,
                font=("Lucinds, 10"),
                command = lambda : [self.step_4()]
            )
        next_button_step3.grid(row=1, column=3, columnspan=4, sticky="se", pady=10, padx=10)

    #next button from step 1 will open up step 2 collapsible section
    def step_2(self):
        self.frame_mains_section.destroy()
        self.frame_vege_section = tk.Frame(self.frame_header, bg="#FDFDFB")

        label_vege_section = tk.Label(
            master=self.frame_vege_section,
            width=100,
            height=10,
            bg="#FDFDFB"
        )
        label_vege_section.grid(row=0, column=0, columnspan=4)
        self.frame_vege_section.grid(row=5, column=0, columnspan=4, sticky="we")

        #making selecting optios for vegetables 
        column = 0
        self.vegesvar=[]
        for text in self.ingredients[1]:
            check_button_choice = tk.StringVar()
            self.vegesvar.append(check_button_choice)
            self.veges = tk.Checkbutton(
                master = label_vege_section,
                text=text,
                bg="#FDFDFB",
                variable = check_button_choice,
                onvalue=text,
                offvalue= "",
                font=("Lucinds, 13"),
                padx = 40,
                pady = 20
            )
            self.veges.grid(row=1, column=column, sticky="w")
            column += 1


        #next button
        next_button_step2 = tk.Button(
                master=self.frame_vege_section,
                text= "next",
                bg="white",
                width=10,
                height=1,
                font=("Lucinds, 10"),
                command = lambda : [self.step_3()]
            )
        next_button_step2.grid(row=1, column=3, columnspan=4, sticky="e", pady=10, padx=10)

    #drop down section 1
    def step_1(self):
        self.frame_mains_section = tk.Frame(self.frame_header, bg="#FDFDFB")
        self.frame_mains_section.grid(row=3, column=0, columnspan=4, sticky="we")
        
        label_mains_section = tk.Label(
            master=self.frame_mains_section,
            width=100,
            height=10,
            bg="#FDFDFB"
        )
        label_mains_section.grid(row=0, column=0, columnspan=4)
           
        self.mainsvar = tk.StringVar()
        self.mainsvar.set(0)
        #making selecting options for sauces
        column = 0
        for text in self.ingredients[0]:
            self.main = tk.Radiobutton(
                master = label_mains_section,
                text=text,
                bg="#FDFDFB",
                variable = self.mainsvar,
                value=text,
                font=("Lucinds, 13"),
                padx = 80,
                pady = 20
            )
            self.main.grid(row=0, column=column, sticky="w")
            column += 1
        
        #next button
        next_button_step1 = tk.Button(
            master=self.frame_mains_section,
            text= "next",
            bg="white",
            width=10,
            height=1,
            font=("Lucinds, 10"),
            command=lambda : [self.step_2()]
            )
        next_button_step1.grid(row=1, column=3, columnspan=4, sticky="e", pady=10, padx=10)

        


class Layout:
               
    def __init__(self):
        
        root = tk.Tk()
        root.title("Bento Bowl Ordering")
        root.geometry("750x600")
        #makes it a fixed window size, doesn't have to be responsive
        root.resizable(False, False)
        root['bg'] = '#eee9e1'

        frame=tk.Frame(root,width=750,height=300)
        frame.pack(expand = True, fill=tk.BOTH)

        canvas = tk.Canvas(frame,bg="#fdfdfb", width = 750,height = 300,
                      scrollregion=(0,0,500,800))


        vbar = tk.Scrollbar(frame,orient = 'vertical')
        vbar.pack(side = 'right', fill = 'y')
        vbar.config(command = canvas.yview)

        canvas.config(width=750,height=300)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side='left', expand = True, fill = 'both')

        self.frame_header = tk.Frame(canvas)
        canvas.create_window((0, 0), window=self.frame_header, anchor='nw')
        self.root = root

        command = Commands(BentoBowl().return_lists(), self)

        #making header
        label_header = tk.Label(
                    master = self.frame_header,
                    text="Bento Bowl Ordering",
                    font=("Lucinds, 15"),
                    bg = "#fdfdfb",
                    width = 70,
                    height = 2,
                    anchor="w",
                    justify="left",
                    padx = 30
                    )
        label_header.grid(row=0, column=0, columnspan=2, sticky='news')

        #introduction
        label_intro = tk.Label(
            master=self.frame_header,
            text="Order your bento bowl here:",
            font=("Lucinds, 13"),
            bg="#B24C63",
            width = 70,
            height = 2,
            anchor="w",
            justify="left",
            padx = 10
            )
        label_intro.grid(row=1, column=0, columnspan=2, sticky='news')

        #making button for mains step 1
        choose_main="step 1: choose your mains"
        main_button = tk.Button(
            master = self.frame_header,
            text = choose_main,
            bg="#3A506B",
            height = 2,
            command = command.step_1,
            activebackground = "#ccd7e3",
            font=("Lucinds, 15"),
            anchor="w",
            padx = 10,
            fg = "#FDFDFB"
            )
        main_button.grid(row=2, column=0, columnspan=2, sticky='news')

        #making button for vege step 2
        choose_vege="step 2: choose your vegetables"

        vege_button = tk.Button(
            master=self.frame_header,
            text = choose_vege,
            bg="#3A506B",
            height = 2,
            command = command.step_2,
            activebackground = "#ccd7e3",
            font=("Lucinds, 15"),
            anchor="w",
            padx = 10,
            fg = "#FDFDFB"
            )
        vege_button.grid(row=4, column=0, columnspan=2, sticky='news')

        #making button for meats step 3
        choose_meats="step 3: choose your meats"

        meats_button = tk.Button(
            master=self.frame_header,
            text = choose_meats,
            bg="#3A506B",
            height = 2,
            command = command.step_3,
            activebackground = "#ccd7e3",
            font=("Lucinds, 15"),
            anchor="w",
            padx = 10,
            fg = "#FDFDFB"
            )
        meats_button.grid(row=6, column=0, columnspan=2, sticky='news')

        #making button for sauces step 4
        choose_sauces="step 4: choose your sauces"

        sauces_button = tk.Button(
            master=self.frame_header,
            text = choose_sauces,
            bg="#3A506B",
            height = 2,
            command = command.step_4,
            activebackground = "#ccd7e3",
            font=("Lucinds, 15"),
            anchor="w",
            padx = 10,
            fg = "#FDFDFB"
            )
        sauces_button.grid(row=8, column=0, columnspan=2, sticky='news') 
        
        root.mainloop()

        
Layout()
#passing the lists through the layout class so that it can be accessed for the selecting options
#Commands(BentoBowl().return_lists())

