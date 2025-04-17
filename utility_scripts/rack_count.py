rack_counter = 1
leaf_counter = 1
while rack_counter < 25:
    print(f"            RACK{rack_counter}:")
    print(f"              hosts:")
    rack_counter += 1
    odd_even_counter = 1
    while odd_even_counter < 3:
        print(f"                leaf{leaf_counter}:")
        leaf_counter += 1
        odd_even_counter += 1
    
   