# https://ffmpeg.org/ffmpeg-filters.html#Filtergraph-syntax-1
# Equivalent to: nullsrc, split[L1], [L2]overlay, nullsink

nullsrc() | split() >> {L1} | {L2} >> overlay() | nullsink()
