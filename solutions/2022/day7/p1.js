const readFileSync = require('fs').readFileSync;
const lines = readFileSync('./input-test.txt', 'utf8').split(/\n/)

//1. create a file system object

let currPath = []
const fileSystem = {}

for (let i = 1; i < lines.length; i++) {

    if (lines[i][0] === '$') {

        if (lines[i].split(' ')[1] === 'ls') {
            continue
        }


        if (lines[i].split(' ')[2] === '..') {
            currPath.pop()
            continue

        } else {
            currPath.push(lines[i].split(' ')[2])
            continue
        }

    }

    if (lines[i][0] === 'd') {

        const dir = lines[i].split(' ')[1]

        workingDir = fileSystem
        for (let j = 0; j < currPath.length; j++) {
            workingDir = workingDir[currPath[j]]
        }

        workingDir[dir] = {}

    } else {
        const file = lines[i].split(' ')[1]
        const size = parseInt(lines[i].split(' ')[0])

        workingDir = fileSystem
        for (let j = 0; j < currPath.length; j++) {
            workingDir = workingDir[currPath[j]]
        }

        workingDir[file] = size
    }
}

console.log(fileSystem)


//2. PART 1 sum up all the files in the file system
const filesUnder100KB = []

function sumUpDirectories(obj) {
    let directorySum = 0;

    for (let key in obj) {
        if (typeof obj[key] === 'object') {
            directorySum += sumUpDirectories(obj[key])
        } else {
            directorySum += obj[key]
        }
    }

    if (directorySum <= 100000) {
        filesUnder100KB.push(directorySum)
    }

    return directorySum
}

sumUpDirectories(fileSystem)
let sum = filesUnder100KB.reduce((a, b) => a + b, 0)
console.log(sum)





