import os
import shutil
from tkinter import *
from tkinter import messagebox

#"config/config_customizations.ini"
if os.path.exists(os.path.join(os.getcwd(), 'config', 'config_customization.ini')):
    print("Loading...")
    if not os.path.exists("costumes"):
        os.makedirs("costumes")
    window = Tk()
    window.title("Novetus Costumes")
    window.configure(background="#008080")
    window.geometry("400x400")
    icon = PhotoImage(file = os.getcwd() + '/bin/preview/content/textures/face.png')
    window.iconphoto(False, icon)
    #label1
    lb1 = Label(window, text="Novetus Costumes", bg="#008080", fg="#ffffff", pady=5, font=("Helvetica", 15))
    lb1.grid(row=1, column=3, sticky=W)
    lb1.config(anchor=CENTER)
    lb1.pack()
    #listbox
    listbox = Listbox(window)
    #listbox.insert(1, "Test")
    #listbox.insert(2, "Test2")
    listbox.pack()
    #button

    def loadCostume():
        itm = listbox.get(listbox.curselection())
        #var.set(itm)
        print(itm)
        shutil.copyfile(os.getcwd() + "/costumes/" + itm,os.getcwd() + "/config/config_customization.ini")
        messagebox.showinfo(title="Load Costume", message="Loaded `" + itm + "`!")
        #print(os.listdir(os.getcwd() + "/costumes/"))
    def saveCostume():
        print("test")
        copfilename = e1.get()
        shutil.copyfile(os.getcwd() + "/config/config_customization.ini",os.getcwd() + "/costumes/" + copfilename + ".ini")
        messagebox.showinfo(title="Save Costume", message="Saved current costume as `" + copfilename + "`")
        refreshList()
    def refreshList():
        listbox.delete(0, END)
        fileamount = 0
        lister = os.listdir(os.getcwd() + "/costumes/")
        listamount = len(lister)
        #listbox.insert(1, lister[0])
        for x in range(listamount):
            #print(x) Uncomment for testing
            listbox.insert(fileamount, lister[fileamount])
            fileamount += 1
            #print("adding " + str(fileamount)) Testing
    lb2 = Label(window, text="Save Costume as:",bg="#008080", fg="#ffffff", pady=5, font=("Helvetica", 12))
    lb2.pack()
    e1 = Entry(window, bd =5)
    e1 .pack()
    bottom = Frame(window, pady=10, bg="#008080")
    bottom.pack(side=BOTTOM)
    load = Button(window, text='Load Costume', pady=5, bg="#bad5e8", command=loadCostume)
    load.pack(in_=bottom, side=LEFT)
    save = Button(window, text='Save Costume', pady=5, bg="#bad5e8", command=saveCostume)
    save.pack(in_=bottom, side=RIGHT)
    refresh = Button(window, text='Refresh List', pady=5, bg="#bad5e8", command=refreshList)
    refresh.pack(in_=bottom, side=RIGHT)
    refreshList()
    print("Script loaded.")
    window.mainloop()
else:
    messagebox.showinfo(title="Novetus Costumes", message="Novetus Costumes could not find your Novetus Installation. Please place this py file in the root of your Novetus installation.")
    print("Novetus Installation not found. Please place this py file in the root of your Novetus Directory.")
