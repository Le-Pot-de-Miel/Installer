# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from tkinter import StringVar, IntVar, BooleanVar, Tk, Canvas

from gui.pages.page1.gui import Page1
from gui.pages.page2.gui import Page2
from gui.pages.page3.gui import Page3
from gui.pages.page4.gui import Page4
from gui.pages.page5.gui import Page5
from gui.pages.page6.gui import Page6

class MainWindow(Tk):
    global user

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Honebrain Installer")

        self.geometry("862x519")
        self.configure(bg="#003061")

        self.data = {
            "interface": StringVar(),
            "subnet": StringVar(),
            "nofakemachine": BooleanVar(),
            "ip_addresses": StringVar(),
            "num_services": StringVar(),
            "noftp": BooleanVar(),
            "ip_address": StringVar(),
            "port": StringVar(),
            "mail": StringVar(),
            "password": StringVar(),
            "dockerfile": StringVar(),
        }

        self.current_window = None

        self.canvas = Canvas(
            self,
            bg="#003061",
            height=519,
            width=862,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)

        # Loop through windows and place them
        self.windows = {
            "page1": Page1(self),
            "page2": Page2(self),
            "page3": Page3(self),
            "page4": Page4(self),
            "page5": Page5(self),
            "page6": Page6(self),
        }

        self.change_page("page1")

        self.current_window.place(x=0, y=0, width=862.0, height=519.0)

        self.current_window.tkraise()
        self.resizable(False, False)

    def change_page(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set ucrrent Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=862.0, height=519.0)
