from  moviepy.video.io.ffmpeg_tools import *
import sys
import os

def to_audio(source, ext, fname):
    ffmpeg_extract_audio(source, fname+'.'+ ext, bitrate=3000, fps=44100)

def dlvideo(url):
    os.system('rm -rf tmp')
    os.system('mkdir tmp')
    os.system('youtube-dl -o \'tmp/%(title)s.%(ext)s\' ' + url)
    print 'Video has been download'

if __name__ == '__main__':
    dlvideo(sys.argv[1])
    for path in os.listdir('tmp'):
        fname = path.split('.')[0]
        p = os.path.join('tmp', path)
        to_audio(p, sys.argv[2], fname)
        os.system('rm -rf tmp')

