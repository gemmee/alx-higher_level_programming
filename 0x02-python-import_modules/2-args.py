#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    no_args = len(argv) - 1
    if not no_args:
        end = 's.'
    else:
        end = "{}:".format("s" if no_args > 1 else "")
    print('{:d} argument{}'.format(no_args, end))
    if no_args:
        for i in range(no_args):
            print('{:d}: {}'.format(i+1, argv[i+1]))
