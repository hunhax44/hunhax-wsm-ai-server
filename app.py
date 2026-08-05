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

    text = data.get("text", "")
    source_lang = data.get("source_lang", "auto")
    target_lang = data.get("target_lang", "en")

    if not text:
        return jsonify({
            "success": False,
            "message": "Metin boş"
        }), 400

    # TEST ÇEVİRİSİ
    # Argos bağlanınca burası değişecek
    translated_text = "[ÇEVRİLDİ] " + text

    return jsonify({
        "success": True,
        "translated_text": translated_text,
        "source_lang": source_lang,
        "target_lang": target_lang
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
