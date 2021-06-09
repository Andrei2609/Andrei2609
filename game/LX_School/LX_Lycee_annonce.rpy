label annonces:
    call screen LyceeAnnonces

label annonces_quit:
    hide screen LyceeAnnonces
    jump hall

screen LyceeAnnonces():
    frame:
        xalign 0.5
        yalign 0.5
        background Frame("Images/CG/03-Divers/tableau.png", gui.frame_borders, tile=gui.frame_tile)
        has vbox:
            xsize 900
            ysize 600
            xalign 0.5
        label _("Annonces") xalign 0.5 yalign 0.03 text_size 60
        vbox:
            xalign 0.5
            yalign 0.1
            text _("{font=FT_Craie.ttf}{size=+30}{color=#ffffff}Prochaine mise à jour.{/color}{/size}{/font}")
            text _("{font=FT_Craie.ttf}{size=+30}{color=#ffffff}Suite de l'histoire de Leni{/color}{/size}{/font}")
            text _("{font=FT_Craie.ttf}{size=+30}{color=#ffffff}et développement sur le Lycée.{/color}{/size}{/font}")
            text _("")
            text _("{font=FT_Craie.ttf}{size=+30}{color=#ffffff}Merci pour votre soutiens.{/color}{/size}{/font}")
        imagebutton:
            xalign 0.08
            yalign 0.75
            idle "gui/Side_menu/retour.png"
            hover "gui/Side_menu/retour_hover.png"

            action Jump("annonces_quit")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
