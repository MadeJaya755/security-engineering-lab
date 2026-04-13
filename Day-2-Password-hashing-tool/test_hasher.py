from password_hasher import PasswordHasher

password = "admin123"

hashed = PasswordHasher.hash_password(password)
print("hashed password:", hashed)

#test benar
print("verify (correct):", PasswordHasher.verify_password("admin123", hashed))
#test salah
print("verify (incorrect):", PasswordHasher.verify_password("wrongpassword", hashed))