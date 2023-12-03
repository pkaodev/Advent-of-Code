package main

import ("fmt";"bufio";"log";"os")

func main() {
	score := 0;
	myMoveScore := map[string]int {
		"X": 1,	//rock
		"Y": 2,	//paper
		"Z": 3,	//scissors
	}
	loseWinDrawScore := map[string]int {
		"X": 0,
		"Y": 3,
		"Z": 6,
	}
	matchOutcomeScore := map[string]map[string]string {
		"A": {	//rock
			"X": "Z",	//lose
			"Y": "X",	//draw
			"Z": "Y",	//win
		},
		"B": {	//paper
			"X": "X",
			"Y": "Y",
			"Z": "Z",
		},
		"C": {	//scissors
			"X": "Y",
			"Y": "Z",
			"Z": "X",
		},
	}
	file, err1 := os.Open("./input.txt")
	if err1 != nil {log.Fatal(err1)}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		currEnemyMove := string(scanner.Text()[0])
		currMyMove := string(scanner.Text()[2])
		score += loseWinDrawScore[currMyMove]
		score += myMoveScore[matchOutcomeScore[currEnemyMove][currMyMove]]
	}

	fmt.Println(score)
}