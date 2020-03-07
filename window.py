from tkinter import *

root = Tk()

class temp_frame():

    def __init__(self, master):
        self.master = master
        self.secondary_win = None

        self.master.geometry('600x300')
        self.master.title("myWeather - Home")

        self.instructions = Label(self.master, text = "Enter your zip code to get \nyour local weather:", font= ("Arial Bold", 10))
        self.instructions.grid()

        self.btn_next = Button(self.master, text="GO", command=self.Forward)
        self.btn_next.grid()

        self.Entry = Entry(self.master, width = 20)
        self.Entry.grid()

    def Forward(self):
        # Open secondary Window

        zipCode = self.Entry.get()
        print(zipCode)

        if not self.secondary_win:
            self.secondary_win = Toplevel()
            back_btn = Button(self.secondary_win, text="Back", command=self.Backward)
            back_btn.pack()
            self.master.withdraw()
        else:
            self.secondary_win.deiconify()
            self.master.withdraw()



    def Backward(self):
        self.secondary_win.withdraw()
        self.master.deiconify()


temp = temp_frame(root)

root.mainloop()