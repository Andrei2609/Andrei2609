init:
    $ spider_cont = 5

screen spider_game():
    zorder 500
    add "Images/Backgrounds/chambre_lori_leni.png"
    if spider_cont == 5:
        imagebutton:
            xalign 0.85
            yalign 0.61
            idle "Images/Mini-Jeux/Spider/frank.png"
            hover "Images/Mini-Jeux/Spider/frank_hover.png"
            action SetVariable("spider_cont", spider_cont - 1)
    if spider_cont == 4:
        imagebutton:
            xalign 0.5
            yalign 0.37
            idle "Images/Mini-Jeux/Spider/frank.png"
            hover "Images/Mini-Jeux/Spider/frank_hover.png"
            action SetVariable("spider_cont", spider_cont - 1)
    if spider_cont == 3:
        imagebutton:
            xalign 0.3
            yalign 0.8
            idle "Images/Mini-Jeux/Spider/frank.png"
            hover "Images/Mini-Jeux/Spider/frank_hover.png"
            action SetVariable("spider_cont", spider_cont - 1)
    if spider_cont == 2:
        imagebutton:
            xalign 0.98
            yalign 0.75
            idle "Images/Mini-Jeux/Spider/frank.png"
            hover "Images/Mini-Jeux/Spider/frank_hover.png"
            action SetVariable("spider_cont", spider_cont - 1)
    if spider_cont == 1:
        imagebutton:
            xalign 0.1
            yalign 0.95
            idle "Images/Mini-Jeux/Spider/frank.png"
            hover "Images/Mini-Jeux/Spider/frank_hover.png"
            action SetVariable("spider_cont", spider_cont - 1)
    if spider_cont == 0:
        imagebutton:
            xalign 0.35
            yalign 1.0
            idle "Images/Plans/Minis/flecheB.png"
            hover "Images/Plans/Minis/flecheB_hover.png"
            action Jump("horror_cham_2020_victory")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
