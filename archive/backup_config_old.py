import random
import string

def generate_backup_code(length):
    characters = string.ascii_letters + string.digits
    backup_code = ''.join(random.choice(characters) for _ in range(length))
    return backup_code

backup_code = generate_backup_code(10)
print(backup_code)