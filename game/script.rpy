
define config.mouse = {"default":[ ("gui/cursor.png", 1, 1) ] }

default persistent.total_play = 0
default persistent.ending_unlocked = False
default persistent.know_rumor = False

# Endings
default persistent.unlock_ending_none = False
default persistent.unlock_ending_rejected = False
default persistent.unlock_ending_bf = False
default persistent.unlock_ending_ms = False
default persistent.unlock_ending_elf = False
default persistent.unlock_ending_secret = False

init python:
    import random

    save_name = "Prologue"

    names = ["???", "Mary", "Charlotte", "Saoirse", "Daoine", "Grandma Sue", "Violet"]
    name_mc = "Short hair girl"
    name_bf = "Long hair girl"
    name_ms = name_elf = name_gr = name_lib = names[0]

    cur_ending = None
    looping = True

    know_rumor_detailed = False
    know_market = False
    know_rumor = False
    know_jewelry = False
    know_selkie = False
    know_ms_human = False
    check = [False, False, False]

    affection = {
        names[2] : 0.15,   # Mary
        names[3] : 0,   # Charlotte
        names[4] : 0,   # Saoirse
        names[0] : 0,   # To avoid bugs
        "Long hair girl" : 0   # To avoid bugs
    }

    has_item = {
        'flowers' : True,
        'necklace' : False
    }
    
    # talk sound
    def bleep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/bleep015.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=0.5)

    def confession_ending(chances=0):
        return random.choices([0, 1], weights=[1.0 - chances, chances], k=1)[0] 

define narrator = Character(callback = [name_callback, bleep], cb_name = None)

define mc = Character("[name_mc]", callback = [name_callback, bleep], cb_name = "mc", image="mc")
define bf = Character("[name_bf]", callback = [name_callback, bleep], cb_name = "bf", image="bf")
define ms = Character("[name_ms]", callback = [name_callback, bleep], cb_name = "ms", image="ms")
define elf = Character("[name_elf]", callback = [name_callback, bleep], cb_name = "e", image="elf")

# NPCs
define gr = Character("[name_gr]", callback = [name_callback, bleep], cb_name = "gr", image="gr")
define lib = Character("[name_lib]", callback = [name_callback, bleep], cb_name = "lib", image="lib")

label start:
    if persistent.unlock_ending_elf == True:
        jump ending_secret
    else:
        jump prologue