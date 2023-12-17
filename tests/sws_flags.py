# https://ffmpeg.org/ffmpeg-scaler.html
# https://ffmpeg.org/ffmpeg-filters.html#Filtergraph-syntax-1

sws_flags = "bilinear"
nullsrc() | scale(640, 360) | nullsink()
