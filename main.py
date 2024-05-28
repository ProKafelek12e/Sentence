import customtkinter
import tkinter as tk
from tkinter import filedialog
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Sentence")
        # Initiate File location variable
        self.FileLocation = ''

        # Create the menu bar
        menu = CTkMenuBar(master=self)
        
        # Add "File" cascade
        file_menu = menu.add_cascade("File")
        
        # Add dropdown options to the "File" cascade
        dropdown = CustomDropdownMenu(widget=file_menu)
        dropdown.add_option(option="Open",command=openFile)
        dropdown.add_option(option="Save",command=saveFile)
        # Add other cascades if needed
        # Display the menu bar
        self.config(menu=menu)

        self.textbox = customtkinter.CTkTextbox(master=self, width=580, height=500, corner_radius=0)
        self.textbox.pack(side='bottom',fill='both')
    
# File menu bar
def saveFile():
    if(app.FileLocation!=''):
        with open(app.FileLocation, 'w') as file:
            print(app.textbox.get('0.0','end'),file=file)
    else:
        print('Wrong location of the file')
def openFile():
    print('opened')
    root = tk.Tk()
    root.withdraw()
    # Open file dialog and return the selected file path
    app.FileLocation = filedialog.askopenfilename()
    if app.FileLocation:
        print(f"Selected file: {app.FileLocation}")
        with open(app.FileLocation, 'r') as file:
            content = file.read()
            app.textbox.delete('0.0','end')
            app.textbox.insert('0.0',content)
    else:
        print("No file selected")
        return None


app=App()
app.mainloop()