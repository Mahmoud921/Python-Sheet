def reverse_string(s):
    return s[::-1]

# another solution
def reverse_string2(s):
    new_str =""
    for i in s:
        new_str = i + new_str
    return new_str

s=input()
print(reverse_string(s))
print(reverse_string2(s))