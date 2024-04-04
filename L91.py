#The author's name is Sydney Eidelbes

numbers={"one":1,"two":2,"three":3}
def my_get_method(dictionary,key):
    if key in dictionary:
        print(dictionary[key])

my_get_method(numbers,"one")
    
