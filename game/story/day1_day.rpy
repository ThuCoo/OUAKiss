label start_day_1:
    $ save_name = "Day 1 - Start"

    show bg black with w12
    play sound phone_ring
    "Ring..."
    "Ring Ring Ring..."

    $ name_mc = names[0]
    mc "Woooaaa...!" with vpunch
    play sound bedfall
    scene farm inside day
    with dissolve
    show mc cover dizzy none at center, Regicide
    with dissolve
    $ name_mc = names[1]
    mc "What a dream I had there."
    if persistent.total_play >= 2:
        mc "Hmm..."
        narrator "Your head hurts"
        if persistent.ending_unlocked:
            narrator "As if you have just gone through a long journey."
        else:
            narrator "As if you have just jumped through some timeskippers."
    play sound phone_ring
    "Ring Ring Ring..."
    mc shock "Ahhh, that must be grandma calling." with vpunch
    show mc -cover at left with ease
    show gr phone at Position(xcenter=0.75, yalign=0.5), Regicide with dissolve
    mc worry "Now how do you use this."
    play sound phone_pickup

    play music farm

    mc "Hello?"
    gr "\"My my, by the sound of your voice, did you just wake up?\""
    mc happy "Ah! Hehe..."
    $ name_gr = names[5]
    gr "\"Don't {b}hehe{/b} me young lady!\""
    gr "\"You told me that you would be waking up early to take care of the farm.\""
    mc @ shock "It's my first day! I just need a little time getting used to it." with vpunch
    gr "\"Really...\""
    mc "Why did you even call me anyways?"
    gr "\"Oh right!\""
    gr "\"I want to give you something.\""
    mc shock "!?"
    gr "\"On the left where you're standing, there must be a box.\""
    gr box "\"That's for you. Open it.\"" with w12

    show gr necklace with dissolve
    show mc shock at left with ease
    mc worry @ cover "Whoa..."
    mc @ happy "It's so pretty..."
    gr "\"It's our family heirloom.\""
    mc @ shock "!"
    gr "\"It's told to help guiding your fate.\""
    mc "Granny..."
    mc "But I'm..."
    gr "\"Did I hear a {b}sniffle{/b}? I thought a certain young lady said she's {b}too old for crying{/b}.\""
    mc shock "O-Of course not!" with vpunch
    mc happy "...thank you."
    gr phone "\"...\"" with w12
    gr "\"Now now, off you go. If we keep talking any longer, the kids are going to starve to death.\""
    mc "Haha"
    mc "Bye then Granny."
    play sound phone_pickup
    hide gr with dissolve
    show mc at center with ease

    if persistent.ending_unlocked == True:
        narrator "Breaking news!"
        mc "Whoa!!!" with vpunch
        show mc at left with ease
        show gr radio at Position(xcenter=0.75, yalign=0.5), Regicide with dissolve
        narrator "Famous actor [names[4]] to be nominated for \"Best lead actor of the year\"."
        mc "{b}[names[4]]{/b}, huh...?"
        mc "Wait, since when did the radio work?"
        hide gr with dissolve
        show mc at center with ease

    mc "Well then, I better head out for some work."

label farm_outside_1:
    $ save_name = "Day 1 - Farm"

    scene farm outside day with w33
    play sound transition
    pause(1.0)
    show mc worry at center, Regicide with dissolve
    mc "Hmmm, what should I do ?"
    menu:
        "Tend the farm":
            mc happy "I mustn't let grandma worry about our farm."
            narrator "You spend the whole day tending to the farm."
            jump end_day_1
        "Go to nearby garage" (badge= "b_move"):
            mc happy "I wonder what she's doing right now."
            jump talk_garage_1
        "Go to town market" (badge= "b_move"):
            mc happy "Well, I have too many products on hand."
            mc "Let's go sell some of them!"
            jump walk_market_1
    
label talk_garage_1:
    $ save_name = "Day 1 - Garage"

    play music garage
    scene garage with w33
    play sound transition
    show bf focus at center, Regicide with dissolve
    pause(0.5)
    show bf quiet
    $ name_bf = names[0]
    bf @ happy "Oh?"
    show mc at left, Regicide with easeinleft
    show bf at right with ease
    bf @ happy "Look what we have here."
    $ name_bf = names[2]
    mc "Hello [bf]!"
    mc "(This is [bf], a childhood friend of mine.)"
    mc "(She really like being pretty, so much that being a mechanic doesn't stop her.)"
    $ looping = True
    bf @ happy "How may I help you now, sweet dearie?"
    while looping == True:
        menu:
            "How have you been?" (badge= "b_talk"):
                mc @ worry "How have you been doing, [bf]?"
                bf @ happy "My my, are you worrying about me?"
                mc huh "..."
                bf @ happy "Haha, look at your face."
                mc @ pouting "Well you're just the same as ever then."
                bf @ happy "And by your face, same to you too."
                show mc happy

                $ affection[name_bf] += 0.05 if affection[name_bf] < 0.3 else 0
            "Anything interesting?" (badge= "b_talk"):
                mc @ worry  "Have you heard anything interesting lately?"
                bf happy "Hmm..."
                bf "I have been too busy lately to hear around."
                bf "But there has been a rumor gathering around in the {b}town market{/b}."
                bf "You should go check it out!"
                $ know_market = True
                show bf quiet
                mc "(Well, I may still have some time on hands.)"

                $ affection[name_bf] += 0.05 if affection[name_bf] < 0.3 else 0
            "I gotta go" (badge="b_move"):
                mc "It's late, I gotta go home."
                bf happy "Hmmm, really?"
                bf "Well, they always said time flies when you are with who you like."
                bf "Bye bye."
                show bf quiet
                
                $ affection[name_bf] += 0.05
                $ looping = False
                hide bf with dissolve
                show mc at center with easeinleft
    
    if know_market == True:
        mc worry "I just learnt that there's a rumor going on in the market nearby."
        mc "What should I do?"
        menu:
            "Go to the market" (badge= "b_move"):
                mc happy "There's still time, let's go to the market!"
                jump walk_market_1
            "Go home" (badge="b_move"):
                mc "It's too late now, I shouldn't go."
    mc "It's been good talking to [bf], let's head home."
    jump end_day_1

label walk_market_1:
    $ save_name = "Day 1 - Market"

    play music market
    scene market day with w33
    play sound transition
    show mc worry cover at center, Regicide with dissolve
    mc "Whoaaaa..."
    mc dizzy "I can never get used to how busy it is!"
    show lib at right, Regicide with easeinright
    mc -cover "!!!" with vpunch
    lib talk "I'M SO SORR-" with vpunch
    lib "Wait!"
    lib "[mc]!!!???" with vpunch
    mc shock "[lib]!"
    show mc at left, Regicide with ease
    show lib quiet
    $ name_lib = names[6]
    mc happy "How long has it been, [lib]!"
    mc "(This is [lib]. She works in the nearby library.)"
    mc "(Since she like to be in the library surrounded by books and I can't really stand them,
        we never get to see each other that often.)"
    $ looping = True
    while looping == True:
        menu:
            "How are you doing" (badge= "b_talk"):
                mc @ worry "[lib], how are you these days?"
                lib @ talk "Well, you know.\n
                    Same old same old."
                mc @ worry "Now that I think about it."
                mc @ worry "Don't you always stay in the library.\n
                    Why are you out here ?"
                lib "..."
                lib talk "There have been so few people coming to the library lately."
                lib "It's hard to make enough money to keep it up."
                lib "I've been running errands left and right trying to get some coins."
                show lib quiet
                mc @ worry "..."
                mc @ worry "(Poor [lib]...)"
            "Anything interesting?" (badge= "b_talk"):
                mc @ worry "Have you heard anything interesting lately?"
                lib talk "Well, there has been tons of gossip here and there."
                lib "But nothing particular to focus on."
                lib "Well, except..."
                show lib quiet
                mc worry "Except?"
                lib @ cover talk "The {b}rumor{/b}."
                mc shock "!" with vpunch
                $ know_rumor = True
            "About the rumor" (badge= "b_talk") if know_rumor == True:
                mc @ shock "[lib], can you tell me more about the rumor?" with vpunch
                lib "..."
                lib talk "There has been talks lately that {b}deep in the forest{/b}..."
                lib "...lies a {b}monster{/b}."
                lib "\"Once in a {b}red{/b} moon. It would only show itself to those it has taken a liking to.\""
                lib "\"And when you meet it, fulfill its needs..."
                lib "...and all your {b}wishes{/b} will come true.\""
                lib "\"But failed to do it..."
                lib "...would {b}cease you from this land{/b}.\""
                mc @ shock "!!!" with vpunch
                mc "Is it really true?"
                lib talk -cover "Well, it's been the most popular talk lately."
                lib "But no one has yet to see the monster in its full glory."
                show lib quiet
                mc worry "..."
                $ persistent.know_rumor = True
                $ know_rumor_detailed = True
            "I gotta go" (badge="b_move"):
                mc @ happy "It's been fun talking to you."
                lib @ talk "Well we don't really get to talk like this often due to how far your farm is."
                mc happy "Haha."
                mc "Maybe I'll visit more often."
                lib @ talk "That's lovely to hear!"
                hide lib with dissolve
                show mc at center with ease
                $ looping = False
    jump end_day_1

label end_day_1:
    $ save_name = "Day 1 - End"

    scene farm outside night with w33
    play sound transition
    show mc worry at center, Regicide with dissolve
    mc "Hmmm..."
    if know_rumor_detailed == True or persistent.know_rumor == True:
        if know_rumor_detailed == True:
            mc "(The {b}rumor{/b})."
        elif persistent.know_rumor == True:
            narrator "You have the feelings that there's something going on in the forest."
        mc "(Should I go see if it's true?)"
        menu:
            "Investigate the forest" (badge="b_move"):
                mc scared "Well, I'm just gonna take a quick peek if it's real." with vpunch
                mc "(Promise!)" with vpunch
                jump forest_outside_1
            "Go to sleep":
                mc "Let's not."
                mc "(Granny said not to go out when it's night afterall.)"
    
    show farm inside night with w33
    play sound transition
    mc "(It's been a long day.)"
    mc -worry "I should go to sleep."

label end_night_1_1:
    scene bg black with eye_close
    narrator "You went to sleep."
    narrator "You feel like you should have done something."
    narrator "That you didn't."
    narrator "Hey, maybe it's best if you don't try to do what is far beyond reach."

    jump start_day_2