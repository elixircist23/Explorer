from tkinter import *;
import os;

class Explorer(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background = "white");
        self.parent = parent;
        
        self.userID = os.getlogin();
        self.startDir = "C:/Users/" + self.userID;
        self.listDir = os.listdir(self.startDir);
        self.listDirLength = len(self.listDir);
        
        self.initUI();
        
    def initUI(self):
        self.parent.title("Explorer");
        self.pack(fill=BOTH, expand=1);

        #FRAMES
        self.topFrame = Frame(self)
        topFrame.pack(side=TOP)
        self.bottomFrame = Frame(self)
        bottomFrame.pack(side=BOTTOM)
        #DIRECTORY SEARCH BAR
        self.dirLabel = Label(topFrame, text="Current Directory", bg="white")
        dirLabel.pack(side=LEFT)

        self.dirEntry = Entry(topFrame)
        dirEntry.insert(0, self.startDir)
        dirEntry.pack()

        #LISTBOX
        self.scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.listBox = Listbox(self, height=20);
        for i in self.listDir:
            listBox.insert(END, i);

        listBox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listBox.yview)
        
        #listBox.bind("<<ListboxSelect>>", "method");
        listBox.pack(fill=BOTH, expand=1);
    
        
def main():
    root = Tk();
    root.geometry("250x150+300+300");
    app = Explorer(root)
    root.mainloop()

if __name__ == '__main__':
    main();
