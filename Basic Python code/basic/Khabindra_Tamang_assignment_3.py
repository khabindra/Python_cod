# 1. Write a program display “Hello World!”.
print("hello world !")

# 2. Write a program to find sum of two numbers. Use input() function to take input from the
# user.
a = int(input("enter the first number: "))
b = int(input("enter the second number : "))
addition = a+b
print(f"the sum of two numbers is: {addition}")


# 3. Write a program to calculate discount on the basis of following assumption:
# a) If purchased amount is greater than or equal to 1000, discount is 5%
def calculate_discount(purchased_account:float)->float:
    if purchased_account >=1000:
        discount = (5/100)*purchased_account
        discounted_amount = purchased_account-discount
        return f'this discount amount is:{discount} and the amount after discount is:{discounted_amount}'
    else: 
        return f'this discount amount is: 0 and the purchased amount:{purchased_account}'



if __name__=='__main__':
    purchased_account = float(input("Enter the purchased amount: "))
    result = calculate_discount(purchased_account)
    print(result)


# 4. Write a program to calculate discount on the basis of following assumption:
# a) If purchased amount is greater than or equal to 1000, discount is 5%
# b) If purchased amount is less than 1000, discount is 3%
purchased_account = int(input("Enter the purchased account: "))

if purchased_account >= 1000:
    discount = 0.05 * purchased_account
    print(f"The discount amount is: {discount}")
else:
    discount = 0.03 * purchased_account
    print(f"The discount amount is: {discount}")


# 5. Write a program to calculate discount on the basis of following assumption:
# a) If purchased amount is greater than or equal to 5000, discount is 10%
# b) If purchased amount is greater than or equal to 4000 and less than 5000, discount is 7%
# c) If purchased amount is greater than or equal to 3000 and less than 4000, discount is 5%
# d) If purchased amount is greater than or equal to 2000 and less than 3000, discount is 3%
# e) If purchased amount is less than 2000, discount is 2%
purchased_account = float(input("Enter the purchased account: "))

if purchased_account >= 5000:
    discount = 0.10 * purchased_account
    print("The discount amount is:", discount)
elif purchased_account >= 4000:
    discount = 0.07 * purchased_account
    print("The discount amount is:", discount)
elif purchased_account >= 3000:
    discount = 0.05 * purchased_account
    print("The discount amount is:", discount)
elif purchased_account >= 2000:
    discount = 0.03 * purchased_account
    print("The discount amount is:", discount)
else:
    discount = 0.02 * purchased_account
    print("The discount amount is:", discount)


# 6. Write a program to calculate the simple interest on the basis of following assumption:
# a) If balance is greater than 99999, interest is 7 %
# b) If balance is greater than or equal to 50000 and less than 100000 interest is 5 %
# c) If balance is less than 50000, interest is 3%
balance = float(input("Enter the balance: "))
balance = float(input("Enter the balance: "))
time = int(input("Enter the number of years: "))

if balance > 99999:
    rate = 7 / 100
elif 50000 <= balance < 100000:
    rate = 5 / 100
else:
    rate = 3 / 100

simple_interest = (balance * time * rate) / 100
print(f"The simple interest is: {simple_interest}")


# 7. Write a program to test whether a number is even or odd.
number = int(input("Enter the number:"))
if number%2==0:
    print('The entered number is even number ')
else:
    print("the entered number is odd. ")


# 8. Admission to a professional course is subject to the following conditions:
# a) Marks in mathematics >=60
# b) Marks in physics >=50
# c) Marks in chemistry >=40
# d) Total in all three subjects >=200

# Or

# Total in mathematics and physics>=150
# Given the marks in three subjects, write a program to process the applications to list eligible
# candidates.
    
math = float(input("Enter the marks obtained in mathematics : "))
physics = float(input("Enter the marks obtained in physics: "))
chemistry = float(input("Enter the marks obtained in chemistry: "))
total_marks = math+physics+chemistry
Total_math_phy = math+physics

if (math>=60 and physics>=50 and chemistry>=40 and total_marks>=200) or Total_math_phy>=150:
    print('You are eligible candidate. ')
else:
    print("You are not eligible candidate. ")


"""
9. The rates of tax on gross salary are as shown below:
Income Tax
Less than 10,000 Nill
Rs. 10,000 to 19,999 10%
Rs. 20,000 to 39,999 15%
Rs. 40,000 to above 20%
Write a program to compute the net salary after deducting the tax for the given information
and print the same.

"""
gross_salary = float(input('Enter the gross salary: '))

if gross_salary<10000:
    rate = 0
elif 10000<=gross_salary<=19999:
    rate = 10/100
elif 20000<=gross_salary<=39999:
    rate = 15/100
else: 
    rate = 20/100

net_salary = gross_salary-rate*gross_salary
print("The net salary is : ",net_salary)

# 10. Write a program to check whether a year entered is leap or not.

def leap_year(year:int):
    if year%400==0 or year%100==0:#for the 21st century.
        print('the entered year is leap year.')
    elif(year%4==0 and year%100 !=0):# for the 20th century.
        print('the entered year is leap year.')
    else: 
        print("The entered year is not leap year.")

leap_year(1992)


# 11. Write a program to display “MDS” 10 times.
for i in range(1,11,1):
    print('MDS')

# 12. Write a program to find sum and average of 10 numbers stored in a list.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_length = len(list1)
sum_of_numbers = 0

for i in range(list_length):
    sum_of_numbers += list1[i]

average = sum_of_numbers / list_length

print("Sum of numbers:", sum_of_numbers)
print("Average of numbers:", average)

# 13. Write a program to display prime numbers up to 100.
def check_prime(number:int):
    for item in range(2,number,1):
        if number%item == 0:
            return False
        else: 
            return True

for num in range(2,101):
    if check_prime(num):
        print(num)


# 14. Write a program to find sum of digits of a number.
def digit_sum(num: int) -> int:
    num_str = str(num)  
    sum_of_digits = 0

    for digit_char in num_str:
        digit = int(digit_char) 
        sum_of_digits += digit

    return sum_of_digits

result = digit_sum(123)
print("Sum of digits:", result)

# 15. Write a program to check whether a number is palindrome or not.
number = str(input("Enter the number : "))
number_str = str(number)
reversed_num = number_str[::-1]
print(reversed_num)

if number == reversed_num:
    print(f'the number {number} is palindrome.')
else:
    print(f'the number {number} is not palindrome.')
    

# 16. Write a program to check if a number is Armstrong Number or not.
number = int(input("Enter the number: "))
str_number = str(number)
sum = 0

for digit_str in str_number:
    digit = int(digit_str)
    sum = digit**3 + sum

if sum == number:
    print('The number is an Armstrong number.')
else:
    print('The number is not an Armstrong number.')


# 17. Write a program to count number of vowels in a string.

def count_vowel(word:str)->int:
    count = 0
    vowel = ['a','e','i','o','u']
    for each in word:
        print(each)
        if each in vowel:
            count = count +1
    return count 
    
result = count_vowel('orange')
print(f'No of the vowels : {result}')

# 18. Write a program to find smallest and largest number among 10 numbers stored in a list.
# Example list of numbers
numbers = [23, 56, 12, 89, 45, 67, 34, 78, 90, 21]

smallest = largest = numbers[0]

for number in numbers[1:]:
    if number < smallest:
        smallest = number
    elif number > largest:
        largest = number


print("Smallest number:", smallest)
print("Largest number:", largest)

# 19. Write a program to count even numbers and odd numbers stored in a list.
l1 = [1,2,3,4,5,6,7,8,9,10,11]
count_odd = 0
count_even = 0 
for item in l1:
    if item%2==0:
        count_even = count_even + 1 
    else:
        count_odd = count_even + 1

print('the number of odd numbers in the list l1 is: ',count_odd)
print(f'the number of even number in list l1 is: {count_even}')


# 20. Write a program to find sum of two matrices.

matrix1 = [[2, 4],
           [5, 6]]
matrix2 = [[4, 3],
           [2, 4]]

row_no = len(matrix1)
col_no = len(matrix1[0])


matrix = []


for i in range(row_no):
    matrix.append([])

    for j in range(col_no):
        matrix[i].append(matrix1[i][j] + matrix2[i][j])

print(matrix)


# 21. Write a program to find product of two matrices.


matrix1 = [[2, 4],
           [5, 6]]
matrix2 = [[4, 3],
           [2, 4]]

row_m1, col_m1 = len(matrix1), len(matrix1[0])
row_m2, col_m2 = len(matrix2), len(matrix2[0])


if col_m1 != row_m2:
    print("Error: Incompatible matrices for multiplication.")
else:
   
    result_matrix = []
    for i in range(row_m1):
        result_matrix.append([])
        for j in range(col_m2):
            result_matrix[i].append(0)
            for k in range(col_m1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    
    for row in result_matrix:
        print(row)

# 22. Write a program using list comprehension to find sum of only even numbers.

def sum_even(list1:list):
    return sum([x for x in list1 if x%2==0])
list2 = [1,2,3,4,5,6,7]
total_sum_of_even = sum_even(list2)
print(total_sum_of_even)

# 23. Write a program using function with return type to find sum of two numbers.
def sum_of_two_numbers(num1:float, num2:float)->float:
    addition = num1 + num2
    return addition

number1 = 3.2
number2 = 4.5
result = sum_of_two_numbers(number1, number2)

print(result)


# 24. Write a program using recursive function to find factorial of a number.
def factorial(num:int):
    if num==0 or num==1:
        return 1
    else:
        fact = num*factorial(num-1)
        return fact
        
a= factorial(5)
print(a)


# 25. Write a program using recursive function to find nth Fibonacci number.
def fibonacci_series_iterative(num):
    fibonacci_sequence = [0, 1]

    for i in range(2, num + 1):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

num = 5
fibonacci_series_result = fibonacci_series_iterative(num)
print(f"Fibonacci series up to {num} terms: {fibonacci_series_result}")




# 26. Create a class Rectangle containing instance variables length and breadth. The class also
# contains two instance methods area() and perimeter() to find area and perimeter of rectangles
# respectively. Use this class to find area and perimeter of two different rectangles.


class Rectangle:
    def __init__(self,l,b) -> None:
        self.length = l
        self.breadth = b

    def area(self):
        return f'the area of the rectangle is:{self.length * self.breadth} '
    
    def perimeter(self):
        return f'the perimeter of the rectangle is:{2*self.length+2*self.breadth}'

if __name__=='__main__':
    rect1 = Rectangle(3,2)
    print(rect1.area())
    print(rect1.perimeter())

    rect2 = Rectangle(5,10)
    area = rect2.area()
    print(area)
    peri = rect2.perimeter()
    print(peri)


# 27. Create a class Circle containing an instance variable radius. The class also contains two
# instance methods area() and circumference() to find area and circumference of circles
# respectively. Use this class to find area and circumference of two different circles. Use PI as a
# class variable.

class Circle():
    PI = 3.15 

    def __init__(self, rad: int) -> None:
        self.radius = rad
    
    def area(self) -> float:
        return Circle.PI * (self.radius**2)
    
    def circumference(self) -> float:
        return 2 * Circle.PI * self.radius


c1 = Circle(3)
area1 = c1.area()
print(f'The area of the circle is: {area1:.2f}')
print('------------------------------------------')
peri1 = c1.circumference() 
print(f'The perimeter of the circle is: {peri1:.2f}')
print('---------------')
c2 = Circle(4)
area2 = c2.area()
print(f'The area of the circle is: {area2:.2f}')
print('-------------------------------------')
peri2 = c2.circumference()  
print(f'The perimeter of the circle is: {peri2:.2f}')

# 28. Create a class Box with instance variables width, height and depth. The class also contains
# instance methods volume() and surface_area() to find volume and surface area of boxes
# respectively. Use this class to find volume and surface area of two different boxes.
class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width * self.height * self.depth

    def surface_area(self):
        return 2 * (self.width * self.height + self.depth * self.width + self.height * self.depth)

# Example usage
box1 = Box(3, 4, 5)
volume1 = box1.volume()
surface_area1 = box1.surface_area()

print(f"Box 1 - Width: {box1.width}, Height: {box1.height}, Depth: {box1.depth}")
print(f"Volume: {volume1}")
print(f"Surface Area: {surface_area1}")
print("-------------------------------")

box2 = Box(2, 6, 3)
volume2 = box2.volume()
surface_area2 = box2.surface_area()

print(f"Box 2 - Width: {box2.width}, Height: {box2.height}, Depth: {box2.depth}")
print(f"Volume: {volume2}")
print(f"Surface Area: {surface_area2}")


"""
29. Create a class Time with three instance variables hours, minutes, and seconds. Add instance
methods display() to display the time in hh:mm:ss format and add() to add two time objects.
Use this class to add and display two different time objects.

"""
class Time():
    def __init__(self,hours,minutes,seconds) -> None:
        self.hours = hours 
        self.minutes = minutes 
        self.seconds = seconds 


    def display(self):
        return f' the time is : {self.hours} hours: {self.minutes} minutes: {self.seconds} seconds'


    def __add__(self,other):
        total_seconds = (self.hours+other.hours) *3600 + (self.minutes+other.minutes) *60 + (self.seconds+other.seconds)
        new_hour = total_seconds//3600
        remaining_seconds = total_seconds%3600
        new_minutes = remaining_seconds//60
        new_seconds = remaining_seconds%60
        return Time(new_hour,new_minutes,new_seconds)


t1 = Time(2,3,4)
t2 = Time(2,33,59)
add = t1+t2
print(add.display())



# 30. Create a class Distance containing instance variables feet and inches. The class also contains
# instance methods add() and compare() to add and compare two distance objects respectively.
# Use this class to create two different distance objects and add and compare these two distance
# objects.
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def display(self):
        return f'The feet is {self.feet} and the inches is: {self.inches}'

    def __add__(self, other):
        total_inches = (self.feet + other.feet) * 12 + self.inches + other.inches
        new_feet = total_inches // 12
        new_inches = total_inches % 12
        return Distance(new_feet, new_inches)

    def compare(self, other):
        if self.feet == other.feet:
            if self.inches > other.inches:
                return 'The object1 distance is greater than object2.'
            else:
                return 'The object1 distance is less than object2.'
        else:
            if self.feet > other.feet:
                return 'The object1 distance is greater than object2.'
            else:
                return 'The object1 distance is less than object2.'


d1 = Distance(4, 4)
d2 = Distance(5, 11)

add_result = d1 + d2
print(add_result.display())

print(d1.compare(d2))


"""
31. Create a class Student with instance variables name, roll_number, and marks in five subjects.
Add three instance methods in this class to calculate total(), percentage(), and division() of the
marks obtained by the students. Use this class to find total marks obtained, percentage, and
division of five students.

"""
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.total = sum(marks)

    def Calculate_Total(self):
        return f'The Total marks obtained is: {self.total} out of total 500.'

    def Percentage(self):
        percent = (self.total / (5 * 100)) * 100  
        return f'The percentage obtained by student is: {percent}%'

    def division(self):
        percent = (self.total / (5 * 100)) * 100  
        if 80 <= percent <= 100:
            return 'The student scored distinction.'
        elif percent >= 60:
            return 'First division.'
        elif percent >= 40:
            return 'Second division.'
        else:
            return 'Third division.'

name = input('Enter the name: ')
roll_no = int(input('Enter the roll number: '))
marks_obtained = [45, 56, 75, 68, 97]
s1 = Student(name, roll_no, marks_obtained)
print(s1.Calculate_Total())
print(s1.Percentage())
print(s1.division())

"""
32. Create a parent class Bonus with instance variables sales_id and sales_amount. Add get_bonus
method that calculates a salesperson’s bonus using the foumula bonus = sales * 0.05. Create a
child class named PremiumBonus from Bonus. The child class’s get_premium_bonus()
method should calculate the bonus using the formula bonus = sales * 0.05 + (sales – 2500) *
0.01. Now, create an object of PremiumBonus class and use this object to find both bonus and
premium bonus.
"""

class Bonus():
    def __init__(self,sales_id,sales_amount) -> None:
        self.sales_id = sales_id
        self.sales_amount = sales_amount
    
    def get_bonus(self):
        salesperson_bonus = self.sales_amount * 0.05
        return salesperson_bonus
    
class PremiumBonus(Bonus):
    def __init__(self, sales_id, sales_amount) -> None:
        super().__init__(sales_id, sales_amount)

    def get_premium_bonus(self):
        bonus = self.sales_amount * 0.05 +(self.sales_amount -2500)*0.01
        return bonus
    

p1 = PremiumBonus(1,2300)

bonus = p1.get_bonus()
print(bonus)
print('---------------------------------')

premium  = p1.get_premium_bonus()
print(premium)



"""
34. Write a program that reads a text file and displays the following:
a. Number of characters
b. Number of vowels
c. Number of consonants
d. Number of words
e. Number of lines
"""


# for the  a)
def count_non_space_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            sum = 0
            for char in content:
                if char !=' ':
                    sum = sum +1
            num_non_space_characters = sum 
            print("Number of non-space characters:", num_non_space_characters)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

count_non_space_characters('file1.txt')



# b). Number of vowels
def count_vowels(file_path):
    try: 
        with open(file_path,'r') as file:
            content = file.read()
            sum =0
            for char in content: 
                if char.lower() in 'aeiou':
                    sum = sum +1
            no_of_vowels = sum
            print(f'The total number of the vowels in the file is:{no_of_vowels}')

    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print('An error occured:',e)

count_vowels('file1.txt')
        
# c). Number of consonants

def count_consonent(file_path):
    try:
        with open(file_path,'r') as file:
            content = file.read()
            count_cons = 0 
            for char in content:
                if char.lower() not in 'aeiou' and char !=' ':
                    count_cons = count_cons +1
            no_of_consonents = count_cons
            print(f'The total number of consonents in the file are: {no_of_consonents}')

            
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print('An error occured:',e)

count_consonent('file1.txt')

# d). Number of words:
def count_words(file_path):
    try:
        with open(file_path,'r') as file:
            content = file.read()
            content_in_list = content.split()
            length = len(content_in_list)
            print('The total words in the file are:', length)

            
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print('An error occured !!!',e)

count_words('file1.txt')


# e). Number of lines
def count_lines(file_path):
    try:
        with open(file_path,'r') as file:
            content = file.read()
            num_lines = content.count('\n')+1
            print(f'The Total number of lines in the file are: {num_lines}')


    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print('An error occured !!!',e)

count_lines('file1.txt')



"""
35. Write a program that reads a text file and writes its output in another text file. The output
should contain
a. Number of letters
b. Number of digits, and
c. Number of other characters
"""
# a) Number of letters
def count_no_of_letters(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file_input:
            content = file_input.read()
            # Count the number of letters (assuming letters are alphabets A-Z or a-z)
            count = sum(c.isalpha() for c in content)

        with open(output_filename, 'w') as file_output:
            file_output.write(f"The number of letters in the {input_filename} is: {count}")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


count_no_of_letters('file1.txt', 'file2.txt')


# b). Number of digits
def count_digits(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            digit_count = sum(c.isdigit() for c in content)

        with open(output_file, 'w') as file_out:
            file_out.write(f'The number of digits in the {input_file} is: {digit_count}')

    except FileNotFoundError:
        print(f'Error! File not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

count_digits('file1.txt', 'file3.txt')

# c). Number of other characters 
def count_other_characters(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            other_character_count = sum(not c.isalnum() for c in content)

        with open(output_file, 'w') as file_out:
            file_out.write(f'The number of other characters in the {input_file} is: {other_character_count}')

    except FileNotFoundError:
        print(f'Error! File not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

count_other_characters('file1.txt', 'file4.txt')



# 36. Write a program that reads the file containing texts and counts the number of whitespaces.
def count_whitespaces(input_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            whitespace_count = sum(c.isspace() for c in content)

        print(f'The number of whitespaces in the {input_file} is: {whitespace_count}')

    except FileNotFoundError:
        print(f'Error! File not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

count_whitespaces('file1.txt')

"""
37. Write a program to find sum and average of numbers stored in a file. Create a separate file to
write output.

"""
def calculate_sum_and_average(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            numbers = []

            for line in file:
                # Split the line into individual values based on commas
                values = line.strip().split(',')
                
                # Try to convert each value to a float
                for value in values:
                    try:
                        number = float(value)
                        numbers.append(number)
                    except ValueError:
                        pass

            if not numbers:
                raise ValueError("No valid numbers found in the file.")

            total_sum = sum(numbers)
            average = total_sum / len(numbers)

        with open(output_file, 'w') as file_out:
            file_out.write(f'Sum of numbers: {total_sum}\n')
            file_out.write(f'Average of numbers: {average}')

        print(f'Sum and average calculated and written to {output_file}')

    except FileNotFoundError:
        print(f'Error! File not found.')
    except ValueError as ve:
        print(f'Error: {ve}')
    except Exception as e:
        print(f'An error occurred: {e}')

calculate_sum_and_average('file5.txt', 'file6.txt')
