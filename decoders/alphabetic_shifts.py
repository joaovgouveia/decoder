def inverted_alphabet(_, line):
    return "".join(list(map(invert_char, line)))

def shift_by(args, line):
    n = int(args.pop(0))
    return "".join(list(map(lambda c : shift_char_by(n, c), line)))

def shift_all(_, line):
    return "".join(list(map(lambda n : f"{shift_by([n], line)}\n", range(1, 26)))).strip()


# Char conversion functions
def invert_char(c):
    if c == " ": return " "
    if not c.isalpha: return c
    return chr((155 - (ord(c)))) if c.isupper() else chr((219 - (ord(c))))

def shift_char_by(n, c):
    if c == " ": return " "
    if not c.isalpha: return c
    return chr(((ord(c) - 65 + n) % 26) + 65) if c.isupper() else chr(((ord(c) - 97 + n) % 26) + 97)