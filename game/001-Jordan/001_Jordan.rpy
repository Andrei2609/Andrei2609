define jordan = Character(
    "Jordan",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_jordan_points = 5
    $ sex_jordan_points = 0
    $ jordan_win = False
    $ jordan_tel = False
    $ jordan_key = False
    $ casier_key_5 = False

screen jordan_menu_stats():
    use girl_stats("jordan", jordan_win, "Jordan", _("camarade"), _("???"), _("???"), "18", love_jordan_points, sex_jordan_points, "")

screen jordan_talk():
    use menu_talk(jordan, love_jordan_points, sex_jordan_points, "jordan_menu_stats")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
