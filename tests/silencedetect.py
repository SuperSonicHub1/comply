# https://ffmpeg.org/ffmpeg-filters.html#silencedetect
# Equivalent to silencedetect=-50dB:d=5
# silencedetect(noise="-50dB", duration=5)
silencedetect("-50dB", duration=5)
