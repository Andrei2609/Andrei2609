
define l5 = Character(
    "Lynn",
    window_background="gui/textbox/l5.png",
    color="#FF0000",
    what_outlines=[( 1, "#FF0000", 0, 0 )]
    )

init:
    $ l5_win = False
    $ love_l5_points = 10
    $ sex_l5_points = 0
    $ l5_cum = 0

screen l5_talk():
    use menu_talk(l5, love_l5_points, sex_l5_points, "l5_menu_stats")

screen l5_menu_stats():
    use girl_stats("l5", l5_win, "Lynn Junior", _("la mauvaise joueuse"), _("Le sport"), _("Perdre"), "18", love_l5_points, sex_l5_points, l5_cum)


image Lynn_abdo_1:
    "Images/CG/01-Personnages/105-Lynn/lynn_abdo1.png"
    pause .99
    "Images/CG/01-Personnages/105-Lynn/lynn_abdo1-1.png"
    pause .99
    repeat
image Lynn_abdo_2 = "Images/CG/01-Personnages/105-Lynn/lynn_abdo2.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
