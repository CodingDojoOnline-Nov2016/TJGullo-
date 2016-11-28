'''Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A'''

#if i > 100 or i < 60:
    #print("Wasn't a valid score")


grades = []
for i in range(10):
    grades.append(int(input("Enter 10 test scores between 60 and 100: ")))

for i in grades:
    if i >= 60 and i <= 69:
        print("Score: "+ str(i) +"; Your grade is a D")
    elif i >= 70 and i <= 79:
        print("Score: "+ str(i) +"; Your grade is a C")
    elif i >= 80 and i <= 89:
        print("Score: "+ str(i) +"; Your grade is a B")
    elif i >= 90 and i <= 100:
        print("Score: "+ str(i) +"; Your grade is an A")
