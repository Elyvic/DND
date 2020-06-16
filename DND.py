# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:11:49 2020

@author: elyvic
"""

import tkinter as tk
import random as rand

def RollD4():    
    val = int(d4Spinbox.get())
    total = 0
    
    for x in range(val):
        roll = rand.randint(1, 4)
        total += roll
        
    d4TextBox.config(state = tk.NORMAL)
    d4TextBox.delete(0, "end")
    d4TextBox.insert(0, str(total))
    d4TextBox.configure(state = tk.DISABLED)
    
    allRollText.config(state = tk.NORMAL)
    allRollText.see(tk.END)
    allRollText.insert(tk.END,  d4Spinbox.get() + " x D4 - " + str(total) + "\n")
    allRollText.config(state = tk.DISABLED)


def RollD6():
    val = int(d6Spinbox.get())
    total = 0
    
    for x in range(val):
        roll = rand.randint(1, 6)
        total += roll
    
    d6TextBox.config(state = tk.NORMAL)    
    d6TextBox.delete(0, "end")
    d6TextBox.insert(0, str(total))
    d6TextBox.config(state = tk.DISABLED)
    
    allRollText.config(state = tk.NORMAL)
    allRollText.see(tk.END)    
    allRollText.insert(tk.END,  d6Spinbox.get() + " x D6 - " + str(total) + "\n")
    allRollText.config(state = tk.DISABLED)

    
def RollD8():
    val = int(d8Spinbox.get())
    total = 0
    
    for x in range(val):
        roll = rand.randint(1, 8)
        total += roll
        
    d8TextBox.config(state = tk.NORMAL)
    d8TextBox.delete(0, "end")
    d8TextBox.insert(0, str(total))
    d8TextBox.config(state = tk.DISABLED)
    
    allRollText.config(state = tk.NORMAL)
    allRollText.see(tk.END)
    allRollText.insert(tk.END,  d8Spinbox.get() + " x D8 - " + str(total) + "\n")
    allRollText.config(state = tk.DISABLED)


def RollD10():
    val = int(d10Spinbox.get())
    total = 0
    
    for x in range(val):
        roll = rand.randint(1, 8)
        total += roll    
    
    d10TextBox.config(state = tk.NORMAL)
    d10TextBox.delete(0, "end")
    d10TextBox.insert(0, str(total))
    d10TextBox.config(state = tk.DISABLED)
    
    allRollText.config(state = tk.NORMAL)
    allRollText.see(tk.END)
    allRollText.insert(tk.END, d10Spinbox.get() + " x D10 - " + str(total) + "\n")
    allRollText.config(state = tk.DISABLED)

    
def RollD12():
    val = int(d12Spinbox.get())
    total = 0
    
    for x in range(val):
        roll = rand.randint(1, 12)
        total += roll
    
    d12TextBox.config(state = tk.NORMAL)
    d12TextBox.delete(0, "end")
    d12TextBox.insert(0, str(total)) 
    d12TextBox.config(state = tk.DISABLED)
    
    allRollText.config(state = tk.NORMAL)
    allRollText.see(tk.END)
    allRollText.insert(tk.END, d12Spinbox.get() + " x D12 - " + str(total) + "\n")
    allRollText.config(state = tk.DISABLED)


def RollD20():
    val = int(d20Spinbox.get())
    total = 0
    
    for x in range(val):
        roll = rand.randint(1, 20)
        total += roll
    
    d20TextBox.config(state = tk.NORMAL)
    d20TextBox.delete(0, "end")
    d20TextBox.insert(0, str(total)) 
    d20TextBox.config(state = tk.DISABLED)
    
    allRollText.config(state = tk.NORMAL)
    allRollText.insert(tk.END, d20Spinbox.get() + " x D20 - " + str(total) + "\n")
    allRollText.see(tk.END)
    allRollText.config(state = tk.DISABLED)

    
def RollD100():
    val = int(d100Spinbox.get())
    total = 0
    
    for x in range(val):
        roll = rand.randint(1, 100)
        total += roll
    
    d100TextBox.config(state = tk.NORMAL)
    d100TextBox.delete(0, "end")
    d100TextBox.insert(0, str(total))
    d100TextBox.config(state = tk.DISABLED)
    
    allRollText.config(state = tk.NORMAL)
    allRollText.insert(tk.END, d100Spinbox.get() + " x D100 - " + str(total) + "\n")
    allRollText.see(tk.END)
    allRollText.configure(state = tk.DISABLED)



def ClearText():
    allRollText.config(state = tk.NORMAL)
    allRollText.delete('1.0', tk.END)
    allRollText.config(state = tk.DISABLED)

root = tk.Tk();

rightFrame = tk.Frame(root, height = 300, width = 120, padx = 5, pady = 5)
leftFrame = tk.Frame(root, height = 300, width = 120, padx = 5, pady = 5)



root.title("Dice Roller")
root.resizable(True, True)


#all dice labels and buttons
d4Label = tk.Label(leftFrame, text = "D4")
d4TextBox = tk.Entry(leftFrame, width = 4)
d4Button = tk.Button(leftFrame, text = "Roll", command = RollD4)
d4Spinbox = tk.Spinbox(leftFrame, from_ = 1, to = 10, width = 4)

d6Label = tk.Label(leftFrame, text = "D6")
d6TextBox = tk.Entry(leftFrame, width = 4)
d6Button = tk.Button(leftFrame, text = "Roll", command = RollD6)
d6Spinbox = tk.Spinbox(leftFrame, from_ = 1, to = 10, width = 4)

d8Label = tk.Label(leftFrame, text = "D8")
d8TextBox = tk.Entry(leftFrame, width = 4)
d8Button = tk.Button(leftFrame, text = "Roll", command = RollD8)
d8Spinbox = tk.Spinbox(leftFrame, from_ = 1, to = 10, width = 4)

d10Label = tk.Label(leftFrame, text = "D10")
d10TextBox = tk.Entry(leftFrame, width = 4)
d10Button = tk.Button(leftFrame, text = "Roll", command = RollD10)
d10Spinbox = tk.Spinbox(leftFrame, from_ = 1, to = 10, width = 4)

d12Label = tk.Label(leftFrame, text = "D12")
d12TextBox = tk.Entry(leftFrame, width = 4)
d12Button = tk.Button(leftFrame, text = "Roll", command = RollD12)
d12Spinbox = tk.Spinbox(leftFrame, from_ = 1, to = 10, width = 4)

d20Label = tk.Label(leftFrame, text = "D20")
d20TextBox = tk.Entry(leftFrame, width = 4)
d20Button = tk.Button(leftFrame, text = "Roll", command = RollD20)
d20Spinbox = tk.Spinbox(leftFrame, from_ = 1, to = 10, width = 4)

d100Label = tk.Label(leftFrame, text = "D100")
d100TextBox = tk.Entry(leftFrame, width = 4)
d100Button = tk.Button(leftFrame, text = "Roll", command = RollD100)
d100Spinbox = tk.Spinbox(leftFrame, from_ = 1, to = 10, width = 4)

allRollText = tk.Text(rightFrame, width = 16, height = 15, padx = 3, pady = 2)
allRollClearButton = tk.Button(rightFrame, text = "Clear", command = ClearText, padx = 3 ,pady = 3)

#make all entry and text not editable
d4TextBox.config(state = tk.DISABLED)
d6TextBox.config(state = tk.DISABLED)
d8TextBox.config(state = tk.DISABLED)
d10TextBox.config(state = tk.DISABLED)
d12TextBox.config(state = tk.DISABLED)
d20TextBox.config(state = tk.DISABLED)
d100TextBox.config(state = tk.DISABLED)
allRollText.config(state = tk.DISABLED)


#labels and buttons placement
rightFrame.grid(column = 1, row = 0)
leftFrame.grid(column = 0, row = 0)

d4Label.grid(row = 0, sticky = tk.W)
d4Spinbox.grid(column = 1, row = 0)
d4TextBox.grid(column = 2, row = 0)
d4Button.grid(column = 3, row = 0, padx = 3, pady = 1)

d6Label.grid(row = 1, sticky = tk.W)
d6Spinbox.grid(column = 1, row = 1)
d6TextBox.grid(column = 2, row = 1)
d6Button.grid(column = 3, row = 1, pady = 1)

d8Label.grid(row = 2, sticky = tk.W)
d8Spinbox.grid(column = 1, row = 2)
d8TextBox.grid(column = 2, row = 2)
d8Button.grid(column = 3, row = 2, pady = 1)

d10Label.grid(row = 3, sticky = tk.W)
d10Spinbox.grid(column = 1, row = 3)
d10TextBox.grid(column = 2, row = 3)
d10Button.grid(column = 3, row = 3, pady = 1)

d12Label.grid(row = 4, sticky = tk.W)
d12Spinbox.grid(column = 1, row = 4)
d12TextBox.grid(column = 2, row = 4)
d12Button.grid(column = 3, row = 4, pady = 1)

d20Label.grid(row = 5, sticky = tk.W)
d20Spinbox.grid(column = 1, row = 5)
d20TextBox.grid(column = 2, row = 5)
d20Button.grid(column = 3, row = 5, pady = 1)

d100Label.grid(row = 6, sticky = tk.W)
d100Spinbox.grid(column = 1, row = 6)
d100TextBox.grid(column = 2, row = 6)
d100Button.grid(column = 3, row = 6, pady = 1)



allRollText.grid(column = 0, row = 0, columnspan = 10, rowspan = 10, sticky = tk.E)
allRollClearButton.grid(column = 9, row = 10, sticky = tk.E)  


root.mainloop()