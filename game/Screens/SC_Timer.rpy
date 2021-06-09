
init:
    $ heure = 0
    $ minute = 0
    $ jour = 1
    $ jour_nom = _("")

label horloge:
    menu:
        "+1 heure" if True:
            call timer (1, 0) from _call_timer_50
            jump horloge
        "+30 minutes" if True:
            call timer (0, 30) from _call_timer_51
            jump horloge
        "Retour" if True:
            call screen bedroom

label timer(h, m):
    $ h_verif = 24 - h
    $ m_verif = 60 - m

    if heure >= h_verif:
        $ heure = 0
        $ minute = 0
        if jour == 7:
            $ jour = 1
        elif True:
            $ jour += 1
    elif heure >= 21 and mall_in == True:
        $ heure += 1
        $ minute = 0
        nar "Le centre commercial ferme ses portes"
        jump exit_mall
    elif heure == 2:
        user "Aaaahhh... C'est l'heure de dormir..."
        jump cham_user
    elif True:
        $ heure = heure + h

    if heure >= 23 and minute >= m_verif:
        $ heure = 0
        $ minute = 0
        if jour == 7:
            $ jour = 1
        elif True:
            $ jour += 1
    elif heure >= 21 and minute >= m_verif and mall_in == True:
        $ heure += 1
        $ minute = 0
        nar "Le centre commercial ferme ses portes"
        jump exit_mall
    elif heure == 2 and minute >= m_verif:
        user "Aaaahhh... C'est l'heure de dormir..."
        jump cham_user
    elif minute >= m_verif:
        $ heure += 1
        $ minute = 0
    elif True:
        $ minute += m

    if heure == 8 and minute == 0 and jour < 6 and home_in == True:
        mom "Lincoln, viens dans la cuisine, c'est l'heure de l'école !"
    elif heure == 12 and minute == 0 and home_in == True or heure == 19 and minute == 0 and home_in == True:
        dad "Lincoln, c'est l'heure de manger !"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
