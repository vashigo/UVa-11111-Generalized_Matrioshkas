#Andres David Vasquez
#2101770
from sys import stdin
def main():
    stack1,stack2,band=None,None,None
    for dato in stdin.readlines():
        dato=dato.strip().split()
        stack1,stack2=list(),list()
        i,j,band,s=0,len(dato),True,None
        while band and i<j:
            datos=int(dato[i])
            if datos<0:
                stack1.append(datos)
                stack2.append(datos*(-1))
            else:
                if len(stack1)==0 or stack1[-1]+datos!=0:
                    band=False
                else:
                    stack2.pop()
                    stack1.pop()
                    if len(stack1)>0:
                        s=stack2.pop()-datos
                        if s<=0:
                            band=False
                        stack2.append(s)
            i+=1
        band=band and len(stack1)==0
        if band:
            print(':-) Matrioshka!')
        else:
            print(':-( Try again.')
main()
