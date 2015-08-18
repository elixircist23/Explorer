from tkinter import *

class Explorer(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, background = "white")
		self.parent = parent
		self.parent.title("Explorer")
		self.pack(fill=BOTH, expand=1)
		
def main():
	root = Tk()
	root.geometry("250x150+300+300")
	app = Explorer(root)
	root.mainloop()

if __name__ == '__main__':
	main();
	
	
