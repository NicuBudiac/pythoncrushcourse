VRs = []
for VR in range(24,88):
    VRs.append(VR)
    print (""" sudo ip link add link eth1 name eth1.{} type vlan id []
    sudo ip link set dev eth1.{} up
    sudo ip address add 10.166.{}.130/25 dev eth1.{}
    sudo ip route add 172.{}. 255.0/24 gw 10.166.{}.129
    """)
