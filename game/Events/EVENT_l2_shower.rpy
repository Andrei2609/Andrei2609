
label salle_de_bain_leni_1:
    $ mastu_dream_leni = True
    play sound "audio/DOUCHE.mp3"
    scene BG_bain
    show EF_brouillard
    with flash
    show screen User(tenue, "")
    with inL
    pause .2
    show screen User(tenue, "_S")
    pause .1
    hide screen User
    with fondu
    show FULL_leni_douche:
        xanchor 0 yanchor 0
        xpos 0 ypos -1760
        linear 10.0 xpos 0 ypos 0
    nar ""
    hide FULL_leni_douche
    show leni_douche behind EF_brouillard
    with fondu
    l2 "Mhmmm... une peau bien hydratée c'est le secret pour une belle peau !"
    show screen User(tenue, "_M")
    with fondu
    user "Leni est déjà à l'intérieur... {w}\nWahou... Quel corps de rêve..."

    $ sex_points += 30

    hide leni_douche
    show leni_dos_douche_P at right
    show screen User(tenue, "I")
    with fondu
    l2 "Hey ! Lincoln, attends ton tour !"
    $ sex_l2_points += 2
    show screen User(tenue, "_P")
    hide leni_dos_douche_P
    show leni_dos_douche at right
    with fondu
    user "Heu ! Oui, désolé !"
    hide leni_dos_douche
    with outR
    menu:
        nar "Que faire ?"
        "Se masturber" if True:
            $ sex_points += 30
            $ mastu_dream_lori = True
            jump masturbe_bain_leni_ko
        "Sortir" if True:
            jump couloir_retour_bain_1

label masturbe_bain_leni_ko:
    show leni_ass_douche at right
    with fondu
    show screen User(tenue, "")
    with trembleV
    nar "Lincoln regarde fixement le corps nu et mouillé de Leni, \ntandis que ses mains se dirigent vers son sexe..."

    hide leni_ass_douche
    with flash
    show screen Actor1("l1", "colere", "normal", "sh_0", "", "sleep", "", "", "", "Colere", "P")
    show screen User(tenue, "I")
    with fondu
    l1 "HEY LINCOLN !!! Qu'est-ce que tu fais là!?"
    show screen Actor1("l1", "colere", "normal", "sh_0", "", "sleep", "", "", "", "Colere", "")
    show screen User(tenue, "_P")
    with fondu
    user "Heu... Rien ! Je suis rentré par erreur. Leni n'a pas fermé la porte !"

    $ sex_points -= 5
    $ warn_loud_points += 5

    hide screen Actor1
    show screen User(tenue, "I")
    show screen Actor2("l1", "nue", "normal", "sh_0", "", "sleep", "", "", "", "Colere", "")
    show screen Actor1("l2", "nue", "mouille", "sh_0", "", "bulle", "", "", "", "Neutre", "P")
    with fondu
    l2 "Bah ! J'ai bien voulu la fermer, mais Lynn a cassé la serrure... {w}\nLincoln, c'est quoi ça !? Hi! Hi! Hi!"

    show screen Actor1("l2", "nue", "mouille", "sh_0", "", "bulle", "", "", "", "Neutre", "")
    show screen User(tenue, "_P")
    with fondu
    user "C'est rien !!!"
    hide screen User
    hide screen Actor1
    hide screen Actor2
    with fondu
    hide EF_brouillard

    jump couloir_retour_bain_1

label couloir_retour_bain_1:
    stop sound fadeout 1

    call timer (0, 10) from _call_timer_28

    scene BG_couloir
    with slideinR

    show screen User(tenue, "_P")
    with inL
    if luna_peek_1 == True and luan_peek_1 == True and lynn_peek_1 == True:
        user "Punaise elles ont quoi aujourd'hui... J'ai trop la gaule... \nFaut que je me branle et vite !"

    elif luna_peek_1 == True and luan_peek_1 == True:
        user "Punaise Leni, Luna et Luan sont trop chaudes ce matin... \nJ'ai trop la gaule... \nFaut que je me branle et vite !"


    elif luna_peek_1 == True and lynn_peek_1 == True:
        user "Punaise Leni, Luna et Lynn sont trop chaudes ce matin... \nJ'ai trop la gaule... \nFaut que je me branle et vite !"


    elif luan_peek_1 == True and lynn_peek_1 == True:
        user "Punaise Leni, Lynn et Luan sont trop chaudes ce matin... \nJ'ai trop la gaule... \nFaut que je me branle et vite !"


    elif luna_peek_1 == True:
        user "Punaise entre Luna et Leni à poil... \nJ'ai trop la gaule... \nFaut que je me branle et vite !"


    elif luan_peek_1 == True:
        user "Punaise entre le cul de Luan et Leni à poil... \nJ'ai trop la gaule... \nFaut que je me branle et vite !"


    elif lynn_peek_1 == True:
        user "Punaise entre Lynn qui fait ses abdos et Leni à poil... \nJ'ai trop la gaule... \nFaut que je me branle et vite !"
    elif True:


        user "Punaise Leni a un de ces corps... \nJ'ai trop la gaule... \nFaut que je me branle et vite !"



    hide screen User
    call screen couloir
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
