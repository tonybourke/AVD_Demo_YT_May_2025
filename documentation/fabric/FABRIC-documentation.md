# FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | l3leaf | leaf1 | 172.20.20.11/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf2 | 172.20.20.12/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf3 | 172.20.20.13/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf4 | 172.20.20.14/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf5 | 172.20.20.15/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf6 | 172.20.20.16/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf7 | 172.20.20.17/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf8 | 172.20.20.18/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf9 | 172.20.20.19/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf10 | 172.20.20.20/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf11 | 172.20.20.21/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf12 | 172.20.20.22/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf13 | 172.20.20.23/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf14 | 172.20.20.24/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf15 | 172.20.20.25/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf16 | 172.20.20.26/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf17 | 172.20.20.27/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf18 | 172.20.20.28/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf19 | 172.20.20.29/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf20 | 172.20.20.30/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf21 | 172.20.20.31/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf22 | 172.20.20.32/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf23 | 172.20.20.33/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf24 | 172.20.20.34/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf25 | 172.20.20.35/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf26 | 172.20.20.36/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf27 | 172.20.20.37/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf28 | 172.20.20.38/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf29 | 172.20.20.39/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf30 | 172.20.20.40/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf31 | 172.20.20.41/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf32 | 172.20.20.42/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf33 | 172.20.20.43/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf34 | 172.20.20.44/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf35 | 172.20.20.45/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf36 | 172.20.20.46/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf37 | 172.20.20.47/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf38 | 172.20.20.48/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf39 | 172.20.20.49/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf40 | 172.20.20.50/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf41 | 172.20.20.51/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf42 | 172.20.20.52/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf43 | 172.20.20.53/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf44 | 172.20.20.54/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf45 | 172.20.20.55/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf46 | 172.20.20.56/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf47 | 172.20.20.57/24 | cEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf48 | 172.20.20.58/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | spine1 | 172.20.20.101/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | spine2 | 172.20.20.102/24 | cEOS-lab | Provisioned | - |
| FABRIC | spine | spine3 | 172.20.20.103/24 | cEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | leaf1 | Ethernet1 | mlag_peer | leaf2 | Ethernet1 |
| l3leaf | leaf1 | Ethernet2 | mlag_peer | leaf2 | Ethernet2 |
| l3leaf | leaf1 | Ethernet3 | spine | spine1 | Ethernet2 |
| l3leaf | leaf1 | Ethernet4 | spine | spine2 | Ethernet2 |
| l3leaf | leaf1 | Ethernet5 | spine | spine3 | Ethernet2 |
| l3leaf | leaf2 | Ethernet3 | spine | spine1 | Ethernet3 |
| l3leaf | leaf2 | Ethernet4 | spine | spine2 | Ethernet3 |
| l3leaf | leaf2 | Ethernet5 | spine | spine3 | Ethernet3 |
| l3leaf | leaf3 | Ethernet1 | mlag_peer | leaf4 | Ethernet1 |
| l3leaf | leaf3 | Ethernet2 | mlag_peer | leaf4 | Ethernet2 |
| l3leaf | leaf3 | Ethernet3 | spine | spine1 | Ethernet4 |
| l3leaf | leaf3 | Ethernet4 | spine | spine2 | Ethernet4 |
| l3leaf | leaf3 | Ethernet5 | spine | spine3 | Ethernet4 |
| l3leaf | leaf4 | Ethernet3 | spine | spine1 | Ethernet5 |
| l3leaf | leaf4 | Ethernet4 | spine | spine2 | Ethernet5 |
| l3leaf | leaf4 | Ethernet5 | spine | spine3 | Ethernet5 |
| l3leaf | leaf5 | Ethernet1 | mlag_peer | leaf6 | Ethernet1 |
| l3leaf | leaf5 | Ethernet2 | mlag_peer | leaf6 | Ethernet2 |
| l3leaf | leaf5 | Ethernet3 | spine | spine1 | Ethernet6 |
| l3leaf | leaf5 | Ethernet4 | spine | spine2 | Ethernet6 |
| l3leaf | leaf5 | Ethernet5 | spine | spine3 | Ethernet6 |
| l3leaf | leaf6 | Ethernet3 | spine | spine1 | Ethernet7 |
| l3leaf | leaf6 | Ethernet4 | spine | spine2 | Ethernet7 |
| l3leaf | leaf6 | Ethernet5 | spine | spine3 | Ethernet7 |
| l3leaf | leaf7 | Ethernet1 | mlag_peer | leaf8 | Ethernet1 |
| l3leaf | leaf7 | Ethernet2 | mlag_peer | leaf8 | Ethernet2 |
| l3leaf | leaf7 | Ethernet3 | spine | spine1 | Ethernet8 |
| l3leaf | leaf7 | Ethernet4 | spine | spine2 | Ethernet8 |
| l3leaf | leaf7 | Ethernet5 | spine | spine3 | Ethernet8 |
| l3leaf | leaf8 | Ethernet3 | spine | spine1 | Ethernet9 |
| l3leaf | leaf8 | Ethernet4 | spine | spine2 | Ethernet9 |
| l3leaf | leaf8 | Ethernet5 | spine | spine3 | Ethernet9 |
| l3leaf | leaf9 | Ethernet1 | mlag_peer | leaf10 | Ethernet1 |
| l3leaf | leaf9 | Ethernet2 | mlag_peer | leaf10 | Ethernet2 |
| l3leaf | leaf9 | Ethernet3 | spine | spine1 | Ethernet10 |
| l3leaf | leaf9 | Ethernet4 | spine | spine2 | Ethernet10 |
| l3leaf | leaf9 | Ethernet5 | spine | spine3 | Ethernet10 |
| l3leaf | leaf10 | Ethernet3 | spine | spine1 | Ethernet11 |
| l3leaf | leaf10 | Ethernet4 | spine | spine2 | Ethernet11 |
| l3leaf | leaf10 | Ethernet5 | spine | spine3 | Ethernet11 |
| l3leaf | leaf11 | Ethernet1 | mlag_peer | leaf12 | Ethernet1 |
| l3leaf | leaf11 | Ethernet2 | mlag_peer | leaf12 | Ethernet2 |
| l3leaf | leaf11 | Ethernet3 | spine | spine1 | Ethernet12 |
| l3leaf | leaf11 | Ethernet4 | spine | spine2 | Ethernet12 |
| l3leaf | leaf11 | Ethernet5 | spine | spine3 | Ethernet12 |
| l3leaf | leaf12 | Ethernet3 | spine | spine1 | Ethernet13 |
| l3leaf | leaf12 | Ethernet4 | spine | spine2 | Ethernet13 |
| l3leaf | leaf12 | Ethernet5 | spine | spine3 | Ethernet13 |
| l3leaf | leaf13 | Ethernet1 | mlag_peer | leaf14 | Ethernet1 |
| l3leaf | leaf13 | Ethernet2 | mlag_peer | leaf14 | Ethernet2 |
| l3leaf | leaf13 | Ethernet3 | spine | spine1 | Ethernet14 |
| l3leaf | leaf13 | Ethernet4 | spine | spine2 | Ethernet14 |
| l3leaf | leaf13 | Ethernet5 | spine | spine3 | Ethernet14 |
| l3leaf | leaf14 | Ethernet3 | spine | spine1 | Ethernet15 |
| l3leaf | leaf14 | Ethernet4 | spine | spine2 | Ethernet15 |
| l3leaf | leaf14 | Ethernet5 | spine | spine3 | Ethernet15 |
| l3leaf | leaf15 | Ethernet1 | mlag_peer | leaf16 | Ethernet1 |
| l3leaf | leaf15 | Ethernet2 | mlag_peer | leaf16 | Ethernet2 |
| l3leaf | leaf15 | Ethernet3 | spine | spine1 | Ethernet16 |
| l3leaf | leaf15 | Ethernet4 | spine | spine2 | Ethernet16 |
| l3leaf | leaf15 | Ethernet5 | spine | spine3 | Ethernet16 |
| l3leaf | leaf16 | Ethernet3 | spine | spine1 | Ethernet17 |
| l3leaf | leaf16 | Ethernet4 | spine | spine2 | Ethernet17 |
| l3leaf | leaf16 | Ethernet5 | spine | spine3 | Ethernet17 |
| l3leaf | leaf17 | Ethernet1 | mlag_peer | leaf18 | Ethernet1 |
| l3leaf | leaf17 | Ethernet2 | mlag_peer | leaf18 | Ethernet2 |
| l3leaf | leaf17 | Ethernet3 | spine | spine1 | Ethernet18 |
| l3leaf | leaf17 | Ethernet4 | spine | spine2 | Ethernet18 |
| l3leaf | leaf17 | Ethernet5 | spine | spine3 | Ethernet18 |
| l3leaf | leaf18 | Ethernet3 | spine | spine1 | Ethernet19 |
| l3leaf | leaf18 | Ethernet4 | spine | spine2 | Ethernet19 |
| l3leaf | leaf18 | Ethernet5 | spine | spine3 | Ethernet19 |
| l3leaf | leaf19 | Ethernet1 | mlag_peer | leaf20 | Ethernet1 |
| l3leaf | leaf19 | Ethernet2 | mlag_peer | leaf20 | Ethernet2 |
| l3leaf | leaf19 | Ethernet3 | spine | spine1 | Ethernet20 |
| l3leaf | leaf19 | Ethernet4 | spine | spine2 | Ethernet20 |
| l3leaf | leaf19 | Ethernet5 | spine | spine3 | Ethernet20 |
| l3leaf | leaf20 | Ethernet3 | spine | spine1 | Ethernet21 |
| l3leaf | leaf20 | Ethernet4 | spine | spine2 | Ethernet21 |
| l3leaf | leaf20 | Ethernet5 | spine | spine3 | Ethernet21 |
| l3leaf | leaf21 | Ethernet1 | mlag_peer | leaf22 | Ethernet1 |
| l3leaf | leaf21 | Ethernet2 | mlag_peer | leaf22 | Ethernet2 |
| l3leaf | leaf21 | Ethernet3 | spine | spine1 | Ethernet22 |
| l3leaf | leaf21 | Ethernet4 | spine | spine2 | Ethernet22 |
| l3leaf | leaf21 | Ethernet5 | spine | spine3 | Ethernet22 |
| l3leaf | leaf22 | Ethernet3 | spine | spine1 | Ethernet23 |
| l3leaf | leaf22 | Ethernet4 | spine | spine2 | Ethernet23 |
| l3leaf | leaf22 | Ethernet5 | spine | spine3 | Ethernet23 |
| l3leaf | leaf23 | Ethernet1 | mlag_peer | leaf24 | Ethernet1 |
| l3leaf | leaf23 | Ethernet2 | mlag_peer | leaf24 | Ethernet2 |
| l3leaf | leaf23 | Ethernet3 | spine | spine1 | Ethernet24 |
| l3leaf | leaf23 | Ethernet4 | spine | spine2 | Ethernet24 |
| l3leaf | leaf23 | Ethernet5 | spine | spine3 | Ethernet24 |
| l3leaf | leaf24 | Ethernet3 | spine | spine1 | Ethernet25 |
| l3leaf | leaf24 | Ethernet4 | spine | spine2 | Ethernet25 |
| l3leaf | leaf24 | Ethernet5 | spine | spine3 | Ethernet25 |
| l3leaf | leaf25 | Ethernet1 | mlag_peer | leaf26 | Ethernet1 |
| l3leaf | leaf25 | Ethernet2 | mlag_peer | leaf26 | Ethernet2 |
| l3leaf | leaf25 | Ethernet3 | spine | spine1 | Ethernet26 |
| l3leaf | leaf25 | Ethernet4 | spine | spine2 | Ethernet26 |
| l3leaf | leaf25 | Ethernet5 | spine | spine3 | Ethernet26 |
| l3leaf | leaf26 | Ethernet3 | spine | spine1 | Ethernet27 |
| l3leaf | leaf26 | Ethernet4 | spine | spine2 | Ethernet27 |
| l3leaf | leaf26 | Ethernet5 | spine | spine3 | Ethernet27 |
| l3leaf | leaf27 | Ethernet1 | mlag_peer | leaf28 | Ethernet1 |
| l3leaf | leaf27 | Ethernet2 | mlag_peer | leaf28 | Ethernet2 |
| l3leaf | leaf27 | Ethernet3 | spine | spine1 | Ethernet28 |
| l3leaf | leaf27 | Ethernet4 | spine | spine2 | Ethernet28 |
| l3leaf | leaf27 | Ethernet5 | spine | spine3 | Ethernet28 |
| l3leaf | leaf28 | Ethernet3 | spine | spine1 | Ethernet29 |
| l3leaf | leaf28 | Ethernet4 | spine | spine2 | Ethernet29 |
| l3leaf | leaf28 | Ethernet5 | spine | spine3 | Ethernet29 |
| l3leaf | leaf29 | Ethernet1 | mlag_peer | leaf30 | Ethernet1 |
| l3leaf | leaf29 | Ethernet2 | mlag_peer | leaf30 | Ethernet2 |
| l3leaf | leaf29 | Ethernet3 | spine | spine1 | Ethernet30 |
| l3leaf | leaf29 | Ethernet4 | spine | spine2 | Ethernet30 |
| l3leaf | leaf29 | Ethernet5 | spine | spine3 | Ethernet30 |
| l3leaf | leaf30 | Ethernet3 | spine | spine1 | Ethernet31 |
| l3leaf | leaf30 | Ethernet4 | spine | spine2 | Ethernet31 |
| l3leaf | leaf30 | Ethernet5 | spine | spine3 | Ethernet31 |
| l3leaf | leaf31 | Ethernet1 | mlag_peer | leaf32 | Ethernet1 |
| l3leaf | leaf31 | Ethernet2 | mlag_peer | leaf32 | Ethernet2 |
| l3leaf | leaf31 | Ethernet3 | spine | spine1 | Ethernet32 |
| l3leaf | leaf31 | Ethernet4 | spine | spine2 | Ethernet32 |
| l3leaf | leaf31 | Ethernet5 | spine | spine3 | Ethernet32 |
| l3leaf | leaf32 | Ethernet3 | spine | spine1 | Ethernet33 |
| l3leaf | leaf32 | Ethernet4 | spine | spine2 | Ethernet33 |
| l3leaf | leaf32 | Ethernet5 | spine | spine3 | Ethernet33 |
| l3leaf | leaf33 | Ethernet1 | mlag_peer | leaf34 | Ethernet1 |
| l3leaf | leaf33 | Ethernet2 | mlag_peer | leaf34 | Ethernet2 |
| l3leaf | leaf33 | Ethernet3 | spine | spine1 | Ethernet34 |
| l3leaf | leaf33 | Ethernet4 | spine | spine2 | Ethernet34 |
| l3leaf | leaf33 | Ethernet5 | spine | spine3 | Ethernet34 |
| l3leaf | leaf34 | Ethernet3 | spine | spine1 | Ethernet35 |
| l3leaf | leaf34 | Ethernet4 | spine | spine2 | Ethernet35 |
| l3leaf | leaf34 | Ethernet5 | spine | spine3 | Ethernet35 |
| l3leaf | leaf35 | Ethernet1 | mlag_peer | leaf36 | Ethernet1 |
| l3leaf | leaf35 | Ethernet2 | mlag_peer | leaf36 | Ethernet2 |
| l3leaf | leaf35 | Ethernet3 | spine | spine1 | Ethernet36 |
| l3leaf | leaf35 | Ethernet4 | spine | spine2 | Ethernet36 |
| l3leaf | leaf35 | Ethernet5 | spine | spine3 | Ethernet36 |
| l3leaf | leaf36 | Ethernet3 | spine | spine1 | Ethernet37 |
| l3leaf | leaf36 | Ethernet4 | spine | spine2 | Ethernet37 |
| l3leaf | leaf36 | Ethernet5 | spine | spine3 | Ethernet37 |
| l3leaf | leaf37 | Ethernet1 | mlag_peer | leaf38 | Ethernet1 |
| l3leaf | leaf37 | Ethernet2 | mlag_peer | leaf38 | Ethernet2 |
| l3leaf | leaf37 | Ethernet3 | spine | spine1 | Ethernet38 |
| l3leaf | leaf37 | Ethernet4 | spine | spine2 | Ethernet38 |
| l3leaf | leaf37 | Ethernet5 | spine | spine3 | Ethernet38 |
| l3leaf | leaf38 | Ethernet3 | spine | spine1 | Ethernet39 |
| l3leaf | leaf38 | Ethernet4 | spine | spine2 | Ethernet39 |
| l3leaf | leaf38 | Ethernet5 | spine | spine3 | Ethernet39 |
| l3leaf | leaf39 | Ethernet1 | mlag_peer | leaf40 | Ethernet1 |
| l3leaf | leaf39 | Ethernet2 | mlag_peer | leaf40 | Ethernet2 |
| l3leaf | leaf39 | Ethernet3 | spine | spine1 | Ethernet40 |
| l3leaf | leaf39 | Ethernet4 | spine | spine2 | Ethernet40 |
| l3leaf | leaf39 | Ethernet5 | spine | spine3 | Ethernet40 |
| l3leaf | leaf40 | Ethernet3 | spine | spine1 | Ethernet41 |
| l3leaf | leaf40 | Ethernet4 | spine | spine2 | Ethernet41 |
| l3leaf | leaf40 | Ethernet5 | spine | spine3 | Ethernet41 |
| l3leaf | leaf41 | Ethernet1 | mlag_peer | leaf42 | Ethernet1 |
| l3leaf | leaf41 | Ethernet2 | mlag_peer | leaf42 | Ethernet2 |
| l3leaf | leaf41 | Ethernet3 | spine | spine1 | Ethernet42 |
| l3leaf | leaf41 | Ethernet4 | spine | spine2 | Ethernet42 |
| l3leaf | leaf41 | Ethernet5 | spine | spine3 | Ethernet42 |
| l3leaf | leaf42 | Ethernet3 | spine | spine1 | Ethernet43 |
| l3leaf | leaf42 | Ethernet4 | spine | spine2 | Ethernet43 |
| l3leaf | leaf42 | Ethernet5 | spine | spine3 | Ethernet43 |
| l3leaf | leaf43 | Ethernet1 | mlag_peer | leaf44 | Ethernet1 |
| l3leaf | leaf43 | Ethernet2 | mlag_peer | leaf44 | Ethernet2 |
| l3leaf | leaf43 | Ethernet3 | spine | spine1 | Ethernet44 |
| l3leaf | leaf43 | Ethernet4 | spine | spine2 | Ethernet44 |
| l3leaf | leaf43 | Ethernet5 | spine | spine3 | Ethernet44 |
| l3leaf | leaf44 | Ethernet3 | spine | spine1 | Ethernet45 |
| l3leaf | leaf44 | Ethernet4 | spine | spine2 | Ethernet45 |
| l3leaf | leaf44 | Ethernet5 | spine | spine3 | Ethernet45 |
| l3leaf | leaf45 | Ethernet1 | mlag_peer | leaf46 | Ethernet1 |
| l3leaf | leaf45 | Ethernet2 | mlag_peer | leaf46 | Ethernet2 |
| l3leaf | leaf45 | Ethernet3 | spine | spine1 | Ethernet46 |
| l3leaf | leaf45 | Ethernet4 | spine | spine2 | Ethernet46 |
| l3leaf | leaf45 | Ethernet5 | spine | spine3 | Ethernet46 |
| l3leaf | leaf46 | Ethernet3 | spine | spine1 | Ethernet47 |
| l3leaf | leaf46 | Ethernet4 | spine | spine2 | Ethernet47 |
| l3leaf | leaf46 | Ethernet5 | spine | spine3 | Ethernet47 |
| l3leaf | leaf47 | Ethernet1 | mlag_peer | leaf48 | Ethernet1 |
| l3leaf | leaf47 | Ethernet2 | mlag_peer | leaf48 | Ethernet2 |
| l3leaf | leaf47 | Ethernet3 | spine | spine1 | Ethernet48 |
| l3leaf | leaf47 | Ethernet4 | spine | spine2 | Ethernet48 |
| l3leaf | leaf47 | Ethernet5 | spine | spine3 | Ethernet48 |
| l3leaf | leaf48 | Ethernet3 | spine | spine1 | Ethernet49 |
| l3leaf | leaf48 | Ethernet4 | spine | spine2 | Ethernet49 |
| l3leaf | leaf48 | Ethernet5 | spine | spine3 | Ethernet49 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.0.0/22 | 1024 | 288 | 28.13 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| leaf1 | Ethernet3 | 10.255.0.61/31 | spine1 | Ethernet2 | 10.255.0.60/31 |
| leaf1 | Ethernet4 | 10.255.0.63/31 | spine2 | Ethernet2 | 10.255.0.62/31 |
| leaf1 | Ethernet5 | 10.255.0.65/31 | spine3 | Ethernet2 | 10.255.0.64/31 |
| leaf2 | Ethernet3 | 10.255.0.67/31 | spine1 | Ethernet3 | 10.255.0.66/31 |
| leaf2 | Ethernet4 | 10.255.0.69/31 | spine2 | Ethernet3 | 10.255.0.68/31 |
| leaf2 | Ethernet5 | 10.255.0.71/31 | spine3 | Ethernet3 | 10.255.0.70/31 |
| leaf3 | Ethernet3 | 10.255.0.73/31 | spine1 | Ethernet4 | 10.255.0.72/31 |
| leaf3 | Ethernet4 | 10.255.0.75/31 | spine2 | Ethernet4 | 10.255.0.74/31 |
| leaf3 | Ethernet5 | 10.255.0.77/31 | spine3 | Ethernet4 | 10.255.0.76/31 |
| leaf4 | Ethernet3 | 10.255.0.79/31 | spine1 | Ethernet5 | 10.255.0.78/31 |
| leaf4 | Ethernet4 | 10.255.0.81/31 | spine2 | Ethernet5 | 10.255.0.80/31 |
| leaf4 | Ethernet5 | 10.255.0.83/31 | spine3 | Ethernet5 | 10.255.0.82/31 |
| leaf5 | Ethernet3 | 10.255.0.85/31 | spine1 | Ethernet6 | 10.255.0.84/31 |
| leaf5 | Ethernet4 | 10.255.0.87/31 | spine2 | Ethernet6 | 10.255.0.86/31 |
| leaf5 | Ethernet5 | 10.255.0.89/31 | spine3 | Ethernet6 | 10.255.0.88/31 |
| leaf6 | Ethernet3 | 10.255.0.91/31 | spine1 | Ethernet7 | 10.255.0.90/31 |
| leaf6 | Ethernet4 | 10.255.0.93/31 | spine2 | Ethernet7 | 10.255.0.92/31 |
| leaf6 | Ethernet5 | 10.255.0.95/31 | spine3 | Ethernet7 | 10.255.0.94/31 |
| leaf7 | Ethernet3 | 10.255.0.97/31 | spine1 | Ethernet8 | 10.255.0.96/31 |
| leaf7 | Ethernet4 | 10.255.0.99/31 | spine2 | Ethernet8 | 10.255.0.98/31 |
| leaf7 | Ethernet5 | 10.255.0.101/31 | spine3 | Ethernet8 | 10.255.0.100/31 |
| leaf8 | Ethernet3 | 10.255.0.103/31 | spine1 | Ethernet9 | 10.255.0.102/31 |
| leaf8 | Ethernet4 | 10.255.0.105/31 | spine2 | Ethernet9 | 10.255.0.104/31 |
| leaf8 | Ethernet5 | 10.255.0.107/31 | spine3 | Ethernet9 | 10.255.0.106/31 |
| leaf9 | Ethernet3 | 10.255.0.109/31 | spine1 | Ethernet10 | 10.255.0.108/31 |
| leaf9 | Ethernet4 | 10.255.0.111/31 | spine2 | Ethernet10 | 10.255.0.110/31 |
| leaf9 | Ethernet5 | 10.255.0.113/31 | spine3 | Ethernet10 | 10.255.0.112/31 |
| leaf10 | Ethernet3 | 10.255.0.115/31 | spine1 | Ethernet11 | 10.255.0.114/31 |
| leaf10 | Ethernet4 | 10.255.0.117/31 | spine2 | Ethernet11 | 10.255.0.116/31 |
| leaf10 | Ethernet5 | 10.255.0.119/31 | spine3 | Ethernet11 | 10.255.0.118/31 |
| leaf11 | Ethernet3 | 10.255.0.121/31 | spine1 | Ethernet12 | 10.255.0.120/31 |
| leaf11 | Ethernet4 | 10.255.0.123/31 | spine2 | Ethernet12 | 10.255.0.122/31 |
| leaf11 | Ethernet5 | 10.255.0.125/31 | spine3 | Ethernet12 | 10.255.0.124/31 |
| leaf12 | Ethernet3 | 10.255.0.127/31 | spine1 | Ethernet13 | 10.255.0.126/31 |
| leaf12 | Ethernet4 | 10.255.0.129/31 | spine2 | Ethernet13 | 10.255.0.128/31 |
| leaf12 | Ethernet5 | 10.255.0.131/31 | spine3 | Ethernet13 | 10.255.0.130/31 |
| leaf13 | Ethernet3 | 10.255.0.133/31 | spine1 | Ethernet14 | 10.255.0.132/31 |
| leaf13 | Ethernet4 | 10.255.0.135/31 | spine2 | Ethernet14 | 10.255.0.134/31 |
| leaf13 | Ethernet5 | 10.255.0.137/31 | spine3 | Ethernet14 | 10.255.0.136/31 |
| leaf14 | Ethernet3 | 10.255.0.139/31 | spine1 | Ethernet15 | 10.255.0.138/31 |
| leaf14 | Ethernet4 | 10.255.0.141/31 | spine2 | Ethernet15 | 10.255.0.140/31 |
| leaf14 | Ethernet5 | 10.255.0.143/31 | spine3 | Ethernet15 | 10.255.0.142/31 |
| leaf15 | Ethernet3 | 10.255.0.145/31 | spine1 | Ethernet16 | 10.255.0.144/31 |
| leaf15 | Ethernet4 | 10.255.0.147/31 | spine2 | Ethernet16 | 10.255.0.146/31 |
| leaf15 | Ethernet5 | 10.255.0.149/31 | spine3 | Ethernet16 | 10.255.0.148/31 |
| leaf16 | Ethernet3 | 10.255.0.151/31 | spine1 | Ethernet17 | 10.255.0.150/31 |
| leaf16 | Ethernet4 | 10.255.0.153/31 | spine2 | Ethernet17 | 10.255.0.152/31 |
| leaf16 | Ethernet5 | 10.255.0.155/31 | spine3 | Ethernet17 | 10.255.0.154/31 |
| leaf17 | Ethernet3 | 10.255.0.157/31 | spine1 | Ethernet18 | 10.255.0.156/31 |
| leaf17 | Ethernet4 | 10.255.0.159/31 | spine2 | Ethernet18 | 10.255.0.158/31 |
| leaf17 | Ethernet5 | 10.255.0.161/31 | spine3 | Ethernet18 | 10.255.0.160/31 |
| leaf18 | Ethernet3 | 10.255.0.163/31 | spine1 | Ethernet19 | 10.255.0.162/31 |
| leaf18 | Ethernet4 | 10.255.0.165/31 | spine2 | Ethernet19 | 10.255.0.164/31 |
| leaf18 | Ethernet5 | 10.255.0.167/31 | spine3 | Ethernet19 | 10.255.0.166/31 |
| leaf19 | Ethernet3 | 10.255.0.169/31 | spine1 | Ethernet20 | 10.255.0.168/31 |
| leaf19 | Ethernet4 | 10.255.0.171/31 | spine2 | Ethernet20 | 10.255.0.170/31 |
| leaf19 | Ethernet5 | 10.255.0.173/31 | spine3 | Ethernet20 | 10.255.0.172/31 |
| leaf20 | Ethernet3 | 10.255.0.175/31 | spine1 | Ethernet21 | 10.255.0.174/31 |
| leaf20 | Ethernet4 | 10.255.0.177/31 | spine2 | Ethernet21 | 10.255.0.176/31 |
| leaf20 | Ethernet5 | 10.255.0.179/31 | spine3 | Ethernet21 | 10.255.0.178/31 |
| leaf21 | Ethernet3 | 10.255.0.181/31 | spine1 | Ethernet22 | 10.255.0.180/31 |
| leaf21 | Ethernet4 | 10.255.0.183/31 | spine2 | Ethernet22 | 10.255.0.182/31 |
| leaf21 | Ethernet5 | 10.255.0.185/31 | spine3 | Ethernet22 | 10.255.0.184/31 |
| leaf22 | Ethernet3 | 10.255.0.187/31 | spine1 | Ethernet23 | 10.255.0.186/31 |
| leaf22 | Ethernet4 | 10.255.0.189/31 | spine2 | Ethernet23 | 10.255.0.188/31 |
| leaf22 | Ethernet5 | 10.255.0.191/31 | spine3 | Ethernet23 | 10.255.0.190/31 |
| leaf23 | Ethernet3 | 10.255.0.193/31 | spine1 | Ethernet24 | 10.255.0.192/31 |
| leaf23 | Ethernet4 | 10.255.0.195/31 | spine2 | Ethernet24 | 10.255.0.194/31 |
| leaf23 | Ethernet5 | 10.255.0.197/31 | spine3 | Ethernet24 | 10.255.0.196/31 |
| leaf24 | Ethernet3 | 10.255.0.199/31 | spine1 | Ethernet25 | 10.255.0.198/31 |
| leaf24 | Ethernet4 | 10.255.0.201/31 | spine2 | Ethernet25 | 10.255.0.200/31 |
| leaf24 | Ethernet5 | 10.255.0.203/31 | spine3 | Ethernet25 | 10.255.0.202/31 |
| leaf25 | Ethernet3 | 10.255.0.205/31 | spine1 | Ethernet26 | 10.255.0.204/31 |
| leaf25 | Ethernet4 | 10.255.0.207/31 | spine2 | Ethernet26 | 10.255.0.206/31 |
| leaf25 | Ethernet5 | 10.255.0.209/31 | spine3 | Ethernet26 | 10.255.0.208/31 |
| leaf26 | Ethernet3 | 10.255.0.211/31 | spine1 | Ethernet27 | 10.255.0.210/31 |
| leaf26 | Ethernet4 | 10.255.0.213/31 | spine2 | Ethernet27 | 10.255.0.212/31 |
| leaf26 | Ethernet5 | 10.255.0.215/31 | spine3 | Ethernet27 | 10.255.0.214/31 |
| leaf27 | Ethernet3 | 10.255.0.217/31 | spine1 | Ethernet28 | 10.255.0.216/31 |
| leaf27 | Ethernet4 | 10.255.0.219/31 | spine2 | Ethernet28 | 10.255.0.218/31 |
| leaf27 | Ethernet5 | 10.255.0.221/31 | spine3 | Ethernet28 | 10.255.0.220/31 |
| leaf28 | Ethernet3 | 10.255.0.223/31 | spine1 | Ethernet29 | 10.255.0.222/31 |
| leaf28 | Ethernet4 | 10.255.0.225/31 | spine2 | Ethernet29 | 10.255.0.224/31 |
| leaf28 | Ethernet5 | 10.255.0.227/31 | spine3 | Ethernet29 | 10.255.0.226/31 |
| leaf29 | Ethernet3 | 10.255.0.229/31 | spine1 | Ethernet30 | 10.255.0.228/31 |
| leaf29 | Ethernet4 | 10.255.0.231/31 | spine2 | Ethernet30 | 10.255.0.230/31 |
| leaf29 | Ethernet5 | 10.255.0.233/31 | spine3 | Ethernet30 | 10.255.0.232/31 |
| leaf30 | Ethernet3 | 10.255.0.235/31 | spine1 | Ethernet31 | 10.255.0.234/31 |
| leaf30 | Ethernet4 | 10.255.0.237/31 | spine2 | Ethernet31 | 10.255.0.236/31 |
| leaf30 | Ethernet5 | 10.255.0.239/31 | spine3 | Ethernet31 | 10.255.0.238/31 |
| leaf31 | Ethernet3 | 10.255.0.241/31 | spine1 | Ethernet32 | 10.255.0.240/31 |
| leaf31 | Ethernet4 | 10.255.0.243/31 | spine2 | Ethernet32 | 10.255.0.242/31 |
| leaf31 | Ethernet5 | 10.255.0.245/31 | spine3 | Ethernet32 | 10.255.0.244/31 |
| leaf32 | Ethernet3 | 10.255.0.247/31 | spine1 | Ethernet33 | 10.255.0.246/31 |
| leaf32 | Ethernet4 | 10.255.0.249/31 | spine2 | Ethernet33 | 10.255.0.248/31 |
| leaf32 | Ethernet5 | 10.255.0.251/31 | spine3 | Ethernet33 | 10.255.0.250/31 |
| leaf33 | Ethernet3 | 10.255.0.253/31 | spine1 | Ethernet34 | 10.255.0.252/31 |
| leaf33 | Ethernet4 | 10.255.0.255/31 | spine2 | Ethernet34 | 10.255.0.254/31 |
| leaf33 | Ethernet5 | 10.255.1.1/31 | spine3 | Ethernet34 | 10.255.1.0/31 |
| leaf34 | Ethernet3 | 10.255.1.3/31 | spine1 | Ethernet35 | 10.255.1.2/31 |
| leaf34 | Ethernet4 | 10.255.1.5/31 | spine2 | Ethernet35 | 10.255.1.4/31 |
| leaf34 | Ethernet5 | 10.255.1.7/31 | spine3 | Ethernet35 | 10.255.1.6/31 |
| leaf35 | Ethernet3 | 10.255.1.9/31 | spine1 | Ethernet36 | 10.255.1.8/31 |
| leaf35 | Ethernet4 | 10.255.1.11/31 | spine2 | Ethernet36 | 10.255.1.10/31 |
| leaf35 | Ethernet5 | 10.255.1.13/31 | spine3 | Ethernet36 | 10.255.1.12/31 |
| leaf36 | Ethernet3 | 10.255.1.15/31 | spine1 | Ethernet37 | 10.255.1.14/31 |
| leaf36 | Ethernet4 | 10.255.1.17/31 | spine2 | Ethernet37 | 10.255.1.16/31 |
| leaf36 | Ethernet5 | 10.255.1.19/31 | spine3 | Ethernet37 | 10.255.1.18/31 |
| leaf37 | Ethernet3 | 10.255.1.21/31 | spine1 | Ethernet38 | 10.255.1.20/31 |
| leaf37 | Ethernet4 | 10.255.1.23/31 | spine2 | Ethernet38 | 10.255.1.22/31 |
| leaf37 | Ethernet5 | 10.255.1.25/31 | spine3 | Ethernet38 | 10.255.1.24/31 |
| leaf38 | Ethernet3 | 10.255.1.27/31 | spine1 | Ethernet39 | 10.255.1.26/31 |
| leaf38 | Ethernet4 | 10.255.1.29/31 | spine2 | Ethernet39 | 10.255.1.28/31 |
| leaf38 | Ethernet5 | 10.255.1.31/31 | spine3 | Ethernet39 | 10.255.1.30/31 |
| leaf39 | Ethernet3 | 10.255.1.33/31 | spine1 | Ethernet40 | 10.255.1.32/31 |
| leaf39 | Ethernet4 | 10.255.1.35/31 | spine2 | Ethernet40 | 10.255.1.34/31 |
| leaf39 | Ethernet5 | 10.255.1.37/31 | spine3 | Ethernet40 | 10.255.1.36/31 |
| leaf40 | Ethernet3 | 10.255.1.39/31 | spine1 | Ethernet41 | 10.255.1.38/31 |
| leaf40 | Ethernet4 | 10.255.1.41/31 | spine2 | Ethernet41 | 10.255.1.40/31 |
| leaf40 | Ethernet5 | 10.255.1.43/31 | spine3 | Ethernet41 | 10.255.1.42/31 |
| leaf41 | Ethernet3 | 10.255.1.45/31 | spine1 | Ethernet42 | 10.255.1.44/31 |
| leaf41 | Ethernet4 | 10.255.1.47/31 | spine2 | Ethernet42 | 10.255.1.46/31 |
| leaf41 | Ethernet5 | 10.255.1.49/31 | spine3 | Ethernet42 | 10.255.1.48/31 |
| leaf42 | Ethernet3 | 10.255.1.51/31 | spine1 | Ethernet43 | 10.255.1.50/31 |
| leaf42 | Ethernet4 | 10.255.1.53/31 | spine2 | Ethernet43 | 10.255.1.52/31 |
| leaf42 | Ethernet5 | 10.255.1.55/31 | spine3 | Ethernet43 | 10.255.1.54/31 |
| leaf43 | Ethernet3 | 10.255.1.57/31 | spine1 | Ethernet44 | 10.255.1.56/31 |
| leaf43 | Ethernet4 | 10.255.1.59/31 | spine2 | Ethernet44 | 10.255.1.58/31 |
| leaf43 | Ethernet5 | 10.255.1.61/31 | spine3 | Ethernet44 | 10.255.1.60/31 |
| leaf44 | Ethernet3 | 10.255.1.63/31 | spine1 | Ethernet45 | 10.255.1.62/31 |
| leaf44 | Ethernet4 | 10.255.1.65/31 | spine2 | Ethernet45 | 10.255.1.64/31 |
| leaf44 | Ethernet5 | 10.255.1.67/31 | spine3 | Ethernet45 | 10.255.1.66/31 |
| leaf45 | Ethernet3 | 10.255.1.69/31 | spine1 | Ethernet46 | 10.255.1.68/31 |
| leaf45 | Ethernet4 | 10.255.1.71/31 | spine2 | Ethernet46 | 10.255.1.70/31 |
| leaf45 | Ethernet5 | 10.255.1.73/31 | spine3 | Ethernet46 | 10.255.1.72/31 |
| leaf46 | Ethernet3 | 10.255.1.75/31 | spine1 | Ethernet47 | 10.255.1.74/31 |
| leaf46 | Ethernet4 | 10.255.1.77/31 | spine2 | Ethernet47 | 10.255.1.76/31 |
| leaf46 | Ethernet5 | 10.255.1.79/31 | spine3 | Ethernet47 | 10.255.1.78/31 |
| leaf47 | Ethernet3 | 10.255.1.81/31 | spine1 | Ethernet48 | 10.255.1.80/31 |
| leaf47 | Ethernet4 | 10.255.1.83/31 | spine2 | Ethernet48 | 10.255.1.82/31 |
| leaf47 | Ethernet5 | 10.255.1.85/31 | spine3 | Ethernet48 | 10.255.1.84/31 |
| leaf48 | Ethernet3 | 10.255.1.87/31 | spine1 | Ethernet49 | 10.255.1.86/31 |
| leaf48 | Ethernet4 | 10.255.1.89/31 | spine2 | Ethernet49 | 10.255.1.88/31 |
| leaf48 | Ethernet5 | 10.255.1.91/31 | spine3 | Ethernet49 | 10.255.1.90/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.255.4.0/24 | 256 | 51 | 19.93 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | leaf1 | 10.255.4.11/32 |
| FABRIC | leaf2 | 10.255.4.12/32 |
| FABRIC | leaf3 | 10.255.4.13/32 |
| FABRIC | leaf4 | 10.255.4.14/32 |
| FABRIC | leaf5 | 10.255.4.15/32 |
| FABRIC | leaf6 | 10.255.4.16/32 |
| FABRIC | leaf7 | 10.255.4.17/32 |
| FABRIC | leaf8 | 10.255.4.18/32 |
| FABRIC | leaf9 | 10.255.4.19/32 |
| FABRIC | leaf10 | 10.255.4.20/32 |
| FABRIC | leaf11 | 10.255.4.21/32 |
| FABRIC | leaf12 | 10.255.4.22/32 |
| FABRIC | leaf13 | 10.255.4.23/32 |
| FABRIC | leaf14 | 10.255.4.24/32 |
| FABRIC | leaf15 | 10.255.4.25/32 |
| FABRIC | leaf16 | 10.255.4.26/32 |
| FABRIC | leaf17 | 10.255.4.27/32 |
| FABRIC | leaf18 | 10.255.4.28/32 |
| FABRIC | leaf19 | 10.255.4.29/32 |
| FABRIC | leaf20 | 10.255.4.30/32 |
| FABRIC | leaf21 | 10.255.4.31/32 |
| FABRIC | leaf22 | 10.255.4.32/32 |
| FABRIC | leaf23 | 10.255.4.33/32 |
| FABRIC | leaf24 | 10.255.4.34/32 |
| FABRIC | leaf25 | 10.255.4.35/32 |
| FABRIC | leaf26 | 10.255.4.36/32 |
| FABRIC | leaf27 | 10.255.4.37/32 |
| FABRIC | leaf28 | 10.255.4.38/32 |
| FABRIC | leaf29 | 10.255.4.39/32 |
| FABRIC | leaf30 | 10.255.4.40/32 |
| FABRIC | leaf31 | 10.255.4.41/32 |
| FABRIC | leaf32 | 10.255.4.42/32 |
| FABRIC | leaf33 | 10.255.4.43/32 |
| FABRIC | leaf34 | 10.255.4.44/32 |
| FABRIC | leaf35 | 10.255.4.45/32 |
| FABRIC | leaf36 | 10.255.4.46/32 |
| FABRIC | leaf37 | 10.255.4.47/32 |
| FABRIC | leaf38 | 10.255.4.48/32 |
| FABRIC | leaf39 | 10.255.4.49/32 |
| FABRIC | leaf40 | 10.255.4.50/32 |
| FABRIC | leaf41 | 10.255.4.51/32 |
| FABRIC | leaf42 | 10.255.4.52/32 |
| FABRIC | leaf43 | 10.255.4.53/32 |
| FABRIC | leaf44 | 10.255.4.54/32 |
| FABRIC | leaf45 | 10.255.4.55/32 |
| FABRIC | leaf46 | 10.255.4.56/32 |
| FABRIC | leaf47 | 10.255.4.57/32 |
| FABRIC | leaf48 | 10.255.4.58/32 |
| FABRIC | spine1 | 10.255.4.1/32 |
| FABRIC | spine2 | 10.255.4.2/32 |
| FABRIC | spine3 | 10.255.4.3/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 10.255.5.0/24 | 256 | 48 | 18.75 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | leaf1 | 10.255.5.11/32 |
| FABRIC | leaf2 | 10.255.5.11/32 |
| FABRIC | leaf3 | 10.255.5.13/32 |
| FABRIC | leaf4 | 10.255.5.13/32 |
| FABRIC | leaf5 | 10.255.5.15/32 |
| FABRIC | leaf6 | 10.255.5.15/32 |
| FABRIC | leaf7 | 10.255.5.17/32 |
| FABRIC | leaf8 | 10.255.5.17/32 |
| FABRIC | leaf9 | 10.255.5.19/32 |
| FABRIC | leaf10 | 10.255.5.19/32 |
| FABRIC | leaf11 | 10.255.5.21/32 |
| FABRIC | leaf12 | 10.255.5.21/32 |
| FABRIC | leaf13 | 10.255.5.23/32 |
| FABRIC | leaf14 | 10.255.5.23/32 |
| FABRIC | leaf15 | 10.255.5.25/32 |
| FABRIC | leaf16 | 10.255.5.25/32 |
| FABRIC | leaf17 | 10.255.5.27/32 |
| FABRIC | leaf18 | 10.255.5.27/32 |
| FABRIC | leaf19 | 10.255.5.29/32 |
| FABRIC | leaf20 | 10.255.5.29/32 |
| FABRIC | leaf21 | 10.255.5.31/32 |
| FABRIC | leaf22 | 10.255.5.31/32 |
| FABRIC | leaf23 | 10.255.5.33/32 |
| FABRIC | leaf24 | 10.255.5.33/32 |
| FABRIC | leaf25 | 10.255.5.35/32 |
| FABRIC | leaf26 | 10.255.5.35/32 |
| FABRIC | leaf27 | 10.255.5.37/32 |
| FABRIC | leaf28 | 10.255.5.37/32 |
| FABRIC | leaf29 | 10.255.5.39/32 |
| FABRIC | leaf30 | 10.255.5.39/32 |
| FABRIC | leaf31 | 10.255.5.41/32 |
| FABRIC | leaf32 | 10.255.5.41/32 |
| FABRIC | leaf33 | 10.255.5.43/32 |
| FABRIC | leaf34 | 10.255.5.43/32 |
| FABRIC | leaf35 | 10.255.5.45/32 |
| FABRIC | leaf36 | 10.255.5.45/32 |
| FABRIC | leaf37 | 10.255.5.47/32 |
| FABRIC | leaf38 | 10.255.5.47/32 |
| FABRIC | leaf39 | 10.255.5.49/32 |
| FABRIC | leaf40 | 10.255.5.49/32 |
| FABRIC | leaf41 | 10.255.5.51/32 |
| FABRIC | leaf42 | 10.255.5.51/32 |
| FABRIC | leaf43 | 10.255.5.53/32 |
| FABRIC | leaf44 | 10.255.5.53/32 |
| FABRIC | leaf45 | 10.255.5.55/32 |
| FABRIC | leaf46 | 10.255.5.55/32 |
| FABRIC | leaf47 | 10.255.5.57/32 |
| FABRIC | leaf48 | 10.255.5.57/32 |
