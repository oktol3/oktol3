from tkinter import *
from tkinter import ttk
from er import ro


def click_button():
    globals()
    root['background'] = '#606060'
    j = 0; l1 = 0; l2 = 0; l3 = 0; l4 = 0; g1 = []; g2 = []; g3 = []; b = [0]; l = [0]; f1 = -1; f2 = -1; cl5 = 0; clh = 0
    file = open('com.txt', 'r', encoding='UTF-8')
    com = file.read()
    cl = com.replace(' ', '')
    cl = cl.replace('\t', '')
    cl2 = cl.split('\n')
    com = com.split('\n')
    x = 0
    y = 0
    try:
        while j < len(com) and clh == 0:
            cl3 = j
            ch = 0
            cl1 = cl2[j]
            c = com[j].split()
            if len(c) == 0:
                c = ['', '']
            if c[0] == 'IFBLOCK':
                ch = 1
                if c[1] == 'RIGHT' and x != 500:
                    h = [i for i, ltr in enumerate(cl.split('\n')) if ltr == 'ENDIF']
                    for i in range(len(h)):
                        if h[i] < j:
                            h[i] = 100000
                    j = min(h)
                if c[1] == 'LEFT' and x != 0:
                    h = [i for i, ltr in enumerate(cl.split('\n')) if ltr == 'ENDIF']
                    for i in range(len(h)):
                        if h[i] < j:
                            h[i] = 100000
                    j = min(h)
                if c[1] == 'UP' and y != 0:
                    h = [i for i, ltr in enumerate(cl.split('\n')) if ltr == 'ENDIF']
                    for i in range(len(h)):
                        if h[i] < j:
                            h[i] = 100000
                    j = min(h)
                if c[1] == 'DOWN' and y != 500:
                    h = [i for i, ltr in enumerate(cl.split('\n')) if ltr == 'ENDIF']
                    for i in range(len(h)):
                        if h[i] < j:
                            h[i] = 100000
                    j = min(h)

            if c[0] == 'RIGHT':
                ch = 1
                try:
                    u = int(c[1])
                except ValueError:
                    u = int(l[b.index(c[1])])
                for i in range(u):
                    canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image1)
                    if x != 500:
                        x += 25
                    else:
                        canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image2)
                        x = 10000
                        j = len(com)
                    canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image)

            if c[0] == 'LEFT':
                ch = 1
                try:
                    u = int(c[1])
                except ValueError:
                    u = int(l[b.index(c[1])])
                for i in range(u):
                    canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image1)
                    if x != 0:
                        x -= 25
                    else:
                        canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image2)
                        x = 10000
                        j = len(com)
                    canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image)

            if c[0] == 'UP':
                ch = 1
                try:
                    u = int(c[1])
                except ValueError:
                    u = int(l[b.index(c[1])])
                for i in range(u):
                    canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image1)
                    if y != 0:
                        y -= 25
                    else:
                        canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image2)
                        x = 10000
                        j = len(com)
                    canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image)

            if c[0] == 'DOWN':
                ch = 1
                try:
                    u = int(c[1])
                except ValueError:
                    u = int(l[b.index(c[1])])
                for i in range(u):
                    canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image1)
                    if y != 500:
                        y += 25
                    else:
                        canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image2)
                        x = 10000
                        j = len(com)
                    canvas.create_image(x + 1, y + 1, anchor=NW, image=python_image)
            if c[0] == 'SET':
                ch = 1
                if c[1] not in b:
                    try:
                        kl = int(c[3])

                    except ValueError:
                        kl = l[b.index(c[1])]
                    b.append(c[1])
                    l.append(kl)

                else:
                    l[b.index(c[1])] = c[3]

            if c[0] == 'REPEAT':
                ch = 1
                try:
                    l3 = int(c[1])

                except ValueError:
                    l3 = int(l[b.index(c[1])])

                h = [i for i, ltr in enumerate(cl.split('\n')) if ltr == 'ENDREPEAT']

                for i in range(len(h)):
                    if h[i] < j:
                        h[i] = 100000
                l1 = min(h)
                l2 = j
                l4 = 0

            if j == l1 and l4 + 1 < l3:
                j = l2
                l4 += 1

            if c[0] == 'PROCEDURE':
                ch = 1
                g3.append(c[1])
                h = [i for i, ltr in enumerate(cl.split('\n')) if ltr == 'ENDPROC']
                for i in range(len(h)):
                    if h[i] < j:
                        h[i] = 100000
                g1.append(min(h))
                g2.append(j)
                j = min(h)

            if c[0] == 'CALL':
                ch = 1
                t = g3.index(c[1])
                f1 = j
                j = g2[t]
                f2 = g1[t]

            if j == f2:
                j = f1
            j += 1
            try:
                if int(c[1]) <= 0 or int(c[1]) >= 1001:
                    if cl5 == 0:
                            cl4 = f'invalid syntax in the string {cl2.index(cl1) + 1} "{cl1}"'
                            cl5 = 1
                            root1 = Tk()
                            root1.title("ERROR")
                            root1.geometry("300x100+125+125")
                            root1.resizable(width=False, height=False)

                    else:
                        cl4 += f', {str(cl2.index(cl1)+1)} "{cl1}"'
                    root['background'] = '#FF0000'
                    label2 = Label(root1, text=cl4)
            except Exception:
                pass
            if ch == 0 and cl1 != '' and cl1 != 'ENDPROC' and cl1 != 'ENDREPEAT' and cl1 != 'ENDIF':
                if cl5 == 0:
                    cl4 = f'invalid syntax in the string {cl2.index(cl1) + 1} "{cl1}"'
                    cl5 = 1
                    root1 = Tk()
                    root1.title("ERROR")
                    root1.geometry("300x100+125+125")
                    root1.resizable(width=False, height=False)

                else:
                    cl4 += f', {str(cl2.index(cl1)+1)} "{cl1}"'
                root['background'] = '#FF0000'
                label2 = Label(root1, text=cl4)
    except Exception:
        if cl5 == 0:
            cl4 = f'invalid syntax in the string {cl2.index(cl1) + 1} "{cl1}"'
            root1 = Tk()
            root1.title("ERROR")
            root1.geometry("300x100+125+125")
            root1.resizable(width=False, height=False)
        else:
            cl4 += f', {str(cl2.index(cl1)+1)} "{cl1}"'
        root['background'] = '#FF0000'
        label2 = Label(root1, text=cl4)
    try:
        label2.place(width=300, height=70)
    except UnboundLocalError:
        pass
def click_button1():
    global clh
    ch = 1
def click_button2():
    for x in range(21):
        for y in range(21):
            canvas.create_image(x * 25 + 1, y * 25 + 1, anchor=NW, image=python_image3)
    canvas.create_image(1, 1, anchor=NW, image=python_image)


def click_button3():
    ro('com.txt')


root = Tk()
root.geometry("550x575+0+0")
root.title("Олегум")
root['background'] = '#606060'

root.resizable(width=False, height=False)
btn = ttk.Button(text='run', command=click_button, width=10)
btn1 = ttk.Button(text='stop', command=click_button1, width=10)
btn2 = ttk.Button(text='reset', command=click_button2, width=10)
btn3 = ttk.Button(text='console', command=click_button3, width=10)
label = ttk.Label()
label1 = ttk.Label()

btn.place(x=45, y=7)
btn1.place(x=145, y=7)
btn2.place(x=320, y=7)
btn3.place(x=420, y=7)
label.pack()
label1.pack()

canvas = Canvas(width=523, height=523)
canvas['background'] = '#808080'
canvas.pack(anchor=N, expand=1)

for i in range(0, 525, 25):
    canvas.create_line(i, 0, i, 525, fill='#404040')
    canvas.create_line(0, i, 525, i, fill="#404040")

python_image  = PhotoImage(file="python.png")
python_image1 = PhotoImage(file="python1.png")
python_image2 = PhotoImage(file="python2.png")
python_image3 = PhotoImage(file="python3.png")
canvas.create_image((0 + 1), 0 + 1, anchor=NW, image=python_image)
ro('com.txt')

root.mainloop()
