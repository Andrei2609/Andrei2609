screen preferences():
    tag menu

    add "gui/Main_menu/background.png"
    vbox:
        spacing 5
        yalign 0.2
        xalign 0.3
        ysize 700
        hbox:
            xsize 1200
            ysize 100
            vbox:
                label "[config.name!t]"
                text _("Version [config.version!t]")
            text _("Préférences"):
                font "FT_name.ttf"
                size 50
                xalign 1.0
                yalign 0.5
        add "gui/Side_menu/banniere_pref.png" xalign 0.5

        hbox:
            spacing 5
            xsize 1200
            vbox:
                spacing 10
                xalign 0.5
                yalign 1.0
                frame:
                    textbutton _("Menu"):
                        action MainMenu()
                imagebutton:
                    idle "gui/Side_menu/retour.png"
                    hover "gui/Side_menu/retour_hover.png"
                    action Return()
            vbox:
                spacing 5
                frame:
                    xsize 300
                    if renpy.variant("pc"):

                        vbox:
                            style_prefix "radio"
                            label _("Affichage")
                            hbox:
                                xalign 0.5
                                spacing 20
                                imagebutton:
                                    idle "gui/Side_menu/window.png"
                                    hover "gui/Side_menu/window_hover.png"
                                    action Preference("display", "window")
                                imagebutton:
                                    idle "gui/Side_menu/full.png"
                                    hover "gui/Side_menu/full_hover.png"
                                    action Preference("display", "fullscreen")
                frame:
                    xsize 300
                    has vbox:
                        style_prefix "radio"
                    label _("Rembobinage côté")
                    textbutton _("Désactivé") action Preference("rollback side", "disable")
                    textbutton _("Gauche") action Preference("rollback side", "left")
                    textbutton _("Droite") action Preference("rollback side", "right")
            vbox:
                spacing 5
                frame:
                    xsize 400
                    has vbox:
                        style_prefix "check"
                    label _("Avance rapide")
                    textbutton _("Texte non lu") action Preference("skip", "toggle")
                    textbutton _("Après les choix") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                frame:
                    xsize 400
                    has vbox:
                        style_prefix "radio"
                    label _("Langage")

                    hbox:
                        spacing 5
                        imagebutton:
                            idle "gui/Main_menu/FR.png"
                            hover "gui/Main_menu/FR_hover.png"

                            action Language(None)
                        imagebutton:
                            idle "gui/Main_menu/EN.png"
                            hover "gui/Main_menu/EN_hover.png"

                            action Language("english")






            vbox:
                spacing 5
                frame:
                    xsize 400
                    has vbox
                    if config.has_music:
                        label _("Volume de la musique")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("Volume des sons")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("Volume des voix")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Couper tous les sons"):
                            text_size 12
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                frame:
                    xsize 400
                    has vbox
                    label _("Vitesse du texte")
                    bar value Preference("text speed")
                    label _("Avance automatique")
                    bar value Preference("auto-forward time")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
