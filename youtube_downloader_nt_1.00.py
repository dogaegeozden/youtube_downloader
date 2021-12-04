# Copyright © 2021 All rights reserved. Doga Ege Ozden
import os
from pytube import YouTube
import sys

# For illustrative purposes.
rM = 'pytube'

if rM in sys.modules:
    while True:
        try:
            question1 = str(input("Would you like to download as video or audio? (v/a): "))
            question2 = input("Enter you the url here: ")

            if question1 == "exit":
                break

            elif question1 == "v":
                yt = YouTube(f'{question2}')
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
                print(yt.title + " has been successfully downloaded.")
                break

            elif question1 == "a":
                yt = YouTube(f'{question2}')

                # extract only audio
                video = yt.streams.filter(only_audio=True).first()

                destination = os.getcwd()

                # download the file
                out_file = video.download(output_path=destination)

                # save the file
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)

                # result of success
                print(yt.title + " has been successfully downloaded.")

        except:
            print("You didn't entered a valid value. You should be entering a url as fallows: https://www.youtube.com/watch?v=htrxWYQayk0")

else:
    print(f"can't find the {rM} module")
