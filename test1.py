tail="***"
blank="      "
x="*"
print(blank+x)

for inc in range(6):
    x+="**"
    blank = blank[:-1]
    print(blank+x)
    inc+=1

print("     "+tail)
