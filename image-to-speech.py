from image_to_text.main import *
from text_to_speech.main_gtts import *
import sys

image_path = '/home/krushi/thgit/image-to-speech/' + sys.argv[1]
text_path = '/home/krushi/thgit/image-to-speech/output.txt'
load_image(image_path, text_path)
read(text_path)
