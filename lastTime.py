import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=650, height=400, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Countdown')
label1.config(font=('helvetica', 14))
canvas1.create_window(325, 25, window=label1)

label2 = tk.Label(root, text='Date of birth:')
label2.config(font=('helvetica', 10))
canvas1.create_window(100, 100, window=label2)

label3 = tk.Label(root, text='Month of birth:')
label3.config(font=('helvetica', 10))
canvas1.create_window(250, 100, window=label3)

label4 = tk.Label(root, text='Year of birth:')
label4.config(font=('helvetica', 10))
canvas1.create_window(400, 100, window=label4)

label5 = tk.Label(root, text='Age:')
label5.config(font=('helvetica', 10))
canvas1.create_window(550, 100, window=label5)


entry1 = tk.Entry(root)
canvas1.create_window(100, 140, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(250, 140, window=entry2)

entry3 = tk.Entry(root)
canvas1.create_window(400, 140, window=entry3)

entry4 = tk.Entry(root)
canvas1.create_window(550, 140, window=entry4)


def count_age():

    db = entry1.get()
    mb = entry2.get()
    yb = entry3.get()
    age = entry4.get()
    num = 0
    dth = 0

    for i in yb:
        num += int(i)
    if int(yb[3]) == 0:
        z = 1
    else:
        z = int(yb[3])
    result = str((int(yb) / int(num)) / (int(db) * int(z) * int(mb)))

    if result[1] == ".":
        y = result[2] + result[3]
    elif result[2] == ".":
        y = result[3] + result[4]
    else:
        y = result[1] + result[2]

    if int(y) <= int(age):
        dth = int(y) + int(age)
    else:
        dth = int(y)
    dth = str(dth)

    label_end = tk.Label(root, text='You will die at the age of ' + dth, font=('helvetica', 10))
    canvas1.create_window(325, 260, window=label_end)


button1 = tk.Button(text='Predict', command=count_age, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(325, 200, window=button1)

root.mainloop()