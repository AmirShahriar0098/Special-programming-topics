# help("keywords")
import math
import os


# Clear function for pages cleaner
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


# Validation for move between 'Pages'
def Validation(f, e, d, i):
    while True:
        if i == f:
            clear()
            print(
                "\t\t\t***********************************************Welcome"
                "***********************************************")
            return 'f'
        elif i == e:
            clear()
            print(
                "\t\t\t***********************************************goodbye"
                "***********************************************")
            return 'e'
        else:
            print("\n\t\t\t\t\t\t\t Please enter a Valid Value\n")
            i = input(d)


# Main list
def MainList():
    print("\t\t\t\t\tPlease enter your favorite environment for visit : \n\n\t\t\t\t\t1. String 'S' : \n\t\t\t\t\t2. "
          "Function 'F' : \n\t\t\t\t\t3. Casting 'C' : \n\t\t\t\t\t4. Type 'T' : \n\t\t\t\t\t5. Range 'R' : "
          "\n\t\t\t\t\t6. List 'L' : ")
    Enter = input('\n\t\t\t\t\tYour choose : ')

    while True:
        match Enter.upper():
            case 'F':
                clear()
                Function()
                return 'f'
            case 'S':
                clear()
                String()
                return 's'
            case 'C':
                clear()
                Casting(input("Enter your value : "), input("\nEnter your data type 'S' String, 'I' Int, 'F' Float : "))
                return 'c'
            case 'T':
                clear()
                Type(input("Enter your value : "))
                return 't'
            case 'R':
                clear()
                Range(input('\nEnter start step : '), input('\nEnter end step : '), input('\nEnter jump step : '))
                return 'r'
            case 'L':
                clear()
                List()
                return 'l'
            case _:
                print("\n\t\t\t\t\t\t\t Please enter a Valid Value\n")
                Enter = input('\t\t\t\t\tYour choose : ')


def insI(a):
    return int(input(f"\n\t\t\t{a}"))


def insS(a):
    return input(f"\n\t\t\t{a}")


def Function():
    print("\n\t\t\tSigmoid 'sigmoid' : ")
    print("\n\t\t\tTanh 'tanh' : ")
    print("\n\t\t\tP 'p' : ")
    print("\n\t\t\tN 'n' : ")
    print("\n\t\t\tFibonacci 'fib' : ")
    print("\n\t\t\tD1 'd1' : ")
    print("\n\t\t\tY 'y' : ")
    print("\n\t\t\tGhar Motlagh 'gm' : ")
    print("\n\t\t\tD2 'd2' : ")
    print("\n\t\t\tL 'l' : ")
    print("\n\t\t\tL1 'l1' : ")
    print("\n\t\t\tFactorial 'fact' : ")
    print("\n\t\t\tD 'd' : ")
    print("\n\t\t\tInclude Y, Z, X1 'yzx' : ")
    print("\n\t\t\tT 't' : ")
    print("\n\t\t\tIf input 0 Increase it to 10 ' if 10' : ")
    print("\n\t\t\tCount Number of Iteration a char in a string 'iteration number' : ")
    print("\n\t\t\tCheck for ISexist a char in a string 'isexist' : ")
    print("\n\t\t\tSimilar 'similar' : ")
    print("\n\t\t\tAnonymous 'anonymous' : ")
    print("\n\t\t\tSeperator ' seperator' : ")
    FunctionMethods(input("\n\t\t\tPlease enter your favorite Function for visit : "))


def FunctionMethods(a):
    match a.lower():
        case 'sigmoid':
            input1 = insI("Enter a number : ")

            def sigmoid(z):
                print(1 / (1 + math.exp(-z)))

            sigmoid(input1)
        case 'tanh':
            input1 = insI("Enter a number : ")

            def tanh(z):
                print((math.exp(-z) - math.exp(z)) / (math.exp(-z) + math.exp(z)))

            tanh(input1)
        case 'p':
            input1 = insI("Enter a number : ")
            input2 = insI("Enter a number : ")
            input3 = insI("Enter a number : ")

            def sPart(x, y):
                result = math.sqrt(x ** 2 + y ** 2)
                return result

            def pPart(x, y, z):
                s = sPart(x, y)

                if s < 0:
                    s = -s
                else:
                    s = s
                print(s * math.cos(z))

            pPart(input1, input2, input3)
        case 'n':
            input1 = insI("Enter a number : ")
            input2 = insI("Enter a number : ")
            input3 = insI("Enter a number : ")

            def nPart(s, m, x):
                # Before math.exp
                a = s * math.sqrt(2 * math.pi)
                t = 1 / a

                # Math.exp
                o = (x - m) ** 2
                k = 2 * (s ** 2)

                c = -(o / k)
                r = math.exp(c)

                # After Math.exp
                all = t * r
                print(all)

            nPart(input1, input2, input3)
        case 'fib':
            input1 = insI("Enter a number : ")

            def Fibonacci(x):
                if x <= 0:
                    print("Incorrect input")
                elif x == 1:
                    return 0
                elif x == 2:
                    return 1
                else:
                    return Fibonacci(x - 1) + Fibonacci(x - 2)

            print(Fibonacci(input1))
        case 'd1':
            input1 = insI("Enter a number : ")
            input2 = insI("Enter a number : ")
            input3 = insI("Enter a number : ")
            input4 = insI("Enter a number : ")

            def D1Part(x1, x2, y1, y2):
                print(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))

            D1Part(input1, input2, input3, input4)
        case 'y':
            input1 = insI("Enter a number : ")
            input2 = insI("Enter a number : ")

            def Ypart(x, y):
                print((x + y / x) / 2)

            Ypart(input1, input2)
        case 'gm':
            input1 = insI("Enter a number : ")

            def GadrMotlagh(z):
                if z >= 0:
                    print(z)
                else:
                    print(-z)

            GadrMotlagh(input1)
        case 'd2':
            input1 = insI("Enter a number : ")
            input2 = insI("Enter a number : ")
            input3 = insI("Enter a number : ")
            input4 = insI("Enter a number : ")

            def D2Part(x1, x2, y1, y2):
                z = (x1 - x2) + (y1 - y2)

                print(GadrMotlagh(z))

            D2Part(input1, input2, input3, input4)
        case 'l':
            input1 = insI("Enter a number : ")
            input2 = insI("Enter a number : ")
            input3 = insI("Enter a number : ")
            input4 = insI("Enter a number : ")
            input5 = insI("Enter a number : ")

            def lPart(h1, h2, m, x, y):
                a = (((h1 * x) + y) + ((h2 * x) + y))
                print(1 / m * a)

            lPart(input1, input2, input3, input4, input5)
        case 'l1':
            input1 = insI("Enter a number : ")
            input2 = insI("Enter a number : ")
            input3 = insI("Enter a number : ")
            input4 = insI("Enter a number : ")

            def L1Part(h, x, y, m):
                a = ((h * x) - y) * x
                print(1 / m * a)

            L1Part(input1, input2, input3, input4)
        case 'fact':
            input1 = insI("Enter a number : ")

            def Factoril(x):
                if x <= 1:
                    return x
                return x * Factoril(x - 1)

            print(Factoril(input1))
        case 'd':
            input1 = insI("Enter a number : ")
            input2 = insI("Enter a number : ")

            def dPart1(h, t):
                return -(h / t * math.log(h / t))

            def dPart2(h, t):
                print(h / t * dPart1(h, t))

            dPart2(input1, input2)
        case 'yzx':
            input1 = insI("Enter a number : ")
            input2 = insI("Enter a number : ")
            input3 = insI("Enter a number : ")
            input4 = insI("Enter a number : ")
            input5 = insI("Enter a number : ")

            def SecondY(w, x, b):
                print(w * x + b)

            def zPart(w, x, b):
                d = SecondY(w, x, b)
                print(1 / (1 + math.exp(-d)))

            def X1Part(x0, a, w, x, b):
                print(x0 + a * zPart(w, x, b))

            X1Part(input1, input2, input3, input4, input5)
        case 't':
            input1 = insI("Enter a number : ")
            input2 = insI("Enter a number : ")
            input3 = insI("Enter a number : ")

            def tPart(b, v, c):
                print(b * math.sqrt(1 - (v ** 2 / c ** 2)))

            tPart(input1, input2, input3)
        case 'if 10':
            input1 = insI("Enter a number : ")

            def CheckZero(n):
                if n == 0:
                    while n < 10:
                        n += 1
                print(n)

            CheckZero(input1)
        case 'iteration number':
            input1 = insS("Enter a String value : ")
            input2 = insS("Enter a char value : ")

            def count(a, b):
                i, x = 0, 0
                while i < len(a):
                    if a[i] == b:
                        x += 1
                    i += 1
                print(x)

            count(input1, input2)
        case 'isexist':
            input1 = insS("Enter a String value : ")
            input2 = insS("Enter a char value : ")

            def find(a, b):
                i = 0
                while i < len(a):
                    if a[i] == b:
                        print(f"{b} in index : ")
                        print(i)
                    i += 1
                print("Not exist")

            find(input1, input2)
        case 'similar':
            input1 = insS("Enter a String value : ")
            input2 = insS("Enter a String value : ")

            def Similar2(a, b):
                for i in a:
                    for j in b:
                        if i == j:
                            print(i)

            Similar2(input1, input2)
        case 'anonymous':
            input1 = insI("Enter a number : ")

            def Anonymous(x):
                while x != 1:
                    if x % 2 == 0:
                        print(x)
                        x /= 2
                    else:
                        x = x * 3 + 1

            Anonymous(input1)
        case 'seperator':
            def Seperator(a):
                u, l, d = "", "", ""

                for i in a:
                    if i.isalpha():
                        if i.isupper():
                            u += i
                        else:
                            l += i
                    else:
                        d += i
                print("Uppers : " + u + ", lowers : " + l + ", Digits : " + d)

            Seperator("abcaAXY235")
        case _:
            print("\n\t\t\t\t\t\t\t Please enter a Valid Value\n")


def List():
    print("\n\t\t\tReverse a list 'R' : ")
    print("\n\t\t\tSort a list from up to down 'S' : ")
    ListMethods(input("\n\t\t\tPlease enter your favorite environment for visit : "))


def ListMethods(public):
    match public.upper():
        case 'R':
            list, list1 = [], []
            i = input("\n\t\t\tEnter a value for a list \"Pay Attention for ended of your list enter '-1'\" : ")
            while i != "-1":
                list.append(i)
                i = input("\n\t\t\tEnter a value for a list \"Pay Attention for ended of your list enter '-1'\" : ")
            f = len(list) - 1
            while f >= 0:
                list1.append(list[f])
                f = f - 1
            print("\n\t\t\t", list1)
        case 'S':
            list = []
            i = input("\n\t\t\tEnter a value for a list \"Pay Attention for ended of your list enter '-1'\" : ")
            while i != "-1":
                list.append(i)
                i = input("\n\t\t\tEnter a value for a list \"Pay Attention for ended of your list enter '-1'\" : ")
            for i in range(len(list)):
                for j in range(i + 1, len(list)):
                    if list[i] <= list[j]:
                        list[i], list[j] = list[j], list[i]
            print("\n\t\t\t", list)


def String():
    print("\n\t\t\tLen() 'LEN' : ")
    print("\n\t\t\tSlicing 'S' : ")
    print("\n\t\t\tTraversing 'T' : ")
    print("\n\t\t\tIsAlpha() 'A' : ")
    print("\n\t\t\tIsUpper() 'P' : ")
    print("\n\t\t\tIsLower() 'O' : ")
    print("\n\t\t\tLower() 'L' : ")
    print("\n\t\t\tUpper() 'U' : ")
    print("\n\t\t\tReverse a string() 'R' : ")
    StringMethods(input("\n\t\t\tPlease enter your favorite environment for visit : "))


def StringMethods(a):
    print("\n\n\t\t\t***Please enter a 'String' value***\n\n")
    public = input("\t\t\tEnter your value : ")
    match a.upper():
        case 'LEN':
            print("\t\t\t", len(public))
        case 'S':
            sStep = input('\n\t\t\tEnter start step : ')
            eStep = input('\n\t\t\tEnter end step : ')
            jStep = input('\n\t\t\tEnter jump step : ')
            if sStep.isdigit() and eStep.isdigit() and jStep.isdigit():
                print("\t\t\t", public[int(float(sStep)): int(float(eStep)): int(float(jStep))])
            else:
                print("\n\t\t\t\t\t\t\t Please enter a Valid Value\n")
        case 'T':
            for i in public:
                print("\t\t\t", i)
        case 'A':
            print("\t\t\t", public.isalpha())
        case 'P':
            print("\t\t\t", public.isupper())
        case 'O':
            print("\t\t\t", public.islower())
        case 'L':
            print("\t\t\t", public.lower())
        case 'U':
            print("\t\t\t", public.upper())
        case 'R':
            print("\t\t\t", public[::-1])
        case _:
            print("\n\t\t\t\t\t\t\t Please enter a Valid Value\n")


def Range(a, b, c):
    if a.isdigit() and b.isdigit() and c.isdigit():
        for i in range(int(float(a)), int(float(b)), int(float(c))):
            print(i)
    else:
        print("\n\t\t\t\t\t\t\t Please enter a Valid Value\n")


def Type(a):
    if a.isalpha():
        print(type(a))
    elif a.isdigit():
        print(type(int(a)))
    else:
        print(type(float(a)))


def Casting(a, b):
    if b.upper() == 'S':
        print(f"Your casting for '{b}' to a String Datatype is : {str(a)}")
    elif b.upper() == 'I':
        print(f"Your casting for '{b}' to a Int Datatype is : {int(float(a))}")
    elif b.upper() == 'F':
        print(f"Your casting for '{b}' to a Float Datatype is : {float(a)}")
    else:
        print("\n\t\t\t\t\t\t\t Please enter a Valid Value\n")


# ----------------------------------------------------------------------------------------------------------------------------------------

# intro of program for visitors
print('\n\t\t\t\t\t\t\t      **Welcome to our program**\n')
print('----------------------------------------------------------------List of Python '
      'services---------------------------------------------------------------------')
print("Author : Amirhossein Shahriarpanah\t\t\t\t\t\t\t\t\t\t\t\t\tMaster : MR.Dehghan\n")
print("    'Hello bro'\n")
print("    This program provides you with a list of all the things that a Python program can\
 do in MR.Dehghan's training classes.\n")
print("    you can select each one you like it then go to a part of program; for example:\n\n\t you go to the \'String\
 part\'; in this section you can use 'slicing', 'range' and etc.\n")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("    if you like this program e \'f\' to com in and enjoy more or otherwise enter \'e\' to exit.\n")

# Validate
Enter = input("\t\t\t\t\t\t\t\tyour choose:")
Enter = Validation('f', 'e', '\t\t\t\t\t\t\t\tyour choose:', Enter)

# Body
while Enter == 'f':
    MainList()

    # Ask for do again
    # clear()
    Enter = input('\t\t\t\t\tWould you like do this progress again?     "f" YES,     "e" NO :')
    Enter = Validation('f', 'e', '\t\t\t\t\tWould you like do this progress again?     "f" YES,     "e" NO :', Enter)
