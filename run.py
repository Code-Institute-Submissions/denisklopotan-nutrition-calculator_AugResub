print("**************************************************************************************") # 86*
print("Welcome user! This simple 'Nutrition Calculator' helps you add calories and nutritional values of food and returns total sum.\n")
print("You can enter multiple articles of food, one after another. They will be simply called 'Article 1', 'Article 2', etc..\n")
print("Enter only round number values or zero (0) of following: energy in calories (cal); fat, carbohydrate and protein content in grams (g).\n")
print("To exit the calculator you can press 'Control + C'. And...dont forget to smile! Its healthy and burns calories too! :D\n")
print("**************************************************************************************") # 86*

def article1():
    
    print("\nArticle 1:\n")
    while True:
        try:
            x = int(input("Enter calories: "))
            y = int(input("How much fat? "))
            z = int(input("Carbohydrates? "))
            w = int(input("And protein? "))
        except ValueError:
            print("This is not a round number! Please provide correct value")
            continue
        else:
            break
    
    article1.variable = [x, y, z, w]

article1()

def article2():
    
    print("\nArticle 2:\n")
    while True:
        try:
            x = int(input("Enter calories: "))
            y = int(input("How much fat? "))
            z = int(input("Carbohydrates? "))
            w = int(input("And protein? "))
        except ValueError:
            print("This is not a number! Please provide correct value")
            continue
        else:
            break
    
    article2.variable = [x, y, z, w]

article2()

result = zip(article1.variable, article2.variable)
sum = [x + y for (x, y) in result]
print(f'\nCalories: {sum[0]}, Fat: {sum[1]}g, Carbohydrates: {sum[2]}g, Protein: {sum[3]}g')