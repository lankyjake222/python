stopwords = set(("my", "name", "is", "I", "am", "called", "hello"))


response = raw_input("What is your name ? ")
print("Hello " + response)
seperate = response.split()
for word in seperate:
    if word in stopwords:
        seperate.remove(word)     



age = raw_input("How old are you ? ")
if (age >= 18):
    print("Fancy a pint ?")
elif(age < 18):
    print("Lemonade I'm afraid !")
print(age)
    
raw_input("What course are you doing? ")
print(" Sounds interesting! ")
