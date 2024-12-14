const _ = require('../../../templates/javascript/utils.js')
const path = require('path');
const readFileSync = require('fs').readFileSync;

const inputPath = path.join(__dirname, 'input');
const data = readFileSync(inputPath, 'utf8');
const lines = data.split(/\n/);

function getLineValue(line) {
	const [_, numLists] = line.split(': ')
	const [winNumsList, haveNumsList] = numLists.split('|')
	const winHash = Object.fromEntries(winNumsList.trim().split(/\s+/).map(key => [key, true]))
	const haveArr = haveNumsList.trim().replace(/[ ]+/g, ' ').split(' ')

	let lineValue = 0

	for (haveNum of haveArr) {
		if (winHash[haveNum]) {
			if (lineValue === 0) {
				lineValue = 1
			} else {
				lineValue *= 2
			}
		}
	}
	return lineValue
}

const SOLUTION_1 = lines.reduce((acc, curr) => {
	return acc + getLineValue(curr)
}, 0)

console.log(SOLUTION_1)