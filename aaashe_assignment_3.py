#Personal information Storage

Full_name = "Abraheem Ashe"
Studen_email = "aaasheh@ncat.edu"
Hometown = "Harlem, NY"
Graduation_semester = "Spring 2027"
Major = "Information technology"

#Academic Data Organization(LISTS)

Current_course_list = ["COMP 163", "MATH 131", "Mgmt 343", "ENVS 201"]
Completed_course_list = ["pre calc", "Public speaking", "African American History", "Biology"]
Credit_hours_list = [3, 3, 3, 3]
GPA_history_list = [3.0, 2.5, 3.0, 2.8]

#Contact Information Storage(TUPLES)

Emergency_contact_tuple = ("Mom", "Amber", "336-345-3444")
Home_address_tuple = ("830 W Market st", "Greensbor, NC", 27401)
Instagram_info_tuple = ("Instagram", "@top_key", 150)
Twitter_info_tuple = ("Twitter", "@AbraheemA", 130)
Birthday_tuple = ("Birthday", 12, 26, 2003)

#Interest Tracking(SETS)

Current_skills_set = {"Python basics", "Computer Hardware","Problem solving", "Time management", "Newgen firewalls"}
current_skills_set_sorted = sorted(Current_skills_set)
Skills_to_learn = {"JavaScript", "Linux", "Azure", "Red hat", "Public speaking"}
Career_interest_set = {"Cybersecurityt", "blue team specialist", "Data science", "cloud security"}
Hobbies_set = {"Gaming", "basketball", "Reading", "Soccer", "Music"}
Entertainment_backlog_set = {"One Piece", "comicks", "Music", "drawing", "sports"}

#Organizational Mapping(Dictionaries)

course_credits_dictionary = {"COMP 163":3, "MATH 150":3, "ENG 101":3, "HIS 105":3}
Course_professors_dictionary = {"COMP 163":"Prof. Rhodes", "MATH 150":"Dr. Lee", "ENG 101":"Dr. Martinez", "HIS 105":"Dr. Brown"}
Course_room_dictionary = {'COMP 163': 'M-Eric 300', 'MATH 150': 'Marteena 201','ENG 101': 'Crosby 121', 'HIS 105': 'Crosby 210'}
Monthly_budget_dictionary = {"Food":450, "Entertainment":200, "Books":125, "Transportation":100}
Study_hours = {"Programming":10, "Math":8, "English":4, "History":3}
Contact_directory = {"Mom":7045550199, "Roommate":3365557821, "Academic Advisor":3363345000}

#Required Calculations

Total_current_credits = sum(Credit_hours_list) 
cumulative_gpa = sum(GPA_history_list) /4
size_current_course = len(Current_course_list)
completed_courses = len(Completed_course_list)
weekly_study_hours = Study_hours["Programming"] + Study_hours["English"] + Study_hours["Math"] + Study_hours["History"]
Academic_load = Total_current_credits + weekly_study_hours
Monthly_budget = Monthly_budget_dictionary["Food"] + Monthly_budget_dictionary["Entertainment"] + Monthly_budget_dictionary["Books"] + Monthly_budget_dictionary["Transportation"]
Daily_food = round(Monthly_budget_dictionary["Food"] / 30, 2)
Annual_budget = Monthly_budget * 12
Study_cost = round(Monthly_budget_dictionary["Books"] / weekly_study_hours , 2)

#Analytics Calculations
Total_socialmedia = Instagram_info_tuple[2] + Twitter_info_tuple[2]
Skills_current = len(Current_skills_set)
Skills_want_learn = len(Skills_to_learn)
contact_directory_size = len(Contact_directory)
entertainment_size = len(Entertainment_backlog_set)
size_hobbies = len(Hobbies_set)

#Print functions
print("=" * 64)
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("=" * 64)
print(f"Student: {Full_name} | Email: {Studen_email}")
print(f'From: {Hometown} | Graduating: {Graduation_semester}')
print(f'Major: {Major}')
print("")
print("=== ACADEMIC PROFILE ===")
print(f'Current Semester: {Total_current_credits} credits across {size_current_course} courses')
print(f'Cumulative GPA: {cumulative_gpa:.2f}')
print(f'Weekly Study Time: {weekly_study_hours} hours')
print(f'Academic Investment: ${Study_cost} per study hour')
print("")
print("Current Courses:")
print(f'COMP 163 - {course_credits_dictionary["COMP 163"]} credits - {Course_professors_dictionary["COMP 163"]} - {Course_room_dictionary["COMP 163"]}')
print(f'MATH 150 - {course_credits_dictionary["MATH 150"]} credits - {Course_professors_dictionary["MATH 150"]} - {Course_room_dictionary["MATH 150"]}')
print(f'ENG 101 - {course_credits_dictionary["ENG 101"]} credits - {Course_professors_dictionary["ENG 101"]} - {Course_room_dictionary["ENG 101"]}')
print(f'HIS 105 - {course_credits_dictionary["HIS 105"]} credits - {Course_professors_dictionary["HIS 105"]} - {Course_room_dictionary["HIS 105"]}')
print("")
print("=== PERSONAL DEVELOPMENT ===")
print(f'Current skills: {Current_skills_set}')
print(f'Learning Goals: {Skills_to_learn}')
print(f'Career Interests: {Career_interest_set}')
print(f'Skills Currently Have: {Skills_current}')
print(f'Skills Want to Learn: {Skills_want_learn}')
print("")
print("=== FINANCIAL OVERVIEW ===")
print(f'Monthly Budget: ${Monthly_budget}')
print(f'Food: ${Monthly_budget_dictionary["Food"]} (${Daily_food:.1f}/day)')
print(f'Entertainment: ${Monthly_budget_dictionary["Entertainment"]}')
print(f'Books: ${Monthly_budget_dictionary["Books"]}')
print(f'Transportation: ${Monthly_budget_dictionary["Transportation"]}')
print(f'Annual Projection: ${Annual_budget}')
print("")
print("=== CONNECTIONS & CONTACTS ===")
print(f'Emergency Contact: {Emergency_contact_tuple[1]} ({Emergency_contact_tuple[0]}) - {Emergency_contact_tuple[2]}')
print(f'Home Address: {Home_address_tuple[0]}, {Home_address_tuple[1]} {Home_address_tuple[2]}')
print(f'Social Media Presence: {Total_socialmedia} followers across 2 platforms')
print(f'Key Contacts: {contact_directory_size} people in directory')
print("")
print("=== LIFE STATISTICS ===")
print(f'Total Courses Completed: {completed_courses}')
print(f'Current Academic Load: {Academic_load} weekly commitments')
print(f'Entertainment Backlog: {entertainment_size} items')
print(f'Current Hobbies: {size_hobbies} activities')
print("=" * 64)