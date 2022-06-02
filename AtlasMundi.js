function getDummyData() {
	return {
		'Cordillera': {
			'Fonts': [{
                'name': 'Vesper Arch', 'aspect': 'Holy', 'location': [39, 16],
                'desc': 'A great arch of white ivory rises from the ground here, though a constant clicking and whirring seems to emanate from it. A melodious chorus of chiming augments the periodic peal of ethereal bells that are heard but not seen emanates from the arch.'
            }],
            'Ley Lines': [{
                'source': 'Vesper Arch', 'start': [39, 16], 'end': [36, 19]
            }],
            'Strongholds': [{
                'faction': 'Dummy Faction', 'location': [11, 24]
            }],
		}
	};
}

function mergeDict(dest, source) {
    if (typeof(dest) != 'object') return;
    if (typeof(source) != 'object') return;
    if (Array.isArray(source)) {
        source.forEach(e => dest.push(e));
        return;
    }
    for (const key of Object.keys(source)) {
        if (dest[key]) mergeDict(dest[key], source[key]);
        else dest[key] = source[key];
    }
}

async function getJsonData(...filenames) {    
    const data = {};
    
	for (const filename of filenames) {
        const json = await fetch('https://argavyon.github.io/CRT-Atlas-Mundi/' + filename).then(resp => resp.json());
        mergeDict(data, json);
	}
	
	return data;
}

function emptyInfo() {
    return {Font: null, LLs: {}, SH: null};
}

const tileX = (x, x_offset) => (x - x_offset) * 48;
const tileY = (y, y_offset) => (y - y_offset) * 48;

const imgFont = new Image();
imgFont.src = 'https://www.nexusclash.com/images/g/status/circle-sparks.png';
async function processFonts(fonts, info, canvasCtx, x_offset, y_offset) {
	for (const font of fonts) {
		const [x,y] = font.location;
		if (!info[`${x}_${y}`]) info[`${x}_${y}`] =  emptyInfo();
		info[`${x}_${y}`].Font = font;
		await imgFont.decode();
        canvasCtx.fillStyle = "#00000060";
        canvasCtx.fillRect(tileX(x, x_offset), tileY(y, y_offset), 46, 46);
		canvasCtx.drawImage(imgFont, tileX(x, x_offset), tileY(y, y_offset), 46, 46);
	}
}

const imgLLdict = {};
const dirDict = {
	'0_-1': 'n',
	'-1_-1': 'nw',
	'1_-1': 'ne',
	'0_1': 's',
	'-1_1': 'sw',
	'1_1': 'se',
	'-1_0': 'w',
	'1_0': 'e',
}
async function processLLs(LLs, info, canvasCtx, x_offset, y_offset) {
	async function imgLL(from, to) {
		const from_to = `${from}_${to}`;
		if (imgLLdict[from_to]) return imgLLdict[`${from}_${to}`];
		imgLLdict[from_to] = new Image();
		imgLLdict[from_to].src = `https://www.nexusclash.com/images/g/inf/ley_${from}_${to}.gif`;
		await imgLLdict[from_to].decode();
		return imgLLdict[from_to];
	}
	
	for (const LL of LLs) {
		const [sx, sy] = LL.start;
		const [ex, ey] = LL.end;
		const [lx, ly] = [Math.abs(ex-sx), Math.abs(ey-sy)];
        const length = Math.max(lx, ly);
		if (lx !== ly && lx !== 0 && ly !== 0) {
			console.log(`Impossible Path: ${LL.source}`);
			continue;
		}
        if (lx === 0 && ly === 0) {
			console.log(`Length Zero Leyline: ${LL.source}`);
			continue;
		}
        const dx = lx === 0 ? 0 : (ex-sx)/lx;
        const dy = ly === 0 ? 0 : (ey-sy)/ly;
		const dirFrom = dirDict[`${-dx}_${-dy}`];
		const dirTo = dirDict[`${dx}_${dy}`];
		LL.direction = dirTo.toUpperCase();
		
		if (!info[`${sx}_${sy}`]) info[`${sx}_${sy}`] = emptyInfo();
		info[`${sx}_${sy}`].LLs[LL.source] = LL;
		canvasCtx.drawImage(await imgLL('c', dirTo), tileX(sx, x_offset), tileY(sy, y_offset), 46, 46);
		
		let [curx, cury] = [sx+dx, sy+dy];
		while (curx !== ex || cury !== ey) {
			if (!info[`${curx}_${cury}`]) info[`${curx}_${cury}`] = emptyInfo();
			info[`${curx}_${cury}`].LLs[LL.source] = LL;
			canvasCtx.drawImage(await imgLL(dirFrom, 'c'), tileX(curx, x_offset), tileY(cury, y_offset), 46, 46);
			canvasCtx.drawImage(await imgLL('c', dirTo), tileX(curx, x_offset), tileY(cury, y_offset), 46, 46);
			[curx, cury] = [curx+dx, cury+dy];
		}
		
		if (!info[`${ex}_${ey}`]) info[`${ex}_${ey}`] = emptyInfo();
        if (!info[`${ex}_${ey}`].LLs[LL.source]) info[`${ex}_${ey}`].LLs[LL.source] = LL;
		canvasCtx.drawImage(await imgLL(dirFrom, 'c'), tileX(ex, x_offset), tileY(ey, y_offset), 46, 46);
	}
}

const imgSH = new Image();
imgSH.src = 'https://www.nexusclash.com/images/g/status/Stronghold.png';
async function processSHs(SHs, info, canvasCtx, x_offset, y_offset) {
	for (const SH of SHs) {
		const [x,y] = SH.location;
		if (!info[`${x}_${y}`]) info[`${x}_${y}`] =  emptyInfo();
		info[`${x}_${y}`].SH = SH;
		await imgSH.decode();
		canvasCtx.drawImage(imgSH, tileX(x, x_offset)+20, tileY(y, y_offset), 26, 26);
	}
}

function tooltipSH(SH) {
	const T = document.createElement('tbody');
	const headRow = T.appendChild(document.createElement('tr')).appendChild(document.createElement('td'));
	headRow.appendChild(document.createElement('b')).textContent = `Stronghold: `;
	headRow.appendChild(document.createTextNode(SH.faction));
	return T;
}

function tooltipFont(font) {
	const T = document.createElement('tbody');
	const headRow = T.appendChild(document.createElement('tr')).appendChild(document.createElement('td'));
	headRow.appendChild(document.createElement('b')).textContent = `${font.aspect} Font: `;
	headRow.appendChild(document.createTextNode(font.name));
	if (font.desc) T.appendChild(document.createElement('tr')).appendChild(document.createElement('td')).textContent = font.desc;
	return T;
}

function tooltipLL(LL) {
	const T = document.createElement('tbody');
	T.appendChild(document.createElement('tr')).appendChild(document.createElement('th')).textContent = 'Ley Line';
	T.appendChild(document.createElement('tr')).appendChild(document.createElement('td')).textContent = `Source: ${LL.source}`;
	if (LL.direction) T.appendChild(document.createElement('tr')).appendChild(document.createElement('td')).textContent = `Direction: ${LL.direction}`;
	return T;
}

function tooltipContent(tileInfo, planeName, x, y) {
	const content = [];
	
	const location = document.createElement('tbody');
	location.appendChild(document.createElement('tr')).appendChild(document.createElement('th')).textContent = `${planeName} (${x}, ${y})`;
	content.push(location);
	
    if (tileInfo.SH) content.push(tooltipSH(tileInfo.SH));
    if (tileInfo.Font) content.push(tooltipFont(tileInfo.Font));
	for (const LL of Object.values(tileInfo.LLs)) content.push(tooltipLL(LL));
	
	return content;
}

async function interactiveMap(curPlaneID, data) {
	const tooltip = document.querySelector('#tooltip');
	tooltip.style.display = 'none';
	tooltip.firstChild.innerHTML = '';
	
	const planes = {
		'416': {'abbrev': 'CEN', 'name': 'Centrum',      'id':416, 'x':743,  'x_offset':26, 'y':743,  'y_offset':16},
		'406': {'abbrev': 'CRD', 'name': 'Cordillera',   'id':406, 'x':1751, 'x_offset':0,  'y':1319, 'y_offset':0},
		'405': {'abbrev': 'PGU', 'name': 'PurgatorioUG', 'id':405, 'x':767,  'x_offset':0,  'y':767,  'y_offset':0},
		'404': {'abbrev': 'PGT', 'name': 'Purgatorio',   'id':404, 'x':767,  'x_offset':0,  'y':767,  'y_offset':0},
		'403': {'abbrev': 'STY', 'name': 'Stygia',       'id':403, 'x':527,  'x_offset':0,  'y':527,  'y_offset':0},
		'402': {'abbrev': 'ELY', 'name': 'Elysium',      'id':402, 'x':527,  'x_offset':0,  'y':527,  'y_offset':0}
	};
	let curPlane = planes[curPlaneID];
	
	const canvas = document.getElementById('map');
	canvas.width = curPlane.x*2;
	canvas.height = curPlane.y*2;
    canvas.style.width = curPlane.x + 'px';
	canvas.style.height = curPlane.y + 'px';
	//canvas.style.backgroundImage = `url(planes/${curPlane.name}.png)`;
    const planeImage = new Image();
    planeImage.src = `planes/${curPlane.name}_template.png`;
    await planeImage.decode();
    canvas.getContext('2d').drawImage(planeImage, 0, 0, curPlane.x*2, curPlane.y*2);
	
    const planeData = data[curPlane.name];
	// console.log(JSON.stringify(data, null, 2));
	
	const canvasCtx = canvas.getContext('2d');
	const info = {};
	if (planeData) {
		if (planeData['Fonts']) await processFonts(planeData['Fonts'], info, canvasCtx, curPlane.x_offset, curPlane.y_offset);
		if (planeData['Ley Lines']) await processLLs(planeData['Ley Lines'], info, canvasCtx, curPlane.x_offset, curPlane.y_offset);
		if (planeData['Strongholds']) await processSHs(planeData['Strongholds'], info, canvasCtx, curPlane.x_offset, curPlane.y_offset);
	}
	
	canvas.addEventListener('mousemove', e => {
		const x = Math.floor((e.offsetX) / 24) + curPlane.x_offset;
		const y = Math.floor((e.offsetY) / 24) + curPlane.y_offset;
		tileInfo = info[`${x}_${y}`];
		if (tileInfo) {
			tooltip.style.left = `${Math.floor(e.pageX) + 12}px`;
			tooltip.style.top = `${Math.floor(e.pageY - 12) - 12}px`;
			tooltip.firstChild.innerHTML = '';
			tooltip.firstChild.append(...tooltipContent(tileInfo, curPlane.name, x, y));
			tooltip.style.display = 'block';
		} else {
			tooltip.style.display = 'none';
			tooltip.firstChild.innerHTML = '';
		}
	});
}

async function main() {
    const data = await getJsonData(
        'data/ley/natural/Cordillera.json',
        'data/ley/natural/Purgatorio.json',
        'data/ley/natural/Stygia.json',
        'data/ley/natural/Elysium.json',
        'data/ley/playermade/Cordillera.json',
        'data/ley/playermade/Centrum.json',
        'data/ley/playermade/Purgatorio.json',
        'data/ley/playermade/Stygia.json',
        'data/ley/playermade/Elysium.json',
        'data/strongholds.json',
    );
    
    for (const plane of Object.keys(data)) {
        for (const category of Object.keys(data[plane])) {
            data[plane][category].sort((a,b) => (a.location > b.location) - (a.location < b.location));
        }
    }
    console.log(data);
	interactiveMap(406, data);
	document.querySelectorAll('li.nav-item button').forEach(btn => {
		btn.onclick = function() { interactiveMap(btn.value, data); }
	});
}
main();
