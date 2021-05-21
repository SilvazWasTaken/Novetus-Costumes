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
    window.configure(background="#364354")
    window.geometry("500x500")
    #icon do not work for now: window.iconbitmap(os.getcwd() + '/NovetusIcon.ico')
    #label1
    lb1 = Label(window, text="Novetus Costumes", bg="#364354", fg="#ffffff", font="SimSun")
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
    lb2 = Label(window, text="Save Costume as:",bg="#364354", fg="#ffffff", font="SimSun")
    lb2.pack()
    e1 = Entry(window, bd =5)
    e1 .pack()
    bottom = Frame(window)
    bottom.pack(side=BOTTOM)
    load = Button(window, text='Load Costume', command=loadCostume)
    load.pack(in_=bottom, side=LEFT)
    save = Button(window, text='Save Costume', command=saveCostume)
    save.pack(in_=bottom, side=RIGHT)
    refresh = Button(window, text='Refresh List', command=refreshList)
    refresh.pack(in_=bottom, side=RIGHT)
    refreshList()
    print("Script loaded.")
    window.mainloop()
else:
    messagebox.showinfo(title="Novetus Costumes", message="Novetus Costumes could not find your Novetus Installation. Please place this py file in the root of your Novetus installation.")
    print("Novetus Installation not found. Please place this py file in the root of your Novetus Directory.")
