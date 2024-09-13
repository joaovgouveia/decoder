def binary_to_ascii(_, line):
    return "".join(list(map(binary_to_ascii_char, line.split())))

def binary_to_ascii_char(seq):
    return chr(int(seq, 2))