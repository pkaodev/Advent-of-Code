const utils = require('../../../templates/javascript/utils.js')
const { submit } = require('../../../lib/aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input')
const data = readFileSync(inputPath, 'utf8')
const lines = data.split(/\n/)

const dirs = {
	up: { x: 0, y: -1 },
	right: { x: 1, y: 0 },
	down: { x: 0, y: 1 },
	left: { x: -1, y: 0 }
};

const dirsOpp = {
	'{"x":0,"y":-1}': dirs.down,
	'{"x":1,"y":0}': dirs.left,
	'{"x":0,"y":1}': dirs.up,
	'{"x":-1,"y":0}': dirs.right
};

function getOppositeDirection(direction) {
	const dirString = JSON.stringify(direction);
	return dirsOpp[dirString];
}

const pipes = {
	"|": [dirs.up, dirs.down],
	"-": [dirs.left, dirs.right],
	"L": [dirs.up, dirs.right],
	"J": [dirs.up, dirs.left],
	"7": [dirs.left, dirs.down],
	"F": [dirs.right, dirs.down]
}

function isValidConnection(prevPipeDir, newPipeSymbol) {
	if (newPipeSymbol === '.') {
		return false
	}
	return pipes[newPipeSymbol].includes(getOppositeDirection(prevPipeDir))
}
function nextPipeDir(prevPipeDir, newPipeSymbol) {
	return pipes[newPipeSymbol].filter(dir => dir !== getOppositeDirection(prevPipeDir))[0]
}

function getNextIndex(x, y, dir) {
	const newX = x + dir.x
	const newY = y + dir.y

	if (newX >= minX && newX <= maxX && newY >= minY && newY <= maxY) {
		return { x: newX, y: newY }
	}
	return false
}

function findStartIndex(lines) {
	for (let y = 0; y < lines.length; y++) {
		for (let x = 0; x < lines[0].length; x++) {
			if (lines[y][x] === 'S') {
				return { x, y }
			}
		}
	}
}

const minX = 0
const minY = 0
const maxX = lines[0].length - 1
const maxY = lines.length - 1

function solution1(lines) {
	const startIndex = findStartIndex(lines)
	let currIndex = startIndex

	for (const assumedPipe of Object.keys(pipes)) {
		let prevPipeDir = pipes[assumedPipe][0]
		let steps = 0

		do {

			const nextIndex = getNextIndex(currIndex.x, currIndex.y, prevPipeDir)

			if (!nextIndex) {
				break
			}

			nextPipeSymbol = lines[nextIndex.y][nextIndex.x]
			if (nextPipeSymbol === 'S') {
				return Math.ceil(steps / 2)
			}

			if (!isValidConnection(prevPipeDir, nextPipeSymbol)) {
				break
			}


			newPipeDir = nextPipeDir(prevPipeDir, nextPipeSymbol)

			currIndex = nextIndex
			prevPipeDir = newPipeDir
			steps++


		} while (currIndex != startIndex)

	}

}




const SOLUTION_1 = solution1(lines)

module.exports = {}

// submit(SOLUTION_1)

console.log(`SOLUTION_1: ${SOLUTION_1}`)
// Example solution: 8