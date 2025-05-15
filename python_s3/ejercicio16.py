import re

def validate_password(password):
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[^a-zA-Z0-9]", password):
        return False

    return True

valid_password = "Contraseña123!"
invalid_password = "contraseña123"

print(f"'{valid_password}' es válida: {validate_password(valid_password)}")
print(f"'{invalid_password}' es válida: {validate_password(invalid_password)}")
