# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:46:33 2024

@author: danie
"""

# This code thinks raise is the best first word in the 2310 list and tares in the 5757 list.

from itertools import product
from collections import defaultdict

fh = open('wordlewordslist.txt','r')

lines = fh.readlines()


def filter_words(word_list, guess, colors):

    """Filter the word list based on feedback from the guess.
    
    Args:
        word_list (list of str): The current list of possible words.
        guess (str): The guessed word.
        colors (list of str): List of colors ('green', 'yellow', 'gray') for each letter in the guess.
    
    Returns:
        list of str: Filtered list of possible words.
    """

    new_list = []
    
    for word in word_list:
        match = True
        for i, (g_letter, color) in enumerate(zip(guess, colors)):
            if color == 'g' and word[i] != g_letter:
                match = False
                break
            elif color == 'y':
                if g_letter not in word or word[i] == g_letter:
                    match = False
                    break
            elif color == 'n' and g_letter in word:
                match = False
                break
        if match:
            new_list.append(word)
    
    return new_list

def calculate_average_elimination(words):
    """
    Determines the word that maximizes elimination of remaining words on average.
    """
    best_word = None
    best_avg_remaining = float('inf')  # Start with infinity for minimization
    #print(words)
    
    for guess in words:
        #print(guess)
        
        remaining_counts = []
        print(guess)
        # Generate all color patterns (gray, yellow, green) for 5 letters
        all_patterns = product(["n", "y", "g"], repeat=5)
        # Calculate remaining words for each color pattern
        
        for pattern in all_patterns:


        
            filtered = filter_words(words, guess, pattern)
            if len(filtered) == 0:
                continue
            #if guess == 'adorn\n' or guess == 'apron\n':
            #    print("\033[31m"+" ".join(word.strip() for word in words)+"\033[0m")
            #    print("\033[32m"+" ".join(pattern)+"\033[0m")
            #    print("\033[33m"+" ".join(rem.strip() for rem in filtered)+"\033[0m")
            
            remaining_counts.append(len(filtered))


            
        
            # Calculate average remaining count for this guess
        #print(remaining_counts)
        avg_remaining = sum(count**2 for count in remaining_counts) / sum(remaining_counts)
        #print(words)  
        print(avg_remaining)

            # Update best word if it has a lower average remaining count
        if avg_remaining < best_avg_remaining:
            best_avg_remaining = avg_remaining
            best_word = guess


    

    return best_word, best_avg_remaining

# Main program loop
possible_words = lines[:]
print("This code thinks that raise(2310)/tares(5757) is the best first word.")
while True:
    #best_guess, avg_remaining = calculate_average_elimination(possible_words)
    #print(f"Best word to guess: {best_guess}, with average words remaining: {avg_remaining:.2f}")
    
    
    guess = input("Enter your guessed word: ").strip().lower()
    colors = input("Enter the colors for each letter (e.g., 'g g y n g'): ").split()
    
    # Check for valid input length
    if len(guess) != 5 or len(colors) != 5:
        print("Error: Guess and color pattern should be exactly 5 letters long. Try again.")
        continue

    # Filter possible words based on feedback
    possible_words = filter_words(possible_words, guess, colors)
    
    print(f"\nPossible words remaining: {len(possible_words)}")
    if possible_words:
        print(" ".join(possible_words))
    else:
        print("No possible words match your criteria.")
        break

    best_guess, avg_remaining = calculate_average_elimination(possible_words)
    print(f"Best word to guess: {best_guess}, with average words remaining: {avg_remaining:.2f}")



