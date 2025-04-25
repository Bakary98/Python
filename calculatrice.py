# Calculatrice 

# Première version
n1 = input("Veuillez entrer votre premier nombre: ")
n2 = input("Veuillez entrer votre deuxieme nombre")

total = int(n1) + int(n2)

print(f"La somme de {n1} et de {n2} font au total {total}")

# Deuxième version

# Online Python - IDE, Editor, Compiler, Interpreter
n1 = n2 = ""

while not(n1.isdigit() and n2.isdigit()):
   
    n1 = input(" Entrez un premier nombre premier nombre: ")
    n2 = input(" Entrez un deuxieme nombre: ")
    if not(n1.isdigit() and n2.isdigit()):
        print(f"Veuillez entrer deux nombres valides")
else : 
   
   print(f"La somme de {n1} et de {n2} font au total {int(n1) + int(n2)}")
