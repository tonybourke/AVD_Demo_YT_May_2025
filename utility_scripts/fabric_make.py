rack_counter = 1
leaf_counter = 1
spine_int_counter = 2
while rack_counter < 25:
    print(f"    - group: RACK{rack_counter}")
    print(f"      nodes:")
    rack_counter += 1
    odd_even_counter = 1
    while odd_even_counter < 3:
        leaf_id = leaf_counter + 10
        print(f"        - name: leaf{leaf_counter}")
        print(f"          id: {leaf_id}")
        print(f"          mgmt_ip: 172.20.20.{leaf_id}/24")
        print(f"          uplink_switch_interfaces: [Ethernet{spine_int_counter}, Ethernet{spine_int_counter}, Ethernet{spine_int_counter}]")
        leaf_counter += 1
        spine_int_counter += 1
        odd_even_counter += 1