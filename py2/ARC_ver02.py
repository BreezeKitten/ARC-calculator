import tkinter as tk

window = tk.Tk()
window.title('ARC計算機_ver02_breezekitten')
window.geometry('405x370')

var_V = tk.StringVar()
var_C = tk.StringVar()
var_L = tk.StringVar()
var_A = tk.StringVar()
var_M = tk.StringVar()
var_E = tk.StringVar()


vanish = tk.PhotoImage(file = 'vanish.gif')
V = tk.Label(window,width=40, height=40, image = vanish)
V.place(x=20,y=20,anchor='nw')

V_lv = tk.Label(window,width=1,heigh=1,font=('Arial',10),text='Lv.')
V_lv.place(x=24,y=65,anchor='nw')

V_lv_in = tk.Entry(window,width=2)
V_lv_in.place(x=43,y=65,anchor='nw')

V_Sl = tk.Label(window,width=1,heigh=1,font=('Arial',12),text='/')
V_Sl.place(x=33,y=87,anchor='nw')

V_num = tk.Label(window,width=3,heigh=1,font=('Arial',10),textvariable= var_V)
V_num.place(x=42,y=88,anchor='nw')

V_num_now_in = tk.Entry(window,width=3)
V_num_now_in.place(x=10,y=90,anchor='nw')

chew = tk.PhotoImage(file = 'chew.gif')
C = tk.Label(window,width=40, height=40, image = chew)
C.place(x=80,y=20,anchor='nw')

C_lv = tk.Label(window,width=1,heigh=1,font=('Arial',10),text='Lv.')
C_lv.place(x=84,y=65,anchor='nw')

C_lv_in = tk.Entry(window,width=2)
C_lv_in.place(x=103,y=65,anchor='nw')

C_Sl = tk.Label(window,width=1,heigh=1,font=('Arial',12),text='/')
C_Sl.place(x=93,y=87,anchor='nw')

C_num = tk.Label(window,width=3,heigh=1,font=('Arial',10),textvariable= var_C)
C_num.place(x=102,y=88,anchor='nw')

C_num_now_in = tk.Entry(window,width=3)
C_num_now_in.place(x=70,y=90,anchor='nw')

Lacheln = tk.PhotoImage(file = 'Lacheln.gif')
L = tk.Label(window,width=40, height=40, image = Lacheln)
L.place(x=140,y=20,anchor='nw')

L_lv = tk.Label(window,width=1,heigh=1,font=('Arial',10),text='Lv.')
L_lv.place(x=144,y=65,anchor='nw')

L_lv_in = tk.Entry(window,width=2)
L_lv_in.place(x=163,y=65,anchor='nw')


L_Sl = tk.Label(window,width=1,heigh=1,font=('Arial',12),text='/')
L_Sl.place(x=153,y=87,anchor='nw')

L_num = tk.Label(window,width=3,heigh=1,font=('Arial',10),textvariable= var_L)
L_num.place(x=162,y=88,anchor='nw')

L_num_now_in = tk.Entry(window,width=3)
L_num_now_in.place(x=130,y=90,anchor='nw')

Arcana = tk.PhotoImage(file = 'Arcana.gif')
A = tk.Label(window,width=40, height=40, image = Arcana)
A.place(x=20,y=110,anchor='nw')

A_lv = tk.Label(window,width=1,heigh=1,font=('Arial',10),text='Lv.')
A_lv.place(x=24,y=155,anchor='nw')

A_lv_in = tk.Entry(window,width=2)
A_lv_in.place(x=43,y=155,anchor='nw')

A_Sl = tk.Label(window,width=1,heigh=1,font=('Arial',12),text='/')
A_Sl.place(x=33,y=177,anchor='nw')

A_num = tk.Label(window,width=3,heigh=1,font=('Arial',10),textvariable= var_A)
A_num.place(x=42,y=178,anchor='nw')

A_num_now_in = tk.Entry(window,width=3)
A_num_now_in.place(x=10,y=180,anchor='nw')

Morass = tk.PhotoImage(file = 'Morass.gif')
M = tk.Label(window,width=40, height=40, image = Morass)
M.place(x=80,y=110,anchor='nw')

M_lv = tk.Label(window,width=1,heigh=1,font=('Arial',10),text='Lv.')
M_lv.place(x=84,y=155,anchor='nw')

M_lv_in = tk.Entry(window,width=2)
M_lv_in.place(x=103,y=155,anchor='nw')

M_Sl = tk.Label(window,width=1,heigh=1,font=('Arial',12),text='/')
M_Sl.place(x=93,y=177,anchor='nw')

M_num = tk.Label(window,width=3,heigh=1,font=('Arial',10),textvariable= var_M)
M_num.place(x=102,y=178,anchor='nw')

M_num_now_in = tk.Entry(window,width=3)
M_num_now_in.place(x=70,y=180,anchor='nw')

Esfera = tk.PhotoImage(file = 'Esfera.gif')
E = tk.Label(window,width=40, height=40, image = Esfera)
E.place(x=140,y=110,anchor='nw')

E_lv = tk.Label(window,width=1,heigh=1,font=('Arial',10),text='Lv.')
E_lv.place(x=144,y=155,anchor='nw')

E_lv_in = tk.Entry(window,width=2)
E_lv_in.place(x=163,y=155,anchor='nw')

E_Sl = tk.Label(window,width=1,heigh=1,font=('Arial',12),text='/')
E_Sl.place(x=153,y=177,anchor='nw')

E_num = tk.Label(window,width=3,heigh=1,font=('Arial',10),textvariable= var_E)
E_num.place(x=162,y=178,anchor='nw')

E_num_now_in = tk.Entry(window,width=3)
E_num_now_in.place(x=130,y=180,anchor='nw')

Lacheln_coin = tk.PhotoImage(file = 'Lacheln_coin.gif')
L_c_p = tk.Label(window,width=40, height=40, image = Lacheln_coin)
L_c_p.place(x=50,y=200,anchor='nw')

L_c_in = tk.Entry(window,width=4)
L_c_in.place(x=56,y=242,anchor='nw')

Arcana_coin = tk.PhotoImage(file = 'Arcana_coin.gif')
A_c_p = tk.Label(window,width=40, height=40, image = Arcana_coin)
A_c_p.place(x=110,y=200,anchor='nw')

A_c_in = tk.Entry(window,width=4)
A_c_in.place(x=116,y=242,anchor='nw')

def num_cal():
    global DATE
    V_rank = int(V_lv_in.get())
    var_V_int = V_rank * V_rank + 11
    var_V.set(str(var_V_int))

    C_rank = int(C_lv_in.get())
    var_C_int = C_rank * C_rank + 11
    var_C.set(str(var_C_int))

    L_rank = int(L_lv_in.get())
    var_L_int = L_rank * L_rank + 11
    var_L.set(str(var_L_int))

    A_rank = int(A_lv_in.get())
    var_A_int = A_rank * A_rank + 11
    var_A.set(str(var_A_int))

    M_rank = int(M_lv_in.get())
    var_M_int = M_rank * M_rank + 11
    var_M.set(str(var_M_int))

    E_rank = int(E_lv_in.get())
    var_E_int = E_rank * E_rank + 11
    var_E.set(str(var_E_int))

    var_ARCn_int = (V_rank+C_rank+L_rank+A_rank+M_rank+E_rank)*10 + ((V_rank>0)+(C_rank>0)+(L_rank>0)+(A_rank>0)+(M_rank>0)+(E_rank>0)) *20
    var_ARCn.set(str(var_ARCn_int))

    DATE = int(DATE_in.get())
    
    ARC_goal = int(ARC_goal_in.get())
    V_num_now = int(V_num_now_in.get())
    C_num_now = int(C_num_now_in.get())
    L_num_now = int(L_num_now_in.get())
    A_num_now = int(A_num_now_in.get())
    M_num_now = int(M_num_now_in.get())
    E_num_now = int(E_num_now_in.get())
    V_add = int(V_add_in.get())
    C_add = int(C_add_in.get())
    L_add = int(L_add_in.get())
    L_add_h = int(L_add_h_in.get())
    A_add = int(A_add_in.get())
    A_add_h = int(A_add_h_in.get())
    M_add = int(M_add_in.get())
    E_add = int(E_add_in.get())
    L_c = int(L_c_in.get())
    A_c = int(A_c_in.get())

   
    while(var_ARCn_int < ARC_goal):
        week = weekday(DATE)
        if(weekend.get() == 1 and (week == 0 or week == 6)):

            V_num_now = V_num_now + V_add
            C_num_now = C_num_now + C_add
            if(coin.get() == 1):
                L_num_now = L_num_now + (L_c + L_add_h)//30
                L_c = (L_c + L_add_h) % 30
                A_num_now = A_num_now + (A_c + A_add_h)//3
                A_c = (A_c + A_add_h) % 3
            else:
                L_num_now = L_num_now + L_add_h
                A_num_now = A_num_now + A_add_h               
            M_num_now = M_num_now + M_add
            E_num_now = E_num_now + E_add
        else:
            V_num_now = V_num_now + V_add
            C_num_now = C_num_now + C_add
            if(coin.get() == 1):
                L_num_now = L_num_now + (L_c + L_add)//30
                L_c = (L_c + L_add) % 30
                A_num_now = A_num_now + (A_c + A_add)//3
                A_c = (A_c + A_add) % 3
            else:
                L_num_now = L_num_now + L_add
                A_num_now = A_num_now + A_add 
            M_num_now = M_num_now + M_add
            E_num_now = E_num_now + E_add           

        if(V_num_now >= (V_rank * V_rank + 11) and V_rank < 20):
            V_num_now = V_num_now - (V_rank * V_rank + 11)
            V_rank = V_rank + 1
            lb.insert('end','無名秘法於 '+repr(DATE)+'升至'+repr(V_rank)+'等')

        if(C_num_now >= (C_rank * C_rank + 11) and C_rank < 20):
            C_num_now = C_num_now - (C_rank * C_rank + 11)
            C_rank = C_rank + 1
            lb.insert('end','啾啾秘法於 '+repr(DATE)+'升至'+repr(C_rank)+'等')

        if(L_num_now >= (L_rank * L_rank + 11) and L_rank < 20):
            L_num_now = L_num_now - (L_rank * L_rank + 11)
            L_rank = L_rank + 1
            lb.insert('end','夢都秘法於 '+repr(DATE)+'升至'+repr(L_rank)+'等')

        if(A_num_now >= (A_rank * A_rank + 11) and A_rank < 20):
            A_num_now = A_num_now - (A_rank * A_rank + 11)
            A_rank = A_rank + 1
            lb.insert('end','阿爾秘法於 '+repr(DATE)+'升至'+repr(A_rank)+'等')

        if(M_num_now >= (M_rank * M_rank + 11) and M_rank < 20):
            M_num_now = M_num_now - (M_rank * M_rank + 11)
            M_rank = M_rank + 1
            lb.insert('end','魔菈秘法於 '+repr(DATE)+'升至'+repr(M_rank)+'等')

        if(E_num_now >= (E_rank * E_rank + 11) and E_rank < 20):
            E_num_now = E_num_now - (E_rank * E_rank + 11)
            E_rank = E_rank + 1
            lb.insert('end','艾斯秘法於 '+repr(DATE)+'升至'+repr(E_rank)+'等')
            
        var_ARCn_int = (V_rank+C_rank+L_rank+A_rank+M_rank+E_rank)*10 + ((V_rank>0)+(C_rank>0)+(L_rank>0)+(A_rank>0)+(M_rank>0)+(E_rank>0)) *20
        DATE = DATE + 1

    DATE = DATE - 1
    weekday(DATE)
    from tkinter import messagebox
    tk.messagebox.showinfo(title='計算完畢',message='ARC將於'+repr(DATE)+'時達到'+repr(ARC_goal))

def weekday(yyyymmdd):
    global DATE
    c = yyyymmdd // 1000000
    y = (yyyymmdd % 1000000)// 10000
    m = (yyyymmdd % 10000)// 100
    d = yyyymmdd % 100
    if( m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12 ):
        if(d > 31):
            m = m + 1
            d = 1
    elif(m == 2):
        if((c*100+y)%4 == 0):
            if(d > 29):
                m = m + 1
                d = 1
        elif(d > 28):
            m = m + 1
            d = 1
    elif( d > 30):
        m = m + 1
        d = 1
    if( m > 12):
        y = y + 1
        m = 1
        if( y > 99):
            c = c + 1
            y = 0
    DATE = c * 1000000 + y * 10000 + m * 100 + d
    if(m < 3):
        m = m + 12
        y = y - 1
    w = ( y + y//4 + c//4 - 2*c + (26*(m+1)//10) + d - 1 ) % 7
    return w
    

var_ARCn = tk.StringVar()

ARC_now = tk.Label(window,width=8,heigh=1,font=('Arial',10),text='目前ARC：')    
ARC_now.place(x=50,y=262,anchor='nw')

ARC_now_var = tk.Label(window,width=3,heigh=1,font=('Arial',10),textvariable= var_ARCn)
ARC_now_var.place(x=123,y=262,anchor='nw')

ARC_goal_s = tk.Label(window,width=8,heigh=1,font=('Arial',10),text='目標ARC：')    
ARC_goal_s.place(x=50,y=282,anchor='nw')

ARC_goal_in = tk.Entry(window,width=4)
ARC_goal_in.place(x=123,y=282,anchor='nw')

V_add_s = tk.Label(window,width=13,heigh=1,font=('Arial',10),text='無名每日：')
V_add_s.place(x=205,y=20,anchor='nw')
V_add_in = tk.Entry(window,width=3)
V_add_in.place(x=295,y=22,anchor='nw')

C_add_s = tk.Label(window,width=13,heigh=1,font=('Arial',10),text='啾啾每日：')
C_add_s.place(x=205,y=40,anchor='nw')
C_add_in = tk.Entry(window,width=3)
C_add_in.place(x=295,y=42,anchor='nw')

L_add_s = tk.Label(window,width=22,heigh=1,font=('Arial',10),text='夢都平日：        高服：')
L_add_s.place(x=205,y=60,anchor='nw')
L_add_in = tk.Entry(window,width=3)
L_add_in.place(x=295,y=62,anchor='nw')
L_add_h_in = tk.Entry(window,width=3)
L_add_h_in.place(x=365,y=62,anchor='nw')

A_add_s = tk.Label(window,width=22,heigh=1,font=('Arial',10),text='阿爾平日：        高服：')
A_add_s.place(x=205,y=80,anchor='nw')
A_add_in = tk.Entry(window,width=3)
A_add_in.place(x=295,y=82,anchor='nw')
A_add_h_in = tk.Entry(window,width=3)
A_add_h_in.place(x=365,y=82,anchor='nw')

M_add_s = tk.Label(window,width=13,heigh=1,font=('Arial',10),text='魔菈每日：')
M_add_s.place(x=205,y=100,anchor='nw')
M_add_in = tk.Entry(window,width=3)
M_add_in.place(x=295,y=102,anchor='nw')

E_add_s = tk.Label(window,width=13,heigh=1,font=('Arial',10),text='艾斯每日：')
E_add_s.place(x=205,y=120,anchor='nw')
E_add_in = tk.Entry(window,width=3)
E_add_in.place(x=295,y=122,anchor='nw')

DATE_s = tk.Label(window,width=20,heigh=1,font=('Arial',10),text='起始日期(yyyymmdd)')
DATE_s.place(x=205,y=142,anchor='nw')
DATE_in = tk.Entry(window,width=10)
DATE_in.place(x=270,y=162,anchor='nw')

weekend = tk.IntVar()
service = tk.Checkbutton(window, text='使用高服', variable=weekend,onvalue=1,offvalue=0)
service.place(x=230,y=182,anchor='nw')

coin = tk.IntVar()
service = tk.Checkbutton(window, text='計算硬幣', variable=coin,onvalue=1,offvalue=0)
service.place(x=310,y=182,anchor='nw')

lb = tk.Listbox(window,width=25,heigh=6)
lb.place(x=215,y=202,anchor='nw')

def clear():
    lb.delete(0,'end')

b = tk.Button(window, 
    text='calculate',      # 显示在按钮上的文字
    width=15, height=2, 
    command=num_cal)     # 点击按钮式执行的命令
b.place(x=60,y=355,anchor = 'sw')    # 按钮位置
    
clc = tk.Button(window, 
    text='clear',      # 显示在按钮上的文字
    width=15, height=2, 
    command=clear)     # 点击按钮式执行的命令
clc.place(x=345,y=355,anchor = 'se')    # 按钮位置


window.mainloop()
