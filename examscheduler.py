import datetime

# Global variable
college_name = "Bhaktapur Multiple Campus"

# Given data
start_date = "2025-05-01"
exams = [
    ("Python Programming", 0),
    ("Data Structures",    3),
    ("Database Systems",   6),
    ("Computer Networks",  10),
    ("Mathematics",        14),
]


def parse_date(date_str):
    """Converts a date string 'YYYY-MM-DD' to a datetime object."""
    return datetime.datetime.strptime(date_str, "%Y-%m-%d")


def get_exam_date(start_str, days):
    """Returns the exam date as a string 'YYYY-MM-DD' by adding days to start date."""
    start = parse_date(start_str)
    exam_date = start + datetime.timedelta(days=days)
    return exam_date.strftime("%Y-%m-%d")


def print_schedule(start_str, exams):
    """Prints the full exam schedule with college name as header."""

    print("=" * 50)
    print(f"       {college_name}")
    print("            Exam Schedule")
    print("=" * 50)
    print(f"  {'Subject':<25} {'Exam Date'}")
    print("-" * 50)

    for subject, days in exams:
        exam_date = get_exam_date(start_str, days)
        print(f"  {subject:<25} {exam_date}")

    print("=" * 50)
    print(f"  Start Date : {start_str}")
    print(f"  End Date   : {get_exam_date(start_str, exams[-1][1])}")
    print("=" * 50)


# Call the schedule function
print_schedule(start_date, exams)