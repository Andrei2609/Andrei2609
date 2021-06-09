
define l3 = Character(
    "Luna",
    window_background="gui/textbox/l3.png",
    color="#7E02BB",
    what_outlines=[( 1, "#7E02BB", 0, 0 )]
    )

init:
    $ l3_win = False
    $ love_l3_points = 10
    $ sex_l3_points = 0
    $ l3_cum = 0

screen l3_talk():
    use menu_talk(l3, love_l3_points, sex_l3_points, "l3_menu_stats")

screen l3_menu_stats():
    use girl_stats("l3", l3_win, "Luna", _("la Rock Star !"), _("La musique"), _("La cuisine"), "20", love_l3_points, sex_l3_points, l3_cum)



image FULL_luna_dos_1 = "Images/CG/01-Personnages/103-Luna/FULL-luna_dos_1.png"
image FULL_luna_dos_2 = "Images/CG/01-Personnages/103-Luna/FULL-luna_dos_2.png"
image FULL_luna_dos_3 = "Images/CG/01-Personnages/103-Luna/FULL-luna_dos_3.png"


image luna_zoom_1 = "Images/CG/01-Personnages/103-Luna/ZOOM-luna_seins.png"
image luna_zoom_2 = "Images/CG/01-Personnages/103-Luna/ZOOM-luna_chatte.png"


image luna_bar = "Images/Plans/Centre_Commercial/luna_bar.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
