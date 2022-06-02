from parse import *

cord = re.finditer(fontRegex, '''
Vesper Arch
holy-aspected
Choral Forest (39, 16 Cordillera, a Forest, Neighborhood: Choral Forest)
A great arch of white ivory rises from the ground here, though a constant clicking and whirring seems to emanate from it. A melodious chorus of chiming augments the periodic peal of ethereal bells that are heard but not seen emanates from the arch
Leyline direction: South-West

The Phantasmal Barrow
death-aspected
Ce Metary (28, 18 Cordillera, a Cemetery, Neighborhood: Sleepy Hollow)
A large heaped mound of earth sits here, covered in lush grass and succulents that have an unearthly, translucent greyish color. The air is heavy with a cloying scent of decaying flowers.
Leyline direction: South

Watchers Light
fire-aspected
Choral Forest (50, 19 Cordillera, a Forest, Neighborhood: Choral Forest)
A great, smokeless, everburning bonfire of blue and green flame dominates the area; oddly, while it puts off light, there is no heat, no fuel, and nothing in the area seems to be consumed.
Leyline direction: South-East

Weeping Cube
unholy-aspected
Tottering Heights (57, 42 Cordillera, a Mountain, Neighborhood: Belmont Court)
An enormous, pitted black cube of wrought iron juts from the ground here. From numerous points on the surface of the cube, half-congealed blood slowly oozes, which has left the ground around the cube stained a deep, almost black, red.
Leyline direction: North-East

Juggling Quagmire
acid-aspected
Grassland (47, 49 Cordillera, a Grassland, Neighborhood: Fenwater Meadow)
Occasionally the ground here trembles as small wet boulders, surfaces pitted and blackened, are belched forth a few feet from the ground before falling back into the earth and sinking quickly beneath the surface, which ripples as though it were liquid as the boulders pass through but still seems solid to the touch.
Leyline direction: North-East

Silverfall
arcane-aspected
Cropland (65, 15 Cordillera, a Cropland, Neighborhood: Port Hope)
A large black obelisk topped by a bowl rather than a point, perhaps three meters high, with no visible markings rises from the ground here. Silver motes of light cascade down from the edges of the bowl and swirl around the obelisk, soundlessly disappearing before touching any solid object
Leyline direction: West

Vampire Rose
piercing-aspected
Cropland (18, 30 Cordillera, a Cropland, Neighborhood: Great Plains)
A number of neatly-trimmed, well-cultivated white and yellow rose bushes sit in an orderly circle here; upon closer inspection, their thorns are abnormally elongated and sharp and even the leaves and the petals of the roses curl and narrow to surprisingly pointed tips.
Leyline direction: ?

Saeth Gylchog
cold-aspected
Cropland (6, 33 Cordillera, a Cropland, Neighborhood: Great Plains)
Five rock circles, with each rock perhaps a foot tall, are arranged in a V-shape with the point of the V facing to the east here.
Leyline direction: ?

Sawcrest
slashing-aspected
Roseway Park (46, 32 Cordillera, a Park, Neighborhood: Belmont Court)
A great semicircular ridge of pyrite-laced quartz rises vertically from the ground here. It sparkles when looked at directly but gives the uneasy illusion of being in rapid motion when in the corners of the field of vision.
Leyline direction: South-West
''')

purg = re.finditer(fontRegex, '''
Crucible of Goros
fire-aspected
Axis Mundi (17, 19 Purgatorio, an Axis Mundi, Neighborhood: Hyperborea 1st Arrondissement)
A hardened lava flow, perhaps the height of a man, has erupted from the ground here; one side gapes open in a white-hot maw from which the glow of a lava pit inside the cooled edges can be seen.
Leyline direction: South-East

Coil of the Pulse
electric-aspected
Iverson Power (8, 15 Purgatorio, a Power Plant, Neighborhood: Iverson)
A thick coil of unknown metal stands here. Sparks race up the coil in a regular rhythm, popping and dissipating as they reach its apex.
Leyline direction: East

Beyonders Howl
slashing-aspected
Northcamp University (13, 11 Purgatorio, an University, Neighborhood: Northcamp)
A sharp, almost cutting wind howls and buffets the air here. As the wind swirls rapidly about the ground, the clatter of small objects caught in its gale almost masks the hissing, eerie howl it makes as it whips about.
Leyline direction: North-West

Ironshrub
piercing-aspected
Forest (17, 28 Purgatorio, a Forest, Neighborhood: Forlorn Hope Mountains)
What appears to be a shrub made of wrought iron has overgrown most of this location, its thin tendrils covered in protective spikes and the thin, black needle clusters at the end of each of its shoots appearing as small, spiked sea urchins.
Leyline direction: North-East

Mouldering Pillar
death-aspected
Ancient Lighthouse (22, 11 Purgatorio, an Ancient Lighthouse, Neighborhood: Ash Harbor)
The stench of rot washes out from a crater that appears to be a great, open sore, with a sickly flow of green and purple mist cascading outward.
Leyline direction: North-East 

Skyswarm
impact-aspected
Lyubov Orlova (23, 4 Purgatorio, a Shipwreck, Neighborhood: Ash Harbor)
A cluster of enormous boulders spin and float gently in the void high above this location. Occasionally there is a great commotion and awful grinding as two boulders slowly come into contact, grinding against each other for a moment before being mutually flung away in different directions than before.
Leyline direction: South-West

Dancing String
acid-aspected
Bathtub Gin (25, 25 Purgatorio, a Forgotten Bar, Neighborhood: Hyperborea 8th Arrondissement)
A ring comprised of perhaps two dozen fist-sized balls of varying colors spins and dances in the air here, weaving and bobbing away from obstacles and obstructions as they float about. A citrus tang wafts in the air.
Leyline direction: West

Gaping Idol
cold-aspected
Forlorn Peak (4, 25 Purgatorio, a Mountain Summit, Neighborhood: Forlorn Hope Mountains)
A small marble figurine carved in the shape of a lizard-like head with mouth that gapes up into the sky sits on the ground here, a whorling vortex of sparkling fog suspended above the open mouth. The ground nearby slick with ice and frost.
Leyline direction: South-East 
''')

styg = re.finditer(fontRegex, '''
Floes Aloft
cold-aspected
The River Antaeus (12, 4 Stygia, a Frozen River, Neighborhood: Hades Tol)
A number of ice floes float at about eye level here, tracing their own slow path across the sky and grinding against each other from time to time, pushing some up and others down so their movement cuts a jagged band through the air.
Leyline direction: West

Wash of E-Moch-Nahr
acid-aspected
Egg Field (17, 7 Stygia, an Egg Field, Neighborhood: Penumbra)
A sour stench stings the nostrils and the eyes here. A large boulder of jet-black stone rises from the ground here, with one of the faces abnormally smooth and flat. From a cleft atop the flat face, a thin amber liquid flows forth, coating the face of the rock and evaporating before it reaches the ground.
Leyline direction: North

Obsidian Sentinel
impact-aspected
Heart's Blood (20, 8 Stygia, an Ebony Tower, Neighborhood: Penumbra)
Two thick walls of lava rock support a large obsidian sculpture, which stands astride the walls. The sculpture is vaguely man-shaped, with great massive, misshapen fists, horned jutting from what looks to be a head set directly atop the torso with no neck and furnished with a deformed mouth twisted into what appears to be a hideous-looking scream.
Leyline direction: North-West

Pustule of Tholaghru
unholy-aspected
Yaruahn Ahr-natthi (3, 12 Stygia, an Ebony Tower, Neighborhood: Magog)
A deep pit sits in this location; overflowing the bounds of the pit is a thick, dark blue liquid that fills the area with an horrific stench. The liquid fizzes and spits as it sloughs off the mound of liquid piled up in the hole and onto the ground around it.
Leyline direction: South 

Hellforge
fire-aspected
Firepits (13, 16 Stygia, a Firepits, Neighborhood: Uffern)
Rising from the earth here is a bulbous structure, appearing to be knit together by some sort of organic fibers. Arches and knots in the fibers reveal a strong blue flame in the midst of the structure; the thick, calloused and flat top of the structure is about half the height of a man and has numerous openings allowing access to the blue flame; the distortions from the heat can be seen in the air above these holes even though the surface of the structure itself is quite cool to the touch.
Leyline direction: North-East

Living Whips
slashing-aspected
Slave Pens (6, 18 Stygia, a Slave Pens, Neighborhood: Chorazin)
A circle of gargantuan weeping-willow like trees grows here; their abnormally elongated branches do not sway with the breeze but rather undulate like malevolent snakes, the air snapping with the sound of cracking whips as they shoot out smartly in all directions.
Leyline direction: North

Hadean Aurora
death-aspected
Forsaken Palace (6, 4 Stygia, an Ebony Tower, Neighborhood: Hades Tol)
The darkness here is illuminated slightly by ribbons of indigo and deep, dark green tracing and undulating across the sky. Occasionally, showers of opalescent violet and green flakes of some unknown substance rain down upon the ground.
Leyline direction: South-West

Rusted Maiden
piercing-aspected
Stygian Ruins (15, 13 Stygia, a Stygian Ruins, Neighborhood: Jahannam)
An enormous, pitted box of cast iron, at least thrice the height of a man, stands here with one side ajar. The open side of the box is fitted with hundreds of long, wicked-looking cast iron spikes, spotted red with rust and black with ichor. 
Leyline direction: North 
''')

elys = re.finditer(fontRegex, '''
Springs of Chimera
arcane-aspected
Forest Primeval (1, 11 Elysium, an Idyllic Forest, Neighborhood: Ashavan)
Several bright, scintillating rainbows dance in the perpetual mist hanging in the air here.
Leyline direction: ???

Marble Dais
holy-aspected
Cradle of Life (17, 18 Elysium, a Lambent Conservatory, Neighborhood: Arcadia)
A large marble dais rise from the ground here. Atop the dais, a number of small carved hemispheres, perhaps the size of a fist, both extend from its surface and are carved in relief. Each raised hemisphere seems to glow from within with a gentle pink light and each relief hemisphere seems to be abnormally dark for the surroundings, appearing as though falling in an indigo shadow.
Leyline direction: ???

Clockwork Cloud
impact-aspected
Automaton Factory (5, 20 Elysium, a Clockwork Tower, Neighborhood: Ashavan)
The air here is abuzz with a mass of tiny, flying bodies that almost obscure one's vision, most the size of insects, but given away as clockwork by the glints and flashes of light off of brass. The mass flows effortlessly around objects and creatures in the area without impeding their progress in the slightest.
Leyline direction: East

Crackling Crevasse
electric-aspected
Agri Dagi (2, 7 Elysium, a Mountain Summit, Neighborhood: Empyrean)
A chasm splits the ground here; large white rocks jutting horizontally from the sides towards the center give it the appearance of a gaping maw. Brilliant blue motes of light can occasionally be glimpsed leaping among the white rocks. 
Leyline direction: South

The Twilight Copse
death-aspected
Idyllic Meadow (6, 10 Elysium, an Idyllic Meadow, Neighborhood: Celestia)
The air here seems dry and brackish, almost hostile to breathe; amid a small cluster of gnarled trees appears a swirling cloud of faint light that seems to roughly outline the shape of a great tree, swaying in the wind with tendrils of faint twinkling light anchored to the soil as roots might be.
Leyline direction: South-West

Crystal Sundial
piercing-aspected
The Tower of Truth (6, 7 Elysium, an Ivory Tower, Neighborhood: Empyrean)
A crystalline structure perhaps the height of a man and twice as wide stands here, focusing rays of light toward a single pitch-black crystal in the center. A single ray of brilliant white light splays forth from this crystal, illuminating in turn three crystals of various colors in progressively larger sizes set in concentric rings.
Leyline direction: South-West 


Kingdom Apple
slashing-aspected
The Tower of Faith (11, 9 Elysium, an Ivory Tower, Neighborhood: Carmel)
An intricately engraved brass sphere of indeterminate origin is mounted on a marble pedestal here. Several spindles on whip around the sphere at varying speeds and in what appear to be random directions, but always following the paths of the intricate engravings and occasionally slowing to avoid collisions with other spindles, but never fully coming to a halt. The sphere itself seems rotate in all directions atop the pedestal, though it never loses contact from the pedestal for even a moment.
Leyline direction: East

Breathing Cloud
fire-aspected
Mountain (8, 4 Elysium, a Mountain, Neighborhood: Empyrean)
An enormous cloud of smokeless flame hovers high in the air here, the cloud slowly pulsing in and out as though alive. The air underneath the cloud is warm, almost uncomfortably hot.
Leyline direction: South-East 
''')

convert(cord, 'Cordillera', 'generated/Cordillera.json')
convert(purg, 'Purgatorio', 'generated/Purgatorio.json')
convert(styg, 'Stygia', 'generated/Stygia.json')
convert(elys, 'Elysium', 'generated/Elysium.json')
