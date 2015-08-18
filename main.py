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
		
	def initUI(self):
		self.parent.title("Explorer");
		self.pack(fill=BOTH, expand=1);
		
		listBox = Listbox(self);
		for i in listDir:
			listBox.insert(END, i);
		
		#listBox.bind("<<ListboxSelect>>", "method");
		
	
		
def main():
	root = Tk();
	root.geometry("250x150+300+300");
	app = Explorer(root)
	root.mainloop()

if __name__ == '__main__':
	main();

