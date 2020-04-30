def my_name(my_name):

    return "My name is " + my_name

def calc_average(*marks):
    """
    This function returns the
    average of marks given in
    the marks tuple.
    """
    return sum(marks) / len(marks)

my_name("Mischa")

print(my_name("Mischa"))
print(calc_average(1,2,3))