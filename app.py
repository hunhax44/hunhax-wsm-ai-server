from flask import Flask, jsonify, request
from argos_service import translate as argos_translate

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
def translate_text():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "JSON veri yok"
        }), 400

    text = data.get("text", "")
    source_lang = data.get("source_lang", "auto")
    target_lang = data.get("target_lang", "en")

    if not text:
        return jsonify({
            "success": False,
            "message": "Metin boş"
        }), 400


    # Auto detect şimdilik
    # Argos doğrudan kaynak dil ister.
    if source_lang == "auto":
        source_lang = "en"


    try:

        translated_text = argos_translate(
            text,
            source_lang,
            target_lang
        )


    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500



    return jsonify({
        "success": True,
        "translated_text": translated_text,
        "source_lang": source_lang,
        "target_lang": target_lang
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
