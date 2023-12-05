const utils = require('../../../language-setups/javascript/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, './input_example')
const data = readFileSync(inputPath, 'utf8')

let [seeds, rest] = data.split('seed-to-soil map:')
seeds = seeds.split('\n')[0].split(': ')[1].split(' ').map(Number)
let [s2s, s2f, f2w, w2l, l2t, t2h, h2l] = rest.split(/\s{1,}[a-z -]{1,}:/)
s2s = s2s.trim().split('\n').map(x=>x.split(' ').map(Number))
s2f = s2f.trim().split('\n').map(x=>x.split(' ').map(Number))
f2w = f2w.trim().split('\n').map(x=>x.split(' ').map(Number))
w2l = w2l.trim().split('\n').map(x=>x.split(' ').map(Number))
l2t = l2t.trim().split('\n').map(x=>x.split(' ').map(Number))
t2h = t2h.trim().split('\n').map(x=>x.split(' ').map(Number))
h2l = h2l.trim().split('\n').map(x=>x.split(' ').map(Number))

mappings = [h2l, t2h, l2t, w2l, f2w, s2f, s2s]

// start with location number (1?)
// map back through to seed
// if that number is in seeds, return it

// humidity-to-location map:
// 60 56 37
// 56 93 4

// check for each mapping
// if locationNum in 60->60+(37-1)
// then humidityNum is locationNum+(56-60)
// else humidityNum is locationNum



let SOLUTION_1

let locationNum = 1
while(true) {
    let currNum = locationNum

    // mapping1 = h2l, t2h...
    for (let mapping1 of mappings) {
        // mapping2 = 60,56,37... dest,source,range
        for (let mapping2 of mapping1) {
            if (currNum >= mapping2[0] && currNum <= mapping2[0]+mapping2[2]-1) {
                currNum = currNum+mapping2[1]-mapping2[0]
                break
            }
        }
    }

    if (seeds.includes(currNum)) {
        SOLUTION_1 = locationNum
    }


    locationNum++
}


console.log(`SOLUTION_1: ${SOLUTION_1}`)
// Example Solution: 35
