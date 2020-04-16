#imports every exposed object in tkinter into your current name space
from tkinter import *
#this provides access to the tk themed widget set 
from tkinter import ttk

import json

#This creates an unordered collection of data values and is used to store data in the program after a user inputs data
spotandname=dict()

#used to create a route window; labeling main as a route window 
main=Tk()
#this sets the size of the "main" window
main.geometry('500x200')

def load():
    with open("data.json","r")as fp:
        spotandname=json.load(fp)
        print(spotandname)
        
def save():
    with open("data.json","w") as fp:
        json.dump(spotandname,fp)

#This sets a label for the title of the "main" page; sets the string variable that will be displayed and the color of the text
title=Label(main,text='Parking Garage',fg='teal')
#this places the label in a specific spot on the window using a grid set up
title.grid(row=0,column=1)

#creates a function that allows the code to pass a variable number of arguments to a function; allows us to create a function with multiple variables that can be used later
def addinfopage(*args):
#when this function is executed a new window will open using the Toplevel widget
    infopage=Toplevel()
#this sets the size of the "infopage" window
    infopage.geometry('500x200')
 
#The label below titles the input the code is asking for in the specific "infopage" window; sets the string variable that will be displayed and the color of the text
    addtitle=Label(infopage,text='Add Information',fg='hotpink')
#The grid below places the label in a set column and row; this allows the label to be displayed on the window that it is set to
    addtitle.grid(row=0,column=1)
#The label below titles the input the code is asking for in the specific "infopage" window; sets the string variable that will be displayed
    lname=ttk.Label(infopage,text='Last Name: ')
#The grid below places the label in a set column and row; this allows the label to be displayed on the window that it is set to
    lname.grid(row=2,column=0)
#this is a widget within the window that allows the user to input information that can be used later in the program
    entry1=ttk.Entry(infopage,width=15)
#this grid specifies the placement of the widget witin the widow; this entry will be next to the "Last Name:" label 
    entry1.grid(row=2,column=1)
#The label below titles the input the code is asking for in the specific "infopage" window; sets the string variable that will be displayed
    lnum=Label(infopage,text='License Number: ')
#The grid below places the label in a set column and row; this allows the label to be displayed on the window that it is set to
    lnum.grid(row=3,column=0)
#this is a widget within the window that allows the user to input information that can be used later in the program
    entry2=ttk.Entry(infopage,width=15)
#this grid specifies the placement of the widget witin the widow; this entry will be next to the "License Number:" label 
    entry2.grid(row=3,column=1)

#provides helper functions for directly creating and accessing variables within the dictionary  
    x=StringVar()
    lname=StringVar()
    lnum=StringVar()
 
#imports "random module package" from python that can be used later in the funtions
    import random
#creates a function titled "spotgen" that allows the code to pass a variable number of arguments to a function; allows us to create a function with multiple variables that can be used later
    def spotgen(*args):
#this sets the variable "norepeat" equal to one
        norepeat=1
#this statement repeatedly executes a target statement as long as a given condition is true, or as long as the "norepeat" variable is equal to one.
        while norepeat==1:
#this sets the variable "ID" equal to a string of a randomly selected integer between 0 and 500.
            ID=str(random.randint(0,500))
#The code in the first block of statements is executed if the Boolean expression condition evaluates to true; otherwise, the code in second block of statements is executed. This makes sure that the ID number is not repeated.
            if ID in spotandname: 
                norepeat=1
            else:
                norepeat=0
#this makes sure that there is no duplicates in the ID numbers and creates a set of this data 
        x.set(ID)
#The label below titles the input the code is asking for in the specific "infopage" window; sets the string variable that will be displayed
        numberlabel=Label(infopage,text='Parking Spot Number: ')
#The grid below places the label in a set column and row; this allows the label to be displayed on the window that it is set to
        numberlabel.grid(row=5,column=0)
#The label below titles the input the code is asking for in the specific "infopage" window; sets the string variable that will be displayed. The displayed value will be determined by the function above that defines "x" as a random nonrepeatable integer.
        gennum=Label(infopage,textvariable=x)
#The grid below places the label in a set column and row; this allows the label to be displayed on the window that it is set to
        gennum.grid(row=5,column=1)
#this retrieves data from the dictionary that was inputed by the user
        lname=entry1.get()
#this retrieves data from the dictionary that was inputed by the user
        lnum=entry2.get()
#this allows the ID that was previously generated to be stored in the dictionary and the values of "lname and lnum" to be included with the certain ID number
        spotandname[ID]=(lname,lnum)
        
        valletticket=Label(infopage,text='If using vallet, please press button below to get ticket.')
        valletticket.grid(row=6,column=1)
        vtbutton=ttk.Button(infopage,text='Ticket')
        vtbutton.grid(row=7,column=1)
        
#this creates a button the user can press to generate the ID, or parking spot number, using the "spotgen" command    
    spotnum=ttk.Button(infopage,text='Generate Parking Spot Number',command=spotgen)
#this places the button in the correcct place on the grid within the widget 
    spotnum.grid(row=4,column=1)
 
#this creates a button the user can press that runs through the "addinfopage" command; this is located on the main window     
infobutton=ttk.Button(main,text='Enter Information',command=addinfopage)
#this places the button in the correcct place on the grid within the widget 
infobutton.grid(row=1,column=1)

#creates a function that allows the code to pass a variable number of arguments to a function; allows us to create a function with multiple variables that can be used later
def addpaypage(*args):
#when this function is executed a new window will open using the Toplevel widget
    paypage=Toplevel()
#this sets the size of the "paypage" window
    paypage.geometry('500x200')

#The label below titles the input the code is asking for in the specific "paypage" window; sets the string variable that will be displayed and the color
    paylabel=Label(paypage,text='Pay to Leave',fg='hotpink')
#The grid below places the label in a set column and row; this allows the label to be displayed on the window that it is set to
    paylabel.grid(row=0,column=1)
#The label below titles the input the code is asking for in the specific "paypage" window; sets the string variable that will be displayed and the color
    lnamelabel=ttk.Label(paypage,text='Enter Parking Spot Number: ')
#The grid below places the label in a set column and row; this allows the label to be displayed on the window that it is set to
    lnamelabel.grid(row=2,column=0)
#this is a widget within the window that allows the user to input information that can be used later in the program
    entry6=ttk.Entry(paypage,width=15)
#this is a widget within the window that allows the user to input information that can be used later in Enter Last Name:" label 
    entry6.grid(row=2,column=1)
    
    info=StringVar()
    
    def pay(*args):
        key=entry6.get()
#values=(lname,lnum,spotnum)
        value=spotandname[key]
        info.set(value)
        print (value)
        label1=Label(paypage,textvariable=info)
        label1.grid(row=4,column=1)
        labelPay=Label(paypage,text='Insert Payment')
        labelPay.grid(row=6,column=1)
    
    paybutton=ttk.Button(paypage,text='Pay',command=pay)
    paybutton.grid(row=4,column=1)

#this creates a button the user can press that runs through the "addpaypage" command; this is located on the main window
paypagebutton=ttk.Button(main,text='Pay to Leave',command=addpaypage)
#this places the button in the correcct place on the grid within the widget
paypagebutton.grid(row=2,column=1)

def addvallet(*args):
    #when this function is executed a new window will open using the Toplevel widget
    valletpage=Toplevel()
#this sets the size of the "valletpage" window
    valletpage.geometry('500x200')
    
    valletlabel=Label(valletpage,text='Vallet Pick Up',fg='hotpink')
    valletlabel.grid(row=0,column=1)
    spotnumlabel=ttk.Label(valletpage,text='Enter Parking Spot Number: ')
    spotnumlabel.grid(row=2,column=0)
    entry7=ttk.Entry(valletpage,width=15)
    entry7.grid(row=2,column=1)    
    
    info=StringVar()
    
    def vallet(*args):  
        key=entry7.get()
        value=spotandname[key]
        info.set(value)
        print (value)
        label1=Label(valletpage,textvariable=info)
        label1.grid(row=4,column=1)
        
        num=int(entry7.get())
        for i in range(0,500):
            if num<=100 and num>=0:
                label2=Label(valletpage,text='Car is located on level 1.')
                label2.grid(row=5,column=1)
            else:
                if num<=200 and num>=101:
                    label3=Label(valletpage,text='Car is located on level 2.')
                    label3.grid(row=5,column=1)
                else:
                    if num<=300 and num>=201:
                        label4=Label(valletpage,text='Car is located on level 3.')
                        label4.grid(row=5,column=1)
                    else:
                        if num<=400 and num>=301:
                            label5=Label(valletpage,text='Car is located level 4.')
                            label5.grid(row=5,column=1)
                        else:
                            if num<=500 and num>=401:
                                label6=Label(valletpage,text='Car is located on level 5.')
                                label6.grid(row=5,column=1)
                            else:
                                 label7=Label(valletpage,text='Invalid Number')
                                 label7.grid(row=5,column=1)
            
            
    valletbutton=ttk.Button(valletpage,text='Generate Car Information',command=vallet)
    valletbutton.grid(row=3,column=1)
        
valletpagebutton=ttk.Button(main,text='Vallet Pick Up',command=addvallet)
valletpagebutton.grid(row=3,column=1)
    
#this is an infinite loop used to run the application; waits for an event to ocuur and porcesses the event as long as the window is not close. This will keep the program running as long as the main window is still open.
main.mainloop()
