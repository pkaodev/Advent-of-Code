const readFileSync = require('fs').readFileSync;
const data = readFileSync('./input1', 'utf8')
const lines = data.split(/\n/);
const solution1 = lines.reduce((prev, curr) => {

	let stringyNum

	for (let i = 0;; i++) {
		if (parseInt(curr[i])) {
			stringyNum = parseInt(curr[i]).toString()
			break
		}
	}

	for (let i = curr.length-1;; i--) {
				if (parseInt(curr[i])) {
			stringyNum += parseInt(curr[i]).toString()
			console.log(stringyNum)
			break
		}
	}

	return prev + parseInt(stringyNum)
}, 0)

console.log(solution1)