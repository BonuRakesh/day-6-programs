
def factorial(n):

	return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

num = int(input("Enter the number"))
print ("Factorial of", num, "is",
	factorial(num))

def printDivisors(n) :
	i = 1
	while i <= n :
		if (n % i==0) :
			print (i,end=" ")
		i = i + 1

print ("The factors of the number are : ")
printDivisors(num)




