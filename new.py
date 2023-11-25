while(True):
    try:

        list_input = [ int(i) for i in input().split(" ")]
        # list_input = [ str(i) for i in input().split("A")]
        # print(list_input[5])
        Velocity = list_input[0]
        Time = list_input[1]
        Displacement = Velocity*(2*Time)
        print(Displacement)
        
    except EOFError:
            break
