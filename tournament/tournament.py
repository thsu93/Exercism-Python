import re

def tally(rows):
    table = ["Team                           | MP |  W |  D |  L |  P"]
    resultlist = []
    teamlist = []
    for i in rows:
        parsed_result = i.split(";")
        result = parsed_result[2]
        resultlist.append([parsed_result[0], result, 1])
        resultlist.append([parsed_result[1], result, 2])
    for result in resultlist:
        teamnames = [team.Name for team in teamlist]
        if result[0] in teamnames:
            teamlist[teamnames.index(result[0])].AddResult(result[1], result[2])
        else:
            newteam = Team(result[0])
            newteam.AddResult(result[1],result[2])
            teamlist.append(newteam)
    teamlist.sort(key = lambda team: (-team.Points, team.Name))
    table.extend([team.Print() for team in teamlist])
    return table
             
        
        
            
            
class Team:
    Name = ""
    Matches_Played = 0
    Wins = 0
    Draws = 0
    Losses = 0
    Points = 0
    
    def __init__(self, teamname):
        self.Name = teamname
    
    def AddResult(self, result, position):
        self.Matches_Played += 1
        if (result == "win" and position == 1) or (result == "loss" and position == 2):
            self.Wins += 1
            self.Points += 3
        elif result == "draw":
            self.Draws += 1
            self.Points +=1
        else:
            self.Losses += 1
    
    def Print(self):
        a= "{0:31}|  " + str(self.Matches_Played) + " |  " + str(self.Wins) + " |  " + str(self.Draws) + " |  " + str(self.Losses) + " |  " + str(self.Points)
        return a.format(self.Name)