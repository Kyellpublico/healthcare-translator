from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from googletrans import Translator
from gtts import gTTS
import uuid
import os
import time  # <-- Add this for safe deletion
from starlette.requests import Request

app = FastAPI()
translator = Translator()

# Directories
audio_dir = "audio/"
os.makedirs(audio_dir, exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate/")
async def translate_text(
    text: str = Query(..., description="Text to translate"),
    src_lang: str = Query("auto", description="Source language"),
    dest_lang: str = Query("en", description="Target language")
):
    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return {"original": text, "translated": translated.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_old_audio():
    """Deletes old audio files safely by ensuring they are not in use."""
    try:
        for file in os.listdir(audio_dir):
            if file.endswith(".mp3"):
                file_path = os.path.join(audio_dir, file)

                # Wait a bit to ensure the file is fully written
                time.sleep(0.5) 

                # Ensure the file is not in use
                try:
                    os.remove(file_path)
                except PermissionError:
                    print(f"Skipping deletion, file in use: {file_path}")
    except Exception as e:
        print(f"Error deleting old audio files: {e}")

@app.get("/speak/")
async def text_to_speech(text: str, lang: str = "en"):
    try:
        delete_old_audio()  # Remove old audio files before generating a new one

        audio_path = os.path.join(audio_dir, f"{uuid.uuid4()}.mp3")
        tts = gTTS(text=text, lang=lang)
        tts.save(audio_path)

        return FileResponse(audio_path, media_type="audio/mpeg", filename="output.mp3")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
