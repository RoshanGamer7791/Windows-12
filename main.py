import customtkinter as ctk
from PIL import Image
import os

os.path.dirname(os.path.abspath(__file__))


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Windows 12")
        self.attributes(fullscreen=True)
        self.backgroundimg = Image.open("background.png")
        self.backgroundctk = ctk.CTkImage(self.backgroundimg, size=(1200, 800))
        self.background = ctk.CTkLabel(self, image=self.backgroundctk, text="")
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.resizebackground)
        Taskbar = TaskbarFrame(self, height=50)
        Taskbar.place(relx=0, rely=1, anchor="sw", relwidth=1)

    def resizebackground(self, event):
        if event.widget == self:
            self.backgroundctk.configure(size=(event.width, event.height))


class TaskbarFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            **kwargs,
            bg_color="transparent",
            fg_color="#8F8F8F",
            corner_radius=10
        )


if __name__ == "__main__":
    root = App()
    root.mainloop()
