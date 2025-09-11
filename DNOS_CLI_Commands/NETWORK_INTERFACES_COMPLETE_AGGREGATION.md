# Network Interfaces Complete Aggregation

This file contains the complete content from all RST files in the Interfaces folder.

This comprehensive documentation covers all network interface configurations including:
- Physical interfaces (Ethernet, Bundle-Ether, Loopback, Null)
- Logical interfaces (VLAN, BVI, LAG)
- Interface configurations (IP addresses, MTU, descriptions, admin state)
- Interface features (flow control, speed/duplex, encapsulation)
- Advanced features (sub-interfaces, QoS, ACLs, mirroring)

Total files:      181

---

## console interface baud-rate.rst

interfaces baud-rate
--------------------

**Minimum user role:** operator

Sets the baud rate of the console interface.

**Command syntax: baud-rate [baud-rate]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Console

**Parameter table**

+-----------+----------------------------------+------------+---------+
| Parameter | Description                      | Range      | Default |
+===========+==================================+============+=========+
| baud-rate | Set console interface baud-rate. | | 115200   | 115200  |
|           |                                  | | 38400    |         |
|           |                                  | | 9600     |         |
+-----------+----------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# console-ncc-0/0
    dnRouter(cfg-if-console-ncc-0/0)# baud-rate 115200


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-console-ncc-0/0)# no baud-rate

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.1.3  | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/admin-state.rst

interfaces dhcp relay-agent admin-state
---------------------------------------

**Minimum user role:** operator

To enable DHCPv4 relay agent on the interface.

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent

**Note**

- At least one DHCPv4 server must be configured for enabling the relay agent on the interface.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                                      | Range        | Default  |
+=============+==================================================================================+==============+==========+
| admin-state | Enables the relay agent on the referenced interface. At least one server address | | enabled    | disabled |
|             | should also be configured for forwarding requests                                | | disabled   |          |
+-------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# admin-state enabled


**Removing Configuration**

To return DHCPv4 relay agent admin-state on the interface to its default value:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# no admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/dhcp_relay-agent.rst

interfaces dhcp relay-agent
---------------------------

**Minimum user role:** operator

To enter DHCPv4 relay agent configuration mode:

**Command syntax: dhcp relay-agent**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - IRB

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)#


**Removing Configuration**

To remove the DHCP relay agent configuration:
::

    dnRouter(cfg-if-ge100-0/0/0)# no dhcp relay-agent

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/option-82/allow-untrusted.rst

interfaces dhcp relay-agent option-82 allow-untrusted
-----------------------------------------------------

**Minimum user role:** operator

To allow untrusted client requests with DHCPv4 Relay Agent Information Option (option 82) on the interface:

**Command syntax: allow-untrusted [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent option-82

**Note**

- Default behavior when the relay agent receives a DHCPv4 packet with giaddr zero is to drop it, unless allow-untrusted mode is enabled.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                                      | Range        | Default  |
+=============+==================================================================================+==============+==========+
| admin-state | Received DHCP packets may contain Relay Agent Information Option with giaddr     | | enabled    | disabled |
|             | zero                                                                             | | disabled   |          |
+-------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# option-82
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# allow-untrusted enabled


**Removing Configuration**

To return DHCPv4 relay agent information option allow-untrusted configuration on the interface to its default value:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# no allow-untrusted

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/option-82/check-reply.rst

interfaces dhcp relay-agent option-82 check-reply
-------------------------------------------------

**Minimum user role:** operator

To enforce validation of the DHCPV4 Relay Agent Information Option (option 82) on the interface:

**Command syntax: check-reply [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent option-82

**Parameter table**

+-------------+---------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                         | Range        | Default  |
+=============+=====================================================================+==============+==========+
| admin-state | Enable validation of option 82 in replies received from DHCP server | | enabled    | disabled |
|             |                                                                     | | disabled   |          |
+-------------+---------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# option-82
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# check-reply enabled


**Removing Configuration**

To return DHCPV4 relay agent information option check-reply configuration on the interface to its default value:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# no check-reply

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/option-82/circuit-id.rst

interfaces dhcp relay-agent option-82 circuit-id
------------------------------------------------

**Minimum user role:** operator

To overwrite the default DHCPv4 Relay Agent Information Option (option 82) circuit ID sub-option on the interface:

**Command syntax: circuit-id [circuit-id]**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent option-82

**Note**

- Unless explicitly overwritten by the user, the default value is the interface-name.
- User configured string may only contain alphanumeric characters, underscores, hyphens, dots, forward slashes, backslashes and colons.

**Parameter table**

+------------+----------------------------------------------------------------------------------+-----------------+----------------+
| Parameter  | Description                                                                      | Range           | Default        |
+============+==================================================================================+=================+================+
| circuit-id | Encodes an agent-local identifier of the circuit from which a DHCP               | | string        | interface-name |
|            | client-to-server packet was received. It is intended for use by agents in        | | length 1-63   |                |
|            | relaying DHCP responses back to the proper circuit. The circuit ID is an opaque  |                 |                |
|            | value                                                                            |                 |                |
+------------+----------------------------------------------------------------------------------+-----------------+----------------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# option-82
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# circuit-id myCircuit


**Removing Configuration**

To return DHCPv4 relay agent information option circuit ID sub-option configuration on the interface to its default value:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# no circuit-id

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/option-82/link-selection.rst

interfaces dhcp relay-agent option-82 link-selection
----------------------------------------------------

**Minimum user role:** operator

"To set the DHCPv4 relay agent option-82, sub-option 5, link-selection as specified in RFC 3527:"

**Command syntax: link-selection [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent option-82

**Note**

- The default behavior is to add link-selection sub option with option 82.

- The sub-option is added when enabled and when option-82 is required (option-insert enabled).

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter   | Description                                                                      | Range        | Default |
+=============+==================================================================================+==============+=========+
| admin-state | Support option-82 sub option 5 - link-selection to reflect client ingress        | | enabled    | enabled |
|             | interface ipv4 address                                                           | | disabled   |         |
+-------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# option-82
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# link-selection enabled


**Removing Configuration**

To revert link-selection sub-option usage to default state:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# no link-selection

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.10   | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/option-82/option-82.rst

interfaces dhcp relay-agent option-82
-------------------------------------

**Minimum user role:** operator

To enter DHCPv4 relay agent's Relay Agent Information Option configuration mode:

**Command syntax: option-82**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# option-82
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)#


**Removing Configuration**

To remove the DHCPv4 relay agent's Relay Agent Information Option configuration:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# no option-82

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/option-82/option-insert.rst

interfaces dhcp relay-agent option-82 option-insert
---------------------------------------------------

**Minimum user role:** operator

To enable the DHCPv4 Relay Agent Information Option (option 82) on the interface:

**Command syntax: option-insert [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent option-82

**Parameter table**

+-------------+-------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                             | Range        | Default  |
+=============+=========================================================================+==============+==========+
| admin-state | Enable sending the DHCP option for Relay Agent information -- option 82 | | enabled    | disabled |
|             |                                                                         | | disabled   |          |
+-------------+-------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# option-82
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# option-insert enabled


**Removing Configuration**

To return DHCPv4 relay agent information option admin-state on the interface to its default value:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# no option-insert

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/option-82/policy.rst

interfaces dhcp relay-agent option-82 policy
--------------------------------------------

**Minimum user role:** operator

To set the DHCPv4 relay agent policy for the Relay Agent Information Option (option 82) on the interface:

**Command syntax: policy [policy]**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent option-82

**Parameter table**

+-----------+--------------------------------------------+-------------+---------+
| Parameter | Description                                | Range       | Default |
+===========+============================================+=============+=========+
| policy    | Define the Relay Agent's forwarding policy | | replace   | replace |
|           |                                            | | keep      |         |
|           |                                            | | drop      |         |
+-----------+--------------------------------------------+-------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# option-82
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# policy replace


**Removing Configuration**

To return DHCPv4 relay agent information option policy configuration on the interface to its default value:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# no policy

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/option-82/remote-id.rst

interfaces dhcp relay-agent option-82 remote-id
-----------------------------------------------

**Minimum user role:** operator

To overwrite the default DHCPv4 Relay Agent Information Option (option 82) remote ID sub-option on the interface:

**Command syntax: remote-id [remote-id]**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent option-82

**Note**

- Unless explicitly overwritten by the user, the default value is the MAC address of the relaying port.
- User configured string may only contain alphanumeric characters, underscores, hyphens, dots, forward slashes, backslashes and colons.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+-----------------+-------------+
| Parameter | Description                                                                      | Range           | Default     |
+===========+==================================================================================+=================+=============+
| remote-id | Provides a mechanism to identify the remote host end of the circuit. The remote  | | string        | MAC address |
|           | ID should be thought of as an opaque value, but must be globally unique          | | length 1-63   |             |
+-----------+----------------------------------------------------------------------------------+-----------------+-------------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# option-82
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# remote-id myRemoteID


**Removing Configuration**

To return DHCPv4 relay agent information option remote ID sub-option configuration on the interface to its default value:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# no remote-id

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/option-82/subscriber-id.rst

interfaces dhcp relay-agent option-82 subscriber-id
---------------------------------------------------

**Minimum user role:** operator

To set the default DHCPv4 Relay Agent Information Option (option 82) subscriber ID sub-option on the interface:

**Command syntax: subscriber-id [subscriber-id]**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent option-82

**Note**

- User configured string may only contain alphanumeric characters, underscores, hyphens, dots, forward slashes, backslashes and colons.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+-----------------+---------+
| Parameter     | Description                                                                      | Range           | Default |
+===============+==================================================================================+=================+=========+
| subscriber-id | Allows DHCP relay agent to associate a stable Subscriber ID with DHCP client     | | string        | \-      |
|               | messages in a way that is independent of the client and of the underlying        | | length 1-63   |         |
|               | physyical network infrastructure                                                 |                 |         |
+---------------+----------------------------------------------------------------------------------+-----------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# option-82
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# subscriber-id mySubscriberID


**Removing Configuration**

To renive DHCPv4 relay agent information option subscriber ID sub-option configuration on the interface:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay-option-82)# no subscriber-id

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/server.rst

interfaces dhcp relay-agent server
----------------------------------

**Minimum user role:** operator

To configure target DHCPv4 servers for the relay agent:

**Command syntax: server [ip-address]** [, ip-address, ip-address]

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent

**Note**

- Up to 8 DHCPv4 servers may be configured for a relay agent

**Parameter table**

+------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter  | Description                                                                      | Range   | Default |
+============+==================================================================================+=========+=========+
| ip-address | List of IPv4 addresses of DHCP servers to which the relay agent should forward   | A.B.C.D | \-      |
|            | DHCPv4 requests. The relay agent is expected to forward DHCPv4/BOOTP requests to |         |         |
|            | all listed server addresses when DHCPv4 relaying is enabled globally, or on the  |         |         |
|            | interface                                                                        |         |         |
+------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# server 10.10.10.10, 20.20.20.20


**Removing Configuration**

To remove all DHCP servers from the list:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# no server

To remove a specific DHCP server from the list:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# no server 10.10.10.10

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/source-interface.rst

interfaces dhcp relay-agent source-interface
--------------------------------------------

**Minimum user role:** operator

"To set the source interface for the relay agent to relay IPv4 addresses:"

**Command syntax: source-interface [source-interface]**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent

**Note**

- The default behavior is to impose IPv4 source address matching of the ingress interface that received the DHCPv4 messages.

- The IPv4 address must be configured for the selected interface.

- When the link-selection sub-option is in use the source-interface will be impose a GI address field.

**Parameter table**

+------------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter        | Description                                                                      | Range            | Default |
+==================+==================================================================================+==================+=========+
| source-interface | The source-interface the relay agent uses as a source address to relay messages. | | string         | \-      |
|                  |                                                                                  | | length 1-255   |         |
+------------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# source-interface lo0


**Removing Configuration**

To revert to default behavior:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# no source-interface

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.10   | Command introduced |
+---------+--------------------+

---

## interface/dhcp_relay-agent/vrf.rst

interfaces dhcp relay-agent vrf
-------------------------------

**Minimum user role:** operator

To configure target VRF for all DHCPv4 servers of the relay agent interface:

**Command syntax: vrf [vrf-name]**

**Command mode:** config

**Hierarchies**

- interfaces dhcp relay-agent

**Note**

- In case that destination VRF is configured, it shall apply to all DHCPv4 servers on the relay agent interface. If not configured, then all DHCPv4 servers must be in the same VRF as the relaying interface.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter | Description                                                                      | Range            | Default |
+===========+==================================================================================+==================+=========+
| vrf-name  | The name of the VRF instance of the DHCPv4 servers (if different from the        | | string         | \-      |
|           | interface VRF)                                                                   | | length 1-255   |         |
+-----------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcp relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# vrf MyVRF_2


**Removing Configuration**

To remove the destination VRF configuration:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# no vrf

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+

---

## interface/dhcpv6_relay-agent/admin-state.rst

interfaces dhcpv6 relay-agent admin-state
-----------------------------------------

**Minimum user role:** operator

To enable DHCPv6 relay agent on the interface:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces dhcpv6 relay-agent

**Note**

- At least one DHCPv6 server must be configured to enable the relay agent on the interface.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                                      | Range        | Default  |
+=============+==================================================================================+==============+==========+
| admin-state | Enables the relay agent on the referenced interface. At least one server address | | enabled    | disabled |
|             | should also be configured for forwarding requests                                | | disabled   |          |
+-------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcpv6 relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# admin-state enabled


**Removing Configuration**

To return DHCPv6 relay agent admin-state on the interface to its default value:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# no admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.10   | Command introduced |
+---------+--------------------+

---

## interface/dhcpv6_relay-agent/dhcpv6_relay-agent.rst

interfaces dhcpv6 relay-agent
-----------------------------

**Minimum user role:** operator

To enter DHCPv6 relay agent configuration mode:

**Command syntax: dhcpv6 relay-agent**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - IRB

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcpv6 relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)#


**Removing Configuration**

To remove the DHCPv6 relay agent configuration:
::

    dnRouter(cfg-if-ge100-0/0/0)# no dhcpv6 relay-agent

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.10   | Command introduced |
+---------+--------------------+

---

## interface/dhcpv6_relay-agent/options/interface-id.rst

interfaces dhcpv6 relay-agent options interface-id
--------------------------------------------------

**Minimum user role:** operator

"To set the DHCPv6 option 18 Interface ID, as specified in RFC 8415:"

**Command syntax: interface-id [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces dhcpv6 relay-agent options

**Note**

- The default behavior is to add the interface ID option to relayed DHCPv6 messages. This option is currently only supported in NC-AI.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter   | Description                                                                      | Range        | Default |
+=============+==================================================================================+==============+=========+
| admin-state | Relay Agent Interface-ID (option 18) — An ASCII string that identifies the       | | enabled    | enabled |
|             | interface on which the client DHCPv6 packet is received.                         | | disabled   |         |
+-------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcpv6 relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# options
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay-options)# interface-id enabled


**Removing Configuration**

To revert the interface-id option configuration to its default value:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay-options)# no interface-id

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+

---

## interface/dhcpv6_relay-agent/options/options.rst

interfaces dhcpv6 relay-agent options
-------------------------------------

**Minimum user role:** operator

To enter DHCPv6 relay agent's options configuration mode:

**Command syntax: options**

**Command mode:** config

**Hierarchies**

- interfaces dhcpv6 relay-agent

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcpv6 relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# options
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay-options)#


**Removing Configuration**

To remove the DHCPv6 relay agent's options configuration:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# no options

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+

---

## interface/dhcpv6_relay-agent/server.rst

interfaces dhcpv6 relay-agent server
------------------------------------

**Minimum user role:** operator

To configure target DHCPv6 servers for the relay agent:

**Command syntax: server [ipv6-address]** [, ipv6-address, ipv6-address]

**Command mode:** config

**Hierarchies**

- interfaces dhcpv6 relay-agent

**Note**

- Up to 2 DHCPv6 servers may be configured for a relay agent.

**Parameter table**

+--------------+----------------------------------------------------------------------------------+----------+---------+
| Parameter    | Description                                                                      | Range    | Default |
+==============+==================================================================================+==========+=========+
| ipv6-address | List of IPv6 addresses of DHCP servers to which the relay agent should forward   | X:X::X:X | \-      |
|              | DHCPv6 requests. The relay agent is expected to forward DHCPv6/BOOTP requests to |          |         |
|              | all listed server addresses when DHCPv6 relaying is enabled globally, or on the  |          |         |
|              | interface                                                                        |          |         |
+--------------+----------------------------------------------------------------------------------+----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcpv6 relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# server faba:bb00::10:10:10:10


**Removing Configuration**

To remove all DHCP servers from the list:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# no server

To remove a specific DHCP server from the list:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcp-relay)# no server faba:bb00::10:10:10:10

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.10   | Command introduced |
+---------+--------------------+

---

## interface/dhcpv6_relay-agent/source-interface.rst

interfaces dhcpv6 relay-agent source-interface
----------------------------------------------

**Minimum user role:** operator

"To set the source interface for the relay agent to relay IPv6 addresses:"

**Command syntax: source-interface [source-interface]**

**Command mode:** config

**Hierarchies**

- interfaces dhcpv6 relay-agent

**Note**

- The default behavior is to impose IPv6 source address matching of the ingress interface that received the DHCPv6 messages.

**Parameter table**

+------------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter        | Description                                                                      | Range            | Default |
+==================+==================================================================================+==================+=========+
| source-interface | The source-interface the relay agent uses as a source address to relay messages. | | string         | \-      |
|                  |                                                                                  | | length 1-255   |         |
+------------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcpv6 relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# source-interface lo0


**Removing Configuration**

To revert to default behavior:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# no source-interface

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.10   | Command introduced |
+---------+--------------------+

---

## interface/dhcpv6_relay-agent/vrf.rst

interfaces dhcpv6 relay-agent vrf
---------------------------------

**Minimum user role:** operator

To configure the target VRF for all DHCPv6 servers of the relay agent interface:

**Command syntax: vrf [vrf-name]**

**Command mode:** config

**Hierarchies**

- interfaces dhcpv6 relay-agent

**Note**

- In case that destination VRF is configured, it shall apply to all DHCPv6 servers on the relay agent interface. If not configured, then all DHCPv6 servers must be in the same VRF as the relaying interface.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter | Description                                                                      | Range            | Default |
+===========+==================================================================================+==================+=========+
| vrf-name  | The name of the VRF instance of the DHCPv6 servers (if different from the        | | string         | \-      |
|           | interface VRF)                                                                   | | length 1-255   |         |
+-----------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcpv6 relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# vrf MyVRF_2


**Removing Configuration**

To remove the destination VRF configuration:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# no vrf

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/install-default-route.rst

interfaces ndp router-advertisement install-default-route
---------------------------------------------------------

**Minimum user role:** operator

If set, installs an IPv6 default route to the router next-hop as a result of receiving a valid router-advertisement on this interface.
To set install-default-route:

**Command syntax: install-default-route**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement

**Note**
- The command is applicable only if ipv6-admin-state is enabled.
- This command is only supported for ``irb`` interfaces.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# irb1
    dnRouter(cfg-if-irb1)# ndp router-advertisement
    dnRouter(cfg-if-irb1-ndp-ra)# install-default-route


**Removing Configuration**

To clear install-default-route behavior:
::

    dnRouter(cfg-if-irb1-ndp-ra)# no install-default-route

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.2    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/admin-state.rst

interfaces ndp router-advertisement prefix-advertisement admin-state
--------------------------------------------------------------------

**Minimum user role:** operator

Once enabled, the router will send router-advertisement icmpv6 messages over the interface.
Router-advertisement messages will be sent over the interface periodically, and upon reception of valid Router solicitation messages.
To enable router-advertisement prefix-advertisement:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Note**

- The interface must be enabled for IPv6, either with LLA only or with global IPv6 address configured

- When prefix-advertisement admin-state is enabled, the router-advertisement install-default-route must be disabled.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                                      | Range        | Default  |
+=============+==================================================================================+==============+==========+
| admin-state | Indicating whether or not the router sends periodic Router Advertisements and    | | enabled    | disabled |
|             | responds to Router Solicitations.                                                | | disabled   |          |
+-------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)#


**Removing Configuration**

To revert the admin-state to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/advertise-mtu.rst

interfaces ndp router-advertisement prefix-advertisement advertise-mtu
----------------------------------------------------------------------

**Minimum user role:** operator

When enabled, send the MTU option under Router Advertisement.
The MTU option will include information about interface ipv6 mtu value.
To enable advertise-mtu:

**Command syntax: advertise-mtu [advertise-mtu]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Parameter table**

+---------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter     | Description                                                                      | Range        | Default  |
+===============+==================================================================================+==============+==========+
| advertise-mtu | Configure if to include MTU option in transmitted router advertisements. The MTU | | enabled    | disabled |
|               | option is used in Router Advertisement messages to ensure that all nodes on a    | | disabled   |          |
|               | link use the same MTU value in those cases where the link MTU is not well known. |              |          |
+---------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# advertise-mtu enabled


**Removing Configuration**

To revert the advertise-mtu to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no advertise-mtu

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/interval.rst

interfaces ndp router-advertisement prefix-advertisement interval max
---------------------------------------------------------------------

**Minimum user role:** operator

To configure the interval for periodic router-advertisement transmissions:
- max - The maximum time, in seconds, allowed between sending unsolicited Multicast Router Advertisements from the interface. The default is 600 seconds.
- min - The minimum time, in seconds, allowed between sending unsolicited Multicast Router Advertisements from the interface. For max >= 9sec, the default is 0.33max, otherwise thr defualt is 0.75max.

**Command syntax: interval max [interval-max]** min [interval-min]

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Note**

- min must be <= 0.75*max.

**Parameter table**

+--------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter    | Description                                                                      | Range   | Default |
+==============+==================================================================================+=========+=========+
| interval-max | The maximum time allowed between sending unsolicited multicast Router            | 4-65535 | 600     |
|              | Advertisements from the interface.                                               |         |         |
+--------------+----------------------------------------------------------------------------------+---------+---------+
| interval-min | The minimum time allowed between sending unsolicited multicast Router            | 3-1350  | \-      |
|              | Advertisements from the interface.  The default value to be used operationally   |         |         |
|              | if this leaf is not configured is determined as follows:  - if                   |         |         |
|              | max-rtr-adv-interval >= 9 seconds, the default value is 0.33 \*                  |         |         |
|              | max-rtr-adv-interval;  - otherwise, it is 0.75 \* max-rtr-adv-interval.          |         |         |
+--------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# interval max 1500
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# interval max 1500 min 1000


**Removing Configuration**

To revert the interval max to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no interval max

To revert the interval min to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no interval max 1500 min

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/managed-addr-config.rst

interfaces ndp router-advertisement prefix-advertisement managed-addr-config
----------------------------------------------------------------------------

**Minimum user role:** operator

Once enabled, set the M flag in router-advertisement advertisements.
M flag set indicates receiving neighbors that addresses are available via DHCPv6 and stateful configuration should be used.
To enable managed-addr-config:

**Command syntax: managed-addr-config [managed-addr-config]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Parameter table**

+---------------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter           | Description                                                                      | Range        | Default  |
+=====================+==================================================================================+==============+==========+
| managed-addr-config | The value to be placed in the 'Managed address configuration' flag field in the  | | enabled    | disabled |
|                     | Router Advertisement.                                                            | | disabled   |          |
+---------------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# managed-addr-config enabled


**Removing Configuration**

To revert the managed-addr-config to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no managed-addr-config

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/other-config.rst

interfaces ndp router-advertisement prefix-advertisement other-config
---------------------------------------------------------------------

**Minimum user role:** operator

Once enabled, set the O flag in router-advertisement advertisements.
O flag set indicates receiving neighbors that other information is available via stateful protocol (DHCPv6) such as DNS-related information.
To enable other-config:

**Command syntax: other-config [other-config]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Note**

- Setting O flag is redundant if M flag is set

**Parameter table**

+--------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter    | Description                                                                      | Range        | Default  |
+==============+==================================================================================+==============+==========+
| other-config | The value to be placed in the 'Other configuration' flag field in the Router     | | enabled    | disabled |
|              | Advertisement.                                                                   | | disabled   |          |
+--------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# other-config enabled


**Removing Configuration**

To revert the other-config to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no other-config

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/preference.rst

interfaces ndp router-advertisement prefix-advertisement preference
-------------------------------------------------------------------

**Minimum user role:** operator

Preference allows a neighbor to prefer a given router router-advertisements.
To configure the local router advertised preference value:

**Command syntax: preference [preference]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Parameter table**

+------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter  | Description                                                                      | Range      | Default |
+============+==================================================================================+============+=========+
| preference | Default router preferences and preferences for more-specific routes. 2-bit       | | medium   | medium  |
|            | signed integer.  Indicates whether to prefer this router over other default      | | high     |         |
|            | routers.  If the Router Lifetime is zero, the preference value MUST be set to    | | low      |         |
|            | (00) by the sender and MUST be ignored by the receiver.  If the Reserved (10)    |            |         |
|            | value is received, the receiver MUST treat the value as if it were (00).         |            |         |
+------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# preference high


**Removing Configuration**

To revert the preference to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no preference

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/prefix-advertisement.rst

interfaces ndp router-advertisement prefix-advertisement
--------------------------------------------------------

**Minimum user role:** operator

The router-advertisement prefix-advertisement configuration defines the router support of transmitting router-advertisement Neighbor Discovery messages over the ipv6 supporting interface.
To enter the prefix-advertisement configuration level:

**Command syntax: prefix-advertisement**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)#


**Removing Configuration**

To clear all prefix-advertisement settings:
::

    - dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# no prefix-advertisement

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/prefix/autonomous-config.rst

interfaces ndp router-advertisement prefix-advertisement prefix autonomous-config
---------------------------------------------------------------------------------

**Minimum user role:** operator

When set, indicates that this prefix can be used for stateless address configuration.
To configure autonomous-config:

**Command syntax: autonomous-config [autonomous-config]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement prefix

**Parameter table**

+-------------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter         | Description                                                                      | Range        | Default |
+===================+==================================================================================+==============+=========+
| autonomous-config | The value to be placed in the Autonomous Flag field in the Prefix Information    | | enabled    | enabled |
|                   | option.                                                                          | | disabled   |         |
+-------------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# prefix 2006:18:91::48/127
    dnRouter(cfg-ndp-ra-pr-adv-prefix)# autonomous-config disabled


**Removing Configuration**

To revert the autonomous-config to its default value:
::

    dnRouter(cfg-ndp-ra-pr-adv-prefix)# no autonomous-config

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/prefix/no-advertise.rst

interfaces ndp router-advertisement prefix-advertisement prefix no-advertise
----------------------------------------------------------------------------

**Minimum user role:** operator

Suppress advertisement of this prefix from Router Advertisement prefix information.
Prefix information will not be transmitted even when the prefix belongs to an interface.

**Command syntax: no-advertise**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement prefix

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# prefix 2006:18:91::48/127
    dnRouter(cfg-ndp-ra-pr-adv-prefix)# no-advertise


**Removing Configuration**

To unset no-advertise:
::

    dnRouter(cfg-ndp-ra-pr-adv-prefix)# no no-advertise

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/prefix/preferred-lifetime.rst

interfaces ndp router-advertisement prefix-advertisement prefix preferred-lifetime
----------------------------------------------------------------------------------

**Minimum user role:** operator

Value to be placed in the Preferred Lifetime in the Prefix Information option, in seconds.
Preferred Lifetime is the length of time during which the address can be used freely as both a source and a destination address for traffic exchanges with other devices.
Preferred Lifetime must be equal to or less than the Valid Lifetime.
If this time expires without the address being refreshed, the address becomes deprecated and should be replaced with a new, preferred address. New sessions cannot use the address obtained by this prefix.
To set the signaled prefix information Preferred-lifetime for Router Advertisement:

**Command syntax: preferred-lifetime [preferred-lifetime]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement prefix

**Note**

- valid-lifetime must be equal to or greater than the preferred-lifetime.

- preferred-lifetime value 4294967295 means infinity.

**Parameter table**

+--------------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter          | Description                                                                      | Range        | Default |
+====================+==================================================================================+==============+=========+
| preferred-lifetime | The value to be placed in the Preferred Lifetime in the Prefix Information       | 0-4294967295 | 604800  |
|                    | option. The designated value of all 1's (0xffffffff) represents infinity.        |              |         |
+--------------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# prefix 2006:18:91::48/127
    dnRouter(cfg-ndp-ra-pr-adv-prefix)# preferred-lifetime 2500000


**Removing Configuration**

To revert the preferred-lifetime to its default value:
::

    dnRouter(cfg-ndp-ra-pr-adv-prefix)# no preferred-lifetime

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/prefix/prefix.rst

interfaces ndp router-advertisement prefix-advertisement prefix
---------------------------------------------------------------

**Minimum user role:** operator

A list of prefixes to be placed in the Prefix Information options in Router Advertisement messages, sent from the interface.
By default, all interface configured global addresses are advertised as prefix information (the link local address is not advertised).
Users may set a locally configured IPv6 prefix to modify its related prefix option attributes.
Users may configure additional prefixes to be sent in Router Advertisement.
To configure a prefix and enter its configuration level:

**Command syntax: prefix [ipv6-prefix]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Note**
- A configured prefix can have both network and host bits set.
- Only the subnet is advertised, i.e., bits not within the prefix-length will be zero.
- Cannot configure (commit validation) multiple prefixes from the same subnet.

**Parameter table**

+-------------+----------------------+------------+---------+
| Parameter   | Description          | Range      | Default |
+=============+======================+============+=========+
| ipv6-prefix | IPv6 address prefix. | X:X::X:X/x | \-      |
+-------------+----------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# prefix 2006:18:91::48/127
    dnRouter(cfg-ndp-ra-pr-adv-prefix)#


**Removing Configuration**

To remove prefixes:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no prefix 

To remove a specific prefix:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no prefix 2006:18:91::48/127

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/prefix/valid-lifetime.rst

interfaces ndp router-advertisement prefix-advertisement prefix valid-lifetime
------------------------------------------------------------------------------

**Minimum user role:** operator

Value to be placed in the Valid Lifetime in the Prefix Information option, in seconds.
Valid Lifetime is the total time the address is available.
Valid Lifetime must be equal to or greater than the Preferred Lifetime.
The valid lifetime enables sessions to continue for transactions that began before the address became deprecated (end of Preferred Lifetime). 
However, in this time frame the address should no longer be used for new sessions. 
If this time expires without the deprecated address being refreshed, the address becomes invalid and may be assigned to another interface.
To set the signaled prefix information valid-lifetime for Router Advertisement:

**Command syntax: valid-lifetime [valid-lifetime]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement prefix

**Note**

- valid-lifetime must be equal or greater than the preferred-lifetime

- valid-lifetime value 4294967295 means infinity.

**Parameter table**

+----------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter      | Description                                                                      | Range        | Default |
+================+==================================================================================+==============+=========+
| valid-lifetime | The value to be placed in the Valid Lifetime in the Prefix Information option.   | 0-4294967295 | 2592000 |
|                | The designated value of all 1's (0xffffffff) represents infinity.                |              |         |
+----------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# prefix 2006:18:91::48/127
    dnRouter(cfg-ndp-ra-pr-adv-prefix)# valid-lifetime 3000000


**Removing Configuration**

To revert the valid-lifetime to its default value:
::

    dnRouter(cfg-ndp-ra-pr-adv-prefix)# no valid-lifetime

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/ndp_router-advertisement/prefix-advertisement/router-lifetime.rst

interfaces ndp router-advertisement prefix-advertisement router-lifetime
------------------------------------------------------------------------

**Minimum user role:** operator

Value to be placed in the Router Lifetime field of the Router Advertisements sent from the interface, in seconds.
A value of zero indicates that the router is not to be used as a default router.
Router-lifetime default value is 3*(interval max).
To configure the router-lifetime:

**Command syntax: router-lifetime [router-lifetime]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Note**

- router-lifetime must be >= interval max

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter       | Description                                                                      | Range   | Default |
+=================+==================================================================================+=========+=========+
| router-lifetime | The value to be placed in the Router Lifetime field of Router Advertisements     | 0-65535 | \-      |
|                 | sent from the interface, in seconds.  It MUST be either zero or between          |         |         |
|                 | max-rtr-adv-interval and 9000 seconds.  A value of zero indicates that the       |         |         |
|                 | router is not to be used as a default router.  These limits may be overridden by |         |         |
|                 | specific documents that describe how IPv6 operates over different link layers.   |         |         |
|                 | If this parameter is not configured, the device SHOULD use a value of 3 \*       |         |         |
|                 | max-rtr-adv-interval.                                                            |         |         |
+-----------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# router-lifetime 2000


**Removing Configuration**

To revert the router-lifetime to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no router-lifetime

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interface/tracking-policy.rst

interfaces tracking-group action
--------------------------------

**Minimum user role:** operator

Configure this interface to track one of the defined tracking groups. According to the state of
the objects in the tracking group (for example all objects have failed) then the action defined here (example: laser off)
will be applied to this interface. When the objects in the tracking group recover then the reverse action (example: laser on)
will be implemented.

**Command syntax: tracking-group [if-tracking-group-name] action [action]**

**Command mode:** config

**Hierarchies**

- interfaces

**Parameter table**

+------------------------+-------------------------------------------------------------------+-----------------+-----------+
| Parameter              | Description                                                       | Range           | Default   |
+========================+===================================================================+=================+===========+
| if-tracking-group-name | The name of the tracking group                                    | | string        | \-        |
|                        |                                                                   | | length 1-63   |           |
+------------------------+-------------------------------------------------------------------+-----------------+-----------+
| action                 | Action to be performed when the tracked group conditions are met. | laser-off       | laser-off |
+------------------------+-------------------------------------------------------------------+-----------------+-----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# tracking-group tracking-group1 action laser-off
    dnRouter(cfg-if-ge400-0/0/0)#


**Removing Configuration**

::

    dnRouter(cfg-if-ge400-0/0/0)# no tracking-group

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.1    | Command introduced |
+---------+--------------------+

---

## interface/transceivers/application.rst

interfaces transceiver application
----------------------------------

**Minimum user role:** operator

Sets the operational mode according to CMIS application. To configure the transceiver application:

**Command syntax: application {media-name [media-name], media-code [media-code], host-name [host-name], host-code [host-code], class-name [class-name]}**

**Command mode:** config

**Hierarchies**

- interfaces transceiver

**Note**

- Both Media and Host applications could be configured using either name or code. If both are configured, code value will be used and the configured name will be ignored.

**Parameter table**

+------------+---------------------------------------------------+-----------------------+---------+
| Parameter  | Description                                       | Range                 | Default |
+============+===================================================+=======================+=========+
| media-name | Optical module CMIS application name              | | UNDEFINED           | \-      |
|            |                                                   | | 10GBASE-SW          |         |
|            |                                                   | | 10GBASE-SR          |         |
|            |                                                   | | 25GBASE-SR          |         |
|            |                                                   | | 40GBASE-SR4         |         |
|            |                                                   | | 40GE-SWDM4          |         |
|            |                                                   | | 40GE-BiDi           |         |
|            |                                                   | | 50GBASE-SR          |         |
|            |                                                   | | 100GBASE-SR10       |         |
|            |                                                   | | 100GBASE-SR4        |         |
|            |                                                   | | 100GE-SWDM4         |         |
|            |                                                   | | 100GE-BiDi          |         |
|            |                                                   | | 100GBASE-SR2        |         |
|            |                                                   | | 100GBASE-SR         |         |
|            |                                                   | | 100GBASE-VR         |         |
|            |                                                   | | 200GBASE-SR4        |         |
|            |                                                   | | 200GBASE-SR2        |         |
|            |                                                   | | 200GBASE-VR2        |         |
|            |                                                   | | 400GBASE-SR16       |         |
|            |                                                   | | 400GBASE-SR8        |         |
|            |                                                   | | 400GBASE-SR4        |         |
|            |                                                   | | 400GBASE-VR4        |         |
|            |                                                   | | 800G-SR8            |         |
|            |                                                   | | 800G-VR8            |         |
|            |                                                   | | 400GBASE-SR4.2      |         |
|            |                                                   | | 800GBASE-VR4.2      |         |
|            |                                                   | | 800GBASE-SR4.2      |         |
|            |                                                   | | 10GBASE-LW          |         |
|            |                                                   | | 10GBASE-EW          |         |
|            |                                                   | | 10G-ZW              |         |
|            |                                                   | | 10GBASE-LR          |         |
|            |                                                   | | 10GBASE-ER          |         |
|            |                                                   | | 10GBASE-BR          |         |
|            |                                                   | | 10G-ZR              |         |
|            |                                                   | | 25GBASE-LR          |         |
|            |                                                   | | 25GBASE-ER          |         |
|            |                                                   | | 25GBASE-BR          |         |
|            |                                                   | | 40GBASE-LR4         |         |
|            |                                                   | | 40GBASE-FR          |         |
|            |                                                   | | 50GBASE-FR          |         |
|            |                                                   | | 50GBASE-LR          |         |
|            |                                                   | | 50GBASE-ER          |         |
|            |                                                   | | 50GBASE-BR          |         |
|            |                                                   | | 100GBASE-LR4        |         |
|            |                                                   | | 100GBASE-ER4        |         |
|            |                                                   | | 100G-PSM4           |         |
|            |                                                   | | 100G-CWDM4-OCP      |         |
|            |                                                   | | 100G-CWDM4          |         |
|            |                                                   | | 100G-4WDM-10        |         |
|            |                                                   | | 100G-4WDM-20        |         |
|            |                                                   | | 100G-4WDM-40        |         |
|            |                                                   | | 100GBASE-DR         |         |
|            |                                                   | | 100GBASE-FR         |         |
|            |                                                   | | 100GBASE-LR         |         |
|            |                                                   | | 100G-LR1-20         |         |
|            |                                                   | | 100G-ER1-30         |         |
|            |                                                   | | 100G-ER1-40         |         |
|            |                                                   | | 100GBASE-ZR         |         |
|            |                                                   | | 200GBASE-DR4        |         |
|            |                                                   | | 200GBASE-FR4        |         |
|            |                                                   | | 200GBASE-LR4        |         |
|            |                                                   | | 200GBASE-ER4        |         |
|            |                                                   | | 400GBASE-FR8        |         |
|            |                                                   | | 400GBASE-LR8        |         |
|            |                                                   | | 400GBASE-ER8        |         |
|            |                                                   | | 400GBASE-DR4        |         |
|            |                                                   | | 400GBASE-FR4        |         |
|            |                                                   | | 400GBASE-LR4-6      |         |
|            |                                                   | | 400GBASE-LR4-10     |         |
|            |                                                   | | 400GBASE-ZR         |         |
|            |                                                   | | 800GBASE-DR8        |         |
|            |                                                   | | 800GBASE-DR8-2      |         |
|            |                                                   | | 400ZR-amplified     |         |
|            |                                                   | | 400ZR-unamplified   |         |
|            |                                                   | | ZR400-OFEC-16QAM    |         |
|            |                                                   | | ZR300-OFEC-8QAM     |         |
|            |                                                   | | ZR200-OFEC-QPSK     |         |
|            |                                                   | | ZR100-OFEC-QPSK     |         |
|            |                                                   | | UNSUPPORTED         |         |
+------------+---------------------------------------------------+-----------------------+---------+
| media-code | Optical module CMIS application media code in hex | \-                    | \-      |
+------------+---------------------------------------------------+-----------------------+---------+
| host-name  | Optical module CMIS host application name         | | UNDEFINED           | \-      |
|            |                                                   | | 400GAUI-8-C2M       |         |
|            |                                                   | | 400GBASE-CR8        |         |
|            |                                                   | | 200GAUI-4-C2M       |         |
|            |                                                   | | 200GBASE-CR4        |         |
|            |                                                   | | 100GAUI-2-C2M       |         |
|            |                                                   | | 100GBASE-CR2        |         |
|            |                                                   | | CAUI-4-C2M          |         |
|            |                                                   | | 100GBASE-CR4        |         |
|            |                                                   | | 100GAUI-4-C2M       |         |
+------------+---------------------------------------------------+-----------------------+---------+
| host-code  | Optical module CMIS application host code in hex  | \-                    | \-      |
+------------+---------------------------------------------------+-----------------------+---------+
| class-name | User defined application identifier               | | string              | \-      |
|            |                                                   | | length 1-255        |         |
+------------+---------------------------------------------------+-----------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-4/1/1
    dnRouter(cfg-if-ge400-4/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# application media-name ZR400-OFEC-16QAM
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-4/1/1
    dnRouter(cfg-if-ge400-4/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# application media-code C8
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-4/1/1
    dnRouter(cfg-if-ge400-4/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# application host-name 400GAUI-8-C2M
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-4/1/1
    dnRouter(cfg-if-ge400-4/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# application host-code 11
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-4/1/1
    dnRouter(cfg-if-ge400-4/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# application class-name my-400GZR+


**Removing Configuration**

::

    dnRouter(cfg-if-ge400-4/1/1-trns)# no application

**Command History**

+---------+------------------------------------------------------+
| Release | Modification                                         |
+=========+======================================================+
| 16.2    | Command introduced                                   |
+---------+------------------------------------------------------+
| 17.1    | Added support for more transceivers                  |
+---------+------------------------------------------------------+
| TBD     | added option for media and host name and code config |
+---------+------------------------------------------------------+

---

## interface/transceivers/optical-transport/center-frequency.rst

interfaces transceiver optical-transport center-frequency
---------------------------------------------------------

**Minimum user role:** operator

Some coherent optics modules allow setting optical channel frequency. Frequency grid is specified in GHz according to Rec. ITU-T G.694.1. To set the optical channel frequency:

**Command syntax: center-frequency [center-frequency] [units]**

**Command mode:** config

**Hierarchies**

- interfaces transceiver optical-transport

**Note**
- No decimals allowed only whole numbers in mhz,ghz,thz.

**Parameter table**

+------------------+----------------------------------+--------------+---------+
| Parameter        | Description                      | Range        | Default |
+==================+==================================+==============+=========+
| center-frequency | Optical channel center frequency | 0-4294967295 | \-      |
+------------------+----------------------------------+--------------+---------+
| units            |                                  | | mhz        | mhz     |
|                  |                                  | | ghz        |         |
|                  |                                  | | thz        |         |
+------------------+----------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-2/1/1
    dnRouter(cfg-if-ge400-42/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# optical-transport
    dnRouter(cfg-if-ge400-4/1/1-trns-optical-transport)# center-frequency 193100


**Removing Configuration**

To revert the center frequency configuration to the default value:
::

    dnRouter(cfg-if-ge400-4/1/1-trns-optical-transport)# no center-frequency

**Command History**

+---------+-------------------------+
| Release | Modification            |
+=========+=========================+
| 16.2    | Command introduced      |
+---------+-------------------------+
| 18.1    | Changed frequency range |
+---------+-------------------------+

---

## interface/transceivers/optical-transport/grid-spacing.rst

interfaces transceiver optical-transport grid-spacing
-----------------------------------------------------

**Minimum user role:** operator

Some coherent optics modules allow setting optical channel grid spacing. Frequency grid is specified in GHz according to Rec. ITU-T G.694.1. To set the optical channel grid-spacing:

**Command syntax: grid-spacing [grid-spacing]**

**Command mode:** config

**Hierarchies**

- interfaces transceiver optical-transport

**Parameter table**

+--------------+------------------------------+--------------+---------+
| Parameter    | Description                  | Range        | Default |
+==============+==============================+==============+=========+
| grid-spacing | Optical channel grid-spacing | | 3.125GHz   | \-      |
|              |                              | | 6.25GHz    |         |
|              |                              | | 12.5GHz    |         |
|              |                              | | 25GHz      |         |
|              |                              | | 33GHz      |         |
|              |                              | | 50GHz      |         |
|              |                              | | 75GHz      |         |
|              |                              | | 100GHz     |         |
+--------------+------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-2/1/1
    dnRouter(cfg-if-ge400-42/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# optical-transport
    dnRouter(cfg-if-ge400-4/1/1-trns-optical-transport)# grid-spacing 100GHz


**Removing Configuration**

To revert the grid spacing configuration to the default value:
::

    dnRouter(cfg-if-ge400-4/1/1-trns-optical-transport)# no grid-spacing

**Command History**

+---------+--------------------------------+
| Release | Modification                   |
+=========+================================+
| 16.2    | Command introduced             |
+---------+--------------------------------+
| 18.1    | Added grid-spacing frequencies |
+---------+--------------------------------+

---

## interface/transceivers/optical-transport/optical-transport.rst

interfaces transceiver optical-transport
----------------------------------------

**Minimum user role:** operator

"The transceiver hierarchy supports various transceiver configuration options including:
- Different applications (as advertised by the transceiver)
- Coherent transceiver parameters configuration (optical frequency, output power etc.)"

**Command syntax: optical-transport**

**Command mode:** config

**Hierarchies**

- interfaces transceiver

**Note**

- The command is applicable to physical interfaces.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-2/1/1
    dnRouter(cfg-if-ge400-2/1/1)# transceiver
    dnRouter(cfg-if-ge100-2/1/1-trns)# optical-transport
    dnRouter(cfg-if-ge100-2/1/1-trns-optical-transport)#


**Removing Configuration**

To remove the optical-transport configuration:
::

    dnRouter(cfg-if-ge100-2/1/1-trns-optical-transport)# no optical-transport

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## interface/transceivers/optical-transport/target-output-power.rst

interfaces transceiver optical-transport target-output-power
------------------------------------------------------------

**Minimum user role:** operator

Some coherent optics modules allow setting optical channel target output power. Power range is -20..10 and specified in dbm (dbm). To set the optical channel output power:

**Command syntax: target-output-power [target-output-power]**

**Command mode:** config

**Hierarchies**

- interfaces transceiver optical-transport

**Parameter table**

+---------------------+----------------------------------------------------+--------------+---------+
| Parameter           | Description                                        | Range        | Default |
+=====================+====================================================+==============+=========+
| target-output-power | Target optical output power range is -20..10 (dbm) | -20.00-10.00 | \-      |
+---------------------+----------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-2/1/1
    dnRouter(cfg-if-ge400-42/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# optical-transport
    dnRouter(cfg-if-ge400-4/1/1-trns-optical-transport)# target-output-power -10


**Removing Configuration**

To revert target output power configuration to the default value:
::

    dnRouter(cfg-if-ge400-4/1/1-trns-optical-transport)# no target-output-power

**Command History**

+---------+--------------------------------+
| Release | Modification                   |
+=========+================================+
| 16.2    | Command introduced             |
+---------+--------------------------------+
| 18.0    | Units changed from dmbm to dbm |
+---------+--------------------------------+

---

## interface/transceivers/transceivers.rst

interfaces transceiver
----------------------

**Minimum user role:** operator

The transceiver hierarchy supports various transceiver configuration options including:
- Different applications (as advertised by the transceiver)
- Coherent transceiver parameters configuration (optical frequency, output power etc.)

**Command syntax: transceiver**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to physical interfaces.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-2/1/1
    dnRouter(cfg-if-ge400-2/1/1)# transceiver


**Removing Configuration**

::

    dnRouter(cfg-if-ge100-2/1/1-trns)# no transceiver

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## interfaces access-list eth.rst

interfaces access-list eth direction
------------------------------------

**Minimum user role:** operator

After creating an access-list, you can link it to an interface. 
When applying an access-list to an interface, you must specify whether it is to be applied to inbound or outbound traffic. 
You can configure only one access-list per direction for each access-list type.
The attachment of the policy to the interface will be rejected.

To apply an access-list to an interface, use the following command:

**Command syntax: access-list eth [access-list-name] direction [direction]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - IRB.

**Parameter table**

+------------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter        | Description                                                                      | Range | Default |
+==================+==================================================================================+=======+=========+
| access-list-name | Specify the name of an existing access-list. This access-list will serve as a    | \-    | \-      |
|                  | global access-list.                                                              |       |         |
+------------------+----------------------------------------------------------------------------------+-------+---------+
| direction        | The direction of the traffic to which to apply the access-list. For mgmt         | in    | \-      |
|                  | interfaces, you can configure only an ingress access-list.                       |       |         |
+------------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# access-list eth MyAccess-list-eth direction in

    dnRouter(cfg-if)# bundle-1.10
    dnRouter(cfg-if-bundle-1.10)# access-list eth MyAccess-list-eth direction in

    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# access-list eth MyAccess-list-eth direction in

    dnRouter(cfg-if)# ge100-1/1/1.20
    dnRouter(cfg-if-ge100-1/1/1.20)# access-list eth MyAccess-list-eth direction in

    dnRouter(cfg-if)# irb0
    dnRouter(cfg-if-irb0)# access-list eth MyAccess-listeth direction in


**Removing Configuration**

To remove all the access lists from the interface:
::

    dnRouter(cfg-if-ge100-1/1/1)# # no access-list

To remove all eth access-lists from the interface:
::

    dnRouter(cfg-if-ge100-1.20)# no access-list eth

To remove a specific access-list from the interface:
::

    dnRouter(cfg-if-bundle-2)# no access-list eth MyAccess-listeth

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interfaces access-list ipv4.rst

interfaces access-list ipv4 direction
-------------------------------------

**Minimum user role:** operator

After creating an access-list, you can link it to an interface. 
When applying an access-list to an interface, you must specify whether it is to be applied to inbound or outbound traffic. 
You can configure only one access-list per direction for each access-list type.
The attachment of the policy to the interface will be rejected.


To apply an access-list to an interface, use the following command:

**Command syntax: access-list ipv4 [access-list-name] direction [direction]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - mgmt0
  - mgmt-ncc-X
  - IRB.

**Parameter table**

+------------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter        | Description                                                                      | Range   | Default |
+==================+==================================================================================+=========+=========+
| access-list-name | Specify the name of an existing access-list. This access-list will serve as a    | \-      | \-      |
|                  | global access-list.                                                              |         |         |
+------------------+----------------------------------------------------------------------------------+---------+---------+
| direction        | The direction of the traffic to which to apply the access-list. For mgmt         | | in    | \-      |
|                  | interfaces, you can configure only an ingress access-list.                       | | out   |         |
+------------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# access-list ipv4 MyAccess-listv4 direction in

    dnRouter(cfg-if)# bundle-1.10
    dnRouter(cfg-if-bundle-1.10)# access-list ipv4 MyAccess-listv4 direction out

    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# access-list ipv4 MyAccess-listv4 direction in

    dnRouter(cfg-if)# ge100-1/1/1.20
    dnRouter(cfg-if-ge100-1/1/1.20)# access-list ipv4 MyAccess-listv4 direction out

    dnRouter(cfg-if)# bundle-2
    dnRouter(cfg-if-bundle-2)# access-list ipv4 MyAccess-listv4 direction in


**Removing Configuration**

To remove all the access lists from the interface:
::

    dnRouter(cfg-if-ge100-1/1/1)# # no access-list

To remove all ipv4 access-lists from the interface:
::

    dnRouter(cfg-if-ge100-1.20)# no access-list ipv4

To remove a specific access-list from the interface:
::

    dnRouter(cfg-if-bundle-2)# no access-list ipv4 MyAccess-listv4

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces; applied new hierarchy |
+---------+--------------------------------------------------------------------+
| 11.1    | Added direction out                                                |
+---------+--------------------------------------------------------------------+
| 16.2    | Split from interfaces access-list                                  |
+---------+--------------------------------------------------------------------+

---

## interfaces access-list ipv6.rst

interfaces access-list ipv6 direction
-------------------------------------

**Minimum user role:** operator

After creating an access-list, you can link it to an interface. When applying an access-list to an interface, you must specify whether it is to be applied to inbound or outbound traffic. You can configure only one access-list per direction for each access-list type.

Access-list-type IPv6 direction out does not support the following access-list rule parameters:

-	Traffic class (TC)
-	Hop-limit
-	TCP-flags
-	Fragmented

The attachment of the policy to the interface will be rejected.


To apply an access-list to an interface, use the following command:

**Command syntax: access-list ipv6 [access-list-name] direction [direction]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - mgmt0
  - mgmt-ncc-X
  - IRB

**Parameter table**

+------------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter        | Description                                                                      | Range   | Default |
+==================+==================================================================================+=========+=========+
| access-list-name | Specify the name of an existing access-list. This access-list will serve as a    | \-      | \-      |
|                  | global access-list.                                                              |         |         |
+------------------+----------------------------------------------------------------------------------+---------+---------+
| direction        | The direction of the traffic to which to apply the access-list. For mgmt         | | in    | \-      |
|                  | interfaces, you can configure only an ingress access-list.                       | | out   |         |
+------------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces

    dnRouter(cfg-if)# bundle-2
    dnRouter(cfg-if-bundle-2)# access-list ipv6 MyAccess-listv6 direction out


**Removing Configuration**

To remove all the access lists from the interface:
::

    dnRouter(cfg-if-ge100-1/1/1)# # no access-list

To remove all ipv6 access-lists from the interface:
::

    dnRouter(cfg-if-ge100-1.20)# no access-list ipv6

To remove a specific access-list from the interface:
::

    dnRouter(cfg-if-bundle-2)# no access-list ipv6 MyAccess-listv6

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces; applied new hierarchy |
+---------+--------------------------------------------------------------------+
| 11.1    | Added direction out                                                |
+---------+--------------------------------------------------------------------+
| 16.2    | Split from interfaces access-list                                  |
+---------+--------------------------------------------------------------------+

---

## interfaces admin-state.rst

interfaces admin-state
----------------------

**Minimum user role:** operator

Sets the administrative state of the interface. When a physical or bundle interface is disabled, the interface's laser signal is shut down. When a sub-interface is disabled, the interface IPv4/IPv6 address is unreachable and traffic cannot be forwarded via this interface (in either direction). When a bundle interface is disabled, the admin-state of the bundle members remains "enabled" and their operational state changes to "down".

To enable/disable an interface, set the admin-state parameter using the following command:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan
  - Loopback
  - mgmt0
  - mgmt-ncc-X
  - mgmt-ncc-X/X
  - Control
  - Fabric
  - Console
  - IPMI
  - Physical smartNIC (SGE)
  - IRB
  - ICE.

- All NNI/UNI physical interfaces are initialized with admin-state Disabled.

- Mgmt and control interfaces are initialized with admin-state Enabled.

- All logical interfaces (Loopback, sub-physical, bundle, sub-bundle) are initialized with admin-state Enabled.

**Parameter table**

+-------------+-------------------------------------------------+--------------+-----------------------------------------+
| Parameter   | Description                                     | Range        | Default                                 |
+=============+=================================================+==============+=========================================+
| admin-state | Sets the administrative state of the interface. | | enabled    | | -Enabled for logical/ctrl/mgmt/ice    |
|             |                                                 | | disabled   | | -Disabled for physical                |
+-------------+-------------------------------------------------+--------------+-----------------------------------------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# admin-state disabled

    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# admin-state enabled

    dnRouter(cfg-if)# bundle-1.4
    dnRouter(cfg-if-bundle-1.4)# admin-state enabled

    dnRouter(cfg-if)# ctrl-ncp-0/0
    dnRouter(cfg-if-ctrl-ncp-0/0)# admin-state enabled

    dnRouter(cfg-if)# ice0
    dnRouter(cfg-if-ice0)# admin-state disabled
    Notice: Continuing with the commit will cause the following:
    The following commit will disable the Intra Cluster Exchange interface. Proceeding with this commit will disable the communication channel between NCPs and may cause loss of synchronization and traffic.
    Enter yes to continue with commit, no to abort commit (yes/no) [no]


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-bundle-1.4)# no admin-state

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces; applied new hierarchy |
+---------+--------------------------------------------------------------------+
| 10.0    | Changed the default admin-state for physical interfaces            |
+---------+--------------------------------------------------------------------+
| 17.0    | Added support for NCM control ports                                |
+---------+--------------------------------------------------------------------+

---

## interfaces arp.rst

interfaces arp host-address mac-address
---------------------------------------

**Minimum user role:** operator

You can add static entries to the ARP table. Static entries are permanent (unless they are manually removed) and take precedence over dynamic updates. To add a static ARP entry, use the following command in configuration mode:

**Command syntax: arp host-address [host-ipv4-address] mac-address [mac-address]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan
  - IRB

- Gratuitous ARP is supported by default on all interfaces.

- Dynamic ARP entries remain in the ARP cache for 60 seconds.

- The command is not available to loopback interface.

- The host-ipv4-address is always a /32 ipv4-address.

**Parameter table**

+-------------------+------------------------------------------------------------------+-------------------+---------+
| Parameter         | Description                                                      | Range             | Default |
+===================+==================================================================+===================+=========+
| host-ipv4-address | The IPv4 address of the host device being added to the ARP table | A.B.C.D           | \-      |
+-------------------+------------------------------------------------------------------+-------------------+---------+
| mac-address       | The MAC address for the host device being added to the ARP table | xx:xx:xx:xx:xx:xx | \-      |
+-------------------+------------------------------------------------------------------+-------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# arp host-address 1.2.3.4 mac-address ab:ab:ab:ab:ab:ab

    dnRouter(cfg-if)# ge100-1/1/2
    dnRouter(cfg-if-ge100-1/1/2)# arp host-address 1.2.3.5 mac-address ab:ab:ab:ab:ab:ab

    dnRouter(cfg-if)# ge100-1/1/1.100
    dnRouter(cfg-if-ge100-1/1/1.100)# arp host-address 10.100.10.1 mac-address ab:ab:ab:ab:ab:ab

    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# arp host-address 10.100.10.1 mac-address ab:ab:ab:ab:ab:ab

    dnRouter(cfg-if)# bundle-1.100
    dnRouter(cfg-if-bundle-1.100)# arp host-address 20.20.20.2 mac-address ab:ab:ab:ab:ab:ab


**Removing Configuration**

To remove a static ARP entry for the interface:
::

    dnRouter(cfg-if-ge10-1/1/1)# no arp

To remove a static ARP entry for a specific ipv4-address:
::

    dnRouter(cfg-if-ge100-1/1/1)# no arp host-address 1.2.3.5

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces, applied new hierarchy |
+---------+--------------------------------------------------------------------+
| 11.0    | Changed syntax from ipv4-address to host-address                   |
+---------+--------------------------------------------------------------------+

---

## interfaces ber-sd admin-state.rst

interfaces ber-sd admin-state
-----------------------------

**Minimum user role:** operator

Sets the administrative state of the BER Signal Degrade alarm on the interface.

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces ber-sd

**Note**
- The command is applicable only to 400G and 100G physical interfaces with FEC.
- By default all applicable interfaces are initialized with ber-sd admin-state disabled.
- When enabled and the configured ber-sd threshold is exceeded, then a system event shall be generated to notify of the violation, thus indicating signal degredation on the link.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                                      | Range        | Default  |
+=============+==================================================================================+==============+==========+
| admin-state | Enable Signal Degrade BER and generate an alarm whenever the SD-BER threshold is | | enabled    | disabled |
|             | crossed for this interface                                                       | | disabled   |          |
+-------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ber-sd admin-state enabled
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ber-sd admin-state disabled


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ber-sd admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.2    | Command introduced |
+---------+--------------------+

---

## interfaces ber-sd threshold.rst

interfaces ber-sd threshold
---------------------------

**Minimum user role:** operator

Sets the Bit Error Rate threshold for the Signal Degrade alarm on the interface.

**Command syntax: threshold [signal-degrade-threshold]**

**Command mode:** config

**Hierarchies**

- interfaces ber-sd

**Note**
- The command is applicable only to 400G and 100G physical interfaces with FEC.
- By default the Signal Degrade Bit Error Rate threshold is set to 1e-8.
- When enabled and the configured ber-sd threshold is exceeded, then a system event shall be generated to notify of the violation, thus indicating signal degradation on the link.

**Parameter table**

+--------------------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter                | Description                                                                      | Range | Default |
+==========================+==================================================================================+=======+=========+
| signal-degrade-threshold | Set the Signal Degrade bit error rate threshold on an interface to a value of    | 5-13  | 8       |
|                          | 1e-x, where x is the value passed in here                                        |       |         |
+--------------------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ber-sd threshold 11


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ber-sd threshold

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.2    | Command introduced |
+---------+--------------------+

---

## interfaces ber-sd.rst

interfaces ber-sd
-----------------

**Minimum user role:** operator

To enter Signal Degrade alarm configuration level on an interface:

**Command syntax: ber-sd**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**
- The command is applicable only to 400G and 100G physical interfaces with FEC.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ber-sd
    dnRouter(cfg-if-ge100-1/1/1-sd)#


**Removing Configuration**

To revert Signal Degrade settings to their default values:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ber-sd

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.2    | Command introduced |
+---------+--------------------+

---

## interfaces ber-sf admin-state.rst

interfaces ber-sf admin-state
-----------------------------

**Minimum user role:** operator

Sets the administrative state of the BER Signal Failure alarm on the interface.

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces ber-sf

**Note**
- The command is applicable only to 400G and 100G physical interfaces with FEC.
- By default all applicable interfaces are initialized with ber-sf admin-state enabled.
- When enabled and the configured ber-sf threshold is exceeded, then a system event shall be generated to notify of the violation, thus indicating signal failure on the link, the interface shall transition to operational down state, and a remote fault signal shall be sent to the peer.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                                      | Range        | Default  |
+=============+==================================================================================+==============+==========+
| admin-state | Disable Signal Failure BER and the generation of an alarm whenever the SF-BER    | | enabled    | disabled |
|             | threshold is crossed for this interface                                          | | disabled   |          |
+-------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ber-sf admin-state disabled

    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ber-sf admin-state enabled


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ber-sf admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.2    | Command introduced |
+---------+--------------------+

---

## interfaces ber-sf threshold.rst

interfaces ber-sf threshold
---------------------------

**Minimum user role:** operator

Sets the Bit Error Rate threshold for the Signal Failure alarm on the interface.

**Command syntax: threshold [signal-fail-threshold]**

**Command mode:** config

**Hierarchies**

- interfaces ber-sf

**Note**
- The command is applicable only to 400G and 100G physical interfaces with FEC.
- By default the Signal Failure Bit Error Rate threshold is set to 1e-5.
- When enabled and the configured ber-sf threshold is exceeded, then a system event shall be generated to notify of the violation, thus indicating signal failure on the link, the interface shall transition to operational down state, and a remote fault signal shall be sent to the peer.

**Parameter table**

+-----------------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter             | Description                                                                      | Range | Default |
+=======================+==================================================================================+=======+=========+
| signal-fail-threshold | Set the Signal Failure bit error rate threshold on an interface to a value of    | 5-13  | 5       |
|                       | 1e-x, where x is the value passed in here                                        |       |         |
+-----------------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ber-sf threshold 6


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ber-sf threshold

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.2    | Command introduced |
+---------+--------------------+

---

## interfaces ber-sf.rst

interfaces ber-sf
-----------------

**Minimum user role:** operator

To enter Signal Failure alarm configuration level on an interface:

**Command syntax: ber-sf**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**
- The command is applicable only to 400G and 100G physical interfaces with FEC.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ber-sf
    dnRouter(cfg-if-ge100-1/1/1-sf)#


**Removing Configuration**

To revert Signal Failure settings to their default values:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ber-sf

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.2    | Command introduced |
+---------+--------------------+

---

## interfaces breakout.rst

interfaces breakout
-------------------

**Minimum user role:** operator

1. NCP-40C port breakout
100GE ports 0..19 of each NCP-40c can be broken out into 4x10GE ports using an external breakout cable. When port 0 is broken out, port 21 is disabled, and similarly each 100GE port broken up disables one associated 100GE port, per the table below:

+-----------------+------------------------------+
| Port broken-out | Port disabled as a result    |
+=================+==============================+
| 0               | 21                           |
+-----------------+------------------------------+
| 1               | 20                           |
+-----------------+------------------------------+
| 2               | 23                           |
+-----------------+------------------------------+
| 3               | 22                           |
+-----------------+------------------------------+
| 4               | 25                           |
+-----------------+------------------------------+
| 5               | 24                           |
+-----------------+------------------------------+
| 6               | 27                           |
+-----------------+------------------------------+
| 7               | 26                           |
+-----------------+------------------------------+
| 8               | 29                           |
+-----------------+------------------------------+
| 9               | 28                           |
+-----------------+------------------------------+
| 10              | 31                           |
+-----------------+------------------------------+
| 11              | 30                           |
+-----------------+------------------------------+
| 12              | 33                           |
+-----------------+------------------------------+
| 13              | 32                           |
+-----------------+------------------------------+
| 14              | 35                           |
+-----------------+------------------------------+
| 15              | 34                           |
+-----------------+------------------------------+
| 16              | 37                           |
+-----------------+------------------------------+
| 17              | 36                           |
+-----------------+------------------------------+
| 18              | 39                           |
+-----------------+------------------------------+
| 19              | 38                           |
+-----------------+------------------------------+

The 4 10GE ports are named ge10-<f>/<n>/<p>/<b>, where b is the breakout port 0..3, with the same forwarder (f), slot number (n) and port (p) of their parent. For example ge100-1/0/2 is broken up to ge10-1/0/2/0, ge10-1/0/2/1, ge10-1/0/2/2 and ge10-1/0/2/3.

The operative state of both the breakout port and the associated disabled port will be set to 'not present'.
When a port is broken-out, the configuration of the port and the associated disabled port are erased and set to default. The 10GE ports configuration is erased from the database once a 'no breakout' command is issued, and the 10GE ports will be removed completely, i.e. they will not be present in 'show interfaces' output or its equivalent.

The breakout command will fail validation if either of the following conditions are not met:
- Both the broken out port and the associated port admin status must be down.
- Both ports must not be members of a LAG. The ports must be removed from the LAG prior to breakout.
- Both ports must not be configured to run any routing or control protocol, e.g. ISIS, OSPF, RSVP, LACP, etc. The protocl configuration must be removed prior to breakout.

The 'no breakout' command will fail validation if either of the following conditions are not met:
- All 4 10GE ports admin status must be down.
- All 4 10GE ports must not be members of a LAG. The ports must be removed from the LAG prior to cancelling breakout.
- All 4 10GE ports must not be configured to run any routing or control protocol, e.g. ISIS, OSPF, RSVP, LACP, etc. The protocl configuration must be removed prior to breakout.

2. NCP-36CD(-S) and NCP-36CD-S-SA port breakout
400GE ports 0..35 of each NCP-36cd can be broken out into 4x100GE, 2x200GE or 2x100GE ports using an external breakout cable. All 400GE NIF ports can breakout to 4x100GE 2x200GE or 2x100GE. No sacrificed ports. The naming convention is similar to 10GE breakout: ge<100/200>-<f>/<n>/<p>/<b>, where b is the breakout port 0..3 (See above for details). All other definitions as detailed above apply, apart from sacrificed ports.

3. NCP-32CD port breakout
400GE ports 0..31 of each NCP-32CD can be broken out into 4x100GE or 2x100GE ports using an external breakout cable. All 400GE NIF ports can breakout to 4x100GE or 2x100GE. No sacrificed ports. The naming convention is similar to 10GE breakout: ge<100/200>-<f>/<n>/<p>/<b>, where b is the breakout port 0..3 (See above for details). All other definitions as detailed above apply, apart from sacrificed ports.

4. NCP-18E port breakout
800GE ports 0..17 can be broken out into 4x200GE or 2x400GE or 4x100GE ports using an external breakout cable. The naming convention is: ge<100/200/400>-<f>/<n>/<p>/<b>, where b is the breakout port 0..3 or 0..1. All other definitions as detailed above apply, apart from sacrificed ports.

**Command syntax: breakout [breakout-mode]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The maximal number of 10G port in any cluster size is limited to 80 ports.

- No limitation on the number of 100G/200G breakout ports.

**Parameter table**

+---------------+-------------------------------+-------------+---------+
| Parameter     | Description                   | Range       | Default |
+===============+===============================+=============+=========+
| breakout-mode | The method used for breakout. | | none      | none    |
|               |                               | | 10g-4x    |         |
|               |                               | | 100g-4x   |         |
|               |                               | | 200g-2x   |         |
|               |                               | | 200g-4x   |         |
|               |                               | | 100g-2x   |         |
|               |                               | | 400g-2x   |         |
+---------------+-------------------------------+-------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# breakout 10g-4x

    dnRouter# configure
    dnRouter(cfg)# interfaces ge100-0/0/0 breakout 10g-4x
    dnRouter(cfg)# no interfaces ge100-0/0/0 breakout 10g-4x
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# breakout 100g-4x
    dnRouter(cfg-if-ge400-0/0/0)# no breakout

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 breakout 100g-4x

    dnRouter(cfg)# no interfaces ge400-0/0/0 breakout 100g-4x
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# breakout 200g-2x
    dnRouter(cfg-if-ge400-0/0/0)# no breakout

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 breakout 200g-2x
    dnRouter(cfg)# no interfaces ge400-0/0/0 breakout 200g-2x
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# breakout 100g-2x
    dnRouter(cfg-if-ge400-0/0/0)# no breakout

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 breakout 100g-2x
    dnRouter(cfg)# no interfaces ge400-0/0/0 breakout 100g-2x


**Removing Configuration**

To remove an interface breakout:
::

    dnRouter(cfg-if-ge100-0/0/0)# no breakout

**Command History**

+---------+------------------------------------------------------------------------+
| Release | Modification                                                           |
+=========+========================================================================+
| 12.0    | Command introduced                                                     |
+---------+------------------------------------------------------------------------+
| 16.1    | Added support for 400GE interface breakout                             |
+---------+------------------------------------------------------------------------+
| 17.1    | Added support for 400GE to 2x200G interface breakout                   |
+---------+------------------------------------------------------------------------+
| 17.3    | Added support for 400GE to 2x100G interface breakout                   |
+---------+------------------------------------------------------------------------+
| 25.1    | Added support for 800GE to 2x400G & 4x200G & 4x100G interface breakout |
+---------+------------------------------------------------------------------------+

---

## interfaces bundle flap-suppression.rst

interfaces flap-suppression
---------------------------

**Minimum user role:** operator

Set the flap suppression timer on the bundle interface, to delay the transition of the bundle interface to operational down state by allowing available standby links
to take the place of failed active links.

To configure the flap suppression timer on the bundle interface:

**Command syntax: flap-suppression [flap-suppression]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to bundle interfaces.

- Flap-suppression is not applicable in cases of transitions from operational down state to operational up state; nor from operational up state to operational down state when there are no standby interfaces available at all.

**Parameter table**

+------------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter        | Description                                                                      | Range | Default |
+==================+==================================================================================+=======+=========+
| flap-suppression | Timer (in seconds) to suppress bundle transition to operational down state when  | 0-300 | \-      |
|                  | it does not have any standby links available.                                    |       |         |
+------------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# flap-suppression 5


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1)# no flap-suppression

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interfaces bundle max-links.rst

interfaces max-links
--------------------

**Minimum user role:** operator

Set the maximum number of interface members that can be active for the aggregate interface (bundle) at a given time.
Interface members are selected to be active according to their port-priority configuration.
An interface member not selected to be active in the aggregate interface will be in standby and will not pass traffic. In case an active member fails, a standby member will be used.
The max-link configuration is independent of LACP configuration.
If LACP is not enabled, the max-link configuration must be identical on both ends of the bundle link.
If LACP is enabled, the LACP state-machine takes precedence over the LAG selection mechanism.
To configure the maximum number of active links in the bundle interface:

**Command syntax: max-links [max-links]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to bundle interfaces.

- Max-links must be greater or equal to min-links. Commit validation expected

**Parameter table**

+-----------+----------------------------------------------------------------------------------+-------+---------+
| Parameter | Description                                                                      | Range | Default |
+===========+==================================================================================+=======+=========+
| max-links | Set the maximum number of interface members that can be active for the aggregate | 1-64  | 64      |
|           | interface (bundle) at a given time. An interface member not selected to be       |       |         |
|           | active in the aggregate interface will be in standby and will not pass traffic   |       |         |
+-----------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# max-links 1


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1)# no max-links

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interfaces bundle min-bandwidth.rst

interfaces min-bandwidth
------------------------

**Minimum user role:** operator

You can set the minimum bandwidth required for the bundle interface to be available (operational status "up"). This option is particularly useful if you have a bundle interface with two links (e.g. one 400Gbps link and another 100Gbps link). The total bandwidth of the bundle interface in this example is 500Gbps, but min-links may not be enough.

If min-links is configured, both configurations apply. That is, if min-links is set to 2 and min-bandwidth is set to 100Gbps, then the operational status of the bundle interface in the above example will be "down" if the 100Gbps link goes down, even though the minimum bandwidth condition is met.

The min-bandwidth configuration is independent of LACP configuration. If LACP is not enabled, the min-bandwidth configuration must be identical on both ends of the bundle link. If LACP is enabled, the LACP state-machine takes precedence over the LAG selection mechanism.

To configure the minimum bandwidth for an aggregated Ethernet bundle:

**Command syntax: min-bandwidth [min-bandwidth]** [units]

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to bundle interfaces.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter     | Description                                                                      | Range        | Default |
+===============+==================================================================================+==============+=========+
| min-bandwidth | The minimum bandwidth for the aggregated bundle interface. 0 means no bandwidth  | 0-6400000000 | 0       |
|               | restriction on the bundle; min-bandwidth will never be triggered.                |              |         |
+---------------+----------------------------------------------------------------------------------+--------------+---------+
| units         | The units used for bandwidth. If you do not specify the unit, kbps will be used. | | kbps       | kbps    |
|               |                                                                                  | | mbps       |         |
|               |                                                                                  | | gbps       |         |
+---------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# min-bandwidth 10000 mbps
    dnRouter(cfg-if-bundle-1)# min-bandwidth 1200000 kbps
    dnRouter(cfg-if-bundle-1)# min-bandwidth 1234567890


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1)# no min-bandwidth

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 10.0    | Command introduced |
+---------+--------------------+

---

## interfaces bundle min-links.rst

interfaces min-links
--------------------

**Minimum user role:** operator

You can set a minimum number of member interfaces that must be active for the bundle interface to be available (operational status "up"). For example, if you have a bundle interface with 5 links of 100GbE, and you set min-links to 3, then if one or two links fail, the bundle will still be operational. However, if three links fail, the entire bundle will be down.

If min-bandwidth is configured, both configurations apply. That is, if min-links is set to 2 and min-bandwidth is set to 100Gbps, then the operational status of the bundle interface in the above example will be "down" if three 100Gbps link go down, even though the minimum bandwidth condition is met if four links fail.

The min-link configuration is independent of LACP configuration. If LACP is not enabled, the min-link configuration must be identical on both ends of the bundle link. If LACP is enabled, the LACP state-machine takes precedence over the LAG selection mechanism.

To configure the minimum number of active links in the bundle interface:

**Command syntax: min-links [min-links]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to bundle interfaces.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+-------+---------+
| Parameter | Description                                                                      | Range | Default |
+===========+==================================================================================+=======+=========+
| min-links | Set the minimum number of interface members that must be active for the          | 1-64  | 1       |
|           | aggregate interface to be available. The operational state of the bundle         |       |         |
|           | interface will remain down until the minimum number of members is reached.       |       |         |
+-----------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# min-links 5


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1)# no min-links

**Command History**

+---------+-------------------------------------------------+
| Release | Modification                                    |
+=========+=================================================+
| 6.0     | Command introduced                              |
+---------+-------------------------------------------------+
| 10.0    | Command moved hierarchy from LACP               |
+---------+-------------------------------------------------+
| 13.1    | Increased maximum number of links from 32 to 64 |
+---------+-------------------------------------------------+

---

## interfaces bundle mixed-type.rst

interfaces mixed-type
---------------------

**Minimum user role:** operator

You can use the following command to configure either a mixed bundle type or none if all members in the bundles are required to be of the same speed. If the bundles allows members of different speeds, the member with the lowest speed allowed in the bundle is determined by the mixed-type. Members of this speed will have weight 1 in the bundle hash resolution, while members of the higher speed will be assigned a weight relative of their speed vs. the speed of the lowest allowed bundle member. Only members with a speed equal to or lower than x10 of the lowest speed member can be added to a 10G-100G mixed-typed bundle, yet 400G members cannot. The total weight of a mixed-type bundle must be less or equal to 64.

+----------------+-------------------+---------------+-------------------------------+---------------------------------+
| Mixed Type     | Possible Members  | Maximal Speed | Maximal Speed Configuration   | Comments                        |
+================+===================+===============+===============================+=================================+
| none           | 10G               | 640Gps        | 64x10G                        |                                 |
+----------------+-------------------+---------------+-------------------------------+---------------------------------+
| none           | 100G              | 6.4Tps        | 64x100G                       |                                 |
+----------------+-------------------+---------------+-------------------------------+---------------------------------+
| none           | 400G              | 6.4Tps        | 16x400G                       | maximum bundle speed limitation |
+----------------+-------------------+---------------+-------------------------------+---------------------------------+
| 10G-100G       | 10G, 100G         | 640Gps        | 64x10G, 54x10G+1x100G, ...    |                                 |
+----------------+-------------------+---------------+-------------------------------+---------------------------------+
| 100G-400G      | 100G, 400G        | 6.4Tps        | 64x100G, 60x100G+1x400G, ...  |                                 |
+----------------+-------------------+---------------+-------------------------------+---------------------------------+

**Command syntax: mixed-type [mixed-type]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to bundle interfaces.

**Parameter table**

+------------+--------------------------------------------------------------+---------------+---------+
| Parameter  | Description                                                  | Range         | Default |
+============+==============================================================+===============+=========+
| mixed-type | Configure which member interfaces are allowed in the bundle. | | none        | none    |
|            |                                                              | | 10G-100G    |         |
|            |                                                              | | 100G-400G   |         |
|            |                                                              | | 1G-10G      |         |
+------------+--------------------------------------------------------------+---------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# mixed-bundle 100G-400G


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1)# no mixed-bundle

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 12.0    | Command introduced |
+---------+--------------------+

---

## interfaces bundle revertive.rst

interfaces revertive
--------------------

**Minimum user role:** operator

When a bundle is configured with max-links (N out of M), N ports are determined as active, the rest as standby.
If an active port is down, a standby port is selected instead.
You can set the revertive behavior for when a higher port-priority member becomes available.
When enabled, when that higher port-priority link becomes operational or a link is added to the aggregated interface that is determined to be higher in priority, it takes precedence over a standby port currently active in the bundle.
To configure revertive behavior:

**Command syntax: revertive [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to bundle interfaces.

- If LACP is not enabled, the revertive configuration must be identical on both ends of the bundle link to prevent misaligned active ports.

**Parameter table**

+-------------+----------------------------------------------+--------------+----------+
| Parameter   | Description                                  | Range        | Default  |
+=============+==============================================+==============+==========+
| admin-state | The revertive state of the bundle interface. | | enabled    | disabled |
|             |                                              | | disabled   |          |
+-------------+----------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# revertive enabled


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1)# no revertive

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interfaces bundle-id.rst

interfaces bundle-id
--------------------

**Minimum user role:** operator

When binding a physical interface to a bundle interface, the physical interface functions as a member of the bundle. You can attach an interface only to an existing bundle.

Only physical interfaces (geX-<f>/<n>/<p>) are allowed.

A bundle can contain only members of the same type (i.e. all members are 10 GbE). Alternatively, a bundle can contain a mixture of physical interfaces of different types/speeds (using the "interfaces mixed-type" command, so that it can have both 100G physical interfaces and 400G physical interfaces simultaneously). The bundle's aggregated maximum speed is 6400Gbps. Traffic is load-balanced over the bundle based on links speeds.

The interface can only be bound to one bundle interface and the bundle interface must exist prior to binding. If you try to bind an interface to a non existing bundle interface, an error is displayed.

Once attached, the physical interface functions as a member in the bundle.

To attach a physical interface to a bundle interface:

**Command syntax: bundle-id [bundle-id]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to physical interfaces.

- Binding a port to a bundle removes all logical configurations (e.g. IP address, MTU) from the physical interface (including any sub-interfaces configured under it). The member interface inherits the configuration from the bundle interface. Only logical configurations related to the member hardware are retained (e.g. led-flash, admin-state). Therefore, unbinding an interface from a bundle, the interface is configured with default parameters only. Any parameters previously configured on the physical interface are not retained.

- The member interface inherits the configuration from the bundle interface.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+---------+---------+
| Parameter | Description                                                                      | Range   | Default |
+===========+==================================================================================+=========+=========+
| bundle-id | Enter the LAG identifier that you have created (see step 1 above) to bind the    | 1-65535 | \-      |
|           | specific physical interface to the bundle.                                       |         |         |
+-----------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# bundle-id 2

    dnRouter(cfg-if)# ge100-1/5/1
    dnRouter(cfg-if-ge100-1/5/1)# bundle-id 4


**Removing Configuration**

This command does not delete the bundle interface.

To unbind an interface from a bundle interface:
::

    dnRouter(cfg-if-ge100-1/5/1)# no bundle-id

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces, applied new hierarchy |
+---------+--------------------------------------------------------------------+
| 7.0     | Removed the keyword "interface" from the syntax                    |
+---------+--------------------------------------------------------------------+

---

## interfaces bundle.rst

interfaces bundle
------------------

**Minimum user role:** operator

The bundle interfaces in DNOS provide datapath connectivity between NCPs. The bundle interfaces are the customer/core interfaces that the user is provisioning. Each bundle will include a member of each of the NCPs, so that all the NCPs are able to send traffic from any ingress interface to any egress interface. Up to 128 enabled bundle interfaces with up to 64 members per bundle can be created. To create a LAG (bundle):

#. Create a bundle interface, using this command.
#. Bind an interface to the bundle using the "interfaces bundle-id" command.

The parameters that you can optionally configure on the bundle interface are the same parameters that you can configure on any interface. If you do not set these parameters, the default values will be assumed. If you configure a parameter on an existing bundle-id, the value of that parameter will be changed. If the bundle-id does not exist, it will be created. The parameters set on the bundle override the parameters of the interface members.

**Command syntax: bundle-<bundle-id>**

**Command mode:** config

**Hierarchies**

- interfaces

**Parameter table**

+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------+
|               |                                                                                                                                                                                                                            |             |            |
| Parameter     | Description                                                                                                                                                                                                                | Range       | Bundle     |
+===============+============================================================================================================================================================================================================================+=============+============+
|               |                                                                                                                                                                                                                            |             |            |
| bundle-id     | The bundle (LAG) identifier. If the ID does not exist, this will create a new bundle interface with the specific identifier. If the ID exists, you will enter the existing bundle interface's configuration mode.          | 1..65535    | \-         |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces
	dnRouter(cfg-if)# bundle-1
	dnRouter(cfg-if-bundle-1)#


**Removing Configuration**

To delete a bundle interface:
::

	dnRouter(cfg-if)# no bundle-1


.. **Help line:** Configures bundle interface

**Command History**

+-------------+-------------------------------------------------------+
|             |                                                       |
| Release     | Modification                                          |
+=============+=======================================================+
|             |                                                       |
| 5.1.0       | Command introduced                                    |
+-------------+-------------------------------------------------------+
|             |                                                       |
| 6.0         | Changed syntax from interface to interfaces           |
|             |                                                       |
|             | Applied new hierarchy                                 |
+-------------+-------------------------------------------------------+
|             |                                                       |
| 7.0         | Removed the keyword "interface" from   the syntax.    |
+-------------+-------------------------------------------------------+
---

## interfaces carrier-delay on-startup interval.rst

interfaces carrier-delay on-startup interval
--------------------------------------------

**Minimum user role:** operator

Use this command on network interfaces to delay their operational status change to "up" when the interface carrier is brought up as a result of any of the following manual operations or events:

- A manual cold or warm system restart (see "request system restart"):

  -	"request system restart"
  -	"request system restart warm"
- A manual cold and warm restart of a specific NCP (see "request system restart"):

  - "request system restart ncp n"
  - "request system restart ncp n warm"
- A manual restart of a container or process:

  - "request system container restart ncp 0 datapath" (see "request system container restart")
  - "request system process restart ncp 0 datapath wb_agent" (see "request system process restart")
- A manual change of the NCP admin-state to "disabled" and back to "enabled" (see "system ncp admin-state")
- After recovering from an NCP system-down state.

To configure the delay time:

**Command syntax: carrier-delay on-startup interval [interval]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to all physical interfaces.

- When interval is set to 0, carrier delay on-startup is disabled.

- If the interval is set while the interface carrier-delay on-startup timer has not yet expired, the new interval value will apply to the next carrier-delay on-startup event.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+--------+---------+
| Parameter | Description                                                                      | Range  | Default |
+===========+==================================================================================+========+=========+
| interval  | The amount of time (in seconds) that the system will wait after the interface is | 0-1800 | 0       |
|           | back up before changing its operational state to "up".                           |        |         |
+-----------+----------------------------------------------------------------------------------+--------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-2/1/1
    dnRouter(cfg-if-ge100-2/1/1)# carrier-delay on-startup interval 1200

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/9
    dnRouter(cfg-if-ge400-0/0/9)# carrier-delay on-startup interval 800


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-2/1/1)# no carrier-delay on-startup interval

::

    dnRouter(cfg-if-ge100-2/1/1)# no carrier-delay

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 13.1    | Command introduced |
+---------+--------------------+

---

## interfaces carrier-delay.rst

interfaces carrier-delay
------------------------

**Minimum user role:** operator

Flapping interfaces may lead to adjacency failures on LDP and IGP protocols, which may dramatically affect the network convergence time and performance. Carrier Delay enables to delay the advertisement of link state change notifications. When the link state changes, a carrier-delay timer is triggered. While the timer is running, any subsequent link state change is ignored. When the timer expires, if the interface has not returned to its original link state, then the router will advertise the link state change. This allows the control protocols to stabilize in case of a flapping link.

The carrier delay feature supports delay for link up and link down notifications.

To configure carrier-delay, use one of the following commands:

**Command syntax: carrier-delay {up [up-time], down [down-time]}**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to all physical interfaces, including breakout.

- Link state change notifications are not issued during the timer countdown; however, the suppressed notifications are logged.

- You can set different up and down timers. Setting either timer to 0 disables the carrier delay feature for the specific links state change. For example, if down-time is set to 0, then when the interface state changes from "up" to "down", the change notification will be advertized immediately.

**Parameter table**

+-----------+------------------------------------------------------------------------+----------+---------+
| Parameter | Description                                                            | Range    | Default |
+===========+========================================================================+==========+=========+
| up-time   | The amount of time (in milliseconds) to delay link-up notifications.   | 0-120000 | 0       |
+-----------+------------------------------------------------------------------------+----------+---------+
| down-time | The amount of time (in milliseconds) to delay link-down notifications. | 0-60000  | 0       |
+-----------+------------------------------------------------------------------------+----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-2/1/1
    dnRouter(cfg-if-ge100-2/1/1)# carrier-delay up 100 down 200

    dnRouter(cfg-if-ge100-2/1/1)# carrier-delay down 100
    dnRouter(cfg-if-ge100-2/1/1)# carrier-delay up 300
    dnRouter(cfg-if-ge100-2/1/1)# carrier-delay down 300 up 200


**Removing Configuration**

To revert the carrier delay configuration to the default value
::

    dnRouter(cfg-if-ge100-2/1/1)# no carrier-delay down

::

    dnRouter(cfg-if-ge100-2/1/1)# no carrier-delay up

::

    dnRouter(cfg-if-ge100-2/1/1)# no carrier-delay

**Command History**

+---------+------------------------+
| Release | Modification           |
+=========+========================+
| 6.0     | Command introduced     |
+---------+------------------------+
| 16.2    | Extended up-time range |
+---------+------------------------+

---

## interfaces console-ncc admin-state.rst

interfaces console-ncc admin-state
----------------------------------

**Minimum user role:** operator

To enable/disable the NCC's console interface:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the console interface.

**Parameter table**

+----------------+--------------------------------------------------------+-------------+-------------+
|                |                                                        |             |             |
| Parameter      | Description                                            | Range       | Default     |
+================+========================================================+=============+=============+
|                |                                                        |             |             |
| admin-state    | The   administrative state of the console interface    | Enabled     | Enabled     |
|                |                                                        |             |             |
|                |                                                        | Disabled    |             |
+----------------+--------------------------------------------------------+-------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# console-ncc-0/0 
	dnRouter(cfg-if-console-ncc-0/0)# admin-state disabled


**Removing Configuration**

To revert to the default state:
::

	dnRouter(cfg-if-console-ncc-0/0)# no admin-state


.. **Help line:** configure console-ncc-<node-id>/0 serial interface

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 10.0        | Command introduced    |
+-------------+-----------------------+

---

## interfaces console-ncc.rst

interfaces console-ncc
----------------------

**Minimum user role:** operator

To configure the NCC's console serial interface, enter its configuration hierarchy:

**Command syntax: console-ncc-<node-id>/0**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the console interface.


**Parameter table**

+---------------+------------------------------------------------+-----------+-------------+
|               |                                                |           |             |
| Parameter     | Description                                    | Range     | Default     |
+===============+================================================+===========+=============+
|               |                                                |           |             |
| node-id       | The ID o fthe node that you want to configure. | 0, 1      | \-          |
+---------------+------------------------------------------------+-----------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# console-ncc-0/0 


**Removing Configuration**

To revert the interface configuration to the default values:
::

	dnRouter(cfg-if)# no console-ncc-0/0 


.. **Help line:** configure console-ncc-0/0 serial interface

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 10.0        | Command introduced    |
+-------------+-----------------------+

---

## interfaces console-ncf admin-state.rst

interfaces console-ncf admin-state
----------------------------------

**Minimum user role:** operator

To enable/disable the NCF's console interface:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the console interface.

**Parameter table**

+----------------+--------------------------------------------------------+-------------+-------------+
|                |                                                        |             |             |
| Parameter      | Description                                            | Range       | Default     |
+================+========================================================+=============+=============+
|                |                                                        |             |             |
| admin-state    | The   administrative state of the console interface    | Enabled     | Enabled     |
|                |                                                        |             |             |
|                |                                                        | Disabled    |             |
+----------------+--------------------------------------------------------+-------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# console-ncf-0/0 
	dnRouter(cfg-if-console-ncf-0/0)# admin-state disabled


**Removing Configuration**

To revert to the default state:
::

	dnRouter(cfg-if-console-ncf-0/0)# no admin-state


.. **Help line:** Configure console-ncf-<node-id>/0 serial interface

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+

---

## interfaces console-ncf.rst

interfaces console-ncf
----------------------

**Minimum user role:** operator

To configure the NCP's console serial interface, enter its configuration hierarchy:

**Command syntax: console-ncf-<node-id>/0**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the console interface.

**Parameter table**

+---------------+------------------------------------------------+-----------+-------------+
|               |                                                |           |             |
| Parameter     | Description                                    | Range     | Default     |
+===============+================================================+===========+=============+
|               |                                                |           |             |
| node-id       | The ID o fthe node that you want to configure. | 0..12     | \-          |
+---------------+------------------------------------------------+-----------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# console-ncf-0/0 


**Removing Configuration**

To revert the interface configuration to the default values:
::

	dnRouter(cfg-if)# no console-ncf-0/0 


.. **Help line:** configure console-ncf-<node-id>/0 serial interface

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+

---

## interfaces console-ncp admin-state.rst

interfaces console-ncp admin-state
----------------------------------

**Minimum user role:** operator

To enable/disable the NCP's console interface:


**Command mode:** config

**Hierarchies**

- interfaces

**Parameter table**

+----------------+--------------------------------------------------------+-------------+-------------+
|                |                                                        |             |             |
| Parameter      | Description                                            | Range       | Default     |
+================+========================================================+=============+=============+
|                |                                                        |             |             |
| admin-state    | The   administrative state of the console interface    | Enabled     | Enabled     |
|                |                                                        |             |             |
|                |                                                        | Disabled    |             |
+----------------+--------------------------------------------------------+-------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# console-ncp-0/0 
	dnRouter(cfg-if-console-ncp-0/0)# admin-state disabled


**Removing Configuration**

To revert to the default state:
::

	dnRouter(cfg-if-console-ncp-0/0)# no admin-state


.. **Help line:** Configure console-ncp-<node-id>/0 serial interface

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+

---

## interfaces console-ncp.rst

interfaces console-ncp
----------------------

**Minimum user role:** operator

To configure the NCP's console serial interface, enter its configuration hierarchy:

**Command syntax: console-ncp-<node-id>/0**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the console interface.

**Parameter table**

+--------------+-----------------------------------------------------+------------------------------+------------+
|              |                                                     |                              |            |
| Parameter    | Description                                         | Range                        | Default    |
+==============+=====================================================+==============================+============+
|              |                                                     |                              |            |
| Node-id      | The ID of the node that you want   to configure.    | 0..47 (per cluster size)     | \-         |
+--------------+-----------------------------------------------------+------------------------------+------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# console-ncp-0/0 


**Removing Configuration**

To revert the interface configuration to the default values:
::

	dnRouter(cfg-if)# no console-ncp-0/0 


.. **Help line:** configure console-ncp-<node-id>/0 serial interface

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+

---

## interfaces dampening admin-state.rst

interfaces dampening admin-state
--------------------------------

**Minimum user role:** operator

To enable/disable interface dampening on the interface:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces dampening

**Note**

- The command is applicable to physical interfaces.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                                      | Range        | Default  |
+=============+==================================================================================+==============+==========+
| admin-state | The administrative state of the dampening feature for the specific interface.    | | enabled    | disabled |
|             | When enabled, advertisement of state changes will act according to the           | | disabled   |          |
|             | configured dampening parameters.                                                 |              |          |
+-------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# dampening
    dnRouter(cfg-if-ge100-1/0/1-dampening)# admin-state enabled
    dnRouter(cfg-if-ge100-1/0/1-dampening)#

    dnRouter# configure
    dnRouter(cfg)# interfaces ge100-1/0/12
    dnRouter(cfg-if-ge100-1/0/12)# dampening
    dnRouter(cfg-if-ge100-1/0/12-dampening)# admin-state disabled
    dnRouter(cfg-if-ge100-1/0/12-dampening)#


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/12-dampening)# no admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.4    | Command introduced |
+---------+--------------------+

---

## interfaces dampening half-life.rst

interfaces dampening half-life
------------------------------

**Minimum user role:** operator

"half-life" defines the amount of time after which the penalty for the interface becomes half of its value.

To configure the half-time threshold:

**Command syntax: half-life [half-life]**

**Command mode:** config

**Hierarchies**

- interfaces dampening

**Note**

- The command is applicable to physical interfaces.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+--------+---------+
| Parameter | Description                                                                      | Range  | Default |
+===========+==================================================================================+========+=========+
| half-life | Half-life time for penalty. The number of seconds after which the penalty for    | 1-3600 | 60      |
|           | the interface becomes half of its value.                                         |        |         |
+-----------+----------------------------------------------------------------------------------+--------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# dampening
    dnRouter(cfg-if-ge100-1/0/1-dampening)# half-life 100
    dnRouter(cfg-if-ge100-1/0/1-dampening)#

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/13
    dnRouter(cfg-if-ge100-1/0/13)# dampening
    dnRouter(cfg-if-ge100-1/0/13-dampening)# half-life 100 reuse-threshold 1100 suppress-threshold 2500 max-suppress 2000
    dnRouter(cfg-if-ge100-1/0/13-dampening)#


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/13-dampening)# no half-life

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.4    | Command introduced |
+---------+--------------------+

---

## interfaces dampening max-suppress.rst

interfaces dampening max-suppress
---------------------------------

**Minimum user role:** operator

This command limits the amount of time that the advertisement of the interface's state is suppressed. To configure the maximum number of seconds that an interface can be suppressed by the device:

**Command syntax: max-suppress [max-suppress]**

**Command mode:** config

**Hierarchies**

- interfaces dampening

**Note**

- The command is applicable to physical interfaces.

**Parameter table**

+--------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter    | Description                                                                      | Range   | Default |
+==============+==================================================================================+=========+=========+
| max-suppress | The maximum number of seconds that an interface can be suppressed by the device. | 2-43200 | 300     |
+--------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# dampening
    dnRouter(cfg-if-ge100-1/0/1-dampening)# max-suppress 250
    dnRouter(cfg-if-ge100-1/0/1-dampening)#

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/13
    dnRouter(cfg-if-ge100-1/0/13)# dampening
    dnRouter(cfg-if-ge100-1/0/13-dampening)# half-life 100 reuse-threshold 1100 suppress-threshold 2500 max-suppress 2000
    dnRouter(cfg-if-ge100-1/0/13-dampening)#


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/13-dampening)# no max-suppress

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.4    | Command introduced |
+---------+--------------------+

---

## interfaces dampening reuse-threshold.rst

interfaces dampening reuse-threshold
------------------------------------

**Minimum user role:** operator

When the dampening threshold falls below the reuse-threshold, the interface becomes available again. To configure the interface dampening reuse threshold:

**Command syntax: reuse-threshold [reuse-threshold]**

**Command mode:** config

**Hierarchies**

- interfaces dampening

**Note**

- The command is applicable to physical interfaces.

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter       | Description                                                                      | Range   | Default |
+=================+==================================================================================+=========+=========+
| reuse-threshold | The minimum threshold below which the interface becomes available again. The     | 1-19999 | 750     |
|                 | value must be lower than the suppress-threshold.                                 |         |         |
+-----------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# dampening
    dnRouter(cfg-if-ge100-1/0/1-dampening)# reuse-threshold 1100
    dnRouter(cfg-if-ge100-1/0/1-dampening)#

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/13
    dnRouter(cfg-if-ge100-1/0/13)# dampening
    dnRouter(cfg-if-ge100-1/0/13-dampening)# half-life 100 reuse-threshold 1100 suppress-threshold 2500 max-suppress 2000
    dnRouter(cfg-if-ge100-1/0/13-dampening)#


**Removing Configuration**

To revert to the default value
::

    dnRouter(cfg-if-ge100-1/0/13-dampening)# no reuse-threshold 1100

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.4    | Command introduced |
+---------+--------------------+

---

## interfaces dampening suppress-threshold.rst

interfaces dampening suppress-threshold
---------------------------------------

**Minimum user role:** operator

Suppress-threshold determines when the advertisement of the interface state starts. To configure the dampening suppress threshold for an interface:

**Command syntax: suppress-threshold [suppress-threshold]**

**Command mode:** config

**Hierarchies**

- interfaces dampening

**Note**

- The command is applicable to physical interfaces.

**Parameter table**

+--------------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter          | Description                                                                      | Range   | Default |
+====================+==================================================================================+=========+=========+
| suppress-threshold | The threshold to start suppressing the advertisement of the interface state. The | 2-20000 | 2000    |
|                    | suppress-threshold value cannot be lower than the reuse-threshold value.         |         |         |
+--------------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# dampening
    dnRouter(cfg-if-ge100-1/0/1-dampening)# suppress-threshold 2500
    dnRouter(cfg-if-ge100-1/0/1-dampening)#

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/13
    dnRouter(cfg-if-ge100-1/0/13)# dampening
    dnRouter(cfg-if-ge100-1/0/13-dampening)# half-life 100 reuse-threshold 1100 suppress-threshold 2500 max-suppress 2000
    dnRouter(cfg-if-ge100-1/0/13-dampening)#


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/13-dampening)# no suppress-threshold

**Command History**

+---------+--------------------------------------+
| Release | Modification                         |
+=========+======================================+
| 11.4    | Command introduced                   |
+---------+--------------------------------------+
| 11.5    | Updated the suppress-threshold range |
+---------+--------------------------------------+

---

## interfaces dampening.rst

interfaces dampening
--------------------

**Minimum user role:** operator

In normal operation, the state of an interface is advertised whenever a change occurs. Dampening helps reduce the number of advertisements when the state of an interface changes frequently (flaps). Changing the interface dampening configuration clears the penalty value. The suppression state is also cleared for interfaces that are in a suppressed state. To configure dampening for an interface, enter the interface dampening configuration hierarchy:

**Command syntax: dampening**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to physical interfaces.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# dampening
    dnRouter(cfg-if-ge100-1/0/1-dampening)#


**Removing Configuration**

To revert to default:
::

    dnRouter(cfg-if-ge100-1/0/1)# no dampening

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.4    | Command introduced |
+---------+--------------------+

---

## interfaces description.rst

interfaces description
----------------------

**Minimum user role:** operator

To provide a textual interface description for the interface, use the following command:

**Command syntax: description [description]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan
  - Loopback
  - Control
  - gre-tunnel
  - IRB
  - Logical Management
  - Physical Management
  - Physical Management Member
  - ICE
  - Fabric

**Parameter table**

+-------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter   | Description                                                                      | Range            | Default |
+=============+==================================================================================+==================+=========+
| description | Provide a description for the interface. Enter free-text description with spaces | | string         | \-      |
|             | in between quotation marks.  If you do not use quotation marks, do not use       | | length 1-255   |         |
|             | spaces.                                                                          |                  |         |
+-------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces

    dnRouter(cfg-if)# ge10-2/1/1
    dnRouter(cfg-if-ge10-2/1/1)# description MyInterfaceDescription

    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# description "The First Bundle Port"

    dnRouter(cfg-if)# bundle-1.100
    dnRouter(cfg-if-bundle-1.100)# description ThisIsMyVlanInterface

    dnRouter(cfg-if)# lo1
    dnRouter(cfg-if-lo1)# description RouterIdLoopback

    dnRouter(cfg-if)# gre-tunnel-0
    dnRouter(cfg-if-gre-0)# description ISISregion0_to_remote_HOST

    dnRouter(cfg-if)# ctrl-ncp-0/0
    dnRouter(cfg-if-ctrl-ncp-0/0)# description MyControlNCPInterfaceDescription


**Removing Configuration**

To remove the interface description:
::

    dnRouter(cfg-if-ge10-2/1/1)# no description

::

    dnRouter(cfg-if-bundle-1.100)# no description

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces, applied new hierarchy |
+---------+--------------------------------------------------------------------+
| 11.4    | Added support for GRE-tunnels                                      |
+---------+--------------------------------------------------------------------+
| 16.2    | Management bond interface removed                                  |
+---------+--------------------------------------------------------------------+
| 17.0    | Added support for NCM control ports                                |
+---------+--------------------------------------------------------------------+
| 19.10   | Added support for ICE interface                                    |
+---------+--------------------------------------------------------------------+
| 25.1    | Added support for fabric interfaces                                |
+---------+--------------------------------------------------------------------+

---

## interfaces fabric fab-ncp400, fab-ncf400.rst

interfaces fabric fab-ncp400, fab-ncf400
----------------------------------------

**Minimum user role:** operator

The fabric interfaces are 400 Gbps interfaces interconnecting NCPs via the NCF. These interfaces are located on the NCPs and NCFs.

To configure the fabric interfaces:

**Command syntax: fab-<node-type>X-Y/Z/W**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the fabric interfaces on the NCP and NCF.

**Parameter table**

+---------------+------------------------------------------------+-----------------------------------+-------------+
|               |                                                |                                   |             |
| Parameter     | Description                                    | Range                             | Default     |
+===============+================================================+===================================+=============+
|               |                                                |                                   |             |
| Node-type     | The node where   the fabric port is located    | NCP                               | \-          |
|               |                                                |                                   |             |
|               |                                                | NCF                               |             |
+---------------+------------------------------------------------+-----------------------------------+-------------+
|               |                                                |                                   |             |
| W-X/Y/Z       | The fabric port identifier                     | X - interface speed               | \-          |
|               |                                                |                                   |             |
|               |                                                | Y - NCP/NCF id                    |             |
|               |                                                |                                   |             |
|               |                                                | Z - slot id, value 0              |             |
|               |                                                |                                   |             |
|               |                                                | W - port id as shown at the WB    |             |
+---------------+------------------------------------------------+-----------------------------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# fab-ncp400-0/0/0


**Removing Configuration**

To revert to the default value:
::

	dnRouter(cfg-if)# no fab-ncp400-0/0/0


.. **Help line:** configures fabric interface

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+

---

## interfaces fec.rst

interfaces fec
--------------

**Minimum user role:** operator

The Forward Error Correction (FEC) provides coding gain to increase the link budget and BER performance.

You can enable or disable Forward Error Correction (FEC) for a physical Ethernet interface, as follows:

-	Clause 74 of the IEEE 802.3 standard. For a PHY with a multi-lane BASE-R PCS, the FEC sublayer is instantiated for each PCS lane and operates autonomously on a per PCS lane basis.

	Encoding based on FC-FEC(2112,2080) ("fire-code") supporting the inter-sublayer interfaces:

	-	10GBASE-R PHY
	-	40GBASE-R PHY
	-	100GBASE-R PHY
-	Clause 91 of the IEEE 802.3 standard, which specifies a Reed-Solomon Forward Error Correction (RS-FEC) sublayer for 100GBASE-R PHYs.

	Encoding based on RS-FEC(528,514) supporting the inter-sublayer interfaces:

	-	100GBASE-CR4 PHY
	-	100GBASE-KR4 PHY
	-	100GBASE-SR4 PHY

	Encoding based on RS-FEC(544,514) supporting the inter-sublayer interfaces:

	-	100GBASE-KP4 PHY
-	Clause 119 of the IEEE P802.3bs

	Encoding based on RS-FEC(544,514) supporting the inter-sublayer interfaces:

	-	400GBASE-R PHY

To configure the interface FEC:

**Command syntax: fec [fec-type]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to physical interfaces.

**Parameter table**

+-----------+---------------------------------------------+--------------------+-----------------------------+
| Parameter | Description                                 | Range              | Default                     |
+===========+=============================================+====================+=============================+
| fec-type  | The type of FEC to enable for the interface | | none             | | None for 10G/100G         |
|           |                                             | | rs-fec-528-514   | | rs-fec-544-514 for 400G   |
|           |                                             | | rs-fec-544-514   |                             |
+-----------+---------------------------------------------+--------------------+-----------------------------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-2/1/1
    dnRouter(cfg-if-ge100-2/1/1)# fec rs-fec-544-514
    dnRouter(cfg-if-ge100-2/1/1)# fec rs-fec-528-514
    dnRouter(cfg-if-ge100-2/1/1)# fec none


**Removing Configuration**

To revert to the default type:
::

    dnRouter(cfg-if-ge100-2/1/1)# no fec

**Command History**

+---------+----------------------+
| Release | Modification         |
+=========+======================+
| 10.0    | Command introduced   |
+---------+----------------------+
| 11.0    | Added rs-fec-544-514 |
+---------+----------------------+

---

## interfaces flow-monitoring ipv4-mpls.rst

interfaces flow-monitoring type ipv4-over-mpls template direction
-----------------------------------------------------------------

**Minimum user role:** operator

The interface flow-monitoring command defines a flow-monitoring profile for the interface. That is, it defines how flow-monitoring is applied on the interface: which flow-monitoring template to use, in which direction, which sampler profile to use, etc.

To define a flow-monitoring profile for the interface:

**Command syntax: flow-monitoring type ipv4-over-mpls template [template] direction [direction]** sampler-profile [sampler-profile]

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan

- You can attach up to 4 flow-monitoring templates per interface (one per type).

- If you do not set a flow-sampler, the sampling rate will be set to 1:1.

- If both ipv4-over-mpls and ipv6-over-mpls templates are attachd to the same interface, they must be attached with the same sampler-profile.

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| Parameter       | Description                                                                      | Range                                                   | Default |
+=================+==================================================================================+=========================================================+=========+
| template        | The name of an existing flow-monitoring template. You can associate only one     | String (see "services flow-monitoring template")        | \-      |
|                 | flow-monitoring template per type. You can select only templates that match the  |                                                         |         |
|                 | selected type.                                                                   |                                                         |         |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| direction       | The direction in which the template applies                                      | in                                                      | in      |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| sampler-profile | The name of an existing flow-sampler.                                            | String (see "services flow-monitoring sampler-profile") | \-      |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces ge100-1/1/1.100
    dnRouter(cfg-if-ge100-1/1/1.100)# flow-monitoring type ipv4-over-mpls template myTemplate direction in
    dnRouter(cfg-if-ge100-1/1/1.100)# flow-monitoring type ipv4-over-mpls template myTemplate direction in sampler-profile mySampler1


**Removing Configuration**

To remove the template attachment for all traffic types:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring

To remove the template attachment for all traffic of IPv4 over MPLS:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring type ipv4-over-mpls

To remove the sampler-profile:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring type ipv4-over-mpls template myTemplate direction in sampler-profile

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.4    | Command introduced |
+---------+--------------------+

---

## interfaces flow-monitoring ipv4.rst

interfaces flow-monitoring type ipv4 template direction
-------------------------------------------------------

**Minimum user role:** operator

The interface flow-monitoring command defines a flow-monitoring profile for the interface. That is, it defines how flow-monitoring is applied on the interface: which flow-monitoring template to use, in which direction, which sampler profile to use, etc.

To define a flow-monitoring profile for the interface:

**Command syntax: flow-monitoring type ipv4 template [template] direction [direction]** sampler-profile [sampler-profile]

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - IRB

- You can attach up to 4 flow-monitoring templates per interface (one per type).

- If you do not set a flow-sampler, the sampling rate will be set to 1:1.

- If both ipv4-over-mpls and ipv6-over-mpls templates are attachd to the same interface, they must be attached with the same sampler-profile.

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| Parameter       | Description                                                                      | Range                                                   | Default |
+=================+==================================================================================+=========================================================+=========+
| template        | The name of an existing flow-monitoring template. You can associate only one     | String (see "services flow-monitoring template")        | \-      |
|                 | flow-monitoring template per type. You can select only templates that match the  |                                                         |         |
|                 | selected type.                                                                   |                                                         |         |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| direction       | The direction in which the template applies                                      | in                                                      | in      |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| sampler-profile | The name of an existing flow-sampler.                                            | String (see "services flow-monitoring sampler-profile") | \-      |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces ge100-1/1/1.100
    dnRouter(cfg-if-ge100-1/1/1.100)# flow-monitoring type ipv4 template myTemplate direction in
    dnRouter(cfg-if-ge100-1/1/1.100)# flow-monitoring type ipv4 template myTemplate direction in sampler-profile mySampler1


**Removing Configuration**

To remove the template attachment for all traffic types:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring

To remove the template attachment for all traffic of IPv4:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring type ipv4

To remove the sampler-profile:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring type ipv4 template myTemplate direction in sampler-profile

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.4    | Command introduced |
+---------+--------------------+

---

## interfaces flow-monitoring ipv6-mpls.rst

interfaces flow-monitoring type ipv6-over-mpls template direction
-----------------------------------------------------------------

**Minimum user role:** operator

The interface flow-monitoring command defines a flow-monitoring profile for the interface. That is, it defines how flow-monitoring is applied on the interface: which flow-monitoring template to use, in which direction, which sampler profile to use, etc.

To define a flow-monitoring profile for the interface:

**Command syntax: flow-monitoring type ipv6-over-mpls template [template] direction [direction]** sampler-profile [sampler-profile]

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan

- You can attach up to 4 flow-monitoring templates per interface (one per type).

- If you do not set a flow-sampler, the sampling rate will be set to 1:1.

- If both ipv4-over-mpls and ipv6-over-mpls templates are attachd to the same interface, they must be attached with the same sampler-profile.

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| Parameter       | Description                                                                      | Range                                                   | Default |
+=================+==================================================================================+=========================================================+=========+
| template        | The name of an existing flow-monitoring template. You can associate only one     | String (see "services flow-monitoring template")        | \-      |
|                 | flow-monitoring template per type. You can select only templates that match the  |                                                         |         |
|                 | selected type.                                                                   |                                                         |         |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| direction       | The direction in which the template applies                                      | in                                                      | in      |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| sampler-profile | The name of an existing flow-sampler.                                            | String (see "services flow-monitoring sampler-profile") | \-      |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces ge100-1/1/1.100
    dnRouter(cfg-if-ge100-1/1/1.100)# flow-monitoring type ipv6-over-mpls template myTemplate direction in
    dnRouter(cfg-if-ge100-1/1/1.100)# flow-monitoring type ipv6-over-mpls template myTemplate direction in sampler-profile mySampler1


**Removing Configuration**

To remove the template attachment for all traffic types:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring

To remove the template attachment for all traffic of IPv6 over MPLS:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring type ipv6-over-mpls

To remove the sampler-profile:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring type ipv6-over-mpls template myTemplate direction in sampler-profile

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.4    | Command introduced |
+---------+--------------------+

---

## interfaces flow-monitoring ipv6.rst

interfaces flow-monitoring type ipv6 template direction
-------------------------------------------------------

**Minimum user role:** operator

The interface flow-monitoring command defines a flow-monitoring profile for the interface. That is, it defines how flow-monitoring is applied on the interface: which flow-monitoring template to use, in which direction, which sampler profile to use, etc.

To define a flow-monitoring profile for the interface:

**Command syntax: flow-monitoring type ipv6 template [template] direction [direction]** sampler-profile [sampler-profile]

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - IRB

- You can attach up to 4 flow-monitoring templates per interface (one per type).

- If you do not set a flow-sampler, the sampling rate will be set to 1:1.

- If both ipv4-over-mpls and ipv6-over-mpls templates are attachd to the same interface, they must be attached with the same sampler-profile.

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| Parameter       | Description                                                                      | Range                                                   | Default |
+=================+==================================================================================+=========================================================+=========+
| template        | The name of an existing flow-monitoring template. You can associate only one     | String (see "services flow-monitoring template")        | \-      |
|                 | flow-monitoring template per type. You can select only templates that match the  |                                                         |         |
|                 | selected type.                                                                   |                                                         |         |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| direction       | The direction in which the template applies                                      | in                                                      | in      |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+
| sampler-profile | The name of an existing flow-sampler.                                            | String (see "services flow-monitoring sampler-profile") | \-      |
+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces ge100-1/1/1.100
    dnRouter(cfg-if-ge100-1/1/1.100)# flow-monitoring type ipv6 template myTemplate direction in
    dnRouter(cfg-if-ge100-1/1/1.100)# flow-monitoring type ipv6 template myTemplate direction in sampler-profile mySampler1


**Removing Configuration**

To remove the template attachment for all traffic types:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring

To remove the template attachment for all traffic of IPv6:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring type ipv6

To remove the sampler-profile:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no flow-monitoring type ipv6 template myTemplate direction in sampler-profile

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.4    | Command introduced |
+---------+--------------------+

---

## interfaces flow-monitoring sflow.rst

interfaces flow-monitoring type sflow direction
-----------------------------------------------

**Minimum user role:** operator

The interface flow-monitoring sflow command defines a flow-monitoring sflow profile for the interface. It defines how flow-monitoring sflow is applied on the interface: which exporter-profiles to use, in which direction, which sampler profile to use, etc.

Interface can support up to 4 exporters.

To define a flow-monitoring sflow for the interface:

**Command syntax: flow-monitoring type sflow direction [direction]** exporter-profile [exporter-profile] sampler-profile [sampler-profile]

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan.

- You can't configure both sflow and netflow/ipfix on the same interface.

- For flow-monitoring type sflow, the exporter-profile version must be configured as sflow.

- Mimimum sampling rate for sflow flow monitoring is 1:2048.

**Parameter table**

+------------------+-----------------------------------------------------------+----------------------------------------------------------+---------+
| Parameter        | Description                                               | Range                                                    | Default |
+==================+===========================================================+==========================================================+=========+
| direction        | Specify the direction for the sflow sampling.             | in                                                       | in      |
+------------------+-----------------------------------------------------------+----------------------------------------------------------+---------+
| exporter-profile | The name of an existing flow-monitoring exporter-profile. | String (see "services flow-monitoring exporter-profile") | \-      |
+------------------+-----------------------------------------------------------+----------------------------------------------------------+---------+
| sampler-profile  | The name of an existing flow-sampler.                     | String (see "services flow-monitoring sampler-profile")  | \-      |
+------------------+-----------------------------------------------------------+----------------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# flow-monitoring type sflow exporter-profile myExporter direction in
    dnRouter(cfg-if-ge100-1/1/1)# flow-monitoring type sflow exporter-profile myExporter direction in sampler-profile mySampler1


**Removing Configuration**

To remove the attachment for all exporters types:
::

    dnRouter(cfg-if-ge100-1/1/1)# no flow-monitoring

To remove the sflow configuration:
::

    dnRouter(cfg-if-ge100-1/1/1)# no flow-monitoring type sflow

To remove the sampler-profile:
::

    dnRouter(cfg-if-ge100-1/1/1)# no flow-monitoring type sflow direction in sampler-profile

To remove all exporter profiles from an interface:
::

    dnRouter(cfg-if-ge100-1/1/1)# no flow-monitoring type sflow direction in exporter-profile

To remove a specific profile from an interface:
::

    dnRouter(cfg-if-ge100-1/1/1)# no flow-monitoring type sflow direction in exporter-profile myExporter

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.1    | Command introduced |
+---------+--------------------+

---

## interfaces flowspec.rst

interfaces flowspec
-------------------

**Minimum user role:** operator

Flowspec is a dynamic data path policy that is received from a remote neighbor through BGP in order to impose different behaviors on different traffic flows. Flowspec is typically used to block or rate-limit distributed denial-of-service (DDoS) attacks and protect against malicious flows.

Flowspec specifies rules for matching a specific flow with source and destination, L4 parameters, and other packet specifics (e.g. length, fragmented, etc.) and encodes them as BGP network layer reachability information (NLRI). It also enables to dynamically install an action at the border router to drop all traffic. The action is coded as an extended community in the NLRI.
The actions that can be taken with FlowSpec are:

- Allow - the traffic is unaffected
- Drop - the traffic-rate community with a rate value of 0 tells the receiving router to discard all the traffic
- Redirect - redirect control or datapath traffic to IPv4 and IPv6 next-hops. This allows to mitigate DDOS attacks by redirecting suspected flows towards a scrubbing center, where further actions will be executed, and the safe traffic will be sent back to the network. The redirect to IP action is supported for both IPv4 and IPv6 addresses.

	The redirect operation is supported within the default VRF. I.e., redirect to a different VRF is not supported.

	Rules that carry both a redirect to IP next-hop and traffic-rate that equals 0.0 bps (i.e., drop) as BGP extended communities, will not be installed and are displayed as unsupported NLRI and/or action.

To configure FlowSpec:

#.	Configure BGP neighbors from which BGP FlowSpec rules are received (see "bgp neighbor" and "bgp neighbor address-family"). This will cause the router to share NLRIs with its peers.
#.	(Optional) Limit the number of FlowSpec rules received from the peers (see "bgp neighbor address-family maximum-prefix" and "bgp neighbor address-family maximum-prefix exceed-action").
#.	Configure the interfaces that will be FlowSpec-enabled:

To enable FlowSpec filtering on an interface:

**Command syntax: flowspec [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

	- Physical
	- Physical vlan
	- Bundle
	- Bundle vlan
	- IRB

- BGP FlowSpec does not impact the normal processing of packets running through the network processing unit (NPU).

- When enabled, ingress flow filtering will be applied according to rules received by BGP FlowSpec.

- A physical interface assigned to a bundle inherits the FlowSpec definition of the bundle.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                                      | Range        | Default  |
+=============+==================================================================================+==============+==========+
| admin-state | Set the administrative state of the FlowSpec feature on the interface. When      | | enabled    | disabled |
|             | enabled, ingress flow filtering will be applied according to the rules received  | | disabled   |          |
|             | by BGP FlowSpec.                                                                 |              |          |
+-------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# flowspec enabled

    dnRouter(cfg-if)# bundle-1.10
    dnRouter(cfg-if-bundle-1.10)# flowspec disabled

    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# flowspec enabled

    dnRouter(cfg-if)# ge100-1/1/1.20
    dnRouter(cfg-if-ge100-1/1/1.20)# flowspec disabled

    dnRouter(cfg-if)# bundle-2
    dnRouter(cfg-if-bundle-2)# flowspec enabled

    dnRouter(cfg-if)# bundle-2
    dnRouter(cfg-if-bundle-2)# flowspec disabled


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/1/1)# no flowspec

::

    dnRouter(cfg-if-ge100-1.20)# no flowspec

::

    dnRouter(cfg-if-bundle-2)# no flowspec

**Command History**

+---------+-------------------------------------------------------+
| Release | Modification                                          |
+=========+=======================================================+
| 13.0    | Command introduced                                    |
+---------+-------------------------------------------------------+
| 13.3    | Added support for redirect to IPv4 and IPv6 next-hops |
+---------+-------------------------------------------------------+

---

## interfaces ge, ge10, ge25, ge40, ge50, ge100, ge400.rst

interfaces ge10, ge100, ge400
---------------------------------------------------

**Minimum user role:** operator

To configure a physical interface:

**Command syntax: ge<speed>-<interface id>**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to physical interfaces.


**Parameter table**

+--------------+-------------------------------------+---------------------------------+------------+
|              |                                     |                                 |            |
| Parameter    | Description                         | Range                           | Default    |
+==============+=====================================+=================================+============+
|              |                                     |                                 |            |
| speed        | The speed of the physical port      | 10                              | \-         |
|              |                                     |                                 |            |
|              |                                     | 100                             |            |
|              |                                     |                                 |            |
|              |                                     | 400                             |            |
+--------------+-------------------------------------+---------------------------------+------------+
| id           | The ID of the specific port         | ge<interface speed>-<A>/<B>/<C> | \-         |
|              |                                     |                                 |            |
|              |                                     | <A> = ncp   id 0-255            |            |
|              |                                     |                                 |            |
|              |                                     | <B> = slot   id 0-255           |            |
|              |                                     |                                 |            |
|              |                                     | <C> = port   id                 |            |
+--------------+-------------------------------------+---------------------------------+------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces
	dnRouter(cfg-if)# ge100-1/1/1
	dnRouter(cfg-if-ge100-1/1/1)# admin-state enabled

	dnRouter(cfg-if)# ge10-1/1/1
	dnRouter(cfg-if-ge10-1/1/1)# ipv4-address 192.168.1.1/30

	dnRouter(cfg-if)# ge-1/1/1
	dnRouter(cfg-if-ge-1/1/1)# mtu 9200

..	dnRouter(cfg-if)# ge25-1/1/1
	dnRouter(cfg-if-ge25-1/1/1)# mpls enabled

	dnRouter(cfg-if)# ge40-1/1/1
	dnRouter(cfg-if-ge40-1/1/1)# ipv6-address 2001:1234::1/122


**Removing Configuration**

To revert to the default values:
::

	dnRouter(cfg-if)# no ge100-1/1/1
	dnRouter(cfg-if)# no ge400-1/1/1

.. **Help line:** Configure interface parameters

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 5.1         | Command introduced    |
+-------------+-----------------------+

---

## interfaces gre-tunnel destination.rst

interfaces destination
----------------------

**Minimum user role:** operator

To configure the tunnel's destination endpoint:

**Command syntax: destination [ipv4-address]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the gre-tunnel interface.

- You cannot create multiple GRE tunnels with the same interface source and destination pair.

**Parameter table**

+--------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter    | Description                                                                      | Range   | Default |
+==============+==================================================================================+=========+=========+
| ipv4-address | Sets the address of tunnel's destination endpoint. The destination address must  | A.B.C.D | \-      |
|              | be a routable unicast IPv4 address.                                              |         |         |
+--------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# gre-tunnel-0
    dnRouter(cfg-if-gre-0)# destination 192.168.153.17


**Removing Configuration**

Destination-address is a mandatory configuration and cannot be removed, only changed.
::


**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.4    | Command introduced |
+---------+--------------------+

---

## interfaces gre-tunnel mtu-gre.rst

interfaces mtu-gre
------------------

**Minimum user role:** operator

The maximum transmission unit (MTU) of a communication protocol of a layer defines the size of the largest protocol data unit that the layer is allowed to transmit over one interface. The MTU command configures L2 or L3 MTU for the interfaces. MTU is applicable to both control and datapath packets. The interface MTU affects only control traffic. Make sure that the MTU values are identical on all devices connected to the L2 network.
For GRE interfaces, the MTU is the payload size over the GRE tunnel (i.e without the IP & GRE header). By default, there is no fragmentation over the GRE tunnel. For the GRE interface, only MTU configuration is allowed. The GRE MTU is not counted as an MTU profile.

-	The sub-interface MTU must not be greater than the physical parent port MTU. The interface/sub-interface MTU must not be greater than max-hw-mtu (9300 for x86/QMX/J2 platforms).
-	NCP-40C and NCP-10CD support up to 8 different MTU configurations.

Each MTU profile configuration includes a unique tuple of all MTU types. For example:

-	MTU profile 0: (L2= 9000B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)
-	MTU profile 1: (L2= 9004B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)

The following table summarizes all available combinations in this version. x denotes the configured frame size.

+-------------+----------------+----------+--------------------------+
| Command     | Interface type | L2 frame | L3 frame                 |
+=============+================+==========+==========================+
+-------------+----------------+----------+--------------------------+
| mtu-gre x   | gre            |          | x                        |
|             |                |          |                          |
|             |                |          |                          |
+-------------+----------------+----------+--------------------------+

**Command syntax: mtu-gre [gre-mtu]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to gre-tunnel interfaces.

**Parameter table**

+-----------+--------------------------------+-----------+---------+
| Parameter | Description                    | Range     | Default |
+===========+================================+===========+=========+
| gre-mtu   | gre tunnel interface MTU value | 1500-9278 | 1500    |
+-----------+--------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# gre-tunnel-1
    dnRouter(cfg-if-gre-tunnel-1)# mtu-gre 5555


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-gre-tunnel-1)# no mtu-gre

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## interfaces gre-tunnel source.rst

interfaces source
-----------------

**Minimum user role:** operator

To configure the tunnel's source endpoint:

**Command syntax: source [source-address]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the gre-tunnel interface.

- You cannot create multiple GRE tunnels with the same interface source and destination pair.

**Parameter table**

+----------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter      | Description                                                                      | Range   | Default |
+================+==================================================================================+=========+=========+
| source-address | Sets the address of tunnel's source endpoint. The source address must be an      | A.B.C.D | \-      |
|                | existing local address in the same VRF.                                          |         |         |
+----------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# gre-tunnel-0
    dnRouter(cfg-if-gre-0)# source 1.1.1.1


**Removing Configuration**

Source-address is a mandatory configuration and cannot be removed, only changed.
::


**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.4    | Command introduced |
+---------+--------------------+

---

## interfaces gre-tunnel.rst

interfaces gre-tunnel
---------------------

**Minimum user role:** operator

Generic Routing Encapsulation (GRE) is a tunneling mechanism that encapsulates packets of any protocol inside IP packets delivered to a destination endpoint. The GRE tunnel behaves as a virtual point-to-point connection between the two endpoints (identified as tunnel source and tunnel destination).

To configure a GRE tunnel interface:

**Command syntax: gre-tunnel-[id]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the gre-tunnel interface.

**Parameter table**

+---------------+--------------------------+-----------+-------------+
|               |                          |           |             |
| Parameter     | Description              | Range     | Default     |
+===============+==========================+===========+=============+
|               |                          |           |             |
| ID            | The tunnel identifier    | 0..4      | \-          |
+---------------+--------------------------+-----------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# gre-tunnel-0 
	dnRouter(cfg-if-gre-0)# 


**Removing Configuration**

To remove the GRE tunnel interface and all its configurations:
::

	dnRouter(cfg-if)# no gre-tunnel-0


.. **Help line:** configures gre tunnel interface

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.4        | Command introduced    |
+-------------+-----------------------+

---

## interfaces ipmi-ncc admin-state.rst

interfaces ipmi-ncc admin-state
-------------------------------

**Minimum user role:** operator

To configure the ipmi-ncc-0/0 interface:


**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the ipmi-ncc interface.


**Parameter table**

+----------------+---------------------------------------------------+-------------+-------------+
|                |                                                   |             |             |
| Parameter      | Description                                       | Range       | Default     |
+================+===================================================+=============+=============+
|                |                                                   |             |             |
| admin-state    | Set the administrative state of the interface.    | Enabled     | Enabled     |
|                |                                                   |             |             |
|                |                                                   | Disabled    |             |
+----------------+---------------------------------------------------+-------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# ipmi-ncc-0/0 
	dnRouter(cfg-if-ipmi-ncc-0/0)# admin-state disabled


**Removing Configuration**

To revert to the default value:
::

	dnRouter(cfg-if)# no ipmi-ncc-0/0 


.. **Help line:** configure ipmi-ncc-0/0 interface

**Command History**

+-------------+---------------------------------------------+
|             |                                             |
| Release     | Modification                                |
+=============+=============================================+
|             |                                             |
| 10.0        | Command introduced                          |
+-------------+---------------------------------------------+

---

## interfaces ipmi-ncc.rst

interfaces ipmi-ncc
-------------------

**Minimum user role:** operator

The intelligent platform management interface (IPMI) provides out-of-band management facilities and platform monitoring capabilities (e.g. temperature, fans, power supplies, etc.).

To configure the IPMI interface for an NCC:


**Command syntax: ipmi-ncc-0/0**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the ipmi-ncc interface.


**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# ipmi-ncc-0/0 
	dnRouter(cfg-if-ipmi-ncc-0/0)# 


**Removing Configuration**

To revert to the default value:
::

	dnRouter(cfg-if)# no ipmi-ncc-0/0 


.. **Help line:** Configure ipmi-ncc-0/0 interface

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 10.0        | Command introduced    |
+-------------+-----------------------+

---

## interfaces ipmi-ncf admin-state.rst

interfaces ipmi-ncf admin-state
-------------------------------

**Minimum user role:** operator

To configure the ipmi-ncf-0/0 interface:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the ipmi-ncf interface.


**Parameter table**

+----------------+---------------------------------------------------+-------------+-------------+
|                |                                                   |             |             |
| Parameter      | Description                                       | Range       | Default     |
+================+===================================================+=============+=============+
|                |                                                   |             |             |
| admin-state    | Set the administrative state of the interface.    | Enabled     | Enabled     |
|                |                                                   |             |             |
|                |                                                   | Disabled    |             |
+----------------+---------------------------------------------------+-------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# ipmi-ncf-0/0 
	dnRouter(cfg-if-ipmi-ncf-0/0)# admin-state disabled


**Removing Configuration**

To revert to the default value:
::

	dnRouter(cfg-if)# no ipmi-ncf-0/0 


.. **Help line:** Configure ipmi-ncf-0/0 interface

**Command History**

+-------------+---------------------------------------------+
|             |                                             |
| Release     | Modification                                |
+=============+=============================================+
|             |                                             |
| 11.0        | Command introduced                          |
+-------------+---------------------------------------------+

---

## interfaces ipmi-ncf.rst

interfaces ipmi-ncf
-------------------

**Minimum user role:** operator

The intelligent platform management interface (IPMI) provides out-of-band management facilities and platform monitoring capabilities (e.g. temperature, fans, power supplies, etc.).

To configure the IPMI interface for an NCF:

**Command syntax: ipmi-ncf-0/0**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the ipmi-ncf interface.


**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# ipmi-ncf-0/0 
	dnRouter(cfg-if-ipmi-ncf-0/0)# 


**Removing Configuration**

To revert to the default value:
::

	dnRouter(cfg-if)# no ipmi-ncf-0/0 


.. **Help line:** configure ipmi-ncf-0/0 interface

**Command History**

+-------------+----------------------------------------------------+
|             |                                                    |
| Release     | Modification                                       |
+=============+====================================================+
|             |                                                    |
| 10.0        | Command introduced                                 |
+-------------+----------------------------------------------------+
|             |                                                    |
| 11.0        | Added support for IPMI interface on NCP and NCF    |
+-------------+----------------------------------------------------+

---

## interfaces ipmi-ncp admin-state.rst

interfaces ipmi-ncp admin-state
-------------------------------

**Minimum user role:** operator

To configure the ipmi-ncp-0/0 interface:


**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the ipmi-ncp interface.


**Parameter table**

+----------------+---------------------------------------------------+-------------+-------------+
|                |                                                   |             |             |
| Parameter      | Description                                       | Range       | Default     |
+================+===================================================+=============+=============+
|                |                                                   |             |             |
| admin-state    | Set the administrative state of the interface.    | Enabled     | Enabled     |
|                |                                                   |             |             |
|                |                                                   | Disabled    |             |
+----------------+---------------------------------------------------+-------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# ipmi-ncp-0/0 
	dnRouter(cfg-if-ipmi-ncp-0/0)# admin-state disabled


**Removing Configuration**

To revert to the default state:
::

	dnRouter(cfg-if)# no ipmi-ncp-0/0 


.. **Help line:** Configure ipmi-ncp-0/0 interface

**Command History**

+-------------+---------------------------------------------+
|             |                                             |
| Release     | Modification                                |
+=============+=============================================+
|             |                                             |
| 11.0        | Command introduced                          |
+-------------+---------------------------------------------+

---

## interfaces ipmi-ncp.rst

interfaces ipmi-ncp
-------------------

**Minimum user role:** operator

The intelligent platform management interface (IPMI) provides out-of-band management facilities and platform monitoring capabilities (e.g. temperature, fans, power supplies, etc.).

To configure the IPMI interface for an NCP:

**Command syntax: ipmi-ncp-0/0**

**Command mode:** config

**Hierarchies**

- interfaces 

**Note**

- The command is applicable to the ipmi-ncp interface.


**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# ipmi-ncp-0/0 
	dnRouter(cfg-if-ipmi-ncp-0/0)# 


**Removing Configuration**

To revert to the default value:
::

	dnRouter(cfg-if)# no ipmi-ncp-0/0 


.. **Help line:** configure ipmi-ncp-0/0 interface

**Command History**

+-------------+----------------------------------------------------+
|             |                                                    |
| Release     | Modification                                       |
+=============+====================================================+
|             |                                                    |
| 10.0        | Command introduced                                 |
+-------------+----------------------------------------------------+
|             |                                                    |
| 11.0        | Added support for IPMI interface on NCP and NCF    |
+-------------+----------------------------------------------------+
---

## interfaces ipv4-address dhcp.rst

interfaces ipv4-address dhcp
----------------------------

**Minimum user role:** operator

To dynamically allocate an IPv4 address for an logical management interface, use the following command:

**Command syntax: ipv4-address dhcp**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - mgmt0
  - mgmt-ncc-X
  - ipmi

- ipmi can only be configured with default gateway IPv4 address in standalone systems.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# mgmt0
    dnRouter(cfg-if-mgmt0)# ipv4-address dhcp


**Removing Configuration**

To revert to default:
::

    dnRouter(cfg-if-mgmt0)# no ipv4-address

**Command History**

+---------+----------------------------------------+
| Release | Modification                           |
+=========+========================================+
| 11.0    | Command introduced                     |
+---------+----------------------------------------+
| 16.2    | Management physical interfaces removed |
+---------+----------------------------------------+
| 19.2    | Add support for ipmi                   |
+---------+----------------------------------------+

---

## interfaces ipv4-address secondary.rst

interfaces ipv4-address secondary
---------------------------------

**Minimum user role:** operator

This command assigns an IPv4 address for the interface being configured.

To configure the IPv4 address for an interface, use the following command:

**Command syntax: ipv4-address [ipv4-address] secondary**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**
- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan
  - IRB

- A primary address must be configured on the interface before attempting to add secondary addresses.

- Up to 19 secondary IPv4 addresses can be configured on an interface in addition to the primary IPv4 address.

- You cannot configure broadcast or subnet network address per subnet mask (the first and last address from /1 up to /30 masks).

- You cannot change or remove the IP address for an interface that is configured as the source-interface for another interface.

- You cannot configure both DHCP and a static IP address for the same interface. The last configuration applies.

**Parameter table**

+--------------+----------------------------------------------------------------------------------+-----------+---------+
| Parameter    | Description                                                                      | Range     | Default |
+==============+==================================================================================+===========+=========+
| ipv4-address | Configures a static IPv4 address for the interface. The subnet mask cannot be    | A.B.C.D/x | \-      |
|              | /0.                                                                              |           |         |
+--------------+----------------------------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ipv4-address 1.2.3.4/22
    dnRouter(cfg-if-ge100-1/1/1)# ipv4-address 1.2.3.5/22 secondary

    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# ipv4-address 1.2.3.254/24

    dnRouter(cfg-if)# mgmt0
    dnRouter(cfg-if-mgmt0)# ipv4-address 1.2.3.4/24

    dnRouter(cfg-if)# gre-tunnel-0
    dnRouter(cfg-if-gre-0)# ipv4-address 10.10.10.0/31
    dnRouter(cfg-if-gre-0)# no ipv4-address


**Removing Configuration**

To remove the IPv4 address:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ipv4-address 10.10.10.0/31

To revert to default:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ipv4-address

**Command History**

+---------+--------------------------------------------------------------------------------------------------------------------------+
| Release | Modification                                                                                                             |
+=========+==========================================================================================================================+
| 5.1     | Command introduced                                                                                                       |
+---------+--------------------------------------------------------------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces; added option for unnumbered interface; applied new hierarchy; added         |
|         | restriction on /0 subnet mask                                                                                            |
+---------+--------------------------------------------------------------------------------------------------------------------------+
| 10.0    | Unnumbered interfaces not supported.                                                                                     |
+---------+--------------------------------------------------------------------------------------------------------------------------+
| 11.4    | Added support for GRE-tunnels                                                                                            |
+---------+--------------------------------------------------------------------------------------------------------------------------+
| 16.2    | Management bond interfaces removed                                                                                       |
+---------+--------------------------------------------------------------------------------------------------------------------------+
| 17.2    | Added support for secondary IPv4 addresses                                                                               |
+---------+--------------------------------------------------------------------------------------------------------------------------+

---

## interfaces ipv4-address.rst

interfaces ipv4-address
-----------------------

**Minimum user role:** operator

This command assigns an IPv4 address for the interface being configured.

To configure the IPv4 address for an interface, use the following command:

**Command syntax: ipv4-address [ipv4-address]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan
  - Loopback
  - mgmt0
  - mgmt-ncc-X
  - gre-tunnel
  - IRB
  - ipmi
  - ICE

- Loopback interfaces can be configured with /32 address only.

- A primary address must be configured on the interface before attempting to add secondary addresses.

- Up to 19 secondary IPv4 addresses can be configured on an interface in addition to the primary IPv4 address.

- ipmi can only be configured with static IP address in standalone systems.

- You cannot configure broadcast or subnet network address per subnet mask (the first and last address from /1 up to /30 masks).

- You cannot change or remove the IP address for an interface that is configured as the source-interface for another interface.

- You cannot configure both DHCP and a static IP address for the same interface. The last configuration applies.

**Parameter table**

+--------------+----------------------------------------------------------------------------------+-----------+---------+
| Parameter    | Description                                                                      | Range     | Default |
+==============+==================================================================================+===========+=========+
| ipv4-address | Configures a static IPv4 address for the interface. The subnet mask cannot be    | A.B.C.D/x | \-      |
|              | /0.                                                                              |           |         |
+--------------+----------------------------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ipv4-address 1.2.3.4/22

    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# ipv4-address 1.2.3.254/24

    dnRouter(cfg-if)# mgmt0
    dnRouter(cfg-if-mgmt0)# ipv4-address 1.2.3.4/24

    dnRouter(cfg-if)# gre-tunnel-0
    dnRouter(cfg-if-gre-0)# ipv4-address 10.10.10.0/31
    dnRouter(cfg-if-gre-0)# no ipv4-address

    dnRouter(cfg-if)# ipmi-ncc-0/0
    dnRouter(cfg-if-ipmi-ncc-0/0)# ipv4-address 1.2.3.4/31
    dnRouter(cfg-if-ipmi-ncc-0/0)# no ipv4-address


**Removing Configuration**

To remove the IPv4 address:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ipv4-address 10.10.10.0/31

To revert to default:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ipv4-address

**Command History**

+---------+--------------------------------------------------------------------------------------------------------------------------+
| Release | Modification                                                                                                             |
+=========+==========================================================================================================================+
| 5.1     | Command introduced                                                                                                       |
+---------+--------------------------------------------------------------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces; added option for unnumbered interface; applied new hierarchy; added         |
|         | restriction on /0 subnet mask                                                                                            |
+---------+--------------------------------------------------------------------------------------------------------------------------+
| 10.0    | Unnumbered interfaces not supported.                                                                                     |
+---------+--------------------------------------------------------------------------------------------------------------------------+
| 11.4    | Added support for GRE-tunnels                                                                                            |
+---------+--------------------------------------------------------------------------------------------------------------------------+
| 16.2    | Management bond interfaces removed                                                                                       |
+---------+--------------------------------------------------------------------------------------------------------------------------+
| 19.10   | Added support for ICE interface                                                                                          |
+---------+--------------------------------------------------------------------------------------------------------------------------+
| 19.2    | Add support for ipmi                                                                                                     |
+---------+--------------------------------------------------------------------------------------------------------------------------+

---

## interfaces ipv4-default-gateway.rst

interfaces ipv4-default-gateway
-------------------------------

**Minimum user role:** operator

This command assigns an IPv4 default gateway address for the interface being configured.

To configure the IPv4 default gateway address for an interface, use the following command:

**Command syntax: ipv4-default-gateway [default-gateway]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - ipmi

- ipmi can only be configured with default gateway IPv4 address in standalone systems.

**Parameter table**

+-----------------+----------------------------------------------------+---------+---------+
| Parameter       | Description                                        | Range   | Default |
+=================+====================================================+=========+=========+
| default-gateway | The IPv4 default gateway address on the interface. | A.B.C.D | 0.0.0.0 |
+-----------------+----------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ipmi-ncc-0/0
    dnRouter(cfg-if-ipmi-ncc-0/0)# ipv4-default-gateway 10.20.30.40
    dnRouter(cfg-if-ipmi-ncc-0/0)# no ipv4-address


**Removing Configuration**

To revert to default:
::

    dnRouter(cfg-if-ipmi-ncc-0/0)# no ipv4-default-gateway

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.2    | Command introduced |
+---------+--------------------+

---

## interfaces ipv6-address dhcp.rst

interfaces ipv6-address dhcpv6
------------------------------

**Minimum user role:** operator

To dynamically allocate an IPv6 address for an interface, use the following command:

**Command syntax: ipv6-address dhcpv6**

**Command mode:** config

**Hierarchies**

- interfaces

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# mgmt0
    dnRouter(cfg-if-mgmt0)# ipv6-address dhcpv6


**Removing Configuration**

To revert to default:
::

    dnRouter(cfg-if-mgmt0)# no ipv6-address

**Command History**

+---------+------------------------------------------------+
| Release | Modification                                   |
+=========+================================================+
| 11.0    | Command introduced                             |
+---------+------------------------------------------------+
| 13.1    | Changed dhcp with dhcpv6 in the command syntax |
+---------+------------------------------------------------+
| 16.2    | Management physical interfaces removed         |
+---------+------------------------------------------------+

---

## interfaces ipv6-address dhcpv6.rst

interfaces ipv6-address dhcpv6
------------------------------

**Minimum user role:** operator

To dynamically allocate an IPv6 address for an interface, use the following command:

**Command syntax: ipv6-address dhcpv6**

**Command mode:** config

**Hierarchies**

- interfaces

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# mgmt0
    dnRouter(cfg-if-mgmt0)# ipv6-address dhcpv6


**Removing Configuration**

To revert to default:
::

    dnRouter(cfg-if-mgmt0)# no ipv6-address

**Command History**

+---------+------------------------------------------------+
| Release | Modification                                   |
+=========+================================================+
| 11.0    | Command introduced                             |
+---------+------------------------------------------------+
| 13.1    | Changed dhcp with dhcpv6 in the command syntax |
+---------+------------------------------------------------+
| 16.2    | Management physical interfaces removed         |
+---------+------------------------------------------------+
| 19.1    | Added support for in-band network interfaces   |
+---------+------------------------------------------------+

---

## interfaces ipv6-address.rst

interfaces ipv6-address
-----------------------

**Minimum user role:** operator

To configure the IPv6 address for an interface, use the following command:

**Command syntax: ipv6-address [ipv6-address]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan
  - Loopback
  - mgmt0
  - mgmt-ncc-X
  - IRB

- Loopback interfaces can be configured with /128 address only.

- You cannot configure both DHCPv6 and a static IP address for the same interface. The last configuration applies.

**Parameter table**

+--------------+-----------------------------------------------------+------------+---------+
| Parameter    | Description                                         | Range      | Default |
+==============+=====================================================+============+=========+
| ipv6-address | Configures a static IPv6 address for the interface. | X:X::X:X/x | \-      |
+--------------+-----------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ipv6-address 2001:ab12::1/127


**Removing Configuration**

To remove the IPv6 address:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ipv6-address

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces; applied new hierarchy |
+---------+--------------------------------------------------------------------+
| 16.2    | Management bond interfaces removed                                 |
+---------+--------------------------------------------------------------------+

---

## interfaces ipv6-admin-state.rst

interfaces ipv6-admin-state
---------------------------

**Minimum user role:** operator

Interface will support ipv6 traffic if one of the following conditions is met
- Interface has ipv6-address configured. Used for Global Unicast Address
- Interface is enabled for dhcpv6 client support
- Interface ipv6-admin-state is explicitly enabled

In case ipv6-admin-state is explicitly disabled, interface will not support ipv6 traffic
In case ipv6-admin-state is enabled, but no ipv6-address configured, interface will support ipv6 traffic leverging link-local address.

To configure ipv6-admin-state:

**Command syntax: ipv6-admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan
  - IRB

**Parameter table**

+-------------+---------------------------------------------------------+--------------+---------+
| Parameter   | Description                                             | Range        | Default |
+=============+=========================================================+==============+=========+
| admin-state | Sets the administrative state of IPv6 on the interface. | | enabled    | \-      |
|             |                                                         | | disabled   |         |
+-------------+---------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# ipv6-admin-state enabled
    dnRouter(cfg-if-ge100-0/0/0)# ipv6-admin-state disabled


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-ge100-0/0/0)# no ipv6-admin-state

**Command History**

+---------+---------------------------------------------------------+
| Release | Modification                                            |
+=========+=========================================================+
| 15.0    | Command introduced                                      |
+---------+---------------------------------------------------------+
| 19.3    | Update behavior for case ipv6-address is not configured |
+---------+---------------------------------------------------------+

---

## interfaces irb.rst

interfaces irb
--------------

**Minimum user role:** operator

The IRB interfaces in DNOS provide ability to connect L2 service (like bridge-domain) to L3 routing.

The parameters that you can optionally configure on the IRB interface are the same parameters that you can configure on any interface. If you do not set these parameters, the default values will be assumed.

**Command syntax: irb<irb-id>**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- Create an IRB interface, using this command.

- Bind the IRB interface to a bridge-domain service using the "router-interface" command.

**Parameter table**

+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
| Parameter     | Description                                                                                                                                                                                                                | Range       | Default     |
+===============+============================================================================================================================================================================================================================+=============+=============+
| irb-id        | The IRB interface identifier. If the ID does not exist, this will create a new IRB interface with the specific identifier. If the ID exists, you will enter the existing IRB interface's configuration mode.               | 1..65535    | \-          |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces
	dnRouter(cfg-if)# irb1
	dnRouter(cfg-if-irb1)#


**Removing Configuration**

To delete an irb interface:
::

	dnRouter(cfg-if)# no irb1


.. **Help line:** Configures irb interface

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.0    | Command introduced |
+---------+--------------------+

---

## interfaces l2-originated-vlan-tags inner-tag.rst

interfaces l2-originated-vlan-tags inner-tag
--------------------------------------------

**Minimum user role:** operator

To configure the inner VLAN tag to be applied to locally-generated traffic originating from a multi-VLAN sub-interface:

**Command syntax: inner-tag [l2-originated-inner-vlan-id]** inner-tpid [l2-originated-inner-tpid]

**Command mode:** config

**Hierarchies**

- interfaces l2-originated-vlan-tags

**Note**
- L2-originated-vlan-tags command is applicable only for L2 multi-VLAN sub-interfaces.

- If the l2-originated-vlan-tags command is not configured, by default a multi-VLAN sub-interface will send locally-generated traffic as untagged.

- VLAN tags of traffic forwarded through L2 multi-VLAN sub-interfaces are preserved as usual.

**Parameter table**

+-----------------------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter                   | Description                                                                      | Range      | Default |
+=============================+==================================================================================+============+=========+
| l2-originated-inner-vlan-id | The inner VLAN ID to assign to locally originated traffic over the multi-VLAN    | 1-4094     | \-      |
|                             | sub-interface. The VLAN ID does not need to match the sub-interface ID.          |            |         |
+-----------------------------+----------------------------------------------------------------------------------+------------+---------+
| l2-originated-inner-tpid    | The TPID to identify the protocol type of the inner VLAN tag.                    | | 0x8100   | 0x8100  |
|                             |                                                                                  | | 0x88a8   |         |
|                             |                                                                                  | | 0x9100   |         |
|                             |                                                                                  | | 0x9200   |         |
+-----------------------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0.100
    dnRouter(cfg-if-ge100-0/0/0.100)# l2-originated-vlan-tags
    dnRouter(cfg-if-ge100-0/0/0.100-l2-originated-vlan-tags)# inner-tag 350 inner-tpid 0x9100


**Removing Configuration**

To remove the inner VLAN tag configuration:
::

    dnRouter(cfg-if-ge100-0/0/0.100-l2-originated-vlan-tags)# no inner-tag

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.2    | Command introduced |
+---------+--------------------+

---

## interfaces l2-originated-vlan-tags outer-tag.rst

interfaces l2-originated-vlan-tags outer-tag
--------------------------------------------

**Minimum user role:** operator

To configure the outer VLAN tag to be applied to locally generated traffic originating from a multi-VLAN sub-interface:

**Command syntax: outer-tag [l2-originated-outer-vlan-id]** outer-tpid [l2-originated-outer-tpid]

**Command mode:** config

**Hierarchies**

- interfaces l2-originated-vlan-tags

**Note**
- L2-originated-vlan-tags command is applicable only for L2 multi-VLAN sub-interfaces.

- If l2-originated-vlan-tags command is not configured, by default a multi-VLAN sub-interface will send locally generated traffic as untagged.

- VLAN tags of traffic forwarded through L2 multi-VLAN sub-interfaces are preserved as usual.

**Parameter table**

+-----------------------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter                   | Description                                                                      | Range      | Default |
+=============================+==================================================================================+============+=========+
| l2-originated-outer-vlan-id | The outer VLAN ID to assign to locally originated traffic over the multi-VLAN    | 1-4094     | \-      |
|                             | sub-interface. The VLAN ID does not need to match the sub-interface ID.          |            |         |
+-----------------------------+----------------------------------------------------------------------------------+------------+---------+
| l2-originated-outer-tpid    | The TPID to identify the protocol type of the outer VLAN tag.                    | | 0x8100   | 0x8100  |
|                             |                                                                                  | | 0x88a8   |         |
|                             |                                                                                  | | 0x9100   |         |
|                             |                                                                                  | | 0x9200   |         |
+-----------------------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0.100
    dnRouter(cfg-if-ge100-0/0/0.100)# l2-originated-vlan-tags
    dnRouter(cfg-if-ge100-0/0/0.100-l2-originated-vlan-tags)# outer-tag 350 outer-tpid 0x9100


**Removing Configuration**

To remove the outer VLAN tag configuration:
::

    dnRouter(cfg-if-ge100-0/0/0.100-l2-originated-vlan-tags)# no outer-tag

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.2    | Command introduced |
+---------+--------------------+

---

## interfaces l2-originated-vlan-tags.rst

interfaces l2-originated-vlan-tags
----------------------------------

**Minimum user role:** operator

To configure the VLAN tags to be applied to locally generated traffic originating from a multi-VLAN sub-interface:

**Command syntax: l2-originated-vlan-tags**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**
- L2-originated-vlan-tags command is applicable only for L2 multi-VLAN sub-interfaces.

- If l2-originated-vlan-tags command is not configured, by default a multi-VLAN sub-interface will send locally generated traffic as untagged.

- VLAN tags of traffic forwarded through L2 multi-VLAN sub-interfaces are preserved as usual.

**Example**
::

    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0.100
    dnRouter(cfg-if-ge100-0/0/0.100)# l2-originated-vlan-tags
    dnRouter(cfg-if-ge100-0/0/0.100-l2-originated-vlan-tags)#


**Removing Configuration**

To remove the l2-originated-vlan-tags configuration:
::

    dnRouter(cfg-if-ge100-0/0/0.100)# no l2-originated-vlan-tags

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.2    | Command introduced |
+---------+--------------------+

---

## interfaces l2-service.rst

interfaces l2-service
---------------------

**Minimum user role:** operator

To configure a sub-interface as an L2 service UNI port:

**Command syntax: l2-service [l2-service-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan

- A sub-interface can be configured as an L2 service UNI port only if there are no IPv4 or IPv6 addresses and no other conflicting settings (such as access-lists) configured on it.

**Parameter table**

+------------------+-----------------------------------------------+--------------+----------+
| Parameter        | Description                                   | Range        | Default  |
+==================+===============================================+==============+==========+
| l2-service-state | The state of the L2 service on this interface | | enabled    | disabled |
|                  |                                               | | disabled   |          |
+------------------+-----------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-100.2
    dnRouter(cfg-if-bundle-100.2)# l2-service enabled

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1.22 l2-service disabled


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-bundle-100.2)# no l2-service

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 12.0    | Command introduced |
+---------+--------------------+

---

## interfaces lo.rst

interfaces lo 
--------------

**Minimum user role:** operator

A loopback interface is valid only if an IP address (IPv4 or IPv6) is configured for it. To create a loopback interface or enter an existing loopback interface's configuration mode:

**Command syntax: lo<id>**

**Command mode:** config

**Hierarchies**

- interfaces 

**Note**

- The command is applicable to loopback interfaces.
- Loopback interface can be created either with or without adding any parameter.

..
	**Internal Note**

	Validations:

	-  Loopback ipv4 interface can be configured only with /32

	-  Loopback ipv6 interface can be configured only with /128


**Parameter table**

+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
|               |                                                                                                                                                                                                                                          |             |             |
| Parameter     | Description                                                                                                                                                                                                                              | Range       | Default     |
+===============+==========================================================================================================================================================================================================================================+=============+=============+
|               |                                                                                                                                                                                                                                          |             |             |
| lo-id         | The loopback interface identifier. If the ID does   not already exist, this will create a loopback interface with the specific   identifier. If exists, this will enter the configuration mode for the   specific loopback interface.    | 0..65535    | \-          |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces
	dnRouter(cfg-if)# lo0
	dnRouter(cfg-if-lo0)# 


**Removing Configuration**

To delete the lo0 interface:
::

	dnRouter(cfg-if)# no lo0 


.. **Help line:**

**Command History**

+-------------+-------------------------------------------------------+
|             |                                                       |
| Release     | Modification                                          |
+=============+=======================================================+
|             |                                                       |
| 5.1.0       | Command introduced                                    |
+-------------+-------------------------------------------------------+
|             |                                                       |
| 6.0         | Changed syntax from interface to interfaces           |
|             |                                                       |
|             | Applied new hierarchy                                 |
+-------------+-------------------------------------------------------+
|             |                                                       |
| 7.0         | Removed the keyword "interface" from   the syntax.    |
+-------------+-------------------------------------------------------+
---

## interfaces mac-address.rst

interfaces mac-address
----------------------

**Minimum user role:** operator

To switch frames between LAN ports efficiently, an address table is maintained. When the system receives a frame, it associates the media access control (MAC) address of the sending network device with the LAN port on which it was received. When it receives a frame for a MAC destination address not listed in its address table, it floods the frame to all LAN ports of the same VLAN except the port that received the frame. When the destination station replies, its MAC address is added to the address table from the source address of the reply.

You can enter a new (static) MAC address for physical or LAG interfaces only. This will replace the default MAC address.

To change MAC address of a physical or LAG interface, use the following command in configuration mode:

**Command syntax: mac-address [mac-address]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Bundle
  - IRB
  - mgmt
  - mgmt-ncc-X

- For a bundle interface, the default value is the mac address of the first member. The MAC address is taken from DriveNets' pool (OUI 84:40:76:XX:XX:XX), where the last 3 bytes are randomized.

- When configuring a bundle interface without configuring a specific mac-address for it, "no mac-address" will not do anything because it has selected the "default" value of the bundle interface.

**Parameter table**

+-------------+-----------------------------------+-------------------+---------+
| Parameter   | Description                       | Range             | Default |
+=============+===================================+===================+=========+
| mac-address | The MAC address for the interface | xx:xx:xx:xx:xx:xx | \-      |
+-------------+-----------------------------------+-------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# mac-address 10:22:33:44:55:00

    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# mac-address 00:00:00:00:00:01


**Removing Configuration**

To revert to the default MAC address (that of the connected device):
::

    dnRouter(cfg-if-ge100-1/1/1)# no mac-address

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces; applied new hierarchy |
+---------+--------------------------------------------------------------------+
| 9.0     | Not supported in this version.                                     |
+---------+--------------------------------------------------------------------+
| 10.0    | Command re-introduced                                              |
+---------+--------------------------------------------------------------------+
| 16.2    | Management bond interfaces removed                                 |
+---------+--------------------------------------------------------------------+

---

## interfaces mgmt0.rst

interfaces mgmt0
----------------

**Minimum user role:** operator

The mgmt0 interface is a logical interface associated with the NCC. After entering the mgmt0 configuration hierarchy, proceed to configure parameters for the interface. Otherwise, default values will be used.

To configure the mgmt0 logical management interface, enter its configuration mode:

**Command syntax: mgmt0**

**Command mode:** config

**Hierarchies**

- interfaces 

**Note**

- The command is applicable to the mgmt0 interface.
- The mgmt0 IP address must differ from the mgmt-ncc address.

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	dnRouter(cfg-if)# mgmt0 
	dnRouter(cfg-if-mgmt0)# 


**Removing Configuration**

To revert to the default value:
::

	dnRouter(cfg-if)# no mgmt0 


.. **Help line:** Configures mgmt0 interface

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+
---

## interfaces mpls.rst

interfaces mpls
---------------

**Minimum user role:** operator

MPLS is a packet-forwarding technology which uses labels in order to make data forwarding decisions. With MPLS, the Layer 3 header analysis is done just once (when the packet enters the MPLS domain). Label inspection drives subsequent packet forwarding. Additionally, it decreases the forwarding overhead on the core routers. When disabled, all mpls traffic received on the interface will be dropped.

To enable MPLS on an interface, use the following command in configuration mode:

**Command syntax: mpls [mpls-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan

**Parameter table**

+------------+------------------------------------------------------+--------------+----------+
| Parameter  | Description                                          | Range        | Default  |
+============+======================================================+==============+==========+
| mpls-state | Enables or disables MPLS on the specified interface. | | enabled    | disabled |
|            |                                                      | | disabled   |          |
+------------+------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge10-1/1/1
    dnRouter(cfg-if-ge10-1/1/1)# mpls enabled

    dnRouter(cfg-if)# ge10-1/1/1.100
    dnRouter(cfg-if-ge10-1/1/1.100)# mpls enabled

    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# mpls disabled


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1)# no mpls

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces; applied new hierarchy |
+---------+--------------------------------------------------------------------+

---

## interfaces mtu-ipv4.rst

interfaces mtu-ipv4
-------------------

**Minimum user role:** operator

The maximum transmission unit (MTU) of a communication protocol of a layer defines the size of the largest protocol data unit that the layer is allowed to transmit over one interface. The MTU command configures L2 or L3 MTU for the interfaces. MTU is applicable to both control and datapath packets. The interface MTU affects only control traffic. Make sure that the MTU values are identical on all devices connected to the L2 network.

-	The sub-interface MTU must not be greater than the physical parent port MTU. The interface/sub-interface MTU must not be greater than max-hw-mtu (9300 for x86/QMX/J2 platforms).
-	NCP-40C and NCP-10CD support up to 8 different MTU configurations.

Each MTU profile configuration includes a unique tuple of all MTU types. For example:

-	MTU profile 0: (L2= 9000B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)
-	MTU profile 1: (L2= 9004B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)

The following table summarizes all available combinations in this version. x denotes the configured frame size.

+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| Command     | Interface type | L2 frame | L3 frame                 | Validated range                                                     |
+=============+================+==========+==========================+=====================================================================+
| mtu-ipv4 x  | untagged       |          | x for ipv4               | -  <1280 - (Max_HW_MTU-14)> if there are no sub interfaces under it |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1280 - (Max_HW_MTU-18)> if there is .1Q interface under it      |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1280 - (Max_HW_MTU-22)> if there is QinQ interface under it     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu-ipv4 x  | .1q            |          | x for ipv4               | -  <1280 - (Max_HW_MTU-18)> if there is no QinQ interface on parent |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1280 - (Max_HW_MTU-22)> if there is QinQ interface on parent    |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu-ipv4 x  | qinq           |          | x for ipv4               | -  <1280 - (Max_HW_MTU-22)>                                         |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+

**Command syntax: mtu-ipv4 [ipv4-mtu]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

The command is applicable to the following interface types:

- Physical
- Physical vlan
- Bundle
- Bundle vlan
- IRB

**Parameter table**

+-----------+----------------------------------+-----------+---------+
| Parameter | Description                      | Range     | Default |
+===========+==================================+===========+=========+
| ipv4-mtu  | ipv4 MTU value of the interface. | 1280-9286 | \-      |
+-----------+----------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces

    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# mtu-ipv4 1514

    dnRouter(cfg-if)# bundle-1.100
    dnRouter(cfg-if-bundle-1.100)# mtu-ipv4 1514

    dnRouter(cfg-if)# ge10-2/1/1.100
    dnRouter(cfg-if-ge10-2/1/1.100)# mtu-ipv4 9000


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1.100)# no mtu-ipv4

**Command History**

+---------+---------------------------------------------------------------+
| Release | Modification                                                  |
+=========+===============================================================+
| 16.1    | Command introduced. Split from general interface MTU command. |
+---------+---------------------------------------------------------------+
| 18.3    | Extended the supported MTU range.                             |
+---------+---------------------------------------------------------------+

---

## interfaces mtu-ipv6.rst

interfaces mtu-ipv6
-------------------

**Minimum user role:** operator

The maximum transmission unit (MTU) of a communication protocol of a layer defines the size of the largest protocol data unit that the layer is allowed to transmit over one interface. The MTU command configures L2 or L3 MTU for the interfaces. MTU is applicable to both control and datapath packets. The interface MTU affects only control traffic. Make sure that the MTU values are identical on all devices connected to the L2 network.

-	The sub-interface MTU must not be greater than the physical parent port MTU. The interface/sub-interface MTU must not be greater than max-hw-mtu (9300 for x86/QMX/J2 platforms).
-	NCP-40C and NCP-10CD support up to 8 different MTU configurations.

Each MTU profile configuration includes a unique tuple of all MTU types. For example:

-	MTU profile 0: (L2= 9000B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)
-	MTU profile 1: (L2= 9004B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)

The following table summarizes all available combinations in this version. x denotes the configured frame size.

+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| Command     | Interface type | L2 frame | L3 frame                 | Validated range                                                     |
+=============+================+==========+==========================+=====================================================================+
| mtu-ipv6 x  | untagged       |          | x for ipv6               | -  <1280 - (Max_HW_MTU-14)> if there are no sub interfaces under it |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1280 - (Max_HW_MTU-18)> if there is .1Q interface under it      |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1280 - (Max_HW_MTU-22)> if there is QinQ interface under it     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu-ipv6 x  | .1q            |          | x for ipv6               | -  <1280 - (Max_HW_MTU-18)> if there is no QinQ interface on parent |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1280 - (Max_HW_MTU-22)> if there is QinQ interface on parent    |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu-ipv6 x  | qinq           |          | x for ipv6               | -  <1280 - (Max_HW_MTU-22)>                                         |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+

**Command syntax: mtu-ipv6 [ipv6-mtu]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

The command is applicable to the following interface types:

- Physical
- Physical vlan
- Bundle
- Bundle vlan
- IRB

**Parameter table**

+-----------+----------------------------------+-----------+---------+
| Parameter | Description                      | Range     | Default |
+===========+==================================+===========+=========+
| ipv6-mtu  | ipv6 MTU value of the interface. | 1280-9286 | \-      |
+-----------+----------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces

    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# mtu-ipv6 1514

    dnRouter(cfg-if)# bundle-1.100
    dnRouter(cfg-if-bundle-1.100)# mtu-ipv6 1514

    dnRouter(cfg-if)# ge10-2/1/1.100
    dnRouter(cfg-if-ge10-2/1/1.100)# mtu-ipv6 9000


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1.100)# no mtu-ipv6

**Command History**

+---------+---------------------------------------------------------------+
| Release | Modification                                                  |
+=========+===============================================================+
| 16.1    | Command introduced. Split from general interface MTU command. |
+---------+---------------------------------------------------------------+
| 18.3    | Extended the supported MTU range.                             |
+---------+---------------------------------------------------------------+

---

## interfaces mtu-l2.rst

interfaces mtu
--------------

**Minimum user role:** operator

The maximum transmission unit (MTU) of a communication protocol of a layer defines the size of the largest protocol data unit that the layer is allowed to transmit over one interface. The MTU command configures L2 or L3 MTU for the interfaces. MTU is applicable to both control and datapath packets. The interface MTU affects only control traffic. Make sure that the MTU values are identical on all devices connected to the L2 network.

-	The sub-interface MTU must not be greater than the physical parent port MTU. The interface/sub-interface MTU must not be greater than max-hw-mtu (9300 for x86/QMX/J2 platforms).
-	NCP-40C and NCP-10CD support up to 8 different MTU configurations.

Each MTU profile configuration includes a unique tuple of all MTU types. For example:

-	MTU profile 0: (L2= 9000B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)
-	MTU profile 1: (L2= 9004B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)

The following table summarizes all available combinations in this version. x denotes the configured frame size.

+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| Command     | Interface type | L2 frame | L3 frame                 | Validated range                                                     |
+=============+================+==========+==========================+=====================================================================+
| mtu x       | untagged       | x        | x - 14                   | -  <1294 - Max_HW_MTU> if there are no sub interfaces under it      |
|             |                |          |                          |                                                                     |
|             |                |          | for MPLS and other types | -  <1294 - (Max_HW_MTU-4)> if there is .1Q interface under it       |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1294 - (Max_HW_MTU-8)> if there is QinQ interface under it      |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu x       | .1q            | x        | x - 18                   | -  <1298 - Max_HW_MTU> if there is no QinQ interface on parent      |
|             |                |          |                          |                                                                     |
|             |                |          | for MPLS and other types | -  <1298 - (Max_HW_MTU-4)> if there is QinQ interface on parent     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu x       | qinq           | x        | x - 22                   | -  <1302 - Max_HW_MTU>                                              |
|             |                |          |                          |                                                                     |
|             |                |          | for MPLS and other types |                                                                     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+

**Command syntax: mtu [l2-mtu]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

The command is applicable to the following interface types:

- Physical
- Physical vlan
- Bundle
- Bundle vlan
- mgmt0
- IRB

**Parameter table**

+-----------+----------------------------------------------------------------+-----------+---------+
| Parameter | Description                                                    | Range     | Default |
+===========+================================================================+===========+=========+
| l2-mtu    | Set the max transmission unit size in octets for L2 interface. | 1294-9300 | \-      |
+-----------+----------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces

    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# mtu 1514

    dnRouter(cfg-if)# bundle-1.100
    dnRouter(cfg-if-bundle-1.100)# mtu 1514

    dnRouter(cfg-if)# ge10-2/1/1.100
    dnRouter(cfg-if-ge10-2/1/1.100)# mtu 9000


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1.100)# no mtu

**Command History**

+---------+---------------------------------------------------------------+
| Release | Modification                                                  |
+=========+===============================================================+
| 16.1    | Command introduced. Split from general interface MTU command. |
+---------+---------------------------------------------------------------+
| 18.3    | Extended the supported MTU range.                             |
+---------+---------------------------------------------------------------+

---

## interfaces mtu-mpls.rst

interfaces mtu-mpls
-------------------

**Minimum user role:** operator

The maximum transmission unit (MTU) of a communication protocol of a layer defines the size of the largest protocol data unit that the layer is allowed to transmit over one interface. The MTU command configures L2 or L3 MTU for the interfaces. MTU is applicable to both control and datapath packets. The interface MTU affects only control traffic. Make sure that the MTU values are identical on all devices connected to the L2 network.

-	The sub-interface MTU must not be greater than the physical parent port MTU. The interface/sub-interface MTU must not be greater than max-hw-mtu (9300 for x86/QMX/J2 platforms).
-	NCP-40C and NCP-10CD support up to 8 different MTU configurations.
-	MPLS MTU assumes 2 MPLS labels (the labels included in the MTU calculation)

Each MTU profile configuration includes a unique tuple of all MTU types. For example:

-	MTU profile 0: (L2= 9000B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)
-	MTU profile 1: (L2= 9004B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)

The following table summarizes all available combinations in this version. x denotes the configured frame size.

+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| Command     | Interface type | L2 frame | L3 frame                 | Validated range                                                     |
+=============+================+==========+==========================+=====================================================================+
| mtu-mpls x  | untagged       |          | x for mpls               | -  <1280 - (Max_HW_MTU-14)> if there are no sub interfaces under it |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1280 - (Max_HW_MTU-18)> if there is .1Q interface under it      |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1280 - (Max_HW_MTU-22)> if there is QinQ interface under it     |
|             |                |          |                          |                                                                     |
|             |                |          |                          |                                                                     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu-mpls x  | .1q            |          | x for mpls               | -  <1280 - (Max_HW_MTU-18)> if there is no QinQ interface on parent |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1280 - (Max_HW_MTU-22)> if there is QinQ interface on parent    |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu-mpls x  | qinq           |          | x for mpls               | -  <1280 - (Max_HW_MTU-22)>                                         |
|             |                |          |                          |                                                                     |
|             |                |          |                          |                                                                     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+

**Command syntax: mtu-mpls [mpls-mtu]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

The command is applicable to the following interface types:

- Physical
- Physical vlan
- Bundle
- Bundle vlan
- IRB

**Parameter table**

+-----------+----------------------------------+-----------+---------+
| Parameter | Description                      | Range     | Default |
+===========+==================================+===========+=========+
| mpls-mtu  | MPLS MTU value of the interface. | 1280-9286 | \-      |
+-----------+----------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces

    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# mtu-mpls 1514

    dnRouter(cfg-if)# bundle-1.100
    dnRouter(cfg-if-bundle-1.100)# mtu-mpls 1514

    dnRouter(cfg-if)# ge10-2/1/1.100
    dnRouter(cfg-if-ge10-2/1/1.100)# mtu-mpls 9000


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1.100)# no mtu-mpls

**Command History**

+---------+---------------------------------------------------------------+
| Release | Modification                                                  |
+=========+===============================================================+
| 16.1    | Command introduced. Split from general interface MTU command. |
+---------+---------------------------------------------------------------+
| 18.3    | Extended the supported MTU range.                             |
+---------+---------------------------------------------------------------+

---

## interfaces mtu.rst

interfaces mtu
--------------

**Minimum user role:** operator

The maximum transmission unit (MTU) of a communication protocol of a layer defines the size of the largest protocol data unit that the layer is allowed to transmit over one interface. The MTU command configures L2 or L3 MTU for the interfaces. MTU is applicable to both control and datapath packets. The interface MTU affects only control traffic. Make sure that the MTU values are identical on all devices connected to the L2 network.

-	The sub-interface MTU must not be greater than the physical parent port MTU. The interface/sub-interface MTU must not be greater than max-hw-mtu (9300 for x86/QMX/J2 platforms).
-	NCP-40C and NCP-10CD support up to 8 different MTU configurations.
-	MPLS MTU assumes 2 MPLS labels (the labels included in the MTU calculation)

Each MTU profile configuration includes a unique tuple of all MTU types. For example:

-	MTU profile 0: (L2= 9000B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)
-	MTU profile 1: (L2= 9004B, ipv4 = 8000B, ipv6 = 8000B, mpls = 8600B)

The following table summarizes all available combinations in this version. x denotes the configured frame size.

+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| Command     | Interface type | L2 frame | L3 frame                 | Validated range                                                     |
+=============+================+==========+==========================+=====================================================================+
| mtu x       | untagged       | x        | x - 14                   | -  <1514 - Max_HW_MTU> if there are no sub interfaces under it      |
|             |                |          |                          |                                                                     |
|             |                |          | for MPLS and other types | -  <1514 - (Max_HW_MTU-4)> if there is .1Q interface under it       |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1514 - (Max_HW_MTU-8)> if there is QinQ interface under it      |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu x       | .1q            | x        | x - 18                   | -  <1518 - Max_HW_MTU> if there is no QinQ interface on parent      |
|             |                |          |                          |                                                                     |
|             |                |          | for MPLS and other types | -  <1518 - (Max_HW_MTU-4)> if there is QinQ interface on parent     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu x       | qinq           | x        | x - 22                   | -  <1522 - Max_HW_MTU>                                              |
|             |                |          |                          |                                                                     |
|             |                |          | for MPLS and other types |                                                                     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu ipv4 x  | untagged       |          | x for ipv4               | -  <1500 - (Max_HW_MTU-14)> if there are no sub interfaces under it |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1500 - (Max_HW_MTU-18)> if there is .1Q interface under it      |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1500 - (Max_HW_MTU-22)> if there is QinQ interface under it     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu ipv4 x  | .1q            |          | x for ipv4               | -  <1500 - (Max_HW_MTU-18)> if there is no QinQ interface on parent |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1500 - (Max_HW_MTU-22)> if there is QinQ interface on parent    |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu ipv4 x  | qinq           |          | x for ipv4               | -  <1500 - (Max_HW_MTU-22)>                                         |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu ipv6 x  | untagged       |          | x for ipv6               | -  <1500 - (Max_HW_MTU-14)> if there are no sub interfaces under it |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1500 - (Max_HW_MTU-18)> if there is .1Q interface under it      |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1500 - (Max_HW_MTU-22)> if there is QinQ interface under it     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu ipv6 x  | .1q            |          | x for ipv6               | -  <1500 - (Max_HW_MTU-18)> if there is no QinQ interface on parent |
|             |                |          |                          |                                                                     |
|             |                |          |                          | <1500 - (Max_HW_MTU-22)> if there is QinQ interface on parent       |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu ipv6 x  | qinq           |          | x for ipv6               | -  <1500 - (Max_HW_MTU-22)>                                         |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu mpls x  | untagged       |          | x for mpls               | -  <1508 - (Max_HW_MTU-14)> if there are no sub interfaces under it |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1508 - (Max_HW_MTU-18)> if there is .1Q interface under it      |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1508 - (Max_HW_MTU-22)> if there is QinQ interface under it     |
|             |                |          |                          |                                                                     |
|             |                |          |                          |                                                                     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu mpls x  | .1q            |          | x for mpls               | -  <1508 - (Max_HW_MTU-18)> if there is no QinQ interface on parent |
|             |                |          |                          |                                                                     |
|             |                |          |                          | -  <1508 - (Max_HW_MTU-22)> if there is QinQ interface on parent    |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+
| mtu mpls x  | qinq           |          | x for mpls               | -  <1508 - (Max_HW_MTU-22)>                                         |
|             |                |          |                          |                                                                     |
|             |                |          |                          |                                                                     |
+-------------+----------------+----------+--------------------------+---------------------------------------------------------------------+

You can limit the allowed size of control packets going through an interface with the following command:

**Command syntax: mtu** [mtu] mtu-ipv4 [mtu-ipv4] mtu-ipv6 [mtu-ipv6] mtu-mpls [mtu-mpls]

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:
	- Physical
	- Physical vlan
	- Bundle
	- Bundle vlan
	- mgmt0


**Parameter table**

+---------------+------------------------------------------------------------------------------+------------------------+-------------+
|               |                                                                              |                        |             |
| Parameter     | Description                                                                  | Range                  | Default     |
+===============+==============================================================================+========================+=============+
|               |                                                                              |                        |             |
| mtu           | The maximum packet size for all packets that go   through the interface.     | 1514..max_hw_mtu       | 1514        |
+---------------+------------------------------------------------------------------------------+------------------------+-------------+
|               |                                                                              |                        |             |
| mtu-ipv4      | The maximum packet size for IPv4 packets that go   through the interface.    | 1500..max_hw_mtu-14    | 1500        |
+---------------+------------------------------------------------------------------------------+------------------------+-------------+
|               |                                                                              |                        |             |
| mtu-ipv6      | The maximum packet size for IPv6 packets that go   through the interface.    | 1500..max_hw_mtu-14    | 1500        |
+---------------+------------------------------------------------------------------------------+------------------------+-------------+
|               |                                                                              |                        |             |
| mtu-mpls      | The maximum packet size for MPLS packets that go   through the interface.    | 1508..max_hw_mtu-14    | 1500        |
+---------------+------------------------------------------------------------------------------+------------------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces 
	
	dnRouter(cfg-if)# bundle-1
	dnRouter(cfg-if-bundle-1)# mtu 1514
	
	dnRouter(cfg-if)# bundle-1.100
	dnRouter(cfg-if-bundle-1.100)# mtu 1514
	
	dnRouter(cfg-if)# ge10-2/1/1.100
	dnRouter(cfg-if-ge10-2/1/1.100)# mtu 9000


**Removing Configuration**

To revert to the default value:
::

	dnRouter(cfg-if-bundle-1.100)# no mtu


.. **Help line:** Configure interface mtu

**Command History**

+-------------+-----------------------------------------------------------------------------------+
|             |                                                                                   |
| Release     | Modification                                                                      |
+=============+===================================================================================+
|             |                                                                                   |
| 5.1.0       | Command introduced                                                                |
+-------------+-----------------------------------------------------------------------------------+
|             |                                                                                   |
| 6.0         | Changed syntax from interface to interfaces,   added address family, removed mpls |
|             |                                                                                   |
|             | Applied new hierarchy                                                             |
+-------------+-----------------------------------------------------------------------------------+
|             |                                                                                   |
| 9.0         | Removed MTU configuration per address-family                                      |
+-------------+-----------------------------------------------------------------------------------+
|             |                                                                                   |
| 11.0        | Added option to configure separately for IPv4,   IPv6 and MPLS                    |
+-------------+-----------------------------------------------------------------------------------+
|             |                                                                                   |
| 11.4        | Added support for GRE-tunnels                                                     |
+-------------+-----------------------------------------------------------------------------------+

---

## interfaces naming conventions.rst

interface naming conventions
----------------------------

The following are the types of interfaces you can provision.

+----------------------+------------------------+----------------------------------------------+----------------------+
| Interface Scheme     | Syntax Convention      | Range                                        | Example              |
+======================+========================+==============================================+======================+
| fab-<nce>X-Y/Z/W     | NCE: Node type         | NCP: fabric interface on NCP (NCP-to-NCF)    | fab-ncp400-1/0/3     |
|                      |                        | NCF: fabric interface on NCF (NCF-to-NCP)    | fab-ncf400-1/0/20    |
|                      +------------------------+----------------------------------------------+                      |
|                      | X: Interface speed     | 400 GbE                                      |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | Y: Node ID             | NCP: 0..255                                  |                      |
|                      |                        | NCF: 0..12                                   |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | Z: Slot ID             | 0                                            |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | W: Port ID             | As displayed on the hardware panel           |                      |
+----------------------+------------------------+----------------------------------------------+----------------------+
| mgmt-ncc-X/Y         | X: Node ID             | 0..1                                         | mgmt-ncc-0           |
|                      +------------------------+----------------------------------------------+ mgmt-ncc-0/0         |
|                      | Y: Eth. port ID        | 0..1                                         | mgmt-ncc-1/1         |
+----------------------+------------------------+----------------------------------------------+----------------------+
| ctrl-<nce>-X/Y       | NCE: Node type         | NCC control interface                        | ctrl-ncc-1/0         |
|                      |                        | NCP control interface                        | ctrl-ncp-3/1         |
|                      |                        | NCF control interface                        | ctrl-ncf-0/0         |
|                      |                        | NCM control interface                        | ctrl-ncm-B0/1        |
|                      +------------------------+----------------------------------------------+                      |
|                      | X: Node ID             | NCC: 0..1                                    |                      |
|                      |                        | NCP: 0..255                                  |                      |
|                      |                        | NCF: 0..12                                   |                      |
|                      |                        | NCM: A0, B0, A1, B1                          |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | Y: Eth. port ID        | 0..1                                         |                      |
+----------------------+------------------------+----------------------------------------------+----------------------+
| ipmi-<nce>-X/Y       | NCE: Node type         | NCC IPMI interface                           | ipmi-ncc-0/0         |
|                      |                        | NCP IPMI interface                           | ipmi-ncp-1/0         |
|                      |                        | NCF IPMI interface                           | ipmi-ncf-0/0         |
|                      +------------------------+----------------------------------------------+                      |
|                      | X: Node ID             | NCC: 0..1                                    |                      |
|                      |                        | NCP: 0..255                                  |                      |
|                      |                        | NCF: 0..12                                   |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | Y: Port ID             | 0                                            |                      |
+----------------------+------------------------+----------------------------------------------+----------------------+
| console-<nce>-X/Y    | NCE: Node type         | NCC console interface                        | console-ncc-0/0      |
|                      |                        | NCP console interface                        | console-ncp-2/0      |
|                      |                        | NCF console interface                        | console-ncf-0/0      |
|                      +------------------------+----------------------------------------------+                      |
|                      | X: Node ID             | NCC: 0..1                                    |                      |
|                      |                        | NCP: 0..255                                  |                      |
|                      |                        | NCF: 0..12                                   |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | Y: Port ID             | 0                                            |                      |
+----------------------+------------------------+----------------------------------------------+----------------------+
| mgmt0                | Logical out-of-band management interface                                                     |
+----------------------+------------------------+----------------------------------------------+----------------------+
| geX-f/n/p            | X: Interface speed     | 10, 25, 40, 50, 100                          | ge100-1/0/39         |
|                      +------------------------+----------------------------------------------+                      |
|                      | f: NCP ID              | 0..255                                       |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | n: Slot ID             | 0..255                                       |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | p: Port ID             | 0..255                                       |                      |
+----------------------+------------------------+----------------------------------------------+----------------------+
| bundle-x             | x: bundle-id           | 1..1023                                      | bundle-2             |
+----------------------+------------------------+----------------------------------------------+----------------------+
| .y                   | y: Sub-interface ID    | 1..65535                                     | ge100-1/0/39.2057    |
|                      |                        |                                              +----------------------+
|                      |                        |                                              | bundle-2.102         |
+----------------------+------------------------+----------------------------------------------+----------------------+
| loX                  | X: Loopback ID         | 0..65535                                     | lo0                  |
+----------------------+------------------------+----------------------------------------------+----------------------+
| gre-tunnel-X         | X: GRE tunnel ID       | 0..4                                         | gre-tunnel-1         |
+----------------------+------------------------+----------------------------------------------+----------------------+
| irbX                 | X: IRB ID              | 1..65535                                     | irb1                 |
+----------------------+------------------------+----------------------------------------------+----------------------+
---

## interfaces ndp router-advertisement.rst

interfaces ndp router-advertisement
-----------------------------------

**Minimum user role:** operator

To enter the ndp router-advertisement configuration level:

**Command syntax: ndp router-advertisement**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan
  - IRB.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# irb1
    dnRouter(cfg-if-irb1)# ndp router-advertisement
    dnRouter(cfg-if-irb1-ndp-ra)#


**Removing Configuration**

To clear all NDP router-advertisement settings:
::

    - dnRouter(cfg-if-irb1)# no ndp router-advertisement

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.2    | Command introduced |
+---------+--------------------+

---

## interfaces ndp.rst

interfaces ndp host-address mac-address
---------------------------------------

**Minimum user role:** operator

For static routing, you need to manually specify the next hop router's address using the link-local address of the router.

To add a static NDP entry for an interface, use the following command in configuration mode:

**Command syntax: ndp host-address [host-ipv6-address] mac-address [mac-address]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan
  - IRB

**Parameter table**

+-------------------+------------------------------------------------------------------+-------------------+---------+
| Parameter         | Description                                                      | Range             | Default |
+===================+==================================================================+===================+=========+
| host-ipv6-address | The IPv6 address of the host device being added to the NDP table | X:X::X:X          | \-      |
+-------------------+------------------------------------------------------------------+-------------------+---------+
| mac-address       | The MAC address for the host device being added to the NDP table | xx:xx:xx:xx:xx:xx | \-      |
+-------------------+------------------------------------------------------------------+-------------------+---------+

**Example**

To add a static NDP entry that maps 2001:ab12::1 to MAC address 12:ab:47:dd:ff:89:
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp host-address 2001:ab12::1 mac-address 12:ab:47:dd:ff:89


**Removing Configuration**

To remove a specific static NDP entry:
::

    dnRouter(cfg-if-ge100-1/1/1)# no ndp host-address 2001:ab12::1

To clear all static NDP entries on the interface and the router-advertisement configuration:
::

    dnRouter(cfg-if-ge10-1/1/1)# no ndp

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces, applied new hierarchy |
+---------+--------------------------------------------------------------------+
| 11.0    | Changed syntax from ipv6-address to host-address                   |
+---------+--------------------------------------------------------------------+

---

## interfaces overview.rst

Interfaces Overview
-------------------
DNOS supports a highly modular range of high-speed Ethernet interfaces in a wide range of speeds, as follows.

- 1 GbE
- 10 GbE
- 25 GbE
- 40 GbE
- 100 GbE
- 400 GbE

This solution requires fewer physical interconnects, accelerating provisioning and reducing deployment and sparing costs.

The following types of interfaces are available for user provisioning:

- High-speed Physical Interfaces
- Link Aggregation Group Interfaces (Bundle Interfaces)
- Loopback Interfaces
- Sub-interfaces
- GRE-tunnel Interface
- Interface Naming Conventions
- Configure Interfaces
- Show Config Interfaces
- Interfaces Displaying Information
- Clear Interfaces Counters
- Clear Interfaces Dampening Penalty

---

## interfaces port-priority.rst

interfaces port-priority
------------------------

**Minimum user role:** operator

Port priority is used to dynamically group ports into bundles. The priority of the port within the bundle determines which ports have precedence in participating in the bundle interface.

To configure the port priority:

**Command syntax: port-priority [port-priority]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the physical interfaces

**Parameter table**

+---------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter     | Description                                                                      | Range   | Default |
+===============+==================================================================================+=========+=========+
| port-priority | The priority withing the bundle to give to the interface.  A lower value denotes | 0-65535 | 32768   |
|               | a higher priority.                                                               |         |         |
+---------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# port-priority 0


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-0/0/0)# no port-priority

**Command History**

+---------+-----------------------------------+
| Release | Modification                      |
+=========+===================================+
| 6.0     | Command introduced                |
+---------+-----------------------------------+
| 10.0    | Command moved hierarchy from LACP |
+---------+-----------------------------------+

---

## interfaces priority-flow-control admin-state.rst

interfaces priority-flow-control admin-state
--------------------------------------------

**Minimum user role:** operator

To enable/disable priority-based flow control on the interface:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter   | Description                                                                      | Range        | Default |
+=============+==================================================================================+==============+=========+
| admin-state | The administrative state of the priority-based flow control feature for the      | | enabled    | \-      |
|             | specific interface.                                                              | | disabled   |         |
+-------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# priority-flow-control
    dnRouter(cfg-if-ge100-1/0/1-pfc)# admin-state enabled
    dnRouter(cfg-if-ge100-1/0/1-pfc)#

    dnRouter# configure
    dnRouter(cfg)# interfaces bundle-2
    dnRouter(cfg-if-bundle-2)# priority-flow-control
    dnRouter(cfg-if-bundle-2-pfc)# admin-state disabled
    dnRouter(cfg-if-bundle-2-pfc)#


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/12-pfc)# no admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## interfaces priority-flow-control clear-threshold.rst

interfaces priority-flow-control clear-threshold
------------------------------------------------

**Minimum user role:** operator

When the VSQ size for a certain queue goes below the PFC clear threshold, the transmition of PFC pause frames on the interface is stopped. To configure the interface PFC clear threshold that applies for all traffic classes:

**Command syntax: clear-threshold [clear-threshold] [units]**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control

**Note**

- Default clear-threshold is 80 kbytes, it is set by global configuration. An explicit configuration for a specific traffic class takes precendence over the inherited configuration

- Clear-threshold must be lower than the interface pause-threshold or the traffic class specific pause-threshold

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+-------------+---------+
| Parameter       | Description                                                                      | Range       | Default |
+=================+==================================================================================+=============+=========+
| clear-threshold | The PFC clear threshold for stopping transmission of pause frames for a certain  | 0-199999744 | \-      |
|                 | traffic class. The threshold is set for each traffic class separately.           |             |         |
+-----------------+----------------------------------------------------------------------------------+-------------+---------+
| units           |                                                                                  | | bytes     | bytes   |
|                 |                                                                                  | | kbytes    |         |
|                 |                                                                                  | | mbytes    |         |
+-----------------+----------------------------------------------------------------------------------+-------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# priority-flow-control
    dnRouter(cfg-if-ge100-1/0/1-pfc)# clear-threshold 100 kbytes
    dnRouter(cfg-if-ge100-1/0/1-pfc)#


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/13-pfc)# no clear-threshold

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## interfaces priority-flow-control deadlock detection-timer.rst

interfaces priority-flow-control deadlock detection-timer
---------------------------------------------------------

**Minimum user role:** operator

If the queue is always in the PFC-XOFF (flow-controlled) state within the specified PFC deadlock detection period, the system determines that a PFC deadlock occurs. 
In this case, the PFC deadlock recovery process needs to be performed.

To configure the priority-based flow control deadlock detection-timer on the interface:

**Command syntax: detection-timer [detection-timer]**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control deadlock

**Note**
- The user-configured value is in milliseconds, but the actual value that is set in the hardware is converted to the closest power of 2 in core clock cycles.
- The PFC deadlock detection-timer must be enabled (greater than 0) for the PFC deadlock feature to be enabled and for the recovery-timer configuration to be valid.
- This configuration must be set with the same value on all applicable ports sharing the same CDU (e.g., breakout interfaces), so that it will not be overriden.

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter       | Description                                                                      | Range | Default |
+=================+==================================================================================+=======+=========+
| detection-timer | The priority-based flow control deadlock detecction timer in milliseconds.       | 0-512 | 0       |
|                 | Specifies the duration of the PFC XOFF state to indicate the PFC deadlock        |       |         |
|                 | condition is present.                                                            |       |         |
+-----------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# priority-flow-control
    dnRouter(cfg-if-ge100-1/0/1-pfc)# deadlock
    dnRouter(cfg-if-ge100-1/0/1-pfc-deadlock)# detection-timer 8


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/12-pfc-deadlock)# no detection-timer

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interfaces priority-flow-control deadlock.rst

interfaces priority-flow-control deadlock
-----------------------------------------

**Minimum user role:** operator

PFC deadlock is a network state in which congestion occurs on multiple switches simultaneously due to a loop or other causes. The interface buffer usage of each switch 
exceeds the threshold, the switches wait for each other to release resources, and data flows on all switches are permanently blocked consequently. 
This feature periodically detects whether the device is in the PFC deadlock state. If an interface is always in the PFC XOFF state within the PFC deadlock detection 
interval, the device enters the PFC deadlock state. If PFC deadlock detection is recovered in automatic mode, the device automatically releases the deadlock state and 
recovers PFC and PFC deadlock detection after the delay timer expires. During the delay timer period, the device disables PFC and PFC deadlock detection on the interface,
so that packets can be forwarded properly.

To enter the PFC deadlock configuration on an interface:

**Command syntax: deadlock**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control

**Note**
- The command is applicable to physical interface types.

- You can view the PFC administrative state on an interface using the show interfaces detail command. See "show interfaces detail".

- To view PFC counters use the show PFC counters command. See "show priority-flow-control interfaces counters".

- To view PFC queues use the show PFC queues command. See "show priority-flow-control interfaces queues".

- The PFC deadlock configuration is applied for all traffic classes on the interface.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# priority-flow-control
    dnRouter(cfg-if-ge100-0/0/0-pfc-deadlock)# deadlock


**Removing Configuration**

To revert all PFC deadlock settings to their default values:
::

    dnRouter(cfg-if-ge100-0/0/0-pfc)# no deadlock

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interfaces priority-flow-control pause-threshold.rst

interfaces priority-flow-control pause-threshold max-threshold
--------------------------------------------------------------

**Minimum user role:** operator

The pause threshold is set dynamically between a minimum and maximum value, proportional to the amount of free buffer resources. The slope between the minimum and maximum values is determined by the alpha parameter. As the amount of free buffer resources increases, the pause threshold increases. When the VSQ size for a certain queue crosses the PFC pause threshold PFC pause frames are sent to the peer until it falls below the clear threshold.

**Command syntax: pause-threshold max-threshold [max-pause-threshold] [units1] min-threshold [min-pause-threshold] [units2] alpha [alpha]**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control

**Note**

- The default pause-threshold is 200Kbytes, it is set by the global configuration. An explicit configuration for a specific interface or traffic class takes precedence over the inherited global configuration. To use dynamic PFC set the minimum threshold to be lower than the maximum threshold and add the alpha.

- The clear-threshold must be lower than the interface pause-threshold or the traffic class specific pause-threshold.

- The dynamic PFC formula (FADT):

- If a free resource/(2^alpha) is bigger than the max-threshold => threshold=max-threshold

- If a free resource/(2^alpha) is smaller than min-threshold (low resources) => threshold=min-threshold

- If the max-threshold > free-resource/(2^alpha) > min-threshold => threshold=free-resource/(2^alpha)

**Parameter table**

+---------------------+------------------------------------------------------------------------------+---------------+---------+
| Parameter           | Description                                                                  | Range         | Default |
+=====================+==============================================================================+===============+=========+
| max-pause-threshold | The PFC max pause threshold is the max VSQ size for triggering pause frames. | 256-200000000 | \-      |
+---------------------+------------------------------------------------------------------------------+---------------+---------+
| units1              |                                                                              | | bytes       | bytes   |
|                     |                                                                              | | kbytes      |         |
|                     |                                                                              | | mbytes      |         |
+---------------------+------------------------------------------------------------------------------+---------------+---------+
| min-pause-threshold | The PFC min pause threshold is the min VSQ size for triggering pause frames. | 256-200000000 | \-      |
+---------------------+------------------------------------------------------------------------------+---------------+---------+
| units2              |                                                                              | | bytes       | bytes   |
|                     |                                                                              | | kbytes      |         |
|                     |                                                                              | | mbytes      |         |
+---------------------+------------------------------------------------------------------------------+---------------+---------+
| alpha               | PFC alpha set dynamic threshold slope.                                       | 0-8           | \-      |
+---------------------+------------------------------------------------------------------------------+---------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# priority-flow-control
    dnRouter(cfg-if-ge100-1/0/1-pfc)# pause-threshold max-threshold 400 kbytes min-threshold 200 kbytes alpha 4
    dnRouter(cfg-if-ge100-1/0/1-pfc)# clear-threshold 100 kbytes


**Removing Configuration**

To revert to the default value
::

    dnRouter(cfg-if-ge100-1/0/13-pfc)# no pause-threshold

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+
| 19.10   | Added Dynamic PFC  |
+---------+--------------------+

---

## interfaces priority-flow-control traffic-class admin-state.rst

interfaces priority-flow-control traffic-class admin-state
----------------------------------------------------------

**Minimum user role:** operator

To enable/disable priority-based flow control on an interface:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control traffic-class

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter   | Description                                                                      | Range        | Default |
+=============+==================================================================================+==============+=========+
| admin-state | The administrative state of the priority-based flow control feature for the      | | enabled    | \-      |
|             | specific traffic-class.                                                          | | disabled   |         |
+-------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# priority-flow-control
    dnRouter(cfg-if-ge100-1/0/1-pfc)# traffic-class 5
    dnRouter(cfg-if-ge100-1/0/1-pfc-tc5)# admin-state enabled


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/1-pfc-tc5)# no admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.10   | Command introduced |
+---------+--------------------+

---

## interfaces priority-flow-control traffic-class clear-threshold.rst

interfaces priority-flow-control traffic-class clear-threshold
--------------------------------------------------------------

**Minimum user role:** operator

When the VSQ size for a certain queue goes below the PFC clear threshold, the transmition of PFC pause frames on the interface is stopped. To configure the PFC clear threshold on the interface for a specific traffic class:

**Command syntax: clear-threshold [clear-threshold] [units]**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control traffic-class

**Note**

- Default clear-threshold is 80Kbytes, it is set by global configuration. An explicit configuration under a certain traffic class takes precendence over the inherited global configuration

- Clear-threshold must be lower than the interface pause-threshold or the traffic class specific pause-threshold

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+-------------+---------+
| Parameter       | Description                                                                      | Range       | Default |
+=================+==================================================================================+=============+=========+
| clear-threshold | The PFC clear threshold for stopping transmission of pause frames for a certain  | 0-199999744 | \-      |
|                 | traffic class. The threshold is configured for each traffic class separately.    |             |         |
+-----------------+----------------------------------------------------------------------------------+-------------+---------+
| units           |                                                                                  | | bytes     | bytes   |
|                 |                                                                                  | | kbytes    |         |
|                 |                                                                                  | | mbytes    |         |
+-----------------+----------------------------------------------------------------------------------+-------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# priority-flow-control
    dnRouter(cfg-if-ge100-1/0/1-pfc)# traffic-class 2
    dnRouter(cfg-ge100-1/0/1-pfc-tc2)# clear-threshold 100 kbytes


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-ge100-1/0/13-pfc-tc2)# no clear-threshold

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.10   | Command introduced |
+---------+--------------------+

---

## interfaces priority-flow-control traffic-class deadlock recovery-timer.rst

interfaces priority-flow-control traffic-class deadlock recovery-timer
----------------------------------------------------------------------

**Minimum user role:** operator

During PFC deadlock recovery, PFC frames received by the interface are ignored. The internal scheduler resumes traffic sending in the specified priority queue. 
After the recovery period expires, the normal flow control mechanism of PFC is resumed. If the system still determines that a deadlock occurs in the next deadlock 
detection period, the deadlock recovery process is performed again.

To configure the priority-based flow control deadlock recovery-timer on the interface:

**Command syntax: deadlock recovery-timer [deadlock-recovery-timer]**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control traffic-class

**Note**
- The PFC deadlock detection-timer must be enabled (greater than 0) for the PFC deadlock feature to be enabled and for the recovery-timer configuration to be valid.
- If the PFC deadlock recovery timer is set to 0, then no action will be performed in case that a deadlock condition is detected.

**Parameter table**

+-------------------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter               | Description                                                                      | Range   | Default |
+=========================+==================================================================================+=========+=========+
| deadlock-recovery-timer | The priority-based flow control deadlock recovery timer in milliseconds.         | 0-10000 | 0       |
|                         | Specifies the duration to ignore the PFC XOFF state and keep transmitting        |         |         |
|                         | traffic after entering PFC deadlock state.                                       |         |         |
+-------------------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# priority-flow-control
    dnRouter(cfg-if-ge100-1/0/1-pfc)# traffic-class 5
    dnRouter(cfg-if-ge100-1/0/1-pfc-tc5)# deadlock recovery-timer 100


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/12-pfc-tc5)# no deadlock recovery-timer

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## interfaces priority-flow-control traffic-class pause-threshold.rst

interfaces priority-flow-control traffic-class pause-threshold max-threshold
----------------------------------------------------------------------------

**Minimum user role:** operator

The pause threshold is set dynamically between a minimum and maximum value, proportional to the amount of free buffer resources. The slope between the minimum and maximum values is determined by the alpha parameter. As the amount of free buffer resources increases, the pause threshold increases. When the VSQ size for a certain queue crosses the PFC pause threshold PFC pause frames are sent to the peer until it falls below the clear threshold.

**Command syntax: pause-threshold max-threshold [max-pause-threshold] [units1] min-threshold [min-pause-threshold] [units2] alpha [alpha]**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control traffic-class

**Note**

- The default pause-threshold is 200KB, it is set by the global configuration. An explicit configuration for a specific interface or traffic class takes precedence over the inherited global configuration. To use dynamic PFC set the minimum threshold to be lower than the maximum threshold and add the alpha.

- The clear-threshold must be lower than the interface pause-threshold or the traffic class specific pause-threshold.

- The dynamic PFC formula (FADT):

- If a free resource/(2^alpha) is bigger than the max-threshold => threshold=max-threshold

- If a free resource/(2^alpha) is smaller than min-threshold (low resources) => threshold=min-threshold

- If the max-threshold > free-resource/(2^alpha) > min-threshold => threshold=free-resource/(2^alpha)

**Parameter table**

+---------------------+----------------------------------------------------------------------------------+---------------+---------+
| Parameter           | Description                                                                      | Range         | Default |
+=====================+==================================================================================+===============+=========+
| max-pause-threshold | PFC max pause threshold for specific traffic class is the min VSQ size for       | 256-200000000 | \-      |
|                     | triggering pause frames.                                                         |               |         |
+---------------------+----------------------------------------------------------------------------------+---------------+---------+
| units1              |                                                                                  | | bytes       | bytes   |
|                     |                                                                                  | | kbytes      |         |
|                     |                                                                                  | | mbytes      |         |
+---------------------+----------------------------------------------------------------------------------+---------------+---------+
| min-pause-threshold | PFC min pause threshold for specific traffic class is the min VSQ size for       | 256-200000000 | \-      |
|                     | triggering pause frames.                                                         |               |         |
+---------------------+----------------------------------------------------------------------------------+---------------+---------+
| units2              |                                                                                  | | bytes       | bytes   |
|                     |                                                                                  | | kbytes      |         |
|                     |                                                                                  | | mbytes      |         |
+---------------------+----------------------------------------------------------------------------------+---------------+---------+
| alpha               | PFC alpha set dynamic threshold slope for a specific traffic class.              | 0-7           | \-      |
+---------------------+----------------------------------------------------------------------------------+---------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# priority-flow-control
    dnRouter(cfg-if-ge100-1/0/1-pfc)# traffic-class 3 pause-threshold max-threshold 400 kbytes min-threshold 200 kbytes alpha 4
    dnRouter(cfg-if-ge100-1/0/1-pfc-tc3)# clear-threshold 100 kbytes


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/13-pfc)# no pause-threshold

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+
| 19.10   | Added Dynamic PFC  |
+---------+--------------------+

---

## interfaces priority-flow-control traffic-class.rst

interfaces priority-flow-control traffic-class
----------------------------------------------

**Minimum user role:** operator

To enter PFC configuration level on the interface for a specific traffic class:

**Command syntax: traffic-class [traffic-class]**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control

**Parameter table**

+---------------+---------------------------------------+-------+---------+
| Parameter     | Description                           | Range | Default |
+===============+=======================================+=======+=========+
| traffic-class | thresholds per specific traffic class | 0-7   | \-      |
+---------------+---------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# priority-flow-control
    dnRouter(cfg-if-ge100-1/0/1-pfc)# traffic-class 3
    dnRouter(cfg-ge100-1/0/1-pfc-tc3)#


**Removing Configuration**

To revert to the default value for a specific traffic class (inherited from global configuration)
::

    dnRouter(cfg-if-ge100-1/0/13-pfc)# no traffic-class 3

To revert to the default value for all traffic classes on the interface (inherited from global configuration)
::

    dnRouter(cfg-if-ge100-1/0/13-pfc)# no traffic-class

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## interfaces priority-flow-control.rst

interfaces priority-flow-control
--------------------------------

**Minimum user role:** operator

Priority Flow Control (PFC; IEEE 802.1Qbb), also referred to as Class-based Flow Control (CBFC) or Per Priority Pause (PPP), is a mechanism that prevents frame loss due to congestion.
PFC is similar to 802.3x Flow Control (pause frames) or Link-level Flow Control (LFC), however, PFC functions on a per traffic class basis.
To enter the PFC configuration on an interface:

**Command syntax: priority-flow-control**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**
- The command is applicable to physical interface types.

- You can view the PFC administrative state on an interface using the show interfaces detail command. See "show interfaces detail".

- To view PFC counters use the show PFC counters command. See "show priority-flow-control interfaces counters".

- To view PFC queues use the show PFC queues command. See "show priority-flow-control interfaces queues".

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# priority-flow-control
    dnRouter(cfg-if-ge100-0/0/0-pfc)#


**Removing Configuration**

To revert all PFC settings to their default values:
::

    dnRouter(cfg-if-ge100-0/0/0)# no priority-flow-control

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## interfaces qos ip-marking.rst

interfaces qos ip-marking
-------------------------

**Minimum user role:** operator

The qos ip-marking configuration allows to determine whether the IP DSCP marking is trusted or not. If the marking is untrusted, the DSCP field is remarked on ingress and on egress. When qos ip-marking is untrusted, the DSCP field is remarked (modified) for IPv4 packets sent and received through the interface (IPv6 TC field is remarked according to the same rules). The incoming DSCP values are remarked according to the qos remarking-map table and the qos-tag and drop-tag assigned to the packet by the ingress policy rules. The DSCP can be overridden by a specific set of dscp commands on the egress policy assigned to the interface.

If qos ip-marking is trusted, the incoming packet DSCP marking is trusted, and the DSCP field is not remarked (unless sent through an untrusted interface).
MPLS packets are not expected to be sent or received through an ip-marking untrusted interface.

To designate interface QoS ip marking as trusted or untrusted:

**Command syntax: qos ip-marking [trust-mode]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan

- While ip-marking is configured on physical and bundle interfaces, it applies to all IPv4 and IPv6 of their sub-interfaces.

- xconnect sub-interfaces are always trusted.

**Parameter table**

+------------+-------------------------------------------------------------+---------------+---------+
| Parameter  | Description                                                 | Range         | Default |
+============+=============================================================+===============+=========+
| trust-mode | Designate interface QoS ip marking as trusted or untrusted. | | trusted     | \-      |
|            |                                                             | | untrusted   |         |
+------------+-------------------------------------------------------------+---------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# qos ip-marking untrusted
    dnRouter(cfg-if-ge100-0/0/0)# qos ip-marking trusted


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-0/0/0)# no qos ip-marking

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 13.0    | Command introduced |
+---------+--------------------+

---

## interfaces qos policy.rst

interfaces qos policy direction
-------------------------------

**Minimum user role:** operator

After you have a policy set up, you need to attach it to an interface. To attach a QoS policy to an interface:

**Command syntax: qos policy [policy-name] direction [direction]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan

**Parameter table**

+-------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter   | Description                                                                      | Range            | Default |
+=============+==================================================================================+==================+=========+
| policy-name | Specify the name of an existing policy that you want to attach to the interface. | | string         | \-      |
|             | If the policy does not exist in the database, an error is displayed.             | | length 1-255   |         |
+-------------+----------------------------------------------------------------------------------+------------------+---------+
| direction   | Specify the direction of the traffic to which the policy will apply.             | | in             | \-      |
|             |                                                                                  | | out            |         |
+-------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# qos policy myQoSPolicy1 direction out
    dnRouter(cfg-if-ge100-0/0/0)# qos policy myQoSPolicy2 direction in


**Removing Configuration**

To remove the policy from the interface:
::

    dnRouter(cfg-if-ge100-0/0/0)# no qos policy

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces; applied new hierarchy |
+---------+--------------------------------------------------------------------+
| 9.0     | Not supported in this version.                                     |
+---------+--------------------------------------------------------------------+
| 11.2    | Command re-introduced                                              |
+---------+--------------------------------------------------------------------+

---

## interfaces qppb admin-state.rst

interfaces qppb
---------------

**Minimum user role:** operator


Enables or disables QPPB policy enforcement on traffic received from the interface.

**Command syntax: qppb [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan.

- To apply the qppb policy to a BGP installation on RIB, see the "protocols bgp address-family ipv4-unicast rib-install policy" command in this publication.
- To configure the QoS qppb policy rules and actions, see the "routing-policy qppb-policy" set of commands in this publication. 

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                                      | Range        | Default  |
+=============+==================================================================================+==============+==========+
| admin-state | When enabled, VRF QPPB policy is enforced on traffic received through this       | | enabled    | disabled |
|             | interface.                                                                       | | disabled   |          |
+-------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# qppb enabled
    dnRouter(cfg-if-ge100-0/0/0)# qppb disabled


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-0/0/0)# no qppb

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## interfaces speed.rst

interfaces speed
----------------

**Minimum user role:** operator

- On NCP-36CD-S and NCP-32CD platforms you can set a 400G interface to support a speed of either 400G or 100G (without breakout).
- On NCP-64X12C-S (NCP-Light) platforms you can set a 10G interface to support a speed of either 25G or 10G or 1G (without breakout).

  To set the Ethernet speed of an interface:

**Command syntax: speed [port-speed]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- This command is applicable to physical 400G interfaces on UfiSpace NCP-36CD-S and Accton NCP-32CD platforms that can be set to 100G or to physical 10G interfaces on ufiSpace NCP-64X12C-S platforms that can be set to 25G or 1G.

- Port speed and breakout cannot be configured at the same time on an interface.

**Parameter table**

+------------+-------------------------+---------+---------+
| Parameter  | Description             | Range   | Default |
+============+=========================+=========+=========+
| port-speed | The desired port speed. | | 1     | \-      |
|            |                         | | 10    |         |
|            |                         | | 25    |         |
|            |                         | | 100   |         |
|            |                         | | 400   |         |
+------------+-------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# speed 100

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 speed 400
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge10-0/0/0
    dnRouter(cfg-if-ge10-0/0/0)# speed 1

    dnRouter# configure
    dnRouter(cfg)# interfaces ge10-0/0/0 speed 10


**Removing Configuration**

To revert interface speed to its default value:
::

    dnRouter(cfg-if-ge400-0/0/0)# no speed

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## interfaces untagged.rst

interfaces untagged
-------------------

**Minimum user role:** operator

The untagged command is available only for l2-service enabled sub-interfaces. Defining either VLANs or untagged is mandatory on sub-interfaces and virtual-l2-interfaces. Therefore, for l2-service enabled sub-interfaces, you can either set untagged or ensure that either vlan-id or vlan-tags are defined.

**Command syntax: untagged**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is available for sub-interface (geX-<f>/<n>/<p>.subinterface) when l2-service is enabled.

- The command is available for bundle.sub-interface (bundle-<bundle id>.subinterface) when l2-service is enabled.

- The command is not available for loopback interfaces.

- vlan-tags and vlan-id and untagged are all mutually exclusive.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# l2-service enabled
    dnRouter(cfg-if-bundle-1.1)# untagged

    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge10-1/1/1.100
    dnRouter(cfg-if-ge10-1/1/1.100)# l2-service enabled
    dnRouter(cfg-if-ge10-1/1/1.100)# untagged


**Removing Configuration**

To remove the untagged configuration:
::

    dnRouter(cfg-if)# no untagged

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.3    | Command introduced |
+---------+--------------------+

---

## interfaces urpf admin-state.rst

interfaces urpf admin-state
---------------------------

**Minimum user role:** operator

To enable/disable uRPF for incoming packets on a specific interface. When enabled, uRPF validation will apply to both IPv4 and IPv6 unicast packets:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces urpf

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - IRB

**Parameter table**

+-------------+---------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                   | Range        | Default  |
+=============+===============================================================+==============+==========+
| admin-state | Set the administrative state of the uRPF for incoming packets | | enabled    | disabled |
|             |                                                               | | disabled   |          |
+-------------+---------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# urpf
    dnRouter(cfg-if-bundle-1-urpf)# admin-state enabled


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1-urpf)# no admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 13.0    | Command introduced |
+---------+--------------------+

---

## interfaces urpf allow-default.rst

interfaces urpf allow-default
-----------------------------

**Minimum user role:** operator

Set whether to allow a match on default route for uRPF validity check. When disabled, the default route is excluded from the uRPF validity check. If the source IP forwarding table lookup results in a match upon default route, the packet will be dropped by uRPF. When enabled, the default route is included in the uRPF validity check.

To enable/disable uRPF for the default route:

**Command syntax: allow-default [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces urpf

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - IRB

- allow-default configuration must be identical for all urpf-enabled interfaces.

- In uRPF loose mode - the default route can point to any interface.

- If the Source IP matches to next-hop null0, the packet will be dropped.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                                      | Range        | Default  |
+=============+==================================================================================+==============+==========+
| admin-state | Set the administrative state of the uRPF validity check for default route        | | enabled    | disabled |
|             | matching.                                                                        | | disabled   |          |
+-------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# urpf
    dnRouter(cfg-if-bundle-1-urpf)# allow-default enabled


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1-urpf)# no allow-default

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 13.0    | Command introduced |
+---------+--------------------+

---

## interfaces urpf mode.rst

interfaces urpf mode
--------------------

**Minimum user role:** operator

Set the uRPF operation mode. When set, uRPF validation applies to both IPV4 and IPv6 unicast packets:

**Command syntax: mode [mode]**

**Command mode:** config

**Hierarchies**

- interfaces urpf

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - IRB

- A forwarding table entry that results in a discard action (RTBH) will be ignored for uRPF validity check. That is, IP packet received with a Source IP that is resolved to a route with next-hop null0 will be dropped by the uRPF validity check.

**Parameter table**

+-----------+-------------------------------------------------------------------------------+-------+---------+
| Parameter | Description                                                                   | Range | Default |
+===========+===============================================================================+=======+=========+
| mode      | A match in the forwarding table is sufficient to pass the uRPF validity check | loose | loose   |
+-----------+-------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# urpf
    dnRouter(cfg-if-bundle-1-urpf)# mode loose


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1-urpf)# no mode

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 13.0    | Command introduced |
+---------+--------------------+

---

## interfaces urpf.rst

interfaces urpf
---------------

**Minimum user role:** operator

Unicast Reverse Path Forwarding (uRPF) is a security mechanism that validates the source of a received IP packet. The uRPF validation aims to block any malicious flow that can be identified as a spoofed IP packet or invalid source IP.

Whenever an IP packet is received on a uRPF enabled interface, the packet source IP will be checked against the forwarding table to verify there is a matching entry in the routing table for the source IP address. If it doesn’t match, the packet will be discarded.

uRPF works in loose mode, where a match in the forwarding table is sufficient to pass the uRPF validity check (in the event of a match of the source IP on-route-to-black-hole, the packet will fail the validity check).

To enter uRPF configuration level on an interface:

**Command syntax: urpf**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - IRB

- You can view the uRPF using the show interfaces detail command. See "show interfaces detail".

- To view uRPF counters, use the show interfaces counters command. See "show interfaces counters".

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# urpf
    dnRouter(cfg-if-bundle-1-urpf)#


**Removing Configuration**

To revert all urpf settings to their default values:
::

    dnRouter(cfg-if-bundle-1)# no urpf

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1     | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Changed syntax from interface to interfaces, applied new hierarchy |
+---------+--------------------------------------------------------------------+
| 9.0     | Not supported in this version                                      |
+---------+--------------------------------------------------------------------+
| 13.0    | Command re-introduced                                              |
+---------+--------------------------------------------------------------------+

---

## interfaces util-rate-threshold.rst

interfaces util-rate-threshold
------------------------------

**Minimum user role:** operator

To configure the interface bandwidth utilization rate threshold:

**Command syntax: util-rate-threshold [util-rate-threshold]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to physical interfaces.
- Set threshold is applicable to both input and output directions independently.

**Parameter table**

+---------------------+-------------+-------+---------+
| Parameter           | Description | Range | Default |
+=====================+=============+=======+=========+
| util-rate-threshold | percentage  | 0-100 | 100     |
+---------------------+-------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# util-rate-threshold 90


**Removing Configuration**

To set interface utilization threshold rate to default:
::

    dnRouter(cfg-if-ge400-0/0/0)# no util-rate-threshold

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.1    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-id list.rst

interfaces vlan-id list
-----------------------

**Minimum user role:** operator

VLANs are mandatory on sub-interfaces and virtual-l2-interfaces. Therefore, you can only change the VLAN on existing interfaces, but not remove them altogether.

**Command syntax: vlan-id list [vlan-id-list]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is available for sub-interface (geX-<f>/<n>/<p>.subinterface) and is mandatory.

- The command is available for bundle.sub-interface (bundle-<bundle id>.subinterface) and is mandatory.

- The command is not available for loopback interfaces.

- vlan-tags and vlan-id are mutually exclusive.

- VLAN lists and ranges are only applicable for L2-service enabled sub-interfaces.

- Sub-interfaces with VLAN lists do not require a TPID. By default the VLAN translation action is to preserve incoming packet's VLAN headers. Locally generated traffic will be sent as untagged.

**Parameter table**

+--------------+----------------------------------------------------------------------------------+--------+---------+
| Parameter    | Description                                                                      | Range  | Default |
+==============+==================================================================================+========+=========+
| vlan-id-list | The list of VLAN IDs to assign to the sub-interface (can be specified as         | 1-4094 | \-      |
|              | specific values and ranges, separated by commas). The VLAN IDs do not need to    |        |         |
|              | match the sub-interface ID.                                                      |        |         |
+--------------+----------------------------------------------------------------------------------+--------+---------+

**Example**
::

    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-2.300
    dnRouter(cfg-if-bundle-2.300)# vlan-id list 300
    dnRouter(cfg-if-bundle-2.300)# vlan-id list 350, 360, 400-410, 510-520


**Removing Configuration**

To remove the sub-interface configuration:
::

    dnRouter(cfg-if)# no bundle-1.1

::

    dnRouter(cfg-if)# no bundle-1.200

::

    dnRouter(cfg-if)# no ge10-1/1/1.100

To remove specific VLAN ID from the list:
::

    dnRouter(cfg-if-ge100-0/0/0.2)# no vlan-id list 100

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.1    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-id.rst

interfaces vlan-id
------------------

**Minimum user role:** operator

VLANs are mandatory on sub-interfaces and virtual-l2-interfaces. Therefore, you can only change the VLAN on existing ones, but not remove them altogether.

**Command syntax: vlan-id [vlan-id]** tpid [tpid]

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is available for sub-interface (geX-<f>/<n>/<p>.subinterface) and is mandatory.

- The command is available for bundle.sub-interface (bundle-<bundle id>.subinterface) and is mandatory.

- The command is not available for loopback interfaces.

- vlan-tags and vlan-id are mutually exclusive.

- VLAN lists and ranges are only applicable for L2-service enabled sub-interfaces

**Parameter table**

+-----------+----------------------------------------------------------------------------------+------------+---------+
| Parameter | Description                                                                      | Range      | Default |
+===========+==================================================================================+============+=========+
| vlan-id   | The VLAN ID to assign to the sub-interface. The VLAN ID does not need to match   | 1-4094     | \-      |
|           | the sub-interface ID.                                                            |            |         |
+-----------+----------------------------------------------------------------------------------+------------+---------+
| tpid      | The TPID to identify the protocol type of the VLAN tag.                          | | 0x8100   | 0x8100  |
|           |                                                                                  | | 0x9100   |         |
|           |                                                                                  | | 0x9200   |         |
+-----------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-id 20

    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.200
    dnRouter(cfg-if-bundle-1.200)# vlan-id 200

    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge10-1/1/1.100
    dnRouter(cfg-if-ge10-1/1/1.100)# vlan-id 301 tpid 0x9100



**Removing Configuration**

To remove the sub-interface configuration:
::

    dnRouter(cfg-if)# no bundle-1.1

::

    dnRouter(cfg-if)# no bundle-1.200

::

    dnRouter(cfg-if)# no ge10-1/1/1.100

**Command History**

+----------+--------------------------------------------------------------------+
| Release  | Modification                                                       |
+==========+====================================================================+
| 5.1      | Command introduced                                                 |
+----------+--------------------------------------------------------------------+
| 6.0      | Changed syntax from interface to interfaces; applied new hierarchy |
+----------+--------------------------------------------------------------------+
| 17.1     | Added support for a configurable TPID                              |
+----------+--------------------------------------------------------------------+
| 18.0.11  | Added support for virtual L2 interfaces (nat, ipsec)               |
+----------+--------------------------------------------------------------------+
| 25.2     | Removed support for virtual L2 interfaces                          |
+----------+--------------------------------------------------------------------+

---

## interfaces vlan-manipulation egress-mapping pop-pop.rst

interfaces vlan-manipulation egress-mapping action pop-pop
----------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation egress mapping for a pop-pop action:

**Command syntax: vlan-manipulation egress-mapping action pop-pop**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

- The PCP policy is determined according to the QoS policy configuration.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation egress-mapping action pop-pop


**Removing Configuration**

To remove VLAN manipulation egress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation egress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-manipulation egress-mapping pop-swap.rst

interfaces vlan-manipulation egress-mapping action pop-swap outer-tag outer-tpid
--------------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation egress mapping for a pop-swap action:

**Command syntax: vlan-manipulation egress-mapping action pop-swap outer-tag [vlan-id-outer] outer-tpid [tpid-outer]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

- The PCP policy is determined according to the QoS policy configuration.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'POP' then a    |            |         |
|               | VLAN identifier is removed from the stack but the value of this leaf is used     |            |         |
|               | instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' |            |         |
|               | or 'SWAP'. The outer VLAN identifier is also applicable to single tagged         |            |         |
|               | actions.                                                                         |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation egress-mapping action pop-swap outer-tag 200 outer-tpid 0x9100


**Removing Configuration**

To remove VLAN manipulation egress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation egress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+------------------------------+
| Release | Modification                 |
+=========+==============================+
| 18.2    | Command introduced           |
+---------+------------------------------+
| 19.1    | Removed PCP policy parameter |
+---------+------------------------------+

---

## interfaces vlan-manipulation egress-mapping pop.rst

interfaces vlan-manipulation egress-mapping action pop
------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation egress mapping for a pop action:

**Command syntax: vlan-manipulation egress-mapping action pop**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

- The PCP policy is determined according to the QoS policy configuration.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation egress-mapping action pop


**Removing Configuration**

To remove VLAN manipulation egress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation egress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-manipulation egress-mapping preserve-preserve.rst

interfaces vlan-manipulation egress-mapping action preserve-preserve
--------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation egress mapping for the preserve-preserve action:

**Command syntax: vlan-manipulation egress-mapping action preserve-preserve**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type

- The PCP policy is determined according to the QoS policy configuration.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation egress-mapping action preserve-preserve


**Removing Configuration**

To remove VLAN manipulation egress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation egress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+------------------------------+
| Release | Modification                 |
+=========+==============================+
| 18.3    | Command introduced           |
+---------+------------------------------+
| 19.1    | Removed PCP policy parameter |
+---------+------------------------------+

---

## interfaces vlan-manipulation egress-mapping preserve-swap.rst

interfaces vlan-manipulation egress-mapping action preserve-swap inner-tag inner-tpid
-------------------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation egress mapping for a preserve-swap action:

**Command syntax: vlan-manipulation egress-mapping action preserve-swap inner-tag [vlan-id-inner] inner-tpid [tpid-inner]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

- The PCP policy is determined according to the QoS policy configuration.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-inner | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'POP' then a    |            |         |
|               | VLAN identifier is removed from the stack but the value of this leaf is used     |            |         |
|               | instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' |            |         |
|               | or 'SWAP'.                                                                       |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-inner    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack.          | | 0x9100   |         |
|               |                                                                                  | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation egress-mapping action preserve-swap inner-tag 200 inner-tpid 0x9100


**Removing Configuration**

To remove VLAN manipulation egress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation egress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+------------------------------+
| Release | Modification                 |
+=========+==============================+
| 18.2    | Command introduced           |
+---------+------------------------------+
| 19.1    | Removed PCP policy parameter |
+---------+------------------------------+

---

## interfaces vlan-manipulation egress-mapping push-push.rst

interfaces vlan-manipulation egress-mapping action push-push outer-tag outer-tpid inner-tag inner-tpid
------------------------------------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation egress mapping for a push action:

**Command syntax: vlan-manipulation egress-mapping action push-push outer-tag [vlan-id-outer] outer-tpid [tpid-outer] inner-tag [vlan-id-inner] inner-tpid [tpid-inner]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

- The PCP policy is determined according to the QoS policy configuration.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'POP' then a    |            |         |
|               | VLAN identifier is removed from the stack but the value of this leaf is used     |            |         |
|               | instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' |            |         |
|               | or 'SWAP'. The outer VLAN identifier is also applicable to single tagged         |            |         |
|               | actions.                                                                         |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| vlan-id-inner | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'POP' then a    |            |         |
|               | VLAN identifier is removed from the stack but the value of this leaf is used     |            |         |
|               | instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' |            |         |
|               | or 'SWAP'.                                                                       |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-inner    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack.          | | 0x9100   |         |
|               |                                                                                  | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation egress-mapping action push-push outer-tag 100 outer-tpid 0x8100 inner-tag 200 outer-tpid 0x9100


**Removing Configuration**

To remove VLAN manipulation egress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation egress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+------------------------------+
| Release | Modification                 |
+=========+==============================+
| 18.2    | Command introduced           |
+---------+------------------------------+
| 19.1    | Removed PCP policy parameter |
+---------+------------------------------+

---

## interfaces vlan-manipulation egress-mapping push.rst

interfaces vlan-manipulation egress-mapping action push outer-tag outer-tpid
----------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation egress mapping for a push action:

**Command syntax: vlan-manipulation egress-mapping action push outer-tag [vlan-id-outer] outer-tpid [tpid-outer]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

- The PCP policy is determined according to the QoS policy configuration.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'POP' then a    |            |         |
|               | VLAN identifier is removed from the stack but the value of this leaf is used     |            |         |
|               | instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' |            |         |
|               | or 'SWAP'. The outer VLAN identifier is also applicable to single tagged         |            |         |
|               | actions.                                                                         |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation egress-mapping action push outer-tag 100 outer-tpid 0x8100


**Removing Configuration**

To remove VLAN manipulation egress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation egress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+------------------------------+
| Release | Modification                 |
+=========+==============================+
| 18.2    | Command introduced           |
+---------+------------------------------+
| 19.1    | Removed PCP policy parameter |
+---------+------------------------------+

---

## interfaces vlan-manipulation egress-mapping swap-push.rst

interfaces vlan-manipulation egress-mapping action swap-push outer-tag outer-tpid inner-tag inner-tpid
------------------------------------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation egress mapping for a swap-push action:

**Command syntax: vlan-manipulation egress-mapping action swap-push outer-tag [vlan-id-outer] outer-tpid [tpid-outer] inner-tag [vlan-id-inner] inner-tpid [tpid-inner]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

- The PCP policy is determined according to the QoS policy configuration.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'POP' then a    |            |         |
|               | VLAN identifier is removed from the stack but the value of this leaf is used     |            |         |
|               | instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' |            |         |
|               | or 'SWAP'. The outer VLAN identifier is also applicable to single tagged         |            |         |
|               | actions.                                                                         |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| vlan-id-inner | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'POP' then a    |            |         |
|               | VLAN identifier is removed from the stack but the value of this leaf is used     |            |         |
|               | instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' |            |         |
|               | or 'SWAP'.                                                                       |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-inner    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack.          | | 0x9100   |         |
|               |                                                                                  | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation egress-mapping action swap-push outer-tag 100 outer-tpid 0x88a8 inner-tag 200 inner-tpid 0x8100


**Removing Configuration**

To remove VLAN manipulation egress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation egress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+------------------------------+
| Release | Modification                 |
+=========+==============================+
| 18.2    | Command introduced           |
+---------+------------------------------+
| 19.1    | Removed PCP policy parameter |
+---------+------------------------------+

---

## interfaces vlan-manipulation egress-mapping swap-swap.rst

interfaces vlan-manipulation egress-mapping action swap-swap outer-tag outer-tpid inner-tag inner-tpid
------------------------------------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation egress mapping for a swap-swap action:

**Command syntax: vlan-manipulation egress-mapping action swap-swap outer-tag [vlan-id-outer] outer-tpid [tpid-outer] inner-tag [vlan-id-inner] inner-tpid [tpid-inner]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

- The PCP policy is determined according to the QoS policy configuration.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'POP' then a    |            |         |
|               | VLAN identifier is removed from the stack but the value of this leaf is used     |            |         |
|               | instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' |            |         |
|               | or 'SWAP'. The outer VLAN identifier is also applicable to single tagged         |            |         |
|               | actions.                                                                         |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| vlan-id-inner | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'POP' then a    |            |         |
|               | VLAN identifier is removed from the stack but the value of this leaf is used     |            |         |
|               | instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' |            |         |
|               | or 'SWAP'.                                                                       |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-inner    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack.          | | 0x9100   |         |
|               |                                                                                  | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation egress-mapping action swap-swap outer-tag 100 outer-tpid 0x88a8 inner-tag 200 inner-tpid 0x8100


**Removing Configuration**

To remove VLAN manipulation egress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation egress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+------------------------------+
| Release | Modification                 |
+=========+==============================+
| 18.2    | Command introduced           |
+---------+------------------------------+
| 19.1    | Removed PCP policy parameter |
+---------+------------------------------+

---

## interfaces vlan-manipulation egress-mapping swap.rst

interfaces vlan-manipulation egress-mapping action swap outer-tag outer-tpid
----------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation egress mapping for a swap action:

**Command syntax: vlan-manipulation egress-mapping action swap outer-tag [vlan-id-outer] outer-tpid [tpid-outer]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

- The PCP policy is determined according to the QoS policy configuration.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'POP' then a    |            |         |
|               | VLAN identifier is removed from the stack but the value of this leaf is used     |            |         |
|               | instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' |            |         |
|               | or 'SWAP'. The outer VLAN identifier is also applicable to single tagged         |            |         |
|               | actions.                                                                         |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation egress-mapping action swap outer-tag 100 outer-tpid 0x8100


**Removing Configuration**

To remove VLAN manipulation egress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation egress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+------------------------------+
| Release | Modification                 |
+=========+==============================+
| 18.2    | Command introduced           |
+---------+------------------------------+
| 19.1    | Removed PCP policy parameter |
+---------+------------------------------+

---

## interfaces vlan-manipulation ingress-mapping pop-pop.rst

interfaces vlan-manipulation ingress-mapping action pop-pop
-----------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation ingress mapping for a pop-pop action:

**Command syntax: vlan-manipulation ingress-mapping action pop-pop**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation ingress-mapping action pop-pop


**Removing Configuration**

To remove VLAN manipulation ingress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation ingress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-manipulation ingress-mapping pop-swap.rst

interfaces vlan-manipulation ingress-mapping action pop-swap outer-tag outer-tpid
---------------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation ingress mapping for a pop-swap action:

**Command syntax: vlan-manipulation ingress-mapping action pop-swap outer-tag [vlan-id-outer] outer-tpid [tpid-outer]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'PUSH' then     |            |         |
|               | this VLAN identifier is added to the stack. This value must be non-zero if the   |            |         |
|               | 'vlan-stack-action' is one of 'PUSH' or 'SWAP'. The outer VLAN identifier is     |            |         |
|               | also applicable to single tagged actions.                                        |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation ingress-mapping action pop-swap outer-tag 200 outer-tpid 0x9100


**Removing Configuration**

To remove VLAN manipulation ingress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation ingress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-manipulation ingress-mapping pop.rst

interfaces vlan-manipulation ingress-mapping action pop
-------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation ingress mapping for a pop action:

**Command syntax: vlan-manipulation ingress-mapping action pop**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation ingress-mapping action pop


**Removing Configuration**

To remove VLAN manipulation ingress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation ingress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-manipulation ingress-mapping preserve-preserve.rst

interfaces vlan-manipulation ingress-mapping action preserve-preserve
---------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation ingress mapping for the preserve-preserve action:

**Command syntax: vlan-manipulation ingress-mapping action preserve-preserve**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation ingress-mapping action preserve-preserve


**Removing Configuration**

To remove VLAN manipulation ingress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation ingress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.1    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-manipulation ingress-mapping preserve-swap.rst

interfaces vlan-manipulation ingress-mapping action preserve-swap outer-tpid inner-tag inner-tpid
-------------------------------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation ingress mapping for a preserve-swap action:

**Command syntax: vlan-manipulation ingress-mapping action preserve-swap outer-tpid [tpid-outer] inner-tag [vlan-id-inner] inner-tpid [tpid-inner]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| vlan-id-inner | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'PUSH' then     |            |         |
|               | this VLAN identifier is added to the stack. This value must be non-zero if the   |            |         |
|               | 'vlan-stack-action' is one of 'PUSH' or 'SWAP'.                                  |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-inner    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack.          | | 0x9100   |         |
|               |                                                                                  | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation ingress-mapping action preserve-swap outer-tpid 0x8100 inner-tag 200 inner-tpid 0x9100


**Removing Configuration**

To remove VLAN manipulation ingress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation ingress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-manipulation ingress-mapping push-push.rst

interfaces vlan-manipulation ingress-mapping action push-push outer-tag outer-tpid inner-tag inner-tpid
-------------------------------------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation ingress mapping for a push action:

**Command syntax: vlan-manipulation ingress-mapping action push-push outer-tag [vlan-id-outer] outer-tpid [tpid-outer] inner-tag [vlan-id-inner] inner-tpid [tpid-inner]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'PUSH' then     |            |         |
|               | this VLAN identifier is added to the stack. This value must be non-zero if the   |            |         |
|               | 'vlan-stack-action' is one of 'PUSH' or 'SWAP'. The outer VLAN identifier is     |            |         |
|               | also applicable to single tagged actions.                                        |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| vlan-id-inner | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'PUSH' then     |            |         |
|               | this VLAN identifier is added to the stack. This value must be non-zero if the   |            |         |
|               | 'vlan-stack-action' is one of 'PUSH' or 'SWAP'.                                  |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-inner    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack.          | | 0x9100   |         |
|               |                                                                                  | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation ingress-mapping action push outer-tag 100 outer-tpid 0x8100 inner-tag 100 inner-tpid 0x9100


**Removing Configuration**

To remove VLAN manipulation ingress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation ingress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-manipulation ingress-mapping push.rst

interfaces vlan-manipulation ingress-mapping action push outer-tag outer-tpid
-----------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation ingress mapping for a push action:

**Command syntax: vlan-manipulation ingress-mapping action push outer-tag [vlan-id-outer] outer-tpid [tpid-outer]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'PUSH' then     |            |         |
|               | this VLAN identifier is added to the stack. This value must be non-zero if the   |            |         |
|               | 'vlan-stack-action' is one of 'PUSH' or 'SWAP'. The outer VLAN identifier is     |            |         |
|               | also applicable to single tagged actions.                                        |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation ingress-mapping action push outer-tag 100 outer-tpid 0x8100


**Removing Configuration**

To remove VLAN manipulation ingress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation ingress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-manipulation ingress-mapping swap-push.rst

interfaces vlan-manipulation ingress-mapping action swap-push outer-tag outer-tpid inner-tag inner-tpid
-------------------------------------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation ingress mapping for a swap-push action:

**Command syntax: vlan-manipulation ingress-mapping action swap-push outer-tag [vlan-id-outer] outer-tpid [tpid-outer] inner-tag [vlan-id-inner] inner-tpid [tpid-inner]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'PUSH' then     |            |         |
|               | this VLAN identifier is added to the stack. This value must be non-zero if the   |            |         |
|               | 'vlan-stack-action' is one of 'PUSH' or 'SWAP'. The outer VLAN identifier is     |            |         |
|               | also applicable to single tagged actions.                                        |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| vlan-id-inner | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'PUSH' then     |            |         |
|               | this VLAN identifier is added to the stack. This value must be non-zero if the   |            |         |
|               | 'vlan-stack-action' is one of 'PUSH' or 'SWAP'.                                  |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-inner    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack.          | | 0x9100   |         |
|               |                                                                                  | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation ingress-mapping action swap-push outer-tag 100 outer-tpid 0x88a8 inner-tag 200 inner-tpid 0x8100


**Removing Configuration**

To remove VLAN manipulation ingress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation ingress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-manipulation ingress-mapping swap-swap.rst

interfaces vlan-manipulation ingress-mapping action swap-swap outer-tag outer-tpid inner-tag inner-tpid
-------------------------------------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation ingress mapping for a swap-swap action:

**Command syntax: vlan-manipulation ingress-mapping action swap-swap outer-tag [vlan-id-outer] outer-tpid [tpid-outer] inner-tag [vlan-id-inner] inner-tpid [tpid-inner]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'PUSH' then     |            |         |
|               | this VLAN identifier is added to the stack. This value must be non-zero if the   |            |         |
|               | 'vlan-stack-action' is one of 'PUSH' or 'SWAP'. The outer VLAN identifier is     |            |         |
|               | also applicable to single tagged actions.                                        |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| vlan-id-inner | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'PUSH' then     |            |         |
|               | this VLAN identifier is added to the stack. This value must be non-zero if the   |            |         |
|               | 'vlan-stack-action' is one of 'PUSH' or 'SWAP'.                                  |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-inner    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack.          | | 0x9100   |         |
|               |                                                                                  | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation ingress-mapping action swap-swap outer-tag 100 outer-tpid 0x88a8 inner-tag 200 inner-tpid 0x8100


**Removing Configuration**

To remove VLAN manipulation ingress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation ingress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-manipulation ingress-mapping swap.rst

interfaces vlan-manipulation ingress-mapping action swap outer-tag outer-tpid
-----------------------------------------------------------------------------

**Minimum user role:** operator

To configure the VLAN manipulation ingress mapping for a swap action:

**Command syntax: vlan-manipulation ingress-mapping action swap outer-tag [vlan-id-outer] outer-tpid [tpid-outer]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is supported for L2 inband network interfaces (single-tagged, double-tagged, port-mode) attached to any L2 service type.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| vlan-id-outer | Optionally specifies a fixed VLAN identifier that is used by the action          | 1-4094     | \-      |
|               | configured in 'vlan-stack-action'. For example, if the action is 'PUSH' then     |            |         |
|               | this VLAN identifier is added to the stack. This value must be non-zero if the   |            |         |
|               | 'vlan-stack-action' is one of 'PUSH' or 'SWAP'. The outer VLAN identifier is     |            |         |
|               | also applicable to single tagged actions.                                        |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid-outer    | Optionally override the tag protocol identifier field (TPID) that is used by the | | 0x8100   | \-      |
|               | action configured by 'vlan-stack-action' when modifying the VLAN stack. The      | | 0x9100   |         |
|               | outer TPID is also applicable to single tagged actions.                          | | 0x9200   |         |
|               |                                                                                  | | 0x88a8   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.1
    dnRouter(cfg-if-bundle-1.1)# vlan-manipulation ingress-mapping action swap outer-tag 100 outer-tpid 0x8100


**Removing Configuration**

To remove VLAN manipulation ingress mapping configuration:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation ingress-mapping

To remove VLAN manipulation configuration altogether:
::

    dnRouter(cfg-if-ge100-1/1/1.100)# no vlan-manipulation

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-tags inner-tag-list.rst

interfaces vlan-tags outer-tag inner-tag-list
---------------------------------------------

**Minimum user role:** operator

To configure a sub-interface with QinQ encapsulation (802.1ad double-tagged VLAN) with a list of inner VLAN tags:

**Command syntax: vlan-tags outer-tag [outer-vlan-id] inner-tag-list [inner-vlan-id-list]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The vlan-tags command is available only for sub-interface/bundle.sub-interface.

- The vlan-tags command is not available for physical/loopback interfaces.

- Vlan-tags is a must parameter for a QinQ sub-interface.

- Vlan-tags and vlan-id commands are mutually exclusive.

- A sub-interface is created when using the interface.sub-interface-id syntax.

- Vlan-tags command configures the sub-interface with QinQ encapsulation.

- To preserve the sub-interface properties, it is possible to change its type from QinQ to VLAN without removing the sub-interface configuration.

- VLAN lists and ranges are only applicable for L2-service enabled sub-interfaces.

- Sub-interfaces with VLAN lists do not require TPID. By default VLAN translation action is to preserve incoming packet's VLAN headers. Locally generated traffic will be sent as untagged.

**Parameter table**

+--------------------+----------------------------------------------------------------------------------+--------+---------+
| Parameter          | Description                                                                      | Range  | Default |
+====================+==================================================================================+========+=========+
| outer-vlan-id      | The outer VLAN ID to assign to the sub-interface. The VLAN ID does not need to   | 1-4094 | \-      |
|                    | match the sub-interface ID.                                                      |        |         |
+--------------------+----------------------------------------------------------------------------------+--------+---------+
| inner-vlan-id-list | The list of VLAN IDs to assign to the sub-interface (can be specified as         | 1-4094 | \-      |
|                    | sepcific values and ranges, separated by commas). The VLAN IDs do not need to    |        |         |
|                    | match the sub-interface ID.                                                      |        |         |
+--------------------+----------------------------------------------------------------------------------+--------+---------+

**Example**
::

    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge10-1/1/2.100
    dnRouter(cfg-if-ge10-1/1/2.100)# vlan-tags outer-tag 100 inner-tag-list 301, 304, 305-310, 400-500


**Removing Configuration**

To remove the sub-interface configuration:
::

    dnRouter(cfg-if)# no bundle-1.2

::

    dnRouter(cfg-if)# no ge10-1/1/2.100

To remove specific VLAN tag from the inner VLAN list:
::

    dnRouter(cfg-if-ge100-0/0/0.2)# no vlan-tags outer-tag 100 inner-tag-list 301

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.1    | Command introduced |
+---------+--------------------+

---

## interfaces vlan-tags.rst

interfaces vlan-tags outer-tag inner-tag
----------------------------------------

**Minimum user role:** operator

To configure a sub-interface with QinQ encapsulation (802.1ad double-tagged VLAN):

**Command syntax: vlan-tags outer-tag [outer-vlan-id] inner-tag [inner-vlan-id]** outer-tpid [tpid]

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- Vlan-tags command is available only for sub-interface/bundle.sub-interface.

- Vlan-tags command is not available for physical/loopback interfaces.

- Vlan-tags is a must parameter for a QinQ sub-interface.

- Vlan-tags and vlan-id commands are mutually exclusive.

- Sub-interface is created when using the interface.sub-interface-id syntax.

- Vlan-tags command configures the sub-interface with QinQ encapsulation.

- To preserve sub-interface properties, it is possible to change its type from QinQ to VLAN without removing the sub-interface configuration.

- The default outer TPID value is 0x8100. Inner TPID value is always 0x8100.

**Parameter table**

+---------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter     | Description                                                                      | Range      | Default |
+===============+==================================================================================+============+=========+
| outer-vlan-id | The outer VLAN ID to assign to the sub-interface. The VLAN ID does not need to   | 1-4094     | \-      |
|               | match the sub-interface ID.                                                      |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| inner-vlan-id | The inner VLAN ID to assign to the sub-interface. The VLAN ID does not need to   | 1-4094     | \-      |
|               | match the sub-interface ID.                                                      |            |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+
| tpid          | The TPID to identify the protocol type of the outer VLAN tag.                    | | 0x8100   | 0x8100  |
|               |                                                                                  | | 0x88a8   |         |
|               |                                                                                  | | 0x9100   |         |
|               |                                                                                  | | 0x9200   |         |
+---------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.2
    dnRouter(cfg-if-bundle-1.2)# vlan-tags outer-tag 20 inner-tag 20

    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.3
    dnRouter(cfg-if-bundle-1.3)# vlan-tags outer-tag 20 inner-tag 30

    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1.4
    dnRouter(cfg-if-bundle-1.4)# vlan-tags outer-tag 20 inner-tag 40

    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge10-1/1/2.100
    dnRouter(cfg-if-ge10-1/1/2.100)# vlan-tags outer-tag 20 inner-tag 301 outer-tpid 0x8100


**Removing Configuration**

To remove the sub-interface configuration:
::

    dnRouter(cfg-if)# no bundle-1.2

::

    dnRouter(cfg-if)# no ge10-1/1/2.100

**Command History**

+---------+---------------------------------------------+
| Release | Modification                                |
+=========+=============================================+
| 16.1    | Command introduced                          |
+---------+---------------------------------------------+
| 17.1    | Added support for a configurable outer TPID |
+---------+---------------------------------------------+

---

## interfaces.rst

Interfaces
----------

The following are the types of interfaces you can provision.

+----------------------+------------------------+----------------------------------------------+----------------------+
| Interface Scheme     | Syntax Convention      | Range                                        | Example              |
+======================+========================+==============================================+======================+
| fab-<nce>X-Y/Z/W     | NCE: Node type         | NCP: fabric interface on NCP (NCP-to-NCF)    | fab-ncp400-1/0/3     |
|                      |                        | NCF: fabric interface on NCF (NCF-to-NCP)    | fab-ncf400-1/0/20    |
|                      +------------------------+----------------------------------------------+                      |
|                      | X: Interface speed     | 400 GbE                                      |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | Y: Node ID             | NCP: 0..249                                  |                      |
|                      |                        | NCF: 0..611                                  |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | Z: Slot ID             | 0                                            |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | W: Port ID             | As displayed on the hardware panel           |                      |
+----------------------+------------------------+----------------------------------------------+----------------------+
| mgmt-<nce>-X/Y       | NCE: Node type         | NCC management interface                     | mgmt-ncc-0           |
|                      |                        | NCP management interface                     | mgmt-ncp-3/0         |
|                      |                        | NCF management interface                     | mgmt-ncf-1-0         |
|                      +------------------------+----------------------------------------------+                      |
|                      | X: Node ID             | NCC: 0..1                                    |                      |
|                      |                        | NCP: 0..249                                  |                      |
|                      |                        | NCF: 0..611                                  |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | Y: Eth. port ID        | 0                                            |                      |
+----------------------+------------------------+----------------------------------------------+----------------------+
| ctrl-<nce>-X/Y       | NCE: Node type         | NCC control interface                        | ctrl-ncc-1/0         |
|                      |                        | NCP control interface                        | ctrl-ncp-3/1         |
|                      |                        | NCF control interface                        | ctrl-ncf-0/0         |
|                      |                        | NCM control interface                        | ctrl-ncm-B0/1        |
|                      +------------------------+----------------------------------------------+                      |
|                      | X: Node ID             | NCC: 0..1                                    |                      |
|                      |                        | NCP: 0..249                                  |                      |
|                      |                        | NCF: 0..611                                  |                      |
|                      |                        | NCM: A0, B0, A1, B1                          |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | Y: Eth. port ID        | 0..1                                         |                      |
+----------------------+------------------------+----------------------------------------------+----------------------+
| ipmi-<nce>-X/Y       | NCE: Node type         | NCC IPMI interface                           | ipmi-ncc-0/0         |
|                      |                        | NCP IPMI interface                           | ipmi-ncp-1/0         |
|                      |                        | NCF IPMI interface                           | ipmi-ncf-0/0         |
|                      +------------------------+----------------------------------------------+                      |
|                      | X: Node ID             | NCC: 0..1                                    |                      |
|                      |                        | NCP: 0..249                                  |                      |
|                      |                        | NCF: 0..611                                  |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | Y: Port ID             | 0                                            |                      |
+----------------------+------------------------+----------------------------------------------+----------------------+
| console-<nce>-X/Y    | NCE: Node type         | NCC console interface                        | console-ncc-0/0      |
|                      |                        | NCP console interface                        | console-ncp-2/0      |
|                      |                        | NCF console interface                        | console-ncf-0/0      |
|                      +------------------------+----------------------------------------------+                      |
|                      | X: Node ID             | NCC: 0..1                                    |                      |
|                      |                        | NCP: 0..249                                  |                      |
|                      |                        | NCF: 0..611                                  |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | Y: Port ID             | 0                                            |                      |
+----------------------+------------------------+----------------------------------------------+----------------------+
| mgmt0                | Logical out-of-band management interface                                                     |
+----------------------+------------------------+----------------------------------------------+----------------------+
| geX-f/n/p            | X: Interface speed     | 10, 25, 40, 50, 100                          | ge100-1/0/39         |
|                      +------------------------+----------------------------------------------+                      |
|                      | f: NCP ID              | 0..255                                       |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | n: Slot ID             | 0..255                                       |                      |
|                      +------------------------+----------------------------------------------+                      |
|                      | p: Port ID             | 0..255                                       |                      |
+----------------------+------------------------+----------------------------------------------+----------------------+
| bundle-x             | x: bundle-id           | 1..1023                                      | bundle-2             |
+----------------------+------------------------+----------------------------------------------+----------------------+
| .y                   | y: Sub-interface ID    | 1..65535                                     | ge100-1/0/39.2057    |
|                      |                        |                                              +----------------------+
|                      |                        |                                              | bundle-2.102         |
+----------------------+------------------------+----------------------------------------------+----------------------+
| loX                  | X: Loopback ID         | 0..65535                                     | lo0                  |
+----------------------+------------------------+----------------------------------------------+----------------------+
| gre-X                | X: GRE tunnel ID       | 0..4                                         | gre-1                |
+----------------------+------------------------+----------------------------------------------+----------------------+
| irbX                 | X: IRB ID              | 1..65535                                     | irb1                 |
+----------------------+------------------------+----------------------------------------------+----------------------+


**Physical Interfaces**
=======================

DNOS supports a highly modular range of high-speed Ethernet interfaces in a wide range of speeds, as follows.

- 1 GbE
- 10 GbE
- 25 GbE
- 100 GbE
- 400 GbE

This solution requires fewer physical interconnects, accelerating provisioning and reducing deployment and sparing costs.

**Name: ge100-<f>/<n>/<p>**

**f** - ncp id

**n** - NIC slot id

**p** - port id

The NIC id is the physical slot.

The physical interfaces of an NCP is set by system after assigning an NCP ID in the cluster.


**Bundle Interfaces**
=====================

**Name: bundle-<bundle id>**

Link aggregation (LAG) is a process of inter-connecting two devices with two or more links between them, so that multiple links are combined into one bigger virtual link that can carry a higher (combined) bandwidth. All these multiple links participating in a LAG (bundle) act as a single large (virtual) link.

Assigning a bundle-id to an interface adds the interface to an existing bundle interface. When a bundle is created, all other configurations/sub-interfaces under the physical member are removed. You should always create a bundle on both the router side and at the other end of the link.

In DNOS, the bundle interfaces in the DNOS system are providing datapath connectivity between NCPs. The bundle interfaces are the customer/core interfaces that the user is provisioning. Each bundle has a representation (member) in each of the NCPs, so that all the NCPs are able to send traffic from any ingress interface to any egress interface.

<INSERT 01_interfaces>


**Physical/Bundle vLAN Sub-interfaces**
=======================================

**Name: bundle-<id.subinterface>**
**Name: ge100-<f>/<n>/<p>.<subinterface>**

Sub-interfaces are created by subdividing the physical interface into two or more virtual interfaces on which you can assign unique Layer 3 network addresses such as IP subnets. With sub-interfaces, the IP routing protocols see the network connection to each remote networking device as a separate physical interface even though the sub-interfaces share a common physical interface.

Sub-interfaces are identified by a prefix that consists of the hardware interface descriptor or bundle interface descriptor followed by a period and then by a number that is unique for that prefix. The full sub-interface number must be unique to the cluster. For example, the first sub-interface for Ethernet interface ge100-1/2/1 might be named ge100-1/2/1.100 where .100 indicates the sub-interface.

**GRE-tunnel Interfaces**
=========================

**Name: gre-tunnel-<id>**

Generic Routing Encapsulation (GRE) is a tunneling mechanism that encapsulates packets of any protocol inside IP packets delivered to a destination endpoint. The GRE tunnel behaves as a virtual point-to-point connection between the two endpoints (identified as tunnel source and tunnel destination).

In DNOS, the GRE interfaces provide a control plane interface in order to establish IS-IS adjacency with a remote neighbor over a connected interface.
The GRE interfaces are not used to solve routes.

**IRB Interfaces**
=========================

**Name: irb<id>**

Integrated Routing and Bridging (IRB) interfaces are interfaces that can be associated with a single layer 2 bridge domain and a layer 3 VRF. The IRB interface acts as a gateway for the bridge domain and allows inter connectivity between bridge domains or routing domains.

**Interface Command List**
==========================

The following table displays the interface commands and the interfaces types to which they apply.

+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| Command               | Bundle | Bundle vlan | Physical | Physical VLAN | lo | Bundle member | Mgmt0 | Mgmt-ncc-X/0 | Console-ncc-X/0 | IPMI | ctrl-ncX-0/0 | fab-ncX-0/0 | GRE tunnel  | IRB |
+=======================+========+=============+==========+===============+====+===============+=======+==============+=================+======+==============+=============+=============+=====+
| admin-state           | -      | -           | -        | -             | -  | -             | -     | -            | -               | -    | -            | -           |             | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| mtu                   | -      | -           | -        | -             |    |               | -     |              |                 |      |              |             | -           | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| ipv4-address          | -      | -           | -        | -             | -  |               | -     | -            |                 |      |              |             | -           | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| ipv6-address          | -      | -           | -        | -             | -  |               | -     | -            |                 |      |              |             |             | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| description           | -      | -           | -        | -             | -  | -             |       | -            |                 |      | -            |             | -           | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| mac-address           | -      |             | -        |               |    |               |       | -            |                 |      |              |             |             | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| mpls                  | -      | -           | -        | -             |    |               |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| urpf                  | -      | -           | -        | -             |    |               |       |              |                 |      |              |             |             | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| vlan-tags             |        | -           |          | -             |    |               |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| vlan-id               |        | -           |          | -             |    |               |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| untagged              |        | -           |          | -             |    |               |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| bundle-id             |        |             | -        |               |    |               |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| access-list           | -      | -           | -        | -             |    |               | -     |              |                 |      |              |             |             | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| qos policy            | -      | -           | -        | -             |    |               |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| arp                   | -      | -           | -        | -             |    |               |       |              |                 |      |              |             |             | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| ndp                   | -      | -           | -        | -             |    |               |       |              |                 |      |              |             |             | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| carrier-delay         |        |             | -        |               |    | -             |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| port-priority         |        |             |          |               |    | -             |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| source                |        |             |          |               |    |               |       |              |                 |      |              |             | -           |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| destination           |        |             |          |               |    |               |       |              |                 |      |              |             | -           |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| flowspec              | -      | -           | -        | -             |    |               |       |              |                 |      |              |             |             | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| flow-monitoring       | -      | -           | -        | -             |    |               |       |              |                 |      |              |             |             | -   |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| l2-service            |        | -           |          | -             |    |               |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| if-dampening          |        |             | -        |               |    | -             |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| speed                 |        |             | -        |               |    |               |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| ber                   |        |             | -        |               |    |               |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| priority-flow-control |        |             | -        |               |    |               |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
| qppb                  | -      | -           | -        | -             |    |               |       |              |                 |      |              |             |             |     |
+-----------------------+--------+-------------+----------+---------------+----+---------------+-------+--------------+-----------------+------+--------------+-------------+-------------+-----+
---

## interfaces/clock/clock.rst

interfaces clock
----------------

**Minimum user role:** operator

Enter timing related configuration options and reference synchronization clock settings.

To configure timing parameters:

**Command syntax: clock**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- Notice the change in prompt.

- This command is currently applicable only to physical 400G and breakout interfaces on UfiSpace NCP3 platforms or physical 10G and 100G interfaces on UfiSpace NCPL platforms.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# clock

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 clock


**Removing Configuration**

To revert interface clock to its default value:
::

    dnRouter(cfg-if-ge400-0/0/0)# no clock

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.2    | Command introduced |
+---------+--------------------+

---

## interfaces/clock/ptp/g8275-1/admin-state.rst

interfaces clock ptp g8275-1 admin-state
----------------------------------------

**Minimum user role:** operator

Enable or disable the PTP port.

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces clock ptp g8275-1

**Parameter table**

+-------------+-------------------------------------------+--------------+----------+
| Parameter   | Description                               | Range        | Default  |
+=============+===========================================+==============+==========+
| admin-state | enable PTP port functionality or reset it | | enabled    | disabled |
|             |                                           | | disabled   |          |
+-------------+-------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# clock
    dnRouter(cfg-if-ge400-0/0/0-clk)# ptp
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp)# g8275-1
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# admin-state enabled

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 clock ptp g8275-1 admin-state enabled


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# no admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.3    | Command introduced |
+---------+--------------------+

---

## interfaces/clock/ptp/g8275-1/announce-receipt-timeout.rst

interfaces clock ptp g8275-1 announce-receipt-timeout
-----------------------------------------------------

**Minimum user role:** operator

Set the PTP per-port announce receipt timeout attribute.

**Command syntax: announce-receipt-timeout [announce-receipt-timeout]**

**Command mode:** config

**Hierarchies**

- interfaces clock ptp g8275-1

**Parameter table**

+--------------------------+-----------------------------------------+-------+---------+
| Parameter                | Description                             | Range | Default |
+==========================+=========================================+=======+=========+
| announce-receipt-timeout | PTP clock port announce-receipt-timeout | 3-10  | 3       |
+--------------------------+-----------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# clock
    dnRouter(cfg-if-ge400-0/0/0-clk)# ptp
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp)# g8275-1
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# announce-receipt-timeout 3

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 clock ptp g8275-1 announce-receipt-timeout 3


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# no announce-receipt-timeout

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.3    | Command introduced |
+---------+--------------------+

---

## interfaces/clock/ptp/g8275-1/delay.rst

interfaces clock ptp g8275-1 delay
----------------------------------

**Minimum user role:** operator

Set the PTP per-port delay attribute.

**Command syntax: delay [delay]**

**Command mode:** config

**Hierarchies**

- interfaces clock ptp g8275-1

**Parameter table**

+-----------+----------------------------------------------------------------------------------+----------------+---------+
| Parameter | Description                                                                      | Range          | Default |
+===========+==================================================================================+================+=========+
| delay     | The additional delay in nSec to compensate for asymmetrical upstream and         | -100000-100000 | 0       |
|           | downstream delays.                                                               |                |         |
+-----------+----------------------------------------------------------------------------------+----------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# clock
    dnRouter(cfg-if-ge400-0/0/0-clk)# ptp
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp)# g8275-1
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# delay 1

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 clock ptp g8275-1 delay 1


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# no delay

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.3    | Command introduced |
+---------+--------------------+

---

## interfaces/clock/ptp/g8275-1/g8275-1.rst

interfaces clock ptp g8275-1
----------------------------

**Minimum user role:** operator

Enter PTP 1588v2 G8275.1 specific interface related configuration options.

To configure ptp G8275.1 interface parameters:

**Command syntax: g8275-1**

**Command mode:** config

**Hierarchies**

- interfaces clock ptp

**Note**

- Notice the change in prompt.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# clock
    dnRouter(cfg-if-ge400-0/0/0-clk)# ptp
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp)# g8275-1
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# admin-state enabled

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 clock ptp g8275-1 admin-state enabled


**Removing Configuration**

Disable G8275.1 profile and remove its settings
::

    dnRouter(cfg-system-ncp-7-clk-ptp)# no g8275-1 

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.3    | Command introduced |
+---------+--------------------+

---

## interfaces/clock/ptp/g8275-1/local-priority.rst

interfaces clock ptp g8275-1 local-priority
-------------------------------------------

**Minimum user role:** operator

Set the PTP per-port local-priority attribute.

**Command syntax: local-priority [local-priority]**

**Command mode:** config

**Hierarchies**

- interfaces clock ptp g8275-1

**Parameter table**

+----------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter      | Description                                                                      | Range | Default |
+================+==================================================================================+=======+=========+
| local-priority | The per port local-priority attribute is used as a tie-breaker in the BMCA data  | 0-255 | 128     |
|                | set comparison algorithm, in the event that all other previous attributes of the |       |         |
|                | data sets being compared are equal. Each parent clock or foreign master clock    |       |         |
|                | data set, whose Announce information was received on the port, is appended with  |       |         |
|                | the local priority attribute of the local port before the BMCA data set          |       |         |
|                | comparison The local priority attribute is not transmitted in Announce messages. |       |         |
+----------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# clock
    dnRouter(cfg-if-ge400-0/0/0-clk)# ptp
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp)# g8275-1
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# local-priority 128

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 clock ptp g8275-1 local-priority 128


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# no local-priority

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.3    | Command introduced |
+---------+--------------------+

---

## interfaces/clock/ptp/g8275-1/master-only.rst

interfaces clock ptp g8275-1 master-only
----------------------------------------

**Minimum user role:** operator

Enable or disable PTP port in Master-only mode.

**Command syntax: master-only [master-only]**

**Command mode:** config

**Hierarchies**

- interfaces clock ptp g8275-1

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter   | Description                                                                      | Range        | Default |
+=============+==================================================================================+==============+=========+
| master-only | Set to true when the port can be used only as Master. When the port mode is set  | | enabled    | False   |
|             | to master-only, the port is never placed in the UNCALIBRATED, SLAVE or PASSIVE   | | disabled   |         |
|             | states, and will always attempt to go to the MASTER state. The port state will   |              |         |
|             | remain in PRE-MASTER state if BMC determines that it is connected to a clock     |              |         |
|             | with                                                                             |              |         |
+-------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# clock
    dnRouter(cfg-if-ge400-0/0/0-clk)# ptp
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp)# g8275-1
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# master-only enabled

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 clock ptp g8275-1 master-only enabled


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# no master-only

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.3    | Command introduced |
+---------+--------------------+

---

## interfaces/clock/ptp/g8275-1/multicast-address.rst

interfaces clock ptp g8275-1 multicast-address
----------------------------------------------

**Minimum user role:** operator

Set the PTP port destination MAC address for G.8275.1 as forwardable or non-forwardable.

**Command syntax: multicast-address [multicast-address]**

**Command mode:** config

**Hierarchies**

- interfaces clock ptp g8275-1

**Parameter table**

+-------------------+---------------------------------------+---------------------+-----------------+
| Parameter         | Description                           | Range               | Default         |
+===================+=======================================+=====================+=================+
| multicast-address | multicast address used as destination | | non-forwardable   | non-forwardable |
|                   |                                       | | forwardable       |                 |
+-------------------+---------------------------------------+---------------------+-----------------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# clock
    dnRouter(cfg-if-ge400-0/0/0-clk)# ptp
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp)# g8275-1
    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# multicast-address forwardable

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 clock ptp g8275-1 multicast-address forwardable


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-ge400-0/0/0-clk-ptp-g8275-1)# no multicast-address

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.3    | Command introduced |
+---------+--------------------+

---

## interfaces/clock/ptp/ptp.rst

interfaces clock ptp
--------------------

**Minimum user role:** operator

Enter PTP 1588v2 port specific related configuration options and reference synchronization clock settings.

To configure ptp per-port parameters:

**Command syntax: ptp**

**Command mode:** config

**Hierarchies**

- interfaces clock

**Note**

- Notice the change in prompt.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# clock
    dnRouter(cfg-if-ge400-0/0/0-clk)# ptp


**Removing Configuration**

Remove ptp port configuration from the interface:
::

    dnRouter(cfg-if-ge400-0/0/0-clk) no ptp

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.1    | Command introduced |
+---------+--------------------+

---

## interfaces/clock/synce/mode.rst

interfaces clock synce mode
---------------------------

**Minimum user role:** operator

When Sync-Ethernet timing feature is enabled, each ethernet port shall be set to either synchronous or non-synchronous.

**Command syntax: mode [mode]**

**Command mode:** config

**Hierarchies**

- interfaces clock synce

**Note**

- This command is currently applicable only to physical 400G and breakout interfaces on UfiSpace NCP3 platforms or physical 10G and 100G interfaces on ufiSpace NCPL platforms.

**Parameter table**

+-----------+---------------------------------------------+---------------------+-----------------+
| Parameter | Description                                 | Range               | Default         |
+===========+=============================================+=====================+=================+
| mode      | The interface sync-ethernet operating mode. | | synchronous       | non-synchronous |
|           |                                             | | non-synchronous   |                 |
+-----------+---------------------------------------------+---------------------+-----------------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# clock
    dnRouter(cfg-if-ge400-0/0/0-clk)# synce
    dnRouter(cfg-if-ge400-0/0/0-clk-synce)# mode synchronous

    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 clock synce mode non-synchronous


**Removing Configuration**

To set interface synce mode to default:
::

    dnRouter(cfg-if-ge400-0/0/0-clk-synce)# no mode

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.2    | Command introduced |
+---------+--------------------+

---

## interfaces/clock/synce/synce.rst

interfaces clock synce
----------------------

**Minimum user role:** operator

Enter interface level Synchronous-Ethernet related configuration options and settings.

**Command syntax: synce**

**Command mode:** config

**Hierarchies**

- interfaces clock

**Note**

- Notice the change in prompt.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-0/0/0
    dnRouter(cfg-if-ge400-0/0/0)# clock
    dnRouter(cfg-if-ge400-0/0/0-clk)# synce
    dnRouter# configure
    dnRouter(cfg)# interfaces ge400-0/0/0 clock synce


**Removing Configuration**

To revert the interface sync-ethernet to its default value:
::

    dnRouter(cfg-if-ge400-0/0/0-clk)# no synce

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.2    | Command introduced |
+---------+--------------------+

---

