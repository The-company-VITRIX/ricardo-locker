import tkinter as tk
import getpass
from PIL import Image, ImageTk
from image import *
import pyautogui



class LockScreen:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.title("Екран заблоковано")
        self.root.attributes("-fullscreen", True)
        self.password = "rik"
        self.create_widgets()
  
    def create_widgets(self):
        self.label1 = tk.Label(self.root, text="Введіть пароль щоб розблокувати:")
        self.label1.pack(pady=20)
        self.entry1 = tk.Entry(self.root, show="*")
        self.entry1.pack(pady=10)
        self.button1 = tk.Button(self.root, text="Розблокувати", command=self.check_password)       
        self.button1.pack(pady=10)
        image()
        
        self.root.mainloop()
        while True:
            if pyautogui.press('alt') and pyautogui.press('f4'):
                pyautogui.hotkey('z', 'v') 

            elif pyautogui.press('alt') and pyautogui.press('shift') and pyautogui.press('esc'):
                pyautogui.hotkey('j', 'k', 'l')

            elif pyautogui.press('win') and pyautogui.press('r'):
                pyautogui.hotkey('o', 'p') 

    def check_password(self):
        if self.entry1.get() == self.password:
            self.root.destroy()


        else:
            self.label1.config(text="Пароль неправельний! Повторіть спробу.")

    def image():
        

        #img = ImageTk.PhotoImage(Image.open("ricardo.png"))

        b = Label(image = img)

        b.pack()
            
if __name__ == "__main__":
    LockScreen()
    
