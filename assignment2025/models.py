from abc import ABC, abstractmethod
from decorators import require_role, log_action
import json

class User(ABC):
    """Abstract base class for all users"""
    
    def __init__(self, username, password, role):
        self._username = username
        self._password = password
        self._role = role
    
    @property
    def username(self):
        return self._username
    
    @property
    def role(self):
        return self._role
    
    def verify_password(self, password):
        """Verify user password"""
        return self._password == password
    
    @abstractmethod
    def show_menu(self):
        """Abstract method - each role has different menu"""
        pass


class Admin(User):
    """Admin class with user management capabilities"""
    
    def __init__(self, username, password):
        super().__init__(username, password, "admin")
    
    @log_action
    @require_role("admin")
    def create_user(self, storage, new_username, password, role):
        """Create new user account"""
        from storage import Storage
        users = storage.load_users()
        
        if new_username in users:
            print(f"❌ User '{new_username}' already exists!")
            return False
        
        users[new_username] = {
            "password": password,
            "role": role
        }
        storage.save_users(users)
        print(f"✅ User '{new_username}' created successfully as {role}!")
        return True
    
    @log_action
    @require_role("admin")
    def delete_user(self, storage, username):
        """Delete user account"""
        users = storage.load_users()
        
        if username not in users:
            print(f"❌ User '{username}' not found!")
            return False
        
        del users[username]
        storage.save_users(users)
        print(f"✅ User '{username}' deleted successfully!")
        return True
    
    @require_role("admin")
    def view_logs(self):
        """View system logs"""
        try:
            with open('logs/system.log', 'r') as f:
                logs = f.readlines()
                print("\n" + "="*60)
                print("SYSTEM LOGS".center(60))
                print("="*60)
                for log in logs[-20:]:  # Show last 20 logs
                    print(log.strip())
        except FileNotFoundError:
            print("❌ No logs found!")
    
    def show_menu(self):
        """Display admin menu"""
        print("\n" + "="*50)
        print("ADMIN MENU".center(50))
        print("="*50)
        print("1. Create User")
        print("2. Delete User")
        print("3. Reset Password")
        print("4. View System Logs")
        print("5. View All Users")
        print("0. Logout")
        print("="*50)


class Teacher(User):
    """Teacher class with attendance and grading capabilities"""
    
    def __init__(self, username, password):
        super().__init__(username, password, "teacher")
    
    @log_action
    @require_role("teacher", "admin")
    def record_attendance(self, storage, student_id, date, status):
        """Record student attendance"""
        attendance = storage.load_attendance()
        
        if student_id not in attendance:
            attendance[student_id] = []
        
        attendance[student_id].append({
            "date": date,
            "status": status
        })
        
        storage.save_attendance(attendance)
        print(f"✅ Attendance recorded for student {student_id}")
        return True
    
    @log_action
    @require_role("teacher", "admin")
    def mark_assignment(self, storage, student_id, assignment_name, grade):
        """Mark student assignment"""
        grades = storage.load_grades()
        
        if student_id not in grades:
            grades[student_id] = []
        
        grades[student_id].append({
            "assignment": assignment_name,
            "grade": grade
        })
        
        storage.save_grades(grades)
        print(f"✅ Grade recorded: {assignment_name} - {grade}/100")
        return True
    
    @require_role("teacher", "admin")
    def view_analytics(self, storage):
        """View class analytics"""
        grades = storage.load_grades()
        attendance = storage.load_attendance()
        
        print("\n" + "="*60)
        print("CLASS ANALYTICS".center(60))
        print("="*60)
        
        for student_id in grades:
            avg = calculate_average([g['grade'] for g in grades[student_id]])
            att_rate = calculate_attendance_rate(attendance.get(student_id, []))
            status = check_academic_risk(avg, att_rate)
            
            print(f"\nStudent: {student_id}")
            print(f"  Average: {avg:.2f}%")
            print(f"  Attendance: {att_rate:.2f}%")
            print(f"  Status: {status}")
    
    def show_menu(self):
        """Display teacher menu"""
        print("\n" + "="*50)
        print("TEACHER MENU".center(50))
        print("="*50)
        print("1. Record Attendance")
        print("2. Mark Assignment")
        print("3. View Student Analytics")
        print("4. Generate Report")
        print("0. Logout")
        print("="*50)


class Student(User):
    """Student class with view-only capabilities"""
    
    def __init__(self, username, password, student_id):
        super().__init__(username, password, "student")
        self._student_id = student_id
    
    @property
    def student_id(self):
        return self._student_id
    
    def view_grades(self, storage):
        """View personal grades"""
        grades = storage.load_grades()
        my_grades = grades.get(self.student_id, [])
        
        print("\n" + "="*50)
        print("MY GRADES".center(50))
        print("="*50)
        
        if not my_grades:
            print("No grades recorded yet.")
            return
        
        for g in my_grades:
            print(f"{g['assignment']}: {g['grade']}/100")
        
        avg = calculate_average([g['grade'] for g in my_grades])
        print(f"\nAverage: {avg:.2f}%")
    
    def view_attendance(self, storage):
        """View personal attendance"""
        attendance = storage.load_attendance()
        my_attendance = attendance.get(self.student_id, [])
        
        print("\n" + "="*50)
        print("MY ATTENDANCE".center(50))
        print("="*50)
        
        if not my_attendance:
            print("No attendance records yet.")
            return
        
        for record in my_attendance:
            print(f"{record['date']}: {record['status']}")
        
        rate = calculate_attendance_rate(my_attendance)
        print(f"\nAttendance Rate: {rate:.2f}%")
    
    def show_menu(self):
        """Display student menu"""
        print("\n" + "="*50)
        print("STUDENT MENU".center(50))
        print("="*50)
        print("1. View Grades")
        print("2. View Attendance")
        print("3. View Academic Status")
        print("0. Logout")
        print("="*50)


# Utility functions
def calculate_average(grades):
    """Calculate average of grades"""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def calculate_attendance_rate(attendance_records):
    """Calculate attendance percentage"""
    if not attendance_records:
        return 0
    present = sum(1 for r in attendance_records if r['status'] == 'present')
    return (present / len(attendance_records)) * 100

def check_academic_risk(average, attendance_rate):
    """Determine academic risk level"""
    if average < 50 or attendance_rate < 75:
        return "⚠️ AT RISK"
    elif average < 70 or attendance_rate < 85:
        return "⚡ WARNING"
    else:
        return "✅ GOOD STANDING"