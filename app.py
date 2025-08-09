# from flask import Flask, request, jsonify, render_template
# import pyodbc
# from datetime import datetime

# app = Flask(__name__)

# def get_db_connection():
#     try:
#         conn = pyodbc.connect(
#             'DRIVER={ODBC Driver 17 for SQL Server};'
#             'SERVER=MARYAMA-ABDIRAS\\SQLEXPRESS;'
#             'DATABASE=GameDB;'
#             'Trusted_Connection=yes;'
#             'TrustServerCertificate=yes;'
#         )
#         return conn
#     except Exception as e:
#         print("Error connecting to database:", e)
#         return None

# # API to save visitor info
# @app.route('/api/visit', methods=['POST'])
# def save_visit():
#     data = request.get_json()
#     ip = data.get('ip')
#     user_agent = data.get('user_agent')
#     visit_time = datetime.now()

#     conn = get_db_connection()
#     if not conn:
#         return jsonify({'status': 'error', 'message': 'DB connection failed'}), 500

#     try:
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO visitors (ip, user_agent, visit_time) VALUES (?, ?, ?)
#         ''', (ip, user_agent, visit_time))
#         conn.commit()
#         return jsonify({'status': 'success'}), 201
#     except Exception as e:
#         print("Error saving visitor:", e)
#         return jsonify({'status': 'error', 'message': str(e)}), 500
#     finally:
#         conn.close()

# # API to get all visitors
# @app.route('/api/visitors', methods=['GET'])
# def get_visitors():
#     conn = get_db_connection()
#     if not conn:
#         return jsonify({'status': 'error', 'message': 'DB connection failed'}), 500

#     try:
#         cursor = conn.cursor()
#         cursor.execute('SELECT ip, user_agent, visit_time FROM visitors ORDER BY visit_time DESC')
#         rows = cursor.fetchall()
#         visitors_list = []
#         for row in rows:
#             visitors_list.append({
#                 'ip': row[0],
#                 'user_agent': row[1],
#                 'visit_time': row[2].strftime('%Y-%m-%d %H:%M:%S')
#             })
#         return jsonify(visitors_list)
#     except Exception as e:
#         print("Error fetching visitors:", e)
#         return jsonify({'status': 'error', 'message': str(e)}), 500
#     finally:
#         conn.close()

# # Optional: home route to test server running
# @app.route('/')
# def index():
#     return "Server is running. Use API endpoints to save or get visitors."

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
import pyodbc
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=MARYAMA-ABDIRAS\\SQLEXPRESS;'
            'DATABASE=GameDB;'
            'Trusted_Connection=yes;'
            'TrustServerCertificate=yes;'
        )
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None

# Save visitor info
@app.route('/api/visit', methods=['POST'])
def save_visit():
    data = request.get_json()
    ip = data.get('ip')
    user_agent = data.get('user_agent')
    visit_time = datetime.now()

    conn = get_db_connection()
    if not conn:
        return jsonify({'status': 'error', 'message': 'DB connection failed'}), 500

    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO visitors (ip, user_agent, visit_time) VALUES (?, ?, ?)
        ''', (ip, user_agent, visit_time))
        conn.commit()
        return jsonify({'status': 'success'}), 201
    except Exception as e:
        print("Error saving visitor:", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        conn.close()

# Get all visitors
@app.route('/api/visitors', methods=['GET'])
def get_visitors():
    conn = get_db_connection()
    if not conn:
        return jsonify({'status': 'error', 'message': 'DB connection failed'}), 500

    try:
        cursor = conn.cursor()
        cursor.execute('SELECT ip, user_agent, visit_time FROM visitors ORDER BY visit_time DESC')
        rows = cursor.fetchall()
        visitors_list = []
        for row in rows:
            visitors_list.append({
                'ip': row[0],
                'user_agent': row[1],
                'visit_time': row[2].strftime('%Y-%m-%d %H:%M:%S')
            })
        return jsonify(visitors_list)
    except Exception as e:
        print("Error fetching visitors:", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        conn.close()

# Save game score
@app.route('/api/game_score', methods=['POST'])
def save_game_score():
    data = request.get_json()
    player_name = data.get('player_name')
    score = data.get('score')
    play_time = datetime.now()

    conn = get_db_connection()
    if not conn:
        return jsonify({'status': 'error', 'message': 'DB connection failed'}), 500

    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO game_scores (player_name, score, play_time) VALUES (?, ?, ?)
        ''', (player_name, score, play_time))
        conn.commit()
        return jsonify({'status': 'success'}), 201
    except Exception as e:
        print("Error saving game score:", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        conn.close()

# Get all game scores
@app.route('/api/game_scores', methods=['GET'])
def get_game_scores():
    conn = get_db_connection()
    if not conn:
        return jsonify({'status': 'error', 'message': 'DB connection failed'}), 500

    try:
        cursor = conn.cursor()
        cursor.execute('SELECT player_name, score, play_time FROM game_scores ORDER BY play_time DESC')
        rows = cursor.fetchall()
        scores_list = []
        for row in rows:
            scores_list.append({
                'player_name': row[0],
                'score': row[1],
                'play_time': row[2].strftime('%Y-%m-%d %H:%M:%S')
            })
        return jsonify(scores_list)
    except Exception as e:
        print("Error fetching game scores:", e)
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
