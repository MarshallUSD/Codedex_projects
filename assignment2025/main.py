"""
Student Progress & Attendance Management System
Main Entry Point

Author: Abdullaev Alimjan
Date: 14-January 2026
Version: 1.0

This is a console-based application for managing student attendance,
grades, and academic progress at a university.
"""

from ui import UI

def main():
    """Main function to start the application"""
    try:
        # Create and run the user interface
        app = UI()
        app.run()
    
    except KeyboardInterrupt:
        print("\n\n⚠️ Application interrupted by user.")
        print("👋 Goodbye!")
    
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please contact system administrator.")

if __name__ == "__main__":
    main()