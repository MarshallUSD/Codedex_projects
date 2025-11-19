import re

class UserIdentity:
    def __init__(self, username: str, email: str, phone_num: str):
        self.username = username

        self._email = None
        self.set_email(email)

        self.__phone_number = None
        self.__set_phone(phone_num)

        self.__verification_status = "UNVERIFIED"  # fixed case

    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        if self.__validate_email(new_email):
            self._email = new_email
            self.__log_state_changes("Email updated")
        else:
            raise ValueError("Invalid email error")

    def get_phone_number(self):   # ✅ nom mos
     return self.__phone_number


    def request_verification(self) -> None:
        if self.__verification_status == "UNVERIFIED":
            self.__verification_status = "PENDING"
            self.__log_state_changes("Verification requested")
        else:
            raise ValueError("Illegal state transition: must be UNVERIFIED to request verification")

    def verify(self):
        if self.__verification_status == "PENDING":
            self.__verification_status = "VERIFIED"  # fixed assignment
            self.__log_state_changes("Verification Accepted")
        else:
            raise ValueError("Illegal state transition: must be PENDING to verify")

    def get_verification_status(self):
        return self.__verification_status

    

    def __validate_email(self, email: str):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

    def __validate_phone(self, phone: str):
        return re.match(r"^\d{10,15}$", phone) is not None

    def __set_phone(self, phone: str):
        if self.__validate_phone(phone):
            self.__phone_number = phone
            self.__log_state_changes("Phone number set")
        else:
            raise ValueError("Invalid phone number format")  # fixed message

    def __log_state_changes(self, message: str) -> None:
        print(f"[State change] {message}")




user = UserIdentity("alimjan", "test@example.com", "998901234567")

print(user.get_email())              # test@example.com
print(user.get_phone_number())              # 998901234567
print(user.get_verification_status())# UNVERIFIED

user.request_verification()
print(user.get_verification_status())# PENDING

user.verify()
print(user.get_verification_status())# VERIFIED
