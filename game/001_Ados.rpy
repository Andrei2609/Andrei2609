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





define carol = Character(
    "Carol",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )
define becky = Character(
    "Becky",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )
define dana = Character(
    "Dana",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )
define mandee = Character(
    "Mandee",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )
define jackie = Character(
    "Jackie",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )
define sam = Character(
    "Sam",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )


define paige = Character(
    "Paige",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )
define margo = Character(
    "Margo",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

screen carol_stats():
    frame:
        xalign 1.0 ypos 0
        has vbox
        imagebutton:
            idle "Images/Bases/Icones/stats.png"
            hover "Images/Bases/Icones/stats_hover.png"

            action ShowMenu("carol_menu_stats")
        label "Carol" xalign 0.5

init:
    $ love_carol_points = 10
    $ sex_carol_points = 0
    $ carol_win = False
    $ carol_tel = False
    $ carol_key = False

    $ love_sam_points = 10
    $ sex_sam_points = 0
    $ sam_win = False
    $ sam_tel = False
    $ sam_key = False

    $ love_paige_points = 10
    $ sex_paige_points = 0
    $ paige_win = False
    $ paige_tel = False
    $ paige_key = False

screen carol_menu_stats():
    use girl_stats("carol", carol_win, "Carol", _("la rivale de Lori"), _("???"), _("???"), "22", love_carol_points, sex_carol_points, "")

screen sam_menu_stats():
    use girl_stats("sam", sam_win, "Sam", _("la chérie de Luna"), _("???"), _("???"), "20", love_sam_points, sex_sam_points, "")

screen paige_menu_stats():
    use girl_stats("paige", paige_win, "Paige", _("camarade"), _("???"), _("???"), "18", love_paige_points, sex_paige_points, "")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
