package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
)

func main() {

	score := 0;

	myMoveScore := map[string]int{
		"X": 1,	//rock
		"Y": 2,	//paper
		"Z": 3,	//scissors
	}

	matchOutcomeScore := map[string]map[string]int {
		"A": {	//rock
			"X": 3,
			"Y": 6,
			"Z": 0,
		},
		"B": {	//paper
			"X": 0,
			"Y": 3,
			"Z": 6,
		},
		"C": {	//scissors
			"X": 6,
			"Y": 0,
			"Z": 3,
		},
	}

	file, err1 := os.Open("./input.txt")

	if err1 != nil {
		log.Fatal(err1)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {

		currEnemyMove := string(scanner.Text()[0])
		currMyMove := string(scanner.Text()[2])

		score += myMoveScore[currMyMove]
		score += matchOutcomeScore[currEnemyMove][currMyMove]
	}

	fmt.Println(score)
}