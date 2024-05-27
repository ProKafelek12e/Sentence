import customtkinter
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Sentence")

        # Create the menu bar
        menu = CTkMenuBar(master=self)
        
        # Add "File" cascade
        file_menu = menu.add_cascade("File")
        
        # Add dropdown options to the "File" cascade
        dropdown = CustomDropdownMenu(widget=file_menu)
        dropdown.add_option(option="Open")
        dropdown.add_option(option="Save")

        # Add other cascades if needed
        
        # Display the menu bar
        self.config(menu=menu)

app=App()
app.mainloop()