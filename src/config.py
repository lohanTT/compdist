import os

class Config:
    secretKey = os.getenv('SECRET_KEY')
    database = os.getenv('DATABASE')
    administrators = os.getenv('ADMINISTRATORS')

config = Config()