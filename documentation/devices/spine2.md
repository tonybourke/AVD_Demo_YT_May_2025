# spine2

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | OOB_MANAGEMENT | oob | MGMT | 172.20.20.102/24 | 172.20.20.1 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management0
   description OOB_MANAGEMENT
   no shutdown
   vrf MGMT
   ip address 172.20.20.102/24
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 192.168.1.9 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 192.168.1.9
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | UNIX-Socket | Default Services |
| ---- | ----- | ----------- | ---------------- |
| False | True | - | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |
| tony | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
username admin ssh-key ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDaaW0yCS+kwtUVIJdwCVaw2+Ul/yYhaPXYltoVcszcEJPWCSwAmMdvrlecxcyEfrs1KJLYVLD8RwmMRlMRrteYJzmk8MGuAyNxQMcma0EWI78suzJOlxGczxwUzZY2+vYwLgWQZPYEZeScjY8ko68r+sEUmgg+y/WC+OGshtytqahs1zaJhDHwu2y3GAW9KnCA1vQL8qyaXvTKkci6+unMlwdc7jTL7bktoudWFKAAHxVtJf0SdBGvWdbbh3JgAt3mHtjKMfm+8qQgv1mfr6Sn41tLlsmn/RTsMMkDbuYVmpjXFSb6LXwf/ylx1zc/FxJHHXh4yD0wOKD3rYEIjndF7uGEqrs1BZtje50L6YPVcjUCGI9kL4R1BUI8uzTmTLATOmDJ03KAaTnXwkhlW96FQshJjiDL4K9FZUaYww6vEp2nk2XOaXxyB1JXe0/2A/H57f2wIR1TwdqAbcHOkGLqj0mS+focnRJvaxPk6ytIGmfRqF9n8K0RLMXN9s/G+sk=
username tony privilege 15 role network-admin secret sha512 <removed>
username tony ssh-key ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDaaW0yCS+kwtUVIJdwCVaw2+Ul/yYhaPXYltoVcszcEJPWCSwAmMdvrlecxcyEfrs1KJLYVLD8RwmMRlMRrteYJzmk8MGuAyNxQMcma0EWI78suzJOlxGczxwUzZY2+vYwLgWQZPYEZeScjY8ko68r+sEUmgg+y/WC+OGshtytqahs1zaJhDHwu2y3GAW9KnCA1vQL8qyaXvTKkci6+unMlwdc7jTL7bktoudWFKAAHxVtJf0SdBGvWdbbh3JgAt3mHtjKMfm+8qQgv1mfr6Sn41tLlsmn/RTsMMkDbuYVmpjXFSb6LXwf/ylx1zc/FxJHHXh4yD0wOKD3rYEIjndF7uGEqrs1BZtje50L6YPVcjUCGI9kL4R1BUI8uzTmTLATOmDJ03KAaTnXwkhlW96FQshJjiDL4K9FZUaYww6vEp2nk2XOaXxyB1JXe0/2A/H57f2wIR1TwdqAbcHOkGLqj0mS+focnRJvaxPk6ytIGmfRqF9n8K0RLMXN9s/G+sk=
```

### Enable Password

Enable password has been disabled

### AAA Authentication

#### AAA Authentication Summary

| Type | Sub-type | User Stores |
| ---- | -------- | ---------- |
| Login | default | local |

#### AAA Authentication Device Configuration

```eos
aaa authentication login default local
!
```

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | local |

Authorization for configuration commands is disabled.

#### AAA Authorization Device Configuration

```eos
aaa authorization exec default local
!
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet2 | P2P_leaf1_Ethernet4 | - | 10.255.0.62/31 | default | 1550 | False | - | - |
| Ethernet3 | P2P_leaf2_Ethernet4 | - | 10.255.0.68/31 | default | 1550 | False | - | - |
| Ethernet4 | P2P_leaf3_Ethernet4 | - | 10.255.0.74/31 | default | 1550 | False | - | - |
| Ethernet5 | P2P_leaf4_Ethernet4 | - | 10.255.0.80/31 | default | 1550 | False | - | - |
| Ethernet6 | P2P_leaf5_Ethernet4 | - | 10.255.0.86/31 | default | 1550 | False | - | - |
| Ethernet7 | P2P_leaf6_Ethernet4 | - | 10.255.0.92/31 | default | 1550 | False | - | - |
| Ethernet8 | P2P_leaf7_Ethernet4 | - | 10.255.0.98/31 | default | 1550 | False | - | - |
| Ethernet9 | P2P_leaf8_Ethernet4 | - | 10.255.0.104/31 | default | 1550 | False | - | - |
| Ethernet10 | P2P_leaf9_Ethernet4 | - | 10.255.0.110/31 | default | 1550 | False | - | - |
| Ethernet11 | P2P_leaf10_Ethernet4 | - | 10.255.0.116/31 | default | 1550 | False | - | - |
| Ethernet12 | P2P_leaf11_Ethernet4 | - | 10.255.0.122/31 | default | 1550 | False | - | - |
| Ethernet13 | P2P_leaf12_Ethernet4 | - | 10.255.0.128/31 | default | 1550 | False | - | - |
| Ethernet14 | P2P_leaf13_Ethernet4 | - | 10.255.0.134/31 | default | 1550 | False | - | - |
| Ethernet15 | P2P_leaf14_Ethernet4 | - | 10.255.0.140/31 | default | 1550 | False | - | - |
| Ethernet16 | P2P_leaf15_Ethernet4 | - | 10.255.0.146/31 | default | 1550 | False | - | - |
| Ethernet17 | P2P_leaf16_Ethernet4 | - | 10.255.0.152/31 | default | 1550 | False | - | - |
| Ethernet18 | P2P_leaf17_Ethernet4 | - | 10.255.0.158/31 | default | 1550 | False | - | - |
| Ethernet19 | P2P_leaf18_Ethernet4 | - | 10.255.0.164/31 | default | 1550 | False | - | - |
| Ethernet20 | P2P_leaf19_Ethernet4 | - | 10.255.0.170/31 | default | 1550 | False | - | - |
| Ethernet21 | P2P_leaf20_Ethernet4 | - | 10.255.0.176/31 | default | 1550 | False | - | - |
| Ethernet22 | P2P_leaf21_Ethernet4 | - | 10.255.0.182/31 | default | 1550 | False | - | - |
| Ethernet23 | P2P_leaf22_Ethernet4 | - | 10.255.0.188/31 | default | 1550 | False | - | - |
| Ethernet24 | P2P_leaf23_Ethernet4 | - | 10.255.0.194/31 | default | 1550 | False | - | - |
| Ethernet25 | P2P_leaf24_Ethernet4 | - | 10.255.0.200/31 | default | 1550 | False | - | - |
| Ethernet26 | P2P_leaf25_Ethernet4 | - | 10.255.0.206/31 | default | 1550 | False | - | - |
| Ethernet27 | P2P_leaf26_Ethernet4 | - | 10.255.0.212/31 | default | 1550 | False | - | - |
| Ethernet28 | P2P_leaf27_Ethernet4 | - | 10.255.0.218/31 | default | 1550 | False | - | - |
| Ethernet29 | P2P_leaf28_Ethernet4 | - | 10.255.0.224/31 | default | 1550 | False | - | - |
| Ethernet30 | P2P_leaf29_Ethernet4 | - | 10.255.0.230/31 | default | 1550 | False | - | - |
| Ethernet31 | P2P_leaf30_Ethernet4 | - | 10.255.0.236/31 | default | 1550 | False | - | - |
| Ethernet32 | P2P_leaf31_Ethernet4 | - | 10.255.0.242/31 | default | 1550 | False | - | - |
| Ethernet33 | P2P_leaf32_Ethernet4 | - | 10.255.0.248/31 | default | 1550 | False | - | - |
| Ethernet34 | P2P_leaf33_Ethernet4 | - | 10.255.0.254/31 | default | 1550 | False | - | - |
| Ethernet35 | P2P_leaf34_Ethernet4 | - | 10.255.1.4/31 | default | 1550 | False | - | - |
| Ethernet36 | P2P_leaf35_Ethernet4 | - | 10.255.1.10/31 | default | 1550 | False | - | - |
| Ethernet37 | P2P_leaf36_Ethernet4 | - | 10.255.1.16/31 | default | 1550 | False | - | - |
| Ethernet38 | P2P_leaf37_Ethernet4 | - | 10.255.1.22/31 | default | 1550 | False | - | - |
| Ethernet39 | P2P_leaf38_Ethernet4 | - | 10.255.1.28/31 | default | 1550 | False | - | - |
| Ethernet40 | P2P_leaf39_Ethernet4 | - | 10.255.1.34/31 | default | 1550 | False | - | - |
| Ethernet41 | P2P_leaf40_Ethernet4 | - | 10.255.1.40/31 | default | 1550 | False | - | - |
| Ethernet42 | P2P_leaf41_Ethernet4 | - | 10.255.1.46/31 | default | 1550 | False | - | - |
| Ethernet43 | P2P_leaf42_Ethernet4 | - | 10.255.1.52/31 | default | 1550 | False | - | - |
| Ethernet44 | P2P_leaf43_Ethernet4 | - | 10.255.1.58/31 | default | 1550 | False | - | - |
| Ethernet45 | P2P_leaf44_Ethernet4 | - | 10.255.1.64/31 | default | 1550 | False | - | - |
| Ethernet46 | P2P_leaf45_Ethernet4 | - | 10.255.1.70/31 | default | 1550 | False | - | - |
| Ethernet47 | P2P_leaf46_Ethernet4 | - | 10.255.1.76/31 | default | 1550 | False | - | - |
| Ethernet48 | P2P_leaf47_Ethernet4 | - | 10.255.1.82/31 | default | 1550 | False | - | - |
| Ethernet49 | P2P_leaf48_Ethernet4 | - | 10.255.1.88/31 | default | 1550 | False | - | - |
| Ethernet52 | P2P_borderleaf1_Ethernet4 | - | 10.255.1.106/31 | default | 1550 | False | - | - |
| Ethernet53 | P2P_borderleaf2_Ethernet4 | - | 10.255.1.112/31 | default | 1550 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet2
   description P2P_leaf1_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.62/31
!
interface Ethernet3
   description P2P_leaf2_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.68/31
!
interface Ethernet4
   description P2P_leaf3_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.74/31
!
interface Ethernet5
   description P2P_leaf4_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.80/31
!
interface Ethernet6
   description P2P_leaf5_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.86/31
!
interface Ethernet7
   description P2P_leaf6_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.92/31
!
interface Ethernet8
   description P2P_leaf7_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.98/31
!
interface Ethernet9
   description P2P_leaf8_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.104/31
!
interface Ethernet10
   description P2P_leaf9_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.110/31
!
interface Ethernet11
   description P2P_leaf10_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.116/31
!
interface Ethernet12
   description P2P_leaf11_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.122/31
!
interface Ethernet13
   description P2P_leaf12_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.128/31
!
interface Ethernet14
   description P2P_leaf13_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.134/31
!
interface Ethernet15
   description P2P_leaf14_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.140/31
!
interface Ethernet16
   description P2P_leaf15_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.146/31
!
interface Ethernet17
   description P2P_leaf16_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.152/31
!
interface Ethernet18
   description P2P_leaf17_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.158/31
!
interface Ethernet19
   description P2P_leaf18_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.164/31
!
interface Ethernet20
   description P2P_leaf19_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.170/31
!
interface Ethernet21
   description P2P_leaf20_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.176/31
!
interface Ethernet22
   description P2P_leaf21_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.182/31
!
interface Ethernet23
   description P2P_leaf22_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.188/31
!
interface Ethernet24
   description P2P_leaf23_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.194/31
!
interface Ethernet25
   description P2P_leaf24_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.200/31
!
interface Ethernet26
   description P2P_leaf25_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.206/31
!
interface Ethernet27
   description P2P_leaf26_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.212/31
!
interface Ethernet28
   description P2P_leaf27_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.218/31
!
interface Ethernet29
   description P2P_leaf28_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.224/31
!
interface Ethernet30
   description P2P_leaf29_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.230/31
!
interface Ethernet31
   description P2P_leaf30_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.236/31
!
interface Ethernet32
   description P2P_leaf31_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.242/31
!
interface Ethernet33
   description P2P_leaf32_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.248/31
!
interface Ethernet34
   description P2P_leaf33_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.0.254/31
!
interface Ethernet35
   description P2P_leaf34_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.4/31
!
interface Ethernet36
   description P2P_leaf35_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.10/31
!
interface Ethernet37
   description P2P_leaf36_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.16/31
!
interface Ethernet38
   description P2P_leaf37_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.22/31
!
interface Ethernet39
   description P2P_leaf38_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.28/31
!
interface Ethernet40
   description P2P_leaf39_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.34/31
!
interface Ethernet41
   description P2P_leaf40_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.40/31
!
interface Ethernet42
   description P2P_leaf41_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.46/31
!
interface Ethernet43
   description P2P_leaf42_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.52/31
!
interface Ethernet44
   description P2P_leaf43_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.58/31
!
interface Ethernet45
   description P2P_leaf44_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.64/31
!
interface Ethernet46
   description P2P_leaf45_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.70/31
!
interface Ethernet47
   description P2P_leaf46_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.76/31
!
interface Ethernet48
   description P2P_leaf47_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.82/31
!
interface Ethernet49
   description P2P_leaf48_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.88/31
!
interface Ethernet52
   description P2P_borderleaf1_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.106/31
!
interface Ethernet53
   description P2P_borderleaf2_Ethernet4
   no shutdown
   mtu 1550
   no switchport
   ip address 10.255.1.112/31
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 10.255.4.2/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 10.255.4.2/32
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 172.20.20.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 172.20.20.1
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001 | 10.255.4.2 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Next-hop unchanged | True |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.255.0.63 | 65111 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.69 | 65111 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.75 | 65113 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.81 | 65113 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.87 | 65115 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.93 | 65115 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.99 | 65117 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.105 | 65117 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.111 | 65119 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.117 | 65119 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.123 | 65121 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.129 | 65121 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.135 | 65123 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.141 | 65123 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.147 | 65125 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.153 | 65125 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.159 | 65127 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.165 | 65127 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.171 | 65129 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.177 | 65129 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.183 | 65131 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.189 | 65131 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.195 | 65133 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.201 | 65133 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.207 | 65135 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.213 | 65135 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.219 | 65137 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.225 | 65137 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.231 | 65139 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.237 | 65139 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.243 | 65141 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.249 | 65141 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.0.255 | 65143 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.5 | 65143 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.11 | 65145 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.17 | 65145 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.23 | 65147 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.29 | 65147 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.35 | 65149 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.41 | 65149 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.47 | 65151 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.53 | 65151 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.59 | 65153 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.65 | 65153 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.71 | 65155 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.77 | 65155 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.83 | 65157 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.89 | 65157 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.107 | 65161 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.1.113 | 65161 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.255.4.11 | 65111 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.12 | 65111 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.13 | 65113 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.14 | 65113 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.15 | 65115 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.16 | 65115 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.17 | 65117 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.18 | 65117 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.19 | 65119 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.20 | 65119 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.21 | 65121 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.22 | 65121 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.23 | 65123 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.24 | 65123 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.25 | 65125 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.26 | 65125 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.27 | 65127 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.28 | 65127 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.29 | 65129 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.30 | 65129 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.31 | 65131 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.32 | 65131 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.33 | 65133 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.34 | 65133 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.35 | 65135 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.36 | 65135 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.37 | 65137 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.38 | 65137 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.39 | 65139 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.40 | 65139 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.41 | 65141 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.42 | 65141 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.43 | 65143 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.44 | 65143 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.45 | 65145 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.46 | 65145 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.47 | 65147 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.48 | 65147 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.49 | 65149 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.50 | 65149 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.51 | 65151 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.52 | 65151 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.53 | 65153 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.54 | 65153 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.55 | 65155 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.56 | 65155 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.57 | 65157 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.58 | 65157 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.61 | 65161 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.4.62 | 65161 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation | Next-hop-self Source Interface |
| ---------- | -------- | ------------ | ------------- | ------------- | ------------------------------ |
| EVPN-OVERLAY-PEERS | True |  - | - | default | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 10.255.4.2
   no bgp default ipv4-unicast
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.255.0.63 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.63 remote-as 65111
   neighbor 10.255.0.63 description leaf1_Ethernet4
   neighbor 10.255.0.69 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.69 remote-as 65111
   neighbor 10.255.0.69 description leaf2_Ethernet4
   neighbor 10.255.0.75 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.75 remote-as 65113
   neighbor 10.255.0.75 description leaf3_Ethernet4
   neighbor 10.255.0.81 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.81 remote-as 65113
   neighbor 10.255.0.81 description leaf4_Ethernet4
   neighbor 10.255.0.87 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.87 remote-as 65115
   neighbor 10.255.0.87 description leaf5_Ethernet4
   neighbor 10.255.0.93 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.93 remote-as 65115
   neighbor 10.255.0.93 description leaf6_Ethernet4
   neighbor 10.255.0.99 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.99 remote-as 65117
   neighbor 10.255.0.99 description leaf7_Ethernet4
   neighbor 10.255.0.105 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.105 remote-as 65117
   neighbor 10.255.0.105 description leaf8_Ethernet4
   neighbor 10.255.0.111 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.111 remote-as 65119
   neighbor 10.255.0.111 description leaf9_Ethernet4
   neighbor 10.255.0.117 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.117 remote-as 65119
   neighbor 10.255.0.117 description leaf10_Ethernet4
   neighbor 10.255.0.123 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.123 remote-as 65121
   neighbor 10.255.0.123 description leaf11_Ethernet4
   neighbor 10.255.0.129 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.129 remote-as 65121
   neighbor 10.255.0.129 description leaf12_Ethernet4
   neighbor 10.255.0.135 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.135 remote-as 65123
   neighbor 10.255.0.135 description leaf13_Ethernet4
   neighbor 10.255.0.141 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.141 remote-as 65123
   neighbor 10.255.0.141 description leaf14_Ethernet4
   neighbor 10.255.0.147 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.147 remote-as 65125
   neighbor 10.255.0.147 description leaf15_Ethernet4
   neighbor 10.255.0.153 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.153 remote-as 65125
   neighbor 10.255.0.153 description leaf16_Ethernet4
   neighbor 10.255.0.159 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.159 remote-as 65127
   neighbor 10.255.0.159 description leaf17_Ethernet4
   neighbor 10.255.0.165 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.165 remote-as 65127
   neighbor 10.255.0.165 description leaf18_Ethernet4
   neighbor 10.255.0.171 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.171 remote-as 65129
   neighbor 10.255.0.171 description leaf19_Ethernet4
   neighbor 10.255.0.177 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.177 remote-as 65129
   neighbor 10.255.0.177 description leaf20_Ethernet4
   neighbor 10.255.0.183 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.183 remote-as 65131
   neighbor 10.255.0.183 description leaf21_Ethernet4
   neighbor 10.255.0.189 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.189 remote-as 65131
   neighbor 10.255.0.189 description leaf22_Ethernet4
   neighbor 10.255.0.195 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.195 remote-as 65133
   neighbor 10.255.0.195 description leaf23_Ethernet4
   neighbor 10.255.0.201 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.201 remote-as 65133
   neighbor 10.255.0.201 description leaf24_Ethernet4
   neighbor 10.255.0.207 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.207 remote-as 65135
   neighbor 10.255.0.207 description leaf25_Ethernet4
   neighbor 10.255.0.213 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.213 remote-as 65135
   neighbor 10.255.0.213 description leaf26_Ethernet4
   neighbor 10.255.0.219 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.219 remote-as 65137
   neighbor 10.255.0.219 description leaf27_Ethernet4
   neighbor 10.255.0.225 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.225 remote-as 65137
   neighbor 10.255.0.225 description leaf28_Ethernet4
   neighbor 10.255.0.231 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.231 remote-as 65139
   neighbor 10.255.0.231 description leaf29_Ethernet4
   neighbor 10.255.0.237 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.237 remote-as 65139
   neighbor 10.255.0.237 description leaf30_Ethernet4
   neighbor 10.255.0.243 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.243 remote-as 65141
   neighbor 10.255.0.243 description leaf31_Ethernet4
   neighbor 10.255.0.249 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.249 remote-as 65141
   neighbor 10.255.0.249 description leaf32_Ethernet4
   neighbor 10.255.0.255 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.0.255 remote-as 65143
   neighbor 10.255.0.255 description leaf33_Ethernet4
   neighbor 10.255.1.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.5 remote-as 65143
   neighbor 10.255.1.5 description leaf34_Ethernet4
   neighbor 10.255.1.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.11 remote-as 65145
   neighbor 10.255.1.11 description leaf35_Ethernet4
   neighbor 10.255.1.17 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.17 remote-as 65145
   neighbor 10.255.1.17 description leaf36_Ethernet4
   neighbor 10.255.1.23 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.23 remote-as 65147
   neighbor 10.255.1.23 description leaf37_Ethernet4
   neighbor 10.255.1.29 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.29 remote-as 65147
   neighbor 10.255.1.29 description leaf38_Ethernet4
   neighbor 10.255.1.35 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.35 remote-as 65149
   neighbor 10.255.1.35 description leaf39_Ethernet4
   neighbor 10.255.1.41 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.41 remote-as 65149
   neighbor 10.255.1.41 description leaf40_Ethernet4
   neighbor 10.255.1.47 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.47 remote-as 65151
   neighbor 10.255.1.47 description leaf41_Ethernet4
   neighbor 10.255.1.53 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.53 remote-as 65151
   neighbor 10.255.1.53 description leaf42_Ethernet4
   neighbor 10.255.1.59 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.59 remote-as 65153
   neighbor 10.255.1.59 description leaf43_Ethernet4
   neighbor 10.255.1.65 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.65 remote-as 65153
   neighbor 10.255.1.65 description leaf44_Ethernet4
   neighbor 10.255.1.71 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.71 remote-as 65155
   neighbor 10.255.1.71 description leaf45_Ethernet4
   neighbor 10.255.1.77 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.77 remote-as 65155
   neighbor 10.255.1.77 description leaf46_Ethernet4
   neighbor 10.255.1.83 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.83 remote-as 65157
   neighbor 10.255.1.83 description leaf47_Ethernet4
   neighbor 10.255.1.89 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.89 remote-as 65157
   neighbor 10.255.1.89 description leaf48_Ethernet4
   neighbor 10.255.1.107 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.107 remote-as 65161
   neighbor 10.255.1.107 description borderleaf1_Ethernet4
   neighbor 10.255.1.113 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.1.113 remote-as 65161
   neighbor 10.255.1.113 description borderleaf2_Ethernet4
   neighbor 10.255.4.11 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.11 remote-as 65111
   neighbor 10.255.4.11 description leaf1_Loopback0
   neighbor 10.255.4.12 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.12 remote-as 65111
   neighbor 10.255.4.12 description leaf2_Loopback0
   neighbor 10.255.4.13 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.13 remote-as 65113
   neighbor 10.255.4.13 description leaf3_Loopback0
   neighbor 10.255.4.14 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.14 remote-as 65113
   neighbor 10.255.4.14 description leaf4_Loopback0
   neighbor 10.255.4.15 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.15 remote-as 65115
   neighbor 10.255.4.15 description leaf5_Loopback0
   neighbor 10.255.4.16 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.16 remote-as 65115
   neighbor 10.255.4.16 description leaf6_Loopback0
   neighbor 10.255.4.17 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.17 remote-as 65117
   neighbor 10.255.4.17 description leaf7_Loopback0
   neighbor 10.255.4.18 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.18 remote-as 65117
   neighbor 10.255.4.18 description leaf8_Loopback0
   neighbor 10.255.4.19 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.19 remote-as 65119
   neighbor 10.255.4.19 description leaf9_Loopback0
   neighbor 10.255.4.20 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.20 remote-as 65119
   neighbor 10.255.4.20 description leaf10_Loopback0
   neighbor 10.255.4.21 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.21 remote-as 65121
   neighbor 10.255.4.21 description leaf11_Loopback0
   neighbor 10.255.4.22 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.22 remote-as 65121
   neighbor 10.255.4.22 description leaf12_Loopback0
   neighbor 10.255.4.23 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.23 remote-as 65123
   neighbor 10.255.4.23 description leaf13_Loopback0
   neighbor 10.255.4.24 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.24 remote-as 65123
   neighbor 10.255.4.24 description leaf14_Loopback0
   neighbor 10.255.4.25 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.25 remote-as 65125
   neighbor 10.255.4.25 description leaf15_Loopback0
   neighbor 10.255.4.26 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.26 remote-as 65125
   neighbor 10.255.4.26 description leaf16_Loopback0
   neighbor 10.255.4.27 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.27 remote-as 65127
   neighbor 10.255.4.27 description leaf17_Loopback0
   neighbor 10.255.4.28 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.28 remote-as 65127
   neighbor 10.255.4.28 description leaf18_Loopback0
   neighbor 10.255.4.29 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.29 remote-as 65129
   neighbor 10.255.4.29 description leaf19_Loopback0
   neighbor 10.255.4.30 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.30 remote-as 65129
   neighbor 10.255.4.30 description leaf20_Loopback0
   neighbor 10.255.4.31 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.31 remote-as 65131
   neighbor 10.255.4.31 description leaf21_Loopback0
   neighbor 10.255.4.32 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.32 remote-as 65131
   neighbor 10.255.4.32 description leaf22_Loopback0
   neighbor 10.255.4.33 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.33 remote-as 65133
   neighbor 10.255.4.33 description leaf23_Loopback0
   neighbor 10.255.4.34 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.34 remote-as 65133
   neighbor 10.255.4.34 description leaf24_Loopback0
   neighbor 10.255.4.35 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.35 remote-as 65135
   neighbor 10.255.4.35 description leaf25_Loopback0
   neighbor 10.255.4.36 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.36 remote-as 65135
   neighbor 10.255.4.36 description leaf26_Loopback0
   neighbor 10.255.4.37 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.37 remote-as 65137
   neighbor 10.255.4.37 description leaf27_Loopback0
   neighbor 10.255.4.38 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.38 remote-as 65137
   neighbor 10.255.4.38 description leaf28_Loopback0
   neighbor 10.255.4.39 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.39 remote-as 65139
   neighbor 10.255.4.39 description leaf29_Loopback0
   neighbor 10.255.4.40 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.40 remote-as 65139
   neighbor 10.255.4.40 description leaf30_Loopback0
   neighbor 10.255.4.41 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.41 remote-as 65141
   neighbor 10.255.4.41 description leaf31_Loopback0
   neighbor 10.255.4.42 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.42 remote-as 65141
   neighbor 10.255.4.42 description leaf32_Loopback0
   neighbor 10.255.4.43 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.43 remote-as 65143
   neighbor 10.255.4.43 description leaf33_Loopback0
   neighbor 10.255.4.44 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.44 remote-as 65143
   neighbor 10.255.4.44 description leaf34_Loopback0
   neighbor 10.255.4.45 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.45 remote-as 65145
   neighbor 10.255.4.45 description leaf35_Loopback0
   neighbor 10.255.4.46 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.46 remote-as 65145
   neighbor 10.255.4.46 description leaf36_Loopback0
   neighbor 10.255.4.47 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.47 remote-as 65147
   neighbor 10.255.4.47 description leaf37_Loopback0
   neighbor 10.255.4.48 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.48 remote-as 65147
   neighbor 10.255.4.48 description leaf38_Loopback0
   neighbor 10.255.4.49 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.49 remote-as 65149
   neighbor 10.255.4.49 description leaf39_Loopback0
   neighbor 10.255.4.50 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.50 remote-as 65149
   neighbor 10.255.4.50 description leaf40_Loopback0
   neighbor 10.255.4.51 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.51 remote-as 65151
   neighbor 10.255.4.51 description leaf41_Loopback0
   neighbor 10.255.4.52 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.52 remote-as 65151
   neighbor 10.255.4.52 description leaf42_Loopback0
   neighbor 10.255.4.53 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.53 remote-as 65153
   neighbor 10.255.4.53 description leaf43_Loopback0
   neighbor 10.255.4.54 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.54 remote-as 65153
   neighbor 10.255.4.54 description leaf44_Loopback0
   neighbor 10.255.4.55 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.55 remote-as 65155
   neighbor 10.255.4.55 description leaf45_Loopback0
   neighbor 10.255.4.56 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.56 remote-as 65155
   neighbor 10.255.4.56 description leaf46_Loopback0
   neighbor 10.255.4.57 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.57 remote-as 65157
   neighbor 10.255.4.57 description leaf47_Loopback0
   neighbor 10.255.4.58 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.58 remote-as 65157
   neighbor 10.255.4.58 description leaf48_Loopback0
   neighbor 10.255.4.61 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.61 remote-as 65161
   neighbor 10.255.4.61 description borderleaf1_Loopback0
   neighbor 10.255.4.62 peer group EVPN-OVERLAY-PEERS
   neighbor 10.255.4.62 remote-as 65161
   neighbor 10.255.4.62 description borderleaf2_Loopback0
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.255.4.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.255.4.0/24 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```
