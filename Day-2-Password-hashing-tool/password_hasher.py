import bcrypt

class PasswordHasher:

    @staticmethod
    def hash_password(password: str) -> bytes:
        password_bytes = password.encode('utf-8')

        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password_bytes, salt)

        return hashed
    
    @staticmethod
    def verify_password(password: str, hashed: bytes) -> bool:
        verify_bytes = password.encode('utf-8')
        return bcrypt.checkpw(verify_bytes, hashed)