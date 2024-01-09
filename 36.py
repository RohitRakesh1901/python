s1 = "HELLO"
s2 = s1.lower()
s3 = s2.upper()
s4 = "hello"
s5 = "Hello"
s6 = "I live in the city of Toronto"
s7 = "I Live In The City Of Toronto"
s8 = "I Live In The City Of Toronto. It Is A Beautiful City."
s9 = "hello"
s10 = "10"
s11 = 10
print(s2)
print(s3)
print(s1.isupper())
print(s4.isupper())
print(s1.islower())
print(s4.islower())
print()

print(s5.isupper())
print(s5.islower())
print()

print(s6.istitle())
print(s7.istitle())
print(s8.istitle())
print()

print(s9.isalnum())
print(s10.isalnum())
#print(s11.isalnum())   s11 is an integer, therefore getting type error
