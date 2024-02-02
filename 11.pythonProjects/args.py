import argparse
def arg():
    pars=argparse.ArgumentParser()
    pars.add_argument("--number1",help="first number ")
    args=pars.parse_args()
    print(args.number1)
arg()
# adding a -- before the argument initiation ill make it a optional arguments