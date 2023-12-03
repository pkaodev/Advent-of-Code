const readFileSync = require('fs').readFileSync;
const data = readFileSync('./i1', 'utf8')
const grid = data.split(/\n/);

numbers = '0123456789'
normals = '.0123456789'

numberHash = {

}

width = grid[0].length
height = grid.length

function setNumberCoordsValue(x,y) {

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
		// if (rightX+1>=width || !numbers.includes(grid[y][rightX+1])) {
		// 	break
		// }
		rightX++
	}

	// console.log(numStr)
	console.log(`${leftX},${y}`)
	console.log(numStr)
	// if (parseInt(numStr)) {
		numberHash[`${leftX},${y}`] = parseInt(numStr)
	// }


}



for (let y=0; y<height; y++) {
	for (let x=0; x<width; x++) {

		// check if value is special
		if (!normals.includes(grid[y][x])) {
			// check each 8 surrounding values for being numbers
			if (y-1>=0 && x-1>=0 && numbers.includes(grid[y-1][x-1])) {
				setNumberCoordsValue(x-1, y-1)
			}
			if (y-1>=0 && numbers.includes(grid[y-1][x])) {
				setNumberCoordsValue(x, y-1)
			}
			if (y-1>=0 && x+1<width && numbers.includes(grid[y-1][x+1])) {
				setNumberCoordsValue(x+1, y-1)
			}
			if (x-1>=0 && numbers.includes(grid[y][x-1])) {
				setNumberCoordsValue(x-1, y)
			}
			if (x+1<width && numbers.includes(grid[y][x+1])) {
				setNumberCoordsValue(x+1, y)
			}
			if (y+1<height && x-1>=0 && numbers.includes(grid[y+1][x-1])) {
				setNumberCoordsValue(x-1, y+1)
			}
			if (y+1<height && numbers.includes(grid[y+1][x])) {
				setNumberCoordsValue(x, y+1)
			}
			if (y+1<height && x+1<width && numbers.includes(grid[y+1][x+1])) {
				setNumberCoordsValue(x+1, y+1)
			}
		}
	}
}

solution1 = Object.values(numberHash).reduce((acc, curr) => {
	// console.log(curr)
	return acc+curr
}, 0)

console.log(numberHash)
console.log(solution1)