s=int(input())

sec=min(s,100000)

horas= int(sec/3600)

b = sec%3600

minu = int(b/60)

a= b%60

sec = int(a)

print(horas,minu,sec, sep=":")