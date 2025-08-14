from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Tic Tac Toe')
root.geometry("400x480")

clicked = True 
count = 0 

buttons = []

def disable_all_buttons():
    for button in buttons:
        button.config(state=DISABLED)
def checkwin():
    global winner
    winner = False

    if b1["text"] == b2["text"] and b2["text"] == b3["text"] and b1["text"] != " ":
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {b1['text']} WINS!!")
        disable_all_buttons()
    elif b4["text"] == b5["text"] and b5["text"] == b6["text"] and b4["text"] != " ":
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {b4['text']} WINS!!")
        disable_all_buttons()
    elif b7["text"] == b8["text"] and b8["text"] == b9["text"] and b7["text"] != " ":
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {b7['text']} WINS!!")
        disable_all_buttons()

    elif b1["text"] == b4["text"] and b4["text"] == b7["text"] and b1["text"] != " ":
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {b1['text']} WINS!!")
        disable_all_buttons()
    elif b2["text"] == b5["text"] and b5["text"] == b8["text"] and b2["text"] != " ":
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {b2['text']} WINS!!")
        disable_all_buttons()
    elif b3["text"] == b6["text"] and b6["text"] == b9["text"] and b3["text"] != " ":
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {b3['text']} WINS!!")
        disable_all_buttons()

    elif b1["text"] == b5["text"] and b5["text"] == b9["text"] and b1["text"] != " ":
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {b1['text']} WINS!!")
        disable_all_buttons()
    elif b3["text"] == b5["text"] and b5["text"] == b7["text"] and b3["text"] != " ":
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {b3['text']} WINS!!")
        disable_all_buttons()

    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's a TIE!\nNo one wins.")
        disable_all_buttons()

def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected.\nPick another box...")

    checkwin()

def reset_game():
    global clicked, count, buttons

    clicked = True
    count = 0

    for button in buttons:
        button.config(text=" ", bg="SystemButtonFace", state=NORMAL)

b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))


buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

reset_button = Button(root, text="Reset Game", font=("Helvetica", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=20)


root.mainloop()
