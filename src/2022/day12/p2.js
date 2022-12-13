const time0 = Date.now()

const readFileSync = require('fs').readFileSync
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/)

instructions[0] = 'a' + instructions[0].slice(1)

const yMax = instructions.length
const xMax = instructions[0].length

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

const createMapFromInstructions = (instructions) => {
    return JSON.stringify(
       instructions.map((line, yindex) => {
        return line.split('').map((char, xindex) => {
            return {
                height: char === 'E' ? 26 : char.charCodeAt(0) - 96,
                visited: false,
                pathValue: 1000,
                x: xindex,
                y: yindex
            }
        })
    })
    )
}

let theMapString = createMapFromInstructions(instructions);
let theMap = JSON.parse(theMapString);

const getLowestPathValue = (map) => {
    let lowestPathValue = 1000
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
        //in bounds check
    ].filter(([y, x]) => {
        return y >= 0 && y < map.length && x >= 0 && x < map[y].length
        //return array of nodes
    }).map(([y, x]) => {
        return map[y][x]
        //check they haven't been visited
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

const quickestRoutes = [];

//[y,x] coordinates
let currentNode = [0, 0]


for (let i = 0; i < instructions.length; i++) {
    for (let j = 0; j < instructions[i].length; j++) {

        if (instructions[i][j] === 'a') {
            currentNode = [i, j];

            //create fresh map
            theMap = JSON.parse(theMapString);

            theMap[currentNode[0]][currentNode[1]].pathValue = 0;

            let finished = false;
            while (!finished) {
                const currentNode = getLowestPathValue(theMap)
                currentNode.visited = true
                const adjacentNodes = getAdjacentNodes(currentNode, theMap)
                updatePathValues(adjacentNodes, currentNode)
                if (currentNode.x === endNode[1] && currentNode.y === endNode[0]) {
                    finished = true
                }

            }

            quickestRoutes.push(theMap[endNode[0]][endNode[1]].pathValue)
        }
    }
}

console.log(quickestRoutes.sort((a, b) => a - b)[0])

console.log('time:', Date.now() - time0)