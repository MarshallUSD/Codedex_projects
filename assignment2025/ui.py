from models import Admin, Teacher, Student
from storage import Storage
from datetime import datetime

class UI:
    """User Interface handler for console interactions"""
    
    def __init__(self):
        self.storage = Storage()
        self.current_user = None
    
    def clear_screen(self):
        """Clear console screen"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_welcome(self):
        """Display welcome screen"""
        self.clear_screen()
        print("\n" + "="*60)
        print("STUDENT PROGRESS & ATTENDANCE MANAGEMENT SYSTEM".center(60))
        print("="*60)
        print("\nWelcome! Please login to continue.\n")
    
    def login(self):
        """Handle user login"""
        users = self.storage.load_users()
        
        print("\n--- LOGIN ---")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if username not in users:
            print("❌ Invalid username or password!")
            return False
        
        user_data = users[username]
        
        if user_data['password'] != password:
            print("❌ Invalid username or password!")
            return False
        
        # Create user object based on role
        role = user_data['role']
        
        if role == 'admin':
            self.current_user = Admin(username, password)
        elif role == 'teacher':
            self.current_user = Teacher(username, password)
        elif role == 'student':
            student_id = user_data.get('student_id', username.upper())
            self.current_user = Student(username, password, student_id)
        else:
            print("❌ Unknown user role!")
            return False
        
        print(f"\n✅ Login successful! Welcome, {username} ({role})")
        input("\nPress Enter to continue...")
        return True
    
    def handle_admin_menu(self):
        """Handle admin-specific menu actions"""
        while True:
            self.clear_screen()
            self.current_user.show_menu()
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                # Create User
                print("\n--- CREATE USER ---")
                new_username = input("Username: ").strip()
                password = input("Password: ").strip()
                print("Roles: admin, teacher, student")
                role = input("Role: ").strip().lower()
                
                if role not in ['admin', 'teacher', 'student']:
                    print("❌ Invalid role!")
                    input("\nPress Enter to continue...")
                    continue
                
                if role == 'student':
                    student_id = input("Student ID: ").strip().upper()
                    users = self.storage.load_users()
                    users[new_username] = {
                        "password": password,
                        "role": role,
                        "student_id": student_id
                    }
                    self.storage.save_users(users)
                    print(f"✅ Student created with ID: {student_id}")
                else:
                    self.current_user.create_user(self.storage, new_username, password, role)
                
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                # Delete User
                print("\n--- DELETE USER ---")
                username = input("Username to delete: ").strip()
                confirm = input(f"Are you sure you want to delete '{username}'? (yes/no): ").strip().lower()
                
                if confirm == 'yes':
                    self.current_user.delete_user(self.storage, username)
                else:
                    print("❌ Deletion cancelled.")
                
                input("\nPress Enter to continue...")
            
            elif choice == '3':
                # Reset Password
                print("\n--- RESET PASSWORD ---")
                username = input("Username: ").strip()
                new_password = input("New Password: ").strip()
                
                users = self.storage.load_users()
                if username in users:
                    users[username]['password'] = new_password
                    self.storage.save_users(users)
                    print(f"✅ Password reset for '{username}'")
                else:
                    print(f"❌ User '{username}' not found!")
                
                input("\nPress Enter to continue...")
            
            elif choice == '4':
                # View Logs
                self.current_user.view_logs()
                input("\nPress Enter to continue...")
            
            elif choice == '5':
                # View All Users
                users = self.storage.load_users()
                print("\n" + "="*50)
                print("ALL USERS".center(50))
                print("="*50)
                for username, data in users.items():
                    print(f"{username} - {data['role']}")
                input("\nPress Enter to continue...")
            
            elif choice == '0':
                print("\n👋 Logging out...")
                break
            
            else:
                print("❌ Invalid choice!")
                input("\nPress Enter to continue...")
    
    def handle_teacher_menu(self):
        """Handle teacher-specific menu actions"""
        while True:
            self.clear_screen()
            self.current_user.show_menu()
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                # Record Attendance
                print("\n--- RECORD ATTENDANCE ---")
                student_id = input("Student ID: ").strip().upper()
                date = datetime.now().strftime("%Y-%m-%d")
                print(f"Date: {date}")
                print("Status: present / absent / late")
                status = input("Status: ").strip().lower()
                
                if status in ['present', 'absent', 'late']:
                    self.current_user.record_attendance(self.storage, student_id, date, status)
                else:
                    print("❌ Invalid status!")
                
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                # Mark Assignment
                print("\n--- MARK ASSIGNMENT ---")
                student_id = input("Student ID: ").strip().upper()
                assignment = input("Assignment Name: ").strip()
                
                try:
                    grade = float(input("Grade (0-100): ").strip())
                    if 0 <= grade <= 100:
                        self.current_user.mark_assignment(self.storage, student_id, assignment, grade)
                    else:
                        print("❌ Grade must be between 0 and 100!")
                except ValueError:
                    print("❌ Invalid grade format!")
                
                input("\nPress Enter to continue...")
            
            elif choice == '3':
                # View Analytics
                self.current_user.view_analytics(self.storage)
                input("\nPress Enter to continue...")
            
            elif choice == '4':
                # Generate Report
                self.current_user.view_analytics(self.storage)
                print("\n(Report also saved to logs folder)")
                input("\nPress Enter to continue...")
            
            elif choice == '0':
                print("\n👋 Logging out...")
                break
            
            else:
                print("❌ Invalid choice!")
                input("\nPress Enter to continue...")
    
    def handle_student_menu(self):
        """Handle student-specific menu actions"""
        while True:
            self.clear_screen()
            self.current_user.show_menu()
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                # View Grades
                self.current_user.view_grades(self.storage)
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                # View Attendance
                self.current_user.view_attendance(self.storage)
                input("\nPress Enter to continue...")
            
            elif choice == '3':
                # View Academic Status
                from models import calculate_average, calculate_attendance_rate, check_academic_risk
                
                grades = self.storage.load_grades()
                attendance = self.storage.load_attendance()
                
                my_grades = grades.get(self.current_user.student_id, [])
                my_attendance = attendance.get(self.current_user.student_id, [])
                
                avg = calculate_average([g['grade'] for g in my_grades])
                att_rate = calculate_attendance_rate(my_attendance)
                status = check_academic_risk(avg, att_rate)
                
                print("\n" + "="*50)
                print("ACADEMIC STATUS".center(50))
                print("="*50)
                print(f"\nAverage Grade: {avg:.2f}%")
                print(f"Attendance Rate: {att_rate:.2f}%")
                print(f"Status: {status}")
                
                input("\nPress Enter to continue...")
            
            elif choice == '0':
                print("\n👋 Logging out...")
                break
            
            else:
                print("❌ Invalid choice!")
                input("\nPress Enter to continue...")
    
    def run(self):
        """Main application loop"""
        while True:
            self.show_welcome()
            
            if self.login():
                # Route to appropriate menu based on role
                if self.current_user.role == 'admin':
                    self.handle_admin_menu()
                elif self.current_user.role == 'teacher':
                    self.handle_teacher_menu()
                elif self.current_user.role == 'student':
                    self.handle_student_menu()
                
                self.current_user = None
            else:
                retry = input("\nTry again? (yes/no): ").strip().lower()
                if retry != 'yes':
                    print("\n👋 Goodbye!")
                    break