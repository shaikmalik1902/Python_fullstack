def validate_phone(phone):
    if len(phone) != 10:
        raise ValueError(f"phone must have 10 digits. Got {len(phone)}")
    return True


try:
    validate_phone("123456")
except ValueError as e:
    print("Error", e)