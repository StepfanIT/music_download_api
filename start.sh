#!/bin/bash
chmod +x ffmpeg.exe ffprobe.exe
export PATH=$PWD:$PATH
uvicorn main:app --host 0.0.0.0 --port 8000
