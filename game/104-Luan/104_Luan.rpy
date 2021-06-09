
define l4 = Character(
    "Luan",
    window_background="gui/textbox/l4.png",
    color="#BDAF00",
    what_outlines=[( 1, "#FFEC00", 0, 0 )]
    )

init:
    $ l4_win = False
    $ love_l4_points = 10
    $ sex_l4_points = 0
    $ l4_cum = 0

screen l4_talk():
    use menu_talk(l4, love_l4_points, sex_l4_points, "l4_menu_stats")

screen l4_menu_stats():
    use girl_stats("l4", l4_win, "Luan", _("la comique"), _("Les blagues"), _("La politique"), "19", love_l4_points, sex_l4_points, l4_cum)


image Luan_ass_sleepA = "Images/CG/01-Personnages/104-Luan/luan_ass_sleepA.png"
image Luan_ass_panty = "Images/CG/01-Personnages/104-Luan/luan_ass_panty.png"


image Luan_zoom_1 = "Images/CG/01-Personnages/104-Luan/ZOOM-luan_slip.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
