#download file
#change to gif
# install moviepy(not work with newest version pillow, need to modify the code),pillow, pygame(preview doesn't work well)
from moviepy.editor import *
import time
import os
import sys

def togif(source, starttime, endtime):
# how to use the file name just downloaded as source
#    source = sys.argv[2]
    start_time = tuple(map(lambda x:float(x), starttime.split(':')))
    end_time = tuple(map(lambda x:float(x), endtime.split(':')))
    clip = VideoFileClip(source).subclip(start_time, end_time).resize(0.3)
    print 'clip has been processed.'
    clip.write_gif('clip_'+time.strftime('%Y_%m_%d_%H_%M_%S.gif'))
    print 'clip has been saved.'

def dlvideo(url):
    url = sys.argv[1]
    os.system('rm -rf tmp')
    os.system('mkdir tmp')
    os.system('youtube-dl -o \'tmp/%(title)s.%(ext)s\' '+ url)
    print 'Video has been download.'

if __name__ == '__main__':
    dlvideo(sys.argv[1])
    for path in os.listdir('tmp'):
        p = os.path.join('tmp', path)
        print 'p:', p
        togif(p, sys.argv[2], sys.argv[3])
    os.system('rm -rf tmp')
