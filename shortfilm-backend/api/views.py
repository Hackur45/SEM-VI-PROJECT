from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .prompts import break_prompt_into_scenes
from .video_generation import generate_video_clip
from .audio_generation import generate_audio_clip
from .merging import merge_audio_video, merge_all_videos, merge_all_audios
from .utils import ensure_duration_match

@csrf_exempt
def generate_final_video(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    try:
        data = json.loads(request.body)
        main_prompt = data.get('prompt', '')

        if not main_prompt:
            return JsonResponse({'error': 'Prompt is required'}, status=400)

        # 1. Break into scenes & scripts
        scenes = break_prompt_into_scenes(main_prompt)  # returns list of {'scene_prompt': ..., 'script': ...}

        video_paths = []
        audio_paths = []
        final_clips = []

        for idx, scene in enumerate(scenes):
            scene_prompt = scene['scene_prompt']
            script = scene['script']

            # 2. Generate video + audio
            video = generate_video_clip(scene_prompt, idx)
            audio = generate_audio_clip(script, idx)

            # 3. Ensure durations are close
            video, audio = ensure_duration_match(video, audio)

            # 4. Merge audio+video
            final_clip = merge_audio_video(video, audio, idx)

            video_paths.append(video)
            audio_paths.append(audio)
            final_clips.append(final_clip)

        # 5. Merge all clips into one video
        merged_video = merge_all_videos(final_clips)

        return JsonResponse({
            'message': 'Final video generated successfully!',
            'final_video_path': merged_video,
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def generate_video(request):
    return JsonResponse({'message': 'generate-video endpoint'})

def generate_audio(request):
    return JsonResponse({'message': 'generate-audio endpoint'})

def merge_audio_video(request):
    return JsonResponse({'message': 'merge-audio-video endpoint'})

def merge_audios(request):
    return JsonResponse({'message': 'merge-audios endpoint'})

def merge_videos(request):
    return JsonResponse({'message': 'merge-videos endpoint'})
