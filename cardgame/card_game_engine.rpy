
init 2 python:

    screen_width = 1920
    screen_height = 1080

    n_cards        = 7
    n_xchanges     = 2
    n_cycles       = 3


    prefix  = "images/cards/"
    types   = ["2ch","ussr","utan","uvao"]
    suffix  = ".png"
    card_height    = 315
    card_width     = 210
    card_dx        = 225
    card_left_dx   = 50
    card_top_dy    = 50
    button_dx      = 0
    button_dy      = 0
    bottom_dy      = 0
    bottom_dy_result = 0

    card_bottom_dy = screen_height - card_top_dy - card_height - bottom_dy

    cards_bg       = None
    card_time_koef = 1.0/7.0

    VISIBLE   = True
    INVISIBLE = False
    CARD_GAME_WITH_EXCHANGE = False


    name_of_none = (0,"none")

    def get_img(img):
        global prefix
        return im.Scale(prefix+img+suffix,card_width,card_height)


    arrow_width = 50

    ints = range(1,14)
    card_img={}
    card_img["cover"] = get_img("cover")
    card_img[name_of_none] = "images/misc/none.png"

    for i in ints:
        for j in types:
            name = "%d_%s"%(i,j)
            card_img[(i,j)] = get_img(name)

    def generate_cards(bg,dialogs):
        global cards_bg
        global game_interuptions
        global cards_my
        global cards_rival
        global cycles_left
        global changes_left
        global cards_state
        global result_status
        
        cards_bg = bg
        game_interuptions = dialogs
        cycles_left  = n_cycles
        changes_left = n_xchanges
        cards_state = "init"
        result_status = "in_progress"
        
        k = 0
        cset = []
        while k<2*n_cards:
            name = (renpy.random.randint(1,13),types[renpy.random.randint(0,3)])
            if  not name in cset:
                cset.append(name)
                k += 1
        
        cards_rival = []
        for i in range(0,n_cards):
            rival = []
            rival.visible = 'INVISIBLE'
            rival.name = cset[i]
            rival.interesting = False
            rival.hot = False
            rival.allow = False
            rival.x = int((screen_width - card_width )/2.0)
            rival.y = int((screen_height- card_height)/2.0)
            rival.dy = 0
            cards_rival.append(rival)
        
        cards_my    = []
        for i in range(0,n_cards):
            my = []
            my.visible = 'VISIBLE'
            my.interesting = False
            my.hot = False
            my.allow = False
            my.name = cset[n_cards+i]
            my.x = int((screen_width - card_width )/2.0)
            my.y = int((screen_height- card_height)/2.0)
            my.dy = 0
            cards_my.append(my)
        
        
        if  not CARD_GAME_WITH_EXCHANGE:
            cards_rival[0].name = name_of_none
            cards_my[0].name = name_of_none
        
        if cards_state == "init":
            
            deal_cards = {"1":"sound/sfx/cardgame/new/deal_card_1.ogg","2":"sound/sfx/cardgame/new/deal_card_2.ogg","3":"sound/sfx/cardgame/new/deal_card_3.ogg","4":"sound/sfx/cardgame/new/deal_card_4.ogg" }
            
            from random import randint
            deal_card = deal_cards[str(randint(1,4))]
            
            renpy.music.play(deal_card, channel="sound")

    def cardflowtime(distance):
        return card_time_koef*distance**0.25

    def card_button(card,newx,newy,ret):
        if  (card.visible == 'VISIBLE' and VISIBLE) or (card.visible == 'INVISIBLE' and INVISIBLE) or card.name == name_of_none:
            passive = card_img[card.name]
        else:
            passive = card_img["cover"]
        if  ret == "ignore":
            active = passive = im.MatrixColor(passive,im.matrix.saturation(0.1))
        else:
            active = im.MatrixColor(passive,im.matrix.brightness(0.1)*im.matrix.saturation(1.5))
        ui.at(Move((card.x, card.y), (newx,newy), cardflowtime( ((newx-card.x)**2+(newy-card.y)**2)**0.5 )))
        if ret == "ignore":
            ui.image(passive)
        else:
            ui.imagebutton(passive,active,clicked=ui.returns(ret))
        card.x = newx
        card.y = newy


init python:

    def play_choose_sound():
        if cards_state != "me_select_1" and cards_state != "me_select_2":
            renpy.music.play("sound/sfx/cardgame/new/choose_card_2.ogg", channel="sound")

    def show_cards():
        
        renpy.scene('underlay')
        renpy.show(cards_bg,layer='underlay')
        ui.layer('underlay')                                
        
        for i in range(0,n_cards):
            if  cards_rival[i].interesting :
                x = int(card_dx*i+card_left_dx+card_width/2.0-arrow_width/2.0)
                y = card_top_dy+card_height+20
                ui.at( Move( (x,y), (x,y), 1 ) )
                ui.image(card_up,xpos=x,ypos=y)
            if  cards_state == "me_select_2" and cards_rival[i].allow:
                card_button(cards_rival[i], card_dx*i+card_left_dx, card_top_dy+cards_rival[i].dy, ("rival",i))
            else:
                card_button(cards_rival[i], card_dx*i+card_left_dx, card_top_dy+cards_rival[i].dy, "ignore")
            
            if  cards_my[i].interesting:
                x = int(card_dx*i+card_left_dx+card_width/2.0-arrow_width/2.0)
                y = card_bottom_dy-100
                ui.at( Move( (x,y), (x,y), 1 ) )
                ui.image(card_down,xpos=x,ypos=y)
            if  cards_state in ["me_select_1","me_defend_1","me_defend_2","rival_select"] or (cards_state == "me_select_2" and i==my_card) :
                card_button(cards_my[i], card_dx*i+card_left_dx, card_bottom_dy+cards_my[i].dy, ("my",i))
            else:
                card_button(cards_my[i], card_dx*i+card_left_dx, card_bottom_dy+cards_my[i].dy, "ignore")
        
        if  cards_state in ["interuption","init"]:
            ui.close() 
            return
        
        
        avatar = LiveComposite(
                         (210,210),
                         (0,0), avatar_frame,
                         (5,5), rival.avatar['body'],
                         (5,5), rival.avatar[rival.mood],
                     )
        
        ui.imagebutton(avatar,avatar,clicked=None,
                  xpos=card_dx*(n_cards)+card_left_dx+20,
                  ypos=card_top_dy,
              )
        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_top_dy+220,
                  style=style.cards_button,
              )
        ui.text(translation["Rival"][_preferences.language], style="cards_button",size=15)
        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_top_dy+240,
                  style=style.cards_button,
              )
        ui.text(rival.name,style="cards_button",size=25)
        
        
        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+0,
                  style=style.cards_button,
              )
        ui.text(translation["Whose_turn"][_preferences.language], style="cards_button",size=15)
        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+20,
                  style=style.cards_button,
              )
        if  cards_state in ["me_defend_1","me_defend_2","me_get","me_select_1","me_select_2"]:
            ui.text(translation["Yours"][_preferences.language], style="cards_button",size=25)
        if  cards_state in ["rival_defend","rival_get","rival_select"]:
            ui.text(translation["Opponents"][_preferences.language], style="cards_button",size=25)
        if  cards_state in ["results"]:
            ui.text(u"---",style="cards_button",size=25)
        
        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+90 - button_dy,
                  style=style.cards_button,
              )
        ui.text(translation["Game_phase"][_preferences.language], style="cards_button",size=15)
        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+110 - button_dy,
                  style=style.cards_button,
              )
        
        if  cards_state in ["me_defend_1","me_defend_2","rival_defend"]:
            ui.text(translation["Defence"][_preferences.language], style="cards_button",size=25)
        if  cards_state == "me_select_1":
            ui.text(translation["Drop"][_preferences.language], style="cards_button",size=25)
        if  cards_state in ["me_select_2","rival_select"]:
            ui.text(translation["Capture"][_preferences.language], style="cards_button",size=25)
        if  cards_state in ["me_get","rival_get"]:
            if  CARD_GAME_WITH_EXCHANGE:
                ui.text(translation["Change"][_preferences.language], style="cards_button",size=25)
            else:
                ui.text(translation["Draw_card"][_preferences.language], style="cards_button",size=25)
        if  cards_state in ["results"]:
            ui.text(translation["Results"][_preferences.language], style="cards_button",size=25)
        
        if  cards_state in ["me_defend_1","me_defend_2"]:
            ui.button(clicked=ui.returns("end_of_turn"), xanchor=1.0, xpadding=6, xminimum=25,
                      xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                      ypos=card_bottom_dy+110 - button_dy,
                      style=style.cards_button,
                  )
            ui.text(u"X",style="cards_button",size=25)
        
        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+180 - button_dy,
                  style=style.cards_button,
              )
        ui.text(translation["Rounds_left"][_preferences.language], style="cards_button",size=15)
        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+200 - button_dy,
                  style=style.cards_button,
              )
        ui.text("%d"%cycles_left,style="cards_button",size=25)
        
        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+270 - button_dy,
                  style=style.cards_button,
              )
        ui.text(translation["Exchanges_left"][_preferences.language], style="cards_button",size=15)
        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+290 - button_dy,
                  style=style.cards_button,
              )
        if  changes_left == 0:
            changes_left_text = "---"
        else:
            changes_left_text = "%d"%changes_left
        ui.text(changes_left_text,style="cards_button",size=25)
        
        if  result_status != 'in_progress':
            renpy.block_rollback()
            ui.button(clicked=ui.returns("ok"), xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=screen_width/2+100,
                  ypos=screen_height/2-35 - bottom_dy - bottom_dy_result,
                  style=style.cards_button,
              )
            if  result_status == 'win':
                ui.text(translation["Win"][_preferences.language], style="cards_button",size=72)
            if  result_status == 'draw':
                ui.text(translation["Draw"][_preferences.language], style="cards_button",size=72)
            if  result_status == 'fail':
                ui.text(u"FAIL", style="cards_button",size=72)
        
        ui.close() 




init python:
    def move_buttons(setk,k,setj,j):
        global cards_my
        global cards_rival
        
        for i in range(0,n_cards):
            cards_my[i].hot = False
            cards_rival[i].hot = False
        setk[k].hot = True
        setj[j].hot = True
        
        tmp = setk[k]
        setk[k] = setj[j]
        setj[j] = tmp

    def cards_interact():
        show_cards()
        answer = ui.interact()
        if  answer=="ignore":
            ui.jumps("cards_gameloop")()
        
        if cards_state == "me_defend_1":
            
            
            
            
            
            
            
            
            renpy.music.play("sound/sfx/cardgame/new/choose_card_2.ogg", channel="sound")
        
        elif cards_state == "me_defend_2":
            renpy.music.play("sound/sfx/cardgame/new/choose_card_1.ogg", channel="sound")
        
        return answer

    def xchange_cards():
        for i in range(0,n_cards):
            cards_my[i].interesting = False
            cards_rival[i].interesting = False
        cards_my[my_card].visible = 'INVISIBLE'
        cards_rival[rival_card].visible = 'VISIBLE'
        move_buttons(cards_my,my_card,cards_rival,rival_card)
        
        take_cards = {"1":"sound/sfx/cardgame/new/take_card_1.ogg","2":"sound/sfx/cardgame/new/take_card_2.ogg","3":"sound/sfx/cardgame/new/take_card_3.ogg" }
        
        from random import randint
        take_card = take_cards[str(randint(1,3))]
        
        renpy.music.play(take_card, channel="sound")

    def card_value(x):
        if  x.name[0] == 1:
            return 14
        else:
            return x.name[0]

    def sort_cards():
        cards_rival.sort(cmp,card_value)
        cards_my.sort(cmp,card_value)

    def interuption_region():
        global cycles_left
        global cards_state
        
        if cards_state == "me_select_1" or cards_state == "me_select_1":
            renpy.music.play("sound/sfx/cardgame/new/choose_card_2.ogg", channel="sound")
        
        
        
        
        
        
        
        elif cards_state == "rival_defend":
            renpy.music.play("sound/sfx/cardgame/new/choose_card_1.ogg", channel="sound")
        
        position = (cycles_left,cards_state,"call")
        if  position in game_interuptions:
            tmp_state = cards_state
            cards_state = "interuption"
            show_cards()
            renpy.call_in_new_context(game_interuptions[position])
            renpy.block_rollback()
            cards_state = tmp_state
            del game_interuptions[position]
        position = (cycles_left,cards_state,"jump")
        if  position in game_interuptions:
            tmp_state = cards_state
            cards_state = "interuption"
            renpy.scene('underlay')
            ui.jumps(game_interuptions[position])()

    def what_category(cardset):
        ans = []
        summ = 0
        for i in range(0,n_cards):
            cardset[i].interesting = False
        for len in [4,3,2]:
            for i in range(0,n_cards-len+1):
                if  cardset[i].interesting:
                    continue
                val = card_value(cardset[i])
                ok  = True
                for j in range(i+1,i+len):
                    if  card_value(cardset[j]) != card_value(cardset[i]):
                        ok = False
                if  ok:
                    for j in range(i,i+len):
                        cardset[j].interesting = True
                    ans.append([len,val])
                    summ += len
        
        if  summ == 0:
            cardset[n_cards-1].interesting = True
            return  1, [[1,card_value(cardset[n_cards-1])]]
        else:
            return summ, ans

    def cmpset(a,b):
        if  a[0]!=b[0]:
            return b[0]-a[0]
        return b[1]-a[1]

    def compare_sets(result_my,gr_my,result_rival,gr_rival):
        
        if  result_my >  result_rival:
            return 'win'
        if  result_my <  result_rival:
            return 'fail'
        
        
        if  len(gr_my) <  len(gr_rival):
            return 'win'
        if  len(gr_my) >  len(gr_rival):
            return 'fail'
        
        for i in range(0,len(gr_my)):
            
            if  gr_my[i][0] >  gr_rival[i][0]:
                return 'win'
            if  gr_my[i][0] <  gr_rival[i][0]:
                return 'fail'
            
            
            if  gr_my[i][1] >  gr_rival[i][1]:
                return 'win'
            if  gr_my[i][1] <  gr_rival[i][1]:
                return 'fail'
        
        return 'draw'

    def count_score():
        result_my,gr_my = what_category(cards_my)
        result_rival,gr_rival = what_category(cards_rival)
        
        gr_my.sort(cmpset)
        gr_rival.sort(cmpset)
        
        return compare_sets(result_my,gr_my,result_rival,gr_rival)

label cards_gameloop:
    python:
        renpy.block_rollback()
        renpy.scene('underlay')
        renpy.scene('master')

        if cards_state == "init":
            show_cards()
            renpy.pause(1)
            new_state = "rival_select"

        if cards_state == "rival_select":
            interuption_region()
            my_card = rival.pick_my_card()
            for i in range(0,n_cards):
                cards_my[i].interesting = False
                cards_rival[i].interesting = False                       
            cards_my[my_card].interesting = True
            
            show_cards()
            renpy.pause(1)
            if  not rival.allow_to_defend():
                new_state = "rival_get"
            else:
                new_state = "me_defend_1"

        if cards_state == "me_defend_1":
            interuption_region()
            answer = cards_interact()
            if  answer=="end_of_turn":
                new_state = "rival_get"
            else:
                type,index = answer
                cards_my[index].dy = -40
                prev_answer = index
                new_state = "me_defend_2"

        if cards_state == "me_defend_2":
            interuption_region()
            answer = cards_interact()
            cards_my[prev_answer].dy = 0
            if  answer=="end_of_turn":
                new_state = "rival_get"
            else:
                type,index = answer
                if  prev_answer == index:
                    cards_my[prev_answer].dy = 0
                    new_state = "me_defend_1"
                else:
                    move_buttons(cards_my,prev_answer,cards_my,index)
                    changes_left -= 1
                    if  changes_left == 0:
                        new_state = "rival_get"
                    else:
                        new_state = "rival_select"

        if cards_state == "rival_get":
            if  changes_left == 0:
                my_card = rival.pick_my_card_last()
            for i in range(0,n_cards):
                cards_my[i].interesting = False
                cards_rival[i].interesting = False
            cards_my[my_card].interesting = True
            
            show_cards()
            renpy.pause(1)
            interuption_region()
            
            if CARD_GAME_WITH_EXCHANGE:
                rival_card = rival.give_away_card()
            else:
                for i in range(0,n_cards):
                    if  cards_rival[i].name == name_of_none:
                        rival_card = i
            xchange_cards()
            changes_left = n_xchanges
            rival.allow_to_take()
            new_state = "me_select_1"

        if cards_state == "me_select_1":
            interuption_region()
            if  CARD_GAME_WITH_EXCHANGE:
                answer = cards_interact()
                type,index = answer
                cards_my[index].dy = -40
                my_card    = index
            else:
                for i in range(0,n_cards):
                    if  cards_my[i].name == name_of_none:
                        my_card = i
            new_state = "me_select_2"

        if cards_state == "me_select_2":
            interuption_region()
            answer = cards_interact()
            type,index = answer
            if  type == "my":
                cards_my[index].dy = 0
                new_state = "me_select_1"
            else:
                rival_card = index
                for i in range(0,n_cards):
                    cards_rival[i].interesting = False
                    cards_my[i].interesting = False
                cards_rival[index].interesting = True
                new_state = "rival_defend"

        if cards_state == "rival_defend":
            show_cards()
            renpy.pause(1)
            interuption_region()
            if  changes_left == 0:
                new_state = "me_get"
            else:
                if  not rival.want_to_defend():
                    changes_left == 0
                    new_state = "me_get"
                else:
                    changes_left -= 1
                    i,j=rival.what_to_xchange()
                    move_buttons(cards_rival,i,cards_rival,j)
                    tmp_interest = cards_rival[i].interesting
                    cards_rival[i].interesting = cards_rival[j].interesting
                    cards_rival[j].interesting = tmp_interest
                    new_state = "me_select_2"

        if cards_state == "me_get":
            interuption_region()
            cards_my[my_card].dy = 0
            xchange_cards()
            cycles_left -= 1
            if  cycles_left != 0:
                changes_left = n_xchanges
                new_state = "rival_select"
            else:
                new_state = "results"

        if cards_state == "results":
            interuption_region()
            show_cards()
            renpy.pause(2)
            sort_cards()
            for i in range(0,n_cards):
                cards_rival[i].visible = 'VISIBLE'
                cards_my[i].visible = 'VISIBLE'
            result_status = count_score()
            answer = "ignore"
            while answer=="ignore":
                show_cards()
                answer = ui.interact()
            new_state = result_status

        if cards_state in ["win","draw","fail"]:
            interuption_region()
            renpy.error("out of end-of-card-game interruption")

        cards_state = new_state
    jump cards_gameloop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
