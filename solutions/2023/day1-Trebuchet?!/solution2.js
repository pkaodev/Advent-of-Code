const { start } = require('repl');

const readFileSync = require('fs').readFileSync;
const data = readFileSync('./input1', 'utf8')
const lines = data.split(/\n/);

const stringNums = {
	one: 1,
	two: 2,
	three: 3,
	four: 4,
	five: 5,
	six: 6,
	seven: 7,
	eight: 8,
	nine: 9
}

function getStringNum(line, startIndex) {
	
	// regex: 3-5 chars
	if (stringNums[line[startIndex]+line[startIndex+1]+line[startIndex+2]]) {
		return stringNums[line[startIndex]+line[startIndex+1]+line[startIndex+2]]
	} else if (stringNums[line[startIndex]+line[startIndex+1]+line[startIndex+2]+line[startIndex+3]]) {
		return stringNums[line[startIndex]+line[startIndex+1]+line[startIndex+2]+line[startIndex+3]]
	} else if (stringNums[line[startIndex]+line[startIndex+1]+line[startIndex+2]+line[startIndex+3]+line[startIndex+4]]) {
		return stringNums[line[startIndex]+line[startIndex+1]+line[startIndex+2]+line[startIndex+3]+line[startIndex+4]]
	}
}

const solution2 = lines.reduce((prev, curr) => {

	lineNum = 0

	// lp=0, while, l#=parseInt || false
	for (let i = 0;; i++) {
		if (parseInt(curr[i])) {
			stringyNum = parseInt(curr[i]).toString()
			console.log(stringyNum)
			break
		} else if (getStringNum(curr, i)) {
			stringyNum = getStringNum(curr, i).toString()
			console.log(stringyNum)
			break
		}
	}

	
	for (let i = curr.length-1;; i--) {
				if (parseInt(curr[i])) {
			stringyNum += parseInt(curr[i]).toString()
			console.log(stringyNum)
			break
		} else if (getStringNum(curr, i)) {
			stringyNum += getStringNum(curr, i).toString()
			console.log(stringyNum)
			break
		}
	}

	return prev + parseInt(stringyNum)

},0)

console.log(solution2)