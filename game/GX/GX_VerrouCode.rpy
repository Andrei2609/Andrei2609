init:
    $ code = ""
    $ codeBon = "3141"
    $ codeCheck = False
    $ codeMessage = ""

screen VerrouCode():
    imagemap:
        idle "Images/Mini-Jeux/Code/verrou_code.png"
        hover "Images/Mini-Jeux/Code/verrou_code_hover.png"
        xalign 1.0
        yalign 0.5

        hotspot (489,368,91,84) action Jump("VC_1")
        hotspot (581,368,83,84) action Jump("VC_2")
        hotspot (665,368,91,84) action Jump("VC_3")

        hotspot (490,454,89,81) action Jump("VC_4")
        hotspot (582,454,82,81) action Jump("VC_5")
        hotspot (666,454,89,81) action Jump("VC_6")

        hotspot (489,538,90,84) action Jump("VC_7")
        hotspot (581,538,81,84) action Jump("VC_8")
        hotspot (665,538,89,84) action Jump("VC_9")

        if codeMessage == "Code Bon":
            hotspot (998,417,179,129) action Jump("bunker_in")
        else:
            hotspot (998,417,179,129) action Jump("VC_verif")

        hotspot (28,611,95,67) action Jump("VC_exit")

    if codeCheck == False:
        label "[code]" xalign 0.5 yalign 0.2 text_size 100 text_font "FT_Open24.ttf"
    else:
        label "[codeMessage]" xalign 0.5 yalign 0.2 text_size 60 text_font "FT_Open24.ttf"

label VC_exit:
    $ code = ""
    jump jardin

label VC_1:
    $ codeMessage = ""
    $ codeCheck = False
    $ code += "1"
    call screen VerrouCode

label VC_2:
    $ codeMessage = ""
    $ codeCheck = False
    $ code += "2"
    call screen VerrouCode

label VC_3:
    $ codeMessage = ""
    $ codeCheck = False
    $ code += "3"
    call screen VerrouCode

label VC_4:
    $ codeMessage = ""
    $ codeCheck = False
    $ code += "4"
    call screen VerrouCode

label VC_5:
    $ codeMessage = ""
    $ codeCheck = False
    $ code += "5"
    call screen VerrouCode

label VC_6:
    $ codeMessage = ""
    $ codeCheck = False
    $ code += "6"
    call screen VerrouCode

label VC_7:
    $ codeMessage = ""
    $ codeCheck = False
    $ code += "7"
    call screen VerrouCode

label VC_8:
    $ codeMessage = ""
    $ codeCheck = False
    $ code += "8"
    call screen VerrouCode

label VC_9:
    $ codeMessage = ""
    $ codeCheck = False
    $ code += "9"
    call screen VerrouCode

label VC_verif:
    $ codeCheck = True
    if code == codeBon:
        $ code = ""
        $ codeMessage = "Code Bon"
        jump bunker_in
    elif True:
        $ code = ""
        $ codeMessage = "Code Faux"
    call screen VerrouCode
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
