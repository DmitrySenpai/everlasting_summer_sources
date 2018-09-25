


init -1600 python:

    _preferences.joymap['joy_left'] = "D-PAD Left"
    _preferences.joymap['joy_right'] = "D-PAD Right"
    _preferences.joymap['joy_up'] = "D-PAD Up"
    _preferences.joymap['joy_down'] = "D-PAD Down"
    _preferences.joymap['joy_dissmiss'] = "Button 0.0"
    _preferences.joymap['joy_menu'] = "Button 0.7"
    _preferences.joymap['joy_hide'] = "Button 0.3"
    _preferences.joymap['joy_rollback'] = "Button 0.2"
    _preferences.joymap['joy_holdskip'] = "Button 0.1"
    _preferences.joymap['joy_toggleskip'] = "Button 0.5"

    config.keymap = dict(
        
        
        
        rollback = [ 'K_PAGEUP', 'mousedown_4', 'joy_rollback' ],
        screenshot = [ 's' ],
        toggle_fullscreen = [ 'f', 'alt_K_RETURN', 'alt_K_KP_ENTER', 'K_F11' ],
        toggle_music = [ 'm' ],
        game_menu = [ 'K_ESCAPE', 'mouseup_3', 'joy_menu' ],
        hide_windows = [ 'mouseup_2', 'h', 'joy_hide' ],
        launch_editor = [ 'E' ],
        dump_styles = [ 'Y' ],
        reload_game = [ 'R' ],
        inspector = [ 'I' ],
        developer = [ 'D' ],
        quit = [ 'meta_q', 'alt_K_F4', 'alt_q' ],
        iconify = [ 'meta_m', 'alt_m' ],
        help = [ 'K_F1', 'meta_shift_/' ],
        choose_renderer = [ 'G' ],
        self_voicing = [ 'K_F13' ],

        
        rollforward = [ 'mousedown_5', 'K_PAGEDOWN' ],
        dismiss = [ 'mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'joy_dismiss' ],

        
        dismiss_hard_pause = [ ],
        
        
        focus_left = [ 'K_LEFT', 'joy_left' ],
        focus_right = [ 'K_RIGHT', 'joy_right' ],
        focus_up = [ 'K_UP', 'joy_up' ],
        focus_down = [ 'K_DOWN', 'joy_down' ],
            
        
        button_ignore = [ 'mousedown_1' ],
        button_select = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'joy_dismiss', 'U' ],
        button_alternate = [ 'mouseup_3', 'O' ],
        button_alternate_ignore = [ 'mousedown_3' ],

        
        input_backspace = [ 'K_BACKSPACE' ],
        input_enter = [ 'K_RETURN', 'K_KP_ENTER' ],
        input_left = [ 'K_LEFT' ],
        input_right = [ 'K_RIGHT' ],
        input_delete = [ 'K_DELETE' ],

        
        viewport_up = [ 'mousedown_4' ],
        viewport_down = [ 'mousedown_5' ],
        viewport_drag_start = [ 'mousedown_1' ],
        viewport_drag_end = [ 'mouseup_1' ],
        
        
        skip = [ 'K_LCTRL', 'K_RCTRL', 'joy_holdskip' ],
        toggle_skip = [ 'K_TAB', 'joy_toggleskip' ],
        fast_skip = [ '>' ],

        
        bar_activate = [ 'mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'joy_dismiss' ],
        bar_deactivate = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'joy_dismiss' ],
        bar_left = [ 'K_LEFT', 'joy_left' ],
        bar_right = [ 'K_RIGHT', 'joy_right' ],
        bar_up = [ 'K_UP', 'joy_up' ],
        bar_down = [ 'K_DOWN', 'joy_down' ],

        
        save_delete = [ 'K_DELETE' ],

        
        drag_activate = [ 'mousedown_1' ],
        drag_deactivate = [ 'mouseup_1' ],
    
        
        console = [ 'shift_O' ],
        console_older = [ 'K_UP' ],
        console_newer = [ 'K_DOWN' ],

        
        

        
        profile_once = [ 'K_F8' ],


        )

    def _screenshot_callback(fn):
        renpy.notify(__("Saved screenshot as \n%s.") % fn)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
