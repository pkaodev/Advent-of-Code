const readFileSync = require('fs').readFileSync
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/).filter(line => line !== '')

function fromSNAFU(snafu) {
    const len = snafu.length
    let digitValue = 0
    for (let i = 0; i < len; i++) {
        switch (snafu[i]) {
            case '2':
                digitValue += (5 ** (len - i - 1)) * 2
                break
            case '1':
                digitValue += (5 ** (len - i - 1))
                break
            case '0':
                break
            case '-':
                digitValue -= (5 ** (len - i - 1))
                break
            case '=':
                digitValue -= (5 ** (len - i - 1)) * 2
        }
    }
    return digitValue
}

const normalSum = instructions.reduce ((prev, curr) => prev + fromSNAFU(curr) , 0)

console.log(normalSum)

function toSNAFU(normal) {
    //1. find how many digits
    let maxValue = 0
    let noOfDigits = 0

    while (maxValue < normal) {
        noOfDigits++
        maxValue += 2 * 5 ** (noOfDigits - 1)
    }

    console.log('noOfDigits', noOfDigits)

    let workValue = 0

    let workString = ''

    for (let pos = 0; pos <= noOfDigits; pos++) {
        if (workValue + 2 * 5 ** (noOfDigits - pos - 1) < normalSum) {
            workValue += 2 * 5 ** (noOfDigits - pos - 1) < normalSum
            workString = workString + '2'
        } else if (workValue + 5 ** (noOfDigits - pos - 1) < normalSum) {
            workValue += 5 ** (noOfDigits - pos - 1) < normalSum
            workString = workString + '1'
        }
    }
}

toSNAFU(normalSum)