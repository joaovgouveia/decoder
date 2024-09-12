import decoders.alphabetic_shifts

def handle_command(line, content):
    if line == "exit": exit()
    return run(format_command(line, content))

def format_command(line, content):
    args = line.split()
    return {"cmd": args.pop(0), "args": args, "content": content}

def run(cmd):
    
    return commands[cmd["cmd"]](cmd["args"],cmd["content"])
    

# commands
commands = {
    "invert_alphabet": decoders.alphabetic_shifts.inverted_alphabet,
    "shift": decoders.alphabetic_shifts.shift_by,
    "shift_all": decoders.alphabetic_shifts.shift_all
}