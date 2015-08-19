from tkinter import *;
import os;


class Explorer(Frame):
    
    def __init__(self, parent):
        
        Frame.__init__(self, parent, background = "white")
        self.parent = parent
        
        self.userID = os.getlogin()
        self.startDir = "C:/Users/" + self.userID
        self.listDir = os.listdir(self.startDir)
        self.listDirLength = len(self.listDir)
        
        self.initUI()

    def updateDir(self, event):
        self.item = self.listBox.curselection()
        print(self.item)
        self.listDir = os.listdir(self.startDir + "/" + self.listBox.get(self.item[0]))
        print(self.listDir)


    def initUI(self):
        self.parent.title("Explorer")
        self.pack(fill=BOTH, expand=1)

        #FRAMES
        self.topFrame = Frame(self)
        self.topFrame.pack(side=TOP)
        self.bottomFrame = Frame(self)
        self.bottomFrame.pack(side=BOTTOM)
        #DIRECTORY SEARCH BAR
        self.dirLabel = Label(self.topFrame, text="Current Directory", bg="white")
        self.dirLabel.pack(side=LEFT)

        self.dirEntry = Entry(self.topFrame)
        self.dirEntry.insert(0, self.startDir)
        self.dirEntry.pack()

        #LISTBOX
        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        self.listBox = Listbox(self, height=20, selectmode=SINGLE)
        for i in self.listDir:
            self.listBox.insert(END, i)

        self.listBox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listBox.yview)
        
        self.listBox.bind("<<ListboxSelect>>", self.updateDir)
        

        self.listBox.pack(fill=BOTH, expand=1)
    
        
def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Explorer(root)
    root.mainloop()

if __name__ == '__main__':
    main()
