oneone="* "
onetwo="* "
onethree="* "
twoone="* "
twotwo="* "
twothree="* "
threeone="* "
threetwo="* "
threethree= "* "
status=1

print(oneone+onetwo+onethree)
print(twoone+twotwo+twothree)
print(threeone+threetwo+threethree)



while status==1:


    p1x = int((input("Player 1 X: ")))
    p1y = int((input("Player 1 Y: ")))

    if p1x == 1:
        if p1y == 1:
            if oneone == "X " or oneone == "O ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                oneone="O "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p1y == 2:
            if onetwo == "X " or onetwo == "O ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                onetwo="O "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p1y == 3:
            if onethree == "X " or onethree == "O ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                onethree="O "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)

    if p1x == 2:
        if p1y == 1:
            if twoone == "X " or twoone == "O ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                twoone="O "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p1y == 2:
            if twotwo == "X " or twotwo == "O ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                twotwo="O "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p1y == 3:
            if twothree == "X " or twothree == "O ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                twothree="O "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)

    if p1x == 3:
        if p1y == 1:
            if threeone == "X " or threeone == "O ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                threeone="O "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p1y == 2:
            if threetwo == "X " or threetwo == "O ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                threetwo="O "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p1y == 3:
            if threethree == "X " or threethree == "O ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                threethree="O "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
                
    if oneone==onetwo==onethree or twoone==twotwo==twothree or threeone==threetwo==threethree or oneone==twoone==threeone or onetwo==twotwo==threetwo or onethree==twothree==threethree or oneone==twotwo==threethree or onethree==twotwo==threeone:
        print("GAME OVER!!!")
        re = str(input("Would you like to rematch(y) or quit(n)?:"))
        if re == "y":
            oneone="* "
            onetwo="* "
            onethree="* "
            twoone="* "
            twotwo="* "
            twothree="* "
            threeone="* "
            threetwo="* "
            threethree= "* "
            status=1

            print(oneone+onetwo+onethree)
            print(twoone+twotwo+twothree)
            print(threeone+threetwo+threethree)
            
            continue
            
        if re == "n":
            print("Exitting...")
            
            status=2
            quit()
        else:
            print("Illegal input, terminating")
            status=2
            quit()
        
            
    p2x = int((input("Player 2 X: ")))
    p2y = int((input("Player 2 Y: ")))



    if p2x == 1:
        if p2y == 1:
            if oneone == "O " or oneone == "X ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                oneone="X "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p2y == 2:
            if onetwo == "O " or onetwo == "X ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                onetwo="X "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p2y == 3:
            if onethree == "O " or onethree == "X ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                onethree="X "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)

    if p2x == 2:
        if p2y == 1:
            if twoone == "O " or twoone == "X ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                twoone="X "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p2y == 2:
            if twotwo == "O " or twotwo == "X ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                twotwo="X "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p2y == 3:
            if twothree == "O " or twothree == "X ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                twothree="X "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)

    if p2x == 3:
        if p2y == 1:
            if threeone == "O " or threeone == "X ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                threeone="X "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p2y == 2:
            if threetwo == "O " or threetwo == "X ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                threetwo="X "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
        if p2y == 3:
            if threethree == "O " or threethree == "X ":
                print("Illegal Move, terminating game.")
                status=2
                quit()
            else:
                threethree="X "
                print(oneone+onetwo+onethree)
                print(twoone+twotwo+twothree)
                print(threeone+threetwo+threethree)
                
    if oneone==onetwo==onethree or twoone==twotwo==twothree or threeone==threetwo==threethree or oneone==twoone==threeone or onetwo==twotwo==threetwo or onethree==twothree==threethree or oneone==twotwo==threethree or onethree==twotwo==threeone:
        print("GAME OVER!!!")
        res = str(input("Would you like to rematch(y) or quit(n)?:"))
        if res == "y":
            oneone="* "
            onetwo="* "
            onethree="* "
            twoone="* "
            twotwo="* "
            twothree="* "
            threeone="* "
            threetwo="* "
            threethree= "* "
            status=1

            print(oneone+onetwo+onethree)
            print(twoone+twotwo+twothree)
            print(threeone+threetwo+threethree)
            
            continue
            
        if res == "n":
            print("Exitting...")
            
            status=2
            quit()
        else:
            print("Illegal input, terminating")
            status=2
            quit()
        
if status == 2:
    quit()        
