const path = require('path');
const readFileSync = require('fs').readFileSync;

const inputPath = path.join(__dirname, 'input');
const data = readFileSync(inputPath, 'utf8');
const lines = data.split(/\n/);

const totalCards = lines.length
console.log(totalCards)
const cardInstances = {}

function updateCardInstances(line) {
	let [cardNum, numLists] = line.split(': ')
	cardNum = parseInt(cardNum.split(/\s+/)[1])
	const [winNumsList, haveNumsList] = numLists.split('|')
	const winHash = Object.fromEntries(winNumsList.trim().split(/\s+/).map(key => [key, true]))
	const haveArr = haveNumsList.trim().replace(/[ ]+/g, ' ').split(' ')
	console.log(cardNum)

	cardInstances[cardNum] = cardInstances[cardNum] ? cardInstances[cardNum] + 1 : 1

	let cardWins = 0

	for (haveNum of haveArr) {
		if (winHash[haveNum]) {
			cardWins++
		}
	}
	console.log('wins', cardWins)

	let nextCardNum = cardNum + 1
	let numOfThisCard = cardInstances[cardNum]

	while (cardWins) {
		if (nextCardNum > totalCards) {
			break
		}
		cardInstances[nextCardNum] = cardInstances[nextCardNum] ? cardInstances[nextCardNum] + numOfThisCard : numOfThisCard

		nextCardNum++
		cardWins--
	}
}

for (line of lines) {
	updateCardInstances(line)
}

SOLUTION_2 = 0
console.log(cardInstances)
for (numOfCards of Object.values(cardInstances)) {
	SOLUTION_2 += numOfCards
}

console.log(SOLUTION_2)