label future:
    if name_bf != names[0] and name_bf != cur_ending:
        scene garage at Regicide
        show bf focus day2 at center, Regicide
        with dissolve 
        narrator "[bf]'s garage has been getting more popular lately."
        narrator "People coming to her asking for inventions that are useful but still stylish."
        narrator "Of course, she's always been talented, it's destined she would thrive no matter the circumstances."
    if name_lib != names[0] and name_lib != cur_ending:
        scene market night at Regicide
        show lib cover talk at center, Regicide
        with dissolve 
        narrator "You heard that [lib] has been working hard."
        narrator "Hard enough that she was able to provide and upgrade her library."
        narrator "More townsfolk have been coming to the library lately too."
        narrator "Maybe they want to educate themselves, who knows."
    if name_ms != names[0] and name_ms != cur_ending:
        scene forest inside night at Regicide
        with dissolve 
        narrator "As for [ms]."
        narrator "You never see her again nor do you hear her in the town's gossip."
        narrator "You thought she got captured but heard no news about it."
    if name_elf != names[0] and name_elf != cur_ending:
        scene farm outside night at Regicide
        show elf at center, Regicide
        with dissolve
        narrator "[elf]..."
        narrator "It makes your heart boil hearing her name from time to time from the radio."
        narrator "She's a big thing now, winning \"Best lead actor of the year\"."
        narrator "Even the town's talks about her even reach your farm."

    return

label ending_none:
    play music endings
    scene farm outside day at Regicide
    show mc at center, Regicide
    with w33
    narrator "It was a hard decision to make, but you decided to put all your energy to do what [name_gr] has wanted you to."
    narrator "You spent your days and nights working endlessly at the farm."
    narrator "You would talk to your friends from time to time."
    call future from _call_future

    scene farm outside day at Regicide
    with dissolve
    narrator "It's been a pleasure listening to your friends."
    narrator "However, they have been very distant as of late."
    if affection[name_bf] <= 0.3:
        narrator "To be honest, it doesn't really matter to you."
    else:
        narrator "It saddens you a little, but you have to move on."
    narrator "You need to focus on your farm, after all."

    show bg black with dissolve
    "Ending - Just Your Average Farm Simulator."
    $ persistent.unlock_ending_none = True
    $ persistent.ending_unlocked = True

    $ MainMenu(confirm=False)()

label ending_rejected:
    play music endings
    scene farm outside day at Regicide
    narrator "Being rejected, you lost the will to even go out."
    narrator "Granny knew what happened later on and went back to the farm."
    narrator "She said she has everything taken care of."
    narrator "Despite feeling bad, you cannot force yourself to take a step outside."
    show farm inside night at Regicide
    narrator "Behind shuttered walls, you hear granny talk about the others."
    call future from _call_future_1
    narrator "Hearing your grandma's words, you can't help but feel."
    narrator "If only there's a {b} better way {/b} to end all this."

    show bg black with dissolve
    "Ending - Rejected Fairytales"
    $ persistent.unlock_ending_rejected = True
    $ persistent.ending_unlocked = True

    $ MainMenu(confirm=False)()

label ending_bf:
    $ cur_ending = name_bf

    play music endings
    scene end_bf at Regicide
    with dissolve
    narrator "As you two exchange a passionate kiss, you wonder if this is what the princess in those stories feels."
    bf "You know."
    bf "You don't need to kiss the moment I accepted your confession."
    mc "...but I want to?"
    bf "Haha."
    bf "How does it feel then?"
    narrator "You think about how your lips touch each other."
    mc "Very soft..."
    bf "My, you really need to work on that."
    show bg black
    with dissolve

    narrator "You and [bf] got together afterwards."
    narrator "It was sweet at first."
    narrator "You believed this is what it feels like in those tales you've heard as a child."
    scene garage at Regicide
    show bf at center, Regicide
    with dissolve 
    narrator "[bf]'s garage got so popular, she has been busy working left and right."
    call future from _call_future_2
    narrator "Of course, you couldn't be happier."
    show bg black
    with dissolve
    narrator "But lately, along with that happiness, there is something else that you have been feeling."
    narrator "A dark, ugly feeling in your heart that arises whenever you see [bf] with others."
    narrator "That somebody would take your {b}beloved princess{/b} away."
    show mc serious at center, Regicide
    with dissolve
    mc "..."
    hide mc
    with dissolve

    narrator "You recently got yourself a little bird."
    scene end_bf_1 at Regicide
    with dissolve
    narrator "She sings sweet songs that would bring tears to your ear."
    narrator "But as all birds do, she wishes to soar through the sky."
    narrator "But let it fly, the little bird would be devoured by all kinds of beasts."
    show bg black
    narrator "That's why you cut her wings' feathers, stripping her ability to fly."
    show end_bf_2 at Regicide
    with dissolve
    narrator "Then put her inside a little, pretty cage, fitting her."
    narrator "The little bird, not understanding it yet, may fight against this."
    narrator "But she will soon know that you only think of the best for her."

    scene bg black
    with dissolve
    "Ending - Caged Bird"
    $ persistent.unlock_ending_bf = True
    $ persistent.ending_unlocked = True
    
    $ MainMenu(confirm=False)()

label ending_ms:
    $ cur_ending = name_ms

    play music endings
    scene end_ms at Regicide
    with dissolve
    narrator "As you two share a gentle kiss, you wonder if this is what the princess in those stories feels."
    narrator "You can see how [ms]'s face is slowly burning up."
    mc "Sorry, it's my first time."
    ms "!" with vpunch
    ms "Fine..."
    ms "Again...?"
    narrator "As [ms] softly guide you to another kiss."
    narrator "You can feel your hearts beating as one."
    show bg black
    with dissolve

    narrator "You and [ms] got together afterwards."
    narrator "It was sweet at first."
    narrator "You believed this is what it feels like in those tales you've heard as a child."
    call future from _call_future_3
    scene farm outside day at Regicide
    show mc at left, Regicide
    show ms human smile at right, Regicide
    with dissolve
    narrator "You and [ms] start to work together at your family's farm."
    narrator "[ms]'s trust of you grew strong enough that she lets you take care of her shedded coat whenever she appears as a human."
    narrator "But fate has its own problems."
    scene market day at Regicide
    show ms human at center
    with dissolve
    narrator "[ms]'s innocent beauty unmatched, making men and women alike flocking by her side."
    narrator "You can't help but feel worried that some of them may take advantage of her."
    
    scene bg black
    with dissolve
    narrator "So you started with small suggestions."
    narrator "Let her stay inside the house more as time passed on."
    narrator "Putting up all those rumors about bad people inside the town."
    narrator "It was for sure a success."
    narrator "Yet, as the nature of the seals, she too yearns deeply for the sea."
    show end_ms_1 at Regicide
    with dissolve
    narrator "But then, an {b}\"accident\"{/b} happened."
    show end_ms_2 at Regicide
    with dissolve
    play sound fire
    narrator "Clumsy as you are, tripping and throwing your clothes basket into the flames."
    mc "..."
    narrator "{b}One that includes her seal coat.{/b}"
    narrator "[ms] cried a lot when she knew."
    show farm inside night
    with dissolve
    narrator "She still does, but she's much more quiet and reclusive now."
    narrator "It's fine, you will continue taking care of her, until she's back to her normal self."
    narrator "After all, {b}you're bound eternally{/b}."

    scene bg black with dissolve
    "Ending - To Play Fire With Water"
    $ persistent.unlock_ending_ms = True
    $ persistent.ending_unlocked = True

    $ MainMenu(confirm=False)()

label ending_elf:
    $ cur_ending = name_elf

    play music endings
    scene end_elf at Regicide
    with dissolve
    narrator "As you fall down, you can feel all kinds of mixed emotions."
    narrator "Yet all of them nearly silenced by the sound of your heartbeats."
    elf "I knew from the start."
    elf "That you would fall for me."
    elf "After all, what you need is a princess for your fairy tale."
    elf "Despite being a side character."
    mc "!" with vpunch
    narrator "You struggle."
    elf "..."
    narrator "Tried as you may, you can feel the will to just lay there as reality hits you."
    mc "N-No!" with vpunch
    elf "In the end, you would never be happy."
    elf "But I can fix that."
    mc "!"
    elf "Be mine. Do as I said, as long as your heart's beating."
    narrator "It sounds absurd."
    narrator "And yet, you pulled [elf]'s head down."
    narrator "As you two share a rough kiss, you wonder if this is what the princess in those stories feels."
    elf "Welcome to your dream..."
    elf "Or should I say...your nightmare."

    show bg black
    with dissolve
    call future from _call_future_4

    scene farm inside night
    with dissolve
    narrator "That's all you heard from [elf], banned from the outside world."
    narrator "Kept in the house, as she became your only source of comfort."
    narrator "Lately, you have been getting obsessed with [elf]."
    narrator "You can feel the need to lock her away for seeing eyes."
    narrator "Yet the mere thought of that contradicts with doing what she told, stopping you from actually doing it."
    narrator "The overwhelming obsessive thoughts and the inability to do so eats you up every night."
    narrator "Despite that, you feel like this is where you belong."
    show bg black
    with eye_close

    "Ending - A Side Character's Tale"
    $ persistent.unlock_ending_elf = True
    $ persistent.ending_unlocked = True

    $ MainMenu(confirm=False)()

label ending_secret:
    $ save_name = "?"

    play music endings
    $ name_mc = names[1]
    scene bg black
    "..."
    show end_elf_s at Regicide
    with dissolve
    elf "..."
    mc "H-Huh?" with vpunch
    elf "Shhh..."
    while True:
        mc "(For some reason, my head feels so heavy.)"
        mc "(I can barely stay awake...)"
        menu:
            elf "Hush now. Go back to sleep."
            "Who are you?":
                elf "Who I am doesn't really matter."
                "Radio" "Breaking news!"
                "Radio" "Famous actor [names[4]] to be nominated for \"Best lead actor of the year\"."
                mc "(Is she...?)"
            "Why are you in my bed?":
                elf "Do you think people will answer if you ask that?"
                mc "Well...no."
                elf "Your stupidity never ceases to amuse me."
            "Close your eyes":
                mc "(But I still have so many questions...)"
                scene bg black with eye_close
                elf "You know."
                elf "Even if you don't remember me."
                elf "As long as that heart is beating."
                elf "You can't escape."
                elf "Both of {b}you{/b}."

                "Ending - Inescapable Dream."
                $ persistent.unlock_ending_secret = True
                $ persistent.ending_unlocked = True
                
                $ MainMenu(confirm=False)()