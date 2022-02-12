import time

a=int(input("Enter half the length of x"))
p="#"
for s in range(a):
    print(s*" ",p,sep="",end="")
    print((a-s)*2*" ",p,sep="")
    time.sleep(0.01)
for t in range(a,0,-1):
    print(t*" ",p,sep="",end="")
    print((a-t)*2*" ",p,sep="")
    time.sleep(0.01)
