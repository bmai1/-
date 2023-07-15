# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("anime girl")
define n = Character("")
define pov = Character("[povname]")


init python:
    def character_callback(event, **kwargs):
        if event == "end":
            renpy.music.play("audio/buttong.mp3", channel="audio")

    config.all_character_callbacks.append(character_callback)

# The game starts here.

label start:

    scene city with dissolve

    $ povname = renpy.input("Enter your name: ", length = 32).strip()
    

    play music "audio/senjo2.mp3" fadeout 1 

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg class1 with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    show senjo happy talk


    # These display lines of dialogue.

    m "\"Have a nice evening [povname]~\""

    show senjo happy

    n "We had just finished packing our bags and I was preparing to walk home when suddenly she called out to me."

    n "I remember that day clearly; the blossom of new love is not something that one experiences often."

    show senjo happy talk

    m "\"Today's a special day, y'know that?\""

    show senjo happy

    n "She had a mysterious look in her eyes that I couldn't quite decipher, and she began to giggle."

    play sound "audio/giggle.mp3"

    m "\"Tee hee!\""

    n "She actually said \"Tee hee\" out loud by way. What a weirdo..."

    n "I'm unsure of how to respond."

    pov "\"...\""

    menu:
        "What do you mean?":
            show senjo neutral
            m "\"I only mean what I mean.\""
            m "\"[povname], if you really have to ask me what I mean then maybe you didn't think hard enough to find a definitive answer.\""
            pov "\"Okay, okay, no need to lecture me...\""
            
            
        "Yeah, today's a really special day.":
            show senjo happy talk
            m "\"So you remembered!\""
            pov "\"That's right.\""
            m "\"That's quite uncharacteristic of you [povname]...\""
            pov "\"What's that supposed to mean?\""
            m "\"Nothing...\""

        "Let's have sex right now.":
            show senjo blush
            m "\"...\""
            m "\"No, you horny pervert, we're in school right now...\""
            n "Why the fuck did I even say that?"
            pov "\"...\""
            n "I sighed in exasperation, mildly disappointed at both myself and also her quick rejection."
        
    
    show senjo neutral talk
    # show senjo pose
    
    m "\"I'm going to rob a bank today.\""

    show senjo neutral

    pov "\"Right...\""

    n "For some reason, this strikes me as something she would actually do on a whim."

    pov "\"...\""

    show senjo neutral talk

    m "\"What, aren't you surprised? Not even the tiniest bit worried about me? You could've offered to lend me a hand, you know. You could be my getaway driver. Isn't that romantic?\""

    show senjo neutral

    pov "\"...\""

    menu:
        "I am not worried at all. I believe in you.":
            show senjo blush
            m "\"Aw, thanks. Doesn't mean much coming from you though.\""
            n "What a tsundere."

        "I'm kind of worried.":
            show senjo sus
            m "\"Do you not have faith in me or something?\""
            show senjo happy
            m "\"That's pretty cold-hearted of you, [povname]. I thought you were a nice guy.\""


        "I'm really worried! That sounds like an extremely bad idea.":
            show senjo sus
            m "\"You're such a chicken. You can't enjoy life if you constantly worry\""
            pov "\"I love chicken, and I love you too.\""
            show senjo neutral
            m "\"wtf dude -_- shut up\""

        "I don't worry about women.":
            show senjo sus
            n "lol"
        
    show senjo neutral talk
    
    m "\"Sigh...I'm just joking. You don't seem very amused. You actually thought I would rob a bank??\""

    show senjo neutral
    
    n "I chuckle weakly."

    pov "\"That wasn't a very funny joke. And yeah, why wouldn't you rob a bank? It's not like you're an exemplar of good behavior.\""

    show senjo happy talk

    m "\"Fuck you.\""

    show senjo sus

    pov "\"Yes, please. Also, why??\""

    m "\"...\""

    pov "\"...\""

    m "\"...\""

    m "\"I think we're getting off topic.\""

    show senjo neutral talk

    m "\"It's my birthday today.\""

    show senjo neutral

    pov "\"Really??\""

    n "I can't believe I forgot such an important event."

    n "It makes me feel kind of guilty."

    n "But I swear, I thought her birthday was in a few years or something."

    show senjo sus

    m "\"What did you think today was...Jeez, you really are dense aren't you?\""

    menu:
        "No idea.":
            show senjo neutral
            play sound "audio/sigh.mp3"
            m "\"Sigh...once again, I must remind myself to never depend on you.\""

        "I thought it was just a normal day?":
            show senjo neutral
            play sound "audio/sigh.mp3"
            m "\"Sigh...of course you did.\""
            pov "\"...\""

        "I am homosexual.":
            show senjo neutral
            play sound "audio/sigh.mp3"
            m "\"Sigh...I know.\""

    m "\"So.\""

    show senjo neutral talk

    m "\"You wanna come over to my house? My parents aren't home; they're in prison right now.\""

    show senjo neutral
    
    menu:
        "Yes.":
            m "\"Great. Shall we get going then?\""
            show senjo happy
            n "She gave me a quick smile as I reached for her hand."
            m "\"None of that naughty business. You can hold my hand when you deserve it.\""

        "No.":
            m "\"That's too bad. I'm going to kidnap you. Lol\""
            n "She pulls a syringe out of her skirt and quickly stabs you in the arm with the needle. You feel your vision getting blurry, before everything goes dark."
    
        "Are we going to have sex?":
            show senjo blush
            m "\"Well, that entirely depends on your behavior. Better be a good boy.\""
            pov "\"Fine, I'll come.\""
            m "\"Good answer.\""
    
        
    scene kitchen with dissolve
    
    play music "audio/main_theme.mp3" fadeout 1 

    n "..."
    play sound "audio/footsteps.mp3"

    show senjo neutral talk
    m "\"Here we are.\""

    show senjo neutral

    n "The sunset painted the sky in hues of fiery orange and warm yellow, casting cascades of brilliant golden rays through her semi-transparent sliding doors."

    n "I catch a lingering aroma of freshly baked bread, which was odd considering her parents were in prison, and therefore nobody could have been baking while we were at school together."

    n "She also didn't strike me as someone who would learn to bake on her own; I always thought of her as an instant ramen type of girl."

    n "This bread paradox is stressing me out. I need to get to the bottom of this."

    pov "\"Wait, I forgot to ask you this earlier, but why are your parents in prison?\""

    show senjo neutral talk

    m "\"Yeah.\""

    show senjo neutral

    m "\"...\""

    pov "\"...\""

    n "???"

    pov "\"What \"yeah\"?\""

    m "\"It is what it is.\""

    m "\"...\""

    show senjo neutral talk
    
    m "\"This is the first time you've been to my house, right?\""

    show senjo neutral

    m "\"Please take off your shoes before coming into my room.\""

    n "She gestures towards the assortment of footwear on a rack next to the door."

    n "I take off my fake Jordans and fling them onto the floor besides her slippers."

    play sound "audio/thump.mp3"

    n "They hit the floor with a sad little thump."

    show senjo happy
    
    m "\"Okay, follow me.\""

    scene room1

    play sound "audio/door.mp3"
    
    n "..."

    show senjo neutral talk at right

    m "\"You can sit on the floor, I guess.\""

    show senjo neutral

    m "\"So...I don't actually have any plans as to what we should do now.\""
    m "\"I usually don't celebrate my birthday; it seems like too much effort and it doesn't really make me happy.\""

    show senjo blush

    m "\"In other words, I used my birthday as an excuse to see you!\""

    m "\"N-not that I l-like being with you or anything...\""

    m "\"You silly b-baka...\""

    n "Since when was she such a tsundere? There seems to be some kind of tension between us."

    show senjo neutral

    m "\"I hope you don't mind coming over.\""

    pov "\"No, no, it's alright.\""

    pov "\"I didn't have any plans for today anyways.\""

    show senjo sus

    m "\"That's not exactly a nice thing to say you know.\""
    m "\"That's basically saying you're only spending time with me now because you're bored and you have nothing better to do.\""

    m "\"Like it's not really something you'd actively desire.\""

    show senjo neutral

    pov "\"Um, what are you talking about??\"" 
    pov "\"I never said I don't like being with you.\""
    pov "\"I just said I didn't have any plans for today, which is simply stating a fact.\""

    pov "\"Why are you reading so deeply into what I'm saying if I genuinely don't have any ulterior message?\""

    show senjo angry talk

    m "\"Because...I don't know, maybe cos I actually care about this kind of thing!\""

    show senjo angry

    m "\"Of course, I wouldn't want to force you to stay at my house like some sort of hostage!\""

    show senjo angry talk

    m "\"Are my feelings so unimportant to you that you think you can just disregard them?\""

    show senjo angry 
   
    m "\"Well, I'll let you know. It feels really shitty when you ignore my desires.\""

    m "\"I don't deserve to be treated like this.\""

    show senjo blush

    m "\"I only want you to enjoy my company, to spend as much time with me as humanly possible...\""

    show senjo neutral

    m "\"Its...complicated. You wouldn't understand. You're like a rock: emotionless.\""

    pov "\"Hey, I'm sorry for whatever I did wrong, but if I didn't want to be here then I would've left already.\""

    show senjo angry

    m "\"How nice.\""

    show senjo neutral

    pov "\"I phrased that poorly.\""
    pov "\"What I meant is that there's no point in worrying about this nonsense.\""

    show senjo sus

    m "\"Nonsense?\""

    pov "\"...Okay, I'll admit that also sounded somewhat accusatory.\""

    pov "\"It's kind of a bad speaking habit...\""

    show senjo neutral

    pov "\"While it's true I had no plans today, I'm glad I'm able to spend time with you right now.\"" 
    pov "\"So can we please not spend our time arguing over whether or not I want to be here with you?\""

    pov "\"Because the answer is yes.\""
    pov "\"I like you. I enjoy your company. Don't question it.\""

    show senjo neutral talk

    m "\"Okay, but what about the times when you genuinely don't want to be with me?\""

    m "\"I get that you can't always wanna spend time with me, but how can I differentiate between your moods, if you don't tell me directly what's on your mind?\""

    show senjo neutral

    m "\"Stop trying to act to mysterious or something by giving me mixed signals, it's cringe.\""

    pov "\"First of all, why would I want to be mysterious..?\""

    pov "\"I don't really have anything to hide.\""

    pov "\"Second, it'll be obvious if I don't want to spend time with you.\""

    pov "\"If I'm acting neutral, which is what I act like most of time, then it doesn't mean anything in particular.\""

    show senjo angry talk

    m "\"[povname], you really are clueless, aren't you?\""
    
    show senjo angry

    m "\"Sometimes I wonder why I even like you.\"" 

    show senjo angry talk
    
    m "\"I shouldn't have to put up with your *ahem*, \"nonsense\"."

    show senjo angry

    pov "\"Wait, you like me?\""

    show senjo angry talk

    m "\"Yes!!!\"" 

    show senjo angry
    
    m "\"You didn't realize until now?\""

    show senjo angry talk
    
    m "\"Man, I knew you were dense, but to this extent? That's worrying.\""

    show senjo angry

    pov "\"Uh...right...well, if you really like me, you'd have to put up with me a little bit.\""

    show senjo angry talk
    
    m "\"Bullshit. Be better.\""

    show senjo angry

    pov "\"Listen, I just don't feel like expressing my emotions all the time okay?\""
    
    pov "\"It's honestly exhausting.\""

    pov "\"Just focus on the present.\""

    pov "\"I didn't come over to argue with you, we both know that.\"" 
    
    pov "\"Can we just settle for a truce at this point in time?\""

    show senjo sus

    m "\"...Alright.\""

    show senjo neutral

    m "\"Tell me, what do you think we should do now then?\""

    menu:
        "We should have sex, of course.":
            stop music
            
            show senjo gun at reset
            window hide
            pov "\"W-What are you doin-\"{nw}"
            scene death
            play sound "audio/gunshot.mp3"

            
            play music "audio/ggws.mp3"
             
            n "{w}{space=625}Continue?{w=2.0}"
    
    scene room1night

    play music "audio/Negotiator.mp3"

    n "(Luckily, I'm the protagonist so I happen to immortal)"

    n "I must've been out for hours because it's now nighttime."

    n "I'm not too sure what happened after I got to her house."

    n "My head really hurts, and I feel nauseous."

    show senjo neutral with dissolve

    m "\"Hey, you.\""

    m "\"You\'re finally awake.\""

    pov "\"Wh-What do you want with me, wench?\""

    n "To (Not) Be Continued"


            



    
    # This ends the game.

    return
