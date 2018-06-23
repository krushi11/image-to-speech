import pyttsx;

engine = pyttsx.init();


with open('data.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

engine.say(data);

engine.runAndWait();
