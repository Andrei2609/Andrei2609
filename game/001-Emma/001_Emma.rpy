define emma = Character(
    "Emma",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_emma_points = 5
    $ sex_emma_points = 0
    $ emma_win = False
    $ emma_tel = False
    $ emma_key = False

screen emma_menu_stats():
    use girl_stats("emma", emma_win, "Emma", _("camarade"), _("???"), _("???"), "18", love_emma_points, sex_emma_points, "")

screen emma_talk():
    use menu_talk(emma, love_emma_points, sex_emma_points, "emma_menu_stats")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
