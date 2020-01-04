from bottle import request
import random

names = ['boto']
afraids = ['baby', 'scardy cat', 'scared']
greetings = ['hi', 'how are you' 'hello', 'hey', 'sup', 'whatsup', 'what it do']
moneyWords = ['paper', 'money', '$', 'currency', 'chedder']
curses = ['fuck', 'bitch', 'shit', 'cunt', 'assface']
questions = ['do', 'how', 'what', 'am', 'are']
info = "Ask if im afraid, if i like dogs, greetings, moneystuff, "
names_animation = ['money', 'takeoff', 'heartbroke', "inlove"]
greet_animation = ['bored', 'crying', 'dancing', 'waiting']


def isMoney(user_message):
    for moneyWord in moneyWords:
        if moneyWord in user_message:
            return True
            
    return False

def naming(user_message):
    for name in names:
        if name in user_message:
            return True

    return False

def afraid(user_message):
    for afraid in afraids:
        if afraid in user_message:
            return True
    return False

def isGreet(user_message):
    for greeting in greetings:
        if greeting in user_message:
            return True
    return False

def cursing(user_message):
    for curse in curses:
        if curse in user_message:
            return True
    return False

def quest(user_message):
   
    isQuestion = False
    

    msg=""
    animation=None

    if '?' in user_message:
        isQuestion=True

    for word in questions:
        if word in user_message:

            if 'dog' in user_message:
                animation = "dog"

                if True:
                    msg = "Yes, I have a dog."

                else:
                    msg = 'I love dogs!'

            elif True:
                if random.randrange(2) == 0:
                    msg = "Nope "
                    animation = "no"
                else:
                    msg = "Yep "
                    animation = "ok"
    return [msg,animation]




