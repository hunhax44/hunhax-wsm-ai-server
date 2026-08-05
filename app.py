from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "name": "WSM AI Server",
        "status": "online",
        "version": "1.0.0"
    })

@app.get("/health")
def health():
    return jsonify({
        "status": "ok"
    })

@app.get("/languages")
def languages():
    return jsonify([
        {"code": "tr", "name": "Türkçe"},
        {"code": "en", "name": "English"}
    ])

@app.post("/translate")
def translate():
    data = request.get_json()

    return jsonify({
        "success": True,
        "message": "API çalışıyor.",
        "received": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
