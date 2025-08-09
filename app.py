from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database setup (simple)
def init_db():
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS visitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            user_agent TEXT,
            visit_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Save visitor info
def save_visitor(ip, user_agent):
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute('INSERT INTO visitors (ip, user_agent, visit_time) VALUES (?, ?, ?)',
              (ip, user_agent, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    # Save visitor data
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    save_visitor(ip, user_agent)
    return render_template('index.html')  # Your game page here

@app.route('/visitors')
def visitors():
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute('SELECT ip, user_agent, visit_time FROM visitors ORDER BY id DESC')
    data = c.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True) 