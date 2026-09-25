


""" def count_words(sentence):
    words = sentence.split()
    return len(words)


x = input("Enter a sentence: ")
word_count = count_words(x)
print(f"Your sentence has {word_count} words.") """



""" def number(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
x = int(input("Enter a number: "))
print(f"Your number is {number(x)}.") """

""" def service(x):
    if x == "good":
        return "20%"
    elif x == "great":
        return "25%"
    elif x == "okay":
        return "15%"
    elif x == "bad":
        return "0%"
x = str(input("How was the service."))
print(f"I will tip {service(x)}") """

def x(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

number = int(input("Enter a number: "))
print(f"Your number is {x(number)}.")



    


        
