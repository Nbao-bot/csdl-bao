students = [
{"id": "22000001", "name": "Nguyen Minh Anh", "major": "KHDL"},
{"id": "22000002", "name": "Tran Duc Long", "major": "KHDL"},
]
courses = [
{
"code": "INT2204",
"name": "Co so du lieu Web va he thong thong tin",
"capacity": 3,
"enrolled": 2,
},
{
"code": "INT2205",
"name": "Khai pha du lieu",
"capacity": 2,
"enrolled": 2,
},
]
enrollments = [
{"student_id": "22000001", "course_code": "INT2204"}
]

def find_course(course_code):
    for course in courses:

        if course["code"] == course_code:
            return course
    return None

def can_enroll(student_id, course_code):
    course = find_course(course_code)

    if course is None:
        return False, "Hoc phan khong ton tai"
    
    if course["enrolled"] >= course["capacity"]:
        return False, "Lop da du so luong"
    
    duplicated = any(
        item["student_id"] == student_id and item["course_code"] == course_code
        for item in enrollments
    )
    if duplicated:
        return False, "Sinh vien da dang ky hoc phan nay"
    return True, "Co the dang ky"

def enroll_student(student_id, course_code):
    student_exists = any(student["id"] == student_id for student in students)
    if not student_exists:
        return False, "Sinh vien khong ton tai"

    can_register, message = can_enroll(student_id, course_code)
    if not can_register:
        return False, message

    course = find_course(course_code)
    enrollments.append({"student_id": student_id, "course_code": course_code})
    course["enrolled"] += 1
    return True, "Dang ky hoc phan thanh cong"

def search_courses(keyword):
    normalized = keyword.strip().lower()
    results = []
    for course in courses:
        code = course["code"].lower()
        name = course["name"].lower()
        if normalized in code or normalized in name:
            results.append(course)
    return results

def main():
    print("CourseHub - Buoi 1")

    for course in courses:
        remaining = course["capacity"] - course["enrolled"]
        print(course["code"], "- con", remaining, "cho")

    print("Tim hoc phan:", find_course("INT2204"))
    print("Kiem tra co the dang ky:", can_enroll("22000002", "INT2204"))

    test_cases = [
        ("Dang ky trung", "22000001", "INT2204"),
        ("Dang ky thanh cong", "22000002", "INT2204"),
        ("Lop day", "22000002", "INT2205"),
        ("Ma hoc phan khong ton tai", "22000002", "INT9999"),
        ("Ma sinh vien khong ton tai", "99999999", "INT2204"),
    ]
    for case_name, student_id, course_code in test_cases:
        print(case_name + ":", enroll_student(student_id, course_code))

    try:
        limit = int(input("Nhap so luong hoc phan muon hien thi: "))
        print(courses[:limit])
    except ValueError:
        print("So luong phai la so nguyen")

    print("Tim kiem hoc phan:", search_courses("web"))


if __name__ == "__main__":
    main()
