
# 🎬 ShortFilm Backend – Django API Guide

This is the backend service for the ShortFilm Generator App. It provides APIs for generating videos and audios from a prompt, merging them, and delivering a final rendered short film. The frontend is built in Next.js and communicates with this backend.



## 📁 Project Structure



# shortfilm-backend Project Structure

shortfilm-backend/
- api/                    # Core app
  - views.py              # All API views
  - urls.py               # Route definitions
  - prompts.py            # Gemini/ChatGPT prompt splitting
  - video_generation.py   # Google VEO2 API logic
  - audio_generation.py   # ElevenLabs API logic
  - merging.py            # Merge logic (video/audio/audio+video)
  - utils.py              # File handling & helper utilities
  - constants.py          # Keys & config

- shortfilm/              # Django project files
  - settings.py
  - urls.py

- venv/                   # Virtual environment
- manage.py
- requirements.txt




## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone <repo-url>
cd shortfilm-backend
````

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

* Windows:

```bash
.\venv\Scripts\Activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install django
```

### 5. Start the project and app (if not already done)

```bash
django-admin startproject shortfilm .
python manage.py startapp api
```

---

## 🧠 Developer Responsibilities

Each teammate works on their assigned function. Use comments and code assistants to scaffold your logic.

| Developer | Task                             | File                      | Function                             |
| --------- | -------------------------------- | ------------------------- | ------------------------------------ |
| Dev A     | Merge multiple videos            | `api/merging.py`          | `merge_all_videos(video_list)`       |
| Dev B     | Merge multiple audios            | `api/merging.py`          | `merge_all_audios(audio_list)`       |
| Dev C     | Merge one video and one audio    | `api/merging.py`          | `merge_audio_video(video, audio, i)` |
| Dev D     | Generate audio from script       | `api/audio_generation.py` | `generate_audio_clip(script, idx)`   |
| Dev E     | Generate video from prompt       | `api/video_generation.py` | `generate_video_clip(prompt, idx)`   |
| Lead      | Break prompt into scenes/scripts | `api/prompts.py`          | `break_prompt_into_scenes(prompt)`   |

Support files:

* `api/utils.py`: Helper functions
* `api/constants.py`: API keys, config

---

## 🌐 API Routes

| Method | Endpoint                    | Purpose                         |
| ------ | --------------------------- | ------------------------------- |
| POST   | `/api/generate-final-video` | Full flow: prompt → final video |
| POST   | `/api/generate-video`       | Generate video for a prompt     |
| POST   | `/api/generate-audio`       | Generate audio for a script     |
| POST   | `/api/merge-audio-video`    | Merge a single audio & video    |
| POST   | `/api/merge-audios`         | Merge multiple audio clips      |
| POST   | `/api/merge-videos`         | Merge multiple video clips      |

---

## 🧪 Run the Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/api/generate-final-video/](http://127.0.0.1:8000/api/generate-final-video/)

---

## 🧾 Sample Request

POST `/api/generate-final-video`

```json
{
  "prompt": "A story about space travel and alien friendship."
}
```

Expected Response:

```json
{
  "message": "Final video generated successfully!",
  "final_video_path": "media/final_video.mp4"
}
```

---

## 🔐 API Keys

Place API keys in:

```python
# api/constants.py

VEO2_API_KEY = "your-veo2-key"
ELEVENLABS_API_KEY = "your-elevenlabs-key"
```

Avoid committing sensitive keys. Use a `.env` file and python-dotenv in production.

---

## 🔄 Final Video Flow

1. Prompt received from frontend
2. Break into multiple scenes + scripts
3. For each scene:

   * Generate video (scene prompt)
   * Generate audio (scene script)
   * Match durations
   * Merge audio & video
4. Merge all scene clips into final video
5. Return the final video file path

---

## ✍️ Add Your Logic Like This:

```python
# api/merging.py

def merge_all_videos(video_list):
    # TODO: Use ffmpeg or moviepy to merge videos
    return "media/final_video.mp4"
```

Use your IDE's assistant to help with ffmpeg or moviepy code!

---

## ✅ To Do Next

* [ ] Handle audio/video duration sync
* [ ] Add logging
* [ ] Add background processing (Celery optional)
* [ ] Add `.env` and use `python-dotenv`

---

## 🧑‍💻 Support

If you're stuck:

* Use ChatGPT or Copilot in VS Code
* Log output paths and errors to debug

Let's make something amazing 🎥🔥

```

Let me know if you want to:
- Include a badge (e.g., build passing, python version)
- Add a GitHub Actions CI file
- Upload this file automatically into your repo

Happy building!
```
