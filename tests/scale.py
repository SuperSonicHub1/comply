# https://ffmpeg.org/ffmpeg-filters.html#graph2dot
# Equivalent to nullsrc,scale=640:360,nullsink
# Worth considering if sinks should just be global vars
nullsrc() | scale(640, 360) | nullsink()
