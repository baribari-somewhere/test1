from collections import Counter
result=[]
with open(r"C:\授業用\プロジェクト\data\report2.txt") as file:
    for line in file:
        sline = line.rstrip("\n")
        slines = sline.split("/")
        result.append(slines)
        
result_1=[]
result_2=[]
result_3=[]
result_4=[]
result_5=[]
result_6=[]
result_7=[]
result_8=[]
result_9=[]
result_10=[]
result_11=[]
result_12=[]
result_13=[]
result_14=[]
result_15=[]
result_16=[]
result_17=[]
result_18=[]
#print(result)
#print(int(result[0][0])+1)
for a in result:
    for b in range(0,18):
        if (a[int(b)])=="1":
            result_1.append(int(b)+1)
        elif (a[int(b)])=="2":
            result_2.append(int(b)+1)
        elif (a[int(b)])=="3":
            result_3.append(int(b)+1)
        elif (a[int(b)])=="4":
            result_4.append(int(b)+1)
        elif (a[int(b)])=="5":
            result_5.append(int(b)+1)
        elif (a[int(b)])=="6":
            result_6.append(int(b)+1)
        elif (a[int(b)])=="7":
            result_7.append(int(b)+1)
        elif (a[int(b)])=="8":
            result_8.append(int(b)+1)
        elif (a[int(b)])=="9":
            result_9.append(int(b)+1)
        elif (a[int(b)])=="10":
            result_10.append(int(b)+1)
        elif (a[int(b)])=="11":
            result_11.append(int(b)+1)
        elif (a[int(b)])=="12":
            result_12.append(int(b)+1)
        elif (a[int(b)])=="13":
            result_13.append(int(b)+1)
        elif (a[int(b)])=="14":
            result_14.append(int(b)+1)
        elif (a[int(b)])=="15":
            result_15.append(int(b)+1)
        elif (a[int(b)])=="16":
            result_16.append(int(b)+1)
        elif (a[int(b)])=="17":
            result_17.append(int(b)+1)
        elif (a[int(b)])=="18":
            result_18.append(int(b)+1)
def pick(x):
    c = Counter(x)
    print(c.most_common())

print("id=1の着席頻度:")
pick(result_1)
print("\n")
print("id=2の着席頻度:")
pick(result_2)
print("\n")
print("id=3の着席頻度:")
pick(result_3)
print("\n")
print("id=4の着席頻度:")
pick(result_4)
print("\n")
print("id=5の着席頻度:")
pick(result_5)
print("\n")
print("id=6の着席頻度:")
pick(result_6)
print("\n")
print("id=7の着席頻度:")
pick(result_7)
print("\n")
print("id=8の着席頻度:")
pick(result_8)
print("\n")
print("id=9の着席頻度:")
pick(result_9)
print("\n")
print("id=10の着席頻度:")
pick(result_10)
print("\n")
print("id=11の着席頻度:")
pick(result_11)
print("\n")
print("id=12の着席頻度:")
pick(result_12)
print("\n")
print("id=13の着席頻度:")
pick(result_13)
print("\n")
print("id=14の着席頻度:")
pick(result_14)
print("\n")
print("id=15の着席頻度:")
pick(result_15)
print("\n")
print("id=16の着席頻度:")
pick(result_16)
print("\n")
print("id=17の着席頻度:")
pick(result_17)
print("\n")
print("id=18の着席頻度:")
pick(result_18)
print("\n")
    
            
            
