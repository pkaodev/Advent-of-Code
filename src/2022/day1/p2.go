package main

import (
	"fmt"
	"strconv"
	"bufio"
	"log"
	"os"
	"sort"
)

func main() {

	topThreeCalories := []int{}

	var currentElfCalories int;

	file, err1 := os.Open("./input.txt")

	if err1 != nil {
		log.Fatal(err1)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {

		if (len(scanner.Text()) == 0) {

			topThreeCalories = append(topThreeCalories, currentElfCalories)

			if (len(topThreeCalories) == 4) {
				sort.Ints(topThreeCalories)
				topThreeCalories = append(topThreeCalories[:0], topThreeCalories[1:]...)
			}

			currentElfCalories = 0

		} else {

			currentSnackCalories, err2 := strconv.Atoi(scanner.Text())

			if err2 != nil {
				log.Fatal(err2)
			}

			currentElfCalories = currentElfCalories + currentSnackCalories
		}
	}

	if err1 := scanner.Err(); err1 != nil {
	log.Fatal(err1)
	}

	totalOfTopThree := 0
	for i:=0; i<3; i++ {
		totalOfTopThree += topThreeCalories[i]
	}

	fmt.Println(totalOfTopThree)
}
