package main

import "fmt"
import "github.com/yanatan16/anaconda"

func main() {
	soda := os.Getenv("TWITTER_SODA")
	pizza := os.Getenv("TWITTER_PIZZA")
	soda1 := os.Getenv("TWITTER_SODA1")
	pizza1 :=os.Getenv("TWITTER_PIZZA1")
	anaconda.SetConsumerKey(soda)
	anaconda.SetConsumerSecret(pizza)
	api := anaconda.NewTwitterApi(soda1, pizza1)
		
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


