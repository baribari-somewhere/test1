from dataclasses import dataclass
from tkinter import Tk, Canvas
import random

tk = Tk()
canvas = Canvas(tk, width=1000, height=1000, bg="white")
canvas.pack()

tick = 2  # フレームレート


# 座席のクラス
@dataclass
class Chair:
    id: int
    x1: int
    y1: int
    x2: int
    y2: int
    state: str
    value: int
    passion: int
    FB : int
    near: int
    yobi : int


chairs = [
    Chair(1, 200, 300, 300, 400, "free",100 ,0,0,0,0),Chair(2, 300, 300, 400, 400, "free",80 ,0,0,0,0),
    Chair(3, 400, 300, 500, 400, "free",80 ,0,0,0,0),Chair(4, 500, 300, 600, 400, "free",80 ,0,0,0,0),
    Chair(5, 600, 300, 700, 400, "free",80 ,0,0,0,0),Chair(6, 700, 300, 800, 400, "free",95 ,0,0,0,0),
    Chair(7, 200, 500, 300, 600, "free",110 ,0,0,0,0),Chair(8, 300, 500, 400, 600, "free",85 ,0,0,0,0),
    Chair(9, 400, 500, 500, 600, "free",85 ,0,0,0,0),Chair(10, 500, 500, 600, 600, "free",85 ,0,0,0,0),
    Chair(11, 600, 500, 700, 600, "free",85 ,0,0,0,0), Chair(12, 700, 500, 800, 600, "free",105 ,0,0,0,0),
    Chair(13, 200, 700, 300, 800, "free",120 ,0,0,0,0),Chair(14, 300, 700, 400, 800, "free",90 ,0,0,0,0),
    Chair(15, 400, 700, 500, 800, "free",90 ,0,0,0,0),Chair(16, 500, 700, 600, 800, "free",90 ,0,0,0,0),
    Chair(17, 500, 700, 700, 800, "free",90 ,0,0,0,0),Chair(18, 700, 700, 800, 800, "free",115 ,0,0,0,0),
]


# 座席の配置
def chair():
    for chair in chairs:
        if chair.state=="free" or chair.state=="search" or chair.state=="sleep":
            canvas.create_rectangle(chair.x1, chair.y1, chair.x2, chair.y2)
        elif chair.state=="dirty":
            canvas.create_rectangle(chair.x1, chair.y1, chair.x2, chair.y2 ,outline="saddle brown")

def view():
    canvas.create_rectangle(400,100,600,200)
    canvas.create_text(25,40,text='入口',font=("Helvetica", 18, "bold"))
    canvas.create_line(50,40,120,40,fill="black",width=3)

# 人のクラス
@dataclass
class Person:
    id: int
    x3: int
    y3: int
    x4: int
    y4: int
    dx: int
    dy: int
    state: str
    passion: int


people = []

# キャンバスの掃除(処理落ち対策)
def delete():
    canvas.delete("all")
    
#座席の上を歩かない
def move4():
    for person in people:
        if person.state == "off" and person.passion==1:
            canvas.create_oval(person.x3, person.y3, person.x4, person.y4, fill="red")
            continue
        elif person.state == "off" and person.passion==-1:
            canvas.create_oval(person.x3, person.y3, person.x4, person.y4, fill="blue")
            continue
        elif person.state == "off" and person.passion==2:
            canvas.create_oval(person.x3, person.y3, person.x4, person.y4, fill="yellow")
            continue

        for chair in chairs:
            if chair.state == "search":
                if person.state == "on":
                    # 円を次の位置に
                    person.y3 = person.y3 + person.dy
                    person.y4 = person.y4 + person.dy
                    canvas.create_oval(person.x3, person.y3, person.x4, person.y4, fill="white")

                    if(person.y3==chair.y2+10):
                        person.dy = 0
                        if(person.dy==0):
                            person.x3 = person.x3 + person.dx
                            person.x4 = person.x4 + person.dx
                            if(person.x4==chair.x2-15):
                                person.dx = 0
                                person.dy = -1
                                person.y3 = person.y3 + person.dy
                                person.y4 = person.y4 + person.dy
                                

                if (person.dx==0 and person.y4==chair.y2-15) and (chair.state== "search" or chair.state=="dirty"):
                    chair.state = "sleep"
                    person.state = "off"
                    break

first_trigger=0
people_counter=0

def first_person():
    global first_trigger
    if first_trigger==0:
        num=random.random()*10
        if num<=9.5 and num>6.1:
            people.append(Person(1,50,50,120,120,1,1,"on",2))
        else:
            people.append(Person(1,50,50,120,120,1,1,"on",1))

        first_trigger=1
#人が位置についたら新しい人を加える
#??%の確率で人の隣を好む人が現れる

def add4():
    if first_trigger==1:
        c=0
        global people_counter
        num=random.random()*10
        for s in people:
            c=c+1
            
        if people[c-1].state== "off" and c<18:
            if people_counter>=3 and num>9.5:
                people.append(Person(c+1, 50,  50, 120, 120, 1,  1, "on",-1))
            elif num<=9.5 and num>=6.1:
                people.append(Person(c+1, 50,  50, 120, 120, 1,  1, "on",2))
            else:
                people.append(Person(c+1, 50,  50, 120, 120, 1,  1, "on",1))
                
            people_counter=people_counter+1               
#椅子を選ばせる(valueが高い席に向かう)
                  

def choice7():
    count1=0
    t=0
    s1=0
    s2=0
    s3=0
    for a in chairs:
        if a.state=="free" or a.state=="sleep" or a.state=="dirty":
            t=t+1
    #print(t)        
    for b in people:
        if b.state=="on" and b.passion==1 and t==18:              
            for c in chairs:
                if c.state=="free":
                    count1=c.value

            for cc in chairs:
                if cc.state=="free" and count1 < cc.value:
                    count1=cc.value
                    
            for d in chairs:
                if d.value==count1 and d.state=="free":
                    s1=s1+1
                    
            if s1==1:
                for dd in chairs:
                    if dd.value==count1 and dd.state=="free":
                        dd.state="search"


            elif s1>1:
                list1=[]
                for ddd in chairs:
                    if ddd.state=="free" and ddd.value==count1:
                        list1.append(ddd.id)

                pick1=random.choice(list1)
                for dddd in chairs:
                    if dddd.id==pick1:
                        dddd.state="search"
                    
                    
        elif b.state=="on" and b.passion==-1 and t==18:              
            for e in chairs:
                if e.state=="free":
                    count1=e.value

            for ee in chairs:
                if ee.state=="free" and count1 > ee.value:
                    count1=ee.value
                        
            for f in chairs:
                if f.value==count1 and f.state=="free":
                    s2=s2+1

            if s2==1:
                for ff in chairs:
                    if ff.state=="free" and ff.value==count1:
                        ff.state="search"

            elif s2>1:
                list2=[]
                for fff in chairs:
                    if fff.state=="free" and fff.value==count1:
                        list2.append(fff.id)

                pick2=random.choice(list2)
                for ffff in chairs:
                    if ffff.id==pick2:
                        ffff.state="search"

        elif b.state=="on" and b.passion==2 and t==18:
            T=0
            list3=[]
            TT=0
            list5=[]
            for g in chairs:
                if g.id<=6 and g.id>=1 and g.state=="free":
                    T=T+1
            if T>0:
                for gg in chairs:
                    if gg.id<=6 and gg.id>=1 and gg.state=="free":
                        list3.append(gg)
                for ggg in list3:
                    N=ggg.value
                for gggg in list3:
                    if gggg.value>N:
                        N=gggg.value
                for ggggg in list3:
                    if ggggg.value==N:
                        ggggg.state="search"
                        break

            elif T==0:
                for G in chairs:
                    if G.id<=12 and G.id>=7 and G.state=="free":
                        TT=TT+1
                if TT>0:
                    for GG in chairs:
                        if GG.id<=12 and GG.id>=7 and GG.state=="free":
                            list5.append(GG)
                    for GGG in list5:
                        M=GGG.value
                    for GGGG in list5:
                        if GGGG.value>M:
                            M=GGGG.value
                    for GGGGG in list5:
                        if GGGGG.value==M:
                            GGGGG.state="search"
                            break

                elif TT==0:                        
                    for h in chairs:
                        if h.state=="free":
                            count1=h.value

                    for hh in chairs:
                        if hh.state=="free" and count1 < hh.value:
                            count1=hh.value
                                    
                    for i in chairs:
                        if i.value==count1 and i.state=="free":
                            s3=s3+1
                                    
                    if s3==1:
                        for ii in chairs:
                            if ii.value==count1 and ii.state=="free":
                                ii.state="search"


                    elif s3>1:
                        list4=[]
                        for iii in chairs:
                            if iii.state=="free" and iii.value==count1:
                                list4.append(iii.id)

                        pick4=random.choice(list4)
                        for iiii in chairs:
                            if iiii.id==pick4:
                                iiii.state="search"
                    


#隣に人が来たら座席の価値が下がる            
def effect1():
    for a in chairs:
        if a.state=="sleep" and a.near==0:
            if (a.id>=2 and a.id<=5) or (a.id>=8 and a.id<=11) or (a.id>=14 and a.id<=17):
                t=a.id
                for b in chairs:
                    if b.id==t-1 or b.id==t+1:
                        b.value=b.value-50

            elif a.id==1 or a.id==7 or a.id==13:
                v=a.id
                for d in chairs:
                    if d.id==v+1:
                        d.value=d.value-50

            elif a.id==6 or a.id==12 or a.id==18:
                w=a.id
                for e in chairs:
                    if e.id==w-1:
                        e.value=e.value-50

            a.near=1

#前後に人がいた場合は座席の価値が下がる
def effect2():
    for a in chairs:
        if a.state=="sleep" and a.FB==0 and (a.id>=2 and a.id<=5):
            for b in chairs:
                if b.id==a.id + 6:
                    b.value=b.value - 30
                    a.FB=1
        
                    
        elif a.state=="sleep" and a.FB==0 and (a.id>=8 and a.id<=11):
            for c in chairs:
                if c.id==a.id + 6:
                    c.value=c.value - 30
                    
                elif c.id==a.id - 6:
                    c.value=c.value - 20
                a.FB=1

        elif a.state=="sleep" and a.FB==0 and (a.id>=14 and a.id<=17):
            for d in chairs:
                if d.id==a.id - 6:
                    d.value=d.value - 20
                    a.FB=1

num=random.randint(1,100)
def dirty():
    global num
    for a in chairs:
        if a.id==num:
            a.state="dirty"
def sit():
    t=0
    for a in chairs:
        if a.state=="sleep":
            t=t+1
    for b in chairs:
        if t==17 and b.state=="dirty":
            b.state="search"

#着席の記録
L=[]
def Reporter(x):
    for a in chairs:
        if a.state=="sleep" and a.passion==0:
            x.append(a.id)
            a.passion=1

path_w='report2.txt'
write_trigger=0

#ファイルに書き込み
def Writer(x):
    global write_trigger
    if len(x)==18 and write_trigger==0:
        L_str=[str(i) for i in L]
        with open(path_w,mode='a') as f:
            f.writelines('/'.join(L_str))
            f.write('\n')
            #f.writelines(L_str)
            write_trigger=1




def main():
    dirty()
    delete()
    chair()
    view()
    sit()
    first_person()
    move4()
    add4()
    effect1()
    effect2()
    choice7()
    Reporter(L)
    Writer(L)
    tk.after(tick, main)

#実行
tk.after(tick, main)
tk.mainloop()
