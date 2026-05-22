from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Vercel!"

# from app import app, db

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()  # DBファイルを作成
#     app.run(debug=True)
