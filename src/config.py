import os

class Config:
    secretKey = os.getenv('SECRET_KEY', 'd5zmAsUt3bZdZrBjhcpJ7T2ocQgmVXfM')
    database = os.getenv('DATABASE', 'sqlite:///usersdb.sqlite3')
    adminUser = os.getenv('ADMIN_USER', 'admin')
    adminPassword = os.getenv('ADMIN_PASSWORD', '123')

config = Config()