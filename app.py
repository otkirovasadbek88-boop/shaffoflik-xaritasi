from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)

SUPABASE_URL = "https://gtidgtyoprhyolerimjp.supabase.co"
SUPABASE_KEY = "sb_publishable_uT8TnBzoLMDutJCQuJpYZg_HUe5EAzk"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

@app.route('/')
def home():
    return jsonify({"xabar": "Shaffoflik Xaritasi API ishlayapti!"})

@app.route('/api/shikoyat', methods=['POST'])
def shikoyat_qabul():
    """Yangi shikoyat qabul qilish"""
    data = request.json
    
    viloyat = data.get('viloyat')
    tashkilot = data.get('tashkilot_nomi')
    matn = data.get('matn')
    
    if not viloyat or not tashkilot or not matn:
        return jsonify({"xato": "Majburiy maydonlar to'ldirilmagan"}), 400
    
    # Supabase ga saqlash
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/shikoyatlar",
        headers=HEADERS,
        json={
            "viloyat": viloyat,
            "tashkilot_nomi": tashkilot,
            "xodim_ismi": data.get('xodim_ismi', ''),
            "soha": data.get('soha', ''),
            "matn": matn,
            "aloqa": data.get('aloqa', ''),
            "holat": "yangi"
        }
    )
    
    if response.status_code == 201:
        return jsonify({"xabar": "Shikoyat muvaffaqiyatli qabul qilindi!"}), 201
    else:
        return jsonify({"xato": "Saqlashda xatolik"}), 500

@app.route('/api/shikoyatlar', methods=['GET'])
def shikoyatlar_royxati():
    """Barcha shikoyatlarni olish"""
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/shikoyatlar?select=*&order=created_at.desc",
        headers=HEADERS
    )
    return jsonify(response.json())

@app.route('/api/statistika', methods=['GET'])
def statistika():
    """Statistika ma'lumotlari"""
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/shikoyatlar?select=viloyat,soha,holat",
        headers=HEADERS
    )
    data = response.json()
    
    jami = len(data)
    hal_qilindi = len([s for s in data if s.get('holat') == 'hal_qilindi'])
    
    viloyatlar = {}
    sohalar = {}
    for s in data:
        v = s.get('viloyat', 'Noma\'lum')
        viloyatlar[v] = viloyatlar.get(v, 0) + 1
        so = s.get('soha', 'Noma\'lum')
        sohalar[so] = sohalar.get(so, 0) + 1
    
    return jsonify({
        "jami": jami,
        "hal_qilindi": hal_qilindi,
        "viloyatlar": viloyatlar,
        "sohalar": sohalar
    })

@app.route('/api/tashkilotlar', methods=['GET'])
def tashkilotlar():
    """Tashkilotlar ro'yxati"""
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/tashkilotlar?select=*",
        headers=HEADERS
    )
    return jsonify(response.json())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
