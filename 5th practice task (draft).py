
#1st
year = int(input())
if year%4 != 0 or year%400 != 0:
    print(365)
else:
    print(366)


import math as m
# 2nd
import turtle as t


def cle(xc, yc, r):
    t.up()
    t.pen(pencolor='orange', pensize=1)
    t.setposition(xc, yc-r)
    t.down()
    t.circle(r)


def dott(x,  y):
    t.up()
    t.setposition(x, y)
    t.down()
    t.dot(10, 'black')


def main():
    xc = int(input())
    yc = int(input())
    r = int(input())
    x = int(input())
    y = int(input())
    cle(xc, yc, r)
    dott(x, y)
    if m.sqrt(abs((xc+x)**2)+abs((yc+y)**2)) > r:
        print('Точка вне окружности')
    elif m.sqrt(abs((xc+x)**2)+abs((yc+y)**2)) == r:
        print('Точка на окружности')
    else:
        print('Точка внутри окружности')
    t.mainloop()


if __name__ == '__main__':
    main()

#3rd
num = int(input())
if num//1000 == num%10 and num//100-((num//1000)*10) == (num%100-num%10)/10:
    print('Настоящее')
else:
    print('Кривое')

#4th
parrot = int(input())
if parrot<10:
    parrot_last = parrot
elif parrot>9:
    parrot_last = parrot%10
match parrot_last:
    case 1:
        print(f'{parrot} попугай')
    case 2,3,4:
        print(f'{parrot} попугая')
    case _:
        print(f'{parrot} попугаев')

#5th
import math
mass = int(input())*0.453592
leg = int(input())*0.0254
ixmb = math.ceil((mass/(leg**2))*100)/100
if ixmb<16:
    print('выраженный дефицит массы тела')
elif ixmb<18.5:
    print('Недостаточная массы тела')
elif ixmb<25:
    print('норма')
elif ixmb<30:
    print('исбыточная масса тела')
elif ixmb<35:
    print('ожирение первой степени')
elif ixmb<40:
    print('ожирение второй степени')
else:
    print('ожирение третьей степени')

#6th
dayone = int(input())
daytwo = int(input())
daythree = int(input())
st = {dayone, daytwo, daythree}
match len(st):
    case 1:
        print(3)
    case 2:
        print(2)
    case 3:
        print(0)

#7th
N = int(input())
K = int(input())
M = int(input())
fst_var = abs(M-K-1)
if fst_var>N//2:
    print(N-fst_var)
else:
    print(fst_var)

#8th
kn = int(input())
gln = kn//(17*29)
skl = kn//29-gln*17
kn = kn-(gln*17*29)-skl
if kn == 0:
    print(f'{gln} галлеон \n{skl} сиклей')
elif kn == 0 and skl == 0:
    print(f'{gln} геллеон')
elif skl == 0:
    print(f'{gln} галеон,\n{kn} кнатов')
else:
    print(f'{gln} галеон,\n{skl} сикелей,\n{kn} кнатов')

#9th
hight = list(map(int, input().split()))
print(hight)

for i in range(0, 3):
    if max(hight) == hight[i]:
        ix_max = i

for i in range(0, 3):
    if min(hight) == hight[i]:
        ix_min = i

for i in range(0,3):
    if i != ix_min and i!= ix_max:
        ix_mid = i
print(hight[ix_min], hight[ix_mid], hight[ix_max])

#10th
pin = input()
error_count = 0
if len(pin)>4:
    error_count+=1

match_l = 0
for i in pin:
    for k in pin:
        if k == i:
            match_l +=1
if match_l >4:
    error_count+=1

for i in range(1900, 2051):
    if i == int(pin):
        error_count+=1

if int(pin[0]) == int(pin[1])+1 == int(pin[2])+2 == int(pin[3])+3:
    error_count +=1

if int(pin[0]) == int(pin[1])-1 == int(pin[2])-2 == int(pin[3])-3:
    error_count +=1


if error_count != 0:
    print('ERROR')
else:
    print('OK')