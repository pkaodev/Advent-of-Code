const utils = require('../../../language-setups/javascript/utils.js')
const {submit} = require('../../../aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input')
const data = readFileSync(inputPath, 'utf8')

parseInput = (data) => {
    const lines = data.split(/\n/)

   const  handBets = lines.map(line=>line.split(' ')).map(handBet=>[handBet[0],Number(handBet[1])])

    return handBets
}

// strong -> weak
const handStrength = ["five", "four", "full", "three", "two", "one", "high"]
const handStrengthObj = handStrength.reduce((obj, strength, index) => {
	obj[strength] = handStrength.length - index;
	return obj;
}, {});

const cardStrength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
const cardStrengthObj = cardStrength.reduce((obj, strength, index) => {
	obj[strength] = cardStrength.length - index;
	return obj;
}, {});

getHandType = (hand) => {
// assumes hand is length 5 and valid

	// count and remove J's from hand
	hand = hand.split('').filter(card=>card!=='J')
	jNum = 5 - hand.length

	const count = {}
	for (const card of hand) {
		count[card] = count[card] ? count[card] + 1 : 1
	}

	const counts = Object.values(count).sort((a,b)=>b-a)
	
	// add J's to highest count
	if (jNum === 5) {
		return 'five'
	}
	counts[0] += jNum

	if (counts[0] === 5) {
		return 'five'
	} else if (counts[0] === 4) {
		return 'four'
	} else if (counts[0] === 3 && counts[1] === 2) {
		return 'full'
	} else if (counts[0] === 3) {
		return 'three'
	} else if (counts[0] === 2 && counts[1] === 2) {
		return 'two'
	} else if (counts[0] === 2) {
		return 'one'
	} else {
		return 'high'
	}
}

const handBets = parseInput(data)

function sortHandBets(a,b) {

	if (handStrengthObj[getHandType(a[0])]<handStrengthObj[getHandType(b[0])]) {
		return -1
	}
	if (handStrengthObj[getHandType(a[0])]>handStrengthObj[getHandType(b[0])]) {
		return 1
	}

	for (let i=0; i<5; i++) {
		if (cardStrengthObj[a[0][i]]<cardStrengthObj[b[0][i]]) {
			return -1
		}
		if (cardStrengthObj[a[0][i]]>cardStrengthObj[b[0][i]]) {
			return 1
		}
	}
}

handBets.sort(sortHandBets)

const SOLUTION_1 = handBets.reduce((sum, handBet, index) => sum + handBet[1]*(index+1), 0)

console.log(`SOLUTION_1: ${SOLUTION_1}`)
// Example solution: 5905

submit(SOLUTION_1)

module.exports = {parseInput, getHandType}