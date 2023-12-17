# https://ffmpeg.org/ffmpeg-filters.html#Examples-89
# Equivalent to:
# nullsrc=size=200x100 [background];
# [0:v] setpts=PTS-STARTPTS, scale=100x100 [left];
# [1:v] setpts=PTS-STARTPTS, scale=100x100 [right];
# [background][left]       overlay=shortest=1       [background_and_left];
# [background_and_left][right] overlay=shortest=1:x=100 [left_and_right]

nullsrc(size="200x100") >> { background }
{ "0:v" } >> setpts('PTS-STARTPTS') | scale("100x100") >> { left }
{ "1:v" } >> setpts('PTS-STARTPTS') | scale("100x100") >> { right }
{ background, left } >> overlay(shortest=1) >> { background_and_left }
{ background_and_left, right } >> overlay(shortest=1, x=100) >> { left_and_right }
