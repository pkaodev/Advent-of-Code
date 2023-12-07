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
		const validHands = ['22AAA', '2T2T2', '333QQ', '77KK7']
        for (const hand of validHands) {
            expect(getHandType(hand)).toBe('full')
        }
    })

    it("three of a kind", () => {
		const validHands = ['21AAA', '2T2Q2', '333KQ', '775K7']
        for (const hand of validHands) {
            expect(getHandType(hand)).toBe('three')
        }
    })

    it("two pairs", () => {
		const validHands = ['22AA3', 'QKQK4', '44233']
        for (const hand of validHands) {
            expect(getHandType(hand)).toBe('two')
        }
    })

    it("one pair", () => {
		const validHands = ['AA423', 'Q654Q', '52324']
        for (const hand of validHands) {
            expect(getHandType(hand)).toBe('one')
        }
    })

    it("high card", () => {
		const validHands = ['23456', 'AKQJT', '2Q3KA']
        for (const hand of validHands) {
            expect(getHandType(hand)).toBe('high')
        }
    })

})