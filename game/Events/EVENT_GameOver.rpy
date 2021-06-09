
image GAME_OVER_loud = "Images/CG/00-Histoire/end/game_over_loud.png"
image GAME_OVER_school = "Images/CG/00-Histoire/end/game_over_school.png"
image GAME_OVER_ville = "Images/CG/00-Histoire/end/game_over_ville.png"

init:
    $ GAME_OVER_count = 0

screen GameOver():
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        label _("Continuez l'histoire mais remettre à zéro tout les stats des filles ?") xalign 0.5
        hbox:
            xalign 0.5
            spacing 20
            button:
                xalign 0.5
                yalign 0.5
                frame:
                    xsize 100
                    ysize 100
                    hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
                    has vbox:
                        xalign 0.5
                        yalign 0.5
                    add "Images/Bases/Icones/aime.png" xalign 0.5
                    text _("Oui") xalign 0.5
                action Jump("continue_game")
            button:
                xalign 0.5
                yalign 0.5
                frame:
                    xsize 100
                    ysize 100
                    hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
                    has vbox:
                        xalign 0.5
                        yalign 0.5
                    add "Images/Bases/Icones/not_aime.png" xalign 0.5
                    text _("Non") xalign 0.5
                action ShowMenu("quit")

label GAME_OVER:
    $ GAME_OVER_count += 1
    if warn_loud_points >= 100:
        show GAME_OVER_loud
        with flash
        pause
        hide GAME_OVER_loud
    elif warn_school_points >= 100:
        show GAME_OVER_school
        with flash
        pause
        hide GAME_OVER_school
    elif warn_ville_points >= 100:
        show GAME_OVER_ville
        with flash
        pause
        hide GAME_OVER_ville
    scene BG_salon
    with flash
    if GAME_OVER_count == 1:
        show d_P at left
        with inL
        d "C'est la première fois que vous perdez..."
        d "On vas être gentil ! On vous offre une seconde chance mais attention à la prochaine fois..."
        hide d_P
        with outL
        $ warn_loud_points = 0
        $ warn_school_points = 0
        $ warn_ville_points = 0
        jump cham_user
    elif True:
        call screen GameOver

label continue_game:
    $ love_mom_points = 0
    $ sex_mom_points = 0
    $ love_l1_points = 0
    $ sex_l1_points = 0
    $ love_l2_points = 0
    $ sex_l2_points = 0
    $ love_l3_points = 0
    $ sex_l3_points = 0
    $ love_l4_points = 0
    $ sex_l4_points = 0
    $ love_l5_points = 0
    $ sex_l5_points = 0
    $ love_cristina_points = 0
    $ sex_cristina_points = 0
    $ love_jordan_points = 0
    $ sex_jordan_points = 0
    $ love_joy_points = 0
    $ sex_joy_points = 0
    $ love_mollie_points = 0
    $ sex_mollie_points = 0
    $ love_ronnie_points = 0
    $ sex_ronnie_points = 0
    $ love_stella_points = 0
    $ sex_stella_points = 0
    $ love_carol_points = 0
    $ sex_carol_points = 0
    $ love_sam_points = 0
    $ sex_sam_points = 0
    $ love_paige_points = 0
    $ sex_paige_points = 0
    $ love_prof1_points = 0
    $ sex_prof1_points = 0
    $ love_prof2_points = 0
    $ sex_prof2_points = 0
    $ love_prof3_points = 0
    $ sex_prof3_points = 0
    $ love_nurse_points = 0
    $ sex_nurse_points = 0
    $ love_maria_points = 0
    $ sex_maria_points = 0
    $ love_journaliste_points = 0
    $ sex_journaliste_points = 0
    $ warn_loud_points = 0
    $ warn_school_points = 0
    $ warn_ville_points = 0

    nar "Vous vous réveillez, ce n'étais qu'un mauvais rêve !"

    jump cham_user
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
