from tkinter import *;
import os;

#create a class inheriting from Frame
class Explorer(Frame):
	
	#create constructor
	def __init__(self, parent):
		
		#starting directory always C:/Users/"user"
		self.currentDir = "C:\\Users\\" + os.getlogin();
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
		
		#create back button
		b = Button(self, text = "<--", command = self.goBack);
		b.pack(side="left", padx = 5, pady = 5);
		
		#create listbox that holds all directories in the current directory
		self.lb = Listbox(self)
		for i in self.listDir():
			self.lb.insert(END, i);
	
		self.lb.bind("<<ListboxSelect>>", self.onselect);
		self.lb.pack(side = RIGHT, fill=BOTH, expand=1, padx = 20, pady = 20);
				
	#returns current working directory	
	def getCurrentDir(self):
		self.currentDir = os.getcwd();
		return self.currentDir;
	
	#changes directory path
	def setCurrentDir(self, path):
		os.chdir(path);
		self.currentDir = os.getcwd()
		self.updateList();		
	
	#returns a list of all directories and files in the current directory
	def listDir(self):
		
		#https://docs.python.org/2/library/errno.html#module-errno <--- FOR FILES
		self.dirList = os.listdir(self.getCurrentDir());
		updateListDir = [];
		for i in range(len(self.dirList)):
			try:
				os.listdir(self.dirList[i])
				updateListDir.append(self.dirList[i]);
			except (WindowsError):
				pass
			
			os.chdir(self.currentDir);
		
		return updateListDir;
	
	#when listbox element is clicked
	def onselect(self, evt):
		
		try:
			#get index and value of clicked item
			w = evt.widget
			index = int(w.curselection()[0]);
			value = w.get(index)
			
			#set new path and pass it to 'setCurrentDir', that will move us to the dir, and change self.currentDir to path
			path = self.currentDir + '\\' + value
			self.setCurrentDir(path);
			
			self.updateList();
		
		except IndexError:
			pass;
		
	#update the list
	def updateList(self):
		self.listDir();
		self.currentDir = self.currentDir + '\\'
		
		#destroy current lb to make way for the new one
		self.lb.destroy();
		
		#create new lb, but update first
		self.lb = Listbox(self)
		for i in self.listDir():
			self.lb.insert(END, i);
		
		self.lb.bind("<<ListboxSelect>>", self.onselect);
		self.lb.pack(side = RIGHT, fill=BOTH, expand=1, padx = 10, pady = 5);
	
	#function that goes to the directory above the current
	def goBack(self):
		#that fuckin 1-liner
		self.setCurrentDir(self.getCurrentDir()[:self.getCurrentDir().rindex("\\")+1]);

		
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
