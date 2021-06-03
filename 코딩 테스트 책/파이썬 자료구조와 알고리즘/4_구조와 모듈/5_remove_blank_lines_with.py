import sys


def read_data(filename):
    lines = []
    with open(filename)  as fh :
        for line in fh:
            if line.strip():
                lines.append(line)
    return lines

def write_data(lines, filename):
    fh = None
    with open(filename, "w") as fh:
        for line in lines:
            fh.write(line)


def remove_blank_lines():
    if len(sys.argv) <2 :
        print("Usage: python {0} [file...]".format(sys.argv[0]))
    for filename in sys.argv[1:]:
        lines = read_data(filename)
        if lines:
            write_data(lines, filename)


remove_blank_lines()