import json
import os

class Storage:
    """Handles all file operations for data persistence"""
    
    def __init__(self):
        self.data_dir = 'data'
        self.logs_dir = 'logs'
        self._ensure_directories()
        self._initialize_files()
    
    def _ensure_directories(self):
        """Create data and logs directories if they don't exist"""
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.logs_dir, exist_ok=True)
    
    def _initialize_files(self):
        """Initialize JSON files with default data if they don't exist"""
        # Initialize users.json with default admin
        users_file = os.path.join(self.data_dir, 'users.json')
        if not os.path.exists(users_file):
            default_users = {
                "admin": {
                    "password": "admin123",
                    "role": "admin"
                },
                "teacher1": {
                    "password": "teacher123",
                    "role": "teacher"
                },
                "student1": {
                    "password": "student123",
                    "role": "student",
                    "student_id": "S001"
                }
            }
            self.save_users(default_users)
        
        # Initialize other files
        for filename in ['students.json', 'attendance.json', 'grades.json']:
            filepath = os.path.join(self.data_dir, filename)
            if not os.path.exists(filepath):
                with open(filepath, 'w') as f:
                    json.dump({}, f, indent=4)
        
        # Initialize log file
        log_file = os.path.join(self.logs_dir, 'system.log')
        if not os.path.exists(log_file):
            with open(log_file, 'w') as f:
                f.write("System Log Initialized\n")
    
    def load_users(self):
        """Load users from JSON file"""
        try:
            with open(os.path.join(self.data_dir, 'users.json'), 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("❌ Error reading users file!")
            return {}
    
    def save_users(self, users):
        """Save users to JSON file"""
        try:
            with open(os.path.join(self.data_dir, 'users.json'), 'w') as f:
                json.dump(users, f, indent=4)
            return True
        except Exception as e:
            print(f"❌ Error saving users: {e}")
            return False
    
    def load_students(self):
        """Load students data"""
        try:
            with open(os.path.join(self.data_dir, 'students.json'), 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
    
    def save_students(self, students):
        """Save students data"""
        try:
            with open(os.path.join(self.data_dir, 'students.json'), 'w') as f:
                json.dump(students, f, indent=4)
            return True
        except Exception as e:
            print(f"❌ Error saving students: {e}")
            return False
    
    def load_attendance(self):
        """Load attendance records"""
        try:
            with open(os.path.join(self.data_dir, 'attendance.json'), 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
    
    def save_attendance(self, attendance):
        """Save attendance records"""
        try:
            with open(os.path.join(self.data_dir, 'attendance.json'), 'w') as f:
                json.dump(attendance, f, indent=4)
            return True
        except Exception as e:
            print(f"❌ Error saving attendance: {e}")
            return False
    
    def load_grades(self):
        """Load grades"""
        try:
            with open(os.path.join(self.data_dir, 'grades.json'), 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
    
    def save_grades(self, grades):
        """Save grades"""
        try:
            with open(os.path.join(self.data_dir, 'grades.json'), 'w') as f:
                json.dump(grades, f, indent=4)
            return True
        except Exception as e:
            print(f"❌ Error saving grades: {e}")
            return False
    
    def generate_report(self, report_type, data):
        """Generate report file"""
        filename = f"report_{report_type}_{self._get_timestamp()}.txt"
        filepath = os.path.join(self.logs_dir, filename)
        
        try:
            with open(filepath, 'w') as f:
                f.write(f"{'='*60}\n")
                f.write(f"{report_type.upper()} REPORT\n")
                f.write(f"{'='*60}\n\n")
                f.write(data)
            print(f"✅ Report generated: {filename}")
            return True
        except Exception as e:
            print(f"❌ Error generating report: {e}")
            return False
    
    def _get_timestamp(self):
        """Get current timestamp for filenames"""
        from datetime import datetime
        return datetime.now().strftime("%Y%m%d_%H%M%S")