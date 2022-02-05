print("형이 지금 당장 죽을 확률은? 0.0041758%.나로 인해 그 확률에 도달하게 될 확률은? 95%. 그게 니가 지금 당장 죽을 확률이야. 나는 5%를 쥐고 있고. 그 5% 마저 먹었지. 상호확증파괴? 아니. 이젠 맞아. 흠 생각해보니까 형이 지금 당장 죽을 확률은 0.0041758%가 맞는거 같군. 휴전? 콜.")

a=int(input())
b=[]
for i in range(a):
    d=int(input())
    b.append(d)
b.sort()
c=b[-1]
e=0
f=[]
for i in range(a):
    g = (b[e] / c) * 100
    f.append(g)
    e=e+1
h=sum(f)
i=h/a
print(i)
