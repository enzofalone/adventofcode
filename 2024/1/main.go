package main

import (
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	dat, err := os.ReadFile("in.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(dat), "\n")
	left := []int{}
	right := []int{}

	for _, line := range lines {
		parts := strings.Fields(line)
		if len(parts) != 2 {
			panic("invalid line")
		}

		leftNum, err := strconv.Atoi(parts[0])
		if err != nil {
			panic(err)
		}
		left = append(left, leftNum)

		rightNum, err := strconv.Atoi(parts[1])
		if err != nil {
			panic(err)
		}
		right = append(right, rightNum)
	}

	slices.Sort(left)
	slices.Sort(right)

	freqRight := map[int]int{}
	distances := []int{}
	sum := 0
	similarity := 0

	for i := 0; i < len(left); i++ {
		fmt.Println(left[i], right[i], right[i]-left[i])
		distances = append(distances, int(math.Abs(float64(right[i]-left[i]))))
		freqRight[right[i]]++

		sum += distances[len(distances)-1]
	}

	for i := 0; i < len(left); i++ {
		similarity += left[i] * freqRight[left[i]]
	}

	fmt.Println("sum", sum)
	fmt.Println("similarity", similarity)
}
