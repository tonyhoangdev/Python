    #!/usr/bin/python3
#
"""
    @author: MinhHT3
    @brief : GUI tkinter
"""
import tkinter

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title('A simple GUI')

        self.label = tkinter.Label(master, text='This is my first GUI!')
        self.label.pack()

        self.greet_button = tkinter.Button(master, text='Greet', command=self.greet)
        self.greet_button.pack()

        self.close_button = tkinter.Button(master, text='Close', command=master.quit)
        self.close_button.pack()

    def greet(self):
        print('Greetings!')

root = tkinter.Tk()
my_gui = MyGUI(root)
root.mainloop()
