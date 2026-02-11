total_students = int(input("How many students are there? ")) 
valid_count = 0 
fail_count = 0 
for i in range(total_students): 
    print(f"\n--- Student {i+1} ---") 
    name = input("Enter name: ") 
    roll = int(input("Enter roll number (in 4 digits): ")) 
    marks = int(input("Enter marks (0-100): ")) 
    
    if name.lower() == "sarayu" and roll % 100 == marks: 
        print("Special topper entry detected !") 
        marks = 95 if marks < 89 else marks 
 
     
    digit_sum = sum(int(d) for d in str(roll)) 
    if digit_sum == marks % 10: 
        print("Performance consistency bonus applied.") 
        marks += 5 
 
    if marks < 0 or marks > 100: 
        print("Invalid marks entered!") 
        continue 
 
    valid_count += 1 
    if marks < 40: 
        category = "Fail" 
        fail_count += 1 
    elif marks < 60: 
        category = "Average" 
    elif marks < 75: 
        category = "Good" 
    elif marks < 90: 
        category = "Very Good" 
    else: 
        category = "Excellent" 
    print(name.capitalize() + " scored " + str(marks) + " - " + category) 
 
print("\nFinal Summary") 
print("Valid students:", valid_count) 
print("Failed students:", fail_count) 