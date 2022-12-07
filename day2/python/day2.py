
def part_one(lines):

 code_meaning={"A":"Rock","B":"Paper", "C":"Scissors","X":"Rock","Y":"Paper","Z":"Scissors"}
 points_for_shape={"Rock":1,"Paper":2,"Scissors":3}
 shape_supperiority={"Rock":"Scissors","Scissors":"Paper","Paper":"Rock"}
 win_points=6
 draw_points=3
 loss_points=0
 total_points=0
 for combination in lines:
     shape_opponent=code_meaning[combination[0]]
     shape_my=code_meaning[combination[2]]
     total_points+=points_for_shape[shape_my]
     if shape_supperiority[shape_opponent]==shape_my:
         total_points+=loss_points
     elif shape_supperiority[shape_my]==shape_opponent:
         total_points+=win_points

     else:
         total_points+=draw_points

 print(total_points)





def part_two(lines):

 code_meaning={"A":"Rock","B":"Paper", "C":"Scissors"}
 prediction={"X":"Loss","Y":"Draw","Z":"Win"}
 points_outcome={"Loss":0,"Draw":3,"Win":6}
 points_for_shape={"Rock":1,"Paper":2,"Scissors":3}
 shape_supperiority={"Rock":"Scissors","Scissors":"Paper","Paper":"Rock"}
 total_points=0
 for combination in lines:
     shape_opponent=code_meaning[combination[0]]
     outcome=prediction[combination[2]]
     total_points+=points_outcome[outcome]
     if outcome=="Loss":
         my_shape=shape_supperiority[shape_opponent]
         total_points+=points_for_shape[my_shape]
     elif outcome=="Win":
         my_shape=list(shape_supperiority.keys())[list(shape_supperiority.values()).index(shape_opponent)]
         total_points+=points_for_shape[my_shape]
     else:
         total_points+=points_for_shape[shape_opponent]

 print(total_points)


lines = open("input.txt").read().splitlines()
part_two(lines)