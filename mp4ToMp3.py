
# Needs moviepy installed
# To install write "pip install moviepy" in your os terminal
# For moviepy docs visit: https://zulko.github.io/moviepy/index.html
from moviepy.editor import *

# Checks the file's name so it has the suffix it must have 
def checkFileTypeName(name, suffix):
    if (len(name) < 4 or not(name[-4:] == suffix)):
        name += suffix
    return name

mp4FileName = checkFileTypeName(input("Mp4 file name: "),".mp4")

sameFileNameForOutput = input("Use the same name for the mp3 file? (Y/N): ").upper()=="Y"

if (sameFileNameForOutput):
    mp3FileName = mp4FileName[:(len(mp4FileName)-3)]+"mp3"
else:
    mp3FileName = checkFileTypeName(input("Mp3 file name: "),".mp3")

# Actual file type "conversion"
mp4WithoutFrames = AudioFileClip(mp4FileName)
mp4WithoutFrames.write_audiofile(mp3FileName) 

mp4WithoutFrames.close()