label map:
    $ city_in = True
    $ checkZone = "map"
    scene BG_ville
    with fondu
    call screen ville

screen ville():
    zorder 100
    imagemap:
        idle "Images/Plans/map.png"
        hover "Images/Plans/map_hover.png"

        hotspot (585,282,131,184) action Jump("home")

        hotspot (579,5,176,61) action Jump("mcbride")
        hotspot (764,376,135,104) action Jump("m_grouse")

        if new_voisin_key == True:
            hotspot (254,428,169,179) action Jump("m_new_voisin")

        if mollie_key == True:
            hotspot (386,255,108,143) action Jump("m_mollie")
        if stella_key == True:
            hotspot (599,165,108,93) action Jump("m_stella")
        if jordan_key == True:
            hotspot (509,564,166,156) action Jump("m_jordan")
        if sam_key == True:
            hotspot (180,93,98,99) action Jump("m_sam")
        if cristina_key == True:
            hotspot (919,425,122,115) action Jump("m_christina")
        if joy_key == True:
            hotspot (860,162,109,106) action Jump("m_joy")

        hotspot (853,0,132,89) action Jump("eglise")
        hotspot (0,310,68,130) action Jump("hopital")
        hotspot (426,89,88,91) action Jump("dentiste")
        hotspot (0,579,156,141) action Jump("parc")
        hotspot (1084,11,196,96) action Jump("mall")
        hotspot (105,233,155,89) action Jump("flip")
        hotspot (0,0,181,88) action Jump("theatre")
        hotspot (1087,243,166,76) action Jump("DMV")

        hotspot (1154,635,108,46) action Jump("school")

        hotspot (243,660,54,56) action Jump("plage")
        hotspot (229,0,58,51) action Jump("casagrande")

label home:
    $ city_in = False
    $ home_in = True
    scene BG_maison_J
    with fondu
    scene BG_devant
    with Dissolve(1.0)
    jump exit

label school:
    $ city_in = False
    scene BG_ville
    with fondu
    if tenue == "normal":
        if jour >= 1 and jour < 6:
            if heure == 8:
                play sound "audio/VOITURE.mp3"
                show bus
                with inL
                pause 0.0
                hide bus
                with outR
                stop sound
                jump bus
            elif heure > 8 and heure <= 15:
                show screen User(tenue, "_P")
                with fondu
                user "J'ai raté le bus... Merde !"
                hide screen User
                jump map
            elif True:
                show screen User(tenue, "_P")
                with fondu
                user "L'école est fermée"
                hide screen User
                jump map
        elif True:
            show screen User(tenue, "_P")
            with fondu
            user "Y'a pas d'école le week end !"
            hide screen User
            jump map
    elif True:
        show screen User(tenue, "_P")
        with fondu
        user "Je peux pas aller à l'école comme ça !"
        hide screen User
        call screen ville
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
