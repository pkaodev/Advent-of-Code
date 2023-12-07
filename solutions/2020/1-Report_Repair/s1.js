const utils = require('../../../language-setups/javascript/utils.js')
const {submit} = require('../../../aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input')
const data = readFileSync(inputPath, 'utf8')

function parseInput(data) {
    const lines = data.split(/\n/).map(Number)

    return lines
}

lines = parseInput(data)

function solution1(lines) {
for (let i = 0; i < lines.length; i++) {
	for (let j = i + 1; j < lines.length; j++) {
		if (lines[i] + lines[j] === 2020) {
			return lines[i] * lines[j]
		}
	}
}
}










const SOLUTION_1 = solution1(lines)

module.exports = {}

submit(SOLUTION_1)

console.log(`SOLUTION_1: ${SOLUTION_1}`)
// Example solution: 514579