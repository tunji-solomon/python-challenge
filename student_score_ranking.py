
#  Challenge: Student Score Ranking
# Write a function called rank_students that:
# 1️⃣ Takes a list of dictionaries. Each dictionary represents a student and contains:

# 'name': student name (string)

# 'scores': list of integers (their test scores)

# 2️⃣ The function should:

# Calculate each student’s average score, rounded to 2 decimal places.

# Return a list of dictionaries, where each dictionary has:

# 'name': student name

# 'average': their average score

# 3️⃣ The list should be sorted in descending order of average score. If two students have the same average, maintain their original order.

def rank_students(student_list: list[dict]) -> list[dict]:
    
    new_list = []
    for student in student_list:
        name = student.get("name")
        scores = student.get("scores")
        total_score = 0
        for score in scores:
            total_score += score
        average = round(total_score/len(scores), 2)
        
        new_list.append(
            {
                "name" : name,
                "average" : average
            }
        )
        
    new_list.sort(key=lambda item: item["average"], reverse=True)
    return new_list

students = [
    {"name": "Alice", "scores": [80, 90, 100]},
    {"name": "Bob", "scores": [70, 75, 72]},
    {"name": "Charlie", "scores": [90, 85, 95]}
]

print(rank_students(students))
        