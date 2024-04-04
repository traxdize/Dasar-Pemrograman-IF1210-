import base64

sandi = "==8GZpRjZvQXauUGdzFGc0NXdq9yL6MHc0RHa"
print(base64.b64decode(sandi[::-1]).decode())