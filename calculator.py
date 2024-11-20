import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def delete_last():
    global calculation
    if calculation:  # Check if there's anything to delete
        calculation = calculation[:-1]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

def add_decimal():
    global calculation
    if "." not in calculation: #Avoid multiple decimals
        calculation += "."
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)


root = tk.Tk()
root.geometry("300x310")  # Increased size to accommodate new buttons
root.config(bg="black")
root.resizable(False, False)
root.title("Basic Calculator by Formasys")

text_result = tk.Text(root, height=2, width=25, font=('Arial', 14))
text_result.grid()

#text_result=tk.Text(root,height=3,width=22,font=('Arial',16))
text_result.grid(row=0, columnspan=8, padx=10, pady=10)

btn_1=tk.Button(root,text="1",command=lambda:add_to_calculation(1),width=5, bg="#A29F9E",font=('Arial',14))
btn_1.grid(row=3,column=1, padx=3, pady=3)

btn_2=tk.Button(root,text="2",command=lambda:add_to_calculation(2),width=5, bg="#A29F9E",font=('Arial',14))
btn_2.grid(row=3,column=2, padx=3, pady=3)

btn_3=tk.Button(root,text="3",command=lambda:add_to_calculation(3),width=5, bg="#A29F9E",font=('Arial',14))
btn_3.grid(row=3,column=3, padx=3, pady=3)

btn_4=tk.Button(root,text="4",command=lambda:add_to_calculation(4),width=5, bg="#A29F9E",font=('Arial',14))
btn_4.grid(row=4,column=1, padx=3, pady=3)

btn_5=tk.Button(root,text="5",command=lambda:add_to_calculation(5),width=5, bg="#A29F9E",font=('Arial',14))
btn_5.grid(row=4,column=2, padx=3, pady=3)

btn_6=tk.Button(root,text="6",command=lambda:add_to_calculation(6),width=5, bg="#A29F9E",font=('Arial',14))
btn_6.grid(row=4,column=3, padx=3, pady=3)

btn_7=tk.Button(root,text="7",command=lambda:add_to_calculation(7),width=5, bg="#A29F9E",font=('Arial',14))
btn_7.grid(row=5,column=1, padx=3, pady=3)

btn_8=tk.Button(root,text="8",command=lambda:add_to_calculation(8),width=5, bg="#A29F9E",font=('Arial',14))
btn_8.grid(row=5,column=2, padx=3, pady=3)

btn_9=tk.Button(root,text="9",command=lambda:add_to_calculation(9),width=5, bg="#A29F9E",font=('Arial',14))
btn_9.grid(row=5,column=3, padx=3, pady=3)

btn_0=tk.Button(root,text="0",command=lambda:add_to_calculation(0),width=5, bg="#A29F9E", font=('Arial',14))
btn_0.grid(row=6,column=2, padx=3, pady=3)

btn_plus=tk.Button(root,text="+",command=lambda:add_to_calculation("+"),width=5, bg="#A29F9E", font=('Arial',14))
btn_plus.grid(row=3,column=4, padx=3, pady=3)

btn_sous=tk.Button(root,text="-",command=lambda:add_to_calculation("-"),width=5, bg="#A29F9E",font=('Arial',14))
btn_sous.grid(row=4,column=4, padx=3, pady=3)

btn_div=tk.Button(root,text="/",command=lambda:add_to_calculation("/"),width=5, bg="#A29F9E", font=('Arial',14))
btn_div.grid(row=5,column=4, padx=3, pady=3)

btn_mul=tk.Button(root,text="x",command=lambda:add_to_calculation("*"),width=5, bg="#A29F9E", font=('Arial',14))
btn_mul.grid(row=6,column=4, padx=3, pady=3)

btn_open=tk.Button(root,text="(",command=lambda:add_to_calculation("("),width=5, bg="#A29F9E", font=('Arial',14))
btn_open.grid(row=6,column=1, padx=3, pady=3)

btn_clos=tk.Button(root,text=")",command=lambda:add_to_calculation(")"),width=5, bg="#A29F9E", font=('Arial',14))
btn_clos.grid(row=6,column=3, padx=3, pady=3)

btn_equal=tk.Button(root,text="=",command=evaluate_calculation,width=5, bg="#A29F9E", font=('Arial',14))
btn_equal.grid(row=7,column=4, padx=3, pady=3)

btn_clear=tk.Button(root,text="C",command=clear_field,width=5, bg="#A29F9E", font=('Arial',14))
btn_clear.grid(row=7,column=1, padx=3, pady=3)
# ... (Existing button code remains the same, juste a little change in pady and touch color) ...

# New Buttons
btn_delete = tk.Button(root, text="DEL", command=delete_last, width=5, bg="#A29F9E",font=('Arial', 14))
btn_delete.grid(row=7, column=2)  

btn_decimal = tk.Button(root, text=".", command=add_decimal, width=5,bg="#A29F9E", font=('Arial', 14))
btn_decimal.grid(row=7, column=3) 


root.mainloop()
