


mySentence = ' loves the color'



color_list = ['red','blue','green','pink','teal','black']

def color_function(name):
    lst = []
    for i in color_list:
       msg = "{0} {1} {2}".format(name,mySentence,i)
       lst.append(msg)
    return lst



print(color_function('Sally'))
for i in lst:
    print(i)


def get_name():
    go = True
    while go:
        name = input('what is your name? ')
        if name == '':
            print("You need to provide your name")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()
