from tkinter import *;
import os;

#create a class inheriting from Frame
class Explorer(Frame):
    
    #create constructor
    def __init__(self, parent):
        
        #starting directory always C:/Users/"user"
        self.currentDir = "C:/Users/" + os.getlogin();
        os.chdir(self.currentDir);
        
        self.dirList = self.listDir();
        
        #call constructor from Frame, create parent to reference object
        Frame.__init__(self, parent, background = "white");
        self.parent = parent;
        
        #call initUI
        self.initUI();
    
    #initUI will be a function where all the widgets will be made and kept in
    def initUI(self):
        
        #set title of window # -->(current directory)
        self.parent.title("Explorer");
        
        #expand frame both directions
        self.pack(fill=BOTH, expand = 1);

        backButton = Button(self, text="Back", fg="blue", bg="white", command=self.back)
        backButton.pack()
        
        #create listbox that holds all directories in the current directory
        self.lb = Listbox(self)
        for i in self.dirList:
            self.lb.insert(END, i);
    
        self.lb.bind("<<ListboxSelect>>", self.onselect);
        self.lb.pack(side = BOTTOM, fill=BOTH, expand=1, padx = 10, pady = 5);
        
    #returns current working directory
    def getCurrentDir(self):
        self.currentDir = os.getcwd();
        return self.currentDir;
    
    #changes directory path
    def setCurrentDir(self, path):
        os.chdir(path);
        self.currentDir = os.getcwd()
        self.updateList()
    
    #returns a list of all directories and files in the current directory
    def listDir(self):
        return os.listdir(self.currentDir);
    
    #when listbox element is clicked
    def onselect(self, evt):
        
        #get index and value of clicked item
        w = evt.widget
        index = int(w.curselection()[0]);
        value = w.get(index)
        
        #set new path and pass it to 'setCurrentDir', that will move us to the dir, and change self.currentDir to path
        path = self.currentDir + '/' + value
        self.setCurrentDir(path);
        
        #destroy current lb to make way for the new one
        self.lb.destroy();
        
        #update first
        self.updateList()
        self.make()

    def make(self):
        self.lb = Listbox(self)
        for i in self.dirList:
            self.lb.insert(END, i);
        
        self.lb.bind("<<ListboxSelect>>", self.onselect);
        self.lb.pack(side = RIGHT, fill=BOTH, expand=1, padx = 10, pady = 5);
        
    #update the list
    def updateList(self):
        self.dirList = self.listDir();
        

    def back(self):
        split = self.getCurrentDir().rsplit("\\")
        dirrr = ""
        for i in range(len(split) - 1):
            dirrr += split[i] + "/"
        self.setCurrentDir(dirrr)
        self.updateList()
        self.make()

        print(dirrr)


def main():   
    #create tk object
    root = Tk();
    #set dimesions of window
    root.geometry("650x500+250+100");
    #pass tk object through our class
    app = Explorer(root);
    #enter mainloop
    root.mainloop();
    
if __name__ == '__main__':
    main();
