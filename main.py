import tkinter
import string
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.ttk import*
import pymysql

top = Tk()
top.title('QuicKart')
top.geometry("450x500")
top['background']='#fff'
 

                    #_______SIGN-UP WINDOW_______
def signup():
    top.destroy()
    global var0, var1,var2, var3, root  #will be used globally
    root = Tk(className= "Sign Up")
    root.geometry("450x500")
    var0, var1,var2, var3 = StringVar(),StringVar(),StringVar(), StringVar()
    l0 = Label(root, text = "Enter your details to Sign-up", font="Algerian")
    l0.place(x = 80, y=70)
    l1 = Label(root, text = "Enter Name", font= ('serif',10)).place(x = 30, y=150)
    en1 = tkinter.Entry(root, width=30,textvariable=var0)
    en1.place(x = 200, y = 150 )
    l2 = Label(root, text = "Enter Mobile Number", font= ('serif',10)).place(x = 30, y=200)
    en2 = tkinter.Entry(root, width=30,textvariable=var1)
    en2.place(x = 200, y = 200 )
    l3 = Label(root, text = "Enter Password", font= ('serif',10)).place(x = 30, y=250)
    en3 = tkinter.Entry(root, width=30 ,textvariable=var2)
    en3.place(x = 200, y = 250 )
    l4 = Label(root, text = "Confirm Password", font= ('serif',10)).place(x = 30, y=300)
    en4 = tkinter.Entry(root, width=30 ,textvariable=var3)
    en4.place(x = 200, y = 300 )
    bu1 = tkinter.Button(root, text = "Sign Up", command=entry)
    bu1.place(x = 190, y = 360 )
    print(var0.get(),var1.get(),var2.get())
    root.mainloop()
    
def entry():
    
    if(var0.get() == "" or var1.get() == "" or var2.get() == "" or var3.get() == ""):
         messagebox.showerror("Error","Fill all the details")
    else:
        if(len(var1.get()) != 10):
            messagebox.showerror("Error","Invalid Mobile Number")
        if(var2.get() != var3.get()):
            messagebox.showerror("Error","Password should match")
        else:
            conn = pymysql.connect(
                host = 'localhost',
                user = 'root',
                password = 'Y@sh12122001',
                db = 'db'
            )
            cur = conn.cursor()
            sql = 'insert into login values(%s,%s,%s)'
            val = (var1.get(),var0.get(),var2.get())
            cur.execute(sql,val)
            conn.commit()
           
            messagebox.showinfo("Confirmation","Signed In successfully")
            root.destroy()
            products()
            
def products():
    global pro
    pro = Tk()
    pro.title('Products')
    pro.geometry("450x500")
    
    l_0 =Label(pro,text="Select product type", width=20,font=("Algerian",20))
    l_0.place(x=70,y=70)
    
    b_1 =tkinter.Button(pro, text='Electronics', command=electronics, width=15, height =3, bg="black",fg='white')
    b_1.place(x=75, y=150)
    b_2 =tkinter.Button(pro, text='Eatables', command=eatables, width=15, height =3, bg="black",fg='white')
    b_2.place(x=250, y=150)
    b_3 =tkinter.Button(pro, text='Clothes', command=clothes, width=15, height =3, bg="black",fg='white')
    b_3.place(x=75, y=240)
    b_4 =tkinter.Button(pro, text='Home Decor', command=home_decor, width=15, height =3, bg="black",fg='white')
    b_4.place(x=250, y=240)
    pro.mainloop()

                    #_______ELECTRONICS WINDOW_______

def electronics():
    pro.destroy()
    global l2
    global root
    root = Tk()
    root.title('Electronics')
    root.geometry("450x500")
    
    l0 =Label(root,text="Electronics", width=20,font=("Algerian",20))
    l0.place(x=155, y=30)
    l1 =Label(root,text="Select from below items to wishlist", width=30,font=("serif",12))
    l1.place(x=90, y=80)
    
    l2= Listbox(root, selectmode='multiple', width=39, height=8)
    l2.insert(1,"Sony WH-CH510")
    l2.insert(2,"boAt Airdopes 131")
    l2.insert(3,"Samsung Galaxy F22")
    l2.insert(4,"realme C20")
    l2.insert(5,"Mi 11x")
    l2.place(x=110, y=130)
    bu =tkinter.Button(root, text='Wishlist',command= selected_item_1, width=10, bg="black",fg='white')
    bu.place(x=190, y=280)
    
    root.mainloop()

def selected_item_1():
    w_list = []   # wishlisted products gets added here
    w_list_price =[]   # wishlisted product's price gets added here
    price=[]   # after sorting wishlisted product's price gets added here
    w_list_compare = []   # after sorting wishlisted products gets added here
    for i in l2.curselection():
        items = l2.get(i)
        w_list.append(items)

 
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'Y@sh12122001',
        db = 'db',
    )
    cur = conn.cursor()
    sql = 'select * from electronics'
    cur.execute(sql)
    output = cur.fetchall()
    for i in w_list:
        for j in output:
            if(j[0] == i):
                w_list_price.append(j[1])
            else:
                continue
    w_list_price.sort()
    for i in w_list_price:
        for j in output:
            if(j[1] == i):
                w_list_compare.append(j[0])
            else:
                continue
    lc = tkinter.Label(root, text=("\n".join(w_list_compare))).place(x=110 ,y=340)

                    #_______EATABLES WINDOW_______

def eatables():
    pro.destroy()
    global l2
    global eat
    eat = Tk()
    eat.title('Eatables')
    eat.geometry("450x500")
    
    l0 =Label(eat, text="Eatables", width=20,font=("Algerian",20))
    l0.place(x=155, y=30)
    l1 =Label(eat, text="Select from below items to wishlist", width=30,font=("serif",12))
    l1.place(x=90, y=80)
    
    l2= Listbox(eat, selectmode='multiple', width=39, height=8)
    l2.insert(1,"Apple")
    l2.insert(2,"Oranges")
    l2.insert(3,"Banana")
    l2.insert(4,"Tomato")
    l2.insert(5,"Cucumber")
    l2.place(x=110, y=130)
    bu =tkinter.Button(eat, text='Wishlist', command=selected_item_2, width=10, bg="black",fg='white')
    bu.place(x=190, y=280)
    
    eat.mainloop()

def selected_item_2():
    w_list = []   # wishlisted products gets added here
    w_list_price =[]   # wishlisted product's price gets added here
    price=[]   # after sorting wishlisted product's price gets added here
    w_list_compare = []   # after sorting wishlisted products gets added here
    for i in l2.curselection():
        items = l2.get(i)
        w_list.append(items)
    
 
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'Y@sh12122001',
        db = 'db',
    )
    cur = conn.cursor()
    sql = 'select * from eatables'
    cur.execute(sql)
    output = cur.fetchall()
    for i in w_list:
        for j in output:
            if(j[0] == i):
                w_list_price.append(j[1])
            else:
                continue
    w_list_price.sort()
    for i in w_list_price:
        for j in output:
            if(j[1] == i):
                w_list_compare.append(j[0])
            else:
                continue
    lc = tkinter.Label(eat, text=("\n".join(w_list_compare))).place(x=110 ,y=340)
    
                    #_______CLOTHES WINDOW_______

def clothes():
    global l2
    global cloth
    pro.destroy()
    cloth = Tk()
    cloth.title('Clothes')
    cloth.geometry("450x500")
    
    l0 =Label(cloth,text="Clothes", width=20,font=("Algerian",20))
    l0.place(x=165, y=30)
    l1 =Label(cloth,text="Select from below items to wishlist", width=30,font=("serif",12))
    l1.place(x=90, y=80)
    
    l2= Listbox(cloth, selectmode='multiple', width=39, height=8)
    l2.insert(1,"Formal shirt")
    l2.insert(2,"Casual T-Shirt")
    l2.insert(3,"Trousers")
    l2.insert(4,"Sports shoes")
    l2.insert(5,"Bomber Jacket")
    l2.place(x=110, y=130)
    bu =tkinter.Button(cloth, text='Wishlist', command=selected_item_3, width=10, bg="black",fg='white')
    bu.place(x=190, y=280)
    
    cloth.mainloop()  
    
def selected_item_3():
    w_list = []
    w_list_price =[]
    price=[]
    w_list_compare = []
    for i in l2.curselection():
        items = l2.get(i)
        w_list.append(items)
    

    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'Y@sh12122001',
        db = 'db',
    )
    cur = conn.cursor()
    sql = 'select * from clothes'
    cur.execute(sql)
    output = cur.fetchall()
    for i in w_list:
        for j in output:
            if(j[0] == i):
                w_list_price.append(j[1])
            else:
                continue
    w_list_price.sort()
    for i in w_list_price:
        for j in output:
            if(j[1] == i):
                w_list_compare.append(j[0])
            else:
                continue
    lc = tkinter.Label(cloth, text=("\n".join(w_list_compare))).place(x=110 ,y=340)
        
    
                    #_______HOME DECOR WINDOW_______

def home_decor():
    global l2
    global home
    pro.destroy()
    home = Tk()
    home.title('Home Decor')
    home.geometry("450x500")
    
    l0 =Label(home,text="Home Decor", width=20,font=("Algerian",20))
    l0.place(x=155, y=30)
    l1 =Label(home,text="Select from below items to wishlist", width=30,font=("serif",12))
    l1.place(x=90, y=80)
    
    l2= Listbox(home, selectmode='multiple', width=39, height=8)
    l2.insert(1,"Wall clock")
    l2.insert(2,"Wooden key holder")
    l2.insert(3,"Wall stickers")
    l2.insert(4,"Night lamp")
    l2.insert(5,"Curtains")
    l2.place(x=110, y=130)
    bu =tkinter.Button(home, text='Wishlist', command=selected_item_4, width=10, bg="black",fg='white')
    bu.place(x=190, y=280)
    
    home.mainloop()

def selected_item_4():
    w_list = []   # wishlisted products gets added here
    w_list_price =[]   # wishlisted product's price gets added here
    price=[]   # after sorting wishlisted product's price gets added here
    w_list_compare = []   # after sorting wishlisted products gets added here
    for i in l2.curselection():
        items = l2.get(i)
        w_list.append(items)
    

    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'Y@sh12122001',
        db = 'db',
    )
    cur = conn.cursor()
    sql = 'select * from home_decor'
    cur.execute(sql)
    output = cur.fetchall()
    for i in w_list:
        for j in output:
            if(j[0] == i):
                w_list_price.append(j[1])
            else:
                continue
    w_list_price.sort()
    for i in w_list_price:
        for j in output:
            if(j[1] == i):
                w_list_compare.append(j[0])
            else:
                continue
    lc = tkinter.Label(home, text=("\n".join(w_list_compare))).place(x=110 ,y=340)
#     price = str(w_list_price)
#     lcp = tkinter.Label(home, text=(" ".join(price))).place(x=240 ,y=340)
#     a = StringVar()
#     for j in w_list_price:
#         a=str(price.append(j))
#         lcp = tkinter.Label(home, textvariable=("\n".join(a)))
#         lcp.place(x=240 ,y=340)
#     for j in w_list_price:
#         a= IntVar()
#         a.set(j)
#         price.append(c,str(a))
#     lcp = tkinter.Label(home, textvariable=price).place(x=240 ,y=340)
#     print(price)
    
def check():

    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'Y@sh12122001',
        db = 'db',
    )
    cur = conn.cursor()
    sql = 'select * from login'
    cur.execute(sql)
    output = cur.fetchall()
    for i in output: 
        if(i[0] == v1.get()):
            if(i[2]==v2.get()):
                top.destroy()
                products()
                break
            else:
                messagebox.showerror("Error","Wrong password")
                break
    else:
        messagebox.showerror("Error","UserId does not exists")
        
    conn.close()

v1, v2 = StringVar(),StringVar()
l0 =Label(top, text ="Welcome to QuicKart",font = ("Algerian",20))
l0.place(x=70, y=50)
l1 =Label(top, text="Enter Mobile Number", font= ('serif',10)).place(x=50, y=125)
e1 =Entry(top,textvariable=v1, width=30).place(x=210, y=125)

l2 =Label(top, text="Enter Password", font= ('serif',10)).place(x=50, y=175)
e2 =Entry(top,textvariable=v2, width=30).place(x=210, y=175)

bu1 =Button(top, text='Sign-In', command= check, width=15)
bu1.place(x=210, y=230)
l3 =Label(top, text="New to QuicKart?", font= ('serif',8)).place(x=165, y=300)
bu1 =Button(top, text='Create a QuicKart account',command=signup, width=30)
bu1.place(x=120, y=330)

top.mainloop()
