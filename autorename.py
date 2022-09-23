import os

print('Please make sure script file is folder level above video files and all srt file are in the same folder as the videos.')
file_path = input('Enter folder name:')
# file_path = "Ozark.S01.COMPLETE.720p.NF.WEBRip.x264-GalaxyTV[TGx]/"
# print(os.getcwd())
fileNames = [names for _, __, names in os.walk(file_path)][0]
srtFiles, vidFiles = fileNames[: len(
    fileNames)//2], fileNames[len(fileNames)//2:]
print(srtFiles)
print("============")
print(vidFiles)
for _, __, files in os.walk(file_path):
    for index, name in enumerate(files, start=0):
        if name.endswith('.srt'):
            os.rename(os.path.join(os.getcwd(), file_path, name),
                      os.path.join(os.getcwd(), file_path, vidFiles[index].replace('.mkv', '.srt')))
