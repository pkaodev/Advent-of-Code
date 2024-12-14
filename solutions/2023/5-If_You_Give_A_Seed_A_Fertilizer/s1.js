const utils = require('../../../templates/javascript/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, './input')
const data = readFileSync(inputPath, 'utf8')

let [seeds, rest] = data.split('seed-to-soil map:')
seeds = seeds.split('\n')[0].split(': ')[1].split(' ').map(Number)
let [s2s, s2f, f2w, w2l, l2t, t2h, h2l] = rest.split(/\s{1,}[a-z -]{1,}:/)
s2s = s2s.trim().split('\n').map(x => x.split(' ').map(Number))
s2f = s2f.trim().split('\n').map(x => x.split(' ').map(Number))
f2w = f2w.trim().split('\n').map(x => x.split(' ').map(Number))
w2l = w2l.trim().split('\n').map(x => x.split(' ').map(Number))
l2t = l2t.trim().split('\n').map(x => x.split(' ').map(Number))
t2h = t2h.trim().split('\n').map(x => x.split(' ').map(Number))
h2l = h2l.trim().split('\n').map(x => x.split(' ').map(Number))

mappings = [s2s, s2f, f2w, w2l, l2t, t2h, h2l]
locationNums = []

for (let seedNum of seeds) {
    let currNum = seedNum

    let mappingI = 0
    for (let mapping1 of mappings) {
        mappingI++

        innerLoop: for (let mapping2 of mapping1) {
            let destStart = mapping2[0]
            let sourceStart = mapping2[1]
            let range = mapping2[2]

            if (currNum >= sourceStart && currNum <= sourceStart + range - 1) {
                currNum = currNum + destStart - sourceStart
                break innerLoop
            }
        }
    }
    locationNums.push(currNum)
}
const SOLUTION_1 = locationNums.sort((a,b)=>a-b)[0]
console.log(`SOLUTION_1: ${SOLUTION_1}`)
// Example Solution: 35
