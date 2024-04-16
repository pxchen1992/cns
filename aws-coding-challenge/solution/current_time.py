# pip3 install flask
# Visiting the root URL (/) will display a welcome message directing users to use /now to get the current time


from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Route to display the current time
@app.route('/now')
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Route for the root URL
@app.route('/')
def index():
    return "Welcome to the current time service. Use /now to get the current time."

# Route for the favicon.ico request (optional)
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
