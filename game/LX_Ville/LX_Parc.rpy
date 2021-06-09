
image BG_parc = "Images/Backgrounds/parc.png"

label parc:
    $ checkZone = "parc"
    call timer (0, 10) from _call_timer_41
    scene BG_parc
    with fondu
    call screen Parc

screen Parc():
    imagebutton:
        xalign 0.5
        yalign 0.99
        idle "Images/Plans/Minis/flecheB.png"
        hover "Images/Plans/Minis/flecheB_hover.png"
        action Jump("map")

    imagebutton:
        xalign 0.275
        yalign 0.385
        idle "Images/Plans/Parc/banc.png"
        hover "Images/Plans/Parc/banc_hover.png"
        action Jump("relax_park")

    imagebutton:
        xalign 0.67
        yalign 0.5
        idle "Images/Plans/Minis/strength.png"
        hover "Images/Plans/Minis/strength_hover.png"
        action Jump("exo_park")

    imagebutton:
        xalign 0.1
        yalign 0.636
        idle "Images/Plans/Parc/buisson.png"
        hover "Images/Plans/Parc/buisson_hover.png"
        action Jump("spy_park")

label relax_park:
    $ vie_points += 10
    show parc_cool_user
    with fondu
    user "Un peu de repos sur ce banc me fera du bien !"
    call timer (0, 30) from _call_timer_42
    hide parc_cool_user
    with fondu
    call screen Parc

label exo_park:
    if vie_points >= 10:
        if tenue == "sport":
            $ vie_points -= 10
            $ force_points += 1
            user "Un peu d'exercice pour me mettre en forme !"
            call timer (0, 30) from _call_timer_43
        elif True:
            user "Je ne peux pas m'entrainer habillé comme ça !"
    elif True:
        user "Trop fatigué pour ça..."
    call screen Parc

label spy_park:
    $ int_points += 1
    call timer (0, 5) from _call_timer_44
    show screen peekParc("PEEK_parc_back")
    nar ""
    hide screen peekParc
    call screen Parc
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
