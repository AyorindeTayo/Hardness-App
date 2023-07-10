
# Installing flask 
-cd /path/to/project-directory      # Choose your project directory
-virtualenv -p python3 venv  # For Python 3, or


-source venv/bin/activate    # Activate the virual environment
(venv)$ pip install flask     # Install flask using 'pip' which is symlinked to pip2 or pip3 (no sudo needed)
......
Successfully installed Jinja2-2.9.5 MarkupSafe-0.23 Werkzeug-0.11.15 click-6.7 flask-0.12 itsdangerous-0.24
(venv)$ pip show flask        # Check installed packages
Name: Flask
Version: 0.12
Summary: A microframework based on Werkzeug, Jinja2 and good intentions
Location: .../venv/lib/python3.5/site-packages
Requires: Werkzeug, itsdangerous, click, Jinja2
(venv)$ pip show Werkzeug
Name: Werkzeug
Version: 0.11.15
Summary: The Swiss Army knife of Python web development
Location: .../venv/lib/python3.5/site-packages
Requires: 
(venv)$ pip show Jinja2
Name: Jinja2
Version: 2.9.5
Summary: A small but fast and easy to use stand-alone template engine written in pure python.
Location: .../venv/lib/python3.5/site-packages
Requires: MarkupSafe
(venv)$ deactivate  # Exit virutal environment


# Hardness-App
Web app for Vickers Hardness Prediction for welded stainless steel. 

![Imgur](https://imgur.com/xwhL9V9.png)

