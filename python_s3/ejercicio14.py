def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = "Murcielago"
vowel_count = count_vowels(text)
print(f"La cadena '{text}' tiene {vowel_count} vocales.")
