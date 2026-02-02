layeredimage mc:
    at sprite_highlight('mc')
    always "mc_base"
    group face auto:
        attribute happy default

    group necklace auto:
        attribute main default
        attribute none:
            Null()

    group hand auto:
        attribute normal default

layeredimage bf:
    at sprite_highlight('bf')
    always "bf_base"

    group clothes auto

    group face auto:
        attribute quiet default

    group necklace auto:
        attribute n1 when day2 default
        attribute n2 when day3 default

layeredimage ms:
    at sprite_highlight('ms')
    
    group base auto:
        attribute normal default

    group face auto when normal:
        attribute quiet default
    
    group hface auto when human:
        attribute quiet default

    group necklace auto when normal:
        attribute main default
        attribute none:
            Null()

layeredimage elf:
    at sprite_highlight("elf")
    always "elf_base"

    group face auto:
        attribute quiet default
    
    group left auto:
        attribute lnormal default

    group right auto:
        attribute rnormal default

layeredimage gr:
    at sprite_highlight("gr")

    group item auto

layeredimage lib:
    at sprite_highlight("lib")
    always "lib_base"

    group face auto:
        attribute quiet default
    
    group hand auto:
        attribute normal default