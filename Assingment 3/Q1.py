def diamond(n):
    def diamondup(n,gap=0):
        if n==0:
            return

        print(f"{" * "*n}{"   "*gap}{" * "*n}")
        gap+=2
        diamondup(n-1,gap)


    def diamonddn(n,gap=-2):
        if n==1:
            return
        gap+=2
        diamonddn(n-1,gap)
        print(f"{" * "*n}{"   "*gap}{" * "*n}")

    diamondup(n)
    diamonddn(n)

n=int(input("enter the value of n : "))
diamond(n)