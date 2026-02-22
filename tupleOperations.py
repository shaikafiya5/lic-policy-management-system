tup=(1,2,3,4,"afiya")## indirect modification of tuple
temp=list(tup)
temp.append(7)
temp.pop(3)
tup=tuple(temp)
print(tup)
tup2=(1,2,3,45,)

print(tup2.count(3))

print(tup2.index(1))
print(len(tup2))





