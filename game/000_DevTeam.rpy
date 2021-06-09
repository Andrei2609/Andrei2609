screen debug():
    vbox:
        xalign 0
        yalign 1.0
        textbutton "+1000$":
            action SetVariable("user_coins", user_coins + 1000)
        textbutton "-1000$":
            action SetVariable("user_coins", user_coins - 1000)
        textbutton "+1 bouteille":
            action SetVariable("bouteille", bouteille + 1)
        textbutton "-1 bouteille":
            action SetVariable("bouteille", bouteille - 1)
        textbutton "+ 100 santé":
            action SetVariable("vie_points", vie_points + 100)
        textbutton "- 100 santé":
            action SetVariable("vie_points", vie_points - 100)
        textbutton "+ 10 sex":
            action SetVariable("sex_points", sex_points + 10)
        textbutton "0 sex":
            action SetVariable("sex_points", 0)
        textbutton "+ 10 int":
            action SetVariable("int_points", int_points + 10)
        textbutton "leni sex":
            action SetVariable("sex_l2_points", 100)
        textbutton "leni love":
            action SetVariable("love_l2_points", 100)
        textbutton "mardi":
            action SetVariable("jour", 2)
        textbutton "jeudi":
            action SetVariable("jour", 4)
        textbutton "dimanche":
            action SetVariable("jour", 7)
        textbutton "Quit":
            action Return(True)


define k = Character(
    _("Développeur"),
    color="#6d071a",
    window_background="gui/textbox/neutre.png",
    what_outlines=[( 1, "#6d071a", 0, 0 )],
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle'
    )

define d = Character(
    _("Illustratrice"),
    color="#9FE855",
    window_background="gui/textbox/neutre.png",
    what_outlines=[( 1, "#9FE855", 0, 0 )],
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle'
    )



image d = "Images/Personnages/000-Intervenants/Actif/dodo_Normal.png"
image d_P:
    "Images/Personnages/000-Intervenants/Actif/dodo_P.png"
    pause .5
    "Images/Personnages/000-Intervenants/Actif/dodo_Normal.png"
    pause .5
    repeat
image d_H = "Images/Personnages/000-Intervenants/Actif/dodo_H.png"


image I_d = "Images/Personnages/000-Intervenants/Inactif/dodo_Normal.png"



image k = "Images/Personnages/000-Intervenants/Actif/kinou_Normal.png"
image k_P:
    "Images/Personnages/000-Intervenants/Actif/kinou_P.png"
    pause .5
    "Images/Personnages/000-Intervenants/Actif/kinou_Normal.png"
    pause .5
    repeat
image k_H = "Images/Personnages/000-Intervenants/Actif/kinou_H.png"
image k_Oeil = "Images/Personnages/000-Intervenants/Actif/kinou_oeil.png"


image I_k = "Images/Personnages/000-Intervenants/Inactif/kinou_Normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
