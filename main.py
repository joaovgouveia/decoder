import command_handler as cmd
import utils.io as io

def main():
    while True:
        io.output(cmd.handle_command(io.get_input("Command: "), io.get_input("> ")))

if __name__ == "__main__":
    main()