#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Macro app
"""
from tkinter import *
from food import *


def main():
    '''
    Main program loop
    '''
    update_count()
    main_menu()
    root.mainloop()


def log_meal():
    '''
    Retrieves macronutrient valus from entries and appends the values
    to a history file
    '''
    macros = []
    for item in log_macro_entries:
        try:
            macros.append(int(item.get()))
        except ValueError:
            macros.append(0)
    macros.append(macros[0]*4 + macros[1]*4 + macros[2]*9)
    write_file(macros)
    clear_entries(log_macro_entries)
    update_count()
    hide_log()
    main_menu()
    
# 
def update_count():
    '''
    Updates macronutrient total labels
    '''
    macros = read_file(get_date()[0])
    for item, x in zip(total_labels, range(len(total_labels))):
        item.configure(text = total_texts[x] + str(macros[x]))
        

def log_menu():
    '''
    Display screen allowing the user to choose whether to enter the name of a
    food or enter exact macronutrient values
    '''
    hide_main()
    show_widgets(log_menu_items)
        
        
def hide_log_menu():
    '''
    Hides the log meal menu
    '''
    hide_widgets(log_menu_items)
        
        
def log_macro():
    '''
    Displays screen allowing the user to enter the macronutrient values 
    of their meal
    '''
    Displays 
    hide_log_menu()
    
    for label, entry, x in zip(log_labels, log_macro_entries, range(3)):
        label.grid(row = x, column = 0)
        entry.grid(row = x, column = 1)
    
    enter_logmeal.grid(row = 3, column = 1)
    
    for item, x in zip(total_labels[:3], range(3)):
        item.grid(row = 4, column = x)    
    

def hide_main():
    '''
    Hides main menu
    '''
    hide_widgets(main_menu_items)
      
    
def hide_log():
    '''
    Hides log meal menu
    '''
    hide_widgets(log_macro_items)


def main_menu():
    '''
    Shows main menu
    '''
    show_widgets(main_menu_items)


def label_maker(texts):
    '''
    Creates a label for each item in a list of label texts
    '''
    labels = []
    for item in texts:
        label = Label(root, text = item)
        labels.append(label)
    return labels


def entry_maker(num):
    '''
    Creates num amount of entries
    '''
    entries = []
    for item in range(num):
        entry = Entry(root)
        entries.append(entry)
    return entries


def clear_entries(entries):
    '''
    Clears text from entries
    '''
    for item in entries:
        item.delete(0,END)
        
        
def show_widgets(widgets):
    '''
    Displays all widgets in a list of widgets
    '''
    x = 0
    for item in widgets:
        for widget in item:
            widget.grid(row = x, column = 0)
            x += 1
            

def hide_widgets(widgets):
    '''
    Hides all widgets in a list of widgets
    '''
    for item in widgets:
        for widget in item:
            widget.grid_forget()


def show_history():
    '''
    Displays history menu
    '''
    hide_main()
    show_widgets(history_items)


def hide_history():
    '''
    Hides history screen 
    '''
    hide_widgets(history_items)
    main_menu()


def history_texts():
    '''
    Generates label texts displaying macronutrient totals from previous days
    '''
    dates = get_history()
    out = []
    for item in dates:
       var = str(item['date']) + ': ' + str(item['calories']) + ' calories'
       out.append(var)
     
    return out


def log_food_menu():
    '''
    Displays screen allowing the user to enter the name of a food 
    '''
    hide_log_menu()
    for label, entry, x in zip(log_food_labels, log_food_entries, range(2)):
        label.grid(row = x, column = 0)
        entry.grid(row = x, column = 1)
    enter_logfood.grid(row = 2, column = 1)

# ADD TRY EXCEPT
def log_food():
    '''
    Retrieves the macronutrient totals for a food and appends them to a 
    history file
    '''
    find_food(log_food_entries[0].get(), int(log_food_entries[1].get())) 
    clear_entries(log_food_entries)
    update_count()
    hide_widgets(log_food_items)
    main_menu()
    

def find_food(name, serving):
    '''
    Returns the macronutrient totals of a food
    '''
    macros = []
    keys = ['carbs','protein','fat']
    for item in food_dicts:
        if item['name'] == name.strip().lower():
            for var in keys:
                macros.append(item[var]*serving)
            macros.append(macros[0]*4 + macros[1]*4 + macros[2]*9)
            write_file(macros)
            break
    
            
root = Tk()
root.title("Meal Tracker")

# Main menu widgets
date_label = Label(root, text = str(get_date()[0]))
date_labels = [date_label]

total_texts = ["Total Carbs: ", "Total Protein: ", "Total Fat: ", 
               "Total Calories: "]
total_labels = label_maker(total_texts)

button0 = Button(None, text = "Log Meal", command = log_menu)
button1 = Button(None, text = "View History", command = show_history)

main_menu_buttons = [button0, button1]
main_menu_items = [date_labels, main_menu_buttons, total_labels]

# History screen widgets
history_labels = label_maker(history_texts())

button2 = Button(None, text = "Main Menu", command = hide_history)

history_buttons = [button2]

history_items = [history_labels, history_buttons]

# Log menu screen widgets
log_texts = ["Carbs:","Protein:","Fat:"]
log_labels = label_maker(log_texts)

log_food_texts = ['Food: ', 'Servings: ']
log_food_labels = label_maker(log_food_texts)

log_macro_entries = entry_maker(3)
log_food_entries = entry_maker(2)

enter_logfood = Button(None, text = "Enter", command = log_food)
enter_logmeal = Button(None, text = "Enter", command = log_meal)

button3 = Button(None, text = "Enter Macros", command = log_macro)
button4 = Button(None, text = "Enter Food", command = log_food_menu)

log_menu_buttons = [button3, button4]
log_menu_items = [log_menu_buttons]

log_macro_buttons = [enter_logmeal]
log_macro_items = [log_labels, total_labels, log_macro_entries, log_macro_buttons]

log_food_buttons = [enter_logfood]
log_food_items = [log_food_entries,log_food_labels, log_food_buttons]


main()








