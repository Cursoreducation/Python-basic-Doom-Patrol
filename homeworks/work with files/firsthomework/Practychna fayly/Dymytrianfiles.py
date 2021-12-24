# 1. Create calculator app which will write results to file.
# User Input
# 3
# +
# 4
# Output in result.txt
# 3 + 4 = 7
# User Input:
# 6
# -
# 1
# Output in result.txt
# 6 - 1 = 5

print("User Input:\n")
a=str(input(" "))
c=str(input(" ")) #введення знаку арифметичної операції
b=str(input(" "))
d=a+c+b
p=eval(d)

with open("result.txt", "a") as fi:
    fi.write(f"{a} {c} {b} = {p} ")

