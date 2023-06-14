# Opdracht 1
n! / r!(n-r)!
r = 12
n = 20

20! / 12!(20-12)! = 775,200

# opdracht 2
n^r
r = 20
n = 4

4^20

# opdracht 3

(r+n-1)! / r!(n-1)!
r = 25
n = 3

27!/(25!2!)

# opdracht 4
n! / r!(n-r)!
r = 30
n = 110
110! / (30!(110-30)!) = 110! / (30!80!)

r = 31
n = 110
110! / (31!(110-31)!) = 110! / (31!79!)

r = 32
n = 110
110! / (32!(110-32)!) = 110! / (32!78!)

110! / (30!80!) + 110! / (31!79!) + 110! / (32!78!)

# opdracht 5
n! / r!(n-r)!
r = 7
n = 26

26! / (7!(26-7)!) = 26! / (7!19!)

# opdracht 6

sum = 0
for r in range(0, 31, 1):
    element = (factorial(45)/(factorial((45-r)) * factorial(r))) * ((factorial((45-r)+(2-1)) / factorial(r) * factorial(2-1)))
    sum += element
print(sum)

1.2353421086674186e+58

1.2353421086674186e+58

# opdracht 7

1 traject:
volgorde traject: belangrijk
repetition traject: belangrijk
n^r
r = gem lengte (6)
n = gem opties (4)
= 4096

meerdere trajecten(1 lijnvoering):
volgorde: niet belangrijk
repetition: niet belangrijk
n!/(r!(n-r)!)
r = aantal trajecten (7)
n = een traject (4096)

statespace = 7,87*10^28

niet gemiddelde, max lengte traject. Herhaling belangrijk.


