package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var bag = map[string]int{
	"red":   12,
	"green": 13,
	"blue":  14,
}

var possibleGames = 0
var totalAmountPow = 0

func main() {
	readFile, err := os.Open("input.txt")

	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(readFile)

	fileScanner.Split(bufio.ScanLines)
	for fileScanner.Scan() {
		line := fileScanner.Text()

		// decompose
		base := strings.Split(line, ":")

		gameNum, _ := strconv.Atoi(strings.Split(base[0], " ")[1])
		sets := strings.Split(base[1], ";")

		minAmount := map[string]int{
			"blue":  0,
			"red":   0,
			"green": 0,
		}

		isImpossible := false
		// decompose each set
		for _, set := range sets {
			cubes := strings.Split(set, ",")
			// check inside every set
			for _, cube := range cubes {
				cubeContent := strings.Split(strings.TrimSpace(cube), " ")

				num, _ := strconv.Atoi(cubeContent[0])
				color := cubeContent[1]

				if num > minAmount[color] {
					minAmount[color] = num
				}

				// check if game would have been impossible
				if num > bag[color] {
					isImpossible = true
				}
			}
		}

		if !isImpossible {
			possibleGames += gameNum
		}

		currentGamePow := 1
		for _, v := range minAmount {
			currentGamePow *= v
		}

		fmt.Println("currentGamePow", currentGamePow)
		totalAmountPow += currentGamePow
	}
	fmt.Println(possibleGames, totalAmountPow)
	readFile.Close()
}
