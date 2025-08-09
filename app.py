# from flask import Flask, request, jsonify, render_template
# import pyodbc
# from datetime import datetime

# app = Flask(__name__)

# # Function to connect to SQL Server - bedel xogta hoos ku qoran
# def get_db_connection():
    
#     conn = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};'
#         'SERVER=MARYAMA-ABDIRAS\\SQLEXPRESS;'
#         'DATABASE=GameDB;'
#         'Trusted_Connection=yes;'
#         'TrustServerCertificate=yes;'
#     )
#     return conn


# # Create visitors table haddii uusan jirin
# def init_db():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute('''
#         IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'visitors')
#         BEGIN
#             CREATE TABLE visitors (
#                 id INT IDENTITY(1,1) PRIMARY KEY,
#                 ip NVARCHAR(50),
#                 user_agent NVARCHAR(255),
#                 visit_time DATETIME
#             )
#         END
#     ''')
#     conn.commit()
#     conn.close()

# init_db()

# def save_visitor(ip, user_agent):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT INTO visitors (ip, user_agent, visit_time) VALUES (?, ?, ?)
#     ''', (ip, user_agent, datetime.now()))
#     conn.commit()
#     conn.close()

# @app.route('/')
# def index():
#     ip = request.remote_addr
#     user_agent = request.headers.get('User-Agent')
#     save_visitor(ip, user_agent)
#     return render_template('index.html')

# @app.route('/visitors')
# def visitors():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT ip, user_agent, visit_time FROM visitors ORDER BY id DESC')
#     rows = cursor.fetchall()
#     conn.close()
#     visitors_list = []
#     for row in rows:
#         visitors_list.append({
#             'ip': row[0],
#             'user_agent': row[1],
#             'visit_time': row[2].strftime('%Y-%m-%d %H:%M:%S')
#         })
#     return jsonify(visitors_list)



# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)


from flask import Flask, request, jsonify
import pyodbc
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=MARYAMA-ABDIRAS\\SQLEXPRESS;'
        'DATABASE=GameDB;'
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )
    return conn

@app.route('/api/visit', methods=['POST'])
def save_visit():
    data = request.get_json()
    ip = data.get('ip')
    user_agent = data.get('user_agent')
    visit_time = datetime.now()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO visitors (ip, user_agent, visit_time) VALUES (?, ?, ?)
    ''', (ip, user_agent, visit_time))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success'}), 201

if __name__ == '__main__':
    app.run(debug=True)
