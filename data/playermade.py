from parse import *

cord = re.finditer(fontRegex, '''
PLAYER-MADE FONTS IN CORDILLERA
Springs of Seymour Butz (arcane-aspected)
Kagawa Park (44, 41 Cordillera, a Park, Neighborhood: Minglewood)
Leyline direction: None
MP: 31
Last scouted: Wed 2022-04-27 20:10:37 
Springs of Value Judgement (cold-aspected)
The Quickway (43, 41 Cordillera, a Quickway, Neighborhood: The Quickway)
Leyline direction: South-East
MP: 36
Last scouted: Wed 2022-04-27 20:12:26 
Springs of Value Judgement (electric-aspected)
Gateway Park (41, 39 Cordillera, a Park, Neighborhood: Minglewood)
Leyline direction: South-East
MP: 24
Last scouted: Wed 2022-04-27 20:13:28
Arglesby — 04/29/2022
Sparks of a floating terror (electric-aspected)
Vergil's (31, 35 Cordillera, a Gravel Parking Lot, Neighborhood: Praxis)
Leyline direction: None
MP: 10
Last scouted: Fri 2022-04-29 09:28:32
a fonting terror (arcane-aspected)
Sink Industrial Expansion Site (33, 36 Cordillera, an Empty Lot, Neighborhood: Praxis)
Leyline direction: None
MP: 18
Last scouted: Fri 2022-04-29 09:30:22)
Springs of a goating terror (cold-aspected)
Qaryat Cemetery (25, 35 Cordillera, a Cemetery, Neighborhood: Praxis)
Leyline direction: None
MP: 29
Last scouted: Fri 2022-04-29 09:33:30 
Arglesby — 04/30/2022
Jumping Falls (arcane-aspected)
(48, 47 Cordillera, a Grassland, Neighborhood: Fenwater Meadow)
Leyline direction: None
MP: 18
Last scouted:  Fri 2022-04-29 23:56:16''')

cent = re.finditer(fontRegex, '''
PLAYER-MADE FONTS IN CENTRUM 
placeholder
Cage of Corona-chan (acid-aspected)
Empty Lot (39, 34 Centrum, an Empty Lot, Neighborhood: Cordillera Centrum)
Leyline direction: None
MP: 26
Last scouted: Thu 2022-04-28 10:33:48
Cage of Corona-chan (unholy-aspected)
The Pearl's Pier (40, 33 Centrum, a Docks, Neighborhood: Centrum)
Leyline direction: None
MP: 45
Last scouted: Thu 2022-04-28 10:35:41
Cage of Clodia (acid-aspected)
Commuter Zone Expansion (45, 29 Centrum, an Empty Lot, Neighborhood: Cordillera Centrum)
Leyline direction: South-East
MP: 100
Last scouted: Thu 2022-04-28 10:36:37
The Gourmand's Special Spice (acid-aspected)
The Quickway (45, 28 Centrum, a Rapid Transit Line, Neighborhood: The Quickway)
Leyline direction: None
MP: 76
Last scouted: Thu 2022-04-28 10:37:30
Cage of Clodia (unholy-aspected)
Centrum Specialty Courtyard (42, 27 Centrum, a Park, Neighborhood: Cordillera Centrum)
Leyline direction: None
MP: 11
Last scouted: Thu 2022-04-28 10:38:54''')

purg = re.finditer(fontRegex, u'''
PLAYER-MADE FONTS IN PURGATORIO
[placeholder]
Springs of Holo (electric-aspected)
Arsenal Park (17, 18 Purgatorio, a Park, Neighborhood: Hyperborea 1st Arrondissement)
Leyline direction: None
MP: 20
Last scouted: Mon 2022-05-02 14:36:53
Arglesby — 05/05/2022
Springs of ᛊᛏᚨᛁᚾᚨᛉ (impact-aspected)
Stoneland (29, 15 Purgatorio, a Stoneland, Neighborhood: Ash Harbor)
Leyline direction: None
MP: 46
Last scouted: Thu 2022-05-05 21:22:50
Springs of ᛊᛏᚨᛁᚾᚨᛉ (??)
Dry Grassland (29, 16 Purgatorio, a Dry Grassland, Neighborhood: Ash Harbor)
Leyline direction: None
MP: ??
Thu 2022-05-05 21:22:13
Springs of a disturbingly sexy weasel (??)
Stoneland (29, 17 Purgatorio, a Stoneland, Neighborhood: Ash Harbor)
Leyline direction: None
MP: ??
Last scouted: Thu 2022-05-05 21:22:05 
Arglesby — 05/06/2022
Water Palace [Cold] (cold-aspected)
Dust Plains (21, 12 Purgatorio, a Dust Plains, Neighborhood: Ash Harbor)
Leyline direction: North-East
MP: 54
Last scouted: Fri 2022-05-06 11:16:25 
Burning Palace [Fire] (fire-aspected)
Dust Plains (22, 13 Purgatorio, a Dust Plains, Neighborhood: Ash Harbor)
Leyline direction: North
MP: 34
Last scouted: Fri 2022-05-06 11:18:14
Wizard's Palace [Arcane] (arcane-aspected)
Stoneland (24, 13 Purgatorio, a Stoneland, Neighborhood: Ash Harbor)
Leyline direction: North-West
MP: 13
Last scouted: Fri 2022-05-06 11:19:13 
The School of the Undefeated of the East (cold-aspected)
Faded Docks (23, 9 Purgatorio, a Faded Docks, Neighborhood: Ash Harbor)
Leyline direction: None
MP: 76
Leyline direction: Fri 2022-05-06 11:20:50
Springs of Ling (cold-aspected)
Faded Docks (24, 9 Purgatorio, a Faded Docks, Neighborhood: Ash Harbor)
Leyline direction: South-West
MP: 44
Last scouted: Fri 2022-05-06 11:21:50
Springs of Ling (cold-aspected)
Faded Docks (23, 8 Purgatorio, a Faded Docks, Neighborhood: Ash Harbor)
Leyline direction: None
MP: 4
Last scouted: Fri 2022-05-06 11:22:46
Frigid Springs of Jwari Disruption (cold-aspected)
Forlorn Peak (4, 24 Purgatorio, a Mountain Summit, Neighborhood: Forlorn Hope Mountains)
Leyline direction: East
MP: 41
Last scouted: Fri 2022-05-06 11:25:53
Sulfur Springs of Jwari Disruption (acid-aspected)
Mountain (5, 24 Purgatorio, a Mountain, Neighborhood: Forlorn Hope Mountains)
Leyline direction: South
MP: 35
Last scouted: Fri 2022-05-06 11:26:49
Galvanic Springs of Jwari Disruption (electric-aspected)
Forlorn Peak (5, 25 Purgatorio, a Mountain Summit, Neighborhood: Forlorn Hope Mountains)
Leyline direction: South
MP: 34
Last scouted: Fri 2022-05-06 11:27:43 
Hot Springs of Jwari Disruption (fire-aspected)
Forlorn Peak (3, 25 Purgatorio, a Mountain Summit, Neighborhood: Forlorn Hope Mountains)
Leyline direction: None
MP: 98
Last scouted: Fri 2022-05-06 11:30:49
Mystic Springs of Jwari Disruption (arcane-aspected)
Forlorn Peak (4, 26 Purgatorio, a Mountain Summit, Neighborhood: Forlorn Hope Mountains)
Leyline direction: None
MP: 97
Last scouted: Fri 2022-05-06 11:31:52
Necrotic Springs of Jwari Disruption (death-aspected)
Mountain (6, 25 Purgatorio, a Mountain, Neighborhood: Forlorn Hope Mountains)
Leyline direction: South-West
MP: 35
Last scouted: Fri 2022-05-06 11:35:04''')

styg = re.finditer(fontRegex, '''
PLAYER-MADE FONTS IN STYGIA 
placeholder
Deadly Cage of Owen Grady (death-aspected)
Frozen River (7, 15 Stygia, a Frozen Wastes, Neighborhood: Uffern)
Leyline direction: North-West
MP: 23
Last scouted: Thu 2022-04-28 19:12:38
Cage of Klotta Gies (unholy-aspected)
Frozen River (6, 15 Stygia, a Frozen Wastes, Neighborhood: Uffern)
Leyline direction: North
MP: 3
Last scouted: Thu 2022-04-28 19:16:26
Arglesby — 04/28/2022
Cage of Owen Grady (fire-aspected)
Frozen Wastes (5, 15 Stygia, a Frozen Wastes, Neighborhood: Magog)
Leyline direction: North-East
MP: 3
Last scouted: Thu 2022-04-28 19:16:26 
Arglesby — 05/04/2022
Cage of Corona-chan (death-aspected)
Boneland (19, 2 Stygia, a Boneland, Neighborhood: Penumbra)
Leyline direction: North-West
MP: 22
Last scouted: Wed 2022-05-04 19:37:07
Cage of Corona-chan (unholy-aspected)
Boneland (20, 1 Stygia, a Boneland, Neighborhood: Penumbra)
Leyline direction: None
MP: 84
Last scouted: Wed 2022-05-04 19:38:50 
Cage of Corona-chan (slashing-aspected)
Boneland (20, 2 Stygia, a Boneland, Neighborhood: Penumbra)
Leyline direction: North
MP: 73
Last scouted: Wed 2022-05-04 19:40:23
Cage of Corona-chan (fire-aspected)
Boneland (19, 1 Stygia, a Boneland, Neighborhood: Penumbra)
Leyline direction: ??
MP: 96
Last scouted: Wed 2022-05-04 19:42:37 
Cage of Corona-chan (piercing-aspected)
Circus Carnivorous (18, 1 Stygia, a Circus Carnivorous, Neighborhood: Penumbra)
Leyline direction: East
MP: 34
Last scouted: Wed 2022-05-04 19:45:40 
Arglesby — 05/04/2022
Cage of Corona-chan (impact-aspected)
Circus Carnivorous (18, 2 Stygia, a Circus Carnivorous, Neighborhood: Penumbra)
Leyline direction: East
MP: 77
Last scouted: Wed 2022-05-04 20:01:39
Cage of Corona-chan (acid-aspected)
Egg Field (19, 3 Stygia, an Egg Field, Neighborhood: Penumbra)
Leyline direction: North
MP: 19
Last scouted: Wed 2022-05-04 20:05:47
Cage of Corona-chan (cold-aspected)
Egg Field (20, 4 Stygia, an Egg Field, Neighborhood: Penumbra)
Leyline direction: North
MP: 35
Wed 2022-05-04 20:07:11''')

elys = re.finditer(fontRegex, '''
PLAYER-MADE FONTS IN ELYSIUM 
placeholder
Arglesby — Yesterday at 1:32 PM
Grove of a patronising old man (holy-aspected)
Mountain (20, 15 Elysium, a Mountain, Neighborhood: Arcadia)
Leyline direction: None
MP: 32
Last scouted: Sat 2022-05-14 11:31:05
Grove of a patronising old man (holy-aspected)
Mountain (19, 15 Elysium, a Mountain, Neighborhood: Arcadia)
Leyline direction: None
MP: 36
Last scouted: Sat 2022-05-14 11:32:44
Grove of a patronising old man (holy-aspected)
Mountain (19, 14 Elysium, a Mountain, Neighborhood: Arcadia)
Leyline direction: None
MP: 35
Last scouted: Sat 2022-05-14 11:33:31
Grove of a patronising old man (impact-aspected)
Mountain (19, 13 Elysium, a Mountain, Neighborhood: Arcadia)
Leyline direction: None
MP: 33
Last scouted: Sat 2022-05-14 11:35:10
Grove of a patronising old man (holy-aspected)
Mountain (20, 13 Elysium, a Mountain, Neighborhood: Arcadia)
Leyline direction: None
MP: 76
Last scouted: Sat 2022-05-14 11:35:48
Grove of Manco (piercing-aspected)
(20, 4 Elysium, a Lush Field, Neighborhood: Zion)
Leyline direction: None
MP: 100
Last scouted: Sat 2022-05-14 11:37:08
Arglesby — Today at 7:33 PM
Springs of Chimera (electric-aspected)
(3, 12 Elysium, an Idyllic Forest, Neighborhood: Ashavan)
Leyline direction: None
MP: 34
Last scouted: Sun 2022-05-15 17:31:46
Springs of Chimera (fire-aspected)
Forest Primeval (2, 12 Elysium, an Idyllic Forest, Neighborhood: Ashavan)
Leyline direction: None
MP: 36
Last scouted: Sun 2022-05-15 17:33:26
Springs of Chimera (cold-aspected)
Forest Primeval (2, 11 Elysium, an Idyllic Forest, Neighborhood: Ashavan)
Leyline direction: None
MP: 35
Last scouted: Sun 2022-05-15 17:34:37)
Springs of Chimera (arcane-aspected)
Forest Primeval (1, 11 Elysium, an Idyllic Forest, Neighborhood: Ashavan)
Leyline direction: None
MP: 34
Last scouted: Sun 2022-05-15 17:35:52''')

convert(cord, 'Cordillera', 'generated/Cordillera.json')
convert(cent, 'Centrum', 'generated/Centrum.json')
convert(purg, 'Purgatorio', 'generated/Purgatorio.json')
convert(styg, 'Stygia', 'generated/Stygia.json')
convert(elys, 'Elysium', 'generated/Elysium.json')
