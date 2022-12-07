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



function sumUpDirectories(obj) {

    const allDirectories = [0]

    for (let key in obj) {
        if (typeof obj[key] === 'object') {
            sumUpDirectories(obj[key]).forEach(dirSum => allDirectories.push(dirSum))
        } else {
            allDirectories[0] += obj[key]
        }
    }

    return allDirectories
}

const allDirectories = sumUpDirectories(fileSystem)

allDirectories.sort((a, b) => a - b)

    for (let i = 0; i < allDirectories.length; i++) {
        if (allDirectories[i] >= 532950) {
            console.log(allDirectories[i])
            break
        }
    }





