const utils = require('../../../language-setups/javascript/utils.js')
const {submit} = require('../../../aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input')
const data = readFileSync(inputPath, 'utf8')

function parseInput(data) {
    const lines = data.split(/\n/)

	const instructions = lines[0]

    let nodePaths = lines.slice(2).map(line=> {
		const [node, adjNodesLong] = line.split(' = ')
		const adjNodes = adjNodesLong.split(', ').map(x=>x.replace(/[^a-zA-Z]/g, ''))
		return [node, adjNodes]
	})

	return [instructions, nodePaths]
}


function createNodePathsHash(nodePaths) {
	const nodePathsHash = {}
	for (const nodePath of nodePaths) {
		nodePathsHash[nodePath[0]] = {
			L: nodePath[1][0],
			R: nodePath[1][1]
		}
	}
	return nodePathsHash
}

const [instructions, nodePaths] = parseInput(data)
const nodePathsHash = createNodePathsHash(nodePaths)

// console.log(nodePathsHash)

let steps = 0
let currInstructionIndex = 0
let currNode = data.split(/\n/)[2].split(' = ')[0]
// const endNode = data.split(/\n/)[data.split(/\n/).length-1].split(' = ')[0]

console.log(instructions)
console.log(currNode)
// console.log(endNode)


while (true) {

	steps++

	currNode = nodePathsHash[currNode][instructions[currInstructionIndex]]

	currInstructionIndex++
	if (currInstructionIndex === instructions.length) {
		currInstructionIndex = 0
	}

	if (currNode === 'ZZZ') {
	// if (currNode === 'Z' && currInstructionIndex === 0) {
		break
	}
}

const SOLUTION_1 = steps

module.exports = {}

// submit(SOLUTION_1)

console.log(`SOLUTION_1: ${SOLUTION_1}`)
// Example solution: 6