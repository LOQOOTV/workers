package main

import "fmt"
import "github.com/yanatan16/anaconda"

func main() {

	anaconda.SetConsumerKey("orwO5vps1L2tYqeZO5w7w")
	anaconda.SetConsumerSecret("qyBUwuXTLEZWQRuGnieSfKSZ8GMp9aWdSvW5eJMg7M")
	api := anaconda.NewTwitterApi("842877536-dKeG40Plx3ZIcISxcdS6jBPOeAeVHzJuaxlzJiDc", "ougcovWV0dLcFDfMzPtyJATpl887VOGCk5V9RVm6xkqmz")
		
	f := "@dsfsdf"
	if (string([]rune(f)[0])) == "@" {
		fmt.Println("its a twitter name")
	} else {
		fmt.Println("its a email address")
	}

	result, err := api.PostTweet("thanks for joining the convo"+f, nil)
	if err != nil {
		panic(err)
}
	fmt.Println(result)
}


