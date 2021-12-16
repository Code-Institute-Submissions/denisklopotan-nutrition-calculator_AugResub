def article1():
    
    print("Article 1:\n")
    x = int(input("Enter calories: "))
    y = int(input("How much fat? "))
    z = int(input("Carbs? "))
    w = int(input("And protein? "))
    
    article1.variable = [x, y, z, w]

article1()

def article2():
    
    print("\nArticle 2:\n")
    x = int(input("Enter calories: "))
    y = int(input("How much fat? "))
    z = int(input("Carbs? "))
    w = int(input("And protein? "))
    
    article2.variable = [x, y, z, w]

article2()

result = zip(article1.variable, article2.variable)
sum = [x + y for (x, y) in result]
print('\nYour score is as follows:\n\n[calories, fat(g), carbs(g), protein(g)]')
print(sum)