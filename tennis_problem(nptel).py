from collections import Counter

#match = []
#while True:
#    line = input()
#    match.append(line)
#    if line == "EOF":
#        break
match = ['Zverev:Alcaraz:2-6,6-7,7-6,6-3,6-1', 'Swiatek:Jabeur:6-4,6-4', 'Alcaraz:Zverev:6-3,6-3', 'Jabeur:Swiatek:1-6,7-5,6-2', 
 'Zverev:Alcaraz:6-0,7-6,6-3', 'Jabeur:Swiatek:2-6,6-2,6-0','Alcaraz:Zverev:6-3,4-6,6-3,6-4', 
 'Swiatek:Jabeur:6-1,3-6,7-5', 'Zverev:Alcaraz:7-6,4-6,7-6,2-6,6-2', 'Jabeur:Swiatek:6-4,1-6,6-3',
 'Alcaraz:Zverev:7-5,7-5', 'Jabeur:Swiatek:3-6,6-3,6-3', 'EOF']

list_of_dict = []
#match = input("enter your string here: ")
for a in range(0,len(match)-1):
       tennis_set = {}
       player_split = match[a].split(":")
       player_name = []
       for l in range(0,2):
              player_name.append(player_split[l])
       scores = player_split[-1].split(",")
       individual_scores = []
       clean_scores = []
       for i in range(0,len(scores)):
              strip_dash = scores[i].split("-")
              individual_scores.append(strip_dash)
       for j in range(0,len(individual_scores)):   # j = 0,1,2 in list
              for k in range(0,len(individual_scores[j])):    # k = 0,1 in list within the list
                     clean_scores.append(individual_scores[j][k])


        # NOW INSERT PLAYER NAMES AND PLAYER SCORES INTO A DICTIONARY --> EFFICIENT ACCESS;)

        # player score list --> scores of players with respect to player name {"player_name1" : list_of_scores_of_that_player,
        #                                                                            "player_name2" : list_of_scores_of_that_player,}
       
       player1 = []
       player2 = []

       for b in range(0,len(clean_scores)):
              if b % 2 == 0:
                     player1.append(clean_scores[b])
              else:
                     player2.append(clean_scores[b])
       
       
       tennis_set[player_name[0]] = player1[:]
       
       tennis_set[player_name[1]] = player2[:]
       
       list_of_dict.append(tennis_set)
       player1.clear()
       player2.clear()
       player_name.clear()
       clean_scores.clear()
       individual_scores.clear()
       player_split = None

total_score_dict = {}
for c in list_of_dict:
       for key,value in c.items():
              #print(key,value)
              for score_idx in range(0,len(value)):
                     value[score_idx]  = int(value[score_idx])     
for d in list_of_dict:
       for key2,value2 in d.items():
              total = sum(value2) 
              if key2 in total_score_dict:
                     total_score_dict[key2] += total
              else:
                     total_score_dict[key2] = total
              
x = []
y = []
alpha = [] # <-- Player occurences counted with name bof 5
beta  = [] 
  
phi = []   # <-- Player occurences counted with name bof 3
chi = []
   
for e in list_of_dict:
       for key3,value3 in e.items():
              x.append(key3)
              y.append(value3)

for f in range(0,len(y)):
       if len(y[f])>=4 and f%2 == 0:
              alpha.append(x[f])
              beta.append(y[f])
       elif len(y[f])<=3 and f%2 == 0:
              phi.append(x[f])
              chi.append(y[f])

alpha_count = Counter(alpha)
phi_count = Counter(phi)

half_x = []
other_half_x = []
half_y = []
other_half_y = []

for mace in range(0,len(y)):
       if mace%2 == 0:
              half_y.append(y[mace])
              half_x.append(x[mace])
       else:
              other_half_y.append(y[mace])
              other_half_x.append(x[mace])

occurence = []

for match_idx, (windu,yoda) in enumerate(zip(half_y,other_half_y)):
       for grogu in range(0,len(windu)):
              if windu[grogu] > yoda[grogu]:
                     occurence.append(half_x[match_idx])
              elif windu[grogu] < yoda[grogu]:
                     occurence.append(other_half_x[match_idx])
              else:
                     pass
#print(occurence)
occurence_count = Counter(occurence)
list_of_list_of_dict = list(total_score_dict)
#print(list_of_list_of_dict)
print(list_of_list_of_dict[0],alpha_count.get(list_of_list_of_dict[0]),phi_count.get(list_of_list_of_dict[0]),
              occurence_count.get(list_of_list_of_dict[0]),total_score_dict.get(list_of_list_of_dict[0]),
              occurence_count.get(list_of_list_of_dict[1]),total_score_dict.get(list_of_list_of_dict[1]))

print(list_of_list_of_dict[1],alpha_count.get(list_of_list_of_dict[1]),phi_count.get(list_of_list_of_dict[1]),
              occurence_count.get(list_of_list_of_dict[1]),total_score_dict.get(list_of_list_of_dict[1]),
              occurence_count.get(list_of_list_of_dict[0]),total_score_dict.get(list_of_list_of_dict[0]))

print(list_of_list_of_dict[3],alpha_count.get(list_of_list_of_dict[3]),phi_count.get(list_of_list_of_dict[3]),
              occurence_count.get(list_of_list_of_dict[3]),total_score_dict.get(list_of_list_of_dict[3]),
              occurence_count.get(list_of_list_of_dict[2]),total_score_dict.get(list_of_list_of_dict[2]))

print(list_of_list_of_dict[2],alpha_count.get(list_of_list_of_dict[2]),phi_count.get(list_of_list_of_dict[2]),
              occurence_count.get(list_of_list_of_dict[2]),total_score_dict.get(list_of_list_of_dict[2]),
              occurence_count.get(list_of_list_of_dict[3]),total_score_dict.get(list_of_list_of_dict[3]))


