
define l1 = Character(
    "Lori",
    window_background="gui/textbox/l1.png",
    color="#00A6FF",
    what_outlines=[( 1, "#00A6FF", 0, 0 )]
    )

init:
    $ l1_win = False
    $ love_l1_points = 10
    $ sex_l1_points = 0
    $ l1_cum = 0

screen l1_talk():
    use menu_talk(l1, love_l1_points, sex_l1_points, "l1_menu_stats")

screen l1_menu_stats():
    use girl_stats("l1", l1_win, "Lori", _("la chipie"), _("Le golf"), _("Carol Pingrey"), "22", love_l1_points, sex_l1_points, l1_cum)


image lori_pose_1 = "Images/CG/01-Personnages/101-Lori/lori_pose.png"
image lori_pose_2 = "Images/CG/01-Personnages/101-Lori/lori_poseA.png"

image clyde_lori_fuck = "Images/CG/01-Personnages/101-Lori/clyde_lori_fuck.png"

image lori_BJ_1 = "Images/CG/01-Personnages/101-Lori/lori_suck.png"
image lori_BJ_2:
    "Images/CG/01-Personnages/101-Lori/lori_suckA.png"
    pause .3
    "Images/CG/01-Personnages/101-Lori/lori_suckB.png"
    pause .3
    repeat
image lori_BJ_3:
    "Images/CG/01-Personnages/101-Lori/lori_suckA.png"
    pause .1
    "Images/CG/01-Personnages/101-Lori/lori_suckB.png"
    pause .1
    repeat
image lori_BJ_cum_1 = "Images/CG/01-Personnages/101-Lori/lori_suckC.png"
image lori_BJ_cum_2 = "Images/CG/01-Personnages/101-Lori/lori_suckD.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
