from dibujo import display_hangman

def hangman():
    word = "ahorcado"
    guessed_letters = []
    tries = 6
    
    print("BIENVENIDO A AHORCADO!")
    
    while True:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(display_hangman(tries))
        print(display_word)
        
        if display_word == word:
            print("FELICIDADES! HAS ADIVINADO LA PALABRA.")
            break
        
        guess = input("Adivina una letra: ").lower()
        
        if guess in guessed_letters:
            print("Ya has adivinado esa letra.")
        else:
            guessed_letters.append(guess)
            if guess not in word:
                tries -= 1
                print(f"Supongo que! tienes {tries} intentos.")
                if tries == 0:
                    print("Lo siento, te has quedado sin intentos. La palabra era", word)
                    break
