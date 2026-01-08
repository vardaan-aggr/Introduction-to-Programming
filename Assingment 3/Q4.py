class Course:
    def __init__(self, cname, credits, assessments, grading_policy):
        self.cname = cname
        self.credits = credits
        self.assessments = assessments  # List of (assessment name, weight)
        self.weights = [weight for _, weight in assessments]
        self.grading_policy = sorted(grading_policy, reverse=True)  
        self.grade_cutoffs = {}
        self.students = []

    def calculate_grades(self):#generates the dict of students in the particulr to help finalize the grade 
        grade_ranges = {f"lis_{i+1}": [] for i in range(4)}
        for student in self.students:
            for i, threshold in enumerate(self.grading_policy):
                if threshold - 2 <= student.total_percent <= threshold + 2:
                    grade_ranges[f"lis_{i+1}"].append(student.total_percent)

        for key, scores in grade_ranges.items():#final grade decider
            scores.sort()
            if len(scores) < 2:
                continue
            max_gap = 0
            cutoff = scores[0]
            for i in range(1, len(scores)):
                gap = scores[i] - scores[i - 1]
                if gap > max_gap:
                    max_gap = gap
                    cutoff = (scores[i] + scores[i - 1]) / 2
            self.grade_cutoffs[key[-1]] = round(cutoff, 2)
            print(self.grade_cutoffs)

        # Set cutoff
        self.grade_cutoffs["A"] = self.grade_cutoffs.get("1", self.grading_policy[0])
        self.grade_cutoffs["B"] = self.grade_cutoffs.get("2", self.grading_policy[1])
        self.grade_cutoffs["C"] = self.grade_cutoffs.get("3", self.grading_policy[2])
        self.grade_cutoffs["D"] = self.grade_cutoffs.get("4", self.grading_policy[3])
        self.grade_cutoffs["F"] = 0

        # Assign grades to students
        for student in self.students:
            student.assign_grade(self.grade_cutoffs)

    def summary_gen(self):
        print(f"Course Name: {self.cname}, Credits: {self.credits}")
        print("Assessments and Weights:")
        for name, weight in self.assessments:
            print(f"  {name}: {weight}%")
        print("\nGrade Cutoffs:")
        for grade, cutoff in self.grade_cutoffs.items():
            print(f"  {grade}: {cutoff}%")
        print("\nGrade Distribution:")
        grade_counts = {grade: 0 for grade in ["A", "B", "C", "D", "F"]}
        for student in self.students:
            grade_counts[student.grade] += 1
        for grade, count in grade_counts.items():
            print(f"  {grade}: {count}")

    def insert_student_data(self, marks_file):
        with open(marks_file, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                roll_no = parts[0]
                marks = [float(m) for m in parts[1:]]
                student_obj = Student(roll_no, marks)
                self.students.append(student_obj)

    def student_file_creater(self, output_file):
        with open(output_file, "w") as f:
            for student in self.students:
                f.write(f"{student.roll_no}, {student.total_percent}, {student.grade}\n")
        print(f"Grades exported to {output_file}")

    def student_finder(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(student.get_summary())
                return
        print("Student not found!")


class Student:
    def __init__(self, roll_no, marks):
        self.roll_no = roll_no
        self.marks = marks  # List of marks for each assessment
        self.total_percent = 0
        self.grade = None

    def calculate_total_percent(self, weights):
        weighted_sum = 0
        sum_weight=sum(weights)
        for i in range (len(weights)):
            mark=self.marks[i]
            # weight=weights[i]
            weighted_sum += (mark / sum_weight)*100
        self.total_percent = round(weighted_sum, 2)

    def assign_grade(self, grade_cutoffs):
        for grade, cutoff in grade_cutoffs.items():
            if grade == "F":
                self.grade = grade  # Assign F if no other grade is assigned
                break
            if self.total_percent >= cutoff:
                self.grade = grade
                break

    def get_summary(self):
        return f"Roll No: {self.roll_no}, Total: {self.total_percent}%, Grade: {self.grade}"


cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
grading_policy = [80, 65, 50, 40]# give only 4 inputs
course = Course(cname, credits, assessments, grading_policy)

course.insert_student_data("marks.txt")# Load student marks from file

for student in course.students:
    student.calculate_total_percent(course.weights)
course.calculate_grades()


while True:
    print("\nOptions: [1] Summary, [2] Export Grades, [3] Search Student")
    choice = input("Enter your choice: ")
    if choice == "1":
        course.summary_gen()
    elif choice == "2":
        course.student_file_creater("student_grades.txt")
    elif choice == "3":
        roll_no = input("Enter Roll No: ")
        course.student_finder(roll_no)
    else:
        break
