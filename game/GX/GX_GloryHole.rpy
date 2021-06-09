
image GloryHole_back = "Images/CG/02-Lieux/GloryHole/lincoln_0.png"

image GloryHole_in = "Images/CG/02-Lieux/GloryHole/lincoln_1.png"
image GloryHole_nada = "Images/CG/02-Lieux/GloryHole/lincoln_2.png"
image GloryHole_KO = "Images/CG/02-Lieux/GloryHole/lincoln_8.png"

image GloryHole_PEEK_1 = "Images/CG/02-Lieux/GloryHole/lincoln_9.png"
image GloryHole_PEEK_2_1 = "Images/CG/02-Lieux/GloryHole/lincoln_10_1.png"
image GloryHole_PEEK_2_2 = "Images/CG/02-Lieux/GloryHole/lincoln_10_2.png"
image GloryHole_PEEK_2_3 = "Images/CG/02-Lieux/GloryHole/lincoln_10_3.png"
image GloryHole_PEEK_3 = "Images/CG/02-Lieux/GloryHole/lincoln_11.png"

image GloryHole_OK = "Images/CG/02-Lieux/GloryHole/lincoln_3.png"
image GloryHole_GO:
    "Images/CG/02-Lieux/GloryHole/lincoln_4.png"
    pause .2
    "Images/CG/02-Lieux/GloryHole/lincoln_5.png"
    pause .2
    repeat
image GloryHole_Cum = "Images/CG/02-Lieux/GloryHole/lincoln_6.png"
image GloryHole_End = "Images/CG/02-Lieux/GloryHole/lincoln_7.png"


image GloryHole_Stella = "Images/CG/02-Lieux/GloryHole/stella.png"
image GloryHole_Jordan = "Images/CG/02-Lieux/GloryHole/jordan.png"
image GloryHole_Mollie = "Images/CG/02-Lieux/GloryHole/mollie.png"
image GloryHole_Cristina = "Images/CG/02-Lieux/GloryHole/cristina.png"
image GloryHole_Joy = "Images/CG/02-Lieux/GloryHole/joy.png"
image GloryHole_Lynn = "Images/CG/02-Lieux/GloryHole/lynn.png"


image GloryHole_morsure_1 = "Images/CG/02-Lieux/GloryHole/morsure_1.png"
image GloryHole_morsure_2 = "Images/CG/02-Lieux/GloryHole/morsure_2.png"
image GloryHole_morsure_3 = "Images/CG/02-Lieux/GloryHole/morsure_3.png"

init:
    $ GH_count = 1

screen GH_menu():
    vbox:
        spacing 5
        xalign 0.8
        yalign 0.5
        xsize 300
        frame:
            xalign 0.5
            textbutton _("Poser un dollar sur ta bite et la glisser dans le trou"):
                action Jump("GH_dollar_in")
        frame:
            xalign 0.5
            textbutton _("Glisser ta bite dans le trou sans mettre d'argent"):
                action Jump("GH_in")
        frame:
            xalign 0.5
            textbutton _("Regarder dans le trou"):
                action Jump("GH_peek")
        imagebutton:
            xalign 1.0
            idle "gui/Side_menu/retour.png"
            hover "gui/Side_menu/retour_hover.png"
            action Jump("GH_exit")

label GH_exit:
    show screen user_stats
    jump wc_garcons

label GloryHole:
    hide screen User
    hide screen user_stats
    show GloryHole_back
    with fondu
    call screen GH_menu

label GH_dollar_in:
    if user_coins >= 1:
        $ user_coins -= 1
        $ vie_points -= 30
        $ sex_points = 0
        if heure < 10 or heure == 12:
            call timer (0, 10) from _call_timer_10
            nar "y'a du bruit de l'autres côtés"
            show GloryHole_OK
            with fondu
            nar ""
            hide GloryHole_OK
            show GloryHole_GO
            user "Wahou, c'est trop bon..."
            nar ""
            hide GloryHole_GO
            show GloryHole_Cum
            with flash
            nar ""
            show GloryHole_Cum
            with flash
            nar ""
            show GloryHole_Cum
            with flash
            nar ""
            hide GloryHole_Cum
            show GloryHole_End
            user "Je me demande bien qui est de l'autre côté ?"
            hide GloryHole_End
            show GloryHole_back
            with fondu
            nar ""
            if GH_count == 1:
                $ GH_count += 1
                show GloryHole_Stella at right
                with fondu
            elif GH_count == 2:
                $ GH_count += 1
                show GloryHole_Jordan at right
                with fondu
            elif GH_count == 3:
                $ GH_count += 1
                show GloryHole_Mollie at right
                with fondu
            elif GH_count == 4:
                $ GH_count += 1
                show GloryHole_Cristina at right
                with fondu
            elif GH_count == 5:
                $ GH_count += 1
                show GloryHole_Joy at right
                with fondu
            elif GH_count == 6:
                $ GH_count = 1
                show GloryHole_Lynn at right
                with fondu
            nar ""
            jump GH_exit
        elif True:
            show GloryHole_nada
            with fondu
            user "Personne... Merde ! J'ai perdu mon dollar..."
            jump GH_exit
    elif True:
        user "J'ai pas d'argent..."
        jump GloryHole

label GH_in:
    if heure < 10 or heure == 12:
        nar "y'a du bruit de l'autres côtés"
        show GloryHole_OK
        with fondu
        user "Yes... C'est trop cool !"
        hide GloryHole_OK
        show GloryHole_KO
        with trembleH
        nar "Haaa !"
        if GH_count == 1:
            $ GH_count += 1
            show GloryHole_morsure_1:
                xalign 0.9
                yalign 0.4
            with fondu
            user "Haaaaaaaaaaa !"
            hide GloryHole_morsure_1
        elif GH_count == 2:
            $ GH_count += 1
            show GloryHole_morsure_2:
                xalign 0.9
                yalign 0.4
            with fondu
            user "Haaaaaaaaaaa !"
            hide GloryHole_morsure_2
        elif True:
            $ GH_count = 1
            show GloryHole_morsure_3:
                xalign 0.9
                yalign 0.4
            with fondu
            user "Haaaaaaaaaaa !"
            hide GloryHole_morsure_3
        hide GloryHole_KO
        show GloryHole_back
        jump GH_KO_exit
    elif True:
        show GloryHole_nada
        with fondu
        user "Personne..."
        jump GH_exit

label GH_KO_exit:
    scene BG_lycee_wc_garcon
    show screen User(tenue, "_T")
    with trembleV
    user "Elle m'a mordue... La prochainne fois mieux vaut mettre un dollar... ouille !"
    $ vie_points -= 50
    $ sex_points = 0
    hide screen User
    jump GH_exit

label GH_peek:
    if heure < 10 or heure == 12:
        nar "y'a du bruit de l'autres côtés"
        show GloryHole_PEEK_1
        with fondu
        nar ""
        hide GloryHole_PEEK_1
        if GH_count == 1:
            $ GH_count += 1
            show GloryHole_PEEK_2_1
            with trembleV
            nar ""
            hide GloryHole_PEEK_2_1
        elif GH_count == 2:
            $ GH_count += 1
            show GloryHole_PEEK_2_2
            with trembleV
            nar ""
            hide GloryHole_PEEK_2_2
        elif True:
            $ GH_count = 1
            show GloryHole_PEEK_2_3
            with trembleV
            nar ""
            hide GloryHole_PEEK_2_3
        show GloryHole_PEEK_3
        user "Vaut mieux pas recommencer..."
        hide GloryHole_PEEK_3
        $ school_points -= 5
        $ vie_points -= 5
        $ sex_points -= 10
        jump GH_exit
    elif True:
        show GloryHole_PEEK_1
        with fondu
        user "Personne, dommage..."
        jump GH_exit
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
