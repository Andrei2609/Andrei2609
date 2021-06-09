screen help():
    tag menu


    default device = "keyboard"

    add "gui/Main_menu/background.png"
    vbox:
        spacing 5
        yalign 0.2
        xalign 0.3
        ysize 720
        hbox:
            xsize 1200
            ysize 100
            vbox:
                label "[config.name!t]"
                text _("Version [config.version!t]")
            text _("Aide"):
                font "FT_name.ttf"
                size 50
                xalign 1.0
                yalign 0.5
        hbox:
            spacing 10
            vbox:
                spacing 10
                xalign 0.0
                yalign 1.0
                frame:
                    textbutton _("Menu"):
                        action MainMenu()
                imagebutton:
                    idle "gui/Side_menu/retour.png"
                    hover "gui/Side_menu/retour_hover.png"

                    action Return()

            vbox:
                spacing 10
                ysize 600
                hbox:
                    spacing 10
                    xalign 0.5
                    frame:
                        textbutton _("Clavier") action SetScreenVariable("device", "keyboard")
                    frame:
                        textbutton _("Souris") action SetScreenVariable("device", "mouse")

                    if GamepadExists():
                        frame:
                            textbutton _("Manette") action SetScreenVariable("device", "gamepad")

                frame:
                    xsize 1000
                    xalign 0.5
                    background Frame("gui/Side_menu/help_back.png", gui.frame_borders, tile=gui.frame_tile)

                    style_prefix "help"
                    if device == "keyboard":
                        use keyboard_help
                    elif device == "mouse":
                        use mouse_help
                    elif device == "gamepad":
                        use gamepad_help
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
