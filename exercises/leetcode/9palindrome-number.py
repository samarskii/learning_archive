x = str(x)
x = list(x)


check = list()
for i in range(len(x)):
    if x[i-1] == x[-i]:
        # print("Palindrome")
        check.append("Palindrome")
    else:
        # print("Not palindrome")
        check.append("Not palindrome")

solution = None
if "Not palindrome" in check:
    solution = False
else: 
    solution = True
    
print(solution)