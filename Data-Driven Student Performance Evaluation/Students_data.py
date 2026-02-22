def students():
    import pandas as pd

    while True:
        try:
            value = input(
                "Do you want to fill in your Data? [Enter yes or no]: "
            ).strip().lower()

            if value == "yes":
                allowed = {
                "Parental_Involvement": ["Low", "Medium", "High"],
                "Access_to_Resources": ["Low", "Medium", "High"],
                "Extracurricular_Activities": ["Yes", "No"],
                "Motivation_Level": ["Low", "Medium", "High"],
                "Internet_Access": ["Yes", "No"],
                "Family_Income": ["Low", "Medium", "High"],
                "Teacher_Quality": ["Low", "Medium", "High"],
                "School_Type": ["Public", "Private"],
                "Peer_Influence": ["Negative", "Neutral", "Positive"],
                "Learning_Disabilities": ["Yes", "No"],
                "Parental_Education_Level": ["High School", "College", "Postgraduate"],
                "Distance_from_Home": ["Near", "Moderate", "Far"],
                "Gender": ["Male", "Female"]
                }

                def get_valid_input(prompt, options):
                    while True:
                        value = input(f"{prompt} {options}: ").strip().title()
                        if value in options:
                            return value
                        print("Invalid input. Please enter one of:", options)

                # Numeric inputs
                Hours_Studied = float(input("Enter Hours Studied (0–40): "))
                Attendance = float(input("Enter Attendance % (0–100): "))
                Sleep_Hours = float(input("Enter Sleep Hours (4–10): "))
                Previous_Scores = float(input("Enter Previous Score (0–100): "))
                Tutoring_Sessions = float(input("Enter Tutoring Sessions (0–5): "))
                Physical_Activity = float(input("Enter Physical Activity Hours (0–10): "))

                # Categorical inputs
                student = {
                    "Hours_Studied": Hours_Studied,
                    "Attendance": Attendance,
                    "Parental_Involvement": get_valid_input("Parental Involvement", allowed["Parental_Involvement"]),
                    "Access_to_Resources": get_valid_input("Access to Resources", allowed["Access_to_Resources"]),
                    "Extracurricular_Activities": get_valid_input("Extracurricular Activities", allowed["Extracurricular_Activities"]),
                    "Sleep_Hours": Sleep_Hours,
                    "Previous_Scores": Previous_Scores,
                    "Motivation_Level": get_valid_input("Motivation Level", allowed["Motivation_Level"]),
                    "Internet_Access": get_valid_input("Internet Access", allowed["Internet_Access"]),
                    "Tutoring_Sessions": Tutoring_Sessions,
                    "Family_Income": get_valid_input("Family Income", allowed["Family_Income"]),
                    "Teacher_Quality": get_valid_input("Teacher Quality", allowed["Teacher_Quality"]),
                    "School_Type": get_valid_input("School Type", allowed["School_Type"]),
                    "Peer_Influence": get_valid_input("Peer Influence", allowed["Peer_Influence"]),
                    "Physical_Activity": Physical_Activity,
                    "Learning_Disabilities": get_valid_input("Learning Disabilities", allowed["Learning_Disabilities"]),
                    "Parental_Education_Level": get_valid_input("Parental Education Level", allowed["Parental_Education_Level"]),
                    "Distance_from_Home": get_valid_input("Distance from Home", allowed["Distance_from_Home"]),
                    "Gender": get_valid_input("Gender", allowed["Gender"])
                }
                return pd.DataFrame([student])
        
            elif value == "no":
                student1 = {
                'Hours_Studied': 15,
                'Attendance': 75,
                'Parental_Involvement': 'Medium',
                'Access_to_Resources': 'Medium',
                'Extracurricular_Activities': 'Yes',
                'Sleep_Hours': 6,
                'Previous_Scores': 65,
                'Motivation_Level': 'Medium',
                'Internet_Access': 'Yes',
                'Tutoring_Sessions': 1,
                'Family_Income': 'Medium',
                'Teacher_Quality': 'Medium',
                'School_Type': 'Public',
                'Peer_Influence': 'Neutral',
                'Physical_Activity': 4,
                'Learning_Disabilities': 'No',
                'Parental_Education_Level': 'College',
                'Distance_from_Home': 'Moderate',
                'Gender': 'Female'
                }
                student2 = {
                    'Hours_Studied': 32,
                    'Attendance': 96,
                    'Parental_Involvement': 'High',
                    'Access_to_Resources': 'High',
                    'Extracurricular_Activities': 'Yes',
                    'Sleep_Hours': 8,
                    'Previous_Scores': 88,
                    'Motivation_Level': 'High',
                    'Internet_Access': 'Yes',
                    'Tutoring_Sessions': 3,
                    'Family_Income': 'High',
                    'Teacher_Quality': 'High',
                    'School_Type': 'Private',
                    'Peer_Influence': 'Positive',
                    'Physical_Activity': 6,
                    'Learning_Disabilities': 'No',
                    'Parental_Education_Level': 'Postgraduate',
                    'Distance_from_Home': 'Near',
                    'Gender': 'Male'
                }
                student3 = {
                    'Hours_Studied': 5,
                    'Attendance': 55,
                    'Parental_Involvement': 'Low',
                    'Access_to_Resources': 'Low',
                    'Extracurricular_Activities': 'No',
                    'Sleep_Hours': 5,
                    'Previous_Scores': 45,
                    'Motivation_Level': 'Low',
                    'Internet_Access': 'No',
                    'Tutoring_Sessions': 0,
                    'Family_Income': 'Low',
                    'Teacher_Quality': 'Low',
                    'School_Type': 'Public',
                    'Peer_Influence': 'Negative',
                    'Physical_Activity': 2,
                    'Learning_Disabilities': 'Yes',
                    'Parental_Education_Level': 'High School',
                    'Distance_from_Home': 'Far',
                    'Gender': 'Male'
                }
                student4 = {
                    'Hours_Studied': 25,
                    'Attendance': 88,
                    'Parental_Involvement': 'Medium',
                    'Access_to_Resources': 'Medium',
                    'Extracurricular_Activities': 'Yes',
                    'Sleep_Hours': 7,
                    'Previous_Scores': 72,
                    'Motivation_Level': 'High',
                    'Internet_Access': 'Yes',
                    'Tutoring_Sessions': 2,
                    'Family_Income': 'Medium',
                    'Teacher_Quality': 'Medium',
                    'School_Type': 'Public',
                    'Peer_Influence': 'Positive',
                    'Physical_Activity': 5,
                    'Learning_Disabilities': 'No',
                    'Parental_Education_Level': 'College',
                    'Distance_from_Home': 'Moderate',
                    'Gender': 'Female'
                }

                student5 = {
                    'Hours_Studied': 8,
                    'Attendance': 92,
                    'Parental_Involvement': 'High',
                    'Access_to_Resources': 'High',
                    'Extracurricular_Activities': 'No',
                    'Sleep_Hours': 7,
                    'Previous_Scores': 68,
                    'Motivation_Level': 'Medium',
                    'Internet_Access': 'Yes',
                    'Tutoring_Sessions': 1,
                    'Family_Income': 'Medium',
                    'Teacher_Quality': 'High',
                    'School_Type': 'Public',
                    'Peer_Influence': 'Neutral',
                    'Physical_Activity': 3,
                    'Learning_Disabilities': 'No',
                    'Parental_Education_Level': 'College',
                    'Distance_from_Home': 'Near',
                    'Gender': 'Male'
                }

                perfect_student = {
                    'Hours_Studied': 40,
                    'Attendance': 100,
                    'Parental_Involvement': 'High',
                    'Access_to_Resources': 'High',
                    'Extracurricular_Activities': 'Yes',
                    'Sleep_Hours': 8,
                    'Previous_Scores': 98,
                    'Motivation_Level': 'High',
                    'Internet_Access': 'Yes',
                    'Tutoring_Sessions': 5,
                    'Family_Income': 'High',
                    'Teacher_Quality': 'High',
                    'School_Type': 'Private',
                    'Peer_Influence': 'Positive',
                    'Physical_Activity': 6,
                    'Learning_Disabilities': 'No',
                    'Parental_Education_Level': 'Postgraduate',
                    'Distance_from_Home': 'Near',
                    'Gender': 'Female'
                }

                worst_student = {
                    'Hours_Studied': 0,
                    'Attendance': 30,
                    'Parental_Involvement': 'Low',
                    'Access_to_Resources': 'Low',
                    'Extracurricular_Activities': 'No',
                    'Sleep_Hours': 4,
                    'Previous_Scores': 35,
                    'Motivation_Level': 'Low',
                    'Internet_Access': 'No',
                    'Tutoring_Sessions': 0,
                    'Family_Income': 'Low',
                    'Teacher_Quality': 'Low',
                    'School_Type': 'Public',
                    'Peer_Influence': 'Negative',
                    'Physical_Activity': 0,
                    'Learning_Disabilities': 'Yes',
                    'Parental_Education_Level': 'High School',
                    'Distance_from_Home': 'Far',
                    'Gender': 'Male'
                }

                hardworking_poor = {
                    'Hours_Studied': 35,
                    'Attendance': 95,
                    'Parental_Involvement': 'Low',
                    'Access_to_Resources': 'Low',
                    'Extracurricular_Activities': 'No',
                    'Sleep_Hours': 6,
                    'Previous_Scores': 70,
                    'Motivation_Level': 'High',
                    'Internet_Access': 'No',
                    'Tutoring_Sessions': 0,
                    'Family_Income': 'Low',
                    'Teacher_Quality': 'Medium',
                    'School_Type': 'Public',
                    'Peer_Influence': 'Neutral',
                    'Physical_Activity': 3,
                    'Learning_Disabilities': 'No',
                    'Parental_Education_Level': 'High School',
                    'Distance_from_Home': 'Far',
                    'Gender': 'Male'
                }

                lazy_rich = {
                    'Hours_Studied': 2,
                    'Attendance': 60,
                    'Parental_Involvement': 'High',
                    'Access_to_Resources': 'High',
                    'Extracurricular_Activities': 'Yes',
                    'Sleep_Hours': 9,
                    'Previous_Scores': 65,
                    'Motivation_Level': 'Low',
                    'Internet_Access': 'Yes',
                    'Tutoring_Sessions': 3,
                    'Family_Income': 'High',
                    'Teacher_Quality': 'High',
                    'School_Type': 'Private',
                    'Peer_Influence': 'Negative',
                    'Physical_Activity': 5,
                    'Learning_Disabilities': 'No',
                    'Parental_Education_Level': 'Postgraduate',
                    'Distance_from_Home': 'Near',
                    'Gender': 'Female'
                }

                impossible_student = {
                    'Hours_Studied': 60,
                    'Attendance': 110,
                    'Parental_Involvement': 'High',
                    'Access_to_Resources': 'High',
                    'Extracurricular_Activities': 'Yes',
                    'Sleep_Hours': 12,
                    'Previous_Scores': 110,
                    'Motivation_Level': 'High',
                    'Internet_Access': 'Yes',
                    'Tutoring_Sessions': 10,
                    'Family_Income': 'High',
                    'Teacher_Quality': 'High',
                    'School_Type': 'Private',
                    'Peer_Influence': 'Positive',
                    'Physical_Activity': 10,
                    'Learning_Disabilities': 'No',
                    'Parental_Education_Level': 'Postgraduate',
                    'Distance_from_Home': 'Near',
                    'Gender': 'Male'
                }

                students = pd.DataFrame([
                    student1,
                    student2,
                    student3,
                    student4,
                    student5,
                    perfect_student,
                    worst_student,
                    hardworking_poor,
                    lazy_rich,
                    impossible_student
                ])  
                return students

            else:
                raise ValueError("Invalid input. Please enter 'yes' or 'no'.")

        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")

        