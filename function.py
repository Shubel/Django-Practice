# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()


### using function between two number addition
def add(x, y):
    sum = x + y
    print(sum)
    
add(10, 20)


### using function between three number addition
def addition(x, y, z):
    sum = x + y + z
    print(sum)
    
addition(10, 30, 40)