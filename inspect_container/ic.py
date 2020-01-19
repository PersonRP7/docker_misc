import subprocess, argparse, sys, os

parser = argparse.ArgumentParser(
    description = "Enter container name."
)

parser.add_argument('-n', type = str, required = True)
args = vars(parser.parse_args())

# Cmd line arg -n signifying the docker container is
# interpolated to the 'command' variable passed to the
# subprocess call.
command = f"docker container inspect {args['n']}"

data = subprocess.run(
    command,
    universal_newlines = True,
    capture_output = True
)

#A generic exception handler. Both functions are run through it.
def exception_handler(function):
    try:
        return function()
    except Exception as e:
        return sys.stderr.write(f"Excepted error:{e}")

def check_empty():
    if len(data.stdout) == 3:
        os.remove(f"{args['n']}.txt")
        sys.stderr.write("Error. Check docker status or container name.")

def write_file():
    with open(f"{args['n']}.txt", "w") as inbound:
        inbound.write(data.stdout)

functions = [
    write_file,
    check_empty
]

def runner():
    for function in functions:
        exception_handler(function)

if __name__ == "__main__":
    runner()
