#Define function that takes in a string
def Palindrome(s):
    #compare string to reversed string
    if s == s[::-1]:
        return True
    else:
        return False
#set the start of 3 digit integers
i = 100
j = 100
#set greatest to 0
greatest = 0
#first factor of three digit number
while (i <= 999):
    #second factor of three digit number
    while (j <= 999):
        #multiplying the numbers
        product = i * j
        if (product > greatest and Palindrome(str(product))):
            greatest = product
        j += 1
    j = 100
    i += 1
print("Answer:" + str(greatest))
