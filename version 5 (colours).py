"""
version 5
author: Ashlee Shum
description: colours
"""


import tkinter as tk
from tkinter import ttk

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

        canvas = tk.Canvas(frame,bg='pink', width = 750,height = 600,
                      scrollregion=(0,0,500,1500))


        vbar = tk.Scrollbar(frame,orient = 'vertical')
        vbar.pack(side = 'right', fill = 'y')
        vbar.config(command = canvas.yview)

        canvas.config(width=750,height=300)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side='left', expand = True, fill = 'both')

        frame_header = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_header, anchor='nw')

        #making header
        label_header = tk.Label(
                    master = frame_header,
                    text="bento bowl ordering",
                    font=(", 15"),
                    bg = "#8bb993",
                    width = 70,
                    height = 2,
                    anchor="w",
                    justify="left"
                    )
        label_header.grid(row=0, column=0, columnspan=2, sticky='news')

        #introduction
        label_intro = tk.Label(
            master=frame_header,
            text="order your bento bowl here:",
            font=("Lucinds,20"),
            bg="grey",
            width = 70,
            height = 3,
            anchor="w",
            justify="left"
            )
        label_intro.grid(row=1, column=0, columnspan=2, sticky='news')

        # creating functions for collapsing sections
        def transition1(frm_main):
            frm_main.grid_remove()
            step_2()

        def transition2(frm_vege):
            frm_vege.grid_remove()
            step_3()

        def transition3(frm_meats):
            frm_meats.grid_remove()
            step_4()

        def transition4(frm_sauces):
            frm_sauces.grid_remove()

        
        #next button from step 3 wll open up step 4 collapsible section
        def step_4():
            frame_sauces_section = tk.Frame(frame_header, bg="#eee9e1")
            label_sauces_section = tk.Label(
                master=frame_sauces_section,
                width=100,
                height=10,
                bg="#eee9e1",
                highlightcolor = "#eee9e1"
            )
            label_sauces_section.grid(row=9, column=0, columnspan=4)
            frame_sauces_section.grid(row=9, column=0, columnspan=4, sticky="we")

            #making selecting options for sauces
            self.sauces = tk.IntVar()
            main_mayo = tk.Radiobutton(
                    master = label_sauces_section,
                    text="kewpie mayo",
                    bg="#eee9e1",
                    variable = self.sauces,
                    value=1,
                    font=("Lucinds, 13"),
                    padx = 40,
                    pady = 20
                    )
            main_mayo.grid(row=0, column=0, sticky="w")

            main_teriyakisauce = tk.Radiobutton(
                    master = label_sauces_section,
                    text="teriyaki chicken sauce",
                    bg="#eee9e1",
                    variable = self.sauces,
                    value=2,
                    font=("Lucinds, 13"),
                    padx = 40,
                    pady = 20
                    )
            main_teriyakisauce.grid(row=0, column=1, sticky="w")

            main_bbq = tk.Radiobutton(
                    master = label_sauces_section,
                    text="BBQ sauce",
                    bg="#eee9e1",
                    variable = self.sauces,
                    value=3,
                    font=("Lucinds, 13"),
                    padx = 40,
                    pady = 20
                    )
            main_bbq.grid(row=0, column=2, sticky="w")

            main_siracha = tk.Radiobutton(
                    master = label_sauces_section,
                    text="siracha",
                    bg="#eee9e1",
                    variable = self.sauces,
                    value=4,
                    font=("Lucinds, 13"),
                    padx = 40,
                    pady = 20
                    )
            main_siracha.grid(row=1, column=0, sticky="w")

            #next button
            next_button_step4 = tk.Button(
                master=frame_sauces_section,
                    text= "finish",
                    bg="white",
                    width=10,
                    height=1,
                    font=("Lucinds, 10"),
                    command = lambda : transition4(frame_sauces_section)
                )
            next_button_step4.grid(row=9, column=0, columnspan=4, sticky="se", pady=10, padx=10)

        #next button from step 2 wll open up step 3 collapsible section
        def step_3():
            frame_meats_section = tk.Frame(frame_header, bg="#eee9e1")
            label_meats_section = tk.Label(
                master=frame_meats_section,
                width=100,
                height=10,
                bg="#eee9e1"
            )
            label_meats_section.grid(row=0, column=0, columnspan=4)
            frame_meats_section.grid(row=7, column=0, columnspan=4, sticky="we")

            #making content (select options)
            self.meats = tk.IntVar()
            main_karage = tk.Checkbutton(
                    master = label_meats_section,
                    text="chicken karage",
                    variable = self.meats,
                    bg="#eee9e1",
                    onvalue=1,
                    font=("Lucinds, 13"),
                    padx = 40,
                    pady = 20
                    )
            main_karage.grid(row=0, column=0, sticky="w")
            
            main_karagespicy = tk.Checkbutton(
                    master = label_meats_section,
                    text="chicken karage (spicy)",
                    bg="#eee9e1",
                    variable = self.meats,
                    onvalue=2,
                    font=("Lucinds, 13"),
                    padx = 40,
                    pady = 20
                    )
            main_karagespicy.grid(row=0, column=1, sticky="w")

            main_katsu = tk.Checkbutton(
                    master = label_meats_section,
                    text="chicken katsu",
                    bg="#eee9e1",
                    variable = self.meats,
                    onvalue=3,
                    font=("Lucinds, 13"),
                    padx = 40,
                    pady = 20
                    )
            main_katsu.grid(row=0, column=2, sticky="w")

            main_tempura = tk.Checkbutton(
                    master = label_meats_section,
                    text="tempura",
                    bg="#eee9e1",
                    variable = self.meats,
                    onvalue=4,
                    font=("Lucinds, 13"),
                    padx = 40,
                    pady = 20
                    )
            main_tempura.grid(row=1, column=0, sticky="w")

            main_salmon = tk.Checkbutton(
                    master = label_meats_section,
                    text="salmon",
                    bg="#eee9e1",
                    variable = self.meats,
                    onvalue=5,
                    font=("Lucinds, 13"),
                    padx = 40,
                    pady = 20
                    )
            main_salmon.grid(row=1, column=1, sticky="w")

            main_teriyakichk = tk.Checkbutton(
                    master = label_meats_section,
                    text="teriyaki chicken",
                    bg="#eee9e1",
                    variable = self.meats,
                    onvalue=6,
                    font=("Lucinds, 13"),
                    padx = 40,
                    pady = 20
                    )
            main_teriyakichk.grid(row=1, column=2, sticky="w")

            #next button
            next_button_step3 = tk.Button(
                    master=frame_meats_section,
                    text= "next",
                    bg="white",
                    width=10,
                    height=1,
                    font=("Lucinds, 10"),
                    command = lambda : transition3(frame_meats_section)
                )
            next_button_step3.grid(row=1, column=3, columnspan=4, sticky="se", pady=10, padx=10)

        #next button from step 1 will open up step 2 collapsible section
        def step_2():
            frame_vege_section = tk.Frame(frame_header, bg="#eee9e1")

            label_vege_section = tk.Label(
                master=frame_vege_section,
                width=100,
                height=10,
                bg="#eee9e1"
            )
            label_vege_section.grid(row=0, column=0, columnspan=4)
            frame_vege_section.grid(row=5, column=0, columnspan=4, sticky="we")

            self.vege = tk.IntVar()
            main_stirfry = tk.Checkbutton(
                    master = label_vege_section,
                    text="stir fry vegetables",
                    bg="#eee9e1",
                    variable = self.vege,
                    onvalue=1,
                    font=("Lucinds, 13"),
                    padx = 25,
                    pady = 20
                    )
            main_stirfry.grid(row=0, column=0, sticky="w")
            
            main_salad = tk.Radiobutton(
                    master = label_vege_section,
                    text="salad (spinach, carates, lettuce)",
                    bg="#eee9e1",
                    variable = self.vege,
                    onvalue=2,
                    font=("Lucinds, 13"),
                    padx = 25,
                    pady = 20
                    )
            main_salad.grid(row=0, column=1, sticky="w")

            main_edamame = tk.Checkbutton(
                    master = label_vege_section,
                    text="edamame beans",
                    bg="#eee9e1",
                    variable = self.vege,
                    onvalue=3,
                    font=("Lucinds, 13"),
                    padx = 25,
                    pady = 20
                    )
            main_edamame.grid(row=0, column=3, sticky="w")

            main_beetroot = tk.Checkbutton(
                    master = label_vege_section,
                    text="beetroot",
                    bg="#eee9e1",
                    variable = self.vege,
                    onvalue=4,
                    font=("Lucinds, 13"),
                    padx = 25,
                    pady = 20,
                    )
            main_beetroot.grid(row=1, column=0, sticky="w")

            #next button
            next_button_step2 = tk.Button(
                    master=frame_vege_section,
                    text= "next",
                    bg="white",
                    width=10,
                    height=1,
                    font=("Lucinds, 10"),
                    command = lambda : transition2(frame_vege_section)
                )
            next_button_step2.grid(row=1, column=3, columnspan=4, sticky="e", pady=10, padx=10)

        #drop down section 1
        def step_1():
            frame_mains_section = tk.Frame(frame_header, bg="#eee9e1")
            frame_mains_section.grid(row=3, column=0, columnspan=4, sticky="we")
            
            label_mains_section = tk.Label(
                master=frame_mains_section,
                width=100,
                height=10,
                bg="#eee9e1"
            )
            label_mains_section.grid(row=0, column=0, columnspan=4)

            #creating function for when radiobutton gets selected
               
            self.main = tk.IntVar()
            main_rice = tk.Radiobutton(
                    master = label_mains_section,
                    text="rice",
                    bg="#eee9e1",
                    variable = self.main,
                    value=1,
                    font=("Lucinds, 13"),
                    padx = 80,
                    pady = 20
                    )
            main_rice.grid(row=0, column=0, sticky="w")
            
            main_noodles = tk.Radiobutton(
                    master = label_mains_section,
                    text="noodles",
                    bg="#eee9e1",
                    variable = self.main,
                    value=2,
                    font=("Lucinds, 13"),
                    padx = 80,
                    pady = 20
                    )
            main_noodles.grid(row=0, column=1, sticky="w")

            main_brownrice = tk.Radiobutton(
                    master = label_mains_section,
                    text="brown rice",
                    bg="#eee9e1",
                    variable = self.main,
                    value=3,
                    font=("Lucinds, 13"),
                    padx = 80,
                    pady = 20
                    )
            main_brownrice.grid(row=0, column=3, sticky="w")
            
            #next button
            next_button_step1 = tk.Button(
                master=frame_mains_section,
                text= "next",
                bg="white",
                width=10,
                height=1,
                font=("Lucinds, 10"),
                command=lambda : transition1(frame_mains_section)
                )
            next_button_step1.grid(row=1, column=3, columnspan=4, sticky="e", pady=10, padx=10)

        self.v = tk.IntVar()
        
        #making button for mains step 1
        choose_main=["step 1: choose your mains here"]
        main_button = tk.Radiobutton(
            master = frame_header,
            text = choose_main,
            bg="#f6e8d5",
            variable = self.v,
            value= 1,
            height = 2,
            command = step_1,
            indicatoron = 0,
            font=("Lucinds, 15"),
            anchor="w"
            )
        main_button.grid(row=2, column=0, columnspan=2, sticky='news')

        #making button for vege step 2
        choose_vege=["step 2: choose your vegetables here"]

        vege_button = tk.Radiobutton(
            master=frame_header,
            text = choose_vege,
            bg="#f6e8d5",
            variable = self.v,
            value = 2,
            height = 2,
            command = step_2,
            indicatoron = 0,
            font=("Lucinds, 15"),
            anchor="w"
            )
        vege_button.grid(row=4, column=0, columnspan=2, sticky='news')

        #making button for meats step 3
        choose_meats=["step 3: choose your meats here"]

        meats_button = tk.Radiobutton(
            master=frame_header,
            text = choose_meats,
            bg="#f6e8d5",
            variable = self.v,
            value = 3,
            height = 2,
            command = step_3,
            indicatoron = 0,
            font=("Lucinds, 15"),
            anchor="w"
            )
        meats_button.grid(row=6, column=0, columnspan=2, sticky='news')

        #making button for sauces step 4
        choose_sauces=["step 4: choose your sauces here"]

        sauces_button = tk.Radiobutton(
            master=frame_header,
            text = choose_sauces,
            bg="#f6e8d5",
            variable = self.v,
            value = 4,
            height = 2,
            command = step_4,
            indicatoron = 0,
            font=("Lucinds, 15"),
            anchor="w"
            )
        sauces_button.grid(row=8, column=0, columnspan=2, sticky='news')

        #creating text box for name
        frame_enter_name = tk.Frame(frame_header, bg="#eee9e1")
        frame_enter_name.grid(row=10, column=0, sticky="w")
        enter_name = tk.Text(
            master=frame_enter_name,
            height = 1,
            width = 30)
        enter_name.grid(row=10, column=0)

        #creating label for name
        lbl_name = tk.Label(
            master=frame_enter_name,
            text="name:",
            bg="#eee9e1",
            font=("Lucinds, 15"),
            anchor="w",
            justify = "left",
            )
        lbl_name.grid(row=10, column=0, sticky="w")

        #making text box for phone number
        frame_enter_phoneno=tk.Frame(frame_header, bg="#eee9e1")
        frame_enter_phoneno.grid(row=10, column=1, sticky="w")
        enter_phoneno = tk.Text(
            master=frame_enter_phoneno,
            height = 1,
            width = 30)
        enter_phoneno.grid(row=10, column=1)

        #creating text box for phone number
        lbl_phoneno = tk.Label(
            master=frame_enter_phoneno,
            text="phone number:",
            bg="#eee9e1",
            font=("Lucinds, 15"),
            anchor="w"
            )
        lbl_phoneno.grid(row=10, column=0, sticky="w", pady=20)

        #creating order button
        order_button = tk.Button(
            master=frame_header,
            text="order",
            font=("Lucinds, 15"),
            anchor="e"
            )
        order_button.grid(row=12, column=1, sticky="e", pady=10, padx=90)



        root.mainloop()

Layout()
