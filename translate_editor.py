#!/usr/bin/env python

import os

# Externalize editor strings.
# Caveat: The strings that contain line breaks do not work automatically.


editor_strings = [
    'L"DETAILED PLACEMENT"',
    'L"Starting Population"',
    'L"Easy"',
    'L"Normal"',
    'L"Diff"',
    'L"Admins"',
    'L"Troops"',
    'L"Elites"',
    'L"BloodCats"',
    'L"Invasion Data"',
    'L"Min Enemies"',
    'L"Attack Probability Rate"',
    'L"Grace period"',
    'L"Insertion GridNo (undergrnd)"',
    'L"Sector Description"',
    'L"Insertion Direction"',
    'L"Loading Screen"',

    'L"Snow"',
    'L"Guard Post"',
    'L"Power Plant"',
    'L"Generic"',
    'L"Town 1"',
    'L"Town 2"',
    'L"Forest"',
    'L"Mine"',
    'L"Cave"',
    'L"Pine"',
    'L"Mine Entrance"',
    'L"Wilderness"',
    'L"Generic Basement"',
    'L"DELETE"', # UB: L"Delete", JA2: L"DELETE"
    'L"north"',
    'L"northeast"',
    'L"east"',
    'L"southeast"',
    'L"south"',
    'L"southwest"',
    'L"west"',
    'L"northwest"',
    'L"Toggle viewing of players"',
    'L"Toggle viewing of enemies"',
    'L"Toggle viewing of creatures"',
    'L"General information mode"',
    'L"Attributes mode"',
    'L"Inventory mode"',
    'L"Schedule mode"',
    'L"Delete currently selected merc (DEL)."',
    'L"Find next merc (SPACE)."',
    'L"Toggle priority existance"',
    'L"STATIONARY"',
    'L"ON GUARD"',
    'L"ON CALL"',
    'L"SEEK ENEMY"',
    'L"CLOSE PATROL"',
    'L"FAR PATROL"',
    'L"POINT PATROL"',
    'L"RND PT PATROL"',
    'L"DEFENSIVE"',
    'L"BRAVE SOLO"',
    'L"BRAVE AID"',
    'L"AGGRESSIVE"',
    'L"CUNNING SOLO"',
    'L"CUNNING AID"',
    'L"Set merc to face %s"',
    'L"Find"',
    'L"Find selected merc"',
    'L"Previous color set"',
    'L"Next color set"',
    'L"Toggle time variance (+ or - 15 minutes)"',
    'L"No action"',
    'L"Clear Schedule"',
    'L"ROOFS"',
    'L"WALLS"',
    'L"ROOM INFO"',
    'L"Place walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\n"', #UB: L"Place walls using selection method\n", JA2: L"Place walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\nPlace walls using selection method\n"
    'L"Place doors using selection method"',
    'L"Place roofs using selection method"',
    'L"Place windows using selection method"',
    'L"Place damaged walls using selection method."',
    'L"Place furniture using selection method"',
    'L"Place wall decals using selection method"',
    'L"Place floors using selection method"',
    'L"Place generic furniture using selection method"',
    'L"Place walls using smart method"',
    'L"Place doors using smart method"',
    'L"Place windows using smart method"',
    'L"Place damaged walls using smart method"',
    'L"Add a new room"',
    'L"Edit cave walls."',
    'L"Remove an area from existing building."',
    'L"Remove a building"',
    'L"Add/replace building\'s roof with new flat roof."',
    'L"Copy a building"',
    'L"Move a building"',
    'L"Draw room number"',
    'L"Erase room numbers"',
    'L"Toggle erase mode ON/OFF"', # UB: L"Toggle erase mode", JA2: L"Toggle erase mode ON/OFF"
    'L"Undo last change"',
    'L"Cycle brush size"',
    'L"Weapons"',
    'L"Ammo"',
    'L"Armour"', # UB: L"Armor", JA2: L"Armour"
    'L"Explosives"',
    'L"E1"',
    'L"E2"',
    'L"E3"',
    'L"Triggers"',
    'L"Add ambient light source"',
    'L"Toggle fake ambient lights."',
    'L"Add exit grids (r-clk to query existing)."',
    'L"Specify north point for validation purposes."',
    'L"Specify west point for validation purposes."',
    'L"Specify east point for validation purposes."',
    'L"Specify south point for validation purposes."',
    'L"Specify center point for validation purposes."',
    'L"Specify isolated point for validation purposes."',
    'L"New map"',
    'L"New basement"',
    'L"New cave level"',
    'L"Save map"',
    'L"Load map"',
    'L"Select tileset"',
    'L"Leave Editor mode"',
    'L"Previous direction"',
    'L"Next direction"',
    'L"Draw ground textures"',
    'L"Set map ground textures"',
    'L"Place banks and cliffs"',
    'L"Draw roads"',
    'L"Draw debris"',
    'L"Place trees & bushes"',
    'L"Place rocks"',
    'L"Place barrels & other junk"',
    'L"Fill area"',
    'L"Raise brush density"',
    'L"Lower brush density"',
    'L"Terrain"',
    'L"Buildings"',
    'L"Items"',
    'L"Mercs"',
    'L"Map Info"',
    'L"Options"', # UB: L"Misc", JA2: L"Options"
    'L"North Entry Point"',
    'L"West Entry Point"',
    'L"East Entry Point"',
    'L"South Entry Point"',
    'L"Center Entry Point"',
    'L"Isolated Entry Point"',
    'L"Prime"',
    'L"Night"',
    'L"24Hrs"', # UB: L"24Hour", JA2: L"24Hrs"
    'L"Panic Trigger1"',
    'L"Panic Trigger2"',
    'L"Panic Trigger3"',
    'L"Panic Trigger4"',
    'L"Panic Trigger5"',
    'L"Panic Trigger6"',
    'L"Trigger%d"',
    'L"Pressure Action"',
    'L"Panic Action1"',
    'L"Panic Action2"',
    'L"Panic Action3"',
    'L"Panic Action4"',
    'L"Panic Action5"',
    'L"Panic Action6"',
    'L"Action%d"',
    'L"No Lock ID"',
    'L"Explosion Trap"',
    'L"Electric Trap"',
    'L"Siren Trap"',
    'L"Silent Alarm"',
    'L"Super Electric Trap"',
    'L"Trap Level %d"',
    'L"H"',
    'L"   (%d)   "', # UB: L"GridNo: %d  ", JA2: L"   (%d)   "
    'L"          "', # UB: L"                ", JA2: L"          "
    'L"No map currently loaded."',
    'L"File:  %S, Current Tileset:  %s"',
    'L"Width: %d"',
    'L"Auto"',
    'L"Player"',
    'L"Enemy"',
    'L"Creature"', # L"Bloodcat" for UB, L"Creature" for JA2
    'L"NEXT"',
    'L"TOGGLE"',
    'L"VIEWS"',
    'L"SELECTION METHOD"',
    'L"SMART METHOD"',
    'L"BUILDING METHOD"',
    'L"Room#"',
    'L"Okay"',
    'L"Cancel"',
    'L"Editing lock attributes at map index %d."',
    'L"Lock ID"',
    'L"Trap Type"',
    'L"Trap Level"',
    'L"Locked"',
    'L"Status Info Line 1"',
    'L"Status Info Line 2"',
    'L"Status Info Line 3"',
    'L"Status Info Line 4"',
    'L"Status Info Line 5"',
    'L"R"',
    'L"G"',
    'L"B"',
    'L"Radius"',
    'L"Underground"',
    'L"Light Level"',
    'L"Outdoors"',
    'L"Basement"',
    'L"Caves"',
    'L"Destination"',
    'L"Sector"',
    'L"Bsmt. Level"',
    'L"Dest."',
    'L"GridNo"',
    'L"Merc Name:"',
    'L"Orders:"',
    'L"Combat Attitude:"',
    'L"Merc Colors"',
    'L"Done"',
    'L"Previous merc standing orders"',
    'L"Next merc standing orders"',
    'L"Previous merc combat attitude"',
    'L"Next merc combat attitude"',
    'L"Decrease merc stat"',
    'L"Increase merc stat"',
    'L"Random"',
    'L"Reg Male"',
    'L"Big Male"',
    'L"Stocky Male"',
    'L"Reg Female"',
    'L"Bloodcat"',
    'L" --=ORDERS=-- "',
    'L"--=ATTITUDE=--"',
    'L"Army"', # UB: L"Army/Troops", JA2: L"Army"
    'L"Admin"',
    'L"Elite"',

    'L"Exp. Level"',
    'L"Life"', # UB: L"Health", JA2: L"Life"
    'L"LifeMax"', # UB: L"Current Health", JA2: L"LifeMax" !!!
    'L"Marksmanship"',
    'L"Strength"',
    'L"Agility"',
    'L"Dexterity"',
    'L"Wisdom"',
    'L"Leadership"',
    'L"Explosives"',
    'L"Medical"',
    'L"Mechanical"',
    'L"Morale"',

    'L"Hair color:"',
    'L"Skin color:"',
    'L"Vest color:"',
    'L"Pant color:"',

    'L"RANDOM"',
    'L"Current Profile:  n/a                            "',

    'L"STATIONARY"',
    'L"ON CALL"',
    'L"ON GUARD"',
    'L"SEEK ENEMY"',
    'L"CLOSE PATROL"',
    'L"FAR PATROL"',
    'L"POINT PATROL"',
    'L"RND PT PATROL"',
    'L"Slot #%d"',
    'L"Patrol orders with no waypoints"',
    'L"Waypoints with no patrol orders"',
    'L"Placement not copied because no placement selected."',
    'L"Placement copied."',
    'L"Placement not pasted as no placement is saved in buffer."',
    'L"Placement pasted."',
    'L"Placement not pasted as the maximum number of placements for this team is already used."',
    'L"Small"',
    'L"Medium"',
    'L"Large"',
    'L"XLarge"',
    'L"Width: "',
    'L"Area"',
    'L"Exit editor?"',
    'L"Are you sure you wish to remove all lights?"',
    'L"Are you sure you wish to reverse the schedules?"',
    'L"Are you sure you wish to clear all of the schedules?"',
    'L"Removing Treetops"',
    'L"Showing Treetops"',
    'L"Delete current map and start a new basement level?"', # UB: L"Start a new basement level?", JA2: L"Delete current map and start a new basement level?"
    'L"Delete current map and start a new cave level?"', # UB: L"Start a new cave level?", JA2: L"Delete current map and start a new cave level?"
    'L"Delete current map and start a new outdoor level?"', # UB: L"Start a new outdoor level?", JA2: L"Delete current map and start a new outdoor level?"
    'L" Wipe out ground textures? "',
    'L"HOME"',
    'L"Toggle fake editor lighting ON/OFF"',
    'L"INSERT"',
    'L"Toggle fill mode ON/OFF"',
    'L"BKSPC"',
    'L"DEL"',
    'L"Quick erase object under mouse cursor"',
    'L"ESC"',
    'L"Exit editor"',
    'L"PGUP/PGDN"',
    'L"Change object to be pasted"',
    'L"F1"',
    'L"This help screen"',
    'L"F10"',
    'L"Save current map"',
    'L"F11"',
    'L"Load map as current"',
    'L"+/-"',
    'L"Change shadow darkness by .01"',
    'L"SHFT +/-"',
    'L"Change shadow darkness by .05"',
    'L"0 - 9"',
    'L"Change map/tileset filename"',
    'L"b"',
    'L"Change brush size"',
    'L"d"',
    'L"o"',
    'L"Draw obstacle"',
    'L"r"',
    'L"Draw rocks"',
    'L"t"',
    'L"Toggle trees display ON/OFF"',
    'L"g"',
    'L"Draw ground textures"',
    'L"w"',
    'L"Draw building walls"',
    'L"e"',
    'L"h"',
    'L"Toggle roofs ON/OFF"',
    'L"Map data has just been corrupted.  Don\'t save, don\'t quit, get Kris!  If he\'s not here, save the map using a temp filename and document everything you just did, especially your last action!"', # UB: L"Map data has just been corrupted.  Don\'t save!", JA2: L"Map data has just been corrupted.  Don't save, don't quit, get Kris!  If he's not here, save the map using a temp filename and document everything you just did, especially your last action!"
    'L"Enter gridno:"',
    'L"Toggle hide flag"',
    'L"No item selected."',
    'L"Slot available for"',
    'L"random generation."',
    'L"Keys not editable."',
    'L"ProfileID of owner"',
    'L"Item class not implemented."',
    'L"Slot locked as empty."',
    'L"Status"',
    'L"Rounds"',
    'L"Trap Level"',
    'L"Quantity"',
    'L"Dollars"',
    'L"Tolerance"',
    'L"Alarm Trigger"',
    'L"Exist Chance"',
    'L"SILENCER"',
    'L"SNIPERSCOPE"',
    'L"LASERSCOPE"',
    'L"BIPOD"',
    'L"DUCKBILL"',
    'L"G-LAUNCHER"',
    'L"CERAMIC PLATES"',
    'L"DETONATOR"',
    'L"If the panic trigger is an alarm trigger,\nenemies won\'t attempt to use it if they\nare already aware of your presence."',
    'L"%s Map (*.dat)"',
    'L"Save"',
    'L"Load"',
    'L"NO FILES IN \\MAPS DIRECTORY"', # UB: L"NO FILES IN CAMPAIGN DIRECTORY", JA2: L"NO FILES IN \\MAPS DIRECTORY"
    'L" Delete READ-ONLY file %s? "',
    'L" Delete file %s? "',
    'L" Illegal filename.  Try another filename? "', # UB: L" Illegal filename.  Try another filename?", JA2: L" Illegal filename.  Try another filename? "
    'L" File is read only!  Choose a different name? "',
    'L" File exists, Overwrite? "',
    'L"Loading map:  %s"',
    'L"Filename"',
    'L"Update world info"', # UB: L"Generate Radar Map", JA2: L"Update world info"
    'L"Saving map:  %s"',
    'L"Map data has just been corrupted!!!  What did you just do?  KM : 0"', #UB: L"Map data has just been corrupted!", JA2: L"Map data has just been corrupted!!!  What did you just do?  KM : 0"
    'L" Error loading file.  Try another filename?"', # UB: L"Error loading file.", JA2: L" Error loading file.  Try another filename?"
    'L".dat"', # UB: L".dat", JA2: can be L".DAT" or L".dat"
    'L"Cancel selections"',
    'L"Accept selections"',
    'L"Scroll window up"',
    'L"Scroll window down"',
    'L"%S[%d] is from default tileset %s (%S)"',
    'L"File:  %S, subindex:  %d (%S)"',
    'L"Current Tileset:  %s"',
    'L"General enemy rank:"',
    'L"Enemy Placements:"',
    'L"Total:"',
    'L"(Missing %d)"',
    'L"Prev Loadscreen"',
    'L"Next Loadscreen"',
    'L"Num Bloodcats:"',
    'L"Current Campaign: %S"',
    'L"Check"',
    'L"droppable"',
    'L"items"',

]

editor_string_enum = [
    "EDITOR_STR_DETAILED_PLACEMENT_TEXT",
    "EDITOR_STR_STARTING_POPULATION",
    "EDITOR_STR_EASY",
    "EDITOR_STR_NORMAL",
    "EDITOR_STR_DIFF",
    "EDITOR_STR_ADMINS",
    "EDITOR_STR_TROOPS",
    "EDITOR_STR_ELITES",
    "EDITOR_STR_BLOODCATS",
    "EDITOR_STR_INVASION_DATA",
    "EDITOR_STR_MIN_ENEMIES",
    "EDITOR_STR_ATTACK_PROB_RATE",
    "EDITOR_STR_GRACE_PERIOD",
    "EDITOR_STR_INSERTION_GRIDNO",
    "EDITOR_STR_LEVEL_NAME",
    "EDITOR_STR_INSERTION_DIRECTION",
    "EDITOR_STR_LOADING_SCREEN",
    "EDITOR_STR_SNOW",
    "EDITOR_STR_GUARD_POST",
    "EDITOR_STR_POWER_PLANT",
    "EDITOR_STR_GENERIC",
    "EDITOR_STR_TOWN1",
    "EDITOR_STR_TOWN2",
    "EDITOR_STR_FOREST",
    "EDITOR_STR_MINE",
    "EDITOR_STR_CAVE",
    "EDITOR_STR_PINE",
    "EDITOR_STR_MINE_ENTRANCE",
    "EDITOR_STR_WILDERNESS",
    "EDITOR_STR_GENERIC_BASEMENT",
    "EDITOR_STR_DELETE",
    "EDITOR_STR_NORTH",
    "EDITOR_STR_NORTHEAST",
    "EDITOR_STR_EAST",
    "EDITOR_STR_SOUTHEAST",
    "EDITOR_STR_SOUTH",
    "EDITOR_STR_SOUTHWEST",
    "EDITOR_STR_WEST",
    "EDITOR_STR_NORTHWEST",
    "EDITOR_STR_TOGGLE_VIEW_PLAYERS",
    "EDITOR_STR_TOGGLE_VIEW_ENEMIES",
    "EDITOR_STR_TOGGLE_VIEW_CREATURES",
    "EDITOR_STR_GENERAL_INFO_MODE",
    "EDITOR_STR_ATTRIBUTES_MODE",
    "EDITOR_STR_INVENTORY_MODE",
    "EDITOR_STR_SCHEDULE_MODE",
    "EDITOR_STR_DELETE_SEL_MERC",
    "EDITOR_STR_FIND_NEXT_MERC",
    "EDITOR_STR_TOGGLE_PRIORITY_EXISTANCE",
    "EDITOR_STR_STATIONARY",
    "EDITOR_STR_ON_GUARD",
    "EDITOR_STR_ON_CALL",
    "EDITOR_STR_SEEK_ENEMY",
    "EDITOR_STR_CLOSE_PATROL",
    "EDITOR_STR_FAR_PATROL",
    "EDITOR_STR_POINT_PATROL",
    "EDITOR_STR_RND_PT_PATROL",
    "EDITOR_STR_DEFENSIVE",
    "EDITOR_STR_BRAVE_SOLO",
    "EDITOR_STR_BRAVE_AID",
    "EDITOR_STR_AGGRESSIVE",
    "EDITOR_STR_CUNNING_SOLO",
    "EDITOR_STR_CUNNING_AID",
    "EDITOR_STR_SET_MERC_TO_FACE",
    "EDITOR_STR_FIND",
    "EDITOR_STR_FIND_SEL_MERC",
    "EDITOR_STR_PREVIOUS_COL_SET",
    "EDITOR_STR_NEXT_COL_SET",
    "EDITOR_STR_TOGGLE_TIME_VAR",
    "EDITOR_STR_NO_ACTION",
    "EDITOR_STR_CLEAR_SCHED",
    "EDITOR_STR_ROOFS",
    "EDITOR_STR_WALLS",
    "EDITOR_STR_ROOM_INFO",
    "EDITOR_STR_PLACE_WALLS",
    "EDITOR_STR_PLACE_DOORS",
    "EDITOR_STR_PLACE_ROOFS",
    "EDITOR_STR_PLACE_WINDOWS",
    "EDITOR_STR_PLACE_DAMAGED_WALLS",
    "EDITOR_STR_PLACE_FURNITURE",
    "EDITOR_STR_PLACE_DECALS",
    "EDITOR_STR_PLACE_FLOORS",
    "EDITOR_STR_PLACE_GEN_FURNITURE",
    "EDITOR_STR_SMART_WALLS",
    "EDITOR_STR_SMART_DOORS",
    "EDITOR_STR_SMART_WINDOWS",
    "EDITOR_STR_SMART_DAMAGED_WALLS",
    "EDITOR_STR_ADD_ROOM",
    "EDITOR_STR_EDIT_CAVE",
    "EDITOR_STR_REMOVE_AREA",
    "EDITOR_STR_REMOVE_BUILDING",
    "EDITOR_STR_REPLACE_ROOF",
    "EDITOR_STR_COPY_BUILDING",
    "EDITOR_STR_MOVE_BUILDING",
    "EDITOR_STR_DRAW_ROOM_NUMBER",
    "EDITOR_STR_ERASE_ROOM_NUMBER",
    "EDITOR_STR_TOGGLE_ERASE_MODE",
    "EDITOR_STR_UNDO_LAST",
    "EDITOR_STR_CYCLE_BRUSH_SIZE",
    "EDITOR_STR_WEAPONS",
    "EDITOR_STR_AMMO",
    "EDITOR_STR_ARMOR",
    "EDITOR_STR_EXPLOSIVES",
    "EDITOR_STR_E1",
    "EDITOR_STR_E2",
    "EDITOR_STR_E3",
    "EDITOR_STR_TRIGGERS",
    "EDITOR_STR_ADD_LIGHT_SOURCE",
    "EDITOR_STR_TOGGLE_FAKE_LIGHTS",
    "EDITOR_STR_ADD_EXIT_GRIDS",
    "EDITOR_STR_SPECIFY_NORTH_POINT",
    "EDITOR_STR_SPECIFY_WEST_POINT",
    "EDITOR_STR_SPECIFY_EAST_POINT",
    "EDITOR_STR_SPECIFY_SOUTH_POINT",
    "EDITOR_STR_SPECIFY_CENTER_POINT",
    "EDITOR_STR_SPECIFY_ISOLATED_POINT",
    "EDITOR_STR_NEW_MAP",
    "EDITOR_STR_NEW_BASEMENT",
    "EDITOR_STR_NEW_CAVE",
    "EDITOR_STR_SAVE_MAP",
    "EDITOR_STR_LOAD_MAP",
    "EDITOR_STR_SELECT_TILESET",
    "EDITOR_STR_LEAVE_EDITOR",
    "EDITOR_STR_PREV_DIR",
    "EDITOR_STR_NEXT_DIR",
    "EDITOR_STR_DRAW_GROUND",
    "EDITOR_STR_SET_GROUND",
    "EDITOR_STR_PLACE_CLIFFS",
    "EDITOR_STR_DRAW_ROADS",
    "EDITOR_STR_DRAW_DEBRIS",
    "EDITOR_STR_PLACE_TREES",
    "EDITOR_STR_PLACE_ROCKS",
    "EDITOR_STR_PLACE_JUNK",
    "EDITOR_STR_FILL_AREA",
    "EDITOR_STR_RAISE_BRUSH_DENSITY",
    "EDITOR_STR_LOWER_BRUSH_DENSITY",
    "EDITOR_STR_TERRAIN",
    "EDITOR_STR_BUILDINGS",
    "EDITOR_STR_ITEMS",
    "EDITOR_STR_MERCS",
    "EDITOR_STR_MAP_INFO",
    "EDITOR_STR_MISC",
    "EDITOR_STR_NORTH_ENTRY_POINT",
    "EDITOR_STR_WEST_ENTRY_POINT",
    "EDITOR_STR_EAST_ENTRY_POINT",
    "EDITOR_STR_SOUTH_ENTRY_POINT",
    "EDITOR_STR_CENTER_ENTRY_POINT",
    "EDITOR_STR_ISOLATED_ENTRY_POINT",
    "EDITOR_STR_PRIME",
    "EDITOR_STR_NIGHT",
    "EDITOR_STR_24HR",
    "EDITOR_STR_PANIC1",
    "EDITOR_STR_PANIC2",
    "EDITOR_STR_PANIC3",
    "EDITOR_STR_PANIC4",
    "EDITOR_STR_PANIC5",
    "EDITOR_STR_PANIC6",
    "EDITOR_STR_TRIGGER_NUM",
    "EDITOR_STR_PRESSURE_ACTION",
    "EDITOR_STR_PANIC_ACTION1",
    "EDITOR_STR_PANIC_ACTION2",
    "EDITOR_STR_PANIC_ACTION3",
    "EDITOR_STR_PANIC_ACTION4",
    "EDITOR_STR_PANIC_ACTION5",
    "EDITOR_STR_PANIC_ACITON6",
    "EDITOR_STR_ACTION_NUM",
    "EDITOR_STR_NO_LOCK_ID",
    "EDITOR_STR_EXPLOSION_TRAP",
    "EDITOR_STR_ELECTRIC_TRAP",
    "EDITOR_STR_SIREN_TRAP",
    "EDITOR_STR_SILENT_ALARM",
    "EDITOR_STR_SUPER_TRAP",
    "EDITOR_STR_TRAP_LEVEL_NUM",
    "EDITOR_STR_HIDDEN_LETTER",
    "EDITOR_STR_GRIDNO_INDICATOR",
    "EDITOR_STR_ERASE_GRIDNO_INDICATOR",
    "EDITOR_STR_NO_MAP_LOADED",
    "EDITOR_STR_FILE_TILESET_INDICATOR",
    "EDITOR_STR_WIDTH_INDICATOR",
    "EDITOR_STR_AUTO",
    "EDITOR_STR_PLAYER",
    "EDITOR_STR_ENEMY",
    "EDITOR_STR_CREATURE",
    "EDITOR_STR_NEXT",
    "EDITOR_STR_TOGGLE",
    "EDITOR_STR_VIEWS",
    "EDITOR_STR_SELECTION_METHOD",
    "EDITOR_STR_SMART_METHOD",
    "EDITOR_STR_BUILDING_METHOD",
    "EDITOR_STR_ROOM_NUM",
    "EDITOR_STR_OKAY",
    "EDITOR_STR_CANCEL",
    "EDITOR_STR_EDIT_LOCK",
    "EDITOR_STR_LOCK_ID",
    "EDITOR_STR_TRAP_TYPE",
    "EDITOR_STR_TRAP_LEVEL",
    "EDITOR_STR_LOCKED",
    "EDITOR_STR_STATUS1",
    "EDITOR_STR_STATUS2",
    "EDITOR_STR_STATUS3",
    "EDITOR_STR_STATUS4",
    "EDITOR_STR_STATUS5",
    "EDITOR_STR_RED_IND",
    "EDITOR_STR_GREEN_IND",
    "EDITOR_STR_BLUE_IND",
    "EDITOR_STR_RADIUS",
    "EDITOR_STR_UNDERGROUND",
    "EDITOR_STR_LIGHT_LEVEL",
    "EDITOR_STR_OUTDOORS",
    "EDITOR_STR_BASEMENT",
    "EDITOR_STR_CAVES",
    "EDITOR_STR_DESTINATION",
    "EDITOR_STR_SECTOR",
    "EDITOR_STR_BASEMENT_LEVEL",
    "EDITOR_STR_DEST_ABBREV",
    "EDITOR_STR_GRIDNO",
    "EDITOR_STR_MERC_NAME",
    "EDITOR_STR_ORDERS",
    "EDITOR_STR_COMBAT_ATTITUDE",
    "EDITOR_STR_MERC_COLORS",
    "EDITOR_STR_DONE",
    "EDITOR_STR_PREV_MERC_STANDING_ORDERS",
    "EDITOR_STR_NEXT_MERC_STANDING_ORDERS",
    "EDITOR_STR_PREV_MERC_COMBAT_ATT",
    "EDITOR_STR_NEXT_MERC_COMBAT_ATT",
    "EDITOR_STR_DECREASE_MERC_STAT",
    "EDITOR_STR_INCREASE_MERC_STAT",
    "EDITOR_STR_RANDOM",
    "EDITOR_STR_REG_MALE",
    "EDITOR_STR_BIG_MALE",
    "EDITOR_STR_STOCKY_MALE",
    "EDITOR_STR_FEMALE",
    "EDITOR_STR_BLOODCAT",
    "EDITOR_STR_ORDERS_LABEL",
    "EDITOR_STR_ATTITUDE_LABEL",
    "EDITOR_STR_ARMY",
    "EDITOR_STR_ADMIN",
    "EDITOR_STR_ELITE",

    "EDITOR_STR_ATT_LABEL_1",
    "EDITOR_STR_ATT_LABEL_2",
    "EDITOR_STR_ATT_LABEL_3",
    "EDITOR_STR_ATT_LABEL_4",
    "EDITOR_STR_ATT_LABEL_5",
    "EDITOR_STR_ATT_LABEL_6",
    "EDITOR_STR_ATT_LABEL_7",
    "EDITOR_STR_ATT_LABEL_8",
    "EDITOR_STR_ATT_LABEL_9",
    "EDITOR_STR_ATT_LABEL_10",
    "EDITOR_STR_ATT_LABEL_11",
    "EDITOR_STR_ATT_LABEL_12",
    "EDITOR_STR_ATT_LABEL_13",

    "EDITOR_STR_BODY_ATT_1",
    "EDITOR_STR_BODY_ATT_2",
    "EDITOR_STR_BODY_ATT_3",
    "EDITOR_STR_BODY_ATT_4",

    "EDITOR_STR_UPPER_RANDOM",
    "EDITOR_STR_CURRENT_PROFILE",

    "EDITOR_STR_ORDER_LABEL_1",
    "EDITOR_STR_ORDER_LABEL_2",
    "EDITOR_STR_ORDER_LABEL_3",
    "EDITOR_STR_ORDER_LABEL_4",
    "EDITOR_STR_ORDER_LABEL_5",
    "EDITOR_STR_ORDER_LABEL_6",
    "EDITOR_STR_ORDER_LABEL_7",
    "EDITOR_STR_ORDER_LABEL_8",
    "EDITOR_STR_SLOT_NUM",
    "EDITOR_STR_PATROL_BUT_NO_WP",
    "EDITOR_STR_WP_BUT_NO_PATROL",
    "EDITOR_STR_PLACEMENT_NOT_COPIED",
    "EDITOR_STR_PLACEMENT_COPIED",
    "EDITOR_STR_BUFFER_EMPTY",
    "EDITOR_STR_PLACEMENT_PASTED",
    "EDITOR_STR_MAX_PLACEMENTS_USED",
    "EDITOR_STR_SMALL",
    "EDITOR_STR_MEDIUM",
    "EDITOR_STR_LARGE",
    "EDITOR_STR_XLARGE",
    "EDITOR_STR_WIDTH",
    "EDITOR_STR_AREA",
    "EDITOR_STR_EXIT_EDITOR",
    "EDITOR_STR_REMOVE_ALL_LIGHTS",
    "EDITOR_STR_REVERSE_SCHEDULES",
    "EDITOR_STR_CLEAR_SCHEDULES",
    "EDITOR_STR_REMOVE_TREETOPS",
    "EDITOR_STR_SHOW_TREETOPS",
    "EDITOR_STR_START_NEW_BASEMENT",
    "EDITOR_STR_START_NEW_CAVE",
    "EDITOR_STR_START_NEW_OUTDOOR",
    "EDITOR_STR_WIPE_GROUND_TEXTURE",
    "EDITOR_STR_HOMEKEY",
    "EDITOR_STR_TOGGLE_LIGHTING",
    "EDITOR_STR_INSERTKEY",
    "EDITOR_STR_TOGGLE_FILLMODE",
    "EDITOR_STR_BKSPACEKEY",
    "EDITOR_STR_DELKEY",
    "EDITOR_STR_QUICKERASE",
    "EDITOR_STR_ESCKEY",
    "EDITOR_STR_EXITEDITOR",
    "EDITOR_STR_PGUPDN",
    "EDITOR_STR_CHANGE_OBJECT",
    "EDITOR_STR_F1KEY",
    "EDITOR_STR_HELP_SCREEN",
    "EDITOR_STR_F10KEY",
    "EDITOR_STR_SAVE_CURRENT_MAP",
    "EDITOR_STR_F11KEY",
    "EDITOR_STR_LOAD_MAP_CURRENT",
    "EDITOR_STR_PLUSMINUSKEY",
    "EDITOR_STR_CHANGE_SHADOW",
    "EDITOR_STR_SHIFTKEY",
    "EDITOR_STR_CHANGE_SHADOW_05",
    "EDITOR_STR_NUMKEY",
    "EDITOR_STR_CHANGE_MAP_FILENAME",
    "EDITOR_STR_BKEY",
    "EDITOR_STR_BRUSHSIZE",
    "EDITOR_STR_DKEY",
    "EDITOR_STR_OKEY",
    "EDITOR_STR_DRAW_OBSTACLE",
    "EDITOR_STR_RKEY",
    "EDITOR_STR_DRAW_ROCKS",
    "EDITOR_STR_TKEY",
    "EDITOR_STR_TOGGLE_TREES",
    "EDITOR_STR_GKEY",
    "EDITOR_STR_DRAW_GROUND_TEXTURES",
    "EDITOR_STR_WKEY",
    "EDITOR_STR_DRAW_BUILDING_WALLS",
    "EDITOR_STR_EKEY",
    "EDITOR_STR_HKEY",
    "EDITOR_STR_TOGGLE_ROOFS",
    "EDITOR_STR_MAP_DATA_CORRUPTED",
    "EDITOR_STR_ENTER_GRIDNO",
    "EDITOR_STR_TOGGLE_HIDE_FLAG",
    "EDITOR_STR_NO_ITEM_SELECTED",
    "EDITOR_STR_SLOT_AVAIL_FOR",
    "EDITOR_STR_RANDOM_GEN",
    "EDITOR_STR_KEYS_NOT",
    "EDITOR_STR_PROFILE_ID_OWNER",
    "EDITOR_STR_ITEM_CLASS_NOT",
    "EDITOR_STR_SLOT_LOCKED",
    "EDITOR_STR_STATUS",
    "EDITOR_STR_ROUNDS",
    "EDITOR_STR_TRAPLVL",
    "EDITOR_STR_QTY",
    "EDITOR_STR_DOLLARS",
    "EDITOR_STR_TOLERANCE",
    "EDITOR_STR_ALARM_TRIG",
    "EDITOR_STR_EXIST_CHANCE",
    "EDITOR_STR_SILENCER",
    "EDITOR_STR_SNIPERSCOPE",
    "EDITOR_STR_LASERSCOPE",
    "EDITOR_STR_BIPOD",
    "EDITOR_STR_DUCKBILL",
    "EDITOR_STR_GLAUNCHER",
    "EDITOR_STR_CERAMIC",
    "EDITOR_STR_DETONATOR",
    "EDITOR_STR_PANIC_WARNING",
    "EDITOR_STR_MAP_STR",
    "EDITOR_STR_SAVE_CHOICE",
    "EDITOR_STR_LOAD_CHOICE",
    "EDITOR_STR_NO_FILES",
    "EDITOR_STR_DEL_READ_ONLY",
    "EDITOR_STR_DELETE_FILE",
    "EDITOR_STR_ILLEGAL_FILENAME",
    "EDITOR_STR_READONLY_TRY_AGAIN",
    "EDITOR_STR_OVERWRITE",
    "EDITOR_STR_LOADING_STR",
    "EDITOR_STR_FILENAME",
    "EDITOR_STR_UPDATE_WORLD",
    "EDITOR_STR_SAVING_STR",
    "EDITOR_STR_MAP_DATA_JUST_CORRUPTED",
    "EDITOR_STR_ERROR_LOADING",
    "EDITOR_STR_DAT_STR",
    "EDITOR_STR_CANCEL_SELECTIONS",
    "EDITOR_STR_ACCEPT_SELECTIONS",
    "EDITOR_STR_SCROLLUP",
    "EDITOR_STR_SCROLLDN",
    "EDITOR_STR_DEFAULT_TILESET_STR",
    "EDITOR_STR_FILE_SUB_STR",
    "EDITOR_STR_CURRENT_TILESET_STR",
    "EDITOR_STR_RANK_LABEL",
    "EDITOR_STR_PLACEMENTS",
    "EDITOR_STR_TOTAL",
    "EDITOR_STR_MISSING",
    "EDITOR_STR_PREV_LOADSCREEN",
    "EDITOR_STR_NEXT_LOADSCREEN",
    "EDITOR_STR_NUM_BLOODCATS",
    "EDITOR_STR_CAMPAIGN",
    "EDITOR_STR_CHECK",
    "EDITOR_STR_DROPPABLE",
    "EDITOR_STR_DROP_ITEMS",
]

def scan_file(path, dupes = None):
    if dupes is None:
        print("Got no valid dupes dict. Generating...")
        dupes = check_for_duplicates()

    lines = []
    with open(path, "rb") as in_:
        for line in in_:
            line = line.decode()
            lines.append(line)

    changed = False
    for line_ind, line in enumerate(lines):
        #if 'L"' in line:
            #print(line)
        line_new = line
        for str1_ind, str1 in enumerate(editor_strings):
            if str1 in line_new:
                #print(str1_ind, str1)
                print("<", line_new, end="")

                enum = editor_string_enum[str1_ind]

                if str1 in dupes:
                    print("Ambiguous string found. Possible choices:")
                    print("0:", dupes[str1][0])
                    print("1:", dupes[str1][1])
                    while True:
                        rep = input("Choose: ")
                        if rep == "0":
                            enum = dupes[str1][0]
                            break
                        elif rep == "1":
                            enum = dupes[str1][1]
                            break



                str2 = "gzEditorStrings[" + enum + "]"
                line_new = line_new.replace(str1, str2)

                print(">", line_new, end="")

                print()
        if line != line_new:
            changed = True
            lines[line_ind] = line_new


    if not changed:
        return

    # make backup:
    os.rename(path, path+".translate_editor.bak")
    with open(path, "wb") as out:
        for line in lines:
            out.write(line.encode())


def translate_all():
    dupes = check_for_duplicates()

    import glob
    for path1 in glob.glob("src_ja2/game/Editor/*.c"):
    #for path1 in glob.glob("src_ub/game/Editor/*.c"):
        print(path1)
        scan_file(path1, dupes = dupes)

def check_for_duplicates():
    seen = []
    seen_enum = []
    # dict of str: [enum1, enum2, ...]
    dupes = {}
    for str1_ind, str1 in enumerate(editor_strings):
        if not str1 in seen:
            seen.append(str1)
            seen_enum.append(editor_string_enum[str1_ind])
        else:
            #print(editor_string_enum[str1_ind], str1, "is a dupe of", seen_enum[seen.index(str1)])
            #print(
            #print(editor_strings.index(str1))

            if str1 in dupes:
                raise Exception("More than two enums for one string not implemented.")

            #print(str1, "has multiple enums:")
            #print("  ", seen_enum[seen.index(str1)])
            #print("  ", editor_string_enum[str1_ind])

            dupes[str1] = [seen_enum[seen.index(str1)], editor_string_enum[str1_ind]]

    return dupes


def query_enum(str1):
    print("Searching for enum containing:", str1)
    for ind, str2 in enumerate(editor_string_enum):
        if str1.casefold() in str2.casefold():
            print(str2, ":", editor_strings[ind])
    print()

def query_str(str1):
    print("Searching for string containing:", str1)
    for ind, str2 in enumerate(editor_strings):
        if str1.casefold() in str2.casefold():
            print(editor_string_enum[ind], ":", str2)
    print()


def main():
    import sys
    if len(sys.argv) == 1:
        print("Usage ...")
        return

    if sys.argv[1] == "-T":
        print("Translate all files.")
        translate_all()
    elif sys.argv[1] == "-e" and len(sys.argv) == 3: # Grep in enum
        query_enum(sys.argv[2])
    elif sys.argv[1] == "-s" and len(sys.argv) == 3: # Grep in string
        query_str(sys.argv[2])
    else:
        print("Invalid argument(s).")



    #query_enum("DRAW_GROUND")
    #query_str("Delete current")

    #query_enum("EDITOR_STR_DAT_STR")





if __name__ == "__main__":
    main()
