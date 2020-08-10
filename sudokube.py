def print_cube():
    print(*bottom[0:3], sep =' ')
    print(*bottom[3:6], sep =' ')
    print(*bottom[6:9], sep =' ')
    print()
    print(*top[0:3], sep =' ')
    print(*top[3:6], sep =' ')
    print(*top[6:9], sep =' ')
    print()
    print(*left[0:3], sep =' ')
    print(*left[3:6], sep =' ')
    print(*left[6:9], sep =' ')
    print()
    print(*front[0:3], sep =' ')
    print(*front[3:6], sep =' ')
    print(*front[6:9], sep =' ')
    print()
    print(*right[0:3], sep =' ')
    print(*right[3:6], sep =' ')
    print(*right[6:9], sep =' ')
    print()

    print(*back[9:5:-1], sep =' ')
    print(*back[5:2:-1], sep =' ')
    print(*back[2::-1], sep =' ')

    

    
   


aa=[]
for i in range(6):
    a1 = list(map(int,input().strip().split()))
    a2 = list(map(int,input().strip().split()))
    a3 = list(map(int,input().strip().split()))
    if i==5:
        a4=a3[::-1]  +a2[::-1]  +a1[::-1]  
    else:
        a4= a1+a2+a3
    aa.append(a4)

c=list(input().strip().split())
top = aa[1]
front = aa[3]
bottom = aa[0]
back = aa[5]
left = aa[2]
right = aa[4]




number_of_moves = c[0]
count = 0
cc=[]
for i in c:
    if len(i)==1:
        cc.append(i)
    elif i[1]=="'":
        cc.append(i)
    elif i[1]=="2":
        cc.append(i[0])
        cc.append(i[0])
    elif i[1]=="3":
        cc.append(i[0])
        cc.append(i[0])
        cc.append(i[0])
    elif i[1]=="4":
        cc.append(i[0])
        cc.append(i[0])
        cc.append(i[0])
        cc.append(i[0])
        

for i in cc:

    # generate a number from 1-12
    random_turn_option = i


    # REGULAR TURNS
    if random_turn_option == "F":  # front turn
        temp1 = top[6]
        temp2 = top[7]
        temp3 = top[8]

        top[6] = left[8]
        top[7] = left[5]
        top[8] = left[2]

        left[8] = bottom[2]
        left[5] = bottom[1]
        left[2] = bottom[0]

        bottom[2] = right[0]
        bottom[1] = right[3]
        bottom[0] = right[6]

        right[0] = temp1
        right[3] = temp2
        right[6] = temp3

        temp4 = front[0]
        temp5 = front[1]
        temp6 = front[2]

        front[0] = front[6]
        front[6] = front[8]
        front[8] = temp6
        front[1] = front[3]
        front[3] = front[7]
        front[7] = front[5]
        front[5] = temp5
        front[2] = temp4

    elif random_turn_option == "F'" :  # front inverted
        temp1 = top[6]
        temp2 = top[7]
        temp3 = top[8]

        top[6] = right[0]
        top[7] = right[3]
        top[8] = right[6]

        right[0] = bottom[2]
        right[3] = bottom[1]
        right[6] = bottom[0]

        bottom[2] = left[8]
        bottom[1] = left[5]
        bottom[0] = left[2]

        left[8] = temp1
        left[5] = temp2
        left[2] = temp3

        temp4 = front[0]
        temp5 = front[1]
        temp6 = front[2]

        front[0] = temp6
        front[2] = front[8]
        front[8] = front[6]
        front[6] = temp4
        front[1] = front[5]
        front[5] = front[7]
        front[7] = front[3]
        front[3] = temp5

    elif random_turn_option == "D":  # bottom turn
        temp1 = front[6]
        temp2 = front[7]
        temp3 = front[8]

        front[6] = left[6]
        front[7] = left[7]
        front[8] = left[8]

        left[6] = back[2]
        left[7] = back[1]
        left[8] = back[0]

        back[2] = right[6]
        back[1] = right[7]
        back[0] = right[8]

        right[6] = temp1
        right[7] = temp2
        right[8] = temp3

        temp4 = bottom[0]
        temp5 = bottom[1]
        temp6 = bottom[2]

        bottom[0] = bottom[6]
        bottom[6] = bottom[8]
        bottom[8] = temp6
        bottom[1] = bottom[3]
        bottom[3] = bottom[7]
        bottom[7] = bottom[5]
        bottom[5] = temp5
        bottom[2] = temp4

    elif random_turn_option == "D'":  # bottom turn inverted
        temp1 = front[6]
        temp2 = front[7]
        temp3 = front[8]

        front[6] = right[6]
        front[7] = right[7]
        front[8] = right[8]

        right[6] = back[0]
        right[7] = back[1]
        right[8] = back[2]

        back[2] = left[6]
        back[1] = left[7]
        back[0] = left[8]

        right[6] = temp1
        right[7] = temp2
        right[8] = temp3

        temp4 = bottom[0]
        temp5 = bottom[1]
        temp6 = bottom[2]

        bottom[0] = temp6
        bottom[2] = bottom[8]
        bottom[8] = bottom[6]
        bottom[6] = temp4
        bottom[1] = bottom[5]
        bottom[5] = bottom[7]
        bottom[7] = bottom[3]
        bottom[3] = temp5

    elif random_turn_option == "R":  # right turn
        temp1 = front[2]
        temp2 = front[5]
        temp3 = front[8]

        front[2] = bottom[2]
        front[5] = bottom[5]
        front[8] = bottom[8]

        bottom[2] = back[2]
        bottom[5] = back[5]
        bottom[8] = back[8]

        back[2] = top[2]
        back[5] = top[5]
        back[8] = top[8]

        top[2] = temp1
        top[5] = temp2
        top[8] = temp3

        temp4 = right[0]
        temp5 = right[1]
        temp6 = right[2]

        right[0] = right[6]
        right[6] = right[8]
        right[8] = temp6
        right[2] = temp4
        right[1] = right[3]
        right[3] = right[7]
        right[7] = right[5]
        right[5] = temp5

    elif random_turn_option == "R'":  # right turn inverted
        temp1 = front[2]
        temp2 = front[5]
        temp3 = front[8]

        front[2] = top[2]
        front[5] = top[5]
        front[8] = top[8]

        top[2] = back[2]
        top[5] = back[5]
        top[8] = back[8]

        back[2] = bottom[2]
        back[5] = bottom[5]
        back[8] = bottom[8]

        bottom[2] = temp1
        bottom[5] = temp2
        bottom[8] = temp3

        temp4 = right[0]
        temp5 = right[1]
        temp6 = right[2]

        right[0] = temp6
        right[2] = right[8]
        right[8] = right[6]
        right[6] = temp4
        right[1] = right[5]
        right[5] = right[7]
        right[7] = right[3]
        right[3] = temp5

    elif random_turn_option == "B":  # back turn
        temp1 = bottom[6]
        temp2 = bottom[7]
        temp3 = bottom[8]

        bottom[6] = left[0]
        bottom[7] = left[3]
        bottom[8] = left[6]

        left[0] = top[2]
        left[3] = top[1]
        left[6] = top[0]

        top[2] = right[8]
        top[1] = right[5]
        top[0] = right[2]

        right[8] = temp1
        right[5] = temp2
        right[2] = temp3

        temp4 = back[0]
        temp5 = back[1]
        temp6 = back[2]

        back[0] = back[6]
        back[6] = back[8]
        back[8] = temp6
        back[2] = temp4
        back[1] = back[3]
        back[3] = back[7]
        back[7] = back[5]
        back[5] = temp5

    elif random_turn_option == "B'":  # back turn inverted
        temp1 = bottom[6]
        temp2 = bottom[7]
        temp3 = bottom[8]

        bottom[6] = right[8]
        bottom[7] = right[5]
        bottom[8] = right[2]

        right[8] = top[0]
        right[5] = top[1]
        right[2] = top[2]

        top[2] = left[0]
        top[1] = left[3]
        top[0] = left[6]

        left[0] = temp1
        left[3] = temp2
        left[6] = temp3

        temp4 = back[0]
        temp5 = back[1]
        temp6 = back[2]

        back[0] = temp6
        back[2] = back[8]
        back[8] = back[6]
        back[6] = temp4
        back[1] = back[5]
        back[5] = back[7]
        back[7] = back[3]
        back[3] = temp5

    elif random_turn_option == "U":  # top turn
        temp1 = front[0]
        temp2 = front[1]
        temp3 = front[2]

        front[0] = right[0]
        front[1] = right[1]
        front[2] = right[2]

        right[0] = back[8]
        right[1] = back[7]
        right[2] = back[6]

        back[8] = left[0]
        back[7] = left[1]
        back[6] = left[2]

        left[0] = temp1
        left[1] = temp2
        left[2] = temp3

        temp4 = top[0]
        temp5 = top[1]
        temp6 = top[2]

        top[0] = top[6]
        top[6] = top[8]
        top[8] = temp6
        top[1] = top[3]
        top[3] = top[7]
        top[7] = top[5]
        top[5] = temp5
        top[2] = temp4

    elif random_turn_option == "U'":  # top turn inverted
        temp1 = front[0]
        temp2 = front[1]
        temp3 = front[2]

        front[0] = left[0]
        front[1] = left[1]
        front[2] = left[2]

        left[0] = back[8]
        left[1] = back[7]
        left[2] = back[6]

        back[8] = right[0]
        back[7] = right[1]
        back[6] = right[2]

        right[0] = temp1
        right[1] = temp2
        right[2] = temp3

        temp4 = top[0]
        temp5 = top[1]
        temp6 = top[2]

        top[0] = temp6
        top[2] = top[8]
        top[8] = top[6]
        top[6] = temp4
        top[1] = top[5]
        top[5] = top[7]
        top[3] = temp5
        top[7] = top[3]

    elif random_turn_option == "L":  # left turn
        temp1 = front[0]
        temp2 = front[3]
        temp3 = front[6]

        front[0] = top[0]
        front[3] = top[3]
        front[6] = top[6]

        top[0] = back[0]
        top[3] = back[3]
        top[6] = back[6]

        back[0] = bottom[0]
        back[3] = bottom[3]
        back[6] = bottom[6]

        bottom[0] = temp1
        bottom[3] = temp2
        bottom[6] = temp3

        temp4 = left[0]
        temp5 = left[1]
        temp6 = left[2]

        left[0] = left[6]
        left[6] = left[8]
        left[8] = temp6
        left[1] = left[3]
        left[3] = left[7]
        left[7] = left[5]
        left[5] = temp5
        left[2] = temp4

    elif random_turn_option == "L'":  # left turn inverted
        temp1 = front[0]
        temp2 = front[3]
        temp3 = front[6]

        front[0] = bottom[0]
        front[3] = bottom[3]
        front[6] = bottom[6]

        bottom[0] = back[0]
        bottom[3] = back[3]
        bottom[6] = back[6]

        back[0] = top[0]
        back[3] = top[3]
        back[6] = top[6]

        top[0] = temp1
        top[3] = temp2
        top[6] = temp3

        temp4 = left[0]
        temp5 = left[1]
        temp6 = left[2]

        left[0] = temp6
        left[2] = left[8]
        left[8] = left[6]
        left[6] = temp4
        left[1] = left[5]
        left[5] = left[7]
        left[7] = left[3]
        left[3] = temp5

    
    count += 1
print_cube()
