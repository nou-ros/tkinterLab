from tkinter import *
from tkinter import messagebox
from db import Database

# 16
db = Database('store.db')


#12 functions
def populate_list():
    # print('populate')
    # 17
    #to delete everything for the second time if we call the populate_list twice 
    parts_list.delete(0,END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    # print('Add')
    # 18
    if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return 

    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    parts_list.delete(0,END)
    parts_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    populate_list()


# 19
def select_item(event):
    # print('selected')
    global selected_item
    index = parts_list.curselection()[0]
    selected_item = parts_list.get(index)
    # print(selected_item)

    part_entry.delete(0, END)
    part_entry.insert(END, selected_item[1])
    customer_entry.delete(0, END)
    customer_entry.insert(END, selected_item[2])
    retailer_entry.delete(0, END)
    retailer_entry.insert(END, selected_item[3])
    price_entry.delete(0, END)
    price_entry.insert(END, selected_item[4])
   

def remove_item():
    # print('remove')
    db.remove(selected_item[0])
    populate_list()

def update_item():
    print('Update')

def clear_item():
    print('clear')

#(1) create window object
app = Tk()

#(4) part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 10), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

#(5) Customer 
customer_text = StringVar()
customer_label = Label(app, text='Customer Name', font=('bold', 10))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)


#(6) Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer Name', font=('bold', 10))
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)


#(7) Price
price_text = StringVar()
price_label = Label(app, text='Price Name', font=('bold', 10))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

#(8) Parts List(Listbox)
parts_list = Listbox(app, height=10, width=60, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#(9) Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

#(10) Connect scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# 19  Bind select
parts_list.bind('<<ListboxSelect>>', select_item)


#(11) buttons
add_btn = Button(app, text="Add Part", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text="Remove Part", width=12, command=remove_item)
remove_btn.grid(row=2, column=1 )

update_btn = Button(app, text="Update Part", width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text="Clear Input", width=12, command=clear_item)
clear_btn.grid(row=2, column=3)

#(3) app title
app.title('Part Manager')

#(4) for app size
app.geometry('600x350')


#(13)populate data
populate_list()


#(2) Start program 
app.mainloop()