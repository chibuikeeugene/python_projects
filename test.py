
def calculate_love_score(name1:str, name2:str):
    t_counter = 0
    r_counter = 0
    u_counter = 0 
    e_counter = 0 
    l_counter = 0 
    o_counter = 0 
    v_counter = 0 
    e_counter = 0

    names =  name1 + name2
    for letter in names:
        if letter == 't':
            t_counter += 1
        elif letter == 'r':
            r_counter += 1
        elif letter == 'u':
            u_counter += 1
        elif letter == 'e':
            e_counter += 1
        elif letter == 'l':
            l_counter += 1
        elif letter == 'o':
            o_counter += 1
        elif letter == 'v':
            v_counter += 1
        elif letter == 'e':
            e_counter += 1
        else:
            pass

    true_score = t_counter + r_counter + u_counter + e_counter
    love_score = l_counter + o_counter + v_counter + e_counter

    print(f"{str(true_score)}" + f"{str(love_score)}")


calculate_love_score(name1='musa', name2='eddy')