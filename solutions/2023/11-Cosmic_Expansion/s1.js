const utils = require('../../../templates/javascript/utils.js')
const {submit} = require('../../../aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input_example')
const data = readFileSync(inputPath, 'utf8')

function parseInput(data) {
    return data.split(/\n/)
}
function isRowEmpty(row) {
 return row.split('').every(x=>x==='.')
}
function isColumnEmpty(column) {
    return column.every(x=>x==='.')
}
function expandRow(grid, rowI) {
    grid.splice(rowI, 0, '.'.repeat(grid[0].length))

}
function expandColumn(grid, columnI) {
    for (const rowI in grid) {
        const newRow = grid[rowI].slice(0,columnI) + '.' + grid[rowI].slice(columnI)
        grid[rowI] = newRow
    }
}
// mutates
function expandUniverse(grid) {
    for (let i=0; i<grid.length; i++) {
        if (isRowEmpty(grid[i])) {
            expandRow(grid, i)
            i++
        }
    }

    for (let i=0; i<grid[0].length; i++) {
        const column = []
        for (let y=0; y<grid.length; y++) {
            column.push(grid[y][i])
        }
        if (isColumnEmpty(column)) {
            expandColumn(grid, i)
            i++
        }
    }

    return grid
}
function findGalaxies(grid) {
    const galaxyLocations = []
    for (let y=0; y<grid.length; y++) {
        for (let x=0; x<grid[0].length; x++) {
            if (grid[y][x] === '#') {
                galaxyLocations.push({x,y})
            }
        }
    }
    return galaxyLocations
}
function findShortestPaths(galaxyLocations) {
    const shortestPaths = []
    for (let g1=0; g1<galaxyLocations.length-1; g1++) {
        for (let g2=g1+1; g2<galaxyLocations.length; g2++) {
            shortestPaths.push(Math.abs(galaxyLocations[g2].x-galaxyLocations[g1].x)+Math.abs(galaxyLocations[g2].y-galaxyLocations[g1].y))
        }
    }
    return shortestPaths
}

const grid = parseInput(data)
// for (const row of grid) {
//     console.log(row)
// }
const expanded = expandUniverse(grid)
// for (const row of expanded) {
//     console.log(row)
// }
const galaxyLocations = findGalaxies(expanded)
// console.log(galaxyLocations)
shortestPaths = findShortestPaths(galaxyLocations)
console.log(shortestPaths)
const SOLUTION_1 = shortestPaths.reduce((a,c)=>a+c)

module.exports = {}

// submit(SOLUTION_1)

console.log(`SOLUTION_1: ${SOLUTION_1}`)
// Example solution: 374