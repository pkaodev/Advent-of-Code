const { parseInput, getHandType } = require("./s1.js")

describe("getHandType", () => {
    it("five of a kind", () => {
        const validHands = ['AAAAA', '22222', 'TTTTT']
        for (const hand of validHands) {
            expect(getHandType(hand)).toBe('five')
        }
    })

    it("four of a kind", () => {
        const validHands = ['2AAAA', '22T22', '3333Q']
        for (const hand of validHands) {
            expect(getHandType(hand)).toBe('four')
        }
    })

    it("full house", () => {
        
    })

    it("three of a kind", () => {
        
    })

    it("two pairs", () => {
        
    })

    it("one pair", () => {
        
    })

    it("high card", () => {
        
    })

})