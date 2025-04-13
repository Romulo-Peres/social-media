import bcrypt
import sys
import os

BCRYPT_ROUNDS = 12

if len(sys.argv) != 3:
    print('Utility usage: python3 create-user.py <username> <password>')
    sys.exit(1)

salt = bcrypt.gensalt(rounds=BCRYPT_ROUNDS)

hashed = bcrypt.hashpw(sys.argv[2].encode('utf-8'), salt)
    
print(f'Your credentials:\nUsername: {sys.argv[1]}, password: {sys.argv[2]}')

print('\n')

print(f'Insert query: INSERT INTO users (name, password) VALUES ("{sys.argv[1]}", "{hashed.decode('utf-8')}");')
