def is_palindrome(text):
    text = text.replace(" ", "").replace(",", "").replace(".", "")
    text = text.lower()
    return text == text[::-1]

text = "Anita lava la tina"
if is_palindrome(text):
    print(f"'{text}' es un palíndromo")
else:
    print(f"'{text}' no es un palíndromo")
