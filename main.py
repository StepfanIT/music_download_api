from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os

app = FastAPI()

class VideoRequest(BaseModel):
    url: str

@app.get("/")
async def root():
    return {"message": "Server is running"}

@app.post("/download")
async def download_audio(req: VideoRequest):
    try:
        filename = "music.mp3"
        cmd = [
            "yt-dlp", "-x", "--audio-format", "mp3",
            "-o", filename, req.url
        ]
        subprocess.run(cmd, check=True)

        if os.path.exists(filename):
            with open(filename, "rb") as f:
                audio_data = f.read()
            os.remove(filename)
            return audio_data
        else:
            raise HTTPException(status_code=500, detail="Помилка обробки")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
