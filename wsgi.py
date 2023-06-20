import os
import sys

path = '/home/Ayorinde/mysite/'
if path not in sys.path:
    sys.path.append(path)

from app import app as application

if __name__ == '__main__':
    application.run()