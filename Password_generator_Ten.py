import customtkinter
import tkinter
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('green')

length = 8
a = "qwertyuiopasdfghjklzxcvbnm"
b = "QWERTYUIOPASDFGHJKLZXCVBNM"
c = "0123456789"
d = "@#$_&-+()/*'%~]["
symbols = a + c

app = customtkinter.CTk()
app.title('Ten PG')
app.geometry('500x320')
app.resizable(False, False)

frame = customtkinter.CTkFrame(master=app, width=430, height=150, corner_radius=0, bg_color='black')
frame.pack(padx=20, pady=20)

check_var = tkinter.StringVar(value='off')
check_var_symbols = tkinter.StringVar(value='off')

def update_symbols():
    global symbols
    symbols = a + c
    if check_var.get() == 'on':
        symbols += b
    if check_var_symbols.get() == 'on':
        symbols += d

def checkbox_az():
    update_symbols()

def checkbox_symbols():
    update_symbols()

checkbox = customtkinter.CTkCheckBox(master=frame, text="A-Z", command=checkbox_az, variable=check_var, onvalue='on', offvalue='off')
checkbox.pack(padx=0.5, pady=0.5)

checkbox1 = customtkinter.CTkCheckBox(master=frame, text="@&?-_!", command=checkbox_symbols, variable=check_var_symbols, onvalue='on', offvalue='off')
checkbox1.pack(padx=0.5, pady=0.6)

def clear():
    text_field.delete(0.0, tkinter.END)

button1 = customtkinter.CTkButton(master=app, width=70, height=30, text='Очистить', command=clear)
button1.place(relx=0.66, rely=0.52)

text_field = customtkinter.CTkTextbox(master=app, width=140, height=37)
text_field.insert(index='0.0', text='')
text_field.place(relx=0.36, rely=0.51)

def generate():
    global length
    password = "".join(random.sample(symbols, length))
    text_field.delete(0.0, tkinter.END)
    text_field.insert(tkinter.END, password)

button = customtkinter.CTkButton(master=app, text="Сгенерировать", command=generate)
button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app, text='Длина вашего пароля', width=140, height=20)
label.place(relx=0.36, rely=0.33)

plf = customtkinter.CTkLabel(master=app, width=40, height=30)
plf.place(relx=0.7, rely=0.35)
plf.configure(text=str(length))

def slider_event(value):
    global length
    length = int(round(float(value)))
    plf.configure(text=str(length))

slider = customtkinter.CTkSlider(master=app, from_=8, to=30, command=slider_event)
slider.place(relx=0.3, rely=0.4)

app.mainloop()