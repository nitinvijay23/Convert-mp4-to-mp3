
# coding: utf-8

# In[ ]:

import moviepy.editor as mp
video = mp.VideoFileClip("SampleVideo.mp4")
video.audio.write_audiofile("SampleAudio.mp3")


# In[ ]:

get_ipython().system('jupyter nbconvert --to script mp4-to-mp3-convertor.ipynb')


# In[ ]:



