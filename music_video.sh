python -m comply -i music_video.py -o music_video.ff || exit 1
ffmpeg -hide_banner -y -i album_art.jpg -filter_complex_script music_video.ff -map [outv] -t 5 test.mp4
