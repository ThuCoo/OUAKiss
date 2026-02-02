label forest_outside_1:
    $ save_name = "Night 1 - Forest"

    play music forest
    scene forest outside night with w33
    play sound transition
    show mc worry at center, Regicide with dissolve
    mc "..."
    if know_rumor_detailed == False:
        mc scared "Why did I even go out here to begin with?"
    mc @ scared "Should I really, really continue on?"
    menu:
        "Continue" (badge="b_move"):
            mc @ scared "I've gone too far to go back!" with vpunch
            mc worry "..."
            jump forest_inside_1
        "Go back" (badge="b_move"):
            mc "U-um..."
            mc "At least I tried, that's enough..." with vpunch
            mc "...right?"
            jump end_night_1_1

label forest_inside_1:
    scene forest inside night
    play sound walk
    show mc worry cover at left, Regicide with dissolve
    pause(2.0)
    show ms none at right, Regicide with dissolve
    mc "Whoa" with vpunch
    ms "!!!" with vpunch
    play music panic
    show mc shock -cover
    menu:
        mc "W-Wait"
        "Are you the monster they're talking about?" (badge="b_talk"): 
            mc "A-Are you the monster in the town's rumor?" with vpunch
            ms @ shock "!!!!!" with vpunch
            hide ms with dissolve
            mc "N-No!" with vpunch
            mc "Please! Come back!" with vpunch
            mc "I don't mean any harm." with vpunch
            show ms at right, Regicide with dissolve
            mc worry "..."
            mc @ dizzy "That was a bit hectic."
            mc @ scared "(We're so lucky that there's no one nearby.)"
        "Stay silent" (badge="b_talk"):
            mc "..."
            ms "..."
            mc @ dizzy "(Welp, at least she doesn't run away.)"
    mc "Can I ask you some questions?"
    $ looping = True
    while looping == True:
        menu:
            "Who are you?" (badge="b_talk"):
                mc "Can you tell me who you are?"
                ms "..."
                $ check[0] = True
            "Why are you here?" (badge="b_talk"):
                mc "Can you tell me why you're here late at night?"
                ms "..."
                $ check[1] = True
            "Say something already!" (badge="b_talk"):
                mc "I really mean no harm. Can you just talk a little?"
                ms "..."
                $ check[2] = True
            "I don't think asking will do anything..." (badge="b_talk") if check == [True, True, True]:
                mc "..."
                mc @ dizzy "If we keep this up like this, nothing will come out tonight."
                mc "(Maybe I should try introducing myself first...)"
                mc happy "Hello! I'm [mc]."
                mc "Can you tell me your name?"
                ms "..."
                $ name_ms = names[3]
                ms @ talk "...[ms]"
                mc @ worry "H-huh!" with vpunch
                ms @ talk "Name...[ms]."
                mc "Hello [ms]!"

                $ affection[name_ms] = -0.05 if affection[name_ms] == 0 else 0
                $ looping = False
    
    $ looping = True
    while looping == True:
        menu:
            "Why are you here?" (badge="b_talk"):
                mc @ worry "Can you tell me why you're here late at night?"
                if persistent.unlock_ending_ms == False:
                    ms @ talk "Pretty..."
                    mc "?"
                    ms @ talk "Water...night...pretty."
                    mc "(Is she trying to say the river looks pretty at night?)"
                    hide ms
                    hide mc
                    with dissolve
                    mc "(She's not wrong for that though. The water's shining as if it's day time.)"
                    show mc at left, Regicide
                    show ms none at right, Regicide
                    with dissolve
                    mc "Well, the water is very pretty."
                else:
                    ms @ talk "...lady..."
                    mc "?"
                    ms @ talk "Wait...white...lady."
                    mc "Are you waiting for someone?"
                    ms "*Nod*"
                    mc "(Who would let a little girl waiting here at night all by herself?)"
                    mc "She must have been really important to you then."
                ms shock "!"
                mc "(By her expression, she's happy with my answer.)"
                show ms quiet
                $ affection[name_ms] -= 0.1 if affection[name_ms] > -0.3 else 0
            "About the monster" (badge="b_talk"):
                mc "(Her legs...well, what's supposed to be her legs...)"
                mc @ worry "Are you really the monster the town's been talking about?"
                ms "..."
                ms "*Nod*"
                mc "(So it's true.)"
                ms @ talk "Some...wrong."
                mc "?"
                mc "(Is she trying to say...)"
                mc "...some parts of the rumor are wrong?"
                ms @ shock "!"
                mc "(I must be correct then.)"
                $ affection[name_ms] -= 0.1 if affection[name_ms] > -0.3 else 0
            "I gotta go" (badge="b_move"):
                mc "It's getting late now. I need to go back."
                ms "..."
                mc "(She looks sad. Maybe I should say something to cheer her up before going.)"
                mc shock "I'll come back here tomorrow, so don't be sad, okay?"
                ms shock "!" with vpunch
                mc "I'll bring a gift too."
                ms "!!!" with vpunch
                mc happy "Bye for now then."
                $ looping = False
                hide ms
                show mc at center with ease
                show forest outside night with w33
                play sound transition

label end_night_1_2:
    $ save_name = "Night 1 - End"

    scene farm inside night
    show mc at center, Regicide
    with w33
    play sound transition
    mc @ dizzy "Too much stuff happened tonight."
    mc @ scared "I'll think about it tomorrow."
    mc "Let's go to sleep first."

    scene bg black with eye_close
    narrator "You went to sleep."
    narrator "You think about the \"monster\" you saw in the forest."
    narrator "You can't help but think of those stories you heard from [bf] when you were younger."
    narrator "As you slowly drift to sleep, you wonder how you can help the poor little soul, just like how the lady helps the frog-turned prince."
    mc "...my own fairy tale..."

    jump start_day_2