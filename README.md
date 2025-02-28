# Healthcare Translation Web App

A web-based prototype that provides **real-time multilingual translation** between patients and healthcare providers. This application converts spoken input into text, provides a live transcript, and offers a translated version with audio playback.

## 🚀 Features
- **Real-Time Speech Recognition**: Converts spoken input into text.
- **Text Translation**: Supports multiple languages.
- **Text-to-Speech (TTS)**: Reads the translated text aloud.
- **Mobile-First Design**: Optimized for both mobile and desktop.
- **Secure Implementation**: Includes rate limiting and error handling.
- **Automatic Audio File Deletion**: Deletes old audio files to save storage.

## 🏗️ Tech Stack
- **Backend**: FastAPI, Google Translate API, gTTS, Cryptography
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Speech Recognition**: Web Speech API / Google Speech-to-Text
- **Deployment**: Vercel / V0 / Cursor

## 📂 File Structure
```
├── main.py                # Backend API (FastAPI)
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Frontend UI
├── static/
│   ├── script.js         # JavaScript for UI interactions
├── audio/                # Generated audio files
├── README.md             # Documentation
```

## 🛠️ Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/healthcare-translator.git
cd healthcare-translator
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Server
```sh
uvicorn main:app --reload
```

### 4️⃣ Access the App
Open **http://127.0.0.1:8000/** in your browser.

## 📡 API Endpoints
### **1️⃣ Translate Text**
**POST** `/translate/`
```sh
curl -X 'POST' 'http://127.0.0.1:8000/translate/?text=Hello doctor&src_lang=en&dest_lang=es'
```
📌 **Response:**
```json
{
  "original": "Hello doctor",
  "translated": "Hola doctor"
}
```

### **2️⃣ Text-to-Speech (TTS)**
**GET** `/speak/`
```sh
curl -X 'GET' 'http://127.0.0.1:8000/speak/?text=Hola doctor&lang=es' --output translated_audio.mp3
```
🔊 **Expected Output:** A new **translated_audio.mp3** file for playback.

## 🌎 Supported Languages
- **English**
- **Spanish**
- **French**
- **German**
- **Chinese**
- **Filipino**
- **Arabic**
- **Russian**
- **Italian**
- **Portuguese**
- **Korean**
- **Japanese**
- **Hindi**
- **Turkish**

## 📖 How to Use
1. **Open the Web App**: Visit the hosted URL or run locally at `http://127.0.0.1:8000/`.
2. **Select Languages**: Choose the input (spoken) language and the output (translated) language.
3. **Speak or Type**: Use the microphone to speak or manually type the text.
4. **Get Translation**: The app will display both the original and translated text.
5. **Listen to Translation**: Click the "Speak" button to hear the translated text.
6. **Repeat as Needed**: Try different phrases or languages.

## ⚠️ Troubleshooting
- **Jinja2 Error**: Install it using `pip install jinja2`
- **Speech-to-Text Not Working**: Ensure microphone access is enabled.
- **File Permission Error on Windows**: Restart the server (`Ctrl + C` → `uvicorn main:app --reload`).

## 📌 Future Improvements
- **User Authentication** (for privacy control)
- **Real-time AI-based Medical Term Correction**
- **Expanded Language Support**

---

🔥 **Developed with FastAPI, Google Translate, and gTTS for rapid healthcare communication!**

