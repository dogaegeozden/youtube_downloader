# Copyright © 2021 All rights reserved. Doga Ege Ozden

# Modules and Libraries
import os
from pytube import YouTube
import sys
import getpass
import time

# The required module
rM = 'pytube'

# Operating system check
if os.name == "nt":

    # Get username
    userN = getpass.getuser()

    # Check if required module is in system modules
    if rM in sys.modules:
        os.system("cls")

        # ASCII art by https://onlineasciitools.com/convert-text-to-ascii-art
        print("""__  __           ______      __            ____                      __                __
\ \/ /___  __  _/_  __/_  __/ /_  ___     / __ \____ _      ______  / /___  ____ _____/ /__  _____
 \  / __ \/ / / // / / / / / __ \/ _ \   / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/
 / / /_/ / /_/ // / / /_/ / /_/ /  __/  / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /
/_/\____/\__,_//_/  \__,_/_.___/\___/  /_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/
                                                                                                  """)

        print(f'Welcome to youtube downloader.\n')
        # Sleep
        time.sleep(0.2)

        while True:
            try:
                # Media type question
                question1 = str(input("Would you like to download video or audio? (v/a): "))

                # Url input
                question2 = input("Enter you the url here: ")

                # Break statement
                if question1 == "exit":
                    break

                elif question1.lower().strip() == "v" or question1.lower().strip() == "video":
                    # Destionation path for videos
                    dest = f'C:\\Users\\{userN}\\Videos'

                    # Content Selection
                    yt = YouTube(f'{question2}')
                    
                    # Filtering
                    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=dest)
                    
                    # Success Message
                    print(f'{yt.title} has been successfully downloaded to your Videos folder.')

                elif question1 == "a":
                    # Destionation path for musics
                    dest = f'C:\\Users\\{userN}\\Music'

                    # Content Selection
                    yt = YouTube(f'{question2}')

                    # extract only audio
                    video = yt.streams.filter(only_audio=True).first()

                    # download the file
                    out_file = video.download(output_path=dest)

                    # save the file
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)

                    # Success Message
                    print(f'{yt.title} has been successfully downloaded to your Music folder.')

            except:
                print("You didn't entered a valid value. You should be entering a url as fallows: https://www.youtube.com/watch?v=htrxWYQayk0")

    else:
        print(f"YouTube downloader can't find the {rM} module.")

else:
    print("This release is designed for Windows users.")
