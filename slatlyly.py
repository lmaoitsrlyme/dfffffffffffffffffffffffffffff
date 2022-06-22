from tkinter import *
window = Tk()


window.title('money wasted calculator')
window.geometry("500x400")
window.configure(bg = "#f4a9bb")
   
def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i, 2)

    
    result.destroy()
    
    message = Label(result_frame,text = "interest" + str(p)+" at rate of interest " + str(r) + "percent for " + str(t) + " years"+str(interest), bg = "grey", font = ("Calibri", 12), width = 55)
    message.place(x = 20,y = 40)
    message.pack()

app_label = Label(window, text = "money wasted calculator", fg = "black", bg = "#f4a9bb", font = ("Helvetica", 20),bd=5)
app_label.place(x = 20, y = 20)

principle_label=Label(window, text = "principle", fg = "black", bg = "#f4a9bb", font = ("Helvetica", 12),bd = 1)
principle_label.place(x = 20, y = 92)

principle=Entry(window, text = "", bd = 2, width = 22)
principle.place(x = 200, y = 92)

rate_label=Label(window, text = "rate of interest in %", fg = "black", bg = "#f4a9bb", font=("Calibri", 12))
rate_label.place(x = 20, y = 140)

rate=Entry(window, text="", bd=2, width=15)
rate.place(x=200, y=142)

time_label = Label(window, text = "time (years)", fg = "black", bg = "#f4a9bb", font = ("Calibri", 12))
time_label.place(x=20, y=185)

time=Entry(window, text = "", bd = 2, width = 15)
time.place(x = 200, y = 187)

calculate_button=Button(window,text = "calculate", fg = "black", bg = "#f4a9bb", bd = 4, command = calculate_interest)
calculate_button.place(x = 20,y = 250)

result_frame = LabelFrame(window,text = "result", bg = "#f4a9bb", font = ("Helvetica", 12))
result_frame.pack(padx = 20, pady = 20)
result_frame.place(x = 20, y = 300)

result = Label(result_frame, text = "result:", bg = "#f4a9bb", font = ("Helvetica", 12), width = 55)
result.place(x = 20,y = 20)
result.pack()

window.mainloop()
