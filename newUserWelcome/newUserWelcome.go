package main

import (
	"io/ioutil"
	"strings"
	"fmt"
	"os"
	"github.com/sendgrid/sendgrid-go"
)

func main() {

	payloadIndex := 0
        for index, arg := range(os.Args) {
                if arg == "-payload" {
                        payloadIndex = index + 1
                }
        }
        if payloadIndex >= len(os.Args) {
                panic("No payload value.")
        }
        payload := os.Args[payloadIndex]
        raw, err := ioutil.ReadFile(payload)
	if err != nil {
				panic(err.Error())
					}
	println(string(raw))
	lines := strings.Split(string(raw), ":")
	name := lines[0]
	println(string(name))
	println(string(payload))
	email := lines[1]
	fmt.Println(name)
	fmt.Println(email)

	
	sg := sendgrid.NewSendGridClient("loqootv", "zxcvbnM1")
    	message := sendgrid.NewMail()
    	message.AddTo(email)
    	message.AddToName(name)
    	message.AddSubject("Welcome To LoqooTV")
    	message.AddText("Thank You for checking out the app. I hope it's of some use in your life")
    	message.AddFrom("sirvon@loqoo.tv")
    	if r := sg.Send(message); r == nil {
        	fmt.Println("Email sent!")
    	} else {
        	fmt.Println(r)
   	 }	


}
