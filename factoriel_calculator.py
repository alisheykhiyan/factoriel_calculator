# factoriel_calculator.py
n = int(input("Please enter your Intended number :"))
factoriel = 1
for x in range(1,n+1):
   factoriel = factoriel * x
print ("The factoriel of",n,"is",factoriel".")  

