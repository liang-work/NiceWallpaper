#import customtkinter as ctk
def open(ctk,lang):
    root = ctk.CTkToplevel()
    root.title(lang["AboutWindow"]["title"])
    root.geometry("300x250")
    root.resizable(0,0)
    about = ctk.CTkLabel(root,text="NiceWallPaper" + "\n" + lang["AboutWindow"]["aboutInfo_1"] + "\n" + lang["AboutWindow"]["aboutInfo_2"])
    about.place(x=70,y=80)
    close = ctk.CTkButton(root,text=lang["AboutWindow"]["close"],command=root.destroy)
    close.place(x=80,y=150)
    root.mainloop()