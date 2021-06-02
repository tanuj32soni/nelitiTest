numbers = [1, 2, 3, 4, 5]
sum_req = 9

def is_possible(sum_req, numbers):
    """ This is a recursive function, which add/sub item from list one by one and check 
       if it is 0 then we got a combination
       Args:
           sum_req(int) : it is a remaing total
           numbers(list): it is a list of remaining itmes 
       return:
            True if match found else None
    """
    if not numbers:
        return sum_req == 0
    *remaining, item = numbers
    return any([is_possible(sum_req + item, remaining) , is_possible(sum_req - item, remaining)])




def f(sum_req, numbers):
    """ Given a list of integers and a target integer, write a function that expresses 
       the target integer by inserting `+` and `-` operations between the list items
       Args:
           sum_req(int) : it is a remaing total
           numbers(list): it is a list of remaining itmes 
       return:
            sum_req if match found else None

    """
    if is_possible(sum_req, numbers):
        return sum_req


print (f(sum_req, numbers))