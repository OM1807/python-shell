from loop import repl

def main():
    while(True):

        cmd = repl()
        if cmd is None:
            break
        
        if cmd == "":
            continue
        
        print(cmd)

if __name__ == "__main__":
    main()