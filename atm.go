package main

import (
    "fmt"
	"math"
	"strings"
    // "strings" // agar kerak bo‘lsa, qoldiring; hozircha ishlatilmayapti
)

var password int = 2014
var ammount int = 5000000
func display() {
    services := []string{
        "1. Withdraw money",
        "2. Checking balance",
        "3. Changing the password",
        "4. Paying for communals",
		"5. Quit",
    }
    fmt.Println(strings.Repeat("=",50))
    for i := 0; i < len(services); i++ {
        fmt.Println(services[i])
    }
	fmt.Println(strings.Repeat("=",50))
}

func withdraw(){
   var quiz int
   fmt.Print("Enter ammount of withdrawing: ")
   fmt.Scanln(&quiz)
   if quiz>=ammount{
	  fmt.Print("You don't have enough money for withdrawing❌")
   }else{
	 ammount-=quiz
	 comission:=float32(quiz)*0.02
	 total:=quiz+int(comission)
	 fmt.Println(strings.Repeat("=", 50))
     fmt.Println("Withdrawing:", quiz,"UZS")
     fmt.Println("Commission:", comission,"UZS")
     fmt.Println("Total:", total,"UZS")
	 fmt.Println("Available balance: ",ammount,"UZS")
     fmt.Println(strings.Repeat("=", 50))	

   }
}

func change(){
	var new_code int
	fmt.Println("Enter the new password: ")
	fmt.Scanln(&new_code)
	
    var retry int
	fmt.Print("Enter the new password retry: ")
	fmt.Scanln(&retry)
	
    if new_code != retry{
		fmt.Println("Password do not match ❌")
	    return
    }
    if new_code==password{
       fmt.Println("Your new password is same with previous one⚠️")
       return
    }
    password = new_code
    fmt.Println("Password changed successfully ✅")
	 
}
func check(){
	fmt.Println("In UZS: ",ammount)
	fmt.Println("In USD:", math.Round(float64(ammount)/11972))

}

func pay(){
   var ammount int=5000000
    bill:=[]string{
		"Natural Gas---45000UZS",
		"Drinking water---60000UZS",
		"Garbage---78000UZS",
		"Electrcity---55000UZS",
	} 
	 var location string
	 fmt.Print("Enter the your address (Region/str/house №): ")
	 fmt.Scanln(&location)
	 fmt.Println(strings.Repeat("=",50))
	 fmt.Print("choose a communal service: \n")
	 for ser:=0; ser<len(bill);ser++{
		fmt.Println(ser+1,"-> Paying for",bill[ser])
	 }
	 fmt.Println(strings.Repeat("=",50))
     var payme int
     fmt.Println("Mark the billing: ")
     fmt.Scanln(&payme)
     switch payme{
     case 1:
        fmt.Println("Paid for Natural Gas successfully ✅\n",location)
        ammount-=45000
     case 2:
        fmt.Println("Paid for Drinking\n",location)
        ammount-=60000
     case 3:
        fmt.Println("Paid for Garbage\n",location)
        ammount-=78000
     case 4:
        fmt.Println("Paid for Electrcity\n",location)
        ammount-=78000         
     default:
        fmt.Println("Incorrect input!!!")
    }
    fmt.Println("Current left: ",ammount)
	fmt.Println(strings.Repeat("=",50))
}
func main() {
    fmt.Println(strings.Repeat("=",50))
	hp := 3 // kartani bloklash uchun urinishlar soni
    for hp > 0 {
        var current int
        fmt.Print("Enter the Password of card: ")
        fmt.Scanln(&current)

        if current == password {
            isRunning := true
            for isRunning {
                display()
                var choice int
                fmt.Print("Enter service: ")
                fmt.Scanln(&choice)

                switch choice {
                case 1:
                    withdraw()
                case 2:
                    check()
                case 3:
                    change()
                case 4:
                    pay()
                case 5:
                    isRunning = false
                default:
                    fmt.Println("Invalid choice")
                }
            }
        } else {
            hp--
            fmt.Println("Wrong password. Attempts left:", hp)
            if hp == 0 {
                fmt.Println("Card is blocked ❌")
                break
            }
        }
    }
	fmt.Println(strings.Repeat("=",50))
}
