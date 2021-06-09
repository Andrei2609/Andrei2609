
label school_hall_l5:
    show screen Actor1("l5", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "P")
    with fondu
    l5 "Qu'est-ce que tu veux Puanteur ?"
    show screen Actor1("l5", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "")
    with fondu
    call screen l5_talk
    hide screen Actor1
    jump hall

label school_eat_l5:
    show table:
        xalign 0.75
        yalign 0.95
    show screen Actor1("l5", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "P")
    with fondu
    l5 "Qu'est-ce que tu veux Puanteur ?"
    show screen Actor1("l5", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "")
    with fondu
    call screen l5_talk
    hide screen Actor1
    jump cantine


label school_stella:
    show screen Actor1("stella", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "P")
    with fondu
    stella "Bonjour, Lincoln."
    show screen Actor1("stella", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "")
    with fondu
    call screen stella_talk
    hide screen Actor1
    jump school_couloir_1

label school_eat_stella:
    show table:
        xalign 0.75
        yalign 0.95
    show screen Actor1("stella", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "P")
    with fondu
    stella "Bonjour, Lincoln."
    show screen Actor1("stella", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "")
    with fondu
    call screen stella_talk
    hide screen Actor1
    jump cantine


label school_cristina:
    show screen Actor1("cristina", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "bandeau_1", "", "Neutre", "P")
    with fondu
    cristina "Bonjour, Lincoln."
    show screen Actor1("cristina", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "bandeau_1", "", "Neutre", "")
    with fondu
    call screen cristina_talk
    hide screen Actor1
    jump school_couloir_1


label school_jordan:
    show screen Actor1("jordan", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "noeud_1", "", "Neutre", "P")
    with fondu
    jordan "Salut, Lincoln."
    show screen Actor1("jordan", "normal", "normal", "sh_1", "sb_1", "normal", "boucle_1", "noeud_1", "", "Neutre", "")
    with fondu
    call screen jordan_talk
    hide screen Actor1
    jump school_couloir_1


label school_chloe:
    show screen Actor1("chloe", "normal", "normal", "sh_1", "sb_1", "normal", "chapeau_1", "", "", "Neutre", "P")
    with fondu
    chloe "Salut, Lincoln."
    show screen Actor1("chloe", "normal", "normal", "sh_1", "sb_1", "normal", "chapeau_1", "", "", "Neutre", "")
    with fondu
    call screen chloe_talk
    hide screen Actor1
    jump school_couloir_2


label school_emma:
    show screen Actor1("emma", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "P")
    with fondu
    emma "Salut, Lincoln."
    show screen Actor1("emma", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "")
    with fondu
    call screen emma_talk
    hide screen Actor1
    jump school_couloir_2


label school_joy:
    menu:
        "Lui toucher les fesses" if True:
            jump joy_school_touch_ass
        "Lui parler" if True:
            jump joy_school_talk

label joy_school_touch_ass:
    show Joy_school_ass at left
    with fondu
    show Lincoln_grab_ass_1 at left
    with inR
    pause 0.1
    hide Lincoln_grab_ass_1
    show Lincoln_grab_ass_2 at left
    with trembleH
    pause
    hide Joy_school_ass
    hide Lincoln_grab_ass_2
    with fondu
    if sex_joy_points >= 20:
        show Joy_school_exciter at right
        with fondu
        joy "Lincoln... Hum..."
        $ sex_joy_points += 20
        $ love_joy_points += 10
    elif True:
        show Lincoln_claque at right
        with flash
        show Joy_school_claque_1 at right
        with inR
        pause 0.1
        hide Joy_school_claque_1
        show Joy_school_claque_2 at right
        with trembleV
        pause
        hide Joy_school_claque_2
        hide Lincoln_claque
        show screen Actor1("joy", "normal", "normal", "sh_0", "sb_1", "normal", "boucle_1", "", "", "Colere", "P")
        with fondu
        joy "Lincoln ! Espèce de sale porc !"
        $ sex_joy_points += 5
        $ love_joy_points -= 10
        $ warn_school_points += 5
        hide screen Actor1
    jump school_couloir_2

label joy_school_talk:
    show screen Actor1("joy", "normal", "normal", "sh_0", "sb_1", "normal", "boucle_1", "", "", "Neutre", "P")
    with fondu
    joy "Salut, Lincoln."
    show screen Actor1("joy", "normal", "normal", "sh_0", "sb_1", "normal", "boucle_1", "", "", "Neutre", "")
    with fondu
    call screen joy_talk
    hide screen Actor1
    jump school_couloir_2


label school_mollie:
    show screen Actor1("mollie", "normal", "normal", "sh_0", "sb_1", "normal", "", "", "", "Neutre", "P")
    with fondu
    mollie "Salut, petite bite !"
    show screen Actor1("mollie", "normal", "normal", "sh_0", "sb_1", "normal", "", "", "", "Neutre", "")
    with fondu
    call screen mollie_talk
    hide screen Actor1
    jump wc


label school_eat_clyde:
    show table:
        xalign 0.75
        yalign 0.95
    show Clyde_job_P at right
    with fondu
    clyde "Lincoln ! Tu veux me parlé ?"
    hide Clyde_job_P
    show Clyde_job at right
    with fondu
    pause
    hide Clyde_job
    jump cantine


label school_eat_geek:
    show table:
        xalign 0.75
        yalign 0.95
    show Geek_P at right
    with fondu
    geek "Salut !"
    hide Geek_P
    show Geek at right
    with fondu
    nar ""
    hide Geek
    jump cantine
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
