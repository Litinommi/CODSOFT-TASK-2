from tkinter import *
root = Tk()
root.title('CALCULATOR')
root.geometry('500x500')
root.config(bg="black")

input_value=""

display_string=StringVar()

def clear_button_action():
    global input_value
    input_value=""
    display_string.set(input_value)
def click_button_action(item):
    global input_value
    input_value=input_value + item
    display_string.set(input_value)
def equal_button_action():
    global input_value
    result=str(eval(input_value))
    display_string.set(result)




input_frame =Frame(root, width=480, height=50, bd=0, highlightbackground="black", highlightcolor="black",highlightthickness=2)
input_frame.pack(side ='top')


input_field =Entry(input_frame, font=('arial', 18, 'bold'), textvariable=display_string, width=50, bg="#eee", bd=0,justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


buttons_frame=Frame(root,width=480,height=272.5,bg='grey')
buttons_frame.pack()

Button(buttons_frame, text="C", fg="black", width=32, height=3, bd=0, bg="silver", cursor="hand2",
                      command=lambda: clear_button_action()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action("/")).grid(row=0, column=3, padx=1, pady=1)

Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action("7")).grid(row=1, column=0, padx=1, pady=1)

Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
       command=lambda: click_button_action("8")).grid(row=1, column=1, padx=1, pady=1)

Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
       command=lambda: click_button_action("9")).grid(row=1, column=2, padx=1, pady=1)

Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action("*")).grid(row=1, column=3, padx=1, pady=1)

Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action("4")).grid(row=2, column=0, padx=1, pady=1)

Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action("4")).grid(row=2, column=1, padx=1, pady=1)

Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2", command=lambda: click_button_action("6")).grid(row=2, column=2, padx=1, pady=1)

Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action("-")).grid(row=2, column=3, padx=1, pady=1)

Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action("1")).grid(row=3, column=0, padx=1, pady=1)
Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action("2")).grid(row=3, column=1, padx=1, pady=1)
Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action("3")).grid(row=3, column=2, padx=1, pady=1)
Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action("+")).grid(row=3, column=3, padx=1, pady=1)

Button(buttons_frame, text="0", fg="black", width=21, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action("0")).grid(row=4, column=0,columnspan=2, padx=1, pady=1)
Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: click_button_action(".")).grid(row=4, column=2, padx=1, pady=1)
Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2",
                       command=lambda: equal_button_action()).grid(row=4, column=3, padx=1, pady=1)
root.update()
root.mainloop()