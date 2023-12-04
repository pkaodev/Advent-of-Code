const path = require('path');
const readFileSync = require('fs').readFileSync;
const inputPath = path.join(__dirname, 'input');
const data = readFileSync(inputPath, 'utf8');
const grid = data.split(/\n/);

numbers = '0123456789'
normals = '.0123456789'

numberHash = {

}

width = grid[0].length
height = grid.length

function returnNum(x, y) {
	numStr = ''
	let leftX = x
	let rightX = x + 1
	while (leftX >= 0 && numbers.includes(grid[y][leftX])) {
		numStr = grid[y][leftX] + numStr
		if (leftX - 1 < 0 || !numbers.includes(grid[y][leftX - 1])) {
			break
		}
		leftX--
	}
	while (rightX < width && numbers.includes(grid[y][rightX])) {
		numStr = numStr + grid[y][rightX]
		rightX++
	}
	return [`${leftX},${y}`, parseInt(numStr)]
}

let solution2 = 0

for (let y = 0; y < height; y++) {
	for (let x = 0; x < width; x++) {

		// check if value is a gear
		if (grid[y][x] === '*') {
			gearRatio = 1
			adjNums = 0
			usedCoords = []

			// top left
			if (y - 1 >= 0 && x - 1 >= 0 && numbers.includes(grid[y - 1][x - 1])) {
				[coords, num] = returnNum(x - 1, y - 1)
				if (!usedCoords.includes(coords)) {
					adjNums += 1
					gearRatio *= num
					usedCoords.push(coords)
				}
			}

			// top middle 
			if (y - 1 >= 0 && numbers.includes(grid[y - 1][x])) {
				[coords, num] = returnNum(x, y - 1)
				if (!usedCoords.includes(coords)) {
					adjNums += 1
					gearRatio *= num
					usedCoords.push(coords)
				}
			}

			// top right
			if (y - 1 >= 0 && numbers.includes(grid[y - 1][x + 1])) {
				[coords, num] = returnNum(x + 1, y - 1)
				if (!usedCoords.includes(coords)) {
					adjNums += 1
					gearRatio *= num
					usedCoords.push(coords)
				}
			}


			// middle left
			if (x - 1 >= 0 && numbers.includes(grid[y][x - 1])) {
				[coords, num] = returnNum(x - 1, y)
				if (!usedCoords.includes(coords)) {
					adjNums += 1
					gearRatio *= num
					usedCoords.push(coords)
				}
			}

			// middle right
			if (x + 1 < width && numbers.includes(grid[y][x + 1])) {
				[coords, num] = returnNum(x + 1, y)
				if (!usedCoords.includes(coords)) {
					adjNums += 1
					gearRatio *= num
					usedCoords.push(coords)
				}
			}

			// bottom left
			if (y + 1 < height && x - 1 >= 0 && numbers.includes(grid[y + 1][x - 1])) {
				[coords, num] = returnNum(x - 1, y + 1)
				if (!usedCoords.includes(coords)) {
					adjNums += 1
					gearRatio *= num
					usedCoords.push(coords)
				}
			}

			// bottom middle
			if (y + 1 < height && numbers.includes(grid[y + 1][x])) {
				[coords, num] = returnNum(x, y + 1)
				if (!usedCoords.includes(coords)) {
					adjNums += 1
					gearRatio *=  num
					usedCoords.push(coords)
				}
			}

			// bottom right
			if (y + 1 < height && x + 1 < width && numbers.includes(grid[y + 1][x + 1])) {
				[coords, num] = returnNum(x + 1, y + 1)
				if (!usedCoords.includes(coords)) {
					adjNums += 1
					gearRatio *=  num
					usedCoords.push(coords)
				}
			}
			if (adjNums == 2) {
				solution2 += gearRatio
			}
		}
	}
}

console.log(solution2)