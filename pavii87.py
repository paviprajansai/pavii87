p1=input()
ab=0
for i in range(0,len(p1)):
    pp=p1[0:i]+n1[i+1::]
    if int(pp)%8==0:
        ab=1
        break
if ab==1:
    print("yes")
else:
    print("no")
