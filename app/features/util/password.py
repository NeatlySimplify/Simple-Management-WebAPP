from bcrypt import gensalt, checkpw, hashpw

def hash_password(password: str) -> str:
    if not isinstance(password, str):
        raise ValueError("Password must be a string.")
    # Generate a salt
    salt = gensalt()
    # Hash the password
    hashed_password = hashpw(password.encode('utf-8'), salt)
    # Return the hashed password as a string
    return hashed_password.decode('utf-8')


def verify_password(password: str, hashed_password: str) -> bool:
    if not isinstance(password, str) or not isinstance(hashed_password, str):
        raise ValueError("Both password and hashed_password must be strings.")
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

