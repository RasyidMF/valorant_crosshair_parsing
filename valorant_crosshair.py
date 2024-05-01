# Made by RasyidMF
# Fixing ur valorant crosshair missing bug by reading RiotUserSettings.ini

# To located ur RiotUserSettings.ini is in C:\Users\{PC_NAME}\AppData\Local\VALORANT\Saved\Config\{YOUR_USER_SETTINGS}\Windows\RiotUserSettings.ini

import random
import sys
from dataclasses import dataclass

import json

def r_int(mn: int, mx: int):
    return random.randrange(mn, mx + 1)

def r_float(mn: int, mx: int, fdiv: int = 100):
    return r_int(int(mn * fdiv), int(mx * fdiv)) / fdiv

def r_bool():
    return (r_int(0, 100) % 2) == 0

def r_byte():
    return hex(r_int(0, 256))[2:].zfill(2)

def r_color():
    return (r_byte() + r_byte() + r_byte() + "ff").upper()  # RGBA

def color_parse(red, green, blue, alpha):
    return ((hex(red)[2:].zfill(2)) + hex(green)[2:].zfill(2) + hex(blue)[2:].zfill(2) + hex(alpha)[2:].zfill(2)).upper()

@dataclass
class GENERAL_CROSSHAIR:
    advanced_options: bool = True

    def __str__(self):
        s = int(self.advanced_options)
        return f"s;{s};"


@dataclass
class GENERAL_OTHER:
    show_spectated_players_crosshair: bool = True
    fade_crosshair_with_firing_error: bool = True
    # disable_crosshair: bool = False (Doesn't matter)

    # def __post_init__(self):
    #     self.show_spectated_players_crosshair = r_bool()
    #     self.fade_crosshair_with_firing_error = r_bool()

    def __str__(self):
        s = int(self.show_spectated_players_crosshair)
        f = int(self.fade_crosshair_with_firing_error)
        # return f"P;f;{f};s;{s};"
        return f"s;{s};"


@dataclass
class PRIMARY_CROSSHAIR:
    # crosshair_color: str = ""
    # always use custom crosshair color
    use_custom_color: bool = False
    custom_color: str = ""
    outlines: bool = False
    outline_color: str = ""
    outline_opacity: float = 0.0
    outline_thickness: int = 0
    center_dot: bool = False
    center_dot_opacity: float = 0.0
    center_dot_thickness: int = 0
    override_firing_error: bool = False
    overide_all_primary: bool = False

    # def __post_init__(self):
    #     self.use_custom_color = r_bool()
    #     self.custom_color = r_color()
    #     self.outlines = r_bool()
    #     self.outline_color = r_color()
    #     self.outline_opacity = r_float(0.0, 1.0)
    #     self.outline_thickness = r_int(1, 6)
    #     self.center_dot = r_bool()
    #     self.center_dot_opacity = r_float(0.0, 1.0)
    #     self.center_dot_thickness = r_int(1, 6)
    #     self.override_firing_error = r_bool()
    #     self.overide_all_primary = r_bool()

    def __str__(self):
        
        ret_str = ""
        if not self.use_custom_color:
            ret_str += f"c;{random.randrange(8)};"
        else:
            ret_str += f"c;8;u;{self.custom_color};b;1;"

        # if self.use_custom_color:
        #     ret_str += ""

        h = int(self.outlines)
        ret_str += f"h;{h};"

        t = self.outline_thickness
        o = self.outline_opacity
        ret_str += f"t;{t};o;{o};"

        d = int(self.center_dot)
        z = self.center_dot_thickness
        a = self.center_dot_opacity
        ret_str += f"d;{d};z;{z};a;{a};"

        m = int(self.override_firing_error)
        ret_str += f"m;{m};"

        return ret_str


@dataclass
class PRIMARY_INNER_LINES:
    meta: int = 0
    show_lines: bool = True
    opacity: float = 0.8
    line_thickness: int = 2
    line_offset: int = 3
    line_length: int = 6
    allow_vert_scaling: bool = False
    line_length_vertical: int = 6
    show_movement_error: bool = False
    movement_error_scale: float = 1.0
    show_shooting_error: bool = False
    firing_error_scale: float = 1.0

    # def __post_init__(self):
    #     # self.show_lines = r_bool() # Always show inner lines
    #     self.opacity = r_float(0.0, 1.0)
    #     self.line_thickness = r_int(1, 10)
    #     self.line_offset = r_int(1, 20)
    #     self.line_length = r_int(1, 20)
    #     self.allow_vert_scaling = r_bool()
    #     self.line_length_vertical = r_int(1, 20)
    #     self.show_movement_error = r_bool()
    #     self.movement_error_scale = r_float(0.0, 3.0)
    #     self.show_shooting_error = r_bool()
    #     self.firing_error_scale = r_float(0.0, 3.0)

    def __str__(self):
        ret_str = ""
        if not self.show_lines:
            return f"{int(self.meta)}b;0;"

        t = self.line_thickness
        ret_str += f"{int(self.meta)}t;{t};"

        a = self.opacity
        ret_str += f"{int(self.meta)}a;{a};"

        o = self.line_offset
        ret_str += f"{int(self.meta)}o;{o};"

        l = self.line_length
        ret_str += f"{int(self.meta)}l;{l};"

        if self.allow_vert_scaling:
            v = self.line_length_vertical
            ret_str += f"{int(self.meta)}v;{v};"
            ret_str += f"{int(self.meta)}g;1;"  # allow_vert_scaling

        if self.show_movement_error:
            ret_str += f"{int(self.meta)}m;1;"
            s = self.movement_error_scale
            ret_str += f"{int(self.meta)}s;{s};"

        if self.show_shooting_error:
            e = self.firing_error_scale
            ret_str += f"{int(self.meta)}e;{e};"
        else:
            ret_str += f"{int(self.meta)}f;0;"

        return ret_str


@dataclass
class PRIMARY_OUTER_LINES(PRIMARY_INNER_LINES):
    meta: int = 1
    ...


@dataclass
class AIMDOWNSIGHTS_COPY_PRIMARY_CROSSHAIR:
    copy_primary_crosshair: bool = True


@dataclass
class AIMDOWNSIGHTS_CROSSHAIR(PRIMARY_CROSSHAIR):
    ...


@dataclass
class AIMDOWNSIGHTS_INNER_LINES(PRIMARY_INNER_LINES):
    ...


@dataclass
class AIMDOWNSIGHTS_OUTER_LINES(PRIMARY_OUTER_LINES):
    ...


@dataclass
class SNIPERSCOPE_GENERAL:
    display_center_dot: bool = True
    use_custom_center_dot_color: bool = False
    center_dot_color_custom: str = ""
    center_dot_thickness: int = 1
    center_dot_opacity: float = 0.75

    # def __post_init__(self):
    #     # self.display_center_dot = r_bool()
    #     self.use_custom_center_dot_color = r_bool()
    #     self.center_dot_color_custom = r_color()
    #     self.center_dot_thickness = r_int(1, 6)
    #     self.center_dot_opacity = r_float(0.0, 1.0)

    def __str__(self):
        ret_str = ""
        if not self.display_center_dot:
            ret_str += "d;0;"
            return ret_str

        if not self.use_custom_center_dot_color:
            ret_str += f"c;{random.randrange(8)};"
        else:
            ret_str += f"c;8;t;{self.center_dot_color_custom};"

        if self.use_custom_center_dot_color:
            ret_str += "b;1;"

        s = self.center_dot_thickness
        ret_str += f"s;{s};"

        o = self.center_dot_opacity
        ret_str += f"o;{o};"

        return ret_str


@dataclass
class GENERAL:
    crosshair: GENERAL_CROSSHAIR
    other: GENERAL_OTHER

    def __str__(self):
        return str(self.crosshair) + str(self.other)


@dataclass
class PRIMARY:
    crosshair: PRIMARY_CROSSHAIR
    inner_lines: PRIMARY_INNER_LINES
    outer_lines: PRIMARY_OUTER_LINES

    def __str__(self):
        ret_str = ""
        if self.crosshair.overide_all_primary:
            ret_str += "c;1;"

        ret_str += "P;"
        ret_str += str(self.crosshair) + str(self.inner_lines) + str(self.outer_lines)
        return ret_str


@dataclass
class AIMDOWNSIGHTS:
    # copy_primary_crosshair: AIMDOWNSIGHTS_COPY_PRIMARY_CROSSHAIR
    crosshair: AIMDOWNSIGHTS_CROSSHAIR
    inner_lines: AIMDOWNSIGHTS_INNER_LINES
    outer_lines: AIMDOWNSIGHTS_OUTER_LINES

    def __str__(self):
        ret_str = "A;"
        ret_str += str(self.crosshair) + str(self.inner_lines) + str(self.outer_lines)
        return ret_str


@dataclass
class SNIPERSCOPE:
    general: SNIPERSCOPE_GENERAL

    def __str__(self):
        ret_str = "S;"
        ret_str += str(self.general)
        return ret_str


def randomize():
    g = GENERAL(GENERAL_CROSSHAIR(), GENERAL_OTHER())
    p = PRIMARY(PRIMARY_CROSSHAIR(), PRIMARY_INNER_LINES(), PRIMARY_OUTER_LINES())
    a = AIMDOWNSIGHTS(
        AIMDOWNSIGHTS_CROSSHAIR(),
        AIMDOWNSIGHTS_INNER_LINES(),
        AIMDOWNSIGHTS_OUTER_LINES(),
    )
    s = SNIPERSCOPE(SNIPERSCOPE_GENERAL())

    return "0;" + str(g) + str(p) + str(a) + str(s)[:-1]

def parsingByProfiles(profiles):
    pass

# Running the code

profiles = open("profiles.txt", "r").read().replace("\\", "")
profiles = json.loads(profiles)

for x in profiles['profiles']:
    
    # Profile Name
    profileName = x['profileName']
    
    # General Crosshair
    g = GENERAL(
        GENERAL_CROSSHAIR(advanced_options = x['bUseAdvancedOptions']),
        GENERAL_OTHER(
            show_spectated_players_crosshair = x['primary']['bShowSpectatedPlayerCrosshair'],
            fade_crosshair_with_firing_error = x['primary']['bFadeCrosshairWithFiringError'],
        )
    )
    
    # Primary Crosshair
    primary = x['primary']
    pInnerLines = primary['innerLines']
    oInnerLines = primary['outerLines']
    
    customColorCode = color_parse(
        blue = primary['color']['b'],
        green = primary['color']['g'],
        red = primary['color']['r'],
        alpha = primary['color']['a'],
    ) if not primary['bUseCustomColor'] else color_parse(
        blue = primary['colorCustom']['b'],
        green = primary['colorCustom']['g'],
        red = primary['colorCustom']['r'],
        alpha = primary['colorCustom']['a'],
    )
    
    p = PRIMARY(
        PRIMARY_CROSSHAIR(
            center_dot = primary['bDisplayCenterDot'],
            center_dot_opacity = primary['centerDotOpacity'],
            center_dot_thickness = primary['centerDotSize'],
            custom_color = customColorCode,
            outline_color = color_parse(
                red = primary['outlineColor']['r'],
                green = primary['outlineColor']['g'],
                blue = primary['outlineColor']['b'],
                alpha = primary['outlineColor']['a'],
            ),
            outline_opacity = primary['outlineOpacity'],
            outline_thickness = primary['outlineThickness'],
            outlines = primary['bHasOutline'],
            overide_all_primary = True,
            override_firing_error = primary['bFadeCrosshairWithFiringError'],
            use_custom_color = primary['bUseCustomColor'],
        ),
        PRIMARY_INNER_LINES(
            allow_vert_scaling = pInnerLines['bAllowVertScaling'],
            firing_error_scale = pInnerLines['firingErrorScale'],
            line_length = pInnerLines['lineLength'],
            line_length_vertical = pInnerLines['lineLengthVertical'],
            line_offset = pInnerLines['lineOffset'],
            line_thickness = pInnerLines['lineThickness'],
            show_movement_error = pInnerLines['bShowMovementError'],
            movement_error_scale = pInnerLines['movementErrorScale'],
            opacity = pInnerLines['opacity'],
            show_lines = pInnerLines['bShowLines'],
            show_shooting_error = pInnerLines['bShowShootingError'],
        ),
        PRIMARY_OUTER_LINES(
            allow_vert_scaling = oInnerLines['bAllowVertScaling'],
            firing_error_scale = oInnerLines['firingErrorScale'],
            line_length = oInnerLines['lineLength'],
            line_length_vertical = oInnerLines['lineLengthVertical'],
            line_offset = oInnerLines['lineOffset'],
            line_thickness = oInnerLines['lineThickness'],
            show_movement_error = oInnerLines['bShowMovementError'],
            movement_error_scale = oInnerLines['movementErrorScale'],
            opacity = oInnerLines['opacity'],
            show_lines = oInnerLines['bShowLines'],
            show_shooting_error = oInnerLines['bShowShootingError']
        )
    )
    
    # ADS Crosshair
    ads = x['aDS']
    aInnerLines = ads['innerLines']
    aOuterLines = ads['outerLines']
    a = AIMDOWNSIGHTS(
        AIMDOWNSIGHTS_CROSSHAIR(
            center_dot = ads['bDisplayCenterDot'],
            center_dot_opacity = ads['centerDotOpacity'],
            center_dot_thickness = ads['centerDotSize'],
            custom_color = color_parse(
                red = ads['color']['r'],
                green = ads['color']['g'],
                blue = ads['color']['b'],
                alpha = ads['color']['a'],
            ),
            outline_color = color_parse(
                red = ads['outlineColor']['r'],
                green = ads['outlineColor']['g'],
                blue = ads['outlineColor']['b'],
                alpha = ads['outlineColor']['a'],
            ),
            outline_opacity = ads['outlineOpacity'],
            outline_thickness = ads['outlineThickness'],
            outlines = ads['bHasOutline'],
            overide_all_primary = True,
            override_firing_error = ads['bFadeCrosshairWithFiringError'],
            use_custom_color = True,
        ),
        AIMDOWNSIGHTS_INNER_LINES(
            allow_vert_scaling = aInnerLines['bAllowVertScaling'],
            firing_error_scale = aInnerLines['firingErrorScale'],
            line_length = aInnerLines['lineLength'],
            line_length_vertical = aInnerLines['lineLengthVertical'],
            line_offset = aInnerLines['lineOffset'],
            line_thickness = aInnerLines['lineThickness'],
            show_movement_error = aInnerLines['bShowMovementError'],
            movement_error_scale = aInnerLines['movementErrorScale'],
            opacity = aInnerLines['opacity'],
            show_lines = aInnerLines['bShowLines'],
            show_shooting_error = aInnerLines['bShowShootingError'],
        ),
        AIMDOWNSIGHTS_OUTER_LINES(
            allow_vert_scaling = aOuterLines['bAllowVertScaling'],
            firing_error_scale = aOuterLines['firingErrorScale'],
            line_length = aOuterLines['lineLength'],
            line_length_vertical = aOuterLines['lineLengthVertical'],
            line_offset = aOuterLines['lineOffset'],
            line_thickness = aOuterLines['lineThickness'],
            show_movement_error = aOuterLines['bShowMovementError'],
            movement_error_scale = aOuterLines['movementErrorScale'],
            opacity = aOuterLines['opacity'],
            show_lines = aOuterLines['bShowLines'],
            show_shooting_error = aOuterLines['bShowShootingError'],
        ),
    )
    
    # Sniper Crosshair
    sniper = x['sniper']
    s = SNIPERSCOPE(SNIPERSCOPE_GENERAL( 
        center_dot_color_custom = color_parse(
            red = sniper['centerDotColor']['r'],
            green = sniper['centerDotColor']['g'],
            blue = sniper['centerDotColor']['b'],
            alpha = sniper['centerDotColor']['a'],
        ),
        center_dot_opacity = sniper['centerDotOpacity'],
        center_dot_thickness = sniper['centerDotSize'],
        display_center_dot = sniper['bDisplayCenterDot'],
        use_custom_center_dot_color = True
    ))
    
    # Result
    code = "0;" + str(g) + str(p) + str(a)
    
    print(f"Profile Name: %s\nCode: %s\n\n-------" % (profileName, code))
    