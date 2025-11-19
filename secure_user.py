from user_identity import UserIdentity
from account_access import AccountAccess

class SecureUser:
    def __init__(self, username: str, email: str, phone: str):
        self._identity = UserIdentity(username, email, phone)
        self.__access = AccountAccess(self._identity)
        self.__audit_log = []

    def grant_permission(self, permission: str):
        if permission in ("TRANSFER", "WITHDRAW"):
            if self._identity.get_verification_status() != "VERIFIED":
                self.__log_action(f"FAILED to GRANT {permission} (user not verified)")
                raise PermissionError(f"User must be verified to receive {permission}")
        self.__access.add_permission(permission)
        self.__log_action(f"Granted permission: {permission}")

    def revoke_permission(self, permission: str):   # ✅ nom to‘g‘rilandi
        self.__access.remove_permission(permission)
        self.__log_action(f"Revoked permission: {permission}")

    def identity_status(self):
        status = self._identity.get_verification_status()
        self.__log_action(f"Checked status: {status}")
        return status

    def get_audit_log(self):
        return list(self.__audit_log)

    def __log_action(self, message: str):
        self.__audit_log.append(message)


secure_user = SecureUser("alimjan", "test@example.com", "998901234567")

print(secure_user.identity_status())  # UNVERIFIED

try:
    secure_user.grant_permission("TRANSFER")
except PermissionError as e:
    print(e)

secure_user.grant_permission("VIEW_BALANCE")

secure_user._identity.request_verification()
secure_user._identity.verify()

secure_user.grant_permission("TRANSFER")

secure_user.revoke_permission("VIEW_BALANCE")

print(secure_user.get_audit_log())



      
