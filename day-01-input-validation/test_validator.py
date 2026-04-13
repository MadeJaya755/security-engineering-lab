from input_validator import InputValidator

test_inputs = [
    "admin",
    "' OR 1=1 --",
    "<script>alert('hack')</script>",
    "normal_user123"
]

for inp in test_inputs:
    print(f"Input: {inp}")
    print("Safe:", InputValidator.is_safe_input(inp))
    print("Sanitized:", InputValidator.sanitize_input(inp))
    print("-" * 30)