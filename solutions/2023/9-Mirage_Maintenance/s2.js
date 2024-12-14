const utils = require('../../../templates/javascript/utils.js')
const {submit} = require('../../../aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input')
const data = readFileSync(inputPath, 'utf8')
const lines = data.split(/\n/)

const rows = lines.map(line=>line.split(' ').map(Number))

function getDiffRow(row) {
	const diffRow = []
	for (let i=0; i<row.length-1; i++) {
		diffRow.push(row[i+1] - row[i])
	}
	return diffRow
}

function predictNextNum(row) {
	let nextRow = row
	let firstNums = [nextRow[0]]

	while (!nextRow.every(num=>num===0)) {
		nextRow = getDiffRow(nextRow)
		firstNums.push(nextRow[0])
	}
	
	const nextNum = firstNums.reduce((p,c,i)=>p+(c*((-1)**i)))
	console.log(nextNum)
	return nextNum
}

function solution2(rows) {
	let solution2 = 0

	rows.forEach(row => {
		solution2 += predictNextNum(row)
	})

	return solution2
}

const SOLUTION_2 = solution2(rows)

module.exports = {}

// submit(SOLUTION_2)

console.log(`SOLUTION_2: ${SOLUTION_2}`)
// Example solution: 114