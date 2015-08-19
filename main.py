from tkinter import *;
import os;

#create a class inheriting from Frame
class Explorer(Frame):
	
	#create constructor
	def __init__(self, parent):
		
		#starting directory always C:/Users/"user"
		self.currentDir = "C:/Users/" + os.getlogin();
		os.chdir(self.currentDir);
		
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
		
		#create listbox that hold all directories in the current directory
		dirList = get
		lb = Listbox(self)
		for i in self.listDir():
			lb.insert(END, i);

		lb.pack(side = RIGHT, fill=BOTH, expand=1, padx = 10, pady = 5);
		
	#returns current working directory	
	def getCurrentDir(self):
		self.currentDir = os.getcwd();
		return self.currentDir;
	
	#changes directory path
	def setCurrentDir(self, path):
		self.currentDir = os.chdir(path);
	
	#returns a list of all directories and files in the current directory
	def listDir(self):
		return os.listdir(self.currentDir);

def main():
	
	#create tk object
	root = Tk();
	#set dimesions of window
	#root.geometry("650x500+250+100");
	#pass tk object through our class
	app = Explorer(root);
	#enter mainloop
	root.mainloop();
	
if __name__ == '__main__':
	main();
