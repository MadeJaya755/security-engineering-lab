import re

class InputValidator:

    # pattern sederhana (bukan production-grade, tapi cukup buat belajar)
    SQLI_PATTERN = re.compile(r"(\bor\b|\band\b|--|;|'|=)", re.IGNORECASE)
    XSS_PATTERN = re.compile(r"(<script>|</script>|<.*?>)", re.IGNORECASE)

    @staticmethod
    def is_safe_input(user_input: str) -> bool:
        if InputValidator.SQLI_PATTERN.search(user_input):
            return False
        if InputValidator.XSS_PATTERN.search(user_input):
            return False
        return True

    @staticmethod
    def sanitize_input(user_input: str) -> str:
        # hapus karakter berbahaya sederhana
        sanitized = re.sub(r"[<>\"'%;()&+]", "", user_input)
        return sanitized