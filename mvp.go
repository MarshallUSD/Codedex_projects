package main

import (
    "fmt"
    "strings"
)

type ATM struct {
    password int        // CHANGED: struct ichida "var" olib tashlandi
    amount   float64    // CHANGED: float o‘rniga float64 ishlatildi
}

func (atm *ATM) display() {
    services := []string{
        "1. Withdraw money",
        "2. Checking balance",
        "3. Changing the password",
        "4. Paying for communals",
        "5. Quit",
    }
    fmt.Println(strings.Repeat("=", 50))
    for i := 0; i < len(services); i++ {
        fmt.Println(services[i])
    }
    fmt.Println(strings.Repeat("=", 50))
}

func (atm *ATM) withdraw() {
    var quiz float64 // CHANGED: int o‘rniga float64 ishlatildi
    fmt.Print("Enter amount of withdrawing: ")
    fmt.Scanln(&quiz)

    if quiz < 10000 {
        fmt.Println("You can't withdraw under 10000 UZS")
        return
    }

    if quiz > atm.amount { // CHANGED: amount tipiga moslashtirildi
        fmt.Println("You don't have enough money for withdrawing ❌")
        return
    }

    commission := quiz * 0.02 // CHANGED: float32 emas, float64 ishlatildi
    total := quiz + commission
    atm.amount -= total

    fmt.Println(strings.Repeat("=", 50))
    fmt.Println("Withdrawing:", quiz, "UZS")
    fmt.Println("Commission:", commission, "UZS")
    fmt.Println("Total:", total, "UZS")
    fmt.Println("Available balance:", atm.amount, "UZS")
    fmt.Println(strings.Repeat("=", 50))
}

func (atm *ATM) change() {
    var new_code int
    fmt.Print("Enter the new password: ")
    fmt.Scanln(&new_code)

    var retry int
    fmt.Print("Enter the new password retry: ")
    fmt.Scanln(&retry)

    if new_code != retry {
        fmt.Println("Password do not match ❌")
        return
    }
    if new_code == atm.password {
        fmt.Println("Your new password is same with previous one ⚠️")
        return
    }
    atm.password = new_code
    fmt.Println("Password changed successfully ✅")
}

func check(atm *ATM) {
    fmt.Println("In UZS:", atm.amount)
    usd := atm.amount / 11972
    fmt.Printf("In USD: %.2f\n", usd)
}

func pay(atm *ATM) {
    cart := map[string]int{}
    bill := map[int]struct {
        name  string
        price int
    }{
        1: {"Natural Gas", 45000},
        2: {"Drinking water", 60000},
        3: {"Garbage", 78000},
        4: {"Electricity", 55000},
    }

    var location string
    fmt.Print("Enter your address (Region/str/house №): ")
    fmt.Scanln(&location)

    for {
        fmt.Println("Choose a communal service:")
        for i := 1; i <= 4; i++ {
            fmt.Printf("%d -> Paying for %s --- %d UZS\n", i, bill[i].name, bill[i].price)
        }

        var payme int
        fmt.Print("Mark the billing: ")
        fmt.Scanln(&payme)

        if service, ok := bill[payme]; ok {
            if atm.amount >= float64(service.price) { // CHANGED
                cart[service.name] += service.price
                atm.amount -= float64(service.price)   // CHANGED
                fmt.Printf("Paid for %s successfully ✅\n%s\n", service.name, location)
            } else {
                fmt.Println("Insufficient balance ❌")
            }
        } else {
            fmt.Println("Incorrect input!!!")
        }

        var loop string
        fmt.Print("Is that all? (y/n): ")
        fmt.Scanln(&loop)

        if strings.ToLower(loop) == "y" {
            fmt.Println("\nYour cart:")
            total := 0
            for key, value := range cart {
                fmt.Printf("%s: %d UZS\n", key, value)
                total += value
            }
            fmt.Printf("Total paid: %d UZS\n", total)
            fmt.Println("Current balance:", atm.amount, "UZS") // CHANGED
            break
        } else if strings.ToLower(loop) != "n" {
            fmt.Println("Wrong input!!!")
        }
    }
}


func main() {
    myATM := ATM{password: 2014, amount: 5000000} // CHANGED: struct fieldlarga qiymat berildi
    var input_password int
    fmt.Print("Enter your password: ")
    fmt.Scanln(&input_password)
    if input_password != myATM.password {
        fmt.Println("Wrong password ❌")
        return
    }
    for {
        myATM.display()
        var choice int
        fmt.Print("Choose a service: ")
        fmt.Scanln(&choice)
        switch choice {
        case 1:
            myATM.withdraw() // CHANGED: metod chaqirish uchun () qo‘shildi
        case 2:
            check(&myATM)
        case 3:
            myATM.change()
        case 4:
            pay(&myATM)
        case 5:
            fmt.Println("Thank you for using our ATM service! 👋")
            return
        default:
            fmt.Println("Invalid choice, please try again ❌")
        }
    }
}
