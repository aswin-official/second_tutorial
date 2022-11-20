def main():
    x = int(input("what is X: "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n % 2 ==0:
        return True

    else:
        return False    
main()                   