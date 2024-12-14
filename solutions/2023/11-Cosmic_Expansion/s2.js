const utils = require('../../../templates/javascript/utils.js')
const { submit } = require('../../../lib/aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input')
const data = readFileSync(inputPath, 'utf8')

function parseInput(data) {
    return data.split(/\n/)
}
function isRowEmpty(row) {
    return row.split('').every(x => x === '.')
}
function isColumnEmpty(column) {
    return column.every(x => x === '.')
}
function expandUniverse(grid) {
    const emptyRows = []
    for (let i = 0; i < grid.length; i++) {
        if (isRowEmpty(grid[i])) {
            emptyRows.push(i)
        }
    }

    const emptyColumns = []
    for (let i = 0; i < grid[0].length; i++) {
        const column = []
        for (let y = 0; y < grid.length; y++) {
            column.push(grid[y][i])
        }
        if (isColumnEmpty(column)) {
            emptyColumns.push(i)
        }
    }

    return {
        emptyRows,
        emptyColumns
    }
}
function findGalaxies(grid) {
    const galaxyLocations = []
    for (let y = 0; y < grid.length; y++) {
        for (let x = 0; x < grid[0].length; x++) {
            if (grid[y][x] === '#') {
                galaxyLocations.push({ x, y })
            }
        }
    }
    return galaxyLocations
}
function findShortestPaths(galaxyLocations, emptyRowsColumns) {
    const expFact = 999999
    const shortestPaths = []
    for (let g1 = 0; g1 < galaxyLocations.length - 1; g1++) {
        for (let g2 = g1 + 1; g2 < galaxyLocations.length; g2++) {
            const maxX = Math.max(galaxyLocations[g1].x, galaxyLocations[g2].x)
            const minX = Math.min(galaxyLocations[g1].x, galaxyLocations[g2].x)
            const maxY = Math.max(galaxyLocations[g1].y, galaxyLocations[g2].y)
            const minY = Math.min(galaxyLocations[g1].y, galaxyLocations[g2].y)
            const expX = emptyRowsColumns.emptyColumns.filter(q => q > minX && q < maxX).length
            const expY = emptyRowsColumns.emptyRows.filter(q => q > minY && q < maxY).length
            shortestPaths.push(Math.abs(galaxyLocations[g2].x - galaxyLocations[g1].x) + Math.abs(galaxyLocations[g2].y - galaxyLocations[g1].y) + ((expY + expX) * expFact))
        }
    }
    return shortestPaths
}

const grid = parseInput(data)

const emptyRowsColumns = expandUniverse(grid)
const galaxyLocations = findGalaxies(grid)
console.log(emptyRowsColumns)
console.log(galaxyLocations)

const shortestPaths = findShortestPaths(galaxyLocations, emptyRowsColumns)


const SOLUTION_1 = shortestPaths.reduce((a, c) => a + c)

module.exports = {}

// submit(SOLUTION_1)

console.log(`SOLUTION_1: ${SOLUTION_1}`)
// Example solution: 374