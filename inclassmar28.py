thing=[1]
def one(thing):
    zork=eval(input())
    thing[0]=thing[0]+zork
    return zork
def two(number,zoi):
    number=number*4
    zoi[0]=number*2+zoi[0]
    thing[0]=3
    fun=one(zoi)
    print(number,thing[0],zoi[0])
    return fun+1
def main():
    thing=[2378]
    thing[0],something=eval(input())
    thing[0]=two(something,thing)
    print(thing[0],something)
main()