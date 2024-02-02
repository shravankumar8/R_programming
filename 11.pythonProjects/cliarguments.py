#  used to process the command line arguments
# two types of arguments 
# 1)positional arguments
# 2)optional arguments
import argparse
def arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument("number1",help="first number")
    parser.add_argument("number2",help="second number")
    parser.add_argument("operation",help="operation")
    args=parser.parse_args()
    args.number1=int(args.number1)
    args.number2=int(args.number2)
    if args.operation =="add":
        print("the addition of ",args.number1,"and",args.number2 ,"=",args.number1+args.number2)
    elif args.operation =="mul":
        print("the multiplication  of ",args.number1,"and",args.number2 ,"=",args.number1*args.number2)
        
    elif args.operation =="sub":
        print("the subtraction  of ",args.number1,"and",args.number2 ,"=",args.number1-args.number2)
        
    elif args.operation =="div":
        print("the division  of ",args.number1,"and",args.number2 ,"=",args.number1/args.number2)
        
     




arguments()    