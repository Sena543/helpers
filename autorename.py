import os

print('Please make sure script file is folder level above video files and all srt file are in the same folder as the videos.')
file_path = input('Enter folder name:')
fileNames = os.listdir(file_path)
srtFiles = []
vidFiles = []


def splitFilesInFolderToArray(srt_files=None, vid_files=None):
    if srt_files is None or vid_files is None:
        return

    for el in fileNames:
        if el.endswith('.srt'):
            srt_files.append(el)
        else:
            vid_files.append(el)
    return srt_files, vid_files

def renameFiles():
    (srt_Files, vid_Files) = splitFilesInFolderToArray(srtFiles, vidFiles)
    print(srt_Files)
    for srt, vid in zip(srt_Files, vid_Files):
        os.rename(os.path.join(os.getcwd(), file_path, srt),
                  os.path.join(os.getcwd(), file_path, vid.replace('.mkv', '.srt')))
    return


if __name__ == "__main__":
    renameFiles()
    # pass
