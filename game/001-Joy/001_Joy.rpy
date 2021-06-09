define joy = Character(
    "Joy",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_joy_points = 5
    $ sex_joy_points = 0
    $ joy_win = False
    $ joy_tel = False
    $ joy_key = False

screen joy_menu_stats():
    use girl_stats("joy", joy_win, "Joy", _("camarade"), _("???"), _("???"), "18", love_joy_points, sex_joy_points, "")

screen joy_talk():
    use menu_talk(joy, love_joy_points, sex_joy_points, "joy_menu_stats")



image Joy_school_ass = "Images/CG/01-Personnages/001-Joy/joy_ass.png"
image Joy_school_exciter = "Images/CG/01-Personnages/001-Joy/joy_exciter.png"
image Joy_school_claque_1 = "Images/CG/01-Personnages/001-Joy/joy_claque_1.png"
image Joy_school_claque_2 = "Images/CG/01-Personnages/001-Joy/joy_claque_2.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
