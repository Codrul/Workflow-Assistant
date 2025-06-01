import customtkinter
import tkinter
from tkinter import filedialog, messagebox, ttk
import os
import subprocess

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
app = customtkinter.CTk()
app.title('Workflow Assistant')
app.geometry('900x600')

def show_timed_message(parent, message, timeout=500000):
    popup = customtkinter.CTkToplevel(parent)
    popup.geometry("300x100")
    popup.title("Info")

    label = customtkinter.CTkLabel(popup, text=message)
    label.pack(expand=True, padx=20, pady=20)

    popup.after(timeout, popup.destroy)

def open_filexplorer():
    file_path = filedialog.askopenfilename(title='Select a file')

def button1():
    print('This does absolutely nothing')

def scan_apps():
    program_dirs = [r"C:\Program Files", r"C:\Program Files (x86)"]
    apps = []
    for dir_path in program_dirs:
        if os.path.exists(dir_path):
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    if file.lower().endswith('.exe'):
                        apps.append(os.path.join(root, file))
    return apps

def on_app_selected(choice):
    full_path = next((app for app in apps if os.path.basename(app) == choice), None)
    if full_path:
        try:
            subprocess.Popen([full_path])
            show_timed_message(app, f"Launching {choice}", timeout=1500)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch {choice}:\n{e}")
    else:
        messagebox.showerror("Error", f"Path for {choice} not found.")


tabview = customtkinter.CTkTabview(app)
tabview.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

tabview.add('tab 1')
tabview.add('tab 2')
tabview.add('tab 3')

tabview.set('tab 1')


button1 = customtkinter.CTkButton(tabview.tab('tab 1'), text='Nothing', command=button1)
button1.grid(row=0, column=0, padx=10, pady=10)


apps = scan_apps()
app_names = [os.path.basename(app) for app in apps]

dropdown = ttk.Combobox(tabview.tab('tab 2'),
                        values=app_names,
                        width=60)
dropdown.bind("<<ComboboxSelected>>", lambda e: on_app_selected(dropdown.get()))
dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

tabview.tab('tab 2').grid_columnconfigure(0, weight=1)


file_picker_button = customtkinter.CTkButton(tabview.tab('tab 3'), text='Select a file', command=open_filexplorer)
file_picker_button.grid(row=0, column=0, padx=10, pady=10)


app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

app.mainloop()
