print("\n== Arrays, Matrices ==")
A = [[1,2],[3,4]]
print(A)
B = [1 ,2 ,3 ,4]
print(B)

print("\n== For loop with numbers==")
for a in [7, 6, 31, 45]:
    print(f"Value of a: {a}")
    print(a*2)
    b = a+4
    print(b)
    
    

print("\n== For loop with strings==")

for glass in ["water", "juice", "buttermilk"]:
    print (glass)


print("\n== Functions==")

def f(x):
    return 2*x


def g(x, y):
    return 2*x*x + 3*y

result = f(1)
print (f"function f value: {result}")

result2 = g(3, 4)
print (f"function f value: {result2}")


# Function to work with strings
def string_work(s):
    print(f"Original: {s}")
    print(f"Uppercase: {s.upper()}")
    print(f"Lowercase: {s.lower()}")
    print(f"Reversed: {s[::-1]}")
    print(f"Length: {len(s)}")
    

print("\n== String Function Demo ==")
string_work("Hello World!")
