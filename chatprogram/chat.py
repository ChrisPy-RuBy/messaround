# based on the raspberry pi exercise
# a simple internet-chat application

import network
import sys

def heard(phrase):
    print("them:" + phrase)

if(len(sys.argv) >= 2):
    print('connected !!')
    network.call(sys.argv[1], whenHearCall=heard)
else:
    network.wait(whenHearCall=heard)

counter = 0 
while network.isConnected():
    phrase = raw_input()
    print('me {}: {}'.format(counter, phrase))
    network.say(phrase)
    counter += 1




