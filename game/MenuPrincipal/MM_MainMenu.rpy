screen main_menu():
    tag menu

    add "gui/Main_menu/background.png"
    vbox:
        spacing 5
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 5
            add "gui/Main_menu/18+.png"
            imagebutton:
                idle "gui/Main_menu/FR.png"
                hover "gui/Main_menu/FR_hover.png"

                action Language(None)
            imagebutton:
                idle "gui/Main_menu/EN.png"
                hover "gui/Main_menu/EN_hover.png"

                action Language("english")
            add "gui/Main_menu/ES_hover.png"





            vbox:
                xsize 815
                text "[config.name!t]":
                    font "FT_name.ttf"
                    color "#990000"
                    size 50
                    xalign 1.0
                text "[config.version]":
                    size 15
                    xalign 1.0
        hbox:
            spacing 5
            vbox:
                spacing 5
                imagebutton:
                    idle "gui/Main_menu/NEW.png"
                    hover "gui/Main_menu/NEW_hover.png"

                    action Start()
                imagebutton:
                    idle "gui/Main_menu/LOAD.png"
                    hover "gui/Main_menu/LOAD_hover.png"

                    action ShowMenu("load")
            add "gui/Main_menu/banniere.png"
        hbox:
            spacing 5
            imagebutton:
                idle "gui/Main_menu/QUIT.png"
                hover "gui/Main_menu/QUIT_hover.png"

                action Quit(confirm=not main_menu)
            imagebutton:
                idle "gui/Main_menu/OPTION.png"
                hover "gui/Main_menu/OPTION_hover.png"

                action ShowMenu("preferences")
            imagebutton:
                idle "gui/Main_menu/ABOUT.png"
                hover "gui/Main_menu/ABOUT_hover.png"

                action ShowMenu("about")
            vbox:
                spacing 5
                imagebutton:
                    idle "gui/Main_menu/HELP.png"
                    hover "gui/Main_menu/HELP_hover.png"

                    action ShowMenu("help")
                imagebutton:
                    idle "gui/Main_menu/SUPPORT.png"
                    hover "gui/Main_menu/SUPPORT_hover.png"

                    action ShowMenu("soutien")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
