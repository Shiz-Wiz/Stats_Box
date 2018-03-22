from tkinter import *

class application(Frame):
    """ A Gui application with three buttons"""
    def __init__(self, master = None):
        """ Inititalization the fram"""
        Frame.__init__(self,master)
        self.master = master
        #self.grid()
        self.create_widgets()



    def create_widgets(self):
        self.master.title("Data Entry")
        self.pack(fill=BOTH, expand=1)
        buttons1 = Button(self,text = "Meow", command= self.program_button)
        buttons1.place(x=450,y=470)
        #self.buttons1.place(x=5, y=10)

        menu = Menu(self.master)
        self.master.config(menu=menu)



        self.xc = StringVar()
        eBox = Entry(self, textvariable=self.xc)
        #eBox.pack()
        eBox.grid()

        self.yc = StringVar()
        eBox = Entry(self, textvariable=self.yc)
        # eBox.pack()
        eBox.grid()

        file = Menu(menu)
        file.add_command(label='Save', command=self.text_capture)
        file.add_command(label='Exit', command=self.program_exit)
        menu.add_cascade(label='File', menu=file)



    def program_button(self):
        import scratch
        scratch
        #exit()

    def program_exit(self):
        exit()

    def text_capture(self):
        x = self.xc.get()
        y = self.yc.get()
        with open("example.txt", "w") as f:
            f.write(x + ',' + y )
        #print(self.test.get())

root = Tk()

root.geometry("500x500")

app = application(root)


root.mainloop()