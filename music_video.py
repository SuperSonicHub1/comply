# This script assumes that your first input is an image
# and that the second is your audio file
# color=c=black:s=1280x720:r=5

# How do I pass text to this?
# Song, album, artist

# Background
color(color="black", size="hd1080", rate="ntsc") >> { background }
{ "0:v" } >> scale(width="1920", height="-1") | boxblur(10) >> { img_background }
# Center image over background
{ background, img_background } >> overlay("(main_w-overlay_w)/2", "(main_h-overlay_h)/2") >> { full_background }

# Album cover
{ "0:v" } >> scale(width="-1", height=500) >> { cover }

# All together now
{ full_background, cover } >> overlay(100, 100) >> { outv }
