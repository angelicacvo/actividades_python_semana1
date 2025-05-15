def count_letter(word, letter):

  return word.count(letter)

word = "Python es un lenguaje de programación"
letter = "n"
quantity = count_letter(word, letter)
print(f"La letra '{letter}' aparece {quantity} veces en la palabra '{word}'") 