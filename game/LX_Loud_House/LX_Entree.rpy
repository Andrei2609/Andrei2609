screen entree():
    imagebutton:
        xalign 0.902
        yalign 0.0
        hover_xalign 0.9
        hover_yalign 0.0
        idle "Images/Plans/Entree/porte.png"
        hover "Images/Plans/Entree/porte_hover.png"
        action Jump("exit")

    imagebutton:
        xalign 0.05
        yalign 0.5
        idle "Images/Plans/Minis/flecheHG.png"
        hover "Images/Plans/Minis/flecheHG_hover.png"
        action Jump("couloir")

    imagebutton:
        xalign 0.35
        yalign 1.0
        idle "Images/Plans/Minis/flecheB.png"
        hover "Images/Plans/Minis/flecheB_hover.png"
        action Jump("salon")

    imagebutton:
        xalign 0.2837
        yalign 0.462
        idle "Images/Plans/Entree/manger.png"
        hover "Images/Plans/Entree/manger_hover.png"
        action Jump("Diningroom")

    if game_theme == "halloween":
        add "Images/Objets/event/citrouille_1.png" xalign 0.95 yalign 0.74
        add "Images/Objets/event/citrouille_2.png" xalign 0.15 yalign 0.75
        add "Images/Objets/event/guirlande_halloween.png" xalign 0.275 yalign 0.2
        add "Images/Objets/event/chapeau_sorciere.png" xalign 0.68 yalign 0.35

screen porch():
    imagebutton:
        xalign 0.009
        yalign 0.99
        idle "Images/Plans/Minis/porte.png"
        hover "Images/Plans/Minis/porte_hover.png"
        if heure >= 15 and INTRO_Actif == 3:
            action Jump("prime_quest_return_home")
        else:
            action Jump("entree")

    imagebutton:
        xalign 0.05
        yalign 0.4
        idle "Images/Plans/Minis/flecheG.png"
        hover "Images/Plans/Minis/flecheG_hover.png"
        action Jump("allee")

    imagebutton:
        xalign 0.9
        yalign 0.78
        idle "Images/Plans/Minis/flecheHD.png"
        hover "Images/Plans/Minis/flecheHD_hover.png"
        action Jump("home_exit_ville")

label entree:
    $ checkZone = "entree"
    scene BG_entre
    with fondu
    call screen entree

label exit:
    if tenue == "slip" or tenue == "slipA":
        show screen User(tenue, "_P")
        with fondu
        user "Je peux pas sortir de la maison comme ça !"
        hide screen User
        with fondu
        jump entree
    elif True:
        $ checkZone = "porch"
        scene BG_devant
        with fondu
        call screen porch

label home_exit_ville:
    if warn_ville_points >= 100:
        jump GAME_OVER
    elif True:
        $ home_in = False
        $ city_in = True
        scene BG_maison_J
        with fondu
        scene BG_ville
        with Dissolve(1.0)
        if INTRO_Actif == 1:
            jump IntroVille
        elif True:
            call screen ville
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
