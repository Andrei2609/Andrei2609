label cham_user:
    scene BG_lincoln
    with fondu
    $ user_room = True
    $ checkZone = "ch_user"
    call screen bedroom

screen bedroom():
    imagemap:
        idle "Images/Plans/chambre_lincoln.png"
        hover "Images/Plans/chambre_lincoln_hover.png"

        hotspot (1077,0,203,720) action Jump("exit_room")
        hotspot (189,369,856,318) action Jump("lit")
        hotspot (484,59,105,126) action Jump("calendrier")
        hotspot (5,216,121,161) action Jump("horloge")
        hotspot (0,468,151,250) action Jump("cham_user_2")

label exit_room:
    if warn_loud_points >= 100:
        jump GAME_OVER
    elif tenue == "nu":
        show screen User(tenue, "_P")
        with fondu
        user "Je peux pas sortir comme ça !"
        hide screen User
        call screen bedroom
    elif True:
        scene BG_couloir
        with fondu
        $ user_room = False
        if INTRO_Actif == 0:
            jump IntroCouloir
        elif True:
            call screen couloir

label lit:
    scene BG_lincoln
    menu:
        "Se masturber" if sex_points >= 50:
            $ tenue = "nu"
            show screen User(tenue, "_P")
            with inR
            user "Ici je serai tranquille pour me branler discrètement..."
            user "Maintenant, à quoi je pense pour en finir avec ça..?"
            menu:
                "Remplir la bouteille de sperme" if l4_tarte == 1:
                    jump user_mastu_creme
                "Se branler comme un fou" if True:
                    jump masturbe_ON
                "Leni sous la douche" if mastu_dream_leni == True:
                    $ mastuChoix_1 = 1
                    jump masturbe_ON
                "Lori qui utilise sa bouche" if mastu_dream_lori == True:
                    $ mastuChoix_1 = 2
                    jump masturbe_ON
                "Retour" if True:
                    hide screen User
                    call screen bedroom
        "Dormir" if heure > 20 or heure < 6:
            jump dormir
        "Retour" if True:
            call screen bedroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
