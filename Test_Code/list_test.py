a = [1, 2, 3, 4]
b = a
b.append(6)
print(a)
print(id(a))
print(id(b))

s1 = "giri"
s2 = s1
print(id(s1))
print(id(s2))
s2 += "is"
print(s1)
print(s2)
print(id(s1))
print(id(s2))