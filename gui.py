import customtkinter
from tkinter import filedialog

from func import save_app_path, open_saved_app, launch_selected, load_config

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

combo = None

app = customtkinter.CTk()
app.title('Workflow Assistant')
app.geometry('900x600')

def open_file_explorer():
    file_path = filedialog.askopenfilename(
        title = "Select an application",
        filetypes =[('Executable files', '*.exe')]
    )
    if file_path:
        choose_name_popup(file_path)

def choose_name_popup(file_path):
    popup = customtkinter.CTkToplevel(app)
    popup.title('What''s your application called?')
    popup.geometry('300x200')

    popup.transient(app)
    popup.focus()

    label = customtkinter.CTkLabel(popup, text= 'Enter the name of your application: ')
    label.pack(pady=10)

    entry = customtkinter.CTkEntry(popup, width=200)
    entry.pack(pady=5)

    def on_submit():
        app_name = entry.get().strip()
        if app_name:
            save_app_path(app_name, file_path)
            status_label.configure(text=f'Saved {app_name} with {file_path}')
            popup.destroy()
        else:
            entry.configure(placeholder_text='Please enter a valid name')

        global combo
        new_config_keys = load_config()
        new_app_names = list(new_config_keys)
        combo.configure(values=new_app_names)

    submit_button = customtkinter.CTkButton(popup, text= 'Save', command=on_submit)
    submit_button.pack(pady=10)


#selection button
select_button = customtkinter.CTkButton(app, text= 'Add application', command = open_file_explorer)
select_button.pack(pady=40)

#status label
status_label = customtkinter.CTkLabel(app, text='No application selected yet')
status_label.pack()

#open apps dropdown
config = load_config()  # This gives you the {app_name: path} dict
app_names = list(config.keys())
combo = customtkinter.CTkOptionMenu(app, values=app_names, width=300)
combo.place(x=20, y=20)

launch_button = customtkinter.CTkButton(
    app,
    text= 'Open application',
    command= lambda: launch_selected(None, combo, config)
)
launch_button.pack(pady=10)

app.mainloop()
