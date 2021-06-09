screen peekLoud(fond):
    viewport:
        xalign 0.5 ypos 40 xysize (200, 500)

        draggable True
        mousewheel True
        arrowkeys True

        xinitial 0.5
        yinitial 0.5

        child_size (1280, 720)

        add fond
    add "PEEK_loud"

screen peek(fond):
    viewport:
        xalign 0.5 ypos 95 xysize (200, 500)

        draggable True
        mousewheel True
        arrowkeys True

        xinitial 0.5
        yinitial 0.5

        child_size (1280, 720)

        add fond
    add "PEEK_keyhole"

screen peekGym(fond):
    viewport:
        xalign 0.7 xysize (500, 720)

        draggable True
        mousewheel True
        arrowkeys True

        xinitial 0.5
        yinitial 0.5

        child_size (1280, 720)

        add fond
    add "PEEK_gymnase"

screen peekParc(fond):
    viewport:
        xalign 0.5 xysize (1160, 677)

        draggable True
        mousewheel True
        arrowkeys True

        xinitial 0.5
        yinitial 0.5

        child_size (1280, 720)

        add fond
    add "EF_plantes"

screen peekShop(fond):
    viewport:
        xalign 0.5 ypos 0 xysize (500, 720)

        draggable True
        mousewheel True
        arrowkeys True

        xinitial 0.5
        yinitial 0.5

        child_size (700, 720)

        add fond
    add "PEEK_rideau"

screen peekPlacard(fond):
    viewport:
        yalign 0.35
        xalign 0.4
        xysize (850, 550)

        draggable True
        mousewheel True
        arrowkeys True

        xinitial 0.5
        yinitial 0.5

        child_size (1280, 720)

        add fond
    add "PEEK_placard"

screen peekWC(fond):
    viewport:
        xalign 0.5
        yalign 1.0
        xysize (1100, 370)

        draggable True
        mousewheel True
        arrowkeys True

        xinitial 0.5
        yinitial 1.0

        child_size (1280, 720)

        add fond
    add "PEEK_wc"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
