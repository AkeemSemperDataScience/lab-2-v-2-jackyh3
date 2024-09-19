def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise

    # palindrome = same backwards as forward like racecar

    # make temp string
    temp = ""
    # iterate backwards through parameter and concatenate each char
    # start at end, backwards by 1 until the end
    for i in range(len(word) - 1, -1, -1):
        # print(f'index: {i}\n char: {word[i]}')
        temp += word[i]
        
    # compare
    if temp == word:
        return True
    else:
        return False

# tests
# q1_corr_1 = False
# q1_corr_2 = True
# q1_corr_3 = False
# print("Q1.1: ", lab2Question1("racecar"), "Correct: ", True)
# print("Q1.2: ", lab2Question1("purple"), "Correct: ", q1_corr_1)
# print("Q1.3: ", lab2Question1("ada"), "Correct: ", q1_corr_2)
# print("Q1.4: ", lab2Question1("purple"), "Correct: ", q1_corr_3)


def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    # fibonacci sequence: for n > 2, Fn is sum of Fn-1 + Fn-2 from the sequence, where Fn = 0, Fn = 1
    fibList = []
    fibNum1 = 0
    fibNum2 = 1
    for i in range(number_val + 1):
        if i == 0:
            # case for n = 0
            fibNum3 = 0
        elif i == 1:
            # case for n = 1
            fibNum3 = 1
        else:
            # print(f"i: {i}, fib1 = {fibNum1}, fib2 = {fibNum2}, fib3 = {fibNum3}\n\n")
            fibNum3 = fibNum1 + fibNum2
            fibNum1 = fibNum2
            fibNum2 = fibNum3
        fibList.append(fibNum3)
    return fibList

# tests, seem to be wrong inputs to answers? 
# q2_corr_1 = [0, 1, 1, 2, 3, 5] #fib(5)
# q2_corr_2 = [0, 1, 1, 2, 3, 5, 8] #fib(6)
# q2_corr_3 = [] #fib(-'ve)
# print("Q2.1: ", lab2Question2(7), "Correct: ", q2_corr_1) 
# print("Q2.2: ", lab2Question2(12), "Correct: ", q2_corr_2)
# print("Q2.3: ", lab2Question2(-5), "Correct: ", q2_corr_3)


def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.

    # could traverse index by index until finds first match, then traverse until all matched...
    # or use find function + in 

    # based off the test cases, it is NOT case sensitive
    str1Lower = str1.lower()
    str2Lower = str2.lower()
    # initialize count
    occurrence = 0
    # check if str2 is in str1
    if str2Lower in str1Lower:
        index = 0
        while index < len(str1Lower):
            # find next occurrence, increment, until reached the end of string
            index = str1Lower.find(str2Lower, index)
            
            # unable to find anymore
            if index == -1:
                break
            occurrence += 1
            # print("index: ", index, "\noccurrence: ", occurrence) 
            # continue to next char
            index += 1
    return occurrence    

#tests
# q3_corr_1 = 2
# q3_corr_2 = 1
# q3_corr_3 = 2
# print("Q3.1: ", lab2Question3("Coding is cool", "co"), "Correct: ", q3_corr_1) # Seems case INSENSITIVE
# print("Q3.2: ", lab2Question3("Attitude is everything", "tt"), "Correct: ", q3_corr_2)
# print("Q3.3: ", lab2Question3("Superstitious and superfluous", "super"), "Correct: ", q3_corr_3)

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    
    #initialize list
    sum_list = []
    try:
        # same length 
        if len(list1) == len(list2):
            for i in range(len(list1)):
                sum = list1[i] + list2[i]
                sum_list.append(sum)
        # else: 
        #     # NOT same length
        #     print("Please supply lists that are the same length")
    except:
        # some other error
        return sum_list
        # print("Error! May be wrong length, or wrong data types in the list. Please provide numbers within the list!")

    return sum_list

#tests
# q4_corr_1 = [6.0, 8.0, 10.0, 12.0]
# q4_corr_2 = []
# q4_corr_3 = [5.0, 7.0, 14.0, 10.0]
# print("Q4.1: ", lab2Question4([1, 2, 3, 4], [5, 6, 7, 8]), "Correct: ", q4_corr_1)
# print("Q4.2: ", lab2Question4([0, 0, 0, 0], [0, 0, 0]), "Correct: ", q4_corr_2)
# print("Q4.3: ", lab2Question4([1, 2, 8, 3], [4, 5, 6, 7]), "Correct: ", q4_corr_3)


def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = None

    # user input???
    while password == None:
        # prompt user
        tempPassword = input('''Enter a password with the following criteria: 
                        \n- At least 8 characters long
                        \n- Contains at least one uppercase letter
                        \n- Contains at least one lowercase letter
                        \n- Contains at least one number\n''')
        if not isValidPassword(tempPassword):
            # password invalid
            print("Invalid password! Try again!")
        else:
            # password valid
            password = tempPassword

    return password

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    LENGTH = 8
    gotUpper = False
    gotLower = False
    gotNum = False

    # check length
    if len(password) >= LENGTH:
        # traverse each character
        for char in password:
            # at least 1 character is uppercase
            if char.isupper():
                gotUpper = True
            # at least 1 character is lowercase
            if char.islower():
                gotLower = True
            # at least 1 character is a digit
            if char.isdigit():
                gotNum = True
        if gotUpper and gotLower and gotNum:
            # all requirements met
            return True
    # 1+ requirement failed
    return False

# lab2Question5()
#tests
# q5_corr_1 = False
# q5_corr_2 = True
# q5_corr_3 = False
# print("Q5.1: ", isValidPassword("password"), "Correct: ", q5_corr_1)
# print("Q5.2: ", isValidPassword("Password1"), "Correct: ", q5_corr_1)
# print("Q5.3: ", isValidPassword("12345678"), "Correct: ", q5_corr_1)

