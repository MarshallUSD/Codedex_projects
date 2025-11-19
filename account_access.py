from user_identity import UserIdentity

class AccountAccess:
    def __init__(self, user_identity):
        self.__user_identity = user_identity
        self.__permissions = []

    def get_permissions(self):
        return list(self.__permissions)

    def add_permission(self, permission: str):   # ✅ argument qo‘shildi
        if permission in ("TRANSFER", "WITHDRAW"):
            if self.__user_identity.get_verification_status() != "VERIFIED":
                raise PermissionError(f"User must be VERIFIED to receive {permission}")

        if permission not in self.__permissions:
            self.__permissions.append(permission)

    def remove_permission(self, permission: str):
        if permission in self.__permissions:
            self.__permissions.remove(permission)

    def has_permission(self, permission: str):
        return permission in self.__permissions



user = UserIdentity("alimjan", "test@example.com", "998901234567")
access = AccountAccess(user)

print(access.get_permissions())  # []

try:
    access.add_permission("TRANSFER")   # ❌ unverified user
except PermissionError as e:
    print(e)

access.add_permission("VIEW_BALANCE")   # ✅ safe permission
print(access.get_permissions())  # ['VIEW_BALANCE']

user.request_verification()
user.verify()

access.add_permission("TRANSFER")       # ✅ now allowed
print(access.get_permissions())  # ['VIEW_BALANCE', 'TRANSFER']

print(access.has_permission("WITHDRAW"))  # False
