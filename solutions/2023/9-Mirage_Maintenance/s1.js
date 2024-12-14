const utils = require('../../../templates/javascript/utils.js')
const {submit} = require('../../../aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input')
const data = readFileSync(inputPath, 'utf8')
const lines = data.split(/\n/)

const rows = lines.map(line=>line.split(' ').map(Number))

console.log(rows)


function getDiffRow(row) {
	const diffRow = []
	for (let i=0; i<row.length-1; i++) {
		diffRow.push(row[i+1] - row[i])
	}
	return diffRow
}

function predictNextNum(row) {
	let nextRow = row
	let lastNums = [nextRow[nextRow.length-1]]

	while (!nextRow.every(num=>num===0)) {
		nextRow = getDiffRow(nextRow)
		lastNums.unshift(nextRow[nextRow.length-1])
	}
	
	const nextNum = lastNums.reduce((p,c)=>p+c)
	return nextNum
}

function solution1(rows) {
	let solution1 = 0

	rows.forEach(row => {
		solution1 += predictNextNum(row)
	})

	return solution1
}

const SOLUTION_1 = solution1(rows)

module.exports = {}

// submit(SOLUTION_1)

console.log(`SOLUTION_1: ${SOLUTION_1}`)
// Example solution: 114