from flask import Flask, request, jsonify 
from flask_cors import CORS

app = Flask(__name__)
CORS= CORS(app, origins="*") #אבטחה

@app.route('/api/users', methods=['GET'])
def users():
    #פעולת אינטרקציה עם בסיס הנתונים שמחזיר את הנתונים שביקשתי
    #עשיתי אינטרקציה וקיבלתי מידע מהבסיס נתונים
    return jsonify({
        "users": [
    {"id": 1, "name": "john", "age":80},
    {"id": 2, "name": "rotem", "age":24},
    {"id": 3, "name": "gila", "age":32},
    {"id": 4, "name": "mimi", "age":54},
    {"id": 5, "name": "tori", "age":43} 
    ] 
})
           


if __name__ == "__main__":
    app.run(port=8090) #הפורט שממנו יפעל 
