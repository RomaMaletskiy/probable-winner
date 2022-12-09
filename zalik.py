file=open("h.txt")
x=file.read()
podil=x.split('\n')
print('Знайдені виміри:')
for line in podil:
    k=line.split(" ")
    print(k[1])

search=input("Введіть число формату AAA ")

for line in podil:
    k = line.split(" ")
    if search < k[1]:
        print(line, end='\n')
