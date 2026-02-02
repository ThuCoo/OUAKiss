label start_day_2:
    $ save_name = "Day 2 - Start"
    show farm inside day with eye_open
    show mc cover worry at center, Regicide with dissolve
    mc @ scared "Whoaaa..."
    mc "I can't really say if I have had a good dream or not."
    mc -cover "..."

    $ has_item['flowers'] = False
    
label farm_outside_2:
    $ save_name = "Day 2 - Farm"
    scene farm outside day
    show mc at center, Regicide
    with w33
    mc "Since I can't go back to sleep, I'll start the morning early."
    play music farm
    menu:
        "Tend to the farm":
            mc "Well, these cows and crops aren't gonna tend themselves."
            narrator "You spend the whole day tending to the farm."
            jump end_day_2
        "Talk with the mechanic." (badge="b_move"):
            mc "Hopefully she's not asleep right now."
            jump talk_garage_2
        "Walk to the town market" (badge="b_move"):
            if name_ms != names[0]:
                mc "I should go investigate more on whatever yesterday was."
            else:
                mc "Let's have a small walk down the bustling street."
            jump walk_market_2
        "Go to the forest" (badge="b_move"):
            if name_ms != names[0]:
                mc "I wonder if she's still here..."
            jump forest_outside_2_day

label talk_garage_2:
    $ save_name = "Day 2 - Garage"
    play music garage
    scene garage with w33
    show bf day2 at right, Regicide with dissolve
    if persistent.unlock_ending_bf == False:
        show mc at left, Regicide with dissolve
    else:
        show elf at left, Regicide with dissolve
        show mc at center, Regicide with dissolve
        mc worry "Who is she talking to?" with vpunch
        elf "..."
        mc @ shock "Eeek, is she looking at me?" with vpunch
        hide elf
        with dissolve
        show mc at left
        with ease
        mc "She's gone."
        show mc happy
    if name_bf != names[0]:
        bf @ happy "Oh? You really did keep up to your promise this time."
        mc @ huh "...what are you taking me for?"
        bf "Haha."
    else:
        $ name_bf = names[2]
        mc "Hi [bf]!"
        bf @ happy "Oh? Look what we have here."
    bf @ happy "I assume you have something you want to talk about?"
    $ looping = True
    while looping == True:
        menu:
            "How have you been?" (badge= "b_talk"):
                mc @ worry "[bf], how are you faring?"
                bf @ happy "Hm? Did you break the lamp I gave you?"
                mc @ scared "Of course not-" with vpunch
                bf @ happy "I'm just kidding."
                bf @ happy "Well I'm all fine and dainty if you so wish..."
                mc @ worry "(She looks like there's something more she want to talk about.)"
                menu:
                    "Is that all?" (badge="b_talk"):
                        mc @ worry "You look like there's more to it."
                        bf @ happy "Well..."
                        if persistent.unlock_ending_bf == False:
                            bf @ happy "I have been talking to someone."
                        else:
                            bf @ happy "You remember the person I was talking to, right?"
                        mc @ shock "!" with vpunch
                        bf @ smile "She was the first person that could take on all my interests."
                        mc "...I see."
                        bf @ happy "It doesn't mean I didn't have fun spending time with you dear."
                        mc @ serious "..."
                    "Let it be." (badge="b_talk") if persistent.unlock_ending_bf == False:
                        mc @ worry "(Well, if she doesn't want to talk about it she doesn't need to.)"
                        mc @ serious "..."
            "What's with the necklace?" (badge="b_talk"):
                mc @ worry "I have never seen that necklace before."
                bf @ happy "Oh this."
                if persistent.unlock_ending_bf == False:
                    bf @ smile "A kind lady gave it to me as a gift."
                else:
                    bf @ smile "The lady you just saw gave it to me while I was wandering the market last night."
                mc "..."
                mc @ serious "(She looks very happy having it.)"
            "Give her flowers" if has_item['flowers'] == True:
                mc "Hey, [bf]."
                bf @ happy "What is it, darling?"
                show gr flowers at truecenter, Regicide
                with dissolve
                mc "I saw some flowers nearby and thought it would suit you."
                bf worry "Dear..."
                bf "It's very gorgeous."
                bf "But consider trimming it and wrapping it a little before gifting it to someone, okay?"
                mc @ worry "..."
                hide gr flowers
                bf @ happy "It's still lovely though, maybe I'll put it in the vase in the living room."
                $ has_item['flowers'] = False
                $ affection[name_bf] += 0.05
            "I gotta go" (badge="b_move"):
                mc @ worry "It's late, I gotta go home."
                bf "My my, are you having a secret lover that you're hurrying to go to?"
                mc @ huh "..."
                bf @ happy "Haha, it's funny how you keep reacting like this."
                mc @ shock "I'm going now!" with vpunch
                bf @ smile "Bye then."
                $ looping = False
                hide bf with dissolve
                show mc at center with ease
    
    if name_ms != names[0]:
        mc "I promise [ms] I would buy her a gift today."
        mc worry "What should I do?"
        menu:
            "Go to the market" (badge= "b_move"):
                mc happy "Well, a promise is a promise."
                jump walk_market_2
            "Go home" (badge="b_move"):
                mc "I don't have that much money on hand."
                mc "She probably wouldn't remember about it either."
                mc @ serious "(I'm just going to {b}pick something{/b}} along the way as a gift.)"
    mc "I have a good time talking to [bf], let's head home."
    jump end_day_2

label walk_market_2:
    $ save_name = "Day 2 - Market"
    play music market
    scene market day
    show mc at center, Regicide with dissolve
    mc "{b}She{/b} should be at the library right now."
    mc scared "But just thinking about all these books..."
    if name_ms == names[0]:
        mc "(Maybe it's best if I go talk with her some other day.)"
    else:
        mc @ worry "(Maybe if I wait around a bit, she'll come out.)"
        mc @ serious "(I have some questions to ask her.)"
    show mc happy at left
    with ease
    show lib at right, Regicide
    with dissolve
    if name_lib == names[0]:
        $ name_lib = names[6]
        mc "[lib]!"
        lib @ talk "Ah, [mc]."
        lib @ talk "It's been so long seeing you here."
        mc "Grandma kept telling me to take care of the farm, it's hard going to town."
        lib @ talk "Haha, at least the farm is well taken care of."
    else:
        mc "[lib]!"
        lib "!" with vpunch
        lib @ talk "When I said it's nice to see you more often, I didn't expect it to be the day after, you know?"
        mc "Haha, I just so happen to have some time on hands."
    lib @ talk "Well, if there's anything you need, I'm all ears."
    $ looping = True
    while looping == True:
        menu:
            "How have you been?" (badge= "b_talk"):
                mc "How are you faring, [lib]?"
                lib @ talk "Well, not very well."
                mc worry "What's wrong?"
                lib @ talk "A bookshelf fell over this morning."
                mc @ shock "!" with vpunch
                lib @ talk "Luckily, it's early so nobody was in there to be worried about."
                lib @ talk "But the property damage..."
                mc "(Poor [lib]...)"
                lib @ talk "Because of that, I'm currently working part-time in a {b}jewelry store{/b} right now."
                if name_ms != names[0]:
                    mc "Huh..."
                    mc "Maybe I can {b}buy jewelry{/b} as a gift."
                    $ know_jewelry = True
            "About [elf]" (badge= "b_talk") if name_elf != names[0]:
                mc "Hey [lib], have any information on [elf]?"
                lib talk "!!!" with vpunch
                lib "Of course I do!" with vpunch
                lib "She's a famous actor."
                lib "Not only that, she has been visiting the town these past few days."
                show lib quiet
                mc "(So [lib] knows about her.)"
                mc @ worry "(What should I ask about [elf]?)"
                menu:
                    "Who is she?" (badge= "b_talk"):
                        mc "Who even is she?"
                        lib @ talk "[elf] is a famous actor who started out just recently."
                        lib @ talk "Yet all her movies are super popular and highly rated."
                        mc @ shock "Wait...{b}all of them{/b}?" with vpunch
                        lib talk "Yeah, it was as if she knew what the trends were going to be."
                        lib "Having the looks, the talents and the vision."
                        lib @ cover "She's gathered all kinds of attention, even some city higher ups are head over heels for her."
                        lib "It's true to say that she's blessed by the gods above."
                        show lib quiet
                        mc @ serious "..."
                    "Why is she here?" (badge= "b_talk"):
                        mc @ worry "Our town is not well-known at all."
                        mc @ dizzy "Why did she even go here?"
                        lib @ talk "Well, it's hard to say."
                        lib @ talk "But when interviewed for being nominated, she said she would take a break to \"finish what she's destined to\"."
                mc @ scared "T-That doesn't make anything clearer at all!" with vpunch
                lib @ talk "She's a celebrity afterall. You know how secretive they can be."
                lib @ talk cover "I'll tell you this one thing though."
                mc "!" with vpunch
                lib @ talk cover "Every night, while I was cleaning up the library."
                lib @ talk cover "I saw her going off somewhere {b}around the forest{/b}."
                mc "!!!" with vpunch
                if name_ms != names[0]:
                    mc @ serious "Is she going to [ms]?" with vpunch
            "About the monster" (badge= "b_talk") if know_rumor_detailed == True or persistent.know_rumor == True:
                mc @ worry "Did you hear any more about the rumored monster?"
                lib talk "Hmmm..."
                lib "Not that much."
                lib "Someone said that the \"monster\" has the ability to change form to a human."
                if name_ms != names[0]:
                    mc @ huh "(Well, judging from what I saw...)"
                    scene forest inside night
                    show ms at center
                    with dissolve
                    mc @ huh "(It's no surprise if she's able to do that.)"
                    hide ms
                    show market day
                    show lib quiet at right, Regicide
                    show mc at left, Regicide
                    with dissolve
                lib @ talk "How about you then?"
                mc "..."
                if name_ms != names[0]:
                    mc @ worry "I heard that the \"monster\" is an aquatic creature."
                    lib "!" with vpunch
                    mc "(That expression!)"
                    menu:
                        "Did you think of anything?" (badge= "b_talk"):
                            mc "Do you have a conclusion on what it is?"
                            lib @ talk "W-well, there could be other options." with vpunch
                            lib @ talk cover "But the first thing that came to my mind is {b}selkie{/b}."
                            mc "!" with vpunch
                            $ know_selkie = True
                        "Do nothing":
                            mc @ serious "(I better not press on it, lets I spilled out about [ms].)"
                else:
                    mc @ worry "Sorry, I didn't get to hear anything."
                    lib @ talk "It's alright."
                    lib @ talk "After all, who even knows if it was real?"
            "About selkie" (badge= "b_talk") if know_selkie == True:
                mc @ shock "Please [lib], tell me more about selkie." with vpunch
                lib "..."
                lib @ talk "Legends are told that selkie bear the power to change between forms."
                lib @ talk "Flow with the water with their kin as a seal."
                lib @ talk "Shedding their skin, putting on the facade of a human on land."
                mc @ shock "(That description!)" with vpunch
                scene forest inside night
                show ms at center
                with dissolve
                mc "(It must be what she is!)" with vpunch
                hide ms
                show market day
                show lib at right, Regicide
                show mc at left, Regicide
                with dissolve
            "About buying jewelry?" (badge= "b_talk") if know_jewelry == True:
                mc @ worry "Hey, you said that you're working in a jewelry store."
                mc @ worry "May I ask you for some advice on what to buy?"
                lib "!" with vpunch
                lib @ talk "A-are you having a lover!?" with vpunch
                mc @ huh "(Really...)"
                mc @ pouting "Just a promise with someone."
                lib @ talk "Hmm, how about this?"
                show gr msnecklace at truecenter, Regicide with dissolve
                lib @ talk "It's a cancelled order that has been in our storage for a good while now."
                lib @ talk "I'll give a discount while you're at it too."
                mc @ serious "(It's a bit pricy but...)"
                mc happy "I'll take it then."
                mc "(I'll just spare my savings this month a little...)"
                lib @ talk "Lovely."
                hide gr with dissolve
            "I gotta go" (badge= "b_move"):
                lib @ talk "Oh my, look at the time."
                lib @ talk "I need to go to my next job."
                mc @ worry "Better get going then."
                hide lib with dissolve
                show mc at center with ease
                mc @ worry "(I hope things go well with [lib])"
                $ looping = False
    jump end_day_2

label forest_outside_2_day:
    $ save_name = "Day 2 - Forest"
    play music forest
    scene forest outside day
    show mc at center, Regicide
    with w33
    $ looping = True
    while looping == True:
        menu:
            "Look around." (badge="b_move"):
                narrator "You spent some time looking about the forest."
                mc "Huh?"
                mc "(Such beautiful flowers.)"
                mc "(I can use it {b}as a gift.{/b})"
                $ has_item['flowers'] = True
                mc "These flowers should be enough."
            "Go in deeper." (badge="b_move"):
                jump forest_inside_2_day
            "Go back" (badge="b_move"):
                jump farm_outside_2

label forest_inside_2_day:
    scene forest inside day
    show mc at center, Regicide
    with w33
    if name_ms != names[0]:
        mc @ shock "(She's not here.)"
        mc @ huh "(Well, who would.)"
    else:
        mc @ shock "Since when did we have a river here?"
        mc worry "(Come to think about it.)"
        mc "(Grandma said how {b}most river goes out to the sea{/b}.)"
        mc "I wonder if this one does."
    menu:
        "Go back" (badge="b_move"):
            jump forest_outside_2_day

label end_day_2:
    $ save_name = "Day 2 - End"
    show farm outside night with w33
    show mc at center, Regicide with ease
    if name_ms == names[0]:
        mc @ cover scared "It's getting late."
        mc "Best if I go to sleep."
    else:
        mc @ serious "([ms] is waiting in the forest.)"
        mc @ worry "What should I do?"
    menu:
        "Go to the forest." (badge="b_move"):
            mc @ worry "I shouldn't keep her waiting for too long."
            jump forest_outside_2_night
        "Go to sleep" (badge="b_move"):
            mc "(Let's go to sleep.)"
            mc "I feel like tomorrow is a big day after all"
        
    show farm inside night with w33
    mc @ scared "*Yawn*"
    mc "(I have never been this exhausted.)"

    scene bg black with eye_close
    narrator "You went to sleep."
    narrator "You dream of living as a bird locked inside a cage."
    narrator "Many people would rather be able to fly high in the sky."
    narrator "Not you though."
    narrator "Why would you fly when there's food and safety in your cage."
    mc "..."

    jump start_day_3