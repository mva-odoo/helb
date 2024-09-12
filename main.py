
# list comprehension
ex_list = [1,2,3,4]
print([i+1 for i in ex_list])


# dict comprehension
ex_dict = {'test': 1, 'tes2':2}
print({i+"_test": a+1 for i,a in ex_dict.items()})


# kwargs & args

def test_simple(a, b, c, d=4):
    return a+b+c+d

print(test_simple(1,2,3))

def test_sum(*args):
    return sum(args)

print(test_sum(1,2,3))


def say_something(**kwargs):
    return kwargs.get('txt')


print(say_something(txt='coucou'))

# lambda
operation = {
    '+': lambda args: sum(args),
}

addition = ['+', 1,2]

print(
    operation.get(addition[0])(addition[1:])
)

# - LAMBDA--------------------(ARGS 1/2)


# nested fonction
def greet(name):
    def display_name():
        print("Hi", name)
    
    display_name()

greet("John")  


# virgule flotante
print(0.1 + 0.1 == 0.2)
print(0.1 + 0.1+ 0.1 == 0.3)


# decorator
def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")
        returned_value = func(*args, **kwargs)
        print("after Execution")
        return returned_value
        
    return inner1


@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

a, b = 1, 2

print("Sum =", sum_two_numbers(a, b))
