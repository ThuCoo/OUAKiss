

label start_day_3:
    $ save_name = "Day 3 - Start"
    show farm inside day with eye_open
    show mc at center, Regicide with dissolve
    mc @ worry "..."
    mc "I feel like today it's an important day!"
    mc "I should get ready."
    play music farm
    
label farm_outside_3:
    $ save_name = "Day 3 - Farm"
    scene farm outside day with w33
    show mc at center, Regicide with dissolve
    mc "The sun's shining and the birds are singing."
    mc "My instinct must be right."
    mc "Now..."
    menu:
        mc "What should I do?."
        "Tend to the farm":
            mc "I kinda understand why granny kept staying here taking care of the farm."
            narrator "You spend the whole day tending to the farm."
            jump ending_none
        "Talk with the mechanic." (badge="b_move"):
            mc "I wonder what she's tinkering this time."
            jump talk_garage_3
        "Walk to the town market" (badge="b_move") if know_ms_human == False:
            mc "Let's have a walk around the market before I start the day!"
            jump walk_market_3
        "Go to the forest" (badge="b_move") if know_ms_human == True:
            mc @ worry "She is still waiting for me there."
            mc "Let's go quick."
            jump forest_outside_3_day

label talk_garage_3:
    $ save_name = "Day 3 - Garage"
    scene garage
    play music garage
    show mc at left, Regicide with dissolve
    show bf day3 focus at right, Regicide with dissolve
    $ looping = True
    while looping == True:
        mc @ worry "Looks like she's busy fixing something."
        mc @ worry "What should I do?"
        menu:
            "Confess" (badge="b_talk") if name_bf != names[0]:
                mc @ serious "(Am I sure to confess my love to [bf]?)"
                menu:
                    "Yes" (badge= "b_talk"):
                        mc @ worry "[bf]!"
                        bf @ worry "Huh, dear?"
                        mc @ worry "I want to say."
                        mc @ worry "You have been a great friend to me."
                        mc @ worry "And that I think I have fallen for you."
                        $ result = confession_ending(affection[name_bf])
                        if result == 1:
                            bf @ worry "You know."
                            bf @ worry "I thought you would confess somewhere more romantic."
                            mc @ worry "Are you rejecting me?"
                            bf @ smile "Who's saying I am, dear?"
                            narrator "She said, as she pulled you towards her."
                            jump ending_bf
                        else:
                            bf "..."
                            bf @ worry "Sorry, darling. Even though I love you alot."
                            bf @ worry "I think it's best if we stay as friends."
                            mc @ worry "Ah...How straight forward."
                            narrator "That's what you liked about [bf]."
                            narrator "Yet now it's killing you from the inside."
                            mc @ serious "..."
                            jump ending_rejected
                    "No":
                        mc @ serious "(I should take a step back and reconsider.)"
            "I gotta go" (badge= "b_move"):
                mc "It's best I leave her alone doing...whatever she's doing."
                $ looping = False
                jump farm_outside_3
    return

label walk_market_3:
    $ save_name = "Day 3 - Market"
    play music market
    scene market day
    play sound crowd
    show mc at left, Regicide with dissolve
    mc @ dizzy "What's with all these commotions?" with vpunch
    show lib at right, Regicide with dissolve
    lib @ talk "[mc]!"
    $ name_lib = names[6]
    mc "Did you know why it's so noisy today, [lib]?"
    lib @ talk "Yes, actually."
    lib @ talk "Look over there!" with vpunch
    play music panic
    if name_ms != names[0] and affection[name_ms] > 0:
        show ms human at center, Regicide with dissolve
        mc shock "!!!" with vpunch
        lib @ talk "You know her, [mc]?"
        ms "..."
        ms @ shock "!!!" with vpunch
        mc @ serious "(Did she notice me?)"
        hide ms with dissolve
    else:
        show elf at center, Regicide with dissolve
        mc serious "!!!" with vpunch
        lib @ talk "She sure is popular."
        elf "..."
        mc @ scared "(D-Did she just look at me?)" with vpunch
        hide elf with dissolve
        if name_elf == names[0]:
            stop music
            lib @ talk "Welp, she's gone all right."
            lib @ talk "How do you feel?"
            mc @ worry "She's scary..."
            lib @ talk "Haha, too intimidated?"
            mc @ worry "Yea..."
            mc @ dizzy "I think the market is too much for me."
            mc @ worry "Best I stick to the farm."
            lib @ talk "..."
            lib @ talk "Bye then, take care of yourself."
            jump ending_none
    lib @ talk "And she's gone."
    mc "(Why do I feel like I know where she's going.)"
    mc @ worry "Sorry [lib], I just realised I forgot to do something."
    lib @ talk "Oh? Going so soon?"
    lib @ talk "Well, take care then."
    $ know_ms_human = True
    jump forest_outside_3_day

label forest_outside_3_day:
    $ save_name = "Day 3 - Forest"
    play music forest
    scene forest outside day
    show mc at center, Regicide with dissolve
    mc @ dizzy "(I'm so tired...)" with vpunch
    mc @ scared "(Having to run around to confuse all those townsfolk was not on my checklist today.)"
    mc @ serious "..."
    mc "(She must be inside.)"
    $ looping = True
    while looping == True:
        menu:
            "Go in deeper." (badge="b_move") if name_ms != names[0] or name_elf != names[0]:
                mc @ shock "She must be by the river." with vpunch
                jump forest_inside_3_day
            "Look around." (badge="b_move"):
                mc "What's there to be looking around for?"
                mc @ scared "I don't have time for this."
            "Go back" (badge="b_move"):
                mc @ dizzy "I need a little breather first."
                jump farm_outside_3

label forest_inside_3_day:
    scene forest inside day
    if persistent.ending_unlocked == False:
        show mc at center, Regicide
        with dissolve
        mc @ worry  "I should have guessed she'd hidden away."
        mc "(Guess I'll wait until it's night time.)"

        show mc at left with ease
        show forest inside night
        show ms at right, Regicide
        with dissolve

        ms @ shock "!" with vpunch
        mc @ worry "Don't worry, it's me."
        mc @ worry "I made sure nobody was following us."
        ms "..."
        mc "(What should I do?)"
        $ looping = True
        while looping == True:
            menu:
                "Why were you at the market?" (badge= "b_talk") if affection[name_ms] > 0:
                    mc @ worry "[ms], why were you at the market today?"
                    mc @ worry "What if someone found out who you are?"
                    ms "..."
                    mc "(She looks so sad, but I've got to tell her lets she's got kidnapped and sold, rare as she is.)"
                    ms @ talk "...gift."
                    mc "?"
                    ms @ talk "Buy...gift...[mc]."
                    mc @ cover worry "Were you trying to buy gifts for me?"
                    ms "*Nod*"
                    mc "Thank you so much."
                    mc @ worry "But I would like you being safe and sound to be a better gift."
                    ms @ talk "...why?"
                    mc @ worry "Cuz I care a lot about you."
                    ms "..."
                    $ affection[name_ms] += 0.1 if affection[name_ms] <= 0.7 else 0 
                "Confess" (badge= "b_talk"):
                    mc "(Am I sure to confess my love to [ms]?)"
                    menu:
                        "Yes" (badge= "b_talk"):
                            mc @ scared "I want to say."
                            mc @ worry "You have been a great friend to me."
                            mc "And that I think I have fallen for you."
                            $ result = confession_ending(affection[name_bf])
                            if result == 1:
                                ms "..."
                                narrator "Just as you were starting to suspect that she would decline."
                                narrator "A reply sent to your confession, not in words but in a pull from [ms]."
                                jump ending_ms
                            else:
                                ms @ shock "N-No!" with vpunch
                                ms @ talk "...sorry..." 
                                hide ms
                                with dissolve
                                mc @ shock "W-Wait!" with vpunch
                                mc @ worry "She's gone..."
                                narrator "You tried your best to compose yourself."
                                mc @ serious "..."
                                jump ending_rejected
                        "No":
                            mc "(I should take a step back and reconsider.)"
                "I gotta go" (badge= "b_move"):
                    mc @ worry "I need to do something."
                    mc @ worry "Can you wait for me a little?"
                    ms "Wait...soon."
                    mc "I will be back quickly."
                    jump farm_outside_3
    else:
        show elf at right, Regicide with dissolve
        show mc at left, Regicide with dissolve
        if name_ms != names[0]:
            mc @ shock "(W-Why is {b}she{/b} here?)"
            elf @ talk "If you're asking about [ms], she's already left."
            mc serious"!!!" with vpunch
        else:
            mc @ serious "(She really is here...)" with vpunch
            elf "..."
        if affection[name_elf] >= 0.3 or affection[name_bf] >= 0.5 or affection[name_ms] >= 0.5:
            mc @ worry "Why are you doing this?" with vpunch
            elf "..."
            mc @ worry "Are you trying to steal my fairy tale away from me!?" with vpunch
            elf @ talk "...shouldn't {b}you{/b} look at yourself first?"
            elf @ talk "Messing with the time for your own selfish gains."
            mc @ worry "Stop getting off the track!" with vpunch
            elf @ talk "Blinded by your own delusion, or better yet..."
            elf @ talk "You never tried to change."
            mc "..."
            elf @ talk "In the end, all you do is hurt people believing in you."
            mc @ shock "!" with vpunch
            jump ending_elf
        else:
            mc "..."
            mc @ worry "I should have just focused on the farm."
            elf @ talk "It's in everybody's best interest if you stay up there."
            narrator "You wanted to argue, but decided best not to."
            narrator "You already wasted too much time here."
            mc "..."
            jump ending_none