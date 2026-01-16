from functools import wraps
from datetime import datetime

def require_role(*allowed_roles):
    """Decorator to restrict function access by user role"""
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if hasattr(self, 'role') and self.role in allowed_roles:
                return func(self, *args, **kwargs)
            else:
                print(f"\n❌ Access Denied! Only {', '.join(allowed_roles)} can perform this action.")
                return None
        return wrapper
    return decorator

def log_action(func):
    """Decorator to log user actions to a file"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = args[0] if args else "Unknown"
        username = getattr(user, 'username', 'System')
        
        try:
            result = func(*args, **kwargs)
            log_entry = f"[{timestamp}] {username} - {func.__name__} - SUCCESS\n"
            
            with open('logs/system.log', 'a') as f:
                f.write(log_entry)
            
            return result
        except Exception as e:
            log_entry = f"[{timestamp}] {username} - {func.__name__} - ERROR: {str(e)}\n"
            with open('logs/system.log', 'a') as f:
                f.write(log_entry)
            raise
    
    return wrapper