s=input()
spaces=""
result=""
for char in s:
    if char==" ":
        spaces+=char
    else:
        result+=char
final_string=spaces+result
print(final_string)