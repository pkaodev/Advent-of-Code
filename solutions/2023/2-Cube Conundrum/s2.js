const readFileSync = require('fs').readFileSync;
const data = readFileSync('./i1', 'utf8')
const lines = data.split(/\n/);


solution2 = lines.reduce((acc, curr) => {

	minCubes = {
		'red': 0,
		'green': 0,
		'blue': 0,
	}

	drawTexts = curr.split(': ')[1].split(/[,;] /)

	for (drawText of drawTexts) {
		[numStr, colorStr ] = drawText.split(' ')
		num = parseInt(numStr)
		if (num > minCubes[colorStr]) {
			minCubes[colorStr] = parseInt(numStr)
		}
	}

	return acc + (minCubes['red'] * minCubes['green'] * minCubes['blue'])

}, 0)

console.log(solution2)