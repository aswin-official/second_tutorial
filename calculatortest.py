def main():
    x = int(input("enter the value"))
    print("The square of entered value is", square(x))

def square(n):
    return n * n

if __name__=="__main__":
    main()