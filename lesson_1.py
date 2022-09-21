print("Hello there")
print("My name is {}, my number is {} ".format('Darwish', '45678905'))

print("The name is  {n}, my number is {m} ".format(n= 'Darwish', m= 45678905))

# List

mylist = [1,3,3,4,5,6,6,[200,300]]
print(mylist)
y = mylist[2]
print(y)

# LOgic 

x= 1>2 and (3 == 2)

print(x)

x= 1<2 and (3 == 3)
print(x)


if 1 == 3:
    print("Yeah!!!!!!!!")
elif 'a'=='a':
    print("NO True")
else:
    print("Not There is an error!!!!!")

# For loop

seq = [1,2,3,4]
for i in seq:
    print(i*3)

i = 1
while i < 4:
    print(" I is {} ".format(i))
    i = i+1


m = [23,3,21,32,14]
n = []
for i in m:
    n.append(i*5)
print(n)

# Funtions 

def my_fun(name =  'No name'):
    print('Hello '+ name)

my_fun("cade")

def square(x):
    return x**2

result = square(8)
print(result)

# String

st = 'Ali husain cade'
w = 'Ali' in st
print(w)
st.lower()
print(st)
x= st.split()
print(x)
st2 = ' hello#election'
y = st2.split('#')
print(y)

d = {'x': 'Ali', 'y': 'hussain'}
q= d.items
print(q)




