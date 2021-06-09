label groupe_1:
    show groupe_1_a
    with fondu
    menu:
        nar "Il y a beaucoup de vent aujourd'hui..."
        "continuer à regarder" if True:
            $ sex_points += 20
            $ school_group_ext = True
            jump groupe_1_next
        "Partir" if True:
            hide groupe_1_a
            jump exit_school

label groupe_1_next:
    show EF_vent:
        yalign 0.8
    with inL
    pause 0.0
    hide EF_vent
    with outR
    hide groupe_1_a
    show groupe_1_b
    with fondu
    nar ""
    hide groupe_1_b
    show zoom_cristina
    with fondu
    nar ""
    hide zoom_cristina
    show zoom_jordan
    with fondu
    nar ""
    hide zoom_jordan
    show zoom_stella
    with fondu
    nar ""
    hide zoom_stella
    jump exit_school
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
