
# ✅ Challenge: Student Pass/Fail Classifier
# Write a function called classify_students that:

# 1️⃣ Takes a list of dictionaries, where each dictionary represents a student with:

# 'name': student name (string)

# 'scores': list of integers (test scores out of 100)

# 2️⃣ For each student, calculate their average score.
# 3️⃣ If the average score is >= 50, the student passes, else they fail.
# 4️⃣ Return a dictionary with two keys:

# 'pass': list of names of students who passed

# 'fail': list of names of students who failed

def classify_student(student_list : list[dict]) -> dict:
    
    def get_length(iterable) -> int:
        length = 0
        for _ in iterable:
            length += 1
        return length
    
    classified_student = {
        "Pass" : [],
        "Fail" : []
    }
    
    for student in student_list:
        name = student.get("name")
        scores = student.get("scores")
        
        overall_score = 0
        for score in scores:
            overall_score += score
        average_score = overall_score/get_length(scores)
        
        if average_score >= 50:
            classified_student["Pass"].append(name)
        else:
            classified_student["Fail"].append(name)
            
    return classified_student

students = [
    {"name": "Alice", "scores": [70, 80, 90]},
    {"name": "Bob", "scores": [40, 50, 45]},
    {"name": "Charlie", "scores": [55, 65, 60]},
    {"name": "Daisy", "scores": [30, 35, 40]}
]

print(classify_student(students))