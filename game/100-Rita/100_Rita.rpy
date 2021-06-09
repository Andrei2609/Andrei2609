
define mom = Character(
    "Rita",
    window_background="gui/textbox/mom.png",
    color="#F82D5E",
    what_outlines=[( 1, "#F82D5E", 0, 0 )]
    )

init:
    $ love_mom_points = 20
    $ sex_mom_points = 0
    $ mom_cum = 0


    $ mom_win = False
    $ mom_win_job = False
    $ mom_win_plage = False
    $ mom_win_shower = False
    $ mom_win_sleep = False


    $ mom_dog_house = False

screen mom_talk():
    use menu_talk(mom, love_mom_points, sex_mom_points, "mom_menu_stats")

screen mom_menu_stats():
    use girl_stats("mom", mom_win, "Rita", _("Maman"), _("La poésie"), _("Les corvées"), "40", love_mom_points, sex_mom_points, mom_cum)


image Rita_dos = "Images/CG/01-Personnages/100-Rita/rita_dos.png"
image Rita_sleep_dos = "Images/CG/01-Personnages/100-Rita/rita_sleep_dos.png"
image Rita_nue_dos = "Images/CG/01-Personnages/100-Rita/rita_nue_dos.png"


image Rita_niche_ass = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_ass.png"
image Rita_niche_ass_1 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_ass_1.png"

image Rita_niche_touch_KO_1 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_surprise_1.png"
image Rita_niche_touch_OK_1 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_excite_1.png"

image Rita_niche_touch_KO_2_1 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_surprise_2_1.png"
image Rita_niche_touch_KO_2_2 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_surprise_2_2.png"
image Rita_niche_touch_OK_2 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_excite_2.png"

image Rita_niche_touch_KO_3 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_surprise_3.png"
image Rita_niche_touch_KO_3_a = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_surprise_3_a.png"
image Rita_niche_touch_OK_3_1 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_excite_3_1.png"
image Rita_niche_touch_OK_3_2 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_excite_3_2.png"

image Rita_niche_touch_KO_4 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_surprise_4.png"
image Rita_niche_touch_OK_4_1 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_excite_4_1.png"
image Rita_niche_touch_OK_4_2 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_excite_4_2.png"
image Rita_niche_touch_OK_4_anim:
    "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_excite_4_1_a.png"
    pause .3
    "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_excite_4_2.png"
    pause .3
    repeat
image Rita_niche_fuck_1 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_fuck_1.png"
image Rita_niche_fuck_2:
    "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_fuck_2.png"
    pause .2
    "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_fuck_3.png"
    pause .2
    "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_fuck_4.png"
    pause .2
    repeat

image Rita_niche_cum_out_1 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_end_1.png"
image Rita_niche_cum_out_2 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_end_1_2.png"

image Rita_niche_cum_in_1 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_end_2.png"

image Rita_niche_face_1:
    "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_face.png"
    pause .5
    "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_face_1.png"
    pause .5
    repeat
image Rita_niche_face_2 = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_face_1.png"
image Rita_niche_miniass = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_miniass.png"
image Rita_niche_minilincoln = "Images/CG/01-Personnages/100-Rita/quest_1/rita_niche_minilincoln.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
