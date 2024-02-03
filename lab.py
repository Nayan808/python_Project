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

font1=('ARIAL',30,'bold')
font2=('ARIAL',30,'bold')
font3=('ARIAL',30,'bold')

app.mainloop()