const readFileSync = require('fs').readFileSync
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/)


let timesToRun = 20;
const timeResults = [];

while (timesToRun--) {
    const time0 = Date.now()

    const createMapFromInstructions = (instructions) => {
        return JSON.stringify(
           instructions.map((line, yindex) => {
            return line.split('').map((char, xindex) => {
                return {
                    height: char === 'S' ? 1 : char === 'E' ? 26 : char.charCodeAt(0) - 96,
                    visited: false,
                    pathValue: char === 'S' ? 0 : 1000,
                    x: xindex,
                    y: yindex
                }
            })
        })
        )
    }

    let theMapString = createMapFromInstructions(instructions);
    let theMap = JSON.parse(theMapString);

//[y,x] coordinates
let currentNode = [0,0]

//[y,x] coordinates
const endNode = [0, 0]

firstLoop:
for (let i = 0; i < yMax; i++) {
    for (let j = 0; j < xMax; j++) {
        if (instructions[i][j] === 'E') {
            endNode[0] = i;
            endNode[1] = j;
            break firstLoop;
        }
    }
}


const getLowestPathValue = (map) => {
    let lowestPathValue = Number.POSITIVE_INFINITY
    let lowestPathValueNode = null
    map.forEach(row => {
        row.forEach(node => {
            if (node.pathValue < lowestPathValue && !node.visited) {
                lowestPathValue = node.pathValue
                lowestPathValueNode = node
            }
        })
    })
    return lowestPathValueNode
}

const getAdjacentNodes = (node, map) => {
    const adjacentNodes = [
        [node.y - 1, node.x],
        [node.y + 1, node.x],
        [node.y, node.x - 1],
        [node.y, node.x + 1]
    ].filter(([y, x]) => {
        return y >= 0 && y < map.length && x >= 0 && x < map[y].length
    }).map(([y, x]) => {
        return map[y][x]
    }).filter(node => {
        return !node.visited
    })
    return adjacentNodes
}
const updatePathValues = (nodes, currentNode) => {
    nodes.forEach(node => {
        if (node.pathValue > currentNode.pathValue + 1 && node.height <= currentNode.height + 1) {
            node.pathValue = currentNode.pathValue + 1
        }
    })
}


while (!theMap[endNode[0]][endNode[1]].visited) {
    const currentNode = getLowestPathValue(theMap)
    currentNode.visited = true
    const adjacentNodes = getAdjacentNodes(currentNode, theMap)
    updatePathValues(adjacentNodes, currentNode)
}

timeResults.push(Date.now() - time0)
}
// console.log(theMap[endNode[0]][endNode[1]].pathValue)
console.log(timeResults)
console.log(timeResults.reduce((acc, time) => acc + time, 0) / timeResults.length)
