import customtkinter
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import database

app=customtkinter.CTk()
app.title('AutoMobile Inventory Management')
app.geometry('900x700')
app.config(bg='#0A0B0C')
app.resizable(False,False)

font1=('ARIAL',35,'bold')
font2=('ARIAL',30,'bold')
font3=('ARIAL',15,'bold')

title_label=customtkinter.CTkLabel(app,font=font1,text='Product Details',text_color='white',bg_color='#0A0B0C')
title_label.place(x=70,y=13)

frame=customtkinter.CTkFrame(app,bg_color="#0A0B0C",fg_color='#1B1B21',corner_radius=10,border_width=2,border_color='#fff',width=300,height=470)
frame.place(x=45,y=55)

# image1=PhotoImage(file="1.png")
# image1_label=Label(frame,image=image1,bg='#1B1B21')
# image1_label.place(x=65,y=5)

id_label=customtkinter.CTkLabel(frame,font=font2,text="Product ID  ",text_color='white',bg_color='#1B1B21')
id_label.place(x=73,y=20)
id_entry=customtkinter.CTkEntry(frame,font=font3,text_color='#000',fg_color='#fff',width=210)
id_entry.place(x=50,y=55)

name_label=customtkinter.CTkLabel(frame,font=font2,text="Product Name  ",text_color='#fff',bg_color='#1B1B21')
name_label.place(x=50,y=95)
name_entry=customtkinter.CTkEntry(frame,font=font3,text_color='#000',fg_color='#fff',width=210)
name_entry.place(x=50,y=130)

stock_label=customtkinter.CTkLabel(frame,font=font2,text="In Stock  ",text_color='#fff')
stock_label.place(x=100,y=175)
stock_entry=customtkinter.CTkEntry(frame,font=font3,text_color='#000',fg_color='#fff',width=210)
stock_entry.place(x=50,y=215)

price_label=customtkinter.CTkLabel(frame,font=font2,text="Price ",text_color='#fff')
price_label.place(x=120,y=255)
price_entry=customtkinter.CTkEntry(frame,font=font3,text_color='#000',fg_color='#fff',width=210)
price_entry.place(x=50,y=290)

add_button=customtkinter.CTkButton(frame,font=font2,text_color='#fff',text="Add",fg_color='#047E43',hover_color='#025B30',bg_color='#1B1B21',cursor='hand2',corner_radius=8,width=80)
add_button.place(x=55,y=350)

clear_button=customtkinter.CTkButton(frame,font=font2,text_color='#fff',text="Clear",fg_color='#047E43',hover_color='#025B30',bg_color='#1B1B21',cursor='hand2',corner_radius=8,width=80)
clear_button.place(x=150,y=350)

update_button=customtkinter.CTkButton(frame,font=font2,text_color='#fff',text="Update",fg_color='#047E43',hover_color='#025B30',bg_color='#1B1B21',cursor='hand2',corner_radius=8,width=80)
update_button.place(x=28,y=400)

delete_button=customtkinter.CTkButton(frame,font=font2,text_color='#fff',text="Delete",fg_color='#047E43',hover_color='#025B30',bg_color='#1B1B21',cursor='hand2',corner_radius=8,width=80)
delete_button.place(x=160,y=400)

# style=ttk.Style(app)

# style.theme_use('clam')
# style.configure('Treeview',font=font3,foreground='#fff',background='#0AB04A7',fieldbackground='#1B1B21')
# style.map('Treeview',background=[('selected','#AA04A7')])


# tree=ttk.Treeview(app,height=17)

# tree['columns']=('Product ID','Product Name','In Stock','Price')

# tree.column('Product ID',anchor=tk.CENTER,width=150)
# tree.column('Product Name',anchor=tk.CENTER,width=150)
# tree.column('In Stock',anchor=tk.CENTER,width=150)
# tree.column('Price',anchor=tk.CENTER,width=150)

# tree.heading('Product ID ',text='Product ID')
# tree.heading('Product Name',text='Product Name')
# tree.heading('In Stock',text='In Stock')
# tree.heading('Price',text='Price')

# tree.place(x=300,y=45)

app.mainloop()
