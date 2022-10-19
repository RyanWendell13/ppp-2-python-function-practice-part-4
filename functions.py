def max_num(*args):
    max = 0
    for n in args:
        if n > 0:
            max = n
    return max

print(max_num(9,20,13))


def mult_list(listOfNums):
    total = 1
    for n in listOfNums:
        total *= n
    return total

print(mult_list([5,2,9,6]))

def rev_string(text):
    if len(text) > 1:
        return rev_string(text[1:])+text[0]
    else: 
        return text[0]

print(rev_string("hello"))

def num_within(num, start, end):
    return (num >= start & num <= end)
    

