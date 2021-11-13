from tkinter import*
root=Tk()
root.geometry("600x400")
name=["rat","cat","fat","sat"]
 car={
      "name":"tesla","color":"black"}
 try:
     print(name[5])
     
except IndexError:
    messagebox.showinfo("Error","index does not exist")
    
root.mainloop()