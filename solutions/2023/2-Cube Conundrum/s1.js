const readFileSync = require('fs').readFileSync;
const data = readFileSync('./i1', 'utf8')
const lines = data.split(/\n/);

maxCubes = {
	'red': 12,
	'green': 13,
	'blue': 14,
}

solution1 = lines.reduce((acc, curr) => {

	[gameName, info] = curr.split(': ')

	// int of game (could also use index+1 of input)
	gameNum = parseInt(gameName.split(' ')[1])

	// ['2 green', '12 red'...]
	drawTexts = info.split(/[,;] /)

	for (draw of drawTexts) {
		[numStr, colorStr ] = draw.split(' ')

		if (parseInt(numStr) > maxCubes[colorStr]) {
			return acc
		}
	}

	return acc + gameNum

}, 0)

console.log(solution1)