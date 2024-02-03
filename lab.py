import customtkinter
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import database

app=customtkinter.CTk()
app.title('AutoMobile Inventory Management-By Gunjan & Nayan')
app.geometry('900x600')
app.config(bg='#0A0B0C')
app.resizable(False,False)

font1=('ARIAL',35,'bold')
font2=('ARIAL',30,'bold')
font3=('ARIAL',12,'bold')

def create_chart():
   product_details=database.fetch_inventory()
   product_name=[product[1] for product in product_details]
   stock_values=[product[2] for product in product_details]

   figure=Figure(figsize=(8,3.8),dpi=80,facecolor='#0A0B0C')
   ax=figure.add_subplot(111)
   ax.bar(product_name,stock_values,width=0.4,color='#11EA05')
   ax.set_xlabel("Product Name",color='#fff',fontsize=10)
   ax.set_ylabel("Stock Value",color='#fff',fontsize=10)
   ax.set_title("Product Stock Levels",color='#fff',fontsize=12)
#    ax.tick_params(axis='x',labelcolor='#fff',fontsize=12)
#    ax.tick_params(axis='y',labelcolor='#fff',fontsize=12)
   ax.set_facecolor('#1B181B')

   canvas=FigureCanvasTkAgg(figure)
   canvas.draw()
   canvas.get_tk_widget().grid(row=0,column=0,padx=475,pady=405)


def Update():
   selected_item=tree.focus()
   if not selected_item:
     messagebox.showerror('Error','Choose a Product to update')
   else:
     id=id_entry.get()
     name=name_entry.get()
     stock=stock_entry.get()
     price=price_entry.get()
     database.update_inventory(name,stock,price,id)
     add_to_treeview()
     clear()
     create_chart()
     messagebox.showinfo('Success','Data has Been Updated')
      

def display(event):
   selected_item=tree.focus()
   if selected_item:
      row=tree.item(selected_item)['values']
      clear()
      id_entry.insert(0,row[0])
      name_entry.insert(0,row[0])
      stock_entry.insert(0,row[0])
      price_entry.insert(0,row[0])
   else:
      pass

def delete():
   selected_item=tree.focus()
   if not selected_item:
      messagebox.showerror('Error','Choose a Product To Delete')
   else:
      id=id_entry.get()
      database.delete_inventory(id)
      add_to_treeview()
      clear()
      create_chart()
      messagebox.showinfo('Success','Data Has Been Deleted')



def add_to_treeview():
   inventory=database.fetch_inventory()
   tree.delete(*tree.get_children())
   for product in inventory:
      tree.insert('',END,values=product)

def clear(*clicked):
  if clicked:
   tree.selection_remove(tree.focus())
   tree.focus('')
  id_entry.delete(0,END)
  name_entry.delete(0,END)
  stock_entry.delete(0,END)
  price_entry.delete(0,END)


def insert():
     id=id_entry.get()
     name=name_entry.get()
     stock=stock_entry.get()
     price= price_entry.get()

     if not(id and name and stock and price):
        messagebox.showerror('Error','Enter all fields.')
     elif database.id_exists(id):
       messagebox.showerror('Error','ID already exits.')
     else:
         try:
            stock_value=int(stock)
            database.insert_inventory(id,name,stock_value,price)
            add_to_treeview()
            clear()  
            create_chart()
            messagebox.showinfo('Success','Data has been inserted.')
         except ValueError:
            messagebox.showerror('Error','stock should be an Integer.')


title_label=customtkinter.CTkLabel(app,font=font1,text='Product Details',text_color='white',bg_color='#0A0B0C')
title_label.place(x=70,y=13)

frame=customtkinter.CTkFrame(app,bg_color="#0A0B0C",fg_color='#1B1B21',corner_radius=10,border_width=2,border_color='#fff',width=300,height=470)
frame.place(x=45,y=55)

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

add_button=customtkinter.CTkButton(frame,command=insert,font=font2,text_color='#fff',text="Add",fg_color='#047E43',hover_color='#025B30',bg_color='#1B1B21',cursor='hand2',corner_radius=8,width=80)
add_button.place(x=55,y=350)

clear_button=customtkinter.CTkButton(frame,command=lambda:clear(True),font=font2,text_color='#fff',text="Clear",fg_color='#047E43',hover_color='#025B30',bg_color='#1B1B21',cursor='hand2',corner_radius=8,width=80)
clear_button.place(x=150,y=350)

update_button=customtkinter.CTkButton(frame,command=Update,font=font2,text_color='#fff',text="Update",fg_color='#047E43',hover_color='#025B30',bg_color='#1B1B21',cursor='hand2',corner_radius=8,width=80)
update_button.place(x=28,y=400)

delete_button=customtkinter.CTkButton(frame,command=delete,font=font2,text_color='#fff',text="Delete",fg_color='#047E43',hover_color='#025B30',bg_color='#1B1B21',cursor='hand2',corner_radius=8,width=80)
delete_button.place(x=160,y=400)


style=ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview',font=font3,foreground='#fff',background='#0AB04A7',fieldbackground='#1B1B21')
style.map('Treeview',background=[('selected','#AA04A7')])


tree=ttk.Treeview(app,height=17)

tree['columns']=('ID','Product Name','In Stock','Price')

tree.column('#0',width=0,stretch=tk.NO)
tree.column('ID',anchor=tk.CENTER,width=150)
tree.column('Product Name',anchor=tk.CENTER,width=150)
tree.column('In Stock',anchor=tk.CENTER,width=150)
tree.column('Price',anchor=tk.CENTER,width=150)

tree.heading('ID',text='ID')
tree.heading('Product Name',text='Product Name')
tree.heading('In Stock',text='In Stock')
tree.heading('Price',text='Price') 

tree.place(x=475,y=25)
tree.bind('<ButtonRelease>',display)

add_to_treeview()
create_chart()
app.mainloop()
