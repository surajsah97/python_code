boll=input('enter the run : ')
run=boll.split()
print('------------------score card------------------\n')
order=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th']
players=[f'{x} player' for x in order]
ii=0
total=0
extra=0
wkt=0
over=0
p1=players[0]
p2=players[1]
recode={}
a,b,c=0,0,0
pp=0
for j in range(len(run)):
    i=run[j]
    if i in '012345678':
        ii=int(i)
        total+=ii
        over+=1
    else:
        if 'wkt' in i:
            wkt+=1
            ii=int(i[0])
            total+=ii
            over+=1
            if c==0 :
                print(p1,'out',a)
                a=0
                p1=players[wkt+1]
            elif c==1:
                print(p2,'out',b)
                b=0
                p2=players[wkt+1]
                
        elif 'lb' in i:
            ii=int(i[0])
            total+=ii
            extra+=ii
            ii=0
            over+=1
            
        elif 'nb' in i:
            ii=int(i[0])
            total+=ii
            extra+=1
            ii=ii-1
            
            
        elif 'wd' in i:
            ii=int(i[0])
            total+=ii
            extra+=ii
            ii=0
              
    if j==0:
        a+=ii
        recode[p1]=a
        c=a
        
    else:
        if c%2==0:
            a=a+ii
            recode[p1]=a
            if ii%2==0 and over%6==0:
                c=1
            elif ii%2==0 or over%6==0:
                c=0
            else:
                c=1    
            
        else:
            b=b+ii
            recode[p2]=b
            if ii%2==0 and over%6==0:
                c=0
            elif ii%2==0 or over%6==0:
                c=1
            else:
                c=0
print(p1,'not out',a)
print(p2,'not  out',b,"\n")
print("total", total)   
print("extra", extra)
       
