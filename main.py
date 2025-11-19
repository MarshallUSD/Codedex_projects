from user_identity import UserIdentity
from secure_user import SecureUser
from account_access import AccountAccess

def main():

    print("=== VALID USAGE ===")
    secure_user = SecureUser("alimjan", "test@example.com", "998901234567")
    print("Initial status:", secure_user.identity_status())  # UNVERIFIED

    
    secure_user.grant_permission("VIEW_BALANCE")

    secure_user._identity.request_verification()
    secure_user._identity.verify()

    secure_user.grant_permission("TRANSFER")


    print("\n=== ILLEGAL DIRECT ACCESS ATTEMPTS ===")

    print("Direct access attempts commented out (would raise AttributeError).")

    print("\n=== ILLEGAL STATE TRANSITIONS ===")
    try:
        secure_user._identity.request_verification()
    except ValueError as e:
        print("Caught error:", e)

    try:
        temp_user = UserIdentity("test", "a@b.com", "998901234567")
        temp_user.verify()
    except ValueError as e:
        print("Caught error:", e)

    print("\n=== RESTRICTED PERMISSIONS BEFORE VERIFICATION ===")
    temp_user2 = SecureUser("test2", "c@d.com", "998901234567")
    try:
        temp_user2.grant_permission("WITHDRAW")
    except PermissionError as e:
        print("Caught error:", e)

    print("\n=== FINAL STATE OUTPUT ===")
    print("Username:", secure_user._identity.username)
    print("Email:", secure_user._identity.get_email())
    print("Phone:", secure_user._identity.get_phone_number())   # ✅ nom mos
  # endi to‘g‘ri ishlaydi
    print("Verification Status:", secure_user.identity_status())
    print("Permissions:", secure_user._SecureUser__access.get_permissions())  # accessing via name-mangled
    print("Audit Log:")
    for log in secure_user.get_audit_log():
        print(" -", log)


if __name__ == "__main__":
    main()








