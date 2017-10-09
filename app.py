import time
from webwhatsapi import WhatsAPIDriver
driver = WhatsAPIDriver("hvamsi")
driver.view_unread()
print "bot started"
import random

class insultGenerator(object):
    def __init__(self):
        # setup the lists of insult fodder

        self.nounList = ['loser',
                         'jerk',
                         'nerd',
                         'doodie head',
                         'butthead',
                         'bonehead',
                         'dunce',
                         'moron',
                         'nerf herder']
        self.adjectiveList = ['smelly',
                              'ugly',
                              'gimpy',
                              'slimy',
                              'crabby',
                              'scabby',
                              'scratchy']
        self.connectorList = ['are one',
                              'are the biggest',
                              'are becoming a']
    def getInsult(self):
        insult = "you"

        # connector phrase
        connector = random.randint(1, len(self.connectorList))
        insult += " " + self.connectorList[connector-1]

        # adjectives
        adjCount = random.randint(2,4)
        random.shuffle(self.adjectiveList)
        for i in xrange(0,adjCount):
            if i != 0:
                insult += ", "

            else:
                insult += " "
            insult += self.adjectiveList[i]

        # ending noun
        noun = random.randint(1,len(self.nounList))
        insult += " " + self.nounList[noun-1]
        return insult
while True:
	time.sleep(10)
	print('checking for more messages')
	for contact in driver.view_unread():
		for message in contact[u'messages']:
			print(contact[u'id'],message[u'message'])
			if(contact[u'id'] == u'919742577569-1490841165@g.us'):
				ig = insultGenerator()
				driver.send_to_whatsapp_id(contact[u'id'],ig.getInsult())