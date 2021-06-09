screen file_slots(title):

    add "gui/Main_menu/background.png"
    vbox:
        xalign 0.5
        yalign 0.5
        ysize 700
        hbox:
            xsize 1200
            ysize 100
            vbox:
                label "[config.name!t]"
                text _("Version [config.version!t]")
            text title:
                font "FT_name.ttf"
                size 50
                xalign 1.0
                yalign 0.5
        hbox:
            spacing 10
            xalign 0.5
            frame:
                textbutton _("Charger"):
                    action ShowMenu("load")
            frame:
                textbutton _("Sauvegarder"):
                    action ShowMenu("save")
        hbox:
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

                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5

                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):

                        $ slot = i + 1
                        frame:
                            xysize (300,250)
                            background None
                            button:
                                action FileAction(slot)
                                yalign 0.5
                                xalign 0.5

                                has vbox

                                add FileScreenshot(slot) xalign 0.5

                                text FileTime(slot, format=_("\n{#file_time}%A %d %B %Y, %H:%M"), empty=_("\nemplacement\nvide")):
                                    style "slot_time_text"

                                text FileSaveName(slot):
                                    style "slot_name_text"

                                key "save_delete" action FileDelete(slot)
                            add "gui/button/save_cadre.png" yalign 0.5 xalign 0.5


                text "" size 10
                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign 1.0

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()


                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
