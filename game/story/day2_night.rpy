label forest_outside_2_night:
    $ save_name = "Night 2 - Forest"

    play music forest
    scene forest outside night
    menu:
        "Look around." (badge="b_move") if has_item['flowers'] == True:
            narrator "You spent some time looking about the forest."
            mc @ worry "Huh?"
            mc "Such beautiful flowers."
            mc "I can use it as a gift."
            $ has_item['flowers'] = 3
            mc "These flowers should be enough."
        "Go in deeper." (badge="b_move"):
            if name_ms == names[0]:
                mc @ scared "(I-I'll be fine.)" with vpunch
                mc @ worry "(Right?)" with vpunch
            jump forest_inside_2_night

label forest_inside_2_night:
    scene forest inside night
    
    play sound walk
    show ms none at right, Regicide with dissolve
    if name_ms == names[0]:
        if persistent.unlock_ending_ms == True:
            show elf at left, Regicide with dissolve
            show mc at center, Regicide with dissolve
            if name_elf != names[0]:
                mc @ worry "(Is that...[elf]?)"
            mc @ serious "(Why are they talking late at night?)"
            play music elf
        ms @ shock "!!!" with vpunch
        mc @ shock "W-Wait-" with vpunch
        hide ms with dissolve
        show mc at right with ease
        mc @ worry "(She's gone.)"
        if persistent.unlock_ending_ms == True:
            $ looping = True
            while looping == True:
                elf @ talk "Don't you think you're invading someone's privacy here?"
                menu:
                    "Who are you?" (badge="b_talk") if name_elf == names[0]:
                        mc @ worry "Who are you?"
                        elf @ talk "You didn't even introduce yourself, yet want me to?"
                        mc @ huh"(She's right, yet I can't help but feel annoyed.)"
                        $ name_elf = names[4]
                        elf @ talk "[elf]...remember that name."
                    "Why are you here?" (badge="b_talk"):
                        mc @ worry "Why are you here?"
                    "About that monster" (badge="b_talk"):
                        mc @ worry "Is that \"monster\" the one people are talking about?"
                        elf @ talk "Stop calling her \"monster\" then maybe I'll tell you."
                        mc @ pouting "(Why is she like this?)" with vpunch
                    "Give flower" if has_item['flowers'] == True:
                        mc @ shock "(Why would I-)" with vpunch
                        elf @ talk "Before you think of giving me those flowers."
                        elf @ talk "Why would I want some flowers picking from the side without a single care in the world?"
                        mc @ huh "(I shouldn't have pulled it out.)" with vpunch
                    "I better go" (badge="b_move"):
                        elf "..."
                        mc @ scared "(I can't stand being here any longer.)"
                        mc @ pouting "(Let's get out.)"
                        jump end_night_2
        else:
            menu:
                "Go back" (badge="b_move"):
                    jump end_night_2
    else:
        if persistent.unlock_ending_ms == True:
            show mc at center, Regicide with dissolve
            show elf at left, Regicide with dissolve
            if name_elf != names[0]:
                mc @ serious "(Why is she talking to...[elf]!?)"
            else:
                $ name_elf = names[4]
                ms "[elf]...thank you."
                mc "[elf]?"
                mc @ shock "W-wait, is she the famous actor [elf]?"
            elf "..."
            mc "A-Ah" with vpunch
            mc @ scared "(She's scary.)"
            play music elf
            $ looping = True
            while looping == True:
                elf @ talk "Maybe if someone has a sense, we wouldn't be in this predicament."
                mc "(Is she trying to make me mad?)"
                menu:
                    "How have you been?" (badge="b_talk"):
                        mc @ worry "Has the day been good to you?"
                        ms @ talk "...fine."
                        mc "(Very to the point...)"
                        elf @ talk "Of course she would say \"fine\"."
                        elf @ talk "I made sure she's in the best health condition."
                        mc @ huh "O-Oh!" with vpunch
                        mc @ worry "(So [elf] was taking care of her.)"
                        mc @ serious "(...)"
                        elf @ talk "Try to ask something more useful next time."
                        mc @ worry "H-Huh" with vpunch
                        mc @ huh "(Why does she keep jabbing at me?)" with vpunch
                        $ affection[name_elf] += 0.1
                    "Stayed the whole day" (badge= "b_talk"):
                        mc @ worry "Did you spend the whole day here?"
                        elf @ talk "Why would she be staying in the cold for the whole day?"
                        ms @ talk "...stay...miss [elf]."
                        mc @ worry "I see." with vpunch
                        mc "(So she was staying with [elf].)"
                        mc @ serious "(...)"
                        elf @ talk "Try to ask something more useful next time."
                        mc @ worry "H-Huh" with vpunch
                        mc @ huh "(Why does she keep jabbing at me?)" with vpunch
                        if affection[name_ms] > 0 and affection[name_ms] < 0.5 :
                            $ affection[name_ms] += 0.05
                        elif affection[name_ms] < 0 and affection[name_ms] > -0.5:
                            $ affection[name_ms] -= 0.05
                        $ affection[name_elf] += 0.1
                    "About the gift" if has_item['flowers'] == True or has_item['necklace'] == True:
                        mc @ shock "(R-Right, I need to give her something.)" with vpunch
                        menu:
                            "Give the necklace" if has_item['necklace'] == True:
                                mc "H-Here-" with vpunch
                                show gr msnecklace at truecenter, Regicide
                                ms @ shock "!" with vpunch
                                mc "You don't have to be so surprised. I bought it in the town's market."
                                ms @ talk "P...Pretty..."
                                ms "*Shake head*"
                                ms @ talk "Ex...pen...sive" with vpunch
                                mc "Don't worry."
                                mc "I bought this because you worth every penny."
                                ms "..."
                                mc "([elf] didn't say anything.)"
                                mc @ serious "(But I can see her eye-rolling at me.)"
                                mc "(Doesn't concern me that much...)"
                                elf @ talk "Maybe try something better than buying a costly gift without knowing the receiver's preference."
                                mc "..."
                                mc @ huh "(I really should have known better.)"
                                $ affection[name_ms] *= -1
                                $ has_item['necklace'] = False
                            "Give the flower" if has_item['flowers'] == True:
                                mc "H-Here-" with vpunch
                                show gr flowers at truecenter, Regicide
                                ms @ shock "!" with vpunch
                                elf @ talk "To be giving someone dying wild flowers."
                                elf @ talk "You don't have an ounce of care for [ms], do you?"
                                mc "I just thought it fits her!" with vpunch
                                elf @ talk "And what if it doesn't."
                                mc "..."
                                elf @ talk "You are going to give it to another girl, aren't you."
                                ms @ shock "No fighting!" with vpunch
                                elf "..."
                                mc "..."
                                ms @ talk "P...Pretty..."
                                ms @ talk "Thank..."
                                if affection[name_ms] > 0:
                                    $ affection[name_ms] += 0.1
                                else:
                                    $ affection[name_ms] -= 0.1
                                $ has_item['flowers'] = False
                        $ affection[name_elf] += 0.1
                    "I better go" (badge="b_move"):
                        elf "..."
                        mc @ huh "(I can't stand being here any longer.)"
                        mc "(Let's get out.)"
                        mc @ worry "Sorry [ms], I'll come back next time."
                        mc @ serious "(Best leave those two to their own tonight.)"
                        ms "..."
                        jump end_night_2
        else:
            show mc at left, Regicide with dissolve
            ms @ talk "[mc]..."
            $ looping = True
            while looping == True:
                menu:
                    "How have you been?" (badge= "b_talk"):
                        mc @ worry "Has the day been good to you?"
                        ms @ talk "...fine."
                        mc @ huh "(Very to the point...)"
                        if affection[name_ms] > 0 and affection[name_ms] < 0.5 :
                            $ affection[name_ms] += 0.05
                        elif affection[name_ms] < 0 and affection[name_ms] > -0.5:
                            $ affection[name_ms] -= 0.05
                    "Stayed the whole day" (badge= "b_talk"):
                        mc @ worry "Did you spend the whole day here?"
                        ms @ talk "No..."
                        ms @ talk "...swim...friends."
                        mc @ worry "I see." with vpunch
                        mc "(I would love swimming around to if I have those tails.)"
                        if affection[name_ms] > 0 and affection[name_ms] < 0.5 :
                            $ affection[name_ms] += 0.05
                        elif affection[name_ms] < 0 and affection[name_ms] > -0.5:
                            $ affection[name_ms] -= 0.05
                    "About the gift" if has_item['flowers'] == True or has_item['necklace'] == True:
                        mc @ worry "What should I give [ms]?"
                        menu:
                            "Give the necklace" if has_item['necklace'] == True:
                                mc "H-Here-" with vpunch
                                show gr msnecklace at truecenter, Regicide
                                with dissolve
                                ms @ shock "!" with vpunch
                                mc @ worry "You don't have to be so surprised. I bought it in the town's market."
                                ms @ talk "P...Pretty..."
                                ms "*Shake head*"
                                ms @ talk "Ex...pen...sive" with vpunch
                                mc @ worry "Don't worry."
                                mc @ worry "I bought this because you worth every penny."
                                ms "..."
                                $ affection[name_ms] *= -1
                                $ has_item['necklace'] = False
                            "Give the flower" if has_item['flowers'] == True:
                                mc "H-Here-" with vpunch
                                show gr flowers at truecenter, Regicide
                                with dissolve
                                ms "!" with vpunch
                                mc @ worry "You don't have to be so surprised. It's just some flowers I pick up nearby."
                                ms @ talk "P...Pretty..."
                                mc @ serious "..."
                                if affection[name_ms] > 0:
                                    $ affection[name_ms] += 0.1
                                else:
                                    $ affection[name_ms] -= 0.1
                                $ has_item['flowers'] = False
                    "I gotta go" (badge= "b_move"):
                        mc happy "It's been late. I better go home soon."
                        ms "..."
                        mc @ worry "Don't worry."
                        mc "I'll be seeing you tomorrow, too."
                        ms @ smile "..."
                        mc @ worry "(That smile.)" with vpunch
                        $ affection[name_ms] += 0.1 if affection[name_ms] > 0 else -0.1 
                        jump end_night_2
            

label end_night_2:
    $ save_name = "Night 1 - End"

    scene farm inside night
    show mc at center, Regicide
    with w33
    mc "That was tiring..."
    mc @ scared cover "*Yawn*"
    mc "Better go to sleep before it's too late."
    mc "Tomorrow is a better day, I know."

    scene bg black with eye_close
    narrator "You went to sleep."
    narrator "You dream of living as a small flame."
    narrator "To some people, they may be scared of burning aflame and wrecking havoc."
    narrator "Not you though."
    narrator "You really love the warmth of fire."
    mc "..."

    jump start_day_3