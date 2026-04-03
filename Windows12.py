from typing import Any, Tuple
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from PIL import Image
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Windows 12")
        self.attributes(fullscreen=True)
        self.geometry("1200x800")
        self.iconbitmap("logo.ico")
        self.backgroundimg = Image.open("background.png")
        self.backgroundctk = ctk.CTkImage(self.backgroundimg, size=(1200, 800))
        self.background = ctk.CTkLabel(self, image=self.backgroundctk, text="")
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.resizebackground)
        Taskbar = TaskbarFrame(self.background, height=50)
        Taskbar.place(x=0, y=0, relwidth=1)
        self.startmenuopened: bool = False
        self.startmenu = StartMenuFrame(self.background, width=300, height=300)
        self.startmenu.grid_propagate(False)
        self.startmenuimg = Image.open("logo.png")
        self.startmenuimgctk = ctk.CTkImage(self.startmenuimg, size=(50, 50))
        self.startmenubtn = ctk.CTkButton(
            Taskbar,
            text="",
            border_width=0,
            image=self.startmenuimgctk,
            command=self.openstartmenu,
            width=50,
            height=50,
            fg_color="transparent",
            hover_color="#9E9E9E",
        )
        self.startmenubtn.pack(side="left")
        self.notepadbtn = StartMenuButton(
            self.startmenu,
            "Notepad",
            "#9E9E9E",
            "notepad.png",
            "transparent",
            (50, 50),
            "#000000",
            command=self.opennotepad,
        )
        self.notepadbtn.grid(row=0, column=0)
        self.calculatorbtn = StartMenuButton(
            self.startmenu,
            "Calculator",
            "#9E9E9E",
            "calc.png",
            "transparent",
            (50, 50),
            "#000000",
            command=self.opencalculator,
        )
        self.calculatorbtn.grid(row=0, column=1)

    def resizebackground(self, event):
        if event.widget == self:
            self.backgroundctk.configure(size=(event.width, event.height))

    def openstartmenu(self):
        if not self.startmenuopened:
            self.startmenu.place(x=10, y=60)
        elif self.startmenuopened:
            self.startmenu.place_forget()
        self.startmenuopened = not self.startmenuopened

    def opennotepad(self):
        self.notepadwindow = Notepad(self)

    def opencalculator(self):
        self.calculatorwindow = Calculator(self)


class TaskbarFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            **kwargs,
            bg_color="transparent",
            fg_color="#969696",
            corner_radius=20,
        )


class StartMenuFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            **kwargs,
            bg_color="transparent",
            fg_color="#969696",
            corner_radius=20,
        )


class Notepad(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#969696", **kwargs)
        self.geometry("640x360")
        self.attributes(topmost=True)
        self.title("Notepad")
        self.btnsframe = ctk.CTkFrame(self, fg_color="#969696")
        self.pack_propagate(True)
        self.btnsframe.pack(side="top", fill="x")
        self.savebtn = ctk.CTkButton(
            self.btnsframe, text="Save File", command=self.savefile
        )
        self.savebtn.pack(side="left", fill="x", expand=True)
        self.loadbtn = ctk.CTkButton(
            self.btnsframe, text="Load Button", command=self.loadfile
        )
        self.loadbtn.pack(side="left", fill="x", expand=True)
        self.textbox = ctk.CTkTextbox(self, fg_color="#969696", text_color="#000000")
        self.textbox.pack(side="top", fill="both", expand=True)

    def savefile(self):
        filename = ctk.filedialog.asksaveasfilename(
            title="Save file",
            defaultextension="*.txt",
            filetypes=[("Text Files", ".txt")],
        )
        with open(filename, "w") as f:
            f.write(self.textbox.get(1.0, "end"))
        CTkMessagebox(title="Saved", message=f"File saved to {filename}", icon="info")

    def loadfile(self):
        filename = ctk.filedialog.askopenfilename(
            title="Load File",
            defaultextension="*.txt",
            filetypes=[("Text Files", ".txt")],
        )
        with open(filename, "r") as f:
            self.textbox.delete("0.0", "end")
            self.textbox.insert("0.0", f.read())


class StartMenuButton(ctk.CTkButton):
    def __init__(
        self,
        master,
        text: str,
        hover_color: str,
        image_path: str,
        fg_color: str,
        size: tuple[int, int],
        text_color: str,
        **kwargs,
    ):
        img = Image.open(image_path)
        ctkimg = ctk.CTkImage(img, size=size)
        super().__init__(
            master,
            hover_color=hover_color,
            fg_color=fg_color,
            text=text,
            width=70,
            height=70,
            text_color=text_color,
            image=ctkimg,
            compound="top",
            **kwargs,
        )


class Calculator(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Calculator")
        self.configure(fg_color="#969696")
        self.attributes(topmost=True)
        self.entry1 = ctk.CTkEntry(self, text_color="#000000", fg_color="#969696")
        self.entry1.pack(side="top")
        self.entry2 = ctk.CTkEntry(self, text_color="#000000", fg_color="#9E9E9E")
        self.entry2.pack(side="top")
        self.label = ctk.CTkLabel(
            self, text="Answer will be here", text_color="#000000"
        )
        self.label.pack(side="top")
        self.addbtn = ctk.CTkButton(
            self,
            text="Add (+)",
            fg_color="#969696",
            text_color="#000000",
            command=self.add,
            hover_color="#9e9e9e",
        )
        self.addbtn.pack(side="top")
        self.subtractbtn = ctk.CTkButton(
            self,
            text="Subtract (-)",
            fg_color="#969696",
            text_color="#000000",
            command=self.subtract,
            hover_color="#9e9e9e",
        )
        self.subtractbtn.pack(side="top")
        self.multiplybtn = ctk.CTkButton(
            self,
            text="Mutliply (*)",
            fg_color="#969696",
            text_color="#000000",
            command=self.multiply,
            hover_color="#9e9e9e",
        )
        self.multiplybtn.pack(side="top")
        self.dividebtn = ctk.CTkButton(
            self,
            text="Divide (/)",
            fg_color="#969696",
            text_color="#000000",
            command=self.divide,
            hover_color="#9e9e9e",
        )
        self.dividebtn.pack(side="top")

    def add(self):
        self.label.configure(
            text=f"{float(self.entry1.get()) + float(self.entry2.get())}"
        )

    def subtract(self):
        self.label.configure(
            text=f"{float(self.entry1.get()) - float(self.entry2.get())}"
        )

    def multiply(self):
        self.label.configure(
            text=f"{float(self.entry1.get())* float(self.entry2.get())}"
        )

    def divide(self):
        self.label.configure(
            text=f"{float(self.entry1.get()) / float(self.entry2.get())}"
        )


class Windows12Button(ctk.CTkButton):
    def __init__(self, master, text: str, **kwargs):
        super().__init__(
            master,
            text=text,
            hover_color="#9e9e9e",
            fg_color="#969696",
            bg_color="transparent",
            text_color="#000000",
            **kwargs,
        )


class Windows12Label(ctk.CTkLabel):
    def __init__(self, master, text: str, **kwargs):
        super().__init__(
            master,
            text=text,
            fg_color="#969696",
            bg_color="transparent",
            text_color="#000000",
            **kwargs,
        )


class Windows12Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#969696", bg_color="transparent", **kwargs)


class Windows12Window(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#969696", **kwargs)


if __name__ == "__main__":
    root = App()
    root.mainloop()
