import bcrypt
a = "Z"
b = 2
c = 3
print(a * b ** c)


def cool():
    d = 4
    v = 10


passwd = b's$cret12'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)

print(salt)
print(hashed)
