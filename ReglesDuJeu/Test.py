class a :
    def __init__(self,a):
        self.a = a


b = a(5)
c = b

c.a = 2

print(b.a)
print(c.a)



tab = [1,2,3,4]

i=0
while i <(len(tab)) :
    print(i)
    if tab[i] < 3 :
        del(tab[0])
    else :
        i+=1
print(tab)