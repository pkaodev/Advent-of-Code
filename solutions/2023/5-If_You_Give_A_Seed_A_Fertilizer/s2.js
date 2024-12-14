const utils = require('../../../templates/javascript/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, './input')
const data = readFileSync(inputPath, 'utf8')

let [seeds, rest] = data.split('seed-to-soil map:')
let startSeeds = seeds.split('\n')[0].split(': ')[1].split(' ').map(Number)
let [s2s, s2f, f2w, w2l, l2t, t2h, h2l] = rest.split(/\s{1,}[a-z -]{1,}:/)
s2s = s2s.trim().split('\n').map(x => x.split(' ').map(Number))
s2f = s2f.trim().split('\n').map(x => x.split(' ').map(Number))
f2w = f2w.trim().split('\n').map(x => x.split(' ').map(Number))
w2l = w2l.trim().split('\n').map(x => x.split(' ').map(Number))
l2t = l2t.trim().split('\n').map(x => x.split(' ').map(Number))
t2h = t2h.trim().split('\n').map(x => x.split(' ').map(Number))
h2l = h2l.trim().split('\n').map(x => x.split(' ').map(Number))

const mappings = [s2s, s2f, f2w, w2l, l2t, t2h, h2l]

let minLocation = Infinity

for (let i = 0; i < startSeeds.length; i += 2) {
    let currentRanges = [[startSeeds[i], startSeeds[i] + startSeeds[i + 1] - 1]]

    for (let stepMapping of mappings) {
        let newRanges = []

        for (let [start, end] of currentRanges) {
            let newNewRange = []

            for (let mapping2 of stepMapping) {
                let [destStart, sourceStart, rangeM] = mapping2
                let sourceEnd = sourceStart + rangeM

                if (start < sourceEnd && end >= sourceStart) {
                    const overlapStart = Math.max(start, sourceStart)
                    const overlapEnd = Math.min(end, sourceEnd)
                    newNewRange.push([destStart + overlapStart - sourceStart, destStart + overlapEnd - sourceStart])
                }
            }
            if (newNewRange.length > 0) {
                newRanges.push(...newNewRange)
            } else {
                newRanges.push([start, end])
            }
        }
        currentRanges = newRanges
    }

    for (let currRange of currentRanges) {
        minLocation = Math.min(minLocation, currRange[0])
    }
}

const SOLUTION_2 = minLocation
console.log(`SOLUTION_2: ${SOLUTION_2}`)
