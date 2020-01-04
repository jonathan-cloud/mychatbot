"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import random
import json
import boto1
import boto_words


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg').lower()

    isBored = False
    isAfraid = False
    money = False
    greet = False
    cursed = False
    isName = False

    msg = "Hey im boto type info to ask me about commands"
    animation = None

    ret = boto_words.quest(user_message)
    msg = ret[0]
    animation = ret[1]

    money = boto_words.isMoney(user_message)

    isAfraid = boto_words.afraid(user_message)

    greet = boto_words.isGreet(user_message)

    cursed = boto_words.cursing(user_message)

    isName = boto_words.naming(user_message)

    if user_message == "info":
        msg = "Ask if im afraid, about my dog, greetings, moneystuff, and if i like stuff"
    if isAfraid:
        msg = "im scaweeeeedd doe"
        animation = "afraid"
    if greet:
        msg = "Heya friend try typing info"
        animation = random.choice(boto_words.greet_animation)
    if money:
        msg = "Let's get this bread! "
        animation = "money"
    if cursed:
        msg = " hey chill out :( "
        animation = "heartbroke"
    if isName:
        msg = " hey you the man "
        animation = random.choice(boto_words.names_animation)

    if money and cursed:
        msg = "Hey!! what the crud dont swear"
    if greet and cursed:
        msg = "Hey!! what the crud dont swear"
    if isAfraid and cursed:
        msg = "Hey!! what the crud dont swear"
    if isName and cursed:
        msg = "Hey!! what the crud dont swear"

    if msg == "":
        msg = "enter your name with 'my name is' to see what we can talk about!"
        animation = "dancing"

    name_greetings = ['my name is ', "i'm ", "i am "]

    for greeting in name_greetings:
        if greeting in user_message:
            username = user_message[user_message.index(
                greeting)+len(greeting):]
            msg = "Hi,"+username + " talk to me about stuff or type info"

    likes_phrase = ['do you like ', 'do you love ']

    for likes in likes_phrase:
        if likes in user_message:
            liking = user_message[user_message.index(
                likes)+len(likes):]
            msg = "I love "+liking + "!"

    return json.dumps({"animation": animation, "msg": msg})


@route("/test", method='POST')
def test():
    user_message = request.POST.get('msg')

    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()
