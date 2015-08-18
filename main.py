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

        topFrame = Frame(self)
        topFrame.pack(side=TOP)

        bottomFrame = Frame(self)
        bottomFrame.pack(side=BOTTOM)

        dirEntry = Entry(self)
        dirEntry.pack()
        

        
                
        listBox = Listbox(self, height=20);
        for i in self.listDir:
            listBox.insert(END, i);
        
        #listBox.bind("<<ListboxSelect>>", "method");
        
        listBox.pack(fill=BOTH, expand=1);
    
        
def main():
    root = Tk();
    root.geometry("250x150+300+300");
    app = Explorer(root)
    root.mainloop()

if __name__ == '__main__':
    main();
