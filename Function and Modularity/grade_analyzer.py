# Mini Student Grade Analyser

# Task 1: Process the Score
    # Function Name : process_scores(students)
    # Input : Student name and lists of marks as a Dictionary
    # Output : Average mark of each student rounded to 2 decimal points and retrun a new dictionary

def process_scores(students):
    student_avg = {}
    for key, value in students.items():
       student_avg[key] = f"{sum(value)/len(value):.2f}"
    return student_avg

# Task 2: Classify the Grades 
    # Function Name : classify_grades(averages)
    # Input : Takes the student average calculated by the function process_scores()
    # Output : Returns the dictionary format { name: (average, grade) }

def classify_grades(averages):
    grade = {}
    for key, value in averages.items():
        if value >= "90.00":
            grade[key] = (value, "A")
        elif value >= "75.00" and value <= "89.00":
            grade[key] = (value, "B")
        elif value >= "60.00" and value <= "74.00":
            grade[key] = (value, "C")
        elif value < "60.00":
            grade[key] = (value, "F")
        else:
            grade[key] = (value, None)
    return grade

# Task 3: Generate the Report
    # Function Name : generate_report(classified, passing_avg=70)
    # Input : The student average and grade returned from the function classify_grades
    # Output : The formatted report
    # =================== Student Grade Report =====================
    # Greeshma  | Avg: 92.00   | Grade: A   | Status: PASS
    # Manu      | Avg: 72.60   | Grade: C   | Status: PASS
    # Nila      | Avg: 54.40   | Grade: F   | Status: FAIL
    # Varsha    | Avg: 88.80   | Grade: B   | Status: PASS
    # ==============================================================
    # Total Students : 4
    # Passed         : 3
    # Failed         : 1

def generate_report(classified, passing_avg=70):
    pass_count = fail_count = 0
    print ("====================Student Grade Report====================")
    for key,value in classified.items():
        avg , grade = value # tuple unpacking
        if (avg > str(passing_avg)):
            status = "PASS"
            pass_count += 1
        else:
            status = "FAIL"
            fail_count += 1
        print (f"\n{key:<10}     | Avg: {avg}   | Grade: {grade}   | Status: {status}\n")
    print ("="*60)
    print(f"{'Total Students':<15}: {len(classified)} \n" )
    print(f"{'Passed':<15}: {pass_count} \n")
    print(f"{'Failed':<15}: {fail_count}")


student = {
        "Greeshma" : [98, 87, 85, 96, 94],
        "Manu" : [66, 77, 74, 70, 76],
        "Nila" : [55, 58, 48, 60, 51],
        "Varsha" : [89, 81, 100, 88, 86],
    }
average_of_students = process_scores(student)
grade_of_students = classify_grades(average_of_students)
generate_report(grade_of_students)

