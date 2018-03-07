#!/usr/bin/env python3
import operator
# import requests

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}
def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    # param = {
    #     "jsonrpc": "2.0",
    #     "method": "generateIntegers",
    #     "params": {
    #         "apiKey": "ea3725d4-270b-4f2d-83ab-9d80e30aac81",
    #         "n": 2,
    #         "min": 0,
    #         "max": 100,
    #         "replacement": True
    #     },
    #     "id": 3405130
    # }
    # r = requests.post('https://api.random.org/json-rpc/1/invoke', json=param)
    # print "Your random numbers for today are ", json.loads(r.text)['result']['random']['data']
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

    # print("hi1")
    # print("hi2")
    # print("hi3")
    # a = 2 * 2
    # print(a)

if __name__ == '__main__':
    main()