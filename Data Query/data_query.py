import pandas as pd

students_data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Alice', 'Bob', None, 'David', 'Emma', 'Frank', 'Grace'],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', None, 'emma@email.com', 'frank@email.com', 'grace@email.com'],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', None, 'Chennai', 'Delhi']
}

enrollments_data = {
    'student_id': [101, 102, 103, 105, 108, 109],
    'course_name': ['Python', 'Data Science', 'Python', 'Machine Learning', 'AI', 'Python'],
    'enrollment_date': ['2024-01-15', '2024-01-20', '2024-02-01', '2024-02-10', '2024-02-15', '2024-03-01']
}

scores_data = {
    'student_id': [101, 102, 104, 105, 106],
    'exam_score': [85, 92, 78, 88, 95]
}


# Task 1: Data Preparation and Missing Value Handling 
# Create all three DataFrames
students = pd.DataFrame(students_data)
enrollments = pd.DataFrame(enrollments_data)
scores = pd.DataFrame(scores_data)

# For the students DataFrame:
# Display null value count and percentage for each column
print(students.isnull().sum())
print(((students.isnull().sum()/len(students))*100).round(2))

# Fill missing 'city' values with 'Unknown'
students["city"] = students['city'].fillna("Unknown")

# Drop rows where 'name' is missing
students = students.dropna(subset = ['name'])

# Display the cleaned students DataFrame
print(students)

# Task 2: Multiple Join Operations (40 points)
# Perform the following join operations and answer questions:

# 1. Inner Join: Merge students and enrollments on student_id
# How many students appear in the result? --3
# Which students from the students table are excluded and why? -- 104, 106, 107
print("\n------------------------------Inner Join------------------------------")
inner = pd.merge(students, enrollments, on="student_id", how="inner")
print(inner)

# 2. Left Join: Merge students and enrollments on student_id
# How many total rows are in the result?
# Which students have null values in course_name and why?
print("\n------------------------------Left Join------------------------------")
left = pd.merge(students, enrollments, on="student_id", how="left")
print(left)

# 3. Right Join: Merge students and enrollments on student_id
# How many total rows are in the result?
# Which student_ids appear in the result but don't have student names?
print("\n------------------------------Right Join------------------------------")
right = pd.merge(students, enrollments, on="student_id", how="right")
print(right)

# 4. Full Outer Join: Merge students and enrollments on student_id
# How many total rows are in the result?
# Display rows where either student name is null OR course_name is null
print("\n------------------------------Outer Join------------------------------")
full_outer = pd.merge(students, enrollments, on="student_id", how="outer")
print(full_outer)

# 5. Add indicator=True parameter to the outer join and show the distribution of merge sources (_merge column)
outer_distribution = pd.merge(students, enrollments, on="student_id", how="outer", indicator=True)
print(outer_distribution)


# Task 3: Lookup Operation and Automation (30 points)
print("--------------------------------Lookup Operation--------------------------------")

# Create a dictionary mapping student_id to exam_score from the scores DataFrame
# Use the .map() function to add exam scores to the students DataFrame
# Display students with their scores (showing NaN for students without scores)
students_copy = students.copy()
score_lookup = dict(zip(scores['student_id'], scores['exam_score']))
students_copy['exam_score'] = students_copy['student_id'].map(score_lookup).fillna("NaN")
print(students_copy)

# Performance Comparison:
# Implement the same score addition using pd.merge() with a left join
# Explain why lookup (map) is more efficient than merge for this scenario
students_for_JOIN = students.copy()
left_Join = pd.merge (students_for_JOIN, scores, on="student_id", how="left")
print(left_Join)

# Simple Automation:
# Create a function auto_merge(df1, df2, join_type, key_column) that:
# Takes two DataFrames, join type, and key column as input
# Performs the specified merge
# Returns a dictionary with: {'result_df': merged_df, 'row_count': count, 'join_type': type}
# Test your function with at least 2 different join types

def auto_merge(df1, df2, join_type, key_column):
    result = {}
    merged_df = pd.merge(df1, df2, on=key_column, how=join_type)
    count = merged_df.shape[0]
    result['result_df'] = merged_df
    result['row_count'] = count
    result['join_type'] = join_type
    return result

print("--------------------------Auto Merge of Student and Enrollment--------------------------")
left_merge = auto_merge(students, enrollments, "left", "student_id")
right_merge = auto_merge(students, enrollments, "right", "student_id")
inner_merge = auto_merge(students, enrollments, "inner", "student_id")
outer_merge = auto_merge(students, enrollments, "outer", "student_id")

print(left_merge)
print(right_merge)
print(inner_merge)
print(outer_merge)