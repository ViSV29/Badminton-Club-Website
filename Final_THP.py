import turtle

Dict_rank = {} #global value
ladder = []#global value

def ladderMaker(): #function to make list that holds players in order ; rank of player = index + 1

    global ladder
    
    lastNum = 0
    for key in Dict_rank:
        if Dict_rank[key] > lastNum :
            lastNum = Dict_rank[key]

    ladder = []

    for i in range(1,lastNum + 1):
        for key in Dict_rank:
            if Dict_rank[key] == i:
                ladder.append(key)
    return ladder

def writeLadderFile(date): #function to generate and save ladder on a specific date

    filename = date + ".txt"
    infile = open(filename, 'w')
    
    with open(filename, 'w') as f:
        f.write("1" + " " + ladder[0])
        for i in range(1,len(ladder)):
            pos = int(i) + 1
            f.write('\n' + str(pos) + " " +ladder[i])
    infile.close()

def DictionaryMaker(): #function to create dictionary to hold updated rankings

    global Dict_rank
    global ladder

    for i in range(len(ladder)):
        Dict_rank[ladder[i]] = i + 1


def rankDiff(key1,key2,n): #key1 = challenger; key2 = challenged; match has been played or match has been cancelled

    pos1 = Dict_rank[key1]
    pos2 = Dict_rank[key2]

    if n == 1 :

        Dict_rank[key1] = pos2
        Dict_rank[key2] = pos1

    elif n == 2 :

        Dict_rank[key1] = pos2
        Dict_rank[key2] += 1

        
        for key in Dict_rank:
            if (key != key2) and Dict_rank[key] == Dict_rank[key2]:
                Dict_rank[key] += 1

    else : #n == 3

        Dict_rank[key1] = pos2
        Dict_rank[key2] += 1

        for key in Dict_rank:
            if Dict_rank[key] == (Dict_rank[key2] + 1):
                Dict_rank[key] += 1

        for key in Dict_rank:
            if (key != key2) and (Dict_rank[key] == Dict_rank[key2]):
                Dict_rank[key] += 1

rank = 0 #global rank

def withdrawPlayer(): #pos - rank of player leaving

    global rank

    for key in Dict_rank:
        if Dict_rank[key] - rank == 1:
            Dict_rank[key] = rank

        else :
            rank += 1

def MatchesPlayed(): #function to create dictionary to keep track of number of matches played by each player

    numMatch = {}

    infile = open("data.txt","r")

    for line in infile :
        line_data = line.split("/")
        if len(line_data) == 4:

            player1_data = line_data[0].split()
            player2_data = line_data[1].split()

            player1Name = player1_data[0] + " " + player1_data[1] 
            player2Name= player2_data[0] + " " + player2_data[1]

            if player1Name in numMatch :
                numMatch[player1Name] += 1
            else :
                numMatch[player1Name] = 1

            if player2Name in numMatch :
                numMatch[player2Name] += 1
            else :
                numMatch[player2Name] = 1
    return numMatch

#=========================================================================MAIN PROGRAM=======================================================================================================

def mainProgram(): #function to sort ladder
    for line in open("data.txt", "r"):
        line_data = line.split("/")

        if len(line_data) == 4: #match has been played or match has been cancelled

            challenger_data = line_data[0].split() #name, score
            challenged_data = line_data[1].split() #name, score
            date = line_data[2]
            scores_data = line_data[-1].split()

            a = challenger_data[0] + " " + challenger_data[1] #challenger name
            Dict_rank[a] = int(challenger_data[-1]) #challenger position

            b = challenged_data[0] + " " + challenged_data[1] #challenged name
            Dict_rank[b] = int(challenged_data[-1]) #challenged position

            wins = 0
            for i in range(len(scores_data)):

                scores_data2 = scores_data[i].split("-")

                if int(scores_data2[0]) > int(scores_data2[1]):
                    wins += 1

            if wins >= 2 :
                n = Dict_rank[a] - Dict_rank[b]
                rankDiff(a,b,n)

                ladderMaker()
                writeLadderFile(date)
                DictionaryMaker()

            else : #challenger lost; position remains the same
                ladderMaker()
                writeLadderFile(date)
                DictionaryMaker()

        elif len(line_data) == 3: #match has been played or match has been cancelled

            challenger_data = line_data[0].split() #name, score
            challenged_data = line_data[1].split() #name, score

            a = challenger_data[0] + " " + challenger_data[1] #challenger name
            Dict_rank[a] = int(challenger_data[-1]) #challenger position

            b = challenged_data[0] + " " + challenged_data[1] #challenged name
            Dict_rank[b] = int(challenged_data[-1]) #challenged position

            n = Dict_rank[a] - Dict_rank[b]
            rankDiff(a,b,n)
            
            ladderMaker()
            writeLadderFile(date)
            DictionaryMaker()

        else : #len(line_data) == 2 : #new player or player withdrawing

            player_data = line_data[0].split() 
            date_data = line_data[1].split("\n")
            date = date_data[0] #joining date/ withdrawing date

            a = player_data[0][1:] + " " + player_data[1] #player name

            if player_data[0][0] == "+" : #new player

                last = 0
                for key in Dict_rank:
                    if Dict_rank[key] > last:
                        last = Dict_rank[key]

                Dict_rank[a] = last + 1

                ladderMaker()
                writeLadderFile(date)
                DictionaryMaker()

            else : #player_data[0][0] == "-"

                rank = Dict_rank[a]

                del Dict_rank[a]
                
                withdrawPlayer()

                ladderMaker()
                writeLadderFile(date)
                DictionaryMaker()

mainProgram()

#============================================================================ GUI =========================================================================================================  
def TurtleWrite(x,y): #(x,y) coordinate system

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def writeScreen(): #to clear left side of turtle display
    
    turtle.color("#FFFFF0")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(1000)
    turtle.left(90)
    turtle.forward(500)
    turtle.end_fill()

def infoScreen(): #to clear right side of turtle display
    
    turtle.color("#FFFFF0")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(1000)
    turtle.right(90)
    turtle.forward(500)
    turtle.end_fill()

def leftBox():

    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

def rightBox():

    turtle.begin_fill()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()

import time
def dateValid(year, month, day):
    date = '%d/%d/%d' % (month, day, year)
    try:
        time.strptime(date, '%m/%d/%Y')
    except ValueError:
        return False
    else:
        return True

def buttonRanking(x,y):
    if x < 100 and x > -100 and y < 50 and y > 0:
        turtle.delay(0)
        turtle.hideturtle()
        TurtleWrite(-200,0)
        writeScreen()
        TurtleWrite(750,0)
        infoScreen()
        
        infile = open("data.txt", "r")
        for line in infile:
            line_data = line.split("/")
            if len(line_data) == 4:
                infoLat = line
                date = line_data[2]
            elif len(line_data) == 2:
                date_data = line_data[1].split("\n")
                date = date_data[0]
            else:
                pass
            
        turtle.color("#722f37")
        TurtleWrite(270,-200)
        turtle.write("Latest Match Results",font=("Times New Roman",25, "bold", "underline"),align="left")
        TurtleWrite(270,-250)
        turtle.write(infoLat,font=("Times New Roman",15),align="left")

        filename = date + ".txt"
        listfile = open(filename, "r")

        turtle.color("#722f37")
        TurtleWrite(-500,110)
        turtle.write(date,font=("Times New Roman",20, "bold", "underline"),align="left")

        count = 0
        for line in listfile:
            count += 1
            turtle.penup()
            turtle.setpos(-500,105-(count*25))
            turtle.pendown()
            if line[-1] == "\n":
                turtle.write(line[:-1],font=("Times New Roman",20),align="left")
            else :
                turtle.write(line,font=("Times New Roman",20),align="left")

        TurtleWrite(270,75)
        turtle.write("Upcoming Matches",font=("Times New Roman",25, "bold", "underline"),align="left")

        count = 0
        for line in open("UpcomingMatches.txt", "r"):
            count += 1
            if count != 3:
                turtle.penup()
                turtle.setpos(270,50-(count*25))
                turtle.pendown()
                turtle.write(line,font=("Times New Roman",15),align="left")
turtle.onscreenclick(buttonRanking, 1, add=True)

def buttonChallenge(x,y):
    global Dict_rank
    if x < 100 and x > -100 and y < -10 and y > -60:
        turtle.delay(0)
        turtle.hideturtle()

        challName = turtle.textinput("Challenger Name","Please enter full name as in Club Records : ")
        challPos = Dict_rank[challName]

        while True:
            dateOfMatch = turtle.textinput("Match Date","Please enter play-by date of the match(dd-mm-yyyy) : ")
            if len(dateOfMatch) == 10:
                pass
            else:
                continue
            try :
                d,m,y = int(dateOfMatch.split("-")[0]), int(dateOfMatch.split("-")[1]), int(dateOfMatch.split("-")[-1])
                if dateValid(y,m,d):
                    break
            except:
                continue

        TurtleWrite(-200,0)
        writeScreen()

        turtle.color("#722f37")

        if challPos >= 4:

            champ1 = challPos - 1
            champ2 = challPos - 2
            champ3 = challPos - 3
            
            TurtleWrite(-500,0)
            turtle.write("Choose opponent:",font=("Times New Roman",20, "bold"),align="left")
            TurtleWrite(-500,-60)
            turtle.write(champ1,font=("Times New Roman",20),align="left")
            TurtleWrite(-500,-120)
            turtle.write(champ2,font=("Times New Roman",20),align="left")
            TurtleWrite(-500,-180)
            turtle.write(champ3,font=("Times New Roman",20),align="left")

            oppPos = turtle.textinput("Opponent Position","Please enter the position of your opponent : ")

        elif challPos >= 3 :

            champ1 = challPos - 1
            champ2 = challPos - 2

            TurtleWrite(-500,0)
            turtle.write("Choose opponent:",font=("Times New Roman",20, "bold"),align="left")
            TurtleWrite(-500,-60)
            turtle.write(champ1,font=("Times New Roman",20),align="left")
            TurtleWrite(-500,-120)
            turtle.write(champ2,font=("Times New Roman",20),align="left")

            oppPos = turtle.textinput("Opponent Position","Please enter the position of your opponent : ")

        elif challPos >= 2 :

            champ1 = challPos - 1

            TurtleWrite(-500,0)
            turtle.write("Choose opponent:",font=("Times New Roman",20, "bold"),align="left")
            TurtleWrite(-500,-60)
            turtle.write(champ1,font=("Times New Roman",20),align="left")

            oppPos = turtle.textinput("Opponent Position","Please enter the position of your opponent : ")

        else :
            TurtleWrite(-500,-20)
            turtle.write("No opponent!",font=("Times New Roman",20, "bold"),align="left")

        try:
            if challPos - int(oppPos) <=3:
                for key in Dict_rank :
                    if Dict_rank[key] == int(oppPos):
                        oppName = key

            TurtleWrite(-250,0)
            writeScreen()

            turtle.color("#722f37")

            TurtleWrite(-500,-125)
            turtle.write(challName + "\n" + "will play against" + "\n" + oppName + "\n" + "on " + dateOfMatch ,font=("Times New Roman",20,),align="center")

            outfile = open("UpcomingMatches.txt", "a")

            print(challName + " " + str(challPos) + "/" + oppName + " " + oppPos + "/" + dateOfMatch, file = outfile) #store matches yet to be played on a new file

            outfile.close()  
        except:
            TurtleWrite(-500,0)
            turtle.write("Invalid input!",font=("Times New Roman",20, "bold"),align="left")
turtle.onscreenclick(buttonChallenge, 1, add=True)

def buttonJoin(x,y):
    if x < 100 and x > -100 and y < -70 and y > -120:
        newPlayerName = turtle.textinput("Name Input","Please enter full name as in ID : ")
        newPlayerData = newPlayerName.split()

        outfile = open("data.txt","a")
        print("+", end = "", file = outfile)

        for i in range(len(newPlayerData)):
            if i == len(newPlayerData)-1:
                print(" " + newPlayerData[i] + "/", end = "", file = outfile)
            else :
                print(newPlayerData[i][0], end= "", file = outfile)
        while True:
            joinDate = turtle.textinput("Date of Admission","Please enter today's date(dd-mm-yyyy): ")
            if len(joinDate) == 10:
                pass
            else:
                continue
            try:
                d,m,y = int(joinDate.split("-")[0]), int(joinDate.split("-")[1]), int(joinDate.split("-")[-1])
                if dateValid(y,m,d):
                    break
            except:
                continue
        print(joinDate, file = outfile)
        outfile.close()
        mainProgram()
turtle.onscreenclick(buttonJoin, 1, add=True)

name = "" #global value
def buttonWithdraw(x,y):
    global name
    global Dict_rank
    if x < 100 and x > -100 and y < -130 and y > -180:
        outfile = open("data.txt", "a")
        
        leavePlayerName = turtle.textinput("Name Input","Please enter full name as in ID : ")
        while True:
            leaveDate = turtle.textinput("Date of Withdrawal","Please enter today's date(dd-mm-yyyy): ")
            if len(leaveDate) == 10:
                pass
            else:
                continue
            try:
                d,m,y = int(leaveDate.split("-")[0]), int(leaveDate.split("-")[1]), int(leaveDate.split("-")[-1])
                if dateValid(y,m,d):
                    break
            except:
                continue   
        leavePlayerData = leavePlayerName.split()
        for i in range(len(leavePlayerData)):
            if i == 0:
                name = leavePlayerData[0][0]
            elif i == len(leavePlayerData)-1:
                name += " " + leavePlayerData[i] 
            else :
                name += leavePlayerData[i][0]       
        try : #check if player in club
            rank = Dict_rank[name]
            print("-" + name + " " + str(rank) + "/", end = "" ,file = outfile)
            print(leaveDate, file = outfile)
            outfile.close()
            mainProgram()
        except:
            turtle.color("#722f37")
            TurtleWrite(-650,0)
            turtle.write("You are not a Member!",font=("Times New Roman",20, "bold"),align="left")            
turtle.onscreenclick(buttonWithdraw, 1, add=True)

numMatch = {}
def buttonQuery(x,y):
    if x < 100 and x > -100 and y < -190 and y > -240:
        turtle.delay(0)
        turtle.hideturtle()
        TurtleWrite(-250,0)
        writeScreen()
        TurtleWrite(750,0)
        infoScreen()
        turtle.color("#722f37")
        TurtleWrite(270,80)
        turtle.write("Press 1 for The Rankings on a specific date",font=("Times New Roman",15, "bold"),align="left")
        TurtleWrite(270,20)
        turtle.write("Press 2 for the list of matches a Player has played",font=("Times New Roman",15, "bold"),align="left")
        TurtleWrite(270,-40)
        turtle.write("Press 3 for the Most Active Player",font=("Times New Roman",15, "bold"),align="left")
        TurtleWrite(270,-100)
        turtle.write("Press 4 for the Least Active Player",font=("Times New Roman",15, "bold"),align="left")
        TurtleWrite(270,-160)
        turtle.write("Press 5 for Match on a Specific date",font=("Times New Roman",15, "bold"),align="left")
        TurtleWrite(270,-220)
        turtle.write("Press 6 for Match between Specific players",font=("Times New Roman",15, "bold"),align="left")
        TurtleWrite(270,-280)
        turtle.write("Press 7 to check number of Matches played in a Month",font=("Times New Roman",15, "bold"),align="left")

        while True:
            option = turtle.textinput("Query","What is your Query : ")
            if option in "1234567":
                 break
            else:
                turtle.color("#722f37")

                TurtleWrite(-500,75)
                turtle.write("Invalid query request!",font=("Times New Roman",20),align="center")
                continue    

        if option == "1" :
            while True:
                date = turtle.textinput("RANKINGS", "Enter date(dd-mm-yyyy):")   
                if len(date) == 10:
                    pass
                else:
                    continue
                try:
                    d,m,y = int(date.split("-")[0]), int(date.split("-")[1]), int(date.split("-")[-1])
                    if dateValid(y,m,d):
                        break
                except:
                    continue    
            infilename = date +".txt"
            try:
                infile = open(infilename, "r")
                turtle.color("#722f37")
                TurtleWrite(-650,110)
                turtle.write(date,font=("Times New Roman",20, "bold", "underline"),align="left")
                count = 0
                for line in infile:
                    count += 1
                    turtle.penup()
                    turtle.setpos(-650,105-(count*25))
                    turtle.pendown()
                    if line[-1] == "\n":
                        turtle.write(line[:-1],font=("Times New Roman",20),align="left")
                    else :
                        turtle.write(line,font=("Times New Roman",20),align="left")
            except:
                turtle.color("#722f37")

                TurtleWrite(-500,75)
                turtle.write("Ladder was not Updated on this Date!",font=("Times New Roman",20),align="center")
   
        elif option == "2" :
            numMatch =  MatchesPlayed()
            global Dict_rank
            
            PlayerNum = turtle.textinput("Number of Matches Played by ","Which Player?(Please enter position of player : ")

            try : #check if player is in the club
                for key in Dict_rank :
                    if Dict_rank[key] == int(PlayerNum):
                        playerName = key        
                turtle.color("#722f37")
                TurtleWrite(-650,0)
                turtle.write(playerName + " has played" + "\n" + str(numMatch[playerName]) + " Matches.",font=("Times New Roman",20),align="left")
                TurtleWrite(-650,-50)
                turtle.write("Matches Played : ",font=("Times New Roman",20),align="left")
                
                count = 0
                for line in open("data.txt", "r"):
                    if (playerName in line) and len(line.split("/")) == 4:
                        count += 1
                        turtle.color("#722f37")
                        turtle.penup()
                        turtle.setpos(-650,-70-(count*25))
                        turtle.pendown()
                        turtle.write(line, font=("Times New Roman",12),align="left")
            except :
                turtle.color("#722f37")
                TurtleWrite(-500,0)
                turtle.write("Player not Found!",font=("Times New Roman",20, "bold"),align="center")                

        elif option == "3":
            numMatch =  MatchesPlayed()
            most = 0
            most_list = []
            for key in numMatch:
                if numMatch[key] > most:
                    most = numMatch[key]
            for key in numMatch:
                if numMatch[key] == most:
                    most_list.append(key)
            turtle.color("#722f37")
            TurtleWrite(-650,100)
            turtle.write("The Most Active Player/s" ,font=("Times New Roman",20),align="left")

            count = 0
            for i in range(len(most_list)):
                count += 1
                TurtleWrite(-650,50-(count*25))
                turtle.write(most_list[i] ,font=("Times New Roman",30, "bold"),align="left")

        elif option == "4":
            numMatch =  MatchesPlayed()
            least = 1
            least_list = []
            for key in numMatch:
                if numMatch[key] >= least:
                    least = least
            for key in numMatch:
                if numMatch[key] == least:
                    least_list.append(key)

            turtle.color("#722f37")
            TurtleWrite(-650,100)
            turtle.write("The Least Active Player/s" ,font=("Times New Roman",20),align="left")

            count = 0
            for i in range(len(least_list)):
                count += 1
                TurtleWrite(-650,50-(count*25))
                turtle.write(least_list[i] ,font=("Times New Roman",30, "bold"),align="left")


        elif option == "5":
            while True:
                date = turtle.textinput("RANKINGS", "Enter date(dd-mm-yyyy):")   
                if len(date) == 10:
                    pass
                else:
                    continue
                try:
                    d,m,y = int(date.split("-")[0]), int(date.split("-")[1]), int(date.split("-")[-1])
                    if dateValid(y,m,d):
                        break
                except:
                    continue

            filename = "data.txt"
            try:
                infile = open(filename, "r")
                count = 0
                for line in infile:
                    if date in line and (len(line.split("/"))==4):
                        count += 1
                        turtle.color("#722f37")
                        TurtleWrite(-650,100-(count*25))
                        turtle.write(line,font=("Times New Roman",12),align="left")
            except:
                turtle.color("#722f37")
                TurtleWrite(-650,0)
                turtle.write("No match on this Date!",font=("Times New Roman",20, "bold"),align="left")

        elif option == "6":
            p1 = turtle.textinput("Player 1 Name","Please enter the name of the player as per Club Records : ")
            p2 = turtle.textinput("Player 2 Name","Please enter the name of the player as per Club Records : ")
            try :
                count = 0
                for line in open("data.txt", "r"):
                    if (p1 in line and p2 in line) and (len(line.split("/"))==4):
                        count += 1
                        turtle.color("#722f37")
                        TurtleWrite(-700,105-(count*25))
                        turtle.write(line,font=("Times New Roman",15),align="left")             
            except:
                turtle.color("#722f37")
                TurtleWrite(-650,0)
                turtle.write("No Results!",font=("Times New Roman",20),align="left")
                
        elif option == "7":
            monthDict = {"01":"January" , "02":"February" , "03":"March" , "04":"April" , "05":"May" ,"06":"June" ,"07" : "July", "08":"August" , "09":"September" , "10":"October" , "11":"November" , "12":"December"}
            month = turtle.textinput("Enter Month","Which Month(mm) : ")
            year = turtle.textinput("Enter Year","Which Year(yyyy) : ")
            try:
                infile = open("data.txt", "r")
                count = 0
                for line in infile:
                    line_data = line.split("/")
                    if len(line_data )==4:
                        date_data = line_data[2].split("-")
                        if date_data[1] == month and date_data[-1] == year:
                            count += 1
                            turtle.color("#722f37")
                            TurtleWrite(-650,100-(count*25))
                            turtle.write(line,font=("Times New Roman",12),align="left")
                            
                TurtleWrite(-650,120)
                turtle.write("Number of matches in " + monthDict[month] + " " + year + ": " + str(count),font=("Times New Roman",15),align="left")
            except:
                turtle.color("#722f37")
                TurtleWrite(-650,0)
                turtle.write("Invalid input!",font=("Times New Roman",20, "bold"),align="left")
        else :
            pass
turtle.onscreenclick(buttonQuery, 1, add=True)

#=========================================================================================================================================================================

window = turtle.Screen()
window.bgcolor("#FFFFF0")

turtle.delay(0) #makes turtle run faster
turtle.hideturtle()

turtle.color("purple")
TurtleWrite(0,200)
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

turtle.color("#FFD700")
TurtleWrite(0,245)
turtle.write("EMPIRE",font=("Times New Roman",36, "bold"),align="center")
TurtleWrite(0,195)
turtle.color("#FFD700")
turtle.write("BADMINTON",font=("Times New Roman",36, "bold"),align="center")

#============================ RANKING BUTTON ==========================

turtle.color("purple")
TurtleWrite(0,0)
leftBox()
turtle.color("#FFD700")
TurtleWrite(0,7)
turtle.write("RANKINGS", font=("Times New Roman",24),align="center")

buttonRanking(0,0)

#============================ CHALLENGE BUTTON ==========================

turtle.color("purple")
TurtleWrite(0,-10)
rightBox()
turtle.color("#FFD700")
TurtleWrite(0,-55)
turtle.write("CHALLENGE", font=("Times New Roman",24),align="center")

buttonChallenge(0,-60)

#=============================== JOIN BUTTON ===========================

turtle.color("purple")
TurtleWrite(0,-70)
rightBox()
turtle.color("#FFD700")
TurtleWrite(0,-115)
turtle.write("JOIN", font=("Times New Roman",24),align="center")

buttonJoin(0,-120)

#============================== WITHDRAW BUTTON ===========================

turtle.color("purple")
TurtleWrite(0,-130)
rightBox()
turtle.color("#FFD700")
TurtleWrite(0,-175)
turtle.write("WITHDRAW", font=("Times New Roman",24),align="center")

buttonWithdraw(0,-180)

#============================= QUERY BUTTON ===============================

turtle.color("purple")
TurtleWrite(0,-190)
rightBox()
turtle.color("#FFD700")
TurtleWrite(0,-235)
turtle.write("QUERY", font=("Times New Roman",24),align="center")

buttonQuery(0,-240)
