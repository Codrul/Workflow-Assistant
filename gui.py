import customtkinter as ctk

def button_callback():
    print("button clicked")

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')
app = ctk.CTk()
app.title("Workflow Assistant")
app.geometry("600x250")

button = ctk.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()