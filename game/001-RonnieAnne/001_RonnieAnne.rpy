
define ronnie = Character(
    "Ronnie Anne",
    window_background="gui/textbox/neutre.png",
    color="#4B0082",
    what_outlines=[( 1, "#4B0082", 0, 0 )]
    )

init:
    $ ronnie_win = False
    $ love_ronnie_points = 15
    $ sex_ronnie_points = 0
    $ ronnie_tel = False

screen ronnie_talk():
    use menu_talk(ronnie, love_ronnie_points, sex_ronnie_points, "ronnie_menu_stats")

screen ronnie_menu_stats():
    use girl_stats("ronnie", ronnie_win, "Ronnie Anne", _("la bonne copine"), _("Les jeux vidéo"), _("Etre traité comme une fille"), "18", love_ronnie_points, sex_ronnie_points, "")


image ronnie_pose_1 = "Images/CG/01-Personnages/001-Ronnie_Anne/ronnie-anne_pose.png"
image ronnie_pose_2 = "Images/CG/01-Personnages/001-Ronnie_Anne/ronnie-anne_pose2.png"

image ronnie_selfi_1 = "Images/CG/01-Personnages/001-Ronnie_Anne/ronnie-anne_selfi_1.png"
image ronnie_selfi_2 = "Images/CG/01-Personnages/001-Ronnie_Anne/ronnie-anne_selfi_2.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
