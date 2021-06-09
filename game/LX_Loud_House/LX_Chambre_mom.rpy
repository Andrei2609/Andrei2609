
image BG_rita = "Images/Backgrounds/chambre_rita.png"
image BG_rita_lit = "Images/Backgrounds/chambre_rita_lit.png"
image mom_lit_back = "Images/Mini-Jeux/Lit/mom/lit_back.png"

screen CH_mom():
    imagebutton:
        xalign 0.839
        yalign 0.0
        hover_xalign 0.7999
        hover_yalign 0.0
        idle "Images/Plans/CH_Rita/porte.png"
        hover "Images/Plans/CH_Rita/porte_hover.png"

        action Jump("salon")

    imagebutton:
        xalign 0.18
        yalign 0.0
        hover_xalign 0.1
        hover_yalign 0.0
        idle "Images/Plans/CH_Rita/placard.png"
        hover "Images/Plans/CH_Rita/placard_hover.png"

        action Jump("placard_mom")

    imagebutton:
        xalign 1.0
        yalign 1.0
        idle "Images/Plans/CH_Rita/lit.png"
        hover "Images/Plans/CH_Rita/lit_hover.png"

        action Jump("lit_mom")

    if heure >= 20:
        imagebutton:
            xalign 0.55
            yalign 0.4
            idle "Images/Plans/CH_Rita/mom.png"
            hover "Images/Plans/CH_Rita/mom_hover.png"

            action Jump("ch_mom_mom")

    if heure < 9 and jour < 6:
        imagebutton:
            xalign 0.05
            yalign 0.9
            idle "Images/Plans/CH_Rita/dad.png"
            hover "Images/Plans/CH_Rita/dad_hover.png"

            action Jump("ch_mom_dad")

label cham_mom:
    call screen porte_cham("ch_in_mom", "peek_mom", "salon")

label ch_in_mom:
    if heure >= 20 and heure < 24 and jour == 5:
        user "C'est fermé..."
    elif True:
        $ checkZone = "ch_mom"
        scene BG_rita
        with fondu
        call screen CH_mom
    jump salon

label placard_mom:
    menu:
        "Se cacher" if True:
            jump peek_placard_mom
        "Fouiller" if True:
            jump search_placard_mom
        "Laisser" if True:
            jump ch_in_mom

label lit_mom:
    if heure >= 22:
        scene mom_lit_back
        with fondu
        $ idFille = "mom"
        call screen sex_sleep
    elif True:
        scene BG_rita_lit
        with fondu
        nar ""
        jump ch_in_mom

label ch_mom_mom:
    show screen Actor1("mom", "normal", "normal", "sh_0", "sb_1", "normalA", "", "", "", "Neutre", "P")
    with fondu
    mom "Oui mon coeur ?"
    show screen Actor1("mom", "normal", "normal", "sh_0", "sb_1", "normalA", "", "", "", "Neutre", "")
    with fondu
    call screen mom_talk
    hide screen Actor1
    jump ch_in_mom

label ch_mom_dad:
    show Dad_P at right
    with fondu
    menu:
        dad "Oui Lincoln ?"
        "Où est maman ?" if True:
            dad "Elle est dans la cuisine !"
            jump ch_in_mom
        "On peut parler ?" if True:
            dad "Désolé mon grand, mais je dois me préparer pour le travail, une prochaine fois !"
            jump ch_in_mom
        "Non, rien." if True:
            hide Dad_P
            jump ch_in_mom

label search_placard_mom:
    if mom_cle == "wait" and heure < 8:
        $ mom_cle = "inpoche"
        show screen User(tenue, "I")
        with fondu
        show mom_cles:
            xalign 0.6
            yalign 0.4
        with inB
        show screen User(tenue, "_P")
        with fondu
        user "Génial, les clés de maman !"
        hide mom_cles
        hide screen User
        with fondu
    elif True:
        user "Rien d'intéressant..."
    jump ch_in_mom

label peek_mom:
    call timer (0, 5) from _call_timer_47
    if heure >= 20 and heure < 24 and jour == 5:
        $ sex_points += 20
        $ int_points += 2
        show screen peekLoud("Images/CG/01-Personnages/100-Rita/rita_dad_fuck_1.png")
        user "Wahou... Maman et papa sont en train de baiser..."
    elif True:
        show screen peekLoud("Images/Backgrounds/chambre_rita_lit.png")
        pause
    hide screen peekLoud
    jump salon

label peek_placard_mom:
    call timer (0, 5) from _call_timer_48
    if heure >= 20 and heure < 24 and jour == 5:
        $ sex_points += 20
        $ int_points += 2
        show screen peekPlacard("Images/CG/01-Personnages/100-Rita/rita_dad_fuck_1.png")
        user "Wahou... Maman et papa sont en train de baiser..."
        nar "Après un moment, vous quittez la chambre discrètement..."
        hide screen peekPlacard
        jump salon
    elif True:
        show screen peekPlacard("Images/Backgrounds/chambre_rita_lit.png")
        user "Rien à voir..."
    hide screen peekPlacard
    jump ch_in_mom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
