from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Deploy com Docker e GitHub Actions funcionando!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
