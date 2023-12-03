const readFileSync = require('fs').readFileSync;
const data = readFileSync('./i1', 'utf8')
const grid = data.split(/\n/);

numbers = '0123456789'
normals = '.0123456789'

numberHash = {

}

width = grid[0].length
height = grid.length

function returnNum(x,y) {

	numStr = ''

	let leftX = x
	let rightX = x+1

	while (leftX >= 0 && numbers.includes(grid[y][leftX])) {
		numStr = grid[y][leftX] + numStr
		if (leftX-1<0 || !numbers.includes(grid[y][leftX-1])) {
			break
		}
		leftX--
	}

	while (rightX<width && numbers.includes(grid[y][rightX])) {
		numStr = numStr + grid[y][rightX]
		rightX++
	}
	console.log(numStr)
	return parseInt(numStr)
}

let solution2 = 0

for (let y=0; y<height; y++) {
	for (let x=0; x<width; x++) {
		gearRatio = 1
		topLeft = false
		bottomLeft = false

		// check if value is a gear
		if (grid[y][x] === '*') {
			// check if it has two numbers next to it
			adjNums = 0
			// top left
			if (y-1>=0 && x-1>=0 && numbers.includes(grid[y-1][x-1])) {
				adjNums += 1
				gearRatio *= returnNum(x-1, y-1)
				topLeft = true
			}

			if (topLeft) {
				// top middle not num and top right is
				if ((y-1>=0 && !numbers.includes(grid[y-1][x])) && y-1>=0 && x+1<width && numbers.includes(grid[y-1][x+1])) {
					adjNums += 1
					gearRatio *= returnNum(x+1, y-1)
				}

			} else {
				// top middle num
				if (y-1>=0 && numbers.includes(grid[y-1][x])) {
					adjNums+= 1
					gearRatio *= returnNum(x, y-1)
				}
			}

			// middle left
			if (x-1>=0 && numbers.includes(grid[y][x-1])) {
				adjNums += 1
				gearRatio *= returnNum(x-1, y)
			}

			if (adjNums > 2) {
				break
			}

			// middle right
			if (x+1<width && numbers.includes(grid[y][x+1])) {
				adjNums += 1
				gearRatio *= returnNum(x+1, y)
			}

			if (adjNums >2) {
				break
			}

			// bottom right
			if (y+1<height && x-1>=0 && numbers.includes(grid[y+1][x-1])) {
				adjNums += 1
				gearRatio *= returnNum(x-1, y+1)
				bottomLeft = true
			}


			if (bottomLeft) {
				// bottom middle not num and bottom right is
				if (y+1<height && !numbers.includes(grid[y+1][x]) && y+1<height && x+1<width && numbers.includes(grid[y+1][x+1])) {
					adjNums += 1
					gearRatio *= returnNum(x+1, y+1)
				}

			} else {
				// bottom middle num
				if (y+1<height && numbers.includes(grid[y+1][x])) {
					adjNums+= 1
					gearRatio *= returnNum(x, y+1)
				}
			}

			if (adjNums = 2) {
				solution2 += gearRatio
			}
		}
	}
}

console.log(solution2)