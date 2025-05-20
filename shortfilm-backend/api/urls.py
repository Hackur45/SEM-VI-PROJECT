from django.urls import path
from . import views

urlpatterns = [
    path('generate-final-video/', views.generate_final_video),
    path('generate-video/', views.generate_video),
    path('generate-audio/', views.generate_audio),
    path('merge-audio-video/', views.merge_audio_video),
    path('merge-audios/', views.merge_audios),
    path('merge-videos/', views.merge_videos),
]
