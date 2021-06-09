define chloe = Character(
    "Chloé",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_chloe_points = 5
    $ sex_chloe_points = 0
    $ chloe_win = False
    $ chloe_tel = False
    $ chloe_key = False

screen chloe_menu_stats():
    use girl_stats("chloe", chloe_win, "Chloé", _("la petite amie de Clyde"), _("???"), _("???"), "18", love_chloe_points, sex_chloe_points, "")

screen chloe_talk():
    use menu_talk(chloe, love_chloe_points, sex_chloe_points, "chloe_menu_stats")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
