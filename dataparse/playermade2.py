from parse import *

cord = re.finditer(tiledescRegex, '''
Sink Industrial Expansion Site (33, 36 Cordillera, an Empty Lot, Neighborhood: Praxis)
You are standing outside of Sink Industrial Expansion Site. This lot has been cleared of vegetation and is surrounded with a damaged chain-link fence. Stacks of supplies and some construction vehicles can be found here, and the foundation of some large building has been partially excavated. The sky overhead is bright and blue, and the structure of a great dome can be seen above the clouds.
Someone has written ALL POWER TO THE PEOPLE in marker on a rock here.
a fonting terror: Several bright, scintillating rainbows dance in the perpetual mist hanging in the air here.

Vergil's (31, 35 Cordillera, a Gravel Parking Lot, Neighborhood: Praxis)
You are standing outside of Vergil's. This area is cluttered with vehicles parked neatly and closely together in a manner that only an expert driver - or more likely, autonomous vehicles - could explain. Part of the area is fenced off for construction of a more space-efficient parking structure. The sky overhead is bright and blue, and the structure of a great dome can be seen above the clouds.
Someone has written the three-pointed star of the Brigades in marker on a rock here.
Sparks of a floating terror: Several bright, scintillating rainbows dance in the perpetual mist hanging in the air here.

Cropland (9, 26 Cordillera, a Cropland, Neighborhood: Great Plains)
You are standing outside of Cropland. This area is dense with crops in a variety of species, planted in clusters which are arranged in rows divided by vehicle paths. A diverse range of pollinator insects can be found here. The sky overhead is bright and blue, and the structure of a great dome can be seen above the clouds.
ᚹᛁᚾᛁᛉ:ᛋᛏᛁᚾ: Several bright, scintillating rainbows dance in the perpetual mist hanging in the air here.

Cropland (8, 26 Cordillera, a Cropland, Neighborhood: Great Plains)
You are standing outside of Cropland. This area is dense with crops in a variety of species, planted in clusters which are arranged in rows divided by vehicle paths. A diverse range of pollinator insects can be found here. A series of large, well-tended white beehives can be found in a clearing. The sky overhead is bright and blue, and the structure of a great dome can be seen above the clouds.
Someone has written GeneralCatton's tanks ran me over in green marker on a rock here.
ᚺᛚᚨᚨᛁᚹᛁᛞᛟ:ᚱᚨᚷᛁᚾᚨ: Several bright, scintillating rainbows dance in the perpetual mist hanging in the air here.
You can feel magic power flowing into this location from two different locations to the East (the Vampire Rose and the ᚹᛁᚾᛁᛉ:ᛋᛏᛁᚾ).

Cropland (8, 27 Cordillera, a Cropland, Neighborhood: Great Plains)
You are standing outside of Cropland. This area is dense with crops in a variety of species, planted in clusters which are arranged in rows divided by vehicle paths. A diverse range of pollinator insects can be found here. The sky overhead is bright and blue, and the structure of a great dome can be seen above the clouds.
Ice Ice BLORTH Font: Several bright, scintillating rainbows dance in the perpetual mist hanging in the air here.

Cropland (7, 27 Cordillera, a Cropland, Neighborhood: Great Plains)
You are standing outside of Cropland. This area is dense with crops in a variety of species, planted in clusters which are arranged in rows divided by vehicle paths. A diverse range of pollinator insects can be found here. The sky overhead is bright and blue, and the structure of a great dome can be seen above the clouds.
Someone has written Oh sure, as soon as there's one that's immediately relevant to YOU, that wouldn't be someone else's problem if it died.. in green chalk on a rock here.
ᚦᚱᚢᛘᛅ:ᛊᛏᚨᛁᚾᚨ: Several bright, scintillating rainbows dance in the perpetual mist hanging in the air here.
You can feel magic power flowing into this location from the South (the Toxicity of BLORTH).

Orchard (7, 28 Cordillera, an Orchard, Neighborhood: Great Plains)
You are standing outside of Orchard. This is a lush orchard filled with a broad diversity of fruit-bearing trees and shrubs, planted in dense clusters that are arranged into rows. The sky overhead is bright and blue, and the structure of a great dome can be seen above the clouds.
Toxicity of BLORTH: Several bright, scintillating rainbows dance in the perpetual mist hanging in the air here.

Orchard (8, 28 Cordillera, an Orchard, Neighborhood: Great Plains)
You are standing outside of Orchard. This is a lush orchard filled with a broad diversity of fruit-bearing trees and shrubs, planted in dense clusters that are arranged into rows. The sky overhead is bright and blue, and the structure of a great dome can be seen above the clouds.
Someone has written Tree in red chalk on a rock here.
Springs of BLORTH: Several bright, scintillating rainbows dance in the perpetual mist hanging in the air here.

The Quickway (51, 21 Cordillera, a Quickway, Neighborhood: The Quickway)
You are standing outside of The Quickway. It is an two-level elevated railway bridge of concrete and steel. Though railway tracks run through the first level of the bridge, the top level is a planted park containing winding pedestrian paths, accessible via the occasional enclosed stairway. The sky overhead is bright and blue, and the structure of a great dome can be seen above the clouds.
Someone has written click, clack, clack; even zombie blood can serve as ink in blood on a rock here.
Ice sculpture of a disturbingly sexy weasel, generously proportioned: Several bright, scintillating rainbows dance in the perpetual mist hanging in the air here.

The Quickway (52, 22 Cordillera, a Quickway, Neighborhood: The Quickway)
You are standing outside of The Quickway. It is an two-level elevated railway bridge of concrete and steel. Railway tracks run through the first level of the bridge, and the lushly planted top level abruptly stops here. The train tracks descend into an underground tunnel and disappear. The sky overhead is bright and blue, and the structure of a great dome can be seen above the clouds.There are 1 items to pickup, 0 of which are targets.
Shrine for a disturbingly sexy weasel: Several bright, scintillating rainbows dance in the perpetual mist hanging in the air here.
''')

convert(cord, 'Cordillera', 'generated/Cordillera.json')
