
init -1000 python:

    import os.path

    def Img(file):
        if os.path.isfile("images/%d/%s.png" % (1080,file)):
            return "images/%d/%s.png" % (1080,file)
        else:
            return "images/%d/%s.jpg" % (1080,file)

    def get_image(file):
        return "images/%s" % file

init -100 python:

    store.selected_slot = "_"
    persistent._file_page = 1


init:

    transform center:
        xalign 0.5
        xanchor 0.5
        yanchor 0.0

    transform left:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0

    transform right:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0

    transform fleft:
        xalign 0.16
        xanchor 0.5
        yanchor 0.0

    transform fright:
        xalign 0.84
        xanchor 0.5
        yanchor 0.0

    transform cleft:
        xalign 0.355
        xanchor 0.5
        yanchor 0.0

    transform cright:
        xalign 0.645
        xanchor 0.5
        yanchor 0.0





init:

    define dis = Dissolve(0.5, alpha=True)
    $ flash = Fade(.25, 0, .75, color="#fff")

    $ none                     = "images/misc/none.png"
    image NoneImage = "images/misc/none.png"
    image black = "#000"
    image white = "#fff"
    image bg black = "#000"
    image bg white = "#fff"

    image bg map = get_image("maps/map_available.jpg")
    image bg hall = im.Sepia(get_image("bg/int_dining_hall_day.jpg"))

    image ctc_animation = Animation("images/misc/ctc01.png", 0.15, "images/misc/ctc02.png", 0.15, "images/misc/ctc03.png", 0.15, "images/misc/ctc04.png", 0.15, "images/misc/ctc05.png", 0.15, "images/misc/ctc06.png", 0.15, "images/misc/ctc07.png", 0.15, "images/misc/ctc08.png", 0.15, xpos=0.905, ypos=0.98, xanchor=1.0, yanchor=1.0)

    image ctc_animation_nvl = Animation("images/misc/ctc01.png", 0.15, "images/misc/ctc02.png", 0.15, "images/misc/ctc03.png", 0.15, "images/misc/ctc04.png", 0.15, "images/misc/ctc05.png", 0.15, "images/misc/ctc06.png", 0.15, "images/misc/ctc07.png", 0.15, "images/misc/ctc08.png", 0.15, xpos=0.9, ypos=0.94, xanchor=1.0, yanchor=1.0)

    image op_uv:
        "images/misc/op/uv1.png"
        pause 0.5
        "images/misc/op/uv2.png"
        pause 0.5
        "images/misc/op/uv3.png"
        pause 0.5
        "images/misc/op/uv2.png"
        pause 0.5
        "images/misc/op/uv1.png"
        pause 0.5

    image stars:
        "images/anim/stars_1.jpg" with Dissolve(1.5)
        pause 1.5
        "images/anim/stars_3.jpg" with Dissolve(1.5)
        pause 1.5
        repeat

    image candle:
        "images/anim/candle_1.png" with Dissolve(2.0)
        pause 2.0
        "images/anim/candle_2.png" with Dissolve(2.0)
        pause 2.0
        repeat

    image prologue_dream:
        "images/anim/prologue_1.png"
        pause 0.1
        "images/anim/prologue_2.png"
        pause 0.1
        "images/anim/prologue_3.png"
        pause 0.1
        "images/anim/prologue_2.png"
        repeat

    image unblink:
        contains:
            "anim blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "anim blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image blink:
        contains:
            "anim blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "anim blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0


    image blinking:
        contains:
            "anim blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "anim blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0
        pause 2.0
        contains:
            "anim blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "anim blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image anim 1_prologue:
        "anim prologue_keyboard_1"
        pause 6
        "anim prologue_keyboard_2"
        pause 0.1
        "anim prologue_keyboard_3"
        pause 0.1
        "anim prologue_keyboard_4"
        pause 3
        "anim prologue_keyboard_3"
        pause 0.1
        "anim prologue_keyboard_2"
        pause 0.1
        "anim prologue_keyboard_1"

    image anim 2_prologue:
        "anim prologue_keyboard_monitor_1"
        pause 6
        "anim prologue_keyboard_monitor_2"
        pause 0.1
        "anim prologue_keyboard_monitor_3"
        pause 0.1
        "anim prologue_keyboard_monitor_4"
        pause 3
        "anim prologue_keyboard_monitor_3"
        pause 0.1
        "anim prologue_keyboard_monitor_2"
        pause 0.1
        "anim prologue_keyboard_monitor_1"

    image anim 3_prologue:
        "anim prologue_monitor_1"
        pause 6
        "anim prologue_monitor_2"
        pause 0.1
        "anim prologue_monitor_3"
        pause 0.1
        "anim prologue_monitor_4"

    image anim 4_prologue:
        "anim prolog_15"
        pause 6
        "anim prolog_3" with fade3
        pause 3
        "anim prolog_4" with fade3

    image owl:
        "anim owl_1"
        pause 5
        "anim owl_2"
        pause 0.5
        repeat

    image bg ext_square_night_flash:
        "bg ext_square_night" with Fade(1, 0.5, 1, color="#fff")
        pause 3
        "bg ext_square_night" with Fade(1, 0.5, 1, color="#fff")
        pause 3
        repeat

    image un_ending_bad:
        "cg epilogue_un_bad" with Dissolve(2.0)
        pause 2
        "cg epilogue_un_bad_red" with Dissolve(2.0)
        pause 2
        repeat

    image op_uv:
        "images/misc/op/uv1.png"
        pause 0.5
        "images/misc/op/uv2.png"
        pause 0.5
        "images/misc/op/uv3.png"
        pause 0.5
        "images/misc/op/uv2.png"
        pause 0.5
        "images/misc/op/uv1.png"
        pause 0.5

    $ m = chr(0)*85+chr(128)*86+chr(255)*85
    image bg ext_camp_entrance_day_sepia = im.Sepia(im.MatrixColor(im.Map("images/bg/ext_camp_entrance_day.jpg",m,m,m), im.matrix.hue(180)))

    image black_long:
        "bg ext_camp_entrance_day_sepia" with Dissolve(2.0)
        "bg black" with Dissolve(50.0)


    $ style.credits = Style(style.default)
    $ style.credits.font  = "fonts/corbelb.ttf"
    $ style.credits.color = "#fff"
    $ style.credits.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.credits.drop_shadow_color = "#000"
    $ style.credits.italic = False
    $ style.credits.bold = False
    $ style.credits.text_align = 0.5
    $ style.credits.xmaximum = 0.8

    image credits = ParameterizedText(style = "credits", size = 50)

    $ style.urhere1 = Style(style.default)
    $ style.urhere1.color = "#eee"
    $ style.urhere1.drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ]
    $ style.urhere1.drop_shadow_color = "#000"
    $ style.urhere1.italic = True
    $ style.urhere1.bold = False

    image urhere1 = ParameterizedText(style = "urhere1", size = 40)

    $ style.urhere2 = Style(style.default)
    $ style.urhere2.color = "#111"
    $ style.urhere2.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.urhere2.drop_shadow_color = "#000"
    $ style.urhere2.italic = False
    $ style.urhere2.bold = False

    image urhere2 = ParameterizedText(style = "urhere2", size = 80)

    $ style.urhere3 = Style(style.default)
    $ style.urhere3.color = "#a3d"
    $ style.urhere3.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.urhere3.drop_shadow_color = "#000"
    $ style.urhere3.italic = False
    $ style.urhere3.bold = False

    image urhere3 = ParameterizedText(style = "urhere3", size = 60)

    $ style.urhere4 = Style(style.default)
    $ style.urhere4.color = "#e34"
    $ style.urhere4.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.urhere4.drop_shadow_color = "#000"
    $ style.urhere4.italic = False
    $ style.urhere4.bold = False

    image urhere4 = ParameterizedText(style = "urhere4", size = 100)

    $ style.urhere5 = Style(style.default)
    $ style.urhere5.color = "#d00"
    $ style.urhere5.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.urhere5.drop_shadow_color = "#000"
    $ style.urhere5.italic = False
    $ style.urhere5.bold = False

    image urhere5 = ParameterizedText(style = "urhere5", size = 50)



    $ style.urhere6 = Style(style.default)
    $ style.urhere6.color = "#e01"
    $ style.urhere6.drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ]
    $ style.urhere6.drop_shadow_color = "#000"
    $ style.urhere6.italic = True
    $ style.urhere6.bold = False

    image urhere6 = ParameterizedText(style = "urhere6", size = 60)

    $ style.urhere7 = Style(style.default)
    $ style.urhere7.color = "#ad5"
    $ style.urhere7.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.urhere7.drop_shadow_color = "#000"
    $ style.urhere7.italic = False
    $ style.urhere7.bold = False

    image urhere7 = ParameterizedText(style = "urhere7", size = 30)

    $ style.urhere8 = Style(style.default)
    $ style.urhere8.color = "#a30"
    $ style.urhere8.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.urhere8.drop_shadow_color = "#000"
    $ style.urhere8.italic = False
    $ style.urhere8.bold = True

    image urhere8 = ParameterizedText(style = "urhere8", size = 70)

    $ style.urhere8 = Style(style.default)
    $ style.urhere8.color = "#f54"
    $ style.urhere8.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.urhere8.drop_shadow_color = "#000"
    $ style.urhere8.italic = True
    $ style.urhere8.bold = False

    image urhere8 = ParameterizedText(style = "urhere8", size = 90)

    $ style.urhere9 = Style(style.default)
    $ style.urhere9.color = "#d10"
    $ style.urhere9.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.urhere9.drop_shadow_color = "#000"
    $ style.urhere9.italic = False
    $ style.urhere9.bold = False

    image urhere9 = ParameterizedText(style = "urhere9", size = 65)

    $ style.urhere10 = Style(style.default)
    $ style.urhere10.color = "#ee1"
    $ style.urhere10.drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ]
    $ style.urhere10.drop_shadow_color = "#000"
    $ style.urhere10.italic = True
    $ style.urhere10.bold = False

    image urhere10 = ParameterizedText(style = "urhere10", size = 30)


init:
    $ std_set_for_preview = {}
    $ std_set = {}
    $ store.colors = {}
    $ store.names = {}
    $ store.names_list = []
    $ time_of_day = 'night'


    $ _show_two_window = True


    $ colors['voice'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
    $ names['voice'] = translation["voice"][_preferences.language]
    $ store.names_list.append('voice')


    $ colors['me'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
    $ names['me'] = translation["Semyon"][_preferences.language]
    $ store.names_list.append('me')


    $ colors['my'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
    $ names['my'] = translation["Myself"][_preferences.language]
    $ store.names_list.append('my')



    $ store.names_list.append('narrator')



    $ store.names_list.append('th')
    $ th_prefix = "~ "
    $ th_suffix = " ~"



    $ colors['el'] = {'night': (205, 205, 0, 255), 'sunset': (255, 255, 0, 255), 'day': (255, 255, 0, 255), 'prolog': (255, 255, 0, 255)}
    $ names['el'] = translation["el"][_preferences.language]
    $ store.names_list.append('el')

    $ colors['elp'] = {'night': (205, 205, 0, 255), 'sunset': (255, 255, 0, 255), 'day': (255, 255, 0, 255), 'prolog': (255, 255, 0, 255)}
    $ names['elp'] = translation["pi"][_preferences.language]
    $ store.names_list.append('elp')

    $ colors['ro'] = {'night': (205, 205, 0, 255), 'sunset': (255, 255, 0, 255), 'day': (255, 255, 0, 255), 'prolog': (255, 255, 0, 255)}
    $ names['ro'] = translation["Router"][_preferences.language]
    $ store.names_list.append('ro')



    $ colors['un'] = {'night': (170, 100, 217, 255), 'sunset': (185, 86, 255, 255), 'day': (185, 86, 255, 255), 'prolog': (185, 86, 255, 255)}
    $ names['un'] = translation["un"][_preferences.language]
    $ store.names_list.append('un')

    $ colors['unp'] = {'night': (170, 100, 217, 255), 'sunset': (185, 86, 255, 255), 'day': (185, 86, 255, 255), 'prolog': (185, 86, 255, 255)}
    $ names['unp'] = translation["pika"][_preferences.language]
    $ store.names_list.append('unp')



    $ colors['dv'] = {'night': (210, 139, 16, 255), 'sunset': (255, 170, 0, 255), 'day': (255, 170, 0, 255), 'prolog': (255, 170, 0, 255)}
    $ names['dv'] = translation["dv"][_preferences.language]
    $ store.names_list.append('dv')

    $ colors['dvp'] = {'night': (210, 139, 16, 255), 'sunset': (255, 170, 0, 255), 'day': (255, 170, 0, 255), 'prolog': (255, 170, 0, 255)}
    $ names['dvp'] = translation["pika"][_preferences.language]
    $ store.names_list.append('dvp')

    $ colors['dvg'] = {'night': (210, 139, 16, 255), 'sunset': (255, 170, 0, 255), 'day': (255, 170, 0, 255), 'prolog': (255, 170, 0, 255)}
    $ names['dvg'] = translation["Girl"][_preferences.language]
    $ store.names_list.append('dvg')



    $ colors['sl'] = {'night': (214, 176, 0, 255), 'sunset': (255, 210, 0, 255), 'day': (255, 210, 0, 255), 'prolog': (255, 210, 0, 255)}
    $ names['sl'] = translation["sl"][_preferences.language]
    $ store.names_list.append('sl')

    $ colors['slp'] = {'night': (214, 176, 0, 255), 'sunset': (255, 210, 0, 255), 'day': (255, 210, 0, 255), 'prolog': (255, 210, 0, 255)}
    $ names['slp'] = translation["pika"][_preferences.language]
    $ store.names_list.append('slp')

    $ colors['slg'] = {'night': (214, 176, 0, 255), 'sunset': (255, 210, 0, 255), 'day': (255, 210, 0, 255), 'prolog': (255, 210, 0, 255)}
    $ names['slg'] = translation["Girl"][_preferences.language]
    $ store.names_list.append('slg')

    $ colors['sa'] = {'night': (214, 176, 0, 255), 'sunset': (255, 210, 0, 255), 'day': (255, 210, 0, 255), 'prolog': (255, 210, 0, 255)}
    $ names['sa'] = translation["Sasha"][_preferences.language]
    $ store.names_list.append('sa')



    $ colors['us'] = {'night': (234, 55, 0, 255), 'sunset': (255, 50, 0, 255), 'day': (255, 50, 0, 255), 'prolog': (255, 50, 0, 255)}
    $ names['us'] = translation["us"][_preferences.language]
    $ store.names_list.append('us')

    $ colors['usp'] = {'night': (234, 55, 0, 255), 'sunset': (255, 50, 0, 255), 'day': (255, 50, 0, 255), 'prolog': (255, 50, 0, 255)}
    $ names['usp'] = translation["pika"][_preferences.language]
    $ store.names_list.append('usp')

    $ colors['usg'] = {'night': (234, 55, 0, 255), 'sunset': (255, 50, 0, 255), 'day': (255, 50, 0, 255), 'prolog': (255, 50, 0, 255)}
    $ names['usg'] = translation["Girl"][_preferences.language]
    $ store.names_list.append('usg')



    $ colors['mt'] = {'night': (0, 182, 39, 255), 'sunset': (0, 234, 50, 255), 'day': (0, 234, 50, 255), 'prolog': (0, 234, 50, 255)}
    $ names['mt'] = translation["mt"][_preferences.language]
    $ store.names_list.append('mt')

    $ colors['mtp'] = {'night': (0, 182, 39, 255), 'sunset': (0, 234, 50, 255), 'day': (0, 234, 50, 255), 'prolog': (0, 234, 50, 255)}
    $ names['mtp'] = translation["Camp_leader"][_preferences.language]
    $ store.names_list.append('mtp')



    $ colors['cs'] = {'night': (134, 134, 230, 255), 'sunset': (165, 165, 255, 255), 'day': (165, 165, 255, 255), 'prolog': (165, 165, 255, 255)}
    $ names['cs'] = translation["cs"][_preferences.language]
    $ store.names_list.append('cs')

    $ colors['csp'] = {'night': (134, 134, 230, 255), 'sunset': (165, 165, 255, 255), 'day': (165, 165, 255, 255), 'prolog': (165, 165, 255, 255)}
    $ names['csp'] = translation["Nurse"][_preferences.language]
    $ store.names_list.append('csp')



    $ colors['mz'] = {'night': (84, 129, 219, 255), 'sunset': (114, 160, 255, 255), 'day': (74, 134, 255, 255), 'prolog': (74, 134, 255, 255)}
    $ names['mz'] = translation["mz"][_preferences.language]
    $ store.names_list.append('mz')

    $ colors['mzp'] = {'night': (84, 129, 219, 255), 'sunset': (114, 160, 255, 255), 'day': (74, 134, 255, 255), 'prolog': (74, 134, 255, 255)}
    $ names['mzp'] = translation["pika"][_preferences.language]
    $ store.names_list.append('mzp')



    $ colors['mi'] = {'night': (0, 180, 207, 255), 'sunset': (0, 252, 255, 255), 'day': (0, 222, 255, 255), 'prolog': (0, 222, 255, 255)}
    $ names['mi'] = translation["mi"][_preferences.language]
    $ store.names_list.append('mi')

    $ colors['mip'] = {'night': (0, 180, 207, 255), 'sunset': (0, 252, 255, 255), 'day': (0, 222, 255, 255), 'prolog': (0, 222, 255, 255)}
    $ names['mip'] = translation["pika"][_preferences.language]
    $ store.names_list.append('mip')

    $ colors['ma'] = {'night': (0, 180, 207, 255), 'sunset': (0, 252, 255, 255), 'day': (0, 222, 255, 255), 'prolog': (0, 222, 255, 255)}
    $ names['ma'] = translation["Masha"][_preferences.language]
    $ store.names_list.append('ma')



    $ colors['uv'] = {'night': (64, 208, 0, 255), 'sunset': (78, 255, 0, 255), 'day': (78, 255, 0, 255), 'prolog': (78, 255, 0, 255)}
    $ names['uv'] = translation["uv"][_preferences.language]
    $ store.names_list.append('uv')

    $ colors['uvp'] = {'night': (64, 208, 0, 255), 'sunset': (78, 255, 0, 255), 'day': (78, 255, 0, 255), 'prolog': (78, 255, 0, 255)}
    $ names['uvp'] = translation["Strange_girl"][_preferences.language]
    $ store.names_list.append('uvp')



    $ colors[ 'sh'] = {'night': (205, 194, 18, 255), 'sunset': (255, 242, 38, 255), 'day': (255, 242, 38, 255), 'prolog': (255, 242, 38, 255)}
    $ names['sh'] = translation["sh"][_preferences.language]
    $ store.names_list.append('sh')

    $ colors[ 'shp'] = {'night': (205, 194, 18, 255), 'sunset': (255, 242, 38, 255), 'day': (255, 242, 38, 255), 'prolog': (255, 242, 38, 255)}
    $ names['shp'] = translation["pi"][_preferences.language]
    $ store.names_list.append('shp')


    $ colors['pi'] = {'night': (230, 0, 0, 255), 'sunset': (230, 0, 0, 255), 'day': (230, 1, 1, 255), 'prolog': (230, 0, 0, 255)}
    $ names['pi'] = translation["pi"][_preferences.language]
    $ store.names_list.append('pi')


    $ colors['all'] = {'night': (227, 58, 58, 255), 'sunset': (227, 58, 58, 255), 'day': (237, 68, 68, 255), 'prolog': (227, 58, 58, 255)}
    $ names['all'] = translation["all"][_preferences.language]
    $ store.names_list.append('all')


    $ colors['dreamgirl'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
    $ names['dreamgirl'] = translation["dreamgirl"][_preferences.language]
    $ store.names_list.append('dreamgirl')


    $ colors['bush'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
    $ names['bush'] = translation["bush"][_preferences.language]
    $ store.names_list.append('bush')


    $ colors['FIXME_voice'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
    $ names['FIXME_voice'] = translation["FIXME_voice"][_preferences.language]
    $ store.names_list.append('FIXME_voice')


    $ colors['odn'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
    $ names['odn'] = translation["odn"][_preferences.language]
    $ store.names_list.append('odn')



    $ colors['message'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
    $ names['message'] = translation["message"][_preferences.language]
    $ store.names_list.append('message')



    $ colors['mt_voice'] = {'night': (0, 182, 39, 255), 'sunset': (0, 234, 50, 255), 'day': (0, 234, 50, 255), 'prolog': (0, 234, 50, 255)}
    $ names['mt_voice'] = translation["mt_voice"][_preferences.language]
    $ store.names_list.append('mt_voice')






init python:

    def char_define(x,is_nvl=False):
        global DynamicCharacter
        global _show_two_window
        global nvl
        global store
        global time_of_day
        gl = globals()
        v = "_voice"
        if  x == 'narrator':
            if  is_nvl:
                gl['narrator'] = Character(None, kind=nvl, what_style="narrator_%s"%time_of_day, ctc="ctc_animation_nvl", ctc_position="fixed")
            else:
                gl['narrator'] = Character(None, what_style="narrator_%s"%time_of_day, ctc="ctc_animation", ctc_position="fixed")
            return
        if  x == 'th':
            if  is_nvl:
                gl['th'] = Character(None, kind=nvl, what_style="thoughts_%s"%time_of_day,what_prefix = th_prefix,what_suffix=th_suffix, ctc="ctc_animation_nvl", ctc_position="fixed")
            else:
                gl['th'] = Character(None, what_style="thoughts_%s"%time_of_day,what_prefix = th_prefix,what_suffix=th_suffix, ctc="ctc_animation", ctc_position="fixed")
            return
        if  is_nvl:
            gl[x] = DynamicCharacter("%s_name"%x, color=store.colors[x][time_of_day], kind=nvl, what_style="normal_%s"%time_of_day,who_suffix=":", ctc="ctc_animation_nvl", ctc_position="fixed")
            gl["%s_name"%x] = store.names[x]
        else:
            gl[x] = DynamicCharacter("%s_name"%x, color=store.colors[x][time_of_day], show_two_window=_show_two_window,  what_style="normal_%s"%time_of_day, ctc="ctc_animation", ctc_position="fixed")
            gl["%s_name"%x] = store.names[x]

    def set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global store
        for x in store.names_list:
            char_define(x)

    def set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global narrator
        global th
        narrator_nvl = narrator
        th_nvl = th
        
        global store
        for x in store.names_list:
            char_define(x,True)

    def reload_names():
        global store
        for x in store.names_list:
            char_define(x)

    set_mode_adv()
    reload_names()


init:
    if _preferences.language == "english":
        image widget map = get_image("maps/map_en.jpg")
    elif _preferences.language == "spanish":
        image widget map = get_image("maps/map_es.jpg")
    elif _preferences.language == "italian":
        image widget map = get_image("maps/map_it.jpg")
    elif _preferences.language == "chinese":
        image widget map = get_image("maps/map_ch.jpg")
    else:
        image widget map = get_image("maps/map.jpg")


init -997 python:
    def bg_tmp_image(bgname):
        renpy.image("text "+bgname,LiveComposite((config.screen_width, config.screen_height),(0, 0),"#ffff7f",(50, 150),Text(u"А здесь будет фон про "+bgname, size=40, color="6A7183")))
        return "text "+bgname

    if _preferences.language == "english":
        store.map_pics = {
            "bgpic": get_image("maps/map_en.jpg"),
            "available": get_image("maps/map_en_available.jpg"),
            "selected": get_image("maps/map_en_selected.jpg")
        }
    elif _preferences.language == "spanish":
        store.map_pics = {
            "bgpic": get_image("maps/map_es.jpg"),
            "available": get_image("maps/map_es_available.jpg"),
            "selected": get_image("maps/map_es_selected.jpg")
        }
    elif _preferences.language == "italian":
        store.map_pics = {
            "bgpic": get_image("maps/map_it.jpg"),
            "available": get_image("maps/map_it_available.jpg"),
            "selected": get_image("maps/map_it_selected.jpg")
        }
    elif _preferences.language == "chinese":
        store.map_pics = {
            "bgpic": get_image("maps/map_ch.jpg"),
            "available": get_image("maps/map_ch_available.jpg"),
            "selected": get_image("maps/map_ch_selected.jpg")
        }
    else:
        store.map_pics = {
            "bgpic": get_image("maps/map.jpg"),
            "available": get_image("maps/map_available.jpg"),
            "selected": get_image("maps/map_selected.jpg")
        }


    store.map_zones = {
            "me_mt_house":   {"position":[825,47,1005,230],"default_bg":bg_tmp_image(u"Мой домик")},
            "estrade":       {"position":[1039,47,1288,230],"default_bg":bg_tmp_image(u"Эстрада")},
            "music_club":    {"position":[541,231,711,356],"default_bg":bg_tmp_image(u"Музклуб")},
            "square":        {"position":[825,357,1005,665],"default_bg":bg_tmp_image(u"Площадь")},
            "dining_hall":   {"position":[1006,457,1159,665],"default_bg":bg_tmp_image(u"Столовая")},
            "sport_area":    {"position":[1160,457,1578,665],"default_bg":bg_tmp_image(u"Спорткомплекс")},
            "beach":         {"position":[1160,666,1578,871],"default_bg":bg_tmp_image(u"Пляж")},
            "boat_station":  {"position":[825,666,1005,871],"default_bg":bg_tmp_image(u"Лодочный причал")},
            "clubs":         {"position":[418,357,711,665],"default_bg":bg_tmp_image(u"Клубы")},
            "library":       {"position":[1160,231,1288,456],"default_bg":bg_tmp_image(u"Библиотека")},
            "medic_house":   {"position":[1039,231,1159,456],"default_bg":bg_tmp_image(u"Медпункт")},
            "camp_entrance": {"position":[278,357,417,665],"default_bg":bg_tmp_image(u"Ворота в лагерь")},
            "forest":        {"position":[541,47,711,230],"default_bg":bg_tmp_image(u"о. Лес")}
        
        
    }

    store.map_chibi = {
        "?" : get_image("maps/map_icon_n00.png"),
        "me": get_image("maps/map_icon_n01.png"),
        "mi": get_image("maps/map_icon_n02.png"),
        "sh": get_image("maps/map_icon_n03.png"),
        "el": get_image("maps/map_icon_n04.png"),
        "mz": get_image("maps/map_icon_n05.png"),
        "mt": get_image("maps/map_icon_n06.png"),
        "uv": get_image("maps/map_icon_n07.png"),
        "un": get_image("maps/map_icon_n08.png"),
        "us": get_image("maps/map_icon_n09.png"),
        "dv": get_image("maps/map_icon_n10.png"),
        "sl": get_image("maps/map_icon_n11.png"),
        "cs": get_image("maps/map_icon_n12.png"),
    }



init -10 python:
    avatar_frame = Frame("images/misc/avaframe.png", 5, 5)
    card_down = "images/misc/down.png"
    card_up = "images/misc/up.png"
    p = "images/avatars/dv/dv-"
    dv_avatar_set = {
             'body':p+"body.png",
             -2    :p+"emo9.png",
             -1    :p+"emo8.png",
             0     :p+"emo6.png",
             1     :p+"emo12.png",
             2     :p+"smile.png",
        }
    p = "images/avatars/sl/sl-"
    sl_avatar_set = {
             'body':p+"body.png",
             -2    :p+"emo04.png",
             -1    :p+"emo01.png",
             0     :p+"emo05.png",
             1     :p+"emo02.png",
             2     :p+"emo03.png",
        }
    p = "images/avatars/un/un-"
    un_avatar_set = {
             'body':p+"body.png",
             -2    :p+"emo07.png",
             -1    :p+"emo08.png",
             0     :p+"emo02.png",
             1     :p+"emo01.png",
             2     :p+"emo10.png",
        }
    p = "images/avatars/us/us-"
    us_avatar_set = {
             'body':p+"body.png",
             -2    :p+"emo01.png",
             -1    :p+"emo11.png",
             0     :p+"emo02.png",
             1     :p+"emo03.png",
             2     :p+"emo09.png",
        }





init -1001 python:

    renpy.music.register_channel("sound", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound_loop", "voice", True)
    renpy.music.register_channel("sound_loop2", "voice", True)
    renpy.music.register_channel("sound_loop3", "voice", True)
    renpy.music.register_channel("ambience", "voice", True)

    def volume(vol, chnl):
        renpy.music.set_volume(vol, channel=chnl)

    def stop_music():
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music"):
            renpy.music.stop(channel=chnl)