a=str(input())
v=['a','e','i','o','u']
s=['#','@','$','&']
if a in v:
    print("Vowel")
elif a in s:
    print("Invalid")
elif a not in v:
    print("Consonant")
