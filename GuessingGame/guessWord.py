import random
words = ['umbrella', 'computer', 'truck','python', 'mathematics', 'fruit', 'duke', 'jack', 'water', 'bridge', 'rain', 'clay']

guessed_word = random.choice(words)

first_word = input("")

if guessed_word[0] == first_word:
    print("You guessed it right")
    j = 0+1
    while j < len(guessed_word):
        next = input("Next word: ")
        if guessed_word[j] == next:
            j+=1
        
        else:
            print("The next word was wrong")
            break
    if j == len(guessed_word):
        print("Congratulations You Guessed the whole word!")
    
    else:
        print("You lost") 
           
else:
    print("Try again")
 

print("the word was", guessed_word)