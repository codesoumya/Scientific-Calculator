from tkinter import *
import math
from PIL import Image, ImageTk
pi = math.pi

def click(event):
    global screenvalue
    text= event.widget.cget("text")
    if text=="=":
        if screenvalue.get().isdigit():
            value = screenvalue.get()
        else:
            value = eval(screenvalue.get())
        screenvalue.set(value)
    elif text=="c":
        screenvalue.set("")
        scndscreenvalu.set("")
        # screen.update()
    elif text=="%":
        screenvalue.set(screenvalue.get()+"/100")
    else:
        screenvalue.set(screenvalue.get()+text)
        # screen.update()

def click2(event):
    global scndscreenvalu
    text= event.widget.cget("text")
    def split(x):
        return list(x)

    if text=="=":
        tt = str(scndscreenvalu.get())
        ll = split(tt)
        k1st = ll[0]
        if scndscreenvalu.get().isdigit():
            value = scndscreenvalu.get()
        else:
            value = eval(scndscreenvalu.get())
        scndscreenvalu.set(value)
    # elif text=="c":
    #     scndscreenvalu.set("")
    #     # screen.update()
    elif text=="c":
        scndscreenvalu.set("")
    elif text=="T":
        screenvalue.set(screenvalue.get()+scndscreenvalu.get())
    else:
        scndscreenvalu.set(scndscreenvalu.get()+text)
        # screen.update()
def click3(event):
    global scndscreenvalu
    text = event.widget.cget("text")
    if text == "x2":
        scndscreenvalu.set(x2(float(scndscreenvalu.get())))
    elif text == "x3":
        scndscreenvalu.set(x3(float(scndscreenvalu.get())))
    elif text == "x/2":
        scndscreenvalu.set(sqrt(float(scndscreenvalu.get())))
    elif text == "x/3":
        scndscreenvalu.set(qbcrt(float(scndscreenvalu.get())))
    elif text == "eX":
        scndscreenvalu.set("e")
    elif text == "xY":
        global restpwnum
        restpwnum = scndscreenvalu.get()
        scndscreenvalu.set(scndscreenvalu.get()+"power")
    elif text == "nPr":
        global restpnum
        restpnum = scndscreenvalu.get()
        scndscreenvalu.set(scndscreenvalu.get()+"p")
    elif text == "nCr":
        global restcnum
        restcnum = scndscreenvalu.get()
        scndscreenvalu.set(scndscreenvalu.get()+"c")
    elif text == "!":
        scndscreenvalu.set(xfac(float(scndscreenvalu.get())))
    elif text == "log10()":
        scndscreenvalu.set("log(")
    elif text == "log":
        global restbnum
        restbnum = scndscreenvalu.get()
        print(restbnum)
        scndscreenvalu.set(restbnum + "log")
def bckpcs(event):
    def split(word):
        return list(word)
    word = str(screenvalue.get())
    ll = split(word)
    nwll = ll[:-1]
    def listtostr(nwll):
        prstr =""
        return(prstr.join(nwll))
    nwst = listtostr(nwll)
    screenvalue.set(nwst)
def bckpcs2(event):
    def split(word):
        return list(word)
    word = str(scndscreenvalu.get())
    ll = split(word)
    nwll = ll[:-1]
    def listtostr(nwll):
        prstr =""
        return(prstr.join(nwll))
    nwst = listtostr(nwll)
    scndscreenvalu.set(nwst)

def tan(x):
    return math.tan(math.radians(x))
def sin(y):
    return math.sin(math.radians(y))
def cos(z):
    return math.cos(math.radians(z))
def asin(p):
    return math.degrees(math.asin(p))
def acos(p):
    return math.degrees(math.acos(p))
def atan(p):
    return math.degrees(math.atan(p))
def x2 (x):
    return x*x
def x3(x):
    return x*x*x
def xfac(x):
    return math.factorial(x)
def ncr(x,y):
    return ((xfac(x))/((xfac(x-y))*xfac(y)))
def npr(x,y):
    return ((xfac(x))/(xfac(x-y)))
def xpy (x,y):
    return x**y
def sqrt (x):
    return x**(1/2)
def qbcrt (x):
    return x**(1/3)
def ln(x):
    return math.log(x, math.e)
def log10(x):
    return math.log10(x)
def log(x,y):
    return math.log(x, y)
def tanget(event):
    # tt = screenvalue.get()
    global k4st, k5st, k6st, k7st, lll, tv

    def split(x):
        return list(x)
    tt = str(scndscreenvalu.get())
    lk = split(tt)
    if len(tt)>2:
        k3st = lk[2]
    else:
        k3st = ""
    if len(tt)>3:
        k4st = lk[3]
    else:
        k4st = ""
    if len(tt) > 4:
        k5st = lk[4]
    else:
        k5st = ""
    if len(tt) > 5:
        k6st = lk[5]
    else:
        k6st = ""
    if len(tt) > 6:
        k7st = lk[6]
    else:
        k7st = ""
    ll = split(tt)

    k1st = ll[0]
    k2st = ll[1]

    unwanted_num = {"t", "a", "n", "(", ")", "s", "i", "n", "c", "o", "s", "e", "p", "o", "w", "r", "l", "n", "g"}

    ll = [ele for ele in ll if ele not in unwanted_num]
    def listtostr (ll):
        prstr = ""
        return (prstr.join(ll))

    if k1st == "t":
        ll = float(listtostr(ll))
        tv = tan(ll)
    elif k1st=="c":
        ll = float(listtostr(ll))
        # global tv
        tv =cos(ll)
    elif k1st == "e":
        ll = float(listtostr(ll))
        tv = math.exp(ll)
    elif k1st == "s":
        ll = float(listtostr(ll))
        tv = sin(ll)
    elif k2st == "s":
        ll = float(listtostr(ll))
        tv = asin(ll)
    elif k2st == "c" and k1st=="a":
        ll = float(listtostr(ll))
        tv = acos(ll)
    elif k2st == "t":
        ll = float(listtostr(ll))
        tv = atan(ll)
    elif k4st == "w" or k5st== "w" or k6st =="w" or k7st =="w":
        if k4st == "w":
            del ll[0]
            lll = float(listtostr(ll))
        elif k5st == "w":
            del ll[0]
            del ll[1]
            lll = float(listtostr(ll))
        elif k6st == "w":
            del ll[0]
            del ll[1]
            del ll[2]
            lll = float(listtostr(ll))
        elif k7st == "w":
            del ll[0]
            del ll[1]
            del ll[2]
            del ll[3]
            lll = float(listtostr(ll))
        tv = xpy(float(restpwnum),lll)
    elif k2st == "p" or k3st== "p" or k4st == "p" or k5st == "p" or k6st == "p":
        if k2st == "p":
            del ll[0]
            lll = float(listtostr(ll))
        elif k3st == "p":
            del ll[0]
            del ll[1]
            lll = float(listtostr(ll))
        elif k4st == "p":
            del ll[0]
            del ll[1]
            del ll[2]
            lll = float(listtostr(ll))
        elif k5st == "p":
            del ll[0]
            del ll[1]
            del ll[2]
            del ll[3]
            lll = float(listtostr(ll))
        elif k6st == "p":
            del ll[0]
            del ll[1]
            del ll[2]
            del ll[3]
            del ll[4]
            lll = float(listtostr(ll))
        tv = npr(float(restpnum),lll)
    elif k2st == "c" or k3st== "c" or k4st == "c" or k5st == "c" or k6st == "c":
        if k2st == "c":
            del ll[0]
            lll = float(listtostr(ll))
        elif k3st == "c":
            del ll[0]
            del ll[1]
            lll = float(listtostr(ll))
        elif k4st == "c":
            del ll[0]
            del ll[1]
            del ll[2]
            lll = float(listtostr(ll))
        elif k5st == "c":
            del ll[0]
            del ll[1]
            del ll[2]
            del ll[3]
            lll = float(listtostr(ll))
        elif k6st == "c":
            del ll[0]
            del ll[1]
            del ll[2]
            del ll[3]
            del ll[4]
            lll = float(listtostr(ll))
        tv = ncr(float(restcnum),lll)
    elif k1st=="l" and k2st=="n":
        lll = float(listtostr(ll))
        tv = ln(lll)
    elif k1st=="l" and k2st=="o" and k4st=="(":
        lll = float(listtostr(ll))
        print(lll)
        tv = log10(lll)
    elif k2st=="l" or k3st=="l" or k4st == "l" or k5st=="l" or k6st=="l":
        if k2st == "l":
            del ll[0]
            lll = float(listtostr(ll))
        elif k3st == "l":
            del ll[0]
            del ll[1]
            lll = float(listtostr(ll))
        elif k4st == "l":
            del ll[0]
            del ll[1]
            del ll[2]
            lll = float(listtostr(ll))
        elif k5st == "l":
            del ll[0]
            del ll[1]
            del ll[2]
            del ll[3]
            lll = float(listtostr(ll))
        elif k6st == "l":
            del ll[0]
            del ll[1]
            del ll[2]
            del ll[3]
            del ll[4]
            lll = float(listtostr(ll))
        tv = log(lll,float(restbnum))
    scndscreenvalu.set(tv)

root = Tk()
root.configure(bg="black")
root.minsize(350,480)
root.maxsize(350,480)
root.title("Scientific Calculator")
image = Image.open("cal.jpg")
photo = ImageTk.PhotoImage(image)
root.iconphoto(False, photo)

screenvalue = StringVar()
screenvalue.set("")
screen = Entry(textvar=screenvalue, font="lucida 30 italic",bg="#e0e0e0").pack(fill=X,padx=10,pady=10,ipady=2)

f1 = Frame(root, bg="grey",padx=10)

b1f1 = Button(f1, text="c", padx=26, pady=0, bg="red", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text=".del", padx=17, pady=0, bg="red", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", bckpcs)

b1f1 = Button(f1, text="%", padx=22, pady=0, bg="#5a35de", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="/", padx=15, pady=0, bg="#5a35de", fg="white", font="lucida 13 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

f1.pack()


f1 = Frame(root, bg="grey", padx=10)

b1f1 = Button(f1, text="9", padx=26, pady=0, bg="brown", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="8", padx=26, pady=0, bg="brown", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="7", padx=26, pady=0, bg="brown", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="+", padx=13, pady=0, bg="#5a35de", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="grey",padx=10)

b1f1 = Button(f1, text="6", padx=26, pady=0, bg="brown", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="5", padx=26, pady=0, bg="brown", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="4", padx=26, pady=0, bg="brown", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="-", padx=15, pady=0, bg="#5a35de", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="grey", padx=10)

b1f1 = Button(f1, text="3", padx=26, pady=0, bg="brown", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="2", padx=26, pady=0, bg="brown", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="1", padx=26, pady=0, bg="brown", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="*", padx=14, pady=0, bg="#5a35de", fg="white", font="lucida 13 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="grey", padx=10)


b1f1 = Button(f1, text="(", padx=7, pady=0, bg="#8a0040", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=4, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text=")", padx=7, pady=0, bg="#8a0040", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="0", padx=26, pady=0, bg="brown", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=6, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text=".", padx=29, pady=0, bg="#a6a300", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)

b1f1 = Button(f1, text="=", padx=13, pady=0, bg="lime", fg="white", font="lucida 12 bold")
b1f1.pack(side=LEFT, padx=5, pady=5)
b1f1.bind("<Button-1>", click)



f1.pack()

f1 = Frame(root, bg="black", padx=5)
scndscreenvalu = StringVar()
scndscreenvalu.set("")
scndscreen = Entry(f1, textvar=scndscreenvalu, font="Roboto 12 italic",bg="#e0e0e0").pack(side=LEFT, padx=6, pady=10, ipady=5)

b1f1 = Button(f1, text=f"T", padx=0, pady=0, bg="#0da694", fg="white", font="Bungee 11 bold")
b1f1.pack(side=LEFT, pady=0, padx=3)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f1, text=f"c", padx=0, pady=0, bg="red", fg="white", font="Roboto 11 bold")
b1f1.pack(side=LEFT, pady=0, padx=3)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f1, text=f".del", padx=0, pady=0, bg="red", fg="white", font="Roboto 11 bold")
b1f1.pack(side=LEFT, pady=0, padx=3)
b1f1.bind("<Button-1>", bckpcs2)

b1f1 = Button(f1, text=f"=", padx=0, pady=0, bg="green", fg="white", font="Roboto 11 bold")
b1f1.pack(side=LEFT, pady=0, padx=3)
b1f1.bind("<Button-1>", tanget)

f1.pack()


ft = Frame(root, bg="black")
f2 = Frame(ft, bg="black", padx=10)

b1f1 = Button(f2, text=f"1", padx=5, pady=0, bg="#e3be02", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"2", padx=5, pady=0, bg="#e3be02", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"3", padx=5, pady=0, bg="#e3be02", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"0", padx=9, pady=0, bg="#e3be02", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=1)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"sin()", padx=5, pady=2, bg="#ff7700", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=10)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"cos()", padx=5, pady=2, bg="#ff7700", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"tan()", padx=5, pady=2, bg="#ff7700", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

f2.pack()



f2 = Frame(ft, bg="black", padx=10)

b1f1 = Button(f2, text=f"4", padx=5, pady=0, bg="#e3be02", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"5", padx=5, pady=0, bg="#e3be02", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"6", padx=5, pady=0, bg="#e3be02", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f".", padx=9, pady=0, bg="#0b0082", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=2)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"asin()", padx=3, pady=2, bg="#ff7700", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=10)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"acos()", padx=2, pady=2, bg="#ff7700", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"atan()", padx=3, pady=2, bg="#ff7700", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)


f2.pack()

f2.pack()

f2 = Frame(ft, bg="black", padx=10)

b1f1 = Button(f2, text=f"7", padx=5, pady=0, bg="#e3be02", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"8", padx=5, pady=0, bg="#e3be02", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"9", padx=5, pady=0, bg="#e3be02", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"(", padx=-2, pady=0, bg="#a18706", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=3)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f")", padx=-2, pady=0, bg="#a18706", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=1)
b1f1.bind("<Button-1>", click2)

b1f1 = Button(f2, text=f"x2", padx=0, pady=2, bg="blue", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=6)
b1f1.bind("<Button-1>", click3)

b1f1 = Button(f2, text=f"x3", padx=0, pady=2, bg="blue", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=4)
b1f1.bind("<Button-1>", click3)

b1f1 = Button(f2, text=f"xY", padx=0, pady=2, bg="blue", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=4)
b1f1.bind("<Button-1>", click3)

b1f1 = Button(f2, text=f"x/2", padx=0, pady=2, bg="blue", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=2)
b1f1.bind("<Button-1>", click3)

b1f1 = Button(f2, text=f"x/3", padx=0, pady=2, bg="blue", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=2)
b1f1.bind("<Button-1>", click3)

b1f1 = Button(f2, text=f"eX", padx=0, pady=2, bg="blue", fg="white", font="Roboto 7 bold")
b1f1.pack(side=LEFT, pady=5, padx=4)
b1f1.bind("<Button-1>", click3)

f2.pack()
ft.pack(anchor="nw", padx=10)


ft2 = Frame(root, bg="black")

f2 = Frame(ft2, bg="black", padx=10)
b1f1 = Button(f2, text=f"nPr", padx=5, pady=2, bg="#920696", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click3)

b1f1 = Button(f2, text=f"nCr", padx=5, pady=2, bg="#920696", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click3)

b1f1 = Button(f2, text=f"!", padx=8, pady=2, bg="#920696", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click3)

b1f1 = Button(f2, text=f"ln", padx=8, pady=2, bg="#920696", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=5)
b1f1.bind("<Button-1>", click2)


b1f1 = Button(f2, text=f"log10()", padx=5, pady=2, bg="#920696", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=6)
b1f1.bind("<Button-1>", click3)

b1f1 = Button(f2, text=f"log", padx=5, pady=2, bg="#920696", fg="white", font="Roboto 8 bold")
b1f1.pack(side=LEFT, pady=5, padx=4)
b1f1.bind("<Button-1>", click3)

f2.pack()
ft2.pack(anchor="nw", padx=10)

# Label(text=f"{math.log(5,math.e)}").pack()
# abal = "titir"
# Label(text="Titir er calculator ",bg="black", font="roboto 20 bold", fg="red").pack()
root.mainloop()
