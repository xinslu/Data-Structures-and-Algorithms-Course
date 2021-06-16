def create_l(start,z,l,index):
    for j in range(start,z//2+1):
        for k in range(2,int(j**(1/2))+1):
            if j%k==0:
                break
        else:
            l+=[j]
            if l[index]*l[index-1]==z:
                print(z)
                break
            elif l[index]*l[index-1]>z and index>2:
                print(l[index-1]*l[index-2])
                break
            index+=1

iterations= 4
l=[]    
z1=[1000000000000000000,1886946507334,82450023503539,641406572202861,923417880949942877,9591521882205647]
index=0
for i in range(iterations):
    z=z1[i]
    length=len(l)
    print(l)
    if l:
        if l[-1]*l[-2]<z:
            create_l(l[-1]+1,z,l,length-1)
        elif l[-1]*l[-2]==z:
            print(z)
            break
        else:
            for j in range(1,len(l)):
                if l[j]*l[j-1]==z:
                    print(z)
                    break
                elif l[j]*l[j-1]>z:
                    print(l[j-1]*l[j-2])
                    break
    else:
        create_l(2,z,l,index)