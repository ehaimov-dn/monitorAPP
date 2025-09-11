# Clear Commands Complete Aggregation

This file contains the complete content from all RST files in the Clear Commands folder.

Total files: 118

---

## clear commands overview.rst

Clear Commands Overview
-----------------------
The clear command removes information from the system's database. The following clear commands are available:

+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| Command                                      | Description                                                                                         | Reference                                        |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear access-lists counters                  | Clear access-list counter information                                                               | clear access-list counters                       |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear arp                                    | Clear entries from the ARP table                                                                    | clear arp                                        |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear bfd sessions                           | Restart BFD session                                                                                 | clear bfd session                                |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear bfd statistics                         | Clear BFD session statistics to reset session counters                                              | clear bfd statistics                             |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear bgp dampening                          | Clear BGP route flap dampening information                                                          | clear bgp dampening                              |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear bgp neighbor                           | Clear BGP neighbors                                                                                 | clear bgp neighbor                               |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear bgp neighbor link-state                | Clear link states received from BGP neighbor                                                        | clear bgp neighbor link-state                    |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear bgp prefix filter                      | Push out prefix-list ORF and do inbound soft reconfigure                                            | clear bgp prefix filter                          |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear bgp redistribute                       | Re-evaluate all redistributed routes                                                                | clear bgp redistribute                           |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear cli history                            | Clear history of CLI commands entered during the session                                            | clear cli history                                |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear cprl counters                          | Clear Control Plane Rate Limiting counters                                                          | clear system cprl counters                       |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear flow-monitoring cache                  | Clear the NCPs' flow-monitoring cache                                                               | clear services flow-monitoring cache             |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear flow-monitoring cache counters         | Clear the NCPs' flow-monitoring cache counters                                                      | clear services flow-monitoring cache counters    |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear flow-monitoring exporter counters      | Clear the NCPs' flow-monitoring exporter counters                                                   | clear services flow-monitoring exporter counters |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear grpc session                           | Kills active gRPC sessions                                                                          | clear grpc session                               |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear grpc session history                   | Clears the list of terminated gRPC sessions                                                         | clear grpc sessions history                      |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear interfaces control counters            | Clear counter information from control interface                                                    | clear interfaces control counters                |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear interfaces counters                    | Clear interface counters information                                                                | clear interfaces counters                        |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear interfaces dampening                   | Clear interfaces dampening penalty value to zero                                                    | clear interfaces dampening penalty               |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear interfaces fabric counters             | Clear counter information from fabric interface                                                     | clear interfaces fabric counters                 |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear isis neighbor                          | Reset IS-IS adjacencies (all, per IS-IS instance, or per system-id)                                 | clear isis neighbor                              |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear isis process                           | Clear the IS-IS database and reset IS-IS adjacencies                                                | clear isis process                               |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear isis routes                            | Clear IS-IS routes                                                                                  | clear isis routes                                |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear isis statistics                        | Clear IS-IS statistics                                                                              | clear isis statistics                            |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear lacp counters                          | Clear LACP interface counters                                                                       | clear lacp counters                              |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear ldp neighbor                           | Clear LDP neighbors                                                                                 | clear ldp neighbor                               |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear lfs counters                           | Clear link fault signaling counters from interfaces                                                 | clear lfs counters                               |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear lldp counters                          | Clear the LLDP counters (all or per interface)                                                      | clear lldp counters                              |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear mpls traffic-engineering pcep counters | Clear PCEP counters                                                                                 | clear mpls traffic-engineering pcep counters     |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear ndp                                    | Clear entries from the NDP table                                                                    | clear ndp                                        |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear netconf session                        | Clear active netconf session                                                                        | clear netconf session                            |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear ospf interface                         | Clear OSPF iterface information                                                                     | clear ospf interfaces                            |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear qos counters                           | Clear QoS counters information                                                                      | clear qos counters                               |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear rib-manager fpm stats                  | Clear RIB manager forwarding path manager statistics                                                | clear rib-manager fpm stats                      |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear rsvp auto-bandwidth                    | Reset the auto-bandwidth adjustment interval timer and clear all the collected average-rate samples | clear rsvp auto-bandwidth                        |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear rsvp statistics all                    | Clear all RSVP statistics on all interfaces and tunnels                                             | clear rsvp statistics all                        |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear rsvp statistics errors                 | Clear RSVP error statistics                                                                         | clear rsvp statistics errors                     |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear rsvp statistics packets                | clear RSVP packet statistics                                                                        | clear rsvp statistics packets                    |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear rsvp statistics tunnels                | Clear statistics for RSVP tunnels                                                                   | clear rsvp statistics tunnels                    |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear rsvp tunnels                           | Reset the RSVP tunnel sessions (all, per tunnel, per destination, per role or per state)            | clear rsvp tunnels                               |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear segment-routing statistics             | Clears the traffic statistics associated with a SR-TE policies                                      | clear segment-routing statistics                 |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear services mpls-oam counters             | Reset the probe and packets counters                                                                | clear services mpls-oam counters                 |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear ssh session                            | Terminate an active SSH session                                                                     | clear ssh session                                |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear system commit                          | Cancel a confirmed commit                                                                           | clear system commit                              |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear system tech-support                    | Clear the current creation of the tech-support file                                                 | clear system tech-support                        |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear twamp session                          | Terminate TWAMP sessions                                                                            | clear twamp session                              |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+
| clear twamp statistics                       | Clears TWAMP statistics for control and data sessions                                               | clear twamp statistics                           |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------+

---

## clear access-lists counters.rst

clear access-lists counters
---------------------------

**Minimum user role:** operator

Clearing the access-list counters resets the access-list counters to zero and deletes the counters' information from the database.

To clear the access-list counters:

**Command syntax: clear access-list counters** [interface-name] [access-list-type] [access-list-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**
 - Clear access-lists counters - clears all ACL rules on all interfaces
 - Clear access-lists counters interface x - clears all ACL rules on the specified interface
 - Clear access-lists counters interface x access-list-type - clears all rules for a specified ACL type (v4 or v6) on a specified interface
 - Clear access-lists counters interface x access-list-type access-list-name - clears all rules for a specified ACL (name+type) on a specified interface.

**Parameter table**

+---------------------+-----------------------------------------------------------------------+---------------------------------------------------+---------+
|                     |                                                                       | Range                                             | Default |
| Parameter           | Description                                                           |                                                   |         |
+=====================+=======================================================================+===================================================+=========+
|                     |                                                                       | ge<interface speed>-<A>/<B>/<C>                   |         |
| interface-name      | Clears the counters for all ACL rules on the specified interface      |                                                   |         |
|                     |                                                                       | ge<interface speed>-<A>/<B>/<C>.<sub-interface id>|         |
|                     |                                                                       |                                                   |         |
|                     |                                                                       | bundle-<bundle-id>                                |\ -      |
|                     |                                                                       |                                                   |         |
|                     |                                                                       | bundle-<bundle-id>.<sub-interface-id>             |         |
|                     |                                                                       |                                                   |         |
|                     |                                                                       | mgmt0                                             |         |
+---------------------+-----------------------------------------------------------------------+---------------------------------------------------+---------+
|                     |                                                                       |                                                   | both    |
| access-list-type    | Clears the counters for the specified ACL type                        | IPv4                                              |         |
|                     |                                                                       |                                                   |         |
|                     |                                                                       | IPv6                                              |         |
+---------------------+-----------------------------------------------------------------------+---------------------------------------------------+---------+
|                     |                                                                       |                                                   |         |
| access-list-name    | Clears the counters for the specified ACL                             | String                                            | \ -     |
+---------------------+-----------------------------------------------------------------------+---------------------------------------------------+---------+


**Example**
::

	dnRouter# clear access-lists counters
	dnRouter# clear access-lists counters ge100-1/1/1
	dnRouter# clear access-lists counters ge100-1/1/1 ipv4
	dnRouter# clear access-lists counters ge100-1/1/1 ipv4 MyAclName

.. **Help line:** clear access-lists counters

**Command History**

+-------------+-----------------------------------------------------+
|             |                                                     |
| Release     | Modification                                        |
+=============+=====================================================+
|             |                                                     |
| 5.1.0       | Command introduced                                  |
+-------------+-----------------------------------------------------+
|             |                                                     |
| 6.0         | Replaced acl with access-list                       |
+-------------+-----------------------------------------------------+
|             |                                                     |
| 7.0         | Replaced access-list with access-lists in syntax    |
+-------------+-----------------------------------------------------+

---

## clear access-lists counters in-band-management.rst

clear access-lists counters in-band-management
----------------------------------------------

**Minimum user role:** operator

To clear the control plane in-band management access-list counters:

**Command syntax: clear access-lists counters in-band-management** [access-list-type] [access-list-name]

**Command mode:** operation

.. **Hierarchies**


.. **Note**
 - Clear access-lists counters in-band-management - clears all Control Plane ACL rules counters for both ACL types
 - Clear access-lists counters in-band-management [access-list-type] - clears Control Plane ACL rules for the specified ACL type
 - Clear access-lists counters in-band-management [access-list-name] - clears Control Plane ACL rules for the specified ACL name.

**Parameter table**

+---------------------+-------------------------------------------------------------+----------------------------------------+---------+
|                     |                                                             |                                        | Default |
| Parameter           | Description                                                 | Range                                  |         |
+=====================+=============================================================+========================================+=========+
|                     |                                                             |                                        |         |
| access-list-type    | Clears the counters for the specified access-list type      | IPv4                                   |         |
|                     |                                                             |                                        | \ -     |
|                     |                                                             | IPv6                                   |         |
+---------------------+-------------------------------------------------------------+----------------------------------------+---------+
|                     |                                                             |                                        |         |
| access-list-name    | Clears the counters for the specified access-list           | The name of an existing access-list    |\ -      |
+---------------------+-------------------------------------------------------------+----------------------------------------+---------+

**Example**
::

	dnRouter# clear access-lists counters in-band-management
	dnRouter# clear access-lists counters in-band-management ipv4
	dnRouter# clear access-lists counters in-band-management CP_ACL_IPv6
	dnRouter# clear access-lists counters in-band-management ipv4 CP_ACL_IPv4

.. **Help line:** Clears control plane in-band-management access list counters

**Command History**

+-----------+-----------------------+
| Release   | Modification          |
+===========+=======================+
| 13.0      | Command introduced    |
+-----------+-----------------------+

---

## clear access-lists counters global-acl.rst

clear access-lists counters global-acl
--------------------------------------

**Minimum user role:** operator

To clear the global access-list counters:

**Command syntax: clear access-lists counters global-acl** [access-list-type]

**Command mode:** operation

.. **Hierarchies**


.. **Note**
 - Clear access-lists counters global-acl - clears all global access-list counters for all directions and types
 - Clear access-lists counters global-acl [access-list-type] - clears global access-list counters for the specified ACL type

**Parameter table**

+---------------------+-------------------------------------------------------------+----------------------------------------+---------+
|                     |                                                             |                                        | Default |
| Parameter           | Description                                                 | Range                                  |         |
+=====================+=============================================================+========================================+=========+
|                     |                                                             |                                        |         |
| access-list-type    | Clears the counters for the specified access-list type      | ipv4                                   |         |
|                     |                                                             |                                        | \ -     |
|                     |                                                             | ipv6                                   |         |
+---------------------+-------------------------------------------------------------+----------------------------------------+---------+

**Example**
::

	dnRouter# clear access-lists counters global-acl
	dnRouter# clear access-lists counters global-acl ipv4

.. **Help line:** Clears global access-list counters

**Command History**

+-----------+-----------------------+
| Release   | Modification          |
+===========+=======================+
| 19.3      | Command introduced    |
+-----------+-----------------------+

---

## clear access-lists counters acl-name.rst

clear access-lists counters acl-name
------------------------------------

**Minimum user role:** operator

Clearing the access-list counters resets the access-list counters to zero and deletes the counters' information from the database.

To clear the all counters related to a given in used access-list:

**Command syntax: clear access-list counters [access-list-type] [access-list-name]**

**Command mode:** operation

.. **Hierarchies**

.. **Note**
 - Clear operation will clear all access-list statistics including case where statistics are per access-list and not per interface
 
**Parameter table**

+---------------------+-----------------------------------------------------------------------+---------------------------------------------------+---------+
|                     |                                                                       | Range                                             | Default |
| Parameter           | Description                                                           |                                                   |         |
+=====================+=======================================================================+===================================================+=========+
|                     |                                                                       |                                                   | \ -     |
| access-list-type    | Clears the counters for the specified ACL type                        | IPv4                                              |         |
|                     |                                                                       |                                                   |         |
|                     |                                                                       | IPv6                                              |         |
+---------------------+-----------------------------------------------------------------------+---------------------------------------------------+---------+
|                     |                                                                       |                                                   |         |
| access-list-name    | Clears the counters for the specified ACL                             | String                                            | \ -     |
+---------------------+-----------------------------------------------------------------------+---------------------------------------------------+---------+


**Example**
::

	dnRouter# clear access-lists counters ipv4 MyAclName

.. **Help line:** clear access-lists counters

**Command History**

+-------------+-----------------------------------------------------+
| Release     | Modification                                        |
+=============+=====================================================+
| 25.2        | Command introduced                                  |
+-------------+-----------------------------------------------------+

---


## clear arp.rst

clear arp
----------
**Minimum user role:** operator

To delete dynamic routes from the ARP table, use the following command:

**Command syntax: clear arp** vrf [vrf-name] interface [interface-name] ipv4-address [ipv4-host-address]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - clear arp - clears all dynamic arp entries in table

 - clear arp interface - clears all dynamic arp entries for specific interface

 - clear arp ipv4-address - clears dynamic arp entry for specific ipv4-address in a specific interface

 - clear arp - clears all dynamic ARP entries under default VRF

 - clear arp vrf - clears dynamic ARP entries for a specific VRF. It is not possible to specify 'all' to clear all dynamic ARP entries from all VRFs.

 - clear arp interface - clears all dynamic ARP entries for a specific interface. when VRF filter is used before, then only relevant interfaces under the specified VRF will be suggested

 - clear arp ipv4-address - clears dynamic ARP entry for a specific ipv4-address in a specific interface

.. **Help line:** clear dynamic arp entries

**Parameter table**

+----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------+
|                      |                                                                           |                                                                             |             |
| Parameter            | Description                                                               | Range                                                                       | Default     |
+======================+===========================================================================+=============================================================================+=============+
|                      |                                                                           |                                                                             |             |
| interface-name       | The name of the interface for which you want to clear all ARP entries     | ge<interface speed>-<A>/<B>/<C>                                             | \-          |
|                      |                                                                           |                                                                             |             |
|                      |                                                                           | ge<interface speed>-<A>/<B>/<C>.<sub-interface id>                          |             |
|                      |                                                                           |                                                                             |             |
|                      |                                                                           | bundle-<bundle id>                                                          |             |
|                      |                                                                           |                                                                             |             |
|                      |                                                                           | bundle-<bundle id>.<sub-interface id>, mgmt0, mgmt-ncc-0, mgmt-ncc-1        |             |
+----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------+
|                      |                                                                           |                                                                             |             |
| ip4v-host-address    | The IPv4 (A.B.C.D) address for which you want to clear all ARP entries    | A.B.C.D                                                                     | \-          |
+----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------+
| vrf-name             | The name of the specific vrf for which you want to clear all ARP entries  | default, mgmt0, mgmt-ncc-0, mgmt-ncc-1, etc                                 | default     |
+----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------+

**Example**
::

	dnRouter# clear arp
	dnRouter# clear arp vrf My_VRF
	dnRouter# clear arp interfaces ge100-1/8/1
	dnRouter# clear arp interfaces ge100-1/8/1 ipv4-address 1.2.3.4

**Command History**

+-------------+--------------------------------------------------------+
| Release     | Modification                                           |
+=============+========================================================+
| 5.1.0       | Command introduced                                     |
+-------------+--------------------------------------------------------+
| 16.1        | Added support to clear arp entries per vrf instance    |
+-------------+--------------------------------------------------------+

---


## clear ndp.rst

clear ndp
----------

**Minimum user role:** operator

To delete dynamic routes from the NDP table, use the following command:

**Command syntax: clear ndp** vrf [vrf-name] interface [interface-name] ipv6-address [ipv6-host-address]

	dnRouter# clear ndp
	dnRouter# clear ndp vrf My_VRF
	dnRouter# clear ndp interfaces ge100-1/8/1
	dnRouter# clear ndp interfaces ge100-1/8/1 ipv6-address 2001:1234::1

**Command mode:** operation

.. **Hierarchies**

**Note**

- If you do not specify an [interface-name] or an [ipv6-host-address], all NDP entries will be cleared from the NDP table

- clear ndp vrf - clears dynamic NDP entries for a specific VRF. It is not possible to specify 'all' to clear all dynamic NDP entries from all VRFs.

.. - clear ndp - clears all dynamic NDP entries under default VRF

.. - clear ndp interface - clears all dynamic NDP entries for a specific interface. when VRF filter is used before, then only relevant interfaces under the specified VRF will be suggested

.. - clear ndp ipv6-address - clears dynamic NDP entry for specific ipv6-address for specific interface


**Parameter table:**

+-------------------+--------------------------------------------------------------------------+---------------+
| Parameter         | Values                                                                   | Default value |
+===================+==========================================================================+===============+
| interface-name    | ge<interface speed>-<A>/<B>/<C>                                          |               |
|                   |                                                                          |               |
|                   | ge<interface speed>-<A>/<B>/<C>.<sub-interface id>                       |               |
|                   |                                                                          |               |
|                   | bundle-<bundle id>                                                       |               |
|                   |                                                                          |               |
|                   | bundle-<bundle id>.<sub-interface id>, mgmt0, mgmt-ncc-0, mgmt-ncc-1     |               |
+-------------------+--------------------------------------------------------------------------+---------------+
| ipv6-host-address | {ipv6-address format} as /128                                            |               |
+-------------------+--------------------------------------------------------------------------+---------------+
| vrf-name          | default, mgmt0, mgmt-ncc-0, mgmt-ncc-1, etc                              | default       |
+-------------------+--------------------------------------------------------------------------+---------------+

**Example**
::

	dnRouter# clear ndp
	dnRouter# clear ndp vrf My_VRF
	dnRouter# clear ndp interfaces ge100-1/8/1
	dnRouter# clear ndp interfaces ge100-1/8/1 ipv6-address 2001:1234::1


.. **Help line:** clear dynamic ndp entries

**Command History**

+-------------+--------------------------------------------------------+
| Release     | Modification                                           |
+=============+========================================================+
| 5.1.0       | Command introduced                                     |
+-------------+--------------------------------------------------------+
| 16.1        | Added support to clear ndp entries per vrf instance    |
+-------------+--------------------------------------------------------+

---

## clear bfd session.rst

clear bfd session
-----------------

**Minimum user role:** operator

Restarting a BFD session will not affect protected protocols. These parameters have the following impact:

- clear bfd - restarts all BFD sessions.

- vrf - clears the BFD sessions running in the specified VRF. When not specified, it effects the default VRF sessions.

- discriminator - clears a BFD session matching the local discriminator.

To restart BFD sessions:

**Command syntax: clear bfd session** tunnel [tunnel-name] | {vrf [vrf-name] | discriminator [discriminator] | local-address [ip-address] | neighbor [neighbor-address] | interface [interface-name] | client [client] }

**Command mode:** operation

.. **Hierarchies**

**Note**

- When both BFD address-family match the clear request, reset both address-family sessions

.. -Restarting the BFD sessions will also clear the BFD session counters.


**Parameter table:**

+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| Parameter        | Values                                                                              | Default value      | notes                                                                         |
+==================+=====================================================================================+====================+===============================================================================+
| vrf-name         | Any configured vrf name                                                             | default            |                                                                               |
|                  |                                                                                     |                    |                                                                               |
|                  | The following vrfs exist by default:  default, mgmt0, mgmt-ncc-0, mgmt-ncc-1        |                    |                                                                               |
|                  |                                                                                     |                    |                                                                               |
|                  | Use 'all' to clear sessions from all vrfs                                           |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| discriminator    | 0-4294967295                                                                        |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| tunnel-name      | string length 1..255                                                                |                    |  Head tunnel name                                                             |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| local-address    | A.B.C.D                                                                             |                    | when neighbor-address is used, must match neighbor-address address-family     |
|                  |                                                                                     |                    |                                                                               |
|                  | {ipv6 address format}                                                               |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| neighbor-address | A.B.C.D                                                                             |                    | when local-address is used, must match local -address address-family          |
|                  |                                                                                     |                    |                                                                               |
|                  | {ipv6 address format}                                                               |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| interface-name   | bundle-<bundle id>                                                                  |                    |                                                                               |
|                  |                                                                                     |                    |                                                                               |
|                  | bundle-<bundle id>.<sub-interface-id>                                               |                    |                                                                               |
|                  |                                                                                     |                    |                                                                               |
|                  | ge<interface speed>-<A>/<B>/<C>                                                     |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| client           | [bundle interface name], bgp, static, rsvp                                          |                    |                                                                               |
|                  | ospf, ospfv3                                                                        |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+

**Example**
::

	dnRouter# clear bfd session
	dnRouter# clear bfd session discriminator 100
	dnRouter# clear bfd session tunnel TUNNEL_1
	dnRouter# clear bfd session neighbor 1.2.3.4
	dnRouter# clear bfd session local-address 1.2.3.3 neighbor 1.2.3.4
	dnRouter# clear bfd session local-address 2001:ab12::2
	dnRouter# clear bfd session interface ge10-2/1/1
	dnRouter# clear bfd session local-address 4.4.4.4 client rsvp
	dnRouter# clear bfd session client rsvp neighbor 5.5.5.5
	dnRouter# clear bfd session client bundle-3
	dnRouter# clear bfd session discriminator 8 interface ge100-0/0/1
	dnRouter# clear bfd session vrf CLIENT_A
	dnRouter# clear bfd session vrf CLIENT_A neighbor 1.2.3.4

.. **Help line:** Clear bfd sessions

**Command History**

+-------------+-----------------------------------------+
|             |                                         |
| Release     | Modification                            |
+=============+=========================================+
| 6.0         | Command introduced                      |
+-------------+-----------------------------------------+
| 9.0         | Command not supported                   |
+-------------+-----------------------------------------+
| 11.2        | Command reintroduced with new syntax    |
+-------------+-----------------------------------------+
| 12.0        | Added support for BFD for IS-IS         |
+-------------+-----------------------------------------+
| 16.1        | Support was added for VRFs              |
+-------------+-----------------------------------------+

---

## clear bfd statistics.rst

clear bfd statistics
--------------------

**Minimum user role:** operator

To clear BFD session statistics, which resets the BFD session counters:

- clear bfd statistics - clears all BFD sessions.

- vrf - clears BFD session statistics running in the specified VRF. When not specified, it assumes the default VRF sessions.

- discriminator - clears BFD sessions matching the local discriminator.

- tunnel - clears BFD sessions protecting an RSVP tunnel matching the tunnel-name.

- local-address - clears BFD sessions matching the local address.

To restart BFD sessions:

**Command syntax: clear bfd statistics** discriminator [discriminator] | tunnel [tunnel-name] | { vrf [vrf-name] local-address [ip-address] neighbor [neighbor-address] interface [interface-name] client [client] }

**Command mode:** operation

.. **Hierarchies**

**Note**

- When both BFD address-family match the clear request, reset both address-family sessions


**Parameter table**

+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| Parameter        | Values                                                                              | Default value      | notes                                                                         |
+==================+=====================================================================================+====================+===============================================================================+
| vrf-name         | Any configured vrf name                                                             | default            |                                                                               |
|                  |                                                                                     |                    |                                                                               |
|                  | The following vrfs exist by default:  default, mgmt0, mgmt-ncc-0, mgmt-ncc-1        |                    |                                                                               |
|                  |                                                                                     |                    |                                                                               |
|                  | Use 'all' to clear statistics form all vrfs                                         |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| discriminator    | 0-4294967295                                                                        |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| tunnel-name      | string length 1..255                                                                |                    |  Head tunnel name                                                             |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| local-address    | A.B.C.D                                                                             |                    | when neighbor-address is used, must match neighbor-address address-family     |
|                  |                                                                                     |                    |                                                                               |
|                  | {ipv6 address format}                                                               |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| neighbor-address | A.B.C.D                                                                             |                    | when local-address is used, must match local -address address-family          |
|                  |                                                                                     |                    |                                                                               |
|                  | {ipv6 address format}                                                               |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| interface-name   | bundle-<bundle id>                                                                  |                    |                                                                               |
|                  |                                                                                     |                    |                                                                               |
|                  | bundle-<bundle id>.<sub-interface-id>                                               |                    |                                                                               |
|                  |                                                                                     |                    |                                                                               |
|                  | ge<interface speed>-<A>/<B>/<C>                                                     |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+
| client           | [bundle interface name], bgp, static, rsvp                                          |                    |                                                                               |
|                  | ospf, ospfv3                                                                        |                    |                                                                               |
+------------------+-------------------------------------------------------------------------------------+--------------------+-------------------------------------------------------------------------------+

**Example**
::

	dnRouter# clear bfd statistics
	dnRouter# clear bfd statistics discriminator 100
	dnRouter# clear bfd statistics tunnel TUNNEL_1
	dnRouter# clear bfd statistics neighbor 1.2.3.4
	dnRouter# clear bfd statistics local-address 1.2.3.3 neighbor 1.2.3.4
	dnRouter# clear bfd statistics local-address 2001:ab12::2
	dnRouter# clear bfd statistics interface ge10-2/1/1
	dnRouter# clear bfd statistics local-address 4.4.4.4 client rsvp
	dnRouter# clear bfd statistics client rsvp neighbor 5.5.5.5
	dnRouter# clear bfd statistics client bundle-3
	dnRouter# clear bfd statistics vrf CLIENT_A


.. **Help line:** Clear bfd statistics


**Command History**

+-------------+------------------------------------+
|             |                                    |
| Release     | Modification                       |
+=============+====================================+
|             |                                    |
| 11.2        | Command introduced                 |
+-------------+------------------------------------+
|             |                                    |
| 12.0        | Added support for BFD for IS-IS    |
+-------------+------------------------------------+
| 16.1        | Support was added for VRFs         |
+-------------+------------------------------------+

---

## clear bgp neighbor.rst

clear bgp neighbor
------------------

**Minimum user role:** operator

To clear BGP neighbors:

**Command syntax: clear bgp** instance vrf [vrf-name] **neighbor {  * \| external \| [neighbor-address] \| remote-as [as-number] \| group [group-name]}** [address-family] [sub-address-family] soft [update-direction]

**Command mode:** operation

.. **Hierarchies**

**Note**

-  Optional parameters must match the order in the command

-  When performing a hard clear for a bgp neighbor with a specific address-family, for example clear bgp neighbor group BGP_GROUP ipv4, the bgp session will tear affecting all address families

-  When stating a sub-address family, the address-family and update direction must be specified

-  Address-family and sub-address-family are used to clear a specific address-family or sub-address-family

-  Use soft to apply soft reconfig

-  When stating 'instance vrf' support is for **'unicast'** sub-address-family only

-  When no update-direction is specified, perform a hard clear.

**Parameter table**

+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| Parameter             | Description                                                                                                                                                            | Range                                                          | Default     |
+=======================+========================================================================================================================================================================+================================================================+=============+
| vrf-name              | Clears only the specified VRF routes. When VRF is specified, only unicast sub-address-family is supported                                                              | 1..255 characters                                              | \ -         |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| \*                    | Clears all neighbors                                                                                                                                                   | \-                                                             | \ -         |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| external              | Clears all eBGP neighbors                                                                                                                                              | \-                                                             |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| neighbor-address      | Clears a specific neighbor                                                                                                                                             | A.B.C.D                                                        |             |
|                       |                                                                                                                                                                        | xx:xx::xx:xx                                                   |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| as-number             | Clears neighbors matching the specific AS number                                                                                                                       | 1..4294967295                                                  |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| group-name            | Clears all neighbors from the specified neighbor group                                                                                                                 | 1..255 characters                                              |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| address-family        | Clears only the specific address-family routes                                                                                                                         | IPv4                                                           |             |
|                       |                                                                                                                                                                        | IPv6                                                           |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| sub-address-family    | Clears neighbors for the specified sub-address family indicator (SAFI). When stating the sub-address-family, address-family and update-direction must be specified.    | unicast                                                        |             |
|                       |                                                                                                                                                                        | labeled-unicast                                                |             |
|                       |                                                                                                                                                                        | vpn                                                            |             |
|                       |                                                                                                                                                                        | flowspec                                                       |             |
|                       |                                                                                                                                                                        | multicast                                                      |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| soft                  | Allows routing tables to be reconfigured and activated without clearing the BGP session.                                                                               | \-                                                             |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| update-direction      | Clears neighbors in the specified direction. When not specified, hard clear is performed                                                                               | in - Triggers inbound soft reconfiguration                     |             |
|                       |                                                                                                                                                                        | out - Triggers inbound soft reconfiguration                    |             |
|                       |                                                                                                                                                                        | both - Triggers inbound and outbound soft   reconfiguration    |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+

**Example**
::

	dnRouter# clear bgp neighbor *
	dnRouter# clear bgp neighbor * ipv4
	dnRouter# clear bgp neighbor * ipv4 unicast out
	dnRouter# clear bgp neighbor * soft
	dnRouter# clear bgp neighbor * soft out

	dnRouter# clear bgp neighbor external
	dnRouter# clear bgp neighbor external ipv4
	dnRouter# clear bgp neighbor external ipv4 unicast out
	dnRouter# clear bgp neighbor external soft
	dnRouter# clear bgp neighbor external ipv6 soft in

	dnRouter# clear bgp neighbor 7.7.7.7
	dnRouter# clear bgp neighbor 7.7.7.7 ipv6
	dnRouter# clear bgp neighbor 7.7.7.7 ipv6 vpn in
	dnRouter# clear bgp neighbor 7.7.7.7 out
	dnRouter# clear bgp neighbor 7.7.7.7 soft out
	dnRouter# clear bgp neighbor 7.7.7.7 ipv6 unicast out

	dnRouter# clear bgp neighbor remote-as 64999
	dnRouter# clear bgp neighbor remote-as 64999 ipv6
	dnRouter# clear bgp neighbor remote-as 64999 ipv6 vpn in
	dnRouter# clear bgp neighbor remote-as 64999 out
	dnRouter# clear bgp neighbor remote-as 64999 ipv6 vpn soft

	dnRouter# clear bgp neighbor group BGP_GROUP
	dnRouter# clear bgp neighbor group BGP_GROUP ipv4
	dnRouter# clear bgp neighbor group BGP_GROUP ipv4 unicast out
	dnRouter# clear bgp neighbor group BGP_GROUP soft
	dnRouter# clear bgp neighbor group BGP_GROUP soft in


	dnRouter# clear bgp instance vrf A neighbor *
	dnRouter# clear bgp instance vrf A neighbor 7.7.7.7 ipv6
	dnRouter# clear bgp instance vrf A neighbor remote-as 64999 ipv6 unicast in
	dnRouter# clear bgp instance vrf A neighbor group BGP_GROUP soft in



.. **Help line:**

**Command History**

+-----------+-------------------------------------------------+
| Release   | Modification                                    |
+===========+=================================================+
| 6.0       | Command introduced                              |
+-----------+-------------------------------------------------+
| 13.0      | Added support for sub-address family flowspec   |
+-----------+-------------------------------------------------+
| 16.1      | Added support for sub-address family multicast  |
+-----------+-------------------------------------------------+
| TBD       | Added support for labeled-unicast safi          |
+-----------+-------------------------------------------------+

---

## clear bgp dampening.rst

clear bgp dampening
-------------------

**Minimum user role:** operator

To clear route flap dampening information:

**Command syntax: clear bgp** instance vrf [vrf-name] **dampening** [address-family] [sub-address-family] {route [route] \| prefix [prefix] \| neighbor [neighbor-address] }

**Command mode:** operation

.. **Hierarchies**

**Note**

- The optional parameters must match the order in the command

- When stating a sub-address family, an address-family must be specified

- If an address-family is specified, the route or prefix must match the address-family

- When stating 'instance vrf' - support is for **'unicast'** sub-address-family only.

**Parameter table**

+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      |             |
| Parameter             | Description                                                                                                                                                            | Range                | Default     |
+=======================+========================================================================================================================================================================+======================+=============+
|                       |                                                                                                                                                                        |                      |             |
| vrf-name              | Clears only the specified VRF routes                                                                                                                                   | 1..255 characters    | \ -         |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      |             |
| neighbor-address      | Clears a specific neighbor                                                                                                                                             | A.B.C.D              | \ -         |
|                       |                                                                                                                                                                        |                      |             |
|                       |                                                                                                                                                                        | xx:xx::xx:xx         |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      |             |
| address-family        | Clears only the specific address-family routes                                                                                                                         | IPv4                 | \ -         |
|                       |                                                                                                                                                                        |                      |             |
|                       |                                                                                                                                                                        | IPv6                 |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      |             |
| sub-address-family    | Clears neighbors for the specified sub-address family indicator (SAFI). When stating the sub-address-family, address-family and update-direction must be specified.    | unicast              | \ -         |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      |             |
| route                 | The route for which to clear dampening information. The route address must match the address-family                                                                    | A.B.C.D              | \ -         |
|                       |                                                                                                                                                                        |                      |             |
|                       |                                                                                                                                                                        | xx:xx::xx:xx         |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      |             |
| prefix                | The prefix for which to clear dampening   information. The prefix address must match the address-family                                                                | A.B.C.D/x            | \ -         |
|                       |                                                                                                                                                                        |                      |             |
|                       |                                                                                                                                                                        | xx:xx::xx:xx/x       |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+

**Example**
::

	dnRouter# clear bgp dampening

	dnRouter# clear bgp dampening ipv4
	dnRouter# clear bgp dampening ipv4 unicast
	dnRouter# clear bgp dampening ipv4 unicast route 1.1.1.1
	dnRouter# clear bgp dampening ipv4 prefix 1.2.0.0/16
	dnRouter# clear bgp dampening ipv4 vpn neighbor 2.2.2.2

	dnRouter# clear bgp dampening ipv6 unicast route 2:2::2:2
	dnRouter# clear bgp dampening ipv6 prefix 2:2::2:0/32
	dnRouter# clear bgp dampening ipv6 vpn neighbor 2.2.2.2

	dnRouter# clear bgp dampening route 1.1.1.1
	dnRouter# clear bgp dampening prefix 1.2.0.0/16
	dnRouter# clear bgp dampening neighbor 2.2.2.2

	dnRouter# clear bgp instance vrf A dampening
	dnRouter# clear bgp instance vrf A dampening ipv4
	dnRouter# clear bgp instance vrf A dampening ipv4 unicast
	dnRouter# clear bgp instance vrf A dampening ipv4 unicast route 1.1.1.1
	dnRouter# clear bgp instance vrf A dampening ipv4 prefix 1.2.0.0/16



.. **Help line:**


**Command History**

+-----------+-----------------------+
| Release   | Modification          |
+===========+=======================+
| 6.0       | Command introduced    |
+-----------+-----------------------+

---

## clear bgp prefix-filter.rst

clear bgp prefix-filter
-----------------------

**Minimum user role:** operator

To push out prefix-list ORF and do inbound soft reconfigure:

**Command syntax: clear bgp** instance vrf [vrf-name] **neighbor {  * \| external \| [neighbor-address] \| remote-as [as-number] \| group [group-name]}** [address-family] [sub-address-family] **in prefix-filter**

**Command mode:** operation

.. **Hierarchies**

**Note**

- Optional parameters must match the order in the command

- When stating a sub-address family, the address-family must be specified.


**Parameter table**

+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      |             |
| Parameter             | Description                                                                                                                                                            | Range                | Default     |
+=======================+========================================================================================================================================================================+======================+=============+
|                       |                                                                                                                                                                        |                      |             |
| vrf-name              | Clears only the specified VRF routes.                                                                                                                                  | 1..255 characters    | Disabled    |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      | \ -         |
| \*                    | Clears all neighbors                                                                                                                                                   | \ -                  |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      | \ -         |
| external              | Clears all eBGP neighbors                                                                                                                                              | \ -                  |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      | \ -         |
| neighbor-address      | Clears a specific neighbor                                                                                                                                             | A.B.C.D              |             |
|                       |                                                                                                                                                                        |                      |             |
|                       |                                                                                                                                                                        | xx:xx::xx:xx         |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      | \ -         |
| as-number             | Clears neighbors matching the specific AS number                                                                                                                       | 1..4294967295        |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      | \ -         |
| group-name            | Clears all neighbors from the specified neighbor group                                                                                                                 | 1..255 characters    |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      | \ -         |
| address-family        | Clears only the specific address-family routes                                                                                                                         | IPv4                 |             |
|                       |                                                                                                                                                                        |                      |             |
|                       |                                                                                                                                                                        | IPv6                 |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                       |                                                                                                                                                                        |                      | \ -         |
| sub-address-family    | Clears neighbors for the specified sub-address family indicator (SAFI). When stating the sub-address-family, address-family and update-direction must be specified.    | unicast              |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+



**Example**
::

	dnRouter# clear bgp neighbor * in prefix-filter
	dnRouter# clear bgp neighbor * ipv4 in prefix-filter
	dnRouter# clear bgp neighbor * ipv4 unicast in prefix-filter

	dnRouter# clear bgp neighbor external in prefix-filter
	dnRouter# clear bgp neighbor external ipv4 in prefix-filter
	dnRouter# clear bgp neighbor external ipv4 unicast in prefix-filter

	dnRouter# clear bgp neighbor 7.7.7.7 in prefix-filter
	dnRouter# clear bgp neighbor 7.7.7.7 ipv6 in prefix-filter
	dnRouter# clear bgp neighbor 7.7.7.7 ipv6 unicast in prefix-filter

	dnRouter# clear bgp neighbor remote-as 64999 in prefix-filter
	dnRouter# clear bgp neighbor remote-as 64999 ipv6 in prefix-filter
	dnRouter# clear bgp neighbor remote-as 64999 ipv6 unicast in prefix-filter

	dnRouter# clear bgp neighbor group BGP_GROUP in prefix-filter
	dnRouter# clear bgp neighbor group BGP_GROUP ipv4 in prefix-filter
	dnRouter# clear bgp neighbor group BGP_GROUP ipv4 unicast in prefix-filter
	dnRouter# clear bgp instance vrf A neighbor * in prefix-filter
	dnRouter# clear bgp instance vrf A neighbor 7.7.7.7 ipv6 in prefix-filter
	dnRouter# clear bgp instance vrf A neighbor remote-as 64999 ipv6 unicast in prefix-filter
	dnRouter# clear bgp instance vrf A neighbors group BGP_GROUP in prefix-filter

.. **Help line:**

**Command History**

+-----------+-------------------------------------------------+
| Release   | Modification                                    |
+===========+=================================================+
| 6.0       | Command introduced                              |
+-----------+-------------------------------------------------+

---

## clear bgp redistribute.rst

clear bgp redistribute
----------------------

**Minimum user role:** operator

To re-evaluate all redistributed routes:

**Command syntax: clear bgp** instance vrf [vrf-name] **redistribute {connected \| ospf \| static}**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table**

+---------------+--------------------------------------------------+-------+-------------+
|               |                                                  | Range |             |
| Parameter     | Description                                      |       | Default     |
+===============+==================================================+=======+=============+
|               |                                                  |       |             |
| vrf-name      | Clear only routes belonging to the specified VRF | \-    | \ -         |
+---------------+--------------------------------------------------+-------+-------------+
|               |                                                  |       |             |
| static        | Clear only static redistributed routes           | \-    | \ -         |
+---------------+--------------------------------------------------+-------+-------------+
|               |                                                  |       |             |
| OSPF          | Clear only OSPF redistributed routes             | \-    | \ -         |
+---------------+--------------------------------------------------+-------+-------------+
|               |                                                  |       |             |
| connected     | Clear only connected redistributed routes        | \-    | \ -         |
+---------------+--------------------------------------------------+-------+-------------+

**Example**
::

	dnRouter# clear bgp redistribute static
	dnRouter# clear bgp redistribute ospf
	dnRouter# clear bgp redistribute connected

	dnRouter# clear bgp instance vrf A redistribute static
	dnRouter# clear bgp instance vrf A redistribute ospf
	dnRouter# clear bgp instance vrf A redistribute connected


.. **Help line:**

**Command History**

+-----------+-----------------------+
| Release   | Modification          |
+===========+=======================+
| 6.0       | Command introduced    |
+-----------+-----------------------+

---

## clear cli history.rst

clear cli history
-----------------

**Minimum user role:** operator

To clear the cli history from all the commands you entered during the current the session:

**Command syntax: clear cli history**	

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. **Parameter table:**


**Example**
::

	dnRouter# clear cli history

.. **Help line:** clear cli command history, clear cli history clears also the cli prompt history.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+

---

## clear system commit.rst

clear system commit
-------------------

**Minimum user role:** operator

To cancel the tentative commit performed with the commit confirm command:

**Command syntax: clear system commit**

**Command mode:** operation

.. **Hierarchies**

**Note**

- Canceling a commit confirm command is equivalent to a rollback 1 action.

- If no pending commit or current commit is running, a message is displayed that no commit is scheduled.

- Any user with the right privileges can clear a pending commit.


.. **Parameter table**


**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interfaces bundle-1 mac-address 00:00:00:00:00:01
	dnRouter(cfg)# commit confirm
	Commit confirm will automatically rollback in 10 minutes unless confirmed
	Commit succeeded by ADMIN at 27-Jan-2017 22:11:00 UTC
	
	dnRouter# clear system commit
	Configuration commit rollback by ADMIN at 27-Jan-2017 22:11:00 UTC
	
	.. (no configuration being done)
	dnRouter# clear system commit
	ERROR: No commit confirm scheduled
	
	
.. **Help line:** cancel the tentative commit performed by the user with the commit confirm command


**Command History**

+-------------+---------------------------------------------+
|             |                                             |
| Release     | Modification                                |
+=============+=============================================+
|             |                                             |
| 6.0         | Command introduced                          |
+-------------+---------------------------------------------+

---


## clear bgp neighbor link-state.rst

clear bgp neighbor link-state
-----------------------------

**Minimum user role:** operator

To clear link states received from BGP neighbor:

**Command syntax: clear bgp** instance vrf [vrf-name] **neighbor {  * \| external \| [neighbor-address] \| remote-as [as-number] \| group [group-name]} link-state**

**Command mode:** operation

.. **Hierarchies**

**Note**

-  Optional parameters must match the order in the command

**Parameter table**

+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| Parameter             | Description                                                                                                                                                            | Range                                                          | Default     |
+=======================+========================================================================================================================================================================+================================================================+=============+
| vrf-name              | Clears only the specified VRF routes.                                                                                                                                 | 1..255 characters                                              | \ -         |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| \*                    | Clears all neighbors                                                                                                                                                   | \-                                                             | \ -         |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| external              | Clears all eBGP neighbors                                                                                                                                              | \-                                                             |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| neighbor-address      | Clears a specific neighbor                                                                                                                                             | A.B.C.D                                                        |             |
|                       |                                                                                                                                                                        | xx:xx::xx:xx                                                   |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| as-number             | Clears neighbors matching the specific AS number                                                                                                                       | 1..4294967295                                                  |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+
| group-name            | Clears all neighbors from the specified neighbor group                                                                                                                 | 1..255 characters                                              |             |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-------------+

**Example**
::

	dnRouter# clear bgp neighbor * link-state
	dnRouter# clear bgp neighbor external link-state
	dnRouter# clear bgp neighbor 7.7.7.7 link-state
	dnRouter# clear bgp neighbor remote-as 64999 link-state
	dnRouter# clear bgp neighbor group BGP_GROUP link-state
	dnRouter# clear bgp instance vrf A neighbor * link-state

.. **Help line:**

**Command History**

+-----------+-------------------------------------------------+
| Release   | Modification                                    |
+===========+=================================================+
| 14.0      | Command introduced                              |
+-----------+-------------------------------------------------+

---

## clear bgp default-originate.rst

clear bgp default-originate
---------------------------

**Minimum user role:** operator

To re-evaluate the default originate policy:

**Command syntax: clear bgp** instance vrf [vrf-name] **default-originate [address-family]**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table**

+-------------------+---------------------------------------------------------------------------------+-----------+-------------+
|                   |                                                                                 |           |             |
| Parameter         | Description                                                                     | Range     | Default     |
+===================+=================================================================================+===========+=============+
|                   |                                                                                 |           |             |
| vrf-name          | Clear only routes belonging to the specified VRF.                               | \-        | \ -         |
+-------------------+---------------------------------------------------------------------------------+-----------+-------------+
|                   |                                                                                 |           |             |
| address-family    | Clear only the specific address-family routes: IPv4-unicast , IPv6-unicast      | \-        | \ -         |
| address-family    |   IPv4-labeled-unicast, IPv6-labeled-unicast                                    | \-        | \ -         |
+-------------------+---------------------------------------------------------------------------------+-----------+-------------+


**Example**
::

	dnRouter# clear bgp default-originate ipv4-unicast
	dnRouter# clear bgp default-originate ipv6-unicast
	dnRouter# clear bgp instance vrf A default-originate ipv4-unicast
	dnRouter# clear bgp instance vrf A default-originate ipv6-unicast

.. **Help line:**

**Command History**

+-----------+-------------------------------------------------+
| Release   | Modification                                    |
+===========+=================================================+
| 6.0       | Command introduced                              |
+-----------+-------------------------------------------------+
| TBD       | Added support for labeled-unicast safi          |
+-----------+-------------------------------------------------+

---

## clear dhcp interface.rst

clear dhcp interfaces
----------------------


**Minimum user role:** operator

To clear the DHCP aquired IP address for a specific interface, use the following command:

**Command syntax: clear dhcp interfaces [interface-name]** [ipv4-address | ipv6-address]  

**Command mode:** operation

.. **Hierarchies**

**Note**

- If no ipv4-address / ipv6-address parameters are specified, both IPv4 and IPv6 addresses are released

- If ipv4-address parameter is specified, IPv4 address is released 

- If ipv6-address parameter is specified, IPv4 address is released.

**Parameter table:**

+-------------------+--------------------------------------------------------------------------------+--------------------------------------+-------------+
|                   |                                                                                |                                      |             |
| Parameter         | Description                                                                    | Range                                | Default     |
+===================+================================================================================+======================================+=============+
|                   |                                                                                |                                      |             |
| interface-name    | The name of the interface for which you want to clear all dhcp IP addresses    | mgmt0, mgmt-ncc-0, mgmt-ncc-1        | \-          |
+-------------------+--------------------------------------------------------------------------------+--------------------------------------+-------------+


**Example**
::

	dnRouter# clear dhcp interfaces mgmt0
	dnRouter# clear dhcp interfaces mgmt-ncc-0 ipv4-address
	dnRouter# clear dhcp interfaces mgmt-ncc-1 ipv6-address

.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.1        | Command introduced    |
+-------------+-----------------------+
| 25.2        | Updated command syntax|
+-------------+-----------------------+

---

## clear interfaces counters.rst

clear interfaces counters
-------------------------

**Minimum user role:** operator

Clearing the interface counters resets the counters to zero and removes the counter information from the database. It does not clear SNMP-based and SyncE ESMC counters.

To clear the interface counters:

**Command syntax: clear interfaces counters [interface-name]**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. - **Clear interfaces dampening** - clears all counters for **ALL** interfaces

.. - **Clear interfaces dampening interface x** - clears **ALL** counters for a specific interface.

.. **Parameter table:**

**Example**
::

	dnRouter# clear interfaces counters
	dnRouter# clear interfaces counters ge100-1/1/1
	dnRouter# clear interfaces counters ge100-1/1/1.134


.. **Help line:** clear access-list counters

**Command History**

+-------------+---------------------------------------+
|             |                                       |
| Release     | Modification                          |
+=============+=======================================+
|             |                                       |
| 5.1.0       | Command introduced                    |
+-------------+---------------------------------------+
|             |                                       |
| 6.0         | Replaced interface with interfaces    |
+-------------+---------------------------------------+

---

## clear lacp counters.rst

clear lacp counters
--------------------

**Minimum user role:** operator

Clearing the LACP interface counters resets the counters to zero and removes the counter information from the database.

To clear the LACP interface counters:

**Command syntax: clear lacp counters [interface-name]**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - **Clear lacp counters** - clears all counters for **ALL** interfaces

 - **Clear lacp counters interface [bundle interface]** - clears all counters for all members in the bundle

 - **Clear lacp counters interface [physical interface]** - clears all counters for a specific member interface


**Parameter table:**

+-------------------+------------------------------------------------------------------------------------------------------+---------------------------------+-------------+
|                   |                                                                                                      |                                 |             |
| Parameter         | Description                                                                                          | Range                           | Default     |
+===================+======================================================================================================+=================================+=============+
|                   |                                                                                                      |                                 |             |
| interface-name    | optionally specify an interface name to clear only the LACP counters for the specified interface.    | ge<interface speed>-<A>/<B>/<C> | \-          |
|                   |                                                                                                      |                                 |             |
|                   |                                                                                                      | bundle-<bundle-id>              |             |
+-------------------+------------------------------------------------------------------------------------------------------+---------------------------------+-------------+


**Example**
::

	dnRouter# clear lacp counters
	dnRouter# clear lacp counters bundle-1
	dnRouter# clear lacp counters ge100-1/1/1



.. **Help line:** clear lacp counters

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 6.0         | Command introduced    |
+-------------+-----------------------+

---

## clear ldp neighbor.rst

clear ldp neighbor
------------------

**Minimum user role:** operator

To restart the LDP sessions (restart TCP sessions only):

**Command syntax: clear ldp neighbor** [neighbor-address]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - clear ldp neighbor - restart all ldp TCP sessions only

 - clear ldp neighbor [neighbor-address] - restart ldp TCP session to a specific ldp neighbor


**Parameter table:**

+---------------------+--------------------------------------------------------+------------+-------------+
|                     |                                                        |            |             |
| Parameter           | Description                                            | Range      | Default     |
+=====================+========================================================+============+=============+
|                     |                                                        |            |             |
| neighbor-address    | Restarts LDP TCP session to a specific LDP neighbor    | A.B.C.D    | \-          |
+---------------------+--------------------------------------------------------+------------+-------------+
|                     |                                                        |            |             |
| statistics          | Clears all LDP neighbor statistics                     | \-         | \-          |
+---------------------+--------------------------------------------------------+------------+-------------+


**Example**
::

	dnRouter# clear ldp neighbor
	dnRouter# clear ldp neighbor 7.7.7.7

.. **Help line:** Restart ldp session

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 6.0         | Command introduced    |
+-------------+-----------------------+

---

## clear lldp counters.rst

clear lldp counters
--------------------

**Minimum user role:** operator

To clear LLDP counters:

**Command syntax: clear lldp counters [interface-name]**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - **Clear lldp counters** - clears all counters for **all** interfaces/sessions

 - **Clear lldp counters interface x** - clears all counters for a specific interface


**Parameter table:**

+-------------------+---------------------------------------------------------------+---------------------------------+-------------+
|                   |                                                               |                                 |             |
| Parameter         | Description                                                   | Range                           | Default     |
+===================+===============================================================+=================================+=============+
|                   |                                                               |                                 |             |
| interface-name    | Clears the LLDP counters only for the specified interface.    | Physical interfaces:            | \-          |
|                   |                                                               |                                 |             |
|                   |                                                               | ge<interface speed>-<A>/<B>/<C> |             |
|                   |                                                               |                                 |             |
|                   |                                                               | ncp-<X>.mgmt<Y>                 |             |
|                   |                                                               |                                 |             |
|                   |                                                               | ncf-<X>.mgmt<Y>                 |             |
|                   |                                                               |                                 |             |
|                   |                                                               | ncc-<X>.mgmt<Y>                 |             |
+-------------------+---------------------------------------------------------------+---------------------------------+-------------+


**Example**
::

	dnRouter# clear lldp counters
	dnRouter# clear lldp counters ge100-2/1/1
	dnRouter# clear lldp counters ge100-4/1/2


.. **Help line:** clear lldp counters

**Command History**

+-------------+----------------------------------+
|             |                                  |
| Release     | Modification                     |
+=============+==================================+
|             |                                  |
| 7.0         | Command introduced               |
+-------------+----------------------------------+
|             |                                  |
| 9.0         | Not supported in this version    |
+-------------+----------------------------------+
|             |                                  |
| 10.0        | Command reintroduced             |
+-------------+----------------------------------+

---


## clear flowspec-local-policies counters.rst

clear flowspec-local-policies counters
--------------------------------------

**Minimum user role:** operator

To clear FlowSpec counters:

**Command syntax: clear flowspec-local-policies counters** {[address-family] \| [address-family] match-class [match-class-id]}

**Command mode:** operation

.. **Hierarchies**

**Note**

- Optional parameters must match the order in the command.

- When clearing counters for a specific NRLI, destination, or source prefix, you must specify an address-family.

**Parameter table:**


+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+
|                   |                                                                                                                                                     |                     |             |
| Parameter         | Description                                                                                                                                         | Range               | Default     |
+===================+=====================================================================================================================================================+=====================+=============+
|                   |                                                                                                                                                     |                     |             |
| address-family    | Clears FlowSpec counters only for the specified address-family. When the address-family is not specified, it will apply to   both IPv4 and IPv6.    | IPv4                | both        |
|                   |                                                                                                                                                     |                     |             |
|                   |                                                                                                                                                     | IPv6                |             |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+
|                   |                                                                                                                                                     |                     |             |
| match-class-id    | Clears counters for a specific match-class                                                                                                          | string              | \-          |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+


**Example**
::

	dnRouter# clear flowspec counters
	dnRouter# clear flowspec counters ipv4
	dnRouter# clear flowspec counters ipv4 match-class mc-1
	dnRouter# clear flowspec counters ipv6
    dnRouter# clear flowspec counters ipv6 match-class mc-3

.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 17.0        | Command introduced    |
+-------------+-----------------------+
---

## clear msdp statistics.rst

clear msdp statistics
---------------------

**Minimum user role:** operator

You can use the command to clear MSDP peer statistics. You can use the peer-address command to clear the statistics from a specific peer address.

**Command syntax: clear msdp statistics** peer [peer-address]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+-----------------+---------------------------+------------+-------------+
|                 |                           |            |             |
| Parameter       | Description               | Range      | Default     |
+=================+===========================+============+=============+
|                 |                           |            |             |
| peer-address    | IPv4 Multicast address    | A.B.C.D    | \-          |
+-----------------+---------------------------+------------+-------------+

**Example**
::

  dnRouter# clear msdp statistics


.. *Help line:** Clear MSDP statistics

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 12.0        | Command introduced    |
+-------------+-----------------------+
---

## clear msdp peers.rst

clear msdp peers
----------------

**Minimum user role:** operator

You can use the [peers-address] command to clear a specific peer TCP connection. 

**Command syntax: clear msdp peers** [peer-address]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+-----------------+---------------------------+------------+-------------+
|                 |                           |            |             |
| Parameter       | Description               | Range      | Default     |
+=================+===========================+============+=============+
|                 |                           |            |             |
| peer-address    | IPv4 Multicast address    | A.B.C.D    | \-          |
+-----------------+---------------------------+------------+-------------+


**Example**
::

  dnRouter# clear msdp peers
  dnRouter# clear msdp peers 3.3.3.3

.. **Help line:** Clear MSDP peers TCP connections

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 12.0        | Command introduced    |
+-------------+-----------------------+
---

## clear msdp cache.rst

clear msdp cache
----------------

**Minimum user role:** operator

You can use the command to clear externally learned MSDP Source-Active (SA) cached entries. You can use the group-address command to clear only those cached MSDP SA entries with a specific group address.

**Command syntax: clear msdp cache** group [group-address]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+------------------+------------------------------------------------------------+---------------------------+-------------+
|                  |                                                            |                           |             |
| Parameter        | Description                                                | Range                     | Default     |
+==================+============================================================+===========================+=============+
|                  |                                                            |                           |             |
| group-address    | To clear cached entries from the specific group address    | IPv4 Multicast address    | \-          |
+------------------+------------------------------------------------------------+---------------------------+-------------+


**Example**
::

  dnRouter# clear msdp cache
  dnRouter# clear msdp cache group 227.34.1.23

.. **Help line:** Clear MSDP SA cache

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 12.0        | Command introduced    |
+-------------+-----------------------+
---

## clear pim statistics.rst

clear pim statistics
--------------------

**Minimum user role:** operator

You can use the command to clear PIM statistics for all interfaces. You can clear the PIM statistics for a specific interface using the [interface-name] command.

**Command syntax: clear pim statistics** interface [interface-name]

**Command mode:** operation

.. **Hierarchies**

**Note**

- If the interface is indicated then only the specified interface PIM statistics are cleared.

**Parameter table:**

+-------------------+----------------------------------------------------------------+-----------------------------------------+-------------+
|                   |                                                                |                                         |             |
| Parameter         | Description                                                    | Range                                   | Default     |
+===================+================================================================+=========================================+=============+
|                   |                                                                |                                         |             |
| interface-name    | Clears the statistics for a specific interface (or for all)    | ge{/10/25/40/100}-X/Y/Z                 | none        |
|                   |                                                                |                                         |             |
|                   |                                                                | bundle<bundle-id>                       |             |
|                   |                                                                |                                         |             |
|                   |                                                                | bundle<bundle-id>.<sub-interface-id>    |             |
+-------------------+----------------------------------------------------------------+-----------------------------------------+-------------+

**Example**
::

  dnRouter# clear pim statistics
  dnRouter# clear pim statistics interface bundle-20.222

.. **Help line:** Clear PIM statistics

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 12.0        | Command introduced    |
+-------------+-----------------------+
---

## clear services ethernet-oam connectivity-fault-management auto-discovery.rst

clear services ethernet-oam connectivity-fault-management auto-discovery
------------------------------------------------------------------------

**Minimum user role:** operator

To clear auto-discovered remote MEPs in a connectivity-fault-management service:

**Command syntax: clear services ethernet-oam connectivity-fault-management auto-discovery {maintenance-domain [md-name] maintenance-association [ma-name] | maintenance-domain [md-name] maintenance-association [ma-name] mep-id [remote-mep-id]}**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+----------------+--------------------------------------------------------------------+------------------------------------------+---------+
| Parameter      | Description                                                        | Range                                    | Default |
+================+====================================================================+==========================================+=========+
| md-name        | The name of the Maintenance Domain                                 | String                                   | \-      |
+----------------+--------------------------------------------------------------------+------------------------------------------+---------+
| ma-name        | The name of the Maintenance Association under a Maintenance Domain | String                                   | \-      |
+----------------+--------------------------------------------------------------------+------------------------------------------+---------+
| remote-mep-id  | The identifier of the remote MEP in the Maintenance Association    | 1-8191                                   | \-      |
+----------------+--------------------------------------------------------------------+------------------------------------------+---------+

**Example**
::

	dnRouter# clear services ethernet-oam connectivity-fault-management auto-discovery maintenance-domain MD1 maintenance-association MA1
	dnRouter# clear services ethernet-oam connectivity-fault-management auto-discovery maintenance-domain MD1 maintenance-association MA1 mep-id 3


.. **Help line:** clear CFM auto-discovered remote MEPs

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
---

## clear ldp neighbor statistics.rst

clear ldp neighbor statistics
-----------------------------

**Minimum user role:** operator

To clear the LDP neighbor statistics:

**Command syntax: clear ldp neighbor** [neighbor-address] **statistics**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+---------------------+--------------------------------------------------------+------------+-------------+
|                     |                                                        |            |             |
| Parameter           | Description                                            | Range      | Default     |
+=====================+========================================================+============+=============+
|                     |                                                        |            |             |
| neighbor-address    | Restarts LDP TCP session to a specific LDP neighbor    | A.B.C.D    | \-          |
+---------------------+--------------------------------------------------------+------------+-------------+
|                     |                                                        |            |             |
| statistics          | Clears all LDP neighbor statistics                     | \-         | \-          |
+---------------------+--------------------------------------------------------+------------+-------------+

**Example**
::

	dnRouter# clear ldp neighbor statistics
	dnRouter# clear ldp neighbor 7.7.7.7 statistics


.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 6.0         | Command introduced    |
+-------------+-----------------------+
---

## clear vpws.rst

clear vpws
----------

**Minimum user role:** operator

To manually reset all aspects related to the specified VPWS service, including counters:

**Command syntax: clear vpws** [instance-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table**

+---------------+-------------------------------+--------+---------+
| Parameter     | Description                   | Range  | Default |
+===============+===============================+========+=========+
| instance-name | The configured VPWS instance. | String | \-      |
|               |                               | 1..255 |         |
+---------------+-------------------------------+--------+---------+

**Example**
::

	dnRouter# clear vpws

    dnRouter# clear vpws R15_R16_1


.. **Help line:**

**Command History**

+---------+---------------------------------------------------+
| Release | Modification                                      |
+=========+===================================================+
| 16.1    | Command introduced                                |
+---------+---------------------------------------------------+

---

## clear system ipv4 fragmentation statistics.rst

clear system ipv4 fragmentation statistics
------------------------------------------

**Minimum user role:** operator

Clears all IPv4 fragmentation statistics displayed by the **show system ipv4 fragmentation statistics** command.

To clear ipv4 fragmentation statistics counters:


**Command syntax: clear system ipv4 fragmentation statistics** ncp [ncp-id]

**Command mode:** operation

.. **Hierarchies**

**Note**

When no NCP-id is provided the IPv4 fragmentation statistics of all NCPs are cleared.

**Parameter table**

+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------+
|               |                                                                                                                                                      |           |             |
| Parameter     | Description                                                                                                                                          | Range     | Default     |
+===============+======================================================================================================================================================+===========+=============+
|               |                                                                                                                                                      |           |             |
| ncp-id        | Clears the fragmentation statistics counters for the specified NCP only. If you do not specify an NCP, the counters for all NCPs will be cleared.    | 0..191    | \-          |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------+


**Example**
::

	dnRouter# clear system ipv4 fragmentation statistics ncp 5
	dnRouter# clear system ipv4 fragmentation statistics


.. **Help line:** Clears ipv4 fragmentation statistics displayed by show system ipv4 fragmentation statistics.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.1        | Command introduced    |
+-------------+-----------------------+
---

## clear flowspec counters.rst

clear flowspec counters
-----------------------

**Minimum user role:** operator

To clear FlowSpec counters:

**Command syntax: clear flowspec counters** instance vrf [vrf-name] {[address-family] | [address-family] nlri [nlri] | [address-family] destination [dest-prefix] source [src-prfix]}

**Command mode:** operation

.. **Hierarchies**

**Note**

- Optional parameters must match the order in the command.

- When clearing counters for a specific NRLI, destination, or source prefix, you must specify an address-family.

**Parameter table:**


+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+
|                   |                                                                                                                                                     |                     |             |
| Parameter         | Description                                                                                                                                         | Range               | Default     |
+===================+=====================================================================================================================================================+=====================+=============+
|                   |                                                                                                                                                     |                     |             |
| vrf-name          | Clears FlowSpec counters only for the specified VRF. If not specified, the clear command will apply to the default VRF.                             | string              | default     |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+
|                   |                                                                                                                                                     |                     |             |
| address-family    | Clears FlowSpec counters only for the specified address-family. When the address-family is not specified, it will apply to   both IPv4 and IPv6.    | IPv4                | both        |
|                   |                                                                                                                                                     |                     |             |
|                   |                                                                                                                                                     | IPv6                |             |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+
|                   |                                                                                                                                                     |                     |             |
| nlri              | Clears counters for a specific flow                                                                                                                 | string              | \-          |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+
|                   |                                                                                                                                                     |                     |             |
| dest-prefix       | Clears counters for all destinations matching the specified destination prefix.                                                                     | A.B.C.D/M           | \-          |
|                   |                                                                                                                                                     |                     |             |
|                   |                                                                                                                                                     | xx:xx::xx:xx/O-M    |             |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+
|                   |                                                                                                                                                     |                     |             |
| src-prefix        | Clears counters for all sources matching the specified source prefix                                                                                | A.B.C.D/M           | \-          |
|                   |                                                                                                                                                     |                     |             |
|                   |                                                                                                                                                     | xx:xx::xx:xx/O-M    |             |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+


**Example**
::

	dnRouter# clear flowspec counters
	dnRouter# clear flowspec counters ipv4
	dnRouter# clear flowspec counters ipv4 nlri "DstPrefix:=50.0.0.0/8,SrcPrefix:=50.1.2.3/32,Protocol:=5,DstPort:<9&>6|=12,SrcPort:=50|=30,Dscp:=5"
	dnRouter# clear flowspec counters ipv4 destination 50.0.0.0/8
	dnRouter# clear flowspec counters ipv4 source 50.1.2.3/24
	dnRouter# clear flowspec counters ipv4 destination 50.0.0.0/8 source 50.1.2.3/24
	dnRouter# clear flowspec ipv6 destination 2011:11:100:1::/8-64


.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.0        | Command introduced    |
+-------------+-----------------------+
---

## clear interfaces dampening penalty.rst

clear interfaces dampening penalty
----------------------------------

**Minimum user role:** operator

This clear action returns the penalty value to zero. This action always results in bringing the interface back up if it is down because of dampening.

To clear the interface dampening penalty:

**Command syntax: clear interfaces dampening penalty** [interface-name]

**Command mode:** operation

.. **Hierarchies**

**Note**

Clearing the penalty parameter will always result in bringing the interface up if the reason it is down is dampening.

.. - **Clear interfaces dampening** - clears dampening penalty value to zero for **ALL** interfaces

.. - **Clear interfaces dampening interface x** - clears dampening penalty value to zero for a specific interface.

**Parameter table:**

+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+-------------+
|                   |                                                                                                                                                        |                                 |             |
| Parameter         | Description                                                                                                                                            | Range                           | Default     |
+===================+========================================================================================================================================================+=================================+=============+
|                   |                                                                                                                                                        | ge<interface speed>-<A>/<B>/<C> | \-          |
| interface-name    | Clears the penalty value for a specific interface only. If an interface-name is not specified, the penalty value is cleared for all interfaces.        |                                 |             |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+-------------+

**Example**
::

	dnRouter# clear interfaces dampening penalty
	dnRouter# clear interfaces dampening penalty ge100-1/0/1


.. **Help line:** clear interface dampening penalty

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.4        | Command introduced    |
+-------------+-----------------------+
---

## clear services flow-monitoring sflow counters.rst

clear services flow-monitoring sflow counters
---------------------------------------------

**Minimum user role:** operator

To clear the flow-monitoring sflow counters:

**Command syntax: clear services flow-monitoring sflow counters**  ncp [ncp-id]

**Command mode:** operation

.. **Hierarchies**

..**Note**

 - "clear services flow-monitoring sflow counters" without parameter, clears counters on all NCPs.

**Parameter table:**

+-----------+-----------------------------------------------------------------------+--------+-------------+
| Parameter | Description                                                           | Range  |             |
|           |                                                                       |        | Default     |
+===========+=======================================================================+========+=============+
| ncp-id    | Clears the flow-monitoring sflow counters from the specified NCP only | 0..255 | \-          |
+-----------+-----------------------------------------------------------------------+--------+-------------+


**Example**
::

	dnRouter# clear services flow-monitoring sflow counters ncp 5


.. **Help line:** clear flow-monitoring sflow counters.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
| 25.1        | Command introduced    |
+-------------+-----------------------+
---

## clear ospf process.rst

clear ospf process
------------------

**Minimum user role:** operator

To clear the entire OSPF database and restart the adjacencies:

**Command syntax: clear ospf** instance [ospf-instance-name] **process**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

	- use "instance [ospf-instance-name]" to clear information from a specific OSPF instance, when not specified, clear information from all OSPF instances

**Parameter table:**

+--------------------+----------------------------------------------------------------+---------------------------------------+-------------+
|                    |                                                                |                                       |             |
| Parameter          | Description                                                    | Range                                 | Default     |
+====================+================================================================+=======================================+=============+
| ospf-instance-name | clears the ospf information for the specified instance         | configured instances names            | all         |
+--------------------+----------------------------------------------------------------+---------------------------------------+-------------+

**Example**
::

	dnRouter# clear ospf process
	dnRouter# clear ospf instance instance1 process

.. **Help line:** Clear OSPF process

**Command History**

+-------------+------------------------+
|             |                        |
| Release     | Modification           |
+=============+========================+
|             |                        |
| 11.6        | Command introduced     |
+-------------+------------------------+
| 18.1        | Add instance parameter |
+-------------+------------------------+

---

## clear services ethernet-oam connectivity-fault-management statistics.rst

clear services ethernet-oam connectivity-fault-management statistics
--------------------------------------------------------------------

**Minimum user role:** operator

To clear the ethernet OAM 802.1ag connectivity-fault-management service counters:

**Command syntax: clear services ethernet-oam connectivity-fault-management statistics {[interface-name] | maintenance-domain [md-name] | maintenance-domain [md-name] maintenance-association [ma-name] | maintenance-domain [md-name] maintenance-association [ma-name] mep-id [local-mep-id] | all}**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+----------------+--------------------------------------------------------------------+------------------------------------------+---------+
| Parameter      | Description                                                        | Range                                    | Default |
+================+====================================================================+==========================================+=========+
| interface-name | Clears ethernet OAM CFM statistics for a specific interface        | geX-<f>/<n>/<p>                          | \-      |
|                |                                                                    | geX-<f>/<n>/<p>[.<sub-interface id>]     |         |
|                |                                                                    | bundle-<bundle id>                       |         |
|                |                                                                    | bundle-<bundle id>[.<sub-interface id>]  |         |
+----------------+--------------------------------------------------------------------+------------------------------------------+---------+
| md-name        | The name of the Maintenance Domain                                 | String                                   | \-      |
+----------------+--------------------------------------------------------------------+------------------------------------------+---------+
| ma-name        | The name of the Maintenance Association under a Maintenance Domain | String                                   | \-      |
+----------------+--------------------------------------------------------------------+------------------------------------------+---------+
| local-mep-id   | The identifier of the local MEP in the Maintenance Association     | 1-8191                                   | \-      |
+----------------+--------------------------------------------------------------------+------------------------------------------+---------+
| all            | Clears all ethernet OAM CFM statistics in the system               | \-                                       | \-      |
+----------------+--------------------------------------------------------------------+------------------------------------------+---------+

**Example**
::

	dnRouter# clear services ethernet-oam connectivity-fault-management statistics ge100-0/0/19
	dnRouter# clear services ethernet-oam connectivity-fault-management statistics maintenance-domain MD1
	dnRouter# clear services ethernet-oam connectivity-fault-management statistics maintenance-domain MD1 maintenance-association MA1
	dnRouter# clear services ethernet-oam connectivity-fault-management statistics maintenance-domain MD1 maintenance-association MA1 mep-id 3
	dnRouter# clear services ethernet-oam connectivity-fault-management statistics all


.. **Help line:** clear 802.1ag CFM statistics

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.1    | Command introduced |
+---------+--------------------+
---

## clear system npu-resources counters.rst

clear system npu-resources counters
-----------------------------------

**Minimum user role:** operator

Clear system NPU resources counters.

**Command syntax: clear system npu-resources counters** resource-type [resource-type] ncp [ncp-id]

**Command mode:** operation

.. **Hierarchies**

**Note**

- If ncp-id is specified, only the system NPU resources counters of the NCP with specified id are cleared. Otherwise system resources counters of all NCPs are cleared.

- If resource-type is specified, only the system NPU resources counters for the specified resource type are cleared. For resources that are per NCP, if ncp-id is also specified, then only the applicable counters are cleared.


**Parameter table**

+---------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
| Parameter     | Description                                                                                                                           | Range                                    |
+===============+=======================================================================================================================================+==========================================+
| ncp-id        | Clear the counters for the specified NCP only. If you do not specify an NCP, the NPU resources counters for all NCPs will be cleared. | 0..max number of NCP per cluster type -1 |
+---------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
| resource-type | Clear the counters for the specified resource only.                                                                                   | shared-buffer                            |
|               |                                                                                                                                       | mtu-profiles                             |
|               |                                                                                                                                       | traffic-utilization                      |
+---------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+


**Example**
::

	dnRouter# clear system npu-resources counters
	dnRouter# clear system npu-resources counters ncp 1
	dnRouter# clear system npu-resources counters resource-type flowspec
	dnRouter# clear system npu-resources counters ncp 2 resource-type shared-buffer


.. **Help line:** clear system NPU resources counters

**Command History**

+-------------+-------------------------------------------------------------------+
| Release     | Modification                                                      |
+=============+===================================================================+
| 11.4        | Command introduced                                                |
+-------------+-------------------------------------------------------------------+
| 19.1        | Command renamed and additional filter per resource-type was added |
+-------------+-------------------------------------------------------------------+
---

## clear interfaces clock ptp counters.rst

clear interfaces clock ptp counters
-----------------------------------

**Minimum user role:** operator

Clearing the interface PTP port counters resets the counters to zero and removes the counter information from the database.

To clear the interface counters:

**Command syntax: clear interfaces clock ptp counters [interface-name]**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. **Parameter table:**

**Example**
::

	dnRouter# clear interfaces clock ptp counters
	dnRouter# clear interfaces clock ptp counters ge400-1/1/1
	dnRouter# clear interfaces clock ptp counters ge400-1/1/1.134


.. **Help line:** clear clock ptp port counters

**Command History**

+-------------+---------------------------------------+
|             |                                       |
| Release     | Modification                          |
+=============+=======================================+
| 18.0        | Command introduced                    |
+-------------+---------------------------------------+

---

## clear rsvp statistics packets.rst

clear rsvp statistics packets
-----------------------------

**Minimum user role:** operator

To clear RSVP packet statistics:

**Command syntax: clear rsvp statistics packets** interface [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+---------------+---------------------------------------------------------------------------------------------------------+----------------------------------------------------+-------------+
|               |                                                                                                         |                                                    |             |
| Parameter     | Description                                                                                             | Range                                              | Default     |
+===============+=========================================================================================================+====================================================+=============+
| interface-name| Clear packet statistics from the specified interface only. Applicable to configured MPLS-TE interfaces. | configured mpls-te interface name.                 | \-          |
|               |                                                                                                         |                                                    |             |
|               |                                                                                                         | ge{/10/25/40/100}-X/Y/Z                            |             |
|               |                                                                                                         |                                                    |             |
|               |                                                                                                         | ge<interface speed>-<A>/<B>/<C>.<sub-interface id> |             |
|               |                                                                                                         |                                                    |             |
|               |                                                                                                         | bundle-<bundle-id>                                 |             |
|               |                                                                                                         |                                                    |             |
|               |                                                                                                         | bundle-<bundle-id.sub-bundle-id>                   |             |
+---------------+---------------------------------------------------------------------------------------------------------+----------------------------------------------------+-------------+


**Example**
::

	dnRouter# clear rsvp statistics packets
	dnRouter# clear rsvp statistics packets bundle-2


.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+
---

## clear mpls traffic-engineering pcep counters.rst

clear mpls traffic-engineering pcep counters
--------------------------------------------

**Minimum user role:** operator

To reset PCEP session counters:

**Command syntax: clear mpls traffic-engineering pcep counters** peer [ipv4-address]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - set "peer [ipv4-address]" to reset counters for a specific peer


**Parameter table:**

+-----------------+----------------------------------------------------+-----------+-------------+
|                 |                                                    |           |             |
| Parameter       | Description                                        | Range     | Default     |
+=================+====================================================+===========+=============+
|                 |                                                    | A.B.C.D   |             |
| ipv4-address    | Clear PCEP counters for the specified peer only    |           | \-          |
+-----------------+----------------------------------------------------+-----------+-------------+

**Example**
::

	dnRouter# clear mpls traffic-engineering pcep counters 
	dnRouter# clear mpls traffic-engineering pcep counters peer 1.1.1.1



**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 10.0        | Command introduced    |
+-------------+-----------------------+
---

## clear interfaces dhcp relay statistics.rst

clear interfaces dhcp relay statistics
--------------------------------------

**Minimum user role:** operator

Clearing the interface DHCP relay statistics resets the counters to zero and removes the counter information from the database.

To clear the interface DHCP relay statistics:

**Command syntax: clear interfaces dhcp relay statistics** [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. - **Clear interfaces dhcp relay statistics** - clears DHCP relay counters for **ALL** interfaces.

.. - **Clear interfaces dhcp relay statistics interface-name** - clears DHCP relay counters for the specified interface.

**Parameter table:**

+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+-------------+
| Parameter         | Description                                                                                                                                            | Range                                             | Default     |
+===================+========================================================================================================================================================+===================================================+=============+
| interface-name    | Clears the DHCP relay counters for the specified interface only. If an interface-name is not specified, the counters are cleared for all interfaces.   | ge<interface speed>-<A>/<B>/<C>                   | \-          |
|                   |                                                                                                                                                        | ge<interface speed>-<A>/<B>/<C>.<sub-interface-id>|             |
|                   |                                                                                                                                                        | bundle-<bundle-id>                                |             |
|                   |                                                                                                                                                        | bundle-<bundle-id>.<sub-interface-id>             |             |
|                   |                                                                                                                                                        | irbX                                              |             |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+-------------+


**Example**
::

	dnRouter# clear interfaces dhcp relay statistics
	dnRouter# clear interfaces dhcp relay statistics ge100-0/0/0

.. **Help line:** Clear interface DHCP relay counters

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 18.0        | Command introduced    |
+-------------+-----------------------+

---

## clear telemetry counters.rst

clear telemetry counters
------------------------

**Minimum user role:** operator

To clear telemetry dial-out counters for each specific destination and/or destination-profile and/or subscription and/or system:

**Command syntax: clear grpc counters** [subscription <subscription-id>] [destination-profile <destination-profile-id>] [ip <ip>] [port <port>]

**Command mode:** operation

.. **Hierarchies**

**Note**

- A command without a specific parameter clears the counters for all subscriptions and destinations in the system.


**Parameter table:**

+------------------------+--------------------------------------------+--------------------+
| Parameter              |        Description                         |   Range            |
+========================+============================================+====================+
| subscription-id        | The ID of the specific subscription        | 1..255 characters  |
+------------------------+--------------------------------------------+--------------------+
| destination-profile-id | The ID of the specific destination-profile | 1..255 characters  |
+------------------------+--------------------------------------------+--------------------+
| ip                     | The IP address of destination              | A.B.C.D            |
|                        |                                            | xx:xx::xx:xx       |
+------------------------+--------------------------------------------+--------------------+
| port                   | The destination port                       | 0..65535           |
+------------------------+--------------------------------------------+--------------------+

**Example**
::

	dnRouter# clear telemetry counters
	dnRouter# clear telemetry counters subscription-id dev-subscription
	dnRouter# clear telemetry counters subscription-id dev-subscription destination-profile Development
	dnRouter# clear telemetry counters destination-profile Development
	dnRouter# clear telemetry counters subscription-id dev-subscription destination-profile Development destination-ip 10.0.0.1 destination-port 62000



**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
| 19.10       | Command introduced    |
+-------------+-----------------------+

---

## clear evpn mac-suppression.rst

clear evpn mac-suppression
--------------------------

**Minimum user role:** operator

To remove the suppression of an evpn service instance mac-address(es):

**Command syntax: clear evpn mac-suppression** {service [instance-name] mac [mac-address]}

**Command mode:** operation

.. **Hierarchies**


**Parameter table**

+---------------+-------------------------------+------------+---------+
| Parameter     | Description                   | Range      | Default |
+===============+===============================+============+=========+
| instance-name | The configured evpn instance. | String     | \-      |
|               |                               | 1..255     |         |
+---------------+-------------------------------+------------+---------+
| mac-address   | The specific mac-address      | String     |         |
+---------------+-------------------------------+------------+---------+

**Example**
::

	dnRouter# clear evpn mac-suppression service evpn1 mac  a2:76:b0:08:9e:02


.. **Help line:**

**Command History**

+---------+---------------------------------------------------+
| Release | Modification                                      |
+=========+===================================================+
| 18.3    | Command introduced                                |
+---------+---------------------------------------------------+

---

## clear interfaces management counters.rst

clear interfaces management counters
------------------------------------

**Minimum user role:** operator

To clear counter information relating to management interfaces:

**Command syntax: clear interfaces management counters** [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. - **Clear interfaces management counters** - clears all counters for **ALL** interfaces

.. - **Clear interfaces management counters interface x** - clears all counters for a specific interface.


**Parameter table:**

+-------------------+-----------------------------------------------------------------+-----------+-------------+
|                   |                                                                 |           |             |
| Parameter         | Description                                                     | Range     | Default     |
+===================+=================================================================+===========+=============+
|                   |                                                                 | String    | \-          |
| interface-name    | Clears counter information from the specified interface only    |           |             |
+-------------------+-----------------------------------------------------------------+-----------+-------------+


**Example**
::

	dnRouter# clear interfaces management counters
	dnRouter# clear interfaces management counters mgmt0
	dnRouter# clear interfaces management counters mgmt-ncc-0



.. **Help line:** clear control interface counters

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+
---

## clear rib-manager fpm statistics.rst

clear rib-manager fpm statistics
--------------------------------

**Minimum user role:** operator

To clear forwarding path manager statistics:

**Command syntax: clear rib-manager fpm statistics**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. **Parameter table:**

**Example**
::

	dnRouter# clear rib-manager fpm statistics
	

.. **Help line:** Clear Forwarding Path Manager statistics

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 6.0         | Command introduced    |
+-------------+-----------------------+
---

## clear grpc session.rst

clear grpc session
------------------

**Minimum user role:** operator

To kill gRPC sessions:

**Command syntax: clear grpc session** [session-id]

**Command mode:** operation

.. **Hierarchies**

**Note**

- A command without a specific session-id clears counters per all active sessions and per system.


**Parameter table:**

+------------+--------------------------------+---------------+--------------+
| Parameter  |        Description             |   Range       |Default value |
+============+================================+===============+==============+
| session-id | The id of the specific session | 1..65535      | \-           |
+------------+--------------------------------+---------------+--------------+

**Example**
::


	dnRouter# clear grpc session
	dnRouter# clear grpc session 776


.. **Help line:** kill specific active or all active grpc sessions.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.2        | Command introduced    |
+-------------+-----------------------+
---

## clear system diagnostics counters test component.rst

clear system diagnostics counters test component
------------------------------------------------

**Minimum user role:** operator

Clears all system diagnostics counters per component or per component id.

**Command syntax: clear system diagnostics counters test [test-type] component [component-type]** [component-id]

**Command mode:** operation

.. **Hierarchies**

**Note**

- When component-id is specified, only the specified component-ids counters are cleared. Otherwise all system diagnostics counters per component-type are cleared.


**Parameter table**

+-------------------+--------------------------+--------------------------+-------------------+
|                   |                          |                          |                   |
| Parameter         | Description              | Value                    | Default           |
+===================+==========================+==========================+===================+
|                   |                          |                          |                   |
| test-type         | The type of test.        | punt-datapath            | \-                |
|                   |                          |                          |                   |
+-------------------+--------------------------+--------------------------+-------------------+
|                   |                          |                          |                   |
| component-type    | The type of component.   | ncp                      | all               |
|                   |                          |                          |                   |
+-------------------+--------------------------+--------------------------+-------------------+
|                   |                          |                          |                   |
| component-id      | The id of the component. | any legal ncp-id, all    | all               |
|                   |                          |                          |                   |
+-------------------+--------------------------+--------------------------+-------------------+


**Example**
::

	dnRouter# clear system diagnostics counters test punt-datapath
	dnRouter# clear system diagnostics counters

.. **Help line:** diagnostics component id counters to be cleared.

**Command History**

+-------------+------------------------------------+
|             |                                    |
| Release     | Modification                       |
+=============+====================================+
|             |                                    |
| 13.1        | Command introduced                 |
+-------------+------------------------------------+
---

## clear interfaces dampening counters.rst

clear interfaces dampening counters
-----------------------------------

**Minimum user role:** operator

This clear action returns the penalty value to zero. This action always results in bringing the interface back up if it is down because of dampening.

To clear the interface dampening counters:

**Command syntax: clear interfaces dampening counters** [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. - **Clear interfaces dampening** - clears dampening counters for **ALL** interfaces

.. - **Clear interfaces dampening interface x** - clears dampening counters value to zero for a specific interface.

**Parameter table:**

+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+-------------+
|                   |                                                                                                                                                        |                                 |             |
| Parameter         | Description                                                                                                                                            | Range                           | Default     |
+===================+========================================================================================================================================================+=================================+=============+
|                   |                                                                                                                                                        | ge<interface speed>-<A>/<B>/<C> | \-          |
| interface-name    | Clears the dampening counters for a specific interface only. If an interface-name is not specified, the counters are cleared for all interfaces.       |                                 |             |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+-------------+



**Example**
::

	dnRouter# clear interfaces dampening counters
	dnRouter# clear interfaces dampening counters ge100-1/0/1

.. **Help line:** Clear interface dampening counters

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.4        | Command introduced    |
+-------------+-----------------------+
---

## clear interfaces control counters.rst

clear interfaces control counters
---------------------------------

**Minimum user role:** operator

To clear counter information relating to control interfaces:

**Command syntax: clear interfaces control counters** [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. - **Clear interfaces dampening** - clears all counters for **ALL** interfaces

.. - **Clear interfaces dampening interface x** - clears **ALL** counters for a specific interface.

**Parameter table:**

+-------------------+-----------------------------------------------------------------+------------------+-------------+
|                   |                                                                 |                  |             |
| Parameter         | Description                                                     | Range            | Default     |
+===================+=================================================================+==================+=============+
|                   |                                                                 |                  | \-          |
| interface-name    | Clears counter information from the specified interface only    | ctrl-ncf-x/y     |             |
|                   |                                                                 |                  |             |
|                   |                                                                 | ctrl-ncp-x/y     |             |
|                   |                                                                 |                  |             |
|                   |                                                                 | ctrl-ncc-x/y     |             |
|                   |                                                                 |                  |             |
|                   |                                                                 | ctrl-ncm-Ax/y    |             |
|                   |                                                                 |                  |             |
|                   |                                                                 | ctrl-ncm-Bx/y    |             |
+-------------------+-----------------------------------------------------------------+------------------+-------------+

**Example**
::

	dnRouter# clear interfaces control counters
	dnRouter# clear interfaces control counters ctrl-ncf-0/0


.. **Help line:** clear control interface counters

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+
---

## clear grpc sessions history.rst

clear grpc session history
--------------------------

**Minimum user role:** operator

To clear the list of terminated grpc sessions:

**Command syntax: clear grpc session history** 

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. **Parameter table:**

**Example**
::

	dnRouter# clear grpc session history


.. **Help line:** clear the list of terminated grpc sessions.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.0        | Command introduced    |
+-------------+-----------------------+
---

## clear system diagnostics counters.rst

clear system diagnostics counters
---------------------------------

**Minimum user role:** operator

You can use this command to clear all the counters for online diagnostics test results.

Supports clearing the following counters:

•	Packets Sent
•	Packets Lost
•	Last Fail Time
•	Last Uptime
•	Test Uptime
•	Test Fails.



**Command syntax: clear system diagnostics counters** test [test-type]

**Command mode:** operation

.. **Hierarchies**

**Note**

When test is specified, only the specific test counters are cleared. Otherwise all system diagnostics counters are cleared.

**Parameter table**

+---------------+--------------------+------------------+-------------------+
|               |                    |                  |                   |
| Parameter     | Description        | Value            | Default           |
+===============+====================+==================+===================+
|               |                    |                  |                   |
| test-type     | The type of test   | punt-datapath    | \-                |
|               |                    |                  |                   |
+---------------+--------------------+------------------+-------------------+


**Example**
::

	dnRouter# clear system diagnostics counters
	dnRouter# clear system diagnostics counters test punt-datapath


.. **Help line:** the type of the test

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.1        | Command introduced    |
+-------------+-----------------------+
---

## clear mpls statistics route p2mp.rst

clear mpls statistics route p2mp
--------------------------------

**Minimum user role:** operator

To clear MPLS P2MP routes counters:

**Command syntax: clear mpls statistics route p2mp**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - Clears all the MPLS P2MP routes counters.

.. **Parameter table:**


**Example**
::

	dnRouter# clear mpls statistics route p2mp


.. **Help line:** Clears MPLS P2MP routes counters.

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 17.1        | Command introduced    |
+-------------+-----------------------+
---

## clear interfaces management access-list.rst

clear interface management access-list
-------------------------------------------------------------------

**Minimum user role:** operator

To remove management physical interface access-list

**Command syntax: clear interfaces management [interface-name] access-list [access-list-type] direction [direction]**

**Command mode:** operation

.. **Note:**


**Parameter table:**

+------------------+---------------------------------------+-------+---------+
| Parameter        | Values                                | Range | Default |
+==================+=======================================+=======+=========+
| interface-name   | mgmt-ncc-0, mgmt-ncc-1                |       | \-      |
+------------------+---------------------------------------+-------+---------+
| access-list-type | ipv4/ipv6                             |       | \-      |
+------------------+---------------------------------------+-------+---------+
| direction        | in                                    |       | \-      |
+------------------+---------------------------------------+-------+---------+


**Example:**
::

	dnRouter# clear interfaces management mgmt-ncc-0 access-list ipv4 direction in
	

.. **Help line:** Clear static route on management physical

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 16.2        | Command introduced    |
+-------------+-----------------------+

---

## clear interfaces clock esmc counters.rst

clear interfaces clock esmc counters
------------------------------------

**Minimum user role:** operator

Clearing the interface SyncE ESMC counters resets the counters to zero and removes the counter information from the database.

To clear the interface counters:

**Command syntax: clear interfaces clock esmc counters [interface-name]**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. **Parameter table:**

**Example**
::

	dnRouter# clear interfaces clock esmc counters
	dnRouter# clear interfaces clock esmc counters ge400-1/1/1
	dnRouter# clear interfaces clock esmc counters ge400-1/1/1.134


.. **Help line:** clear clock esmc counters

**Command History**

+-------------+---------------------------------------+
|             |                                       |
| Release     | Modification                          |
+=============+=======================================+
| 17.2        | Command introduced                    |
+-------------+---------------------------------------+

---

## clear rsvp statistics errors.rst

clear rsvp statistics errors
----------------------------

**Minimum user role:** operator

To clear RSVP error statistics:

**Command syntax: clear rsvp statistics errors** interface [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+----------------+--------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| Parameter      | Description                                                                                            | Range                                              | Default |
+================+========================================================================================================+====================================================+=========+
| interface-name | clear error statistics from the specified interface only. Applicable to configured MPLS-TE interfaces. | configured mpls-te interface name.                 | \-      |
|                |                                                                                                        |                                                    |         |
|                |                                                                                                        | ge{/10/25/40/100}-X/Y/Z                            |         |
|                |                                                                                                        |                                                    |         |
|                |                                                                                                        | ge<interface speed>-<A>/<B>/<C>.<sub-interface id> |         |
|                |                                                                                                        |                                                    |         |
|                |                                                                                                        | bundle-<bundle-id>                                 |         |
|                |                                                                                                        |                                                    |         |
|                |                                                                                                        | bundle-<bundle-id.sub-bundle-id>                   |         |
+----------------+--------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+


**Example**
::

	dnRouter# clear rsvp statistics errors
	dnRouter# clear rsvp statistics errors bundle-2


.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+
---

## clear interfaces management ipv6-address.rst

clear interface management ipv6-address
-------------------------------------------------------------------

**Minimum user role:** operator


To remove the ipv6-address from the management bond interface:


**Command syntax: clear interfaces management [interface-name] ipv6-address**

**Command mode:** operator

.. **Note:**


**Parameter table:**

+------------------+----------------------------------------------+-------+-------+
| Parameter        | Values                                       | Range | Value |
+==================+==============================================+=======+=======+
| interface-name   | mgmt-ncc-0, mgmt-ncc-1                       |       | \-    |
+------------------+----------------------------------------------+-------+-------+


**Example:**
::

	dnRouter# clear interfaces management mgmt-ncc-0 ipv6-address
	

.. **Help line:** Remove ipv6-address address from management bond interface


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 16.2        | Command introduced    |
+-------------+-----------------------+

---

## clear services flow-monitoring exporter counters.rst

clear services flow-monitoring exporter counters
------------------------------------------------------------

**Minimum user role:** operator

To clear the flow-monitoring cache counters:

**Command syntax: clear services flow-monitoring exporter counters**  ncp [ncp-id] exporter-profile [exporter-profile]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - "clear services flow-monitoring export counters" without parameter, clears counters for exported profiles on all NCPs.


**Parameter table:**

+------------------+--------------------------------------------------------------------------------------+-----------------------------------+-------------+
| Parameter        | Description                                                                          | Range                             |             |
|                  |                                                                                      |                                   | Default     |
+==================+======================================================================================+===================================+=============+
| ncp-id           | Clears the flow-monitoring exporter counters from the specified NCP only             | 0..255                            | \-          |
+------------------+--------------------------------------------------------------------------------------+-----------------------------------+-------------+
| exporter-profile | Clears the flow-monitoring exporter counters for the specified exporter profile only | An existing exporter-profile name | \-          |
+------------------+--------------------------------------------------------------------------------------+-----------------------------------+-------------+

**Example**
::

	dnRouter# clear services flow-monitoring exporter counters ncp 5 

	dnRouter# clear services flow-monitoring exporter counters ncp 5 export-profile myExporter


.. **Help line:** clear counters for exported flows by flow-monitoring.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.4        | Command introduced    |
+-------------+-----------------------+
---

## clear isis process.rst

clear isis process
------------------

**Minimum user role:** operator

To clear the IS-IS database and reset IS-IS adjacencies:

**Command syntax: clear isis** instance [isis-instance-name] **process**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - use "instance [isis-instance-name]" to clear from a specific ISIS instance


**Parameter table:**

+-----------------------+--------------------------------------------------------------------+---------------------+-------------+
|                       |                                                                    |                     |             |
| Parameter             | Description                                                        | Range               | Default     |
+=======================+====================================================================+=====================+=============+
|                       |                                                                    |                     |             |
| no parameter          | Clear the entire IS-IS database                                    | \-                  | \-          |
+-----------------------+--------------------------------------------------------------------+---------------------+-------------+
|                       |                                                                    |                     | \-          |
| isis-instance-name    | Clear IS-IS neighbor adjacencies for the specified IS-IS instance  | 1..255 characters   |             |
+-----------------------+--------------------------------------------------------------------+---------------------+-------------+


**Example**
::

	dnRouter# clear isis process
	dnRouter# clear isis process ISIS_A process

.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 9.0         | Command introduced    |
+-------------+-----------------------+

---

## clear lfs counters.rst

clear lfs counters
------------------

**Minimum user role:** operator

To clear the link fault signaling counters:

**Command syntax: clear lfs counters** [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - clear lfs counters** clears all LFS counters


**Parameter table:**

+-------------------+---------------------------------------------------------------+----------------------------------+-------------+
|                   |                                                               |                                  |             |
| Parameter         | Description                                                   | Range                            | Default     |
+===================+===============================================================+==================================+=============+
|                   |                                                               |                                  |             |
| interface-name    | Clears the LFS counters from the specified interface only.    | ge<interface speed>-<A>/<B>/<C>  | \-          |
+-------------------+---------------------------------------------------------------+----------------------------------+-------------+


**Example**
::

	dnRouter# clear lfs counters
	dnRouter# clear lfs counters ge400-2/0/3


.. **Help line:** Clear 100GE and 400GE and other physical interfaces link fault signaling statistics

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.2        | Command introduced    |
+-------------+-----------------------+
---

## clear twamp session.rst

clear twamp session
-------------------

**Minimum user role:** operator

The clear twamp session command enables to terminate TWAMP sessions. The termination command operates on control sessions, which also terminates all associated data sessions.

To clear active TWAMP sessions:

**Command syntax: clear twamp session** [connection-id]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - clear twamp statistics, by default command clears all twamp statistics for all sessions. Connection-id applies to control session, Session-id applies for data sessions. Clearing control connection-id does not clear statistics of its respective data sessions. In order to clear data session-id, user must mention the control connection-id.

 - session id as seen in show services twamp session

**Parameter table**

+------------------+---------------------------------------------------------------------+------------------------------------------------------------------+-------------------+
|                  |                                                                     |                                                                  |                   |
| Parameter        | Description                                                         | Value                                                            | Default           |
+==================+=====================================================================+==================================================================+===================+
|                  |                                                                     | Available control session ID. See "show services twamp sessions" |                   |
| connection-id    | Terminates only the TWAMP session that matches the specified ID     |                                                                  | \-                |
+------------------+---------------------------------------------------------------------+------------------------------------------------------------------+-------------------+

**Example**
::

	dnRouter# clear twamp session 57
	TWAMP control session 57 was successfully terminated

	dnRouter# clear twamp session

	TWAMP control session 57 was successfully terminated
	TWAMP control session 58 was successfully terminated


.. **Help line:** Clear active twamp session

**Command History**

+-------------+---------------------------------------------+
|             |                                             |
| Release     | Modification                                |
+=============+=============================================+
|             |                                             |
| 11.2        | Command introduced                          |
+-------------+---------------------------------------------+
---

## clear ber counters.rst

clear ber counters
------------------

**Minimum user role:** operator

To clear the bit error rate counters:

**Command syntax: clear ber counters** [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**
 - clear ber counters** clears all BER counters

**Parameter table:**

+-------------------+---------------------------------------------------------------+--------------------------------+-------------+
| Parameter         | Description                                                   | Range                          | Default     |
+===================+===============================================================+================================+=============+
| interface-name    | Clears the BER counters from the specified interface only.    | ge<interface speed>-<A>/<B>/<C>| \-          |
+-------------------+---------------------------------------------------------------+--------------------------------+-------------+


**Example**
::

	dnRouter# clear ber counters
	dnRouter# clear ber counters ge400-2/0/3


.. **Help line:** Clear 400GE and 100GE physical interfaces with FEC BER signaling statistics

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 17.2        | Command introduced    |
+-------------+-----------------------+

---

## clear multicast route statistics.rst

clear multicast route statistics
--------------------------------

**Minimum user role:** operator

You can use this command to clear the statistics of (S,G) MFIB entries in the multicast route (by source address or group address).

**Command syntax: clear multicast route statistics** group [group-address] source [source-address]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - Using group [group-address] option clears the statistics of (S,G) multicast route entries with the related G = group address.

 - Using source [source-address] option clears the statistics of (S,G) multicast route entries with the related S = source address.

 - Using group [group-address] source [source-address] options clears the statistics of multicast route entries with S = source-address and G = group-address.


**Parameter table:**

+-------------------+------------------------------------+-----------+-------------+
|                   |                                    |           |             |
| Parameter         | Description                        | Range     | Default     |
+===================+====================================+===========+=============+
|                   |                                    |           |             |
| group-address     | The multicast group IP address     | IPv4      | \-          |
+-------------------+------------------------------------+-----------+-------------+
|                   |                                    |           |             |
| source-address    | The multicast source IP address    | IPv4      | \-          |
+-------------------+------------------------------------+-----------+-------------+


**Example**
::

	dnRouter# clear multicast route statistics
	dnRouter# clear multicast route statistics group 227.2.3.4
	dnRouter# clear multicast route statistics source 12.2.43.12
	dnRouter# clear multicast route statistics group 227.2.3.4 source 12.2.43.12


.. **Help line:** Clear multicast route statistics

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 12.0        | Command introduced    |
+-------------+-----------------------+
---

## clear event-manager counters policy-type.rst

clear event-manager counters policy-type
----------------------------------------

**Minimum user role:** operator

Use this command to clear all policy counters, or the counters for a specific policy type.

**Command syntax: clear event-manager counters policy-type [policy-type]** policy-name [policy-name]

**Command mode:** operation

.. **Hierarchies**

**Note**

- When the policy-name is specified the command clears all policy counters per policy-type per policy name.

- clear event-manager counters policy-type - clears all policy counters per policy type, for the following policy types:

  - event-policy - policy that will be executed upon matching trigger of registered system event.
 
  - periodic-policy - a recurrent policy according to the scheduled configuration, with limited execution time.
 
  - generic-policy - policy that will be executed only once and unlimited in execution time.

**Parameter table**

+----------------+-----------------------+-------------------+---------+
|                |                       |                   | Default |
| Parameter      | Description           | Range             |         |
+================+=======================+===================+=========+
|                |                       |                   | \ -     |
| policy-type    | The type of policy    | event-policy      |         |
|                |                       |                   |         |
|                |                       | periodic-policy   |         |
|                |                       |                   |         |
|                |                       | generic-policy    |         |
+----------------+-----------------------+-------------------+---------+


**Example**
::

    dnRouter# clear event-manager counters policy-type periodic-policy
    dnRouter# clear event-manager counters policy-type generic-policy policy-name test



.. **Help line:** insert the policy-name who's counters shall be cleared.

**Command History**

+-------------+------------------------------------+
|             |                                    |
| Release     | Modification                       |
+=============+====================================+
|             |                                    |
| 11.2        | Command introduced                 |
+-------------+------------------------------------+
---

## clear services ethernet-oam link-fault-management statistics.rst

clear services ethernet-oam link-fault-management statistics
------------------------------------------------------------

**Minimum user role:** operator

To clear ethernet OAM link-fault-management service counters:

**Command syntax: clear services ethernet-oam link-fault-management statistics** [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+----------------+------------------------------------------------------------------+---------------------------------+---------+
| Parameter      | Description                                                      | Range                           | Default |
+================+==================================================================+=================================+=========+
| interface-name | Clears ethernet OAM LFM statistics for a specific interface      | ge<interface speed>-<A>/<B>/<C> | \-      |
+----------------+------------------------------------------------------------------+---------------------------------+---------+

**Example**
::

	dnRouter# clear services ethernet-oam link-fault-management statistics
	dnRouter# clear services ethernet-oam link-fault-management statistics ge100-0/0/19


.. **Help line:** clear 802.3ah EFM link-OAM statistics

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## clear services flow-monitoring cache counters.rst

clear services flow-monitoring cache counters
---------------------------------------------

**Minimum user role:** operator

To clear the flow-monitoring cache counters:

**Command syntax: clear services flow-monitoring cache counters**  ncp [ncp-id]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - "clear services flow-monitoring counters" without parameter, clears counters on all NCPs.

**Parameter table:**

+-----------+-----------------------------------------------------------------------+--------+-------------+
| Parameter | Description                                                           | Range  |             |
|           |                                                                       |        | Default     |
+===========+=======================================================================+========+=============+
| ncp-id    | Clears the flow-monitoring cache counters from the specified NCP only | 0..255 | \-          |
+-----------+-----------------------------------------------------------------------+--------+-------------+


**Example**
::

	dnRouter# clear services flow-monitoring cache counters ncp 5


.. **Help line:** clear flow-monitoring counters.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.4        | Command introduced    |
+-------------+-----------------------+
---

## clear evpn counters.rst

clear evpn counters
-------------------

**Minimum user role:** operator

To reset the evpn service instance counters:

**Command syntax: clear evpn counters** {instance [instance-name]}

**Command mode:** operation

.. **Hierarchies**

**Note**

- The Attachment Circuit (AC) counters are not reset.

**Parameter table**

+---------------+-------------------------------+------------+---------+
| Parameter     | Description                   | Range      | Default |
+===============+===============================+============+=========+
| instance-name | The configured evpn instance. | String     | \-      |
|               |                               | 1..255     |         |
+---------------+-------------------------------+------------+---------+

**Example**
::

	dnRouter# clear evpn counters instance evpn1


.. **Help line:**

**Command History**

+---------+---------------------------------------------------------------+
| Release | Modification                                                  |
+=========+===============================================================+
| 18.1    | Command introduced                                            |
+---------+---------------------------------------------------------------+



---

## clear mpls statistics forwarding-table.rst

clear mpls statistics forwarding-table
--------------------------------------

**Minimum user role:** operator

To clear MPLS forwarding table counters:

**Command syntax: clear mpls statistics forwarding-table**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - Clears all the MPLS forwarding table counters.

.. **Parameter table:**


**Example**
::

	dnRouter# clear mpls statistics forwarding-table


.. **Help line:** Clears MPLS forwarding table counters.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 15.1        | Command introduced    |
+-------------+-----------------------+
---

## clear qppb counters.rst

clear qppb counters
-------------------

**Minimum user role:** operator

To clear the QPPB counters, use the following command:

**Command syntax: clear qppb counters** interface [interface-name] rule-id [rule-id]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - **Clear qppb counters** - if no interface clears all QPPB counters on all interfaces

 - **Clear qppb counters interface x** - clears all QPPB counters on the specified interface

 - **Clear qppb counters** - if no rule-id is given, clears all QPPB counters on all rules

 - **Clear qppb counters rule-id x** - clears all QPPB counters of the specified rule-id

**Parameter table:**

+----------------+-------------------------------------------------------------------------------+---------------------------------+---------+
| Parameter      | Description                                                                   | Range                           | Default |
+================+===============================================================================+=================================+=========+
| interface-name | Clears the QPPB counters from the specified interface only.                   | ge<interface speed>-<A>/<B>/<C> | \-      |
|                | If you do not specify an [interface-name], all QPPB counters will be cleared. |                                 |         |
|                |                                                                               |                                 |         |
+----------------+-------------------------------------------------------------------------------+---------------------------------+---------+
| rule-id        | Clears the QPPB counters of the specified rule only.                          | 1..128                          | \-      |
|                | If you do not specify a rule-id, all QPPB counters will be cleared.           |                                 |         |
|                |                                                                               |                                 |         |
+----------------+-------------------------------------------------------------------------------+---------------------------------+---------+


**Example**
::

	dnRouter# clear qppb counters
	dnRouter# clear qppb counters interface ge100-1/1/1
	dnRouter# clear qppb counters interface bundle-1
    dnRouter# clear qppb counters interface ge100-1/1/1 rule-id 10
	dnRouter# clear qppb counters rule-id 30


.. **Help line:** clear qppb counters attached to interface

**Command History**

+---------+-----------------------------------------------------------------------------------+
| Release | Modification                                                                      |
+=========+===================================================================================+
| 17.1    | Command introduced                                                                |
+---------+-----------------------------------------------------------------------------------+
---

## clear services mpls-oam counters.rst

clear services mpls-oam counters
--------------------------------

**Minimum user role:** operator

To clear MPLS-OAM service counters:

**Command syntax: clear services mpls-oam counters** {profile [profile-name] \| tunnel-name [tunnel-name] \| service-name [service-name] \| auto-mesh [template-name] \| auto-bypass}

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+---------------+------------------------------------------------------------------------------------------------+-------+---------+
| Parameter     | Description                                                                                    | Range | Default |
+===============+================================================================================================+=======+=========+
| profile-name  | Clears the counters for MPLS-OAM profile only                                                  | \-    | \-      |
+---------------+------------------------------------------------------------------------------------------------+-------+---------+
| tunnel-name   | Clears the counters for the specified tunnel only                                              | \-    | \-      |
+---------------+------------------------------------------------------------------------------------------------+-------+---------+
| service-name  | Clears the counters for the specified service only                                             | \-    | \-      |
+---------------+------------------------------------------------------------------------------------------------+-------+---------+
| template-name | Clears the counters for the tunnels that were created by the specified auto-mesh template only | \-    | \-      |
+---------------+------------------------------------------------------------------------------------------------+-------+---------+
| auto-bypass   | Clears the counters for auto-bypass tunnels                                                    | \-    | \-      |
+---------------+------------------------------------------------------------------------------------------------+-------+---------+

**Example**
::

	dnRouter# clear services mpls-oam counters
	dnRouter# clear services mpls-oam counters profile COS_1
	dnRouter# clear services mpls-oam counters tunnel-name tunnel_1


.. **Help line:**

**Command History**

+---------+----------------------+
| Release | Modification         |
+=========+======================+
| 11.0    | Command introduced   |
+---------+----------------------+
| TBD     | Added service filter |
+---------+----------------------+
---

## clear system icmp unreachable statistics.rst

clear system icmp unreachable statistics
-----------------------------------------

**Minimum user role:** operator

Clears all ICMP unreachable statistics counters (these are presented by the show system unreachable statistics command. See "show system icmp unreachable statistics".

To clear icmp unreachable statistics counters:

**Command syntax: clear system icmp unreachable statistics** ncp [ncp-id]

**Command mode:** operation

.. **Hierarchies**

.. **Note**


**Parameter table**

+-----------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Description                                                                                                                                    |
+===========+================================================================================================================================================+
| ncp-id    | Clear the unreachable statistics counters for the specified NCP only. If you do not specify an NCP, the counters for all NCPs will be cleared. |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------+

**Example**
::

	dnRouter# clear system icmp unreachable statistics ncp 5

	dnRouter# clear system icmp unreachable statistics


.. **Help line:** Clears all icmp unreachable statistics counters (presented by show system icmp unreachable statisitics CLI command).


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.0        | Command introduced    |
+-------------+-----------------------+
---

## clear system upgrade.rst

clear system upgrade
--------------------

**Minimum user role:** operator

This command removes nodes whose upgrade has failed from the list of "nodes in upgrade" in the show system command output. The failed upgrade state refers to:
•	Firmware-upgrade (failed)
•	BaseOS-upgrade (failed)
To clear system nodes in failed upgrade state:

**Command syntax: clear system upgrade** [serial-number]

**Command mode:** operation

.. **Hierarchies**

**Note**

- Only nodes that are in failed upgrade state can be cleared:
 
  - firmware-upgrade (failed)

  - baseos-upgrade (failed)

If no serial number is specified, all nodes in failed upgrade state will be cleared.

**Parameter table**

+------------------+-----------------------------------------------------------------------------------------------------------------+-----------+-------------+
|                  |                                                                                                                 |           |             |
| Parameter        | Description                                                                                                     | Range     | Default     |
+==================+=================================================================================================================+===========+=============+
|                  |                                                                                                                 |           |             |
| serial-number    | Specify a node's serial-number to remove it from the list. All other nodes (failed or otherwise) remain intact. | \-        | \-          |
|                  |                                                                                                                 |           |             |
|                  | If you do not specify a serial-number, all nodes with a failed upgrade state will be cleared.                   |           |             |
+------------------+-----------------------------------------------------------------------------------------------------------------+-----------+-------------+

**Example**
::

	dnRouter# clear system upgrade ABCDE
	node ABCDE cleared failed state

	dnRouter# clear system upgrade
	node DDDDD cleared failed state
	node BBBBB cleared failed state

	dnRouter# clear system upgrade BBBBB
	Error: node with serial-number BBBBB does not exist!

	dnRouter# clear system upgrade CCCCC
	Error: node with serial-number CCCC is not in upgrade failed state!
	
	dnRouter# clear system upgrade ABCDE
	Error: no nodesin upgrade failed state!



.. **Help line:** clear system nodes in failed upgrade state.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.5        | Command introduced    |
+-------------+-----------------------+
---

## clear event-manager counters.rst

clear event-manager counters
----------------------------

**Minimum user role:** operator

Use this command to clear all policy counters, or the counters for a specific policy type.

**Command syntax: clear event-manager counters** policy-type [policy-type]

**Command mode:** operation

.. **Hierarchies**

**Note**

- clear event-manager counters - clears all policy counters.

- clear event-manager counters policy-type - clears all policy counters per policy type, for the following policy types:

  - event-policy - policy that will be executed upon matching trigger of registered system event.

  - periodic-policy - a recurrent policy according to the scheduled configuration, with limited execution time.

  - generic-policy - policy that will be executed only once and unlimited in execution time.

**Parameter table:**

+--------------------+-----------------------+-----------------+-------------+
|                    |                       |                 |             |
| Parameter Name     | Description           | Range           | Default     |
+====================+=======================+=================+=============+
|                    |                       | event-policy    | \-          |
| policy-type        | The type of policy    |                 |             |
|                    |                       | periodic-policy |             |
|                    |                       |                 |             |
|                    |                       | generic-policy  |             |
+--------------------+-----------------------+-----------------+-------------+


**Example**
::

    dnRouter#
    dnRouter# clear event-manager counters
    dnRouter# clear event-manager counters policy-type periodic-policy
    dnRouter# clear event-manager counters policy-type generic-policy
    dnRouter# clear event-manager counters policy-type event-policy
    dnRouter#

.. **Help line:** this action will clear all policies counters.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.1        | Command introduced    |
+-------------+-----------------------+
---

## clear segment-routing pcep policy delegation.rst

clear segment-routing pcep policy delegation
--------------------------------------------

**Minimum user role:** operator

To flush the PCE ERO for a PCC delegated policy path:

**Command syntax: clear segment-routing pcep policy delegation** {policy [policy-name] | policy [policy-name] path [path-name]}

**Command mode:** operation

**Note**

 - Apply only for PCC initiated 'pcep-delegation' paths.
 - The policy path remains delegated to the active PCE.
 - The policy path will clear its ERO and change to a down state.


**Parameter table:**

+-----------------+----------------------------------------------------+-----------+-------------+
| Parameter       | Description                                        | Range     | Default     |
+=================+====================================================+===========+=============+
| policy-name     | Clear all delegated path of specific policy        | string    | \-          |
+-----------------+----------------------------------------------------+-----------+-------------+
| path-name       | Clear specific delegated path of specific policy   | string    | \-          |
+-----------------+----------------------------------------------------+-----------+-------------+


**Example**
::

	dnRouter# clear segment-routing pcep policy delegation
	dnRouter# clear segment-routing pcep policy delegation policy SR_TE_POLICY_1
    dnRouter# clear segment-routing pcep policy delegation policy SR_TE_POLICY_1 path PCEP_PATH_2



**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 19.1        | Command introduced    |
+-------------+-----------------------+
---

## clear rpki sessions statistics.rst

clear rpki sessions statistics
------------------------------

**Minimum user role:** operator

To clear rpki sessions statistics:

**Command syntax: clear rpki sessions** [server-address] **statistics**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+----------------+-------------------------------------------+-------------------------+---------+
| Parameter      | Description                               | Range                   | Default |
+================+===========================================+=========================+=========+
| server-address | Clear the statistics of a specific server | IP-address or hostname  | \-      |
+----------------+-------------------------------------------+-------------------------+---------+


**Example**
::

	dnRouter# clear rpki sessions statistics
	dnRouter# clear rpki sessions 1.1.1.1 statistics
	dnRouter# clear rpki sessions 2001:125:125::1 statistics
	dnRouter# clear rpki sessions rpkiv.drivenets.com statistics


.. **Help line:**

**Command History**

+----------+-----------------------------------------------------+
| Release  | Modification                                        |
+==========+=====================================================+
| 15.1     | Command introduced                                  |
+----------+-----------------------------------------------------+
| 16.2     | Replaced server-id parameter with server-address    |
+----------+-----------------------------------------------------+

---

## clear grpc counters.rst

clear grpc counters
-------------------

**Minimum user role:** operator

To clear grpc counters per specific session and/or per system:

**Command syntax: clear grpc counters** [session-id]

**Command mode:** operation

.. **Hierarchies**

**Note**

- A command without a specific session-id clears counters per all active sessions and per system.


**Parameter table:**

+------------+--------------------------------+---------------+--------------+
| Parameter  |        Description             |   Range       |Default value |
+============+================================+===============+==============+
| session-id | The id of the specific session | 1..65535      | \-           |
+------------+--------------------------------+---------------+--------------+

**Example**
::

	dnRouter# clear grpc counters
	dnRouter# clear grpc counters 776

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.2        | Command introduced    |
+-------------+-----------------------+
---

## clear twamp statistics.rst

clear twamp statistics
----------------------

**Minimum user role:** operator

To clear TWAMP statistics:

**Command syntax: clear twamp statistics** {control [connection-id] data [session-id]}

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - clear twamp statistics, by default command clears all twamp statistics for all sessions. Connection-id applies to control session, Session-id applies for data sessions. Clearing control connection-id does not clear statistics of its respective data sessions. In order to clear data session-id, user must mention the control connection-id.

 - session id as seen in show services twamp session

**Parameter table**

+------------------+----------------------------------------------------------------------+------------------------------------------------------------------+-------------------+
|                  |                                                                      |                                                                  |                   |
| Parameter        | Description                                                          | Value                                                            | Default           |
+==================+======================================================================+==================================================================+===================+
|                  |                                                                      | Available control session ID. See "show services twamp sessions" |                   |
| connection-id    | Clears TWAMP statistics for the specified control   session only.    |                                                                  | \-                |
+------------------+----------------------------------------------------------------------+------------------------------------------------------------------+-------------------+
|                  |                                                                      | Available data session ID. See "show services twamp sessions"    | \-                |
| session-id       | Clears TWAMP statistics for the specified data   session only.       |                                                                  |                   |
+------------------+----------------------------------------------------------------------+------------------------------------------------------------------+-------------------+


**Example**
::

	dnRouter# clear twamp statistics control [connection-id]
	dnRouter# clear twamp statistics control [connection-id] data [session-id]

	dnRouter# clear twamp statistics control 1
	dnRouter# clear twamp statistics control 1 data 2

	dnRouter# clear twamp statistics



.. **Help line:**

**Command History**

+-------------+---------------------------------------------+
|             |                                             |
| Release     | Modification                                |
+=============+=============================================+
|             |                                             |
| 11.2        | Command introduced                          |
+-------------+---------------------------------------------+
---

## clear interfaces management ipv4-address.rst

clear interface management ipv4-address
-------------------------------------------------------------------

**Minimum user role:** operator


To remove the ipv4-address from the management bond interface:


**Command syntax: clear interfaces management [interface-name] ipv4-address**

**Command mode:** operator

.. **Note:**


**Parameter table:**

+------------------+----------------------------------------------+-------+-------+
| Parameter        | Values                                       | Range | Value |
+==================+==============================================+=======+=======+
| interface-name   | mgmt-ncc-0, mgmt-ncc-1                       |       | \-    |
+------------------+----------------------------------------------+-------+-------+


**Example:**
::

	dnRouter# clear interfaces management mgmt-ncc-0 ipv4-address
	

.. **Help line:** Remove ipv4-address address from management bond interface


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 16.2        | Command introduced    |
+-------------+-----------------------+

---

## clear isis neighbor.rst

clear isis neighbor
-------------------

**Minimum user role:** operator

To clear the IS-IS database and reset IS-IS adjacencies:

**Command syntax: clear isis** instance [isis-instance-name] **process**

**Command mode:** operation

.. **Hierarchies**

**Note:**

-  Use "instance [isis-instance-name]" to clear from a specific ISIS instance

-  Use "set [system-id]" to reset specific neighbor adjacency

**Parameter table:**

+--------------------+-----------------------------------------------------------------------+-----------------------------------------+
| Parameter          | Description                                                           | Range                                   |
+====================+=======================================================================+=========================================+
| no parameter       | Reset all IS-IS neighbor adjacencies                                  | \-                                      |
+--------------------+-----------------------------------------------------------------------+-----------------------------------------+
| isis-instance-name | Reset all IS-IS neighbor adjacencies for the specified IS-IS instance | 1..255 characters                       |
+--------------------+-----------------------------------------------------------------------+-----------------------------------------+
| system-id          | Resets a specific neighbor adjacency.                                 | ssss.ssss.ssss (where s is a hex value) |
+--------------------+-----------------------------------------------------------------------+-----------------------------------------+

**Example**
::

	dnRouter# clear isis neighbor

	dnRouter# clear isis neighbor 0100.0070.1A45

	dnRouter# clear isis instance ISIS_A neighbor 0100.0070.1A45
	50.0001.F100.0070.1A45.00, 50.0002.F100.0070.1A45.00




.. **Help line:**

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## clear ospfv3 routes.rst

clear ospfv3 routes
-------------------

**Minimum user role:** operator

The following command clears and re-installs OSPFv3 routes to RIB (for OSPF only - unless fast-reroute is indicated, in order to clear only the LFA routes):

**Command syntax: clear ospfv3 routes**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. **Parameter table:**

**Example**
::

	dnRouter# clear ospfv3 routes


.. **Help line:** Clear and reinstall OSPFv3 routes

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.6        | Command introduced    |
+-------------+-----------------------+
---

## clear evpn restore-cycles.rst

clear evpn restore-cycles
-------------------------

**Minimum user role:** operator

To reset the evpn service instance restore-cycles:

**Command syntax: clear evpn restore-cyles** {service [instance-name] mac [mac-address]}

**Command mode:** operation

.. **Hierarchies**


**Parameter table**

+---------------+-------------------------------+------------+---------+
| Parameter     | Description                   | Range      | Default |
+===============+===============================+============+=========+
| instance-name | The configured evpn instance. | String     | \-      |
|               |                               | 1..255     |         |
+---------------+-------------------------------+------------+---------+
| mac-address   | The specific mac-address      | String     |         |
+---------------+-------------------------------+------------+---------+

**Example**
::

	dnRouter# clear evpn restore-cycles service evpn1 mac  a2:76:b0:08:9e:02


.. **Help line:**

**Command History**

+---------+---------------------------------------------------+
| Release | Modification                                      |
+=========+===================================================+
| 18.3    | Command introduced                                |
+---------+---------------------------------------------------+

---

## clear pim tree.rst

clear pim tree
--------------

**Minimum user role:** operator

You can use the command to clear all dynamically-signaled or data-driven PIM tree entries.
When group-address command is indicated, all the PIM tree entries with the related group address will be cleared.
The command clears all the PIM tree dynamic or data driven tree states (statically created entries or PIM SM static entries are not cleared unless the related static RP range or IGMP Join are deleted).

**Command syntax: clear pim tree** group [group-address] source [source-address]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**

+----------------+----------------------------------------------------------------------------+-------------+---------+
| Parameter      | Description                                                                | Range       | Default |
+================+============================================================================+=============+=========+
| group-address  | Clears PIM tree entries for the specified group address or prefix          | A.B.C.D     | \-      |
|                |                                                                            | A.B.C.D/M   |         |
+----------------+----------------------------------------------------------------------------+-------------+---------+
| source-address | Clears PIM tree entries for the specified source address                   | A.B.C.D     | \-      |
+----------------+----------------------------------------------------------------------------+-------------+---------+


**Example**
::

  dnRouter# clear pim tree
  dnRouter# clear pim tree 227.1.1.1


.. **Help line:** Clear PIM dynamic Tree entries

**Command History**

+-------------+--------------------------------+
| Release     | Modification                   |
+=============+================================+
| 12.0        | Command introduced             |
+-------------+--------------------------------+
| 16.2        | Added source-address parameter |
+-------------+--------------------------------+

---

## clear telnet session.rst

clear telnet session
--------------------

**Minimum user role:** operator

To terminate active telnet sessions:

**Command syntax: clear telnet session [session-id]**

**Command mode:** operation

.. **Hierarchies**

.. **Note**


**Parameter table**

+------------+---------------------------------------------------------------------------+
| Parameter  | Description                                                               |
+============+===========================================================================+
| session-id | Any active session id presented by "show system telnet sessions" commands |
+------------+---------------------------------------------------------------------------+

**Example**
::

	dnRouter# clear telnet session 57
	Telnet session userName@pts2 was successfully terminated

	dnRouter# clear telnet session 131
	Telnet session userName@pts2 was successfully terminated


.. **Help line:** Clear active telnet session


**Command History**

+-------------+---------------------------------------------+
|             |                                             |
| Release     | Modification                                |
+=============+=============================================+
|             |                                             |
| 13.1        | Command introduced                          |
+-------------+---------------------------------------------+
---

## clear clock ptp counters.rst

clear clock ptp counters
------------------------

**Minimum user role:** operator

Clearing the PTP clock level counters resets the counters to zero and removes the counter information from the database. It does not clear PTP port or other clock counters as the SyncE ESMC counters.

To clear the PTP clock counters:

**Command syntax: clear clock ptp counters**

**Command mode:** operation

.. **Hierarchies**

.. **Note**


.. **Parameter table:**

**Example**
::

	dnRouter# clear clock ptp counters


.. **Help line:** clear ptp counters

**Command History**

+-------------+---------------------------------------+
| Release     | Modification                          |
+=============+=======================================+
| 18.0        | Command introduced                    |
+-------------+---------------------------------------+

---

## clear isis statistics.rst

clear isis statistics
---------------------

**Minimum user role:** operator

To clear IS-IS statistics:

**Command syntax: clear isis** instance [isis-instance-name] **statistics**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - use "instance [isis-instance-name]" to clear from a specific ISIS instance


**Parameter table:**

+-----------------------+-------------------------------------------------------------+---------------------+-------------+
|                       |                                                             |                     |             |
| Parameter             | Description                                                 | Range               | Default     |
+=======================+=============================================================+=====================+=============+
|                       |                                                             |                     |             |
| no parameter          | Clear all IS-IS statistics                                  | \-                  | \-          |
+-----------------------+-------------------------------------------------------------+---------------------+-------------+
|                       |                                                             |                     | \-          |
| isis-instance-name    | Clear IS-IS statistics from the specified IS-IS instance    | 1..255 characters   |             |
+-----------------------+-------------------------------------------------------------+---------------------+-------------+


**Example**
::

	dnRouter# clear isis statistics
	dnRouter# clear isis instance ISIS_A statistics


.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 10.0        | Command introduced    |
+-------------+-----------------------+
---

## clear ospf statistics.rst

clear ospf statistics
---------------------

**Minimum user role:** operator

Use the following command to clear the OSPF statistics. If an interface is specified the counters for the specific interface will be cleared:

**Command syntax: clear ospf** instance [ospf-instance-name] **statistics** interface [ interface-name ]

**Command mode:** operation

.. **Hierarchies**

**Note**

- clearing an interface counters must not impact the global counters and vice versa.

- use "instance [ospf-instance-name]" to clear information from a specific OSPF instance, when not specified, clear information from all OSPF instances

**Parameter table:**

+--------------------+----------------------------------------------------------------+---------------------------------------------------+-------------+
|                    |                                                                |                                                   |             |
| Parameter          | Description                                                    | Range                                             | Default     |
+====================+================================================================+===================================================+=============+
|                    |                                                                |                                                   |             |
| interface-name     | clears the ospf statistics for the specified interface         | ge<interface speed>-<A>/<B>/<C>                   | \-          |
|                    |                                                                |                                                   |             |
|                    |                                                                | ge<interface speed>-<A>/<B>/<C>.<sub-interface id>|             |
|                    |                                                                |                                                   |             |
|                    |                                                                | bundle-<bundle id>                                |             |
|                    |                                                                |                                                   |             |
|                    |                                                                | bundle-<bundle id>.<sub-interface id>             |             |
|                    |                                                                |                                                   |             |
|                    |                                                                | lo<lo-interface id>                               |             |
+--------------------+----------------------------------------------------------------+---------------------------------------------------+-------------+
| ospf-instance-name | clears the ospf information for the specified instance         | configured instances names                        | all         |
+--------------------+----------------------------------------------------------------+---------------------------------------------------+-------------+

**Example**
::

	dnRouter# clear ospf statistics
	dnRouter# clear ospf instance instance1 statistics

.. **Help line:** Clear OSPF statistics

**Command History**

+-------------+------------------------+
|             |                        |
| Release     | Modification           |
+=============+========================+
|             |                        |
| 11.6        | Command introduced     |
+-------------+------------------------+
| 18.1        | Add instance parameter |
+-------------+------------------------+

---

## clear system diagnostics counters test.rst

clear system diagnostics counters test
--------------------------------------

**Minimum user role:** operator

Clears system diagnostics counters per test or per component.


**Command syntax: clear system diagnostics counters test [test-type]** component [component-type]

**Command mode:** operation

.. **Hierarchies**

**Note**

When component is specified, only the specified component/s counters are cleared. Otherwise all system diagnostics counters per test are cleared.


**Parameter table**


+-------------------+------------------------+------------------+-------------------+
|                   |                        |                  |                   |
| Parameter         | Description            | Value            | Default           |
+===================+========================+==================+===================+
|                   |                        |                  |                   |
| test-type         | The type of test       | punt-datapath    | \-                |
+-------------------+------------------------+------------------+-------------------+
|                   |                        |                  |                   |
| component-type    | The type of component. | ncp              | all               |
+-------------------+------------------------+------------------+-------------------+


**Example**
::

	dnRouter# clear system diagnostics counters test punt-datapath
	dnRouter# clear system diagnostics counters test punt-datapath component ncp



.. **Help line:** diagnostics component id counters to be cleared.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.1        | Command introduced    |
+-------------+-----------------------+
---

## clear ospfv3 neighbor interface.rst

clear ospfv3 neighbor interfaces
--------------------------------

**Minimum user role:** operator

To clear OSPFv3 interface information:

**Command syntax: clear ospfv3 neighbor interface** [interface-name]

**Command mode:** operation

.. **Hierarchies**

**Note**

- add *interface-name* to clear information for a specific interface


**Parameter table:**

**Parameter table:**

+-------------------+--------------------------------------------------------------+---------------------------------------+-------------+
|                   |                                                              |                                       |             |
| Parameter         | Description                                                  | Range                                 | Default     |
+===================+==============================================================+=======================================+=============+
|                   |                                                              |                                       |             |
| interface-name    | clears the ospf information for the specified interface      | configured interface name.            | \-          |
|                   |                                                              |                                       |             |
|                   |                                                              | ge{/10/25/40/100}-X/Y/Z               |             |
|                   |                                                              |                                       |             |
|                   |                                                              | bundle-<bundle id>                    |             |
|                   |                                                              |                                       |             |
|                   |                                                              | bundle-<bundle id>.<sub-interface id> |             |
|                   |                                                              |                                       |             |
|                   |                                                              |                                       |             |
+-------------------+--------------------------------------------------------------+---------------------------------------+-------------+


**Example**
::

	dnRouter# clear ospfv3 neighbor interface
	dnRouter# clear ospfv3 neighbor interfaces bundle-2.2004

.. **Help line:** Clear OSPFv3 neighbor interface information


**Command History**

+-------------+------------------------------------------------------------------+
|             |                                                                  |
| Release     | Modification                                                     |
+=============+==================================================================+
|             |                                                                  |
| 6.0         | Command introduced                                               |
+-------------+------------------------------------------------------------------+
|             |                                                                  |
| 11.6        | Renamed to 'ospfv3 neighbor interfaces' and introduced OSPFv3    |
+-------------+------------------------------------------------------------------+
---

## clear rsvp auto-bandwidth.rst

clear rsvp auto-bandwidth
--------------------------

**Minimum user role:** operator

This command resets the auto-bandwidth adjustment interval timer and clears all the collected average-rate samples. The tunnel will continue to use the current bandwidth until the next auto-bandwidth adjustment.

To clear auto-bandwidth information:

**Command syntax: clear rsvp auto-bandwidth** tunnel [tunnel-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table:**


+-------------+-----------------------------------------------------------------+
| Parameter   | Description                                                     |
+=============+=================================================================+
| tunnel-name | Clear auto-bandwidth information for the specified tunnel only. |
+-------------+-----------------------------------------------------------------+


**Example**
::

	dnRouter# clear rsvp auto-bandwidth

	dnRouter# clear rsvp auto-bandwidth tunnel auto_tunnel_R1_R8_PRIOIRTY_CORE


.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+
---

## clear ospf routes.rst

clear ospf routes
-----------------

**Minimum user role:** operator

The following command clears and re-installs OPSF routes to RIB (for OSPF only - unless fast-reroute is indicated, in order to clear only the LFA routes):

**Command syntax: clear ospf** instance [ospf-instance-name] **routes**

**Command mode:** operation

.. **Hierarchies**

**Note**

- use "instance [ospf-instance-name]" to clear information from a specific OSPF instance, when not specified, clear information from all OSPF instances

**Parameter table:**

+--------------------+----------------------------------------------------------------+---------------------------------------+-------------+
|                    |                                                                |                                       |             |
| Parameter          | Description                                                    | Range                                 | Default     |
+====================+================================================================+=======================================+=============+
| ospf-instance-name | clears the ospf information for the specified instance         | configured instances names            | all         |
+--------------------+----------------------------------------------------------------+---------------------------------------+-------------+

**Example**
::

	dnRouter# clear ospf routes
	dnRouter# clear ospf instance instance1 routes

.. **Help line:** Clear and reinstall OSPF routes

**Command History**

+-------------+------------------------+
|             |                        |
| Release     | Modification           |
+=============+========================+
|             |                        |
| 11.6        | Command introduced     |
+-------------+------------------------+
| 18.1        | Add instance parameter |
+-------------+------------------------+

---

## clear mgmt dnor-server.rst

clear mgmt dnor-server
----------------------

**Minimum user role:** operator

To clear the configured DNOR servers in the system:

**Command syntax: clear mgmt dnor-server**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - Clears all configured DNOR servers.

.. **Parameter table:**


**Example**
::

	dnRouter# clear mgmt dnor-server


.. **Help line:** Clears DNOR servers configuration.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 18.2.1      | Command introduced    |
+-------------+-----------------------+

---

## clear rsvp statistics tunnels.rst

clear rsvp statistics tunnels
-----------------------------

**Minimum user role:** operator

To clear statistics for RSVP tunnels:

**Command syntax: clear rsvp statistics tunnels** name [tunnel-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**


**Parameter table:**

+-------------+------------------------------------------------------------+
| Parameter   | Description                                                |
+=============+============================================================+
| tunnel-name | Clear RSVP statistics from the specified RSVP tunnel only. |
+-------------+------------------------------------------------------------+


**Example**
::

	dnRouter# clear rsvp statistics tunnels
	dnRouter# clear rsvp statistics tunnels name TUNNEL_1

.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+
---

## clear ospfv3 statistics.rst

clear ospfv3 statistics
-----------------------

**Minimum user role:** operator

Use the following command to clear the OSPFv3 statistics. If an interface is specified the counters for the specific interface will be cleared:

**Command syntax: clear ospfv3 statistics** interface [ interface-name ]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - clearing an interface counters must not impact the global counters and vice versa.

**Parameter table:**

+-------------------+-------------------------------------------------------------+---------------------------------------------------+-------------+
|                   |                                                             |                                                   |             |
| Parameter         | Description                                                 | Range                                             | Default     |
+===================+=============================================================+===================================================+=============+
|                   |                                                             |                                                   |             |
| interface-name    | clears the ospfv3 statistics for the specified interface    | ge<interface speed>-<A>/<B>/<C>                   | all         |
|                   |                                                             |                                                   |             |
|                   |                                                             | ge<interface speed>-<A>/<B>/<C>.<sub-interface id>|             |
|                   |                                                             |                                                   |             |
|                   |                                                             | bundle-<bundle id>                                |             |
|                   |                                                             |                                                   |             |
|                   |                                                             | bundle-<bundle id>.<sub-interface id>             |             |
|                   |                                                             |                                                   |             |
|                   |                                                             | lo<lo-interface id>                               |             |
+-------------------+-------------------------------------------------------------+---------------------------------------------------+-------------+

**Example**
::

	dnRouter# clear ospfv3 statistics
	dnRouter# clear ospfv3 statistics interafce bundle-12.1234


.. **Help line:** Clear OSPFv3 statistics

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.6        | Command introduced    |
+-------------+-----------------------+
---

## clear ospfv3 process.rst

clear ospfv3 process
--------------------

**Minimum user role:** operator

To clear the entire OSPFv3 database and restart the adjacencies:

**Command syntax: clear ospfv3 process**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. **Parameter table:**


**Example**
::

	dnRouter# clear ospfv3 process

.. **Help line:** Clear OSPFv3 process

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.6        | Command introduced    |
+-------------+-----------------------+
---

## clear ftp session.rst

clear ftp session
------------------

**Minimum user role:** operator

To clear ftp sessions:

**Command syntax: clear ftp session [session-id]**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. **Parameter table:**

+------------+-----------------------------------------------------------------------+-------+---------+
| Parameter  | Description                                                           | Range | Default |
+------------+-----------------------------------------------------------------------+-------+---------+
| session-id | Any active session-id presented by "show system ftp sessions" command | /-    | /-      |
+------------+-----------------------------------------------------------------------+-------+---------+


**Example**
::

	dnRouter# clear ftp session 57
	FTP session MyUserName@pts2 was successfully terminated

	dnRouter# clear ftp session 131
	FTP session MyUserName@pts2 was successfully terminated


.. **Help line:** Clear active ftp session

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 11.2        | Command introduced    |
+-------------+-----------------------+
---

## clear interfaces dhcpv6 relay statistics.rst

clear interfaces dhcpv6 relay statistics
-----------------------------------------

**Minimum user role:** operator

Clearing the interface DHCPv6 relay statistics resets the counters to zero and removes the counter information from the database.

To clear the interface DHCPv6 relay statistics:

**Command syntax: clear interfaces dhcpv6 relay statistics** [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. - **Clear interfaces dhcpv6 relay statistics** - clears DHCPv6 relay counters for **ALL** interfaces.

.. - **Clear interfaces dhcpv6 relay statistics interface-name** - clears DHCPv6 relay counters for the specified interface.

**Parameter table:**

+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+-------------+
| Parameter         | Description                                                                                                                                            | Range                                             | Default     |
+===================+========================================================================================================================================================+===================================================+=============+
| interface-name    | Clears the DHCPv6 relay counters for the specified interface only. If an interface-name is not specified, the counters are cleared for all interfaces. | ge<interface speed>-<A>/<B>/<C>                   | \-          |
|                   |                                                                                                                                                        | ge<interface speed>-<A>/<B>/<C>.<sub-interface-id>|             |
|                   |                                                                                                                                                        | bundle-<bundle-id>                                |             |
|                   |                                                                                                                                                        | bundle-<bundle-id>.<sub-interface-id>             |             |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+-------------+


**Example**
::

	dnRouter# clear interfaces dhcpv6 relay statistics
	dnRouter# clear interfaces dhcpv6 relay statistics ge100-0/0/0

.. **Help line:** Clear interface DHCPv6 relay counters

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 19.10       | Command introduced    |
+-------------+-----------------------+

---

## clear snmp statistics.rst

clear snmp statistics
---------------------

**Minimum user role:** operator

Use the following command to reset the number of SNMP requests, responses, and traps that the SNMP agent received and set:

**Command syntax: clear snmp statistics** 

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. **Parameter table:**

**Example**
::

	dnRouter# clear snmp statistics

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.6        | Command introduced    |
+-------------+-----------------------+
---

## clear ospf neighbor interface.rst

clear ospf neighbor interface
-----------------------------

**Minimum user role:** operator

To clear the entire OSPF interface information:

**Command syntax: clear ospf** instance [ospf-instance-name] **neighbor interface** [interface-name]

**Command mode:** operation

.. **Hierarchies**

**Note**

- add *interface-name* to clear information for a specific interface

- use "instance [ospf-instance-name]" to clear information from a specific OSPF instance, when not specified, clear information from all OSPF instances

**Parameter table:**

+--------------------+----------------------------------------------------------------+---------------------------------------+-------------+
|                    |                                                                |                                       |             |
| Parameter          | Description                                                    | Range                                 | Default     |
+====================+================================================================+=======================================+=============+
|                    |                                                                |                                       |             |
| interface-name     | clears the ospf information for the specified interface        | configured interface name.            | \-          |
|                    |                                                                |                                       |             |
|                    |                                                                | ge{/10/25/40/100}-X/Y/Z               |             |
|                    |                                                                |                                       |             |
|                    |                                                                | bundle-<bundle id>                    |             |
|                    |                                                                |                                       |             |
|                    |                                                                | bundle-<bundle id>.<sub-interface id> |             |
|                    |                                                                |                                       |             |
|                    |                                                                |                                       |             |
+--------------------+----------------------------------------------------------------+---------------------------------------+-------------+
| ospf-instance-name | clears the ospf information for the specified instance         | configured instances names            | all         |
+--------------------+----------------------------------------------------------------+---------------------------------------+-------------+


**Example**
::

	dnRouter# clear ospf neighbor interface
	dnRouter# clear ospf instance instance1 neighbor interface
	dnRouter# clear ospf neighbor interface bundle-2.2004
	dnRouter# clear ospf instance instance1 neighbor interface bundle-2.2004


.. **Help line:** Clear OSPF neighbor interfaces information.

**Command History**

+-------------+------------------------------------------------------------------+
|             |                                                                  |
| Release     | Modification                                                     |
+=============+==================================================================+
|             |                                                                  |
| 6.0         | Command introduced                                               |
+-------------+------------------------------------------------------------------+
|             |                                                                  |
| 11.6        | Renamed to 'ospf neighbor interfaces'                            |
+-------------+------------------------------------------------------------------+
| 18.1        | Add instance parameter                                           |
+-------------+------------------------------------------------------------------+

---

## clear interfaces fabric counters.rst

clear interfaces fabric counters
--------------------------------

**Minimum user role:** operator

Clearing fabric interface counters resets the counters to zero and removes the counter information from the database. It does not clear SNMP-based counters.

To clear counter information relating to fabric interfaces:

**Command syntax: clear interfaces fabric counters** [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. - **Clear interfaces fabric counters** - clears all fabric counters for **ALL** interfaces

.. - **Clear interfaces management counters interface x** - clears all counters for a specific interface.


.. **Parameter table:**


**Example**
::

	dnRouter# clear interfaces fabric counters
	dnRouter# clear interfaces fabric counters fab-ncf400-0/0/0


.. **Help line:** clear fabric interface counters

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 11.0        | Command introduced    |
+-------------+-----------------------+
---

## clear ldp label-allocation.rst

clear ldp label-allocation
--------------------------

**Minimum user role:** operator

 Restart the ldp label allocation, as a result, ldp  withdraws the allocated label and re-runs binding and allocation logic for requested prefix / fec.
 To reset the ldp label allocations:

**Command syntax: clear ldp label-allocation** {ipv4 [ipv4-prefix] | pw-binding neighbor-address [neighbor-address] fec-value [fec-value] | p2mp root-address [root-address] opaque-value [opaque-value]}

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - clear ldp label-allocation - restart all ldp labels.

 - clear ldp label-allocation ipv4 [ipv4-prefix] - restart the ldp label of a given unicast prefix.

 - clear ldp label-allocation pw-binding - restart the ldp label of a given vpws pw, per the pw neighbor and fec-value (pw-id).

 - clear ldp label-allocation p2mp - restart the ldp p2mp lsp label per MC root-address and opaque-value.


**Parameter table:**

+---------------------+--------------------------------------------------------+---------------+-------------+
|                     |                                                        |               |             |
| Parameter           | Description                                            | Range         | Default     |
+=====================+========================================================+===============+=============+
|                     |                                                        |               |             |
| ipv4-prefix         | Restart ldp label of a given prefix                    | A.B.C.D/M     | \-          |
+---------------------+--------------------------------------------------------+---------------+-------------+
| neighbor-address    | Restart ldp label of a vpws pw per neighbor            | A.B.C.D       |             |
+---------------------+--------------------------------------------------------+---------------+-------------+
| fec-value           | Restart ldp label of a vpws pw per neighbor pw-id      | 1..4294967295 |             |
+---------------------+------------------------------------------------------------------------+-------------+
| root-address        | Restart ldp label of a root node IP address            | A.B.C.D       |             |
+---------------------+------------------------------------------------------------------------+-------------+
| opaque-value        | uniquely identifying the P2MP LSP in the               | string        |             |
|                     | context of the root node                               | no spaces     |             |
+---------------------+------------------------------------------------------------------------+-------------+


**Example**
::

	dnRouter# clear ldp label-allocation
	dnRouter# clear ldp label-allocation ipv4 7.7.7.7/32
	dnRouter# clear ldp label-allocation pw-binding neighbor-address 1.1.1.1 fec-value 444
	dnRouter# clear ldp label-allocation p2mp root-address 20.20.20.20 opaque-value 07000B0000010000000100000000

.. **Help line:** Restart ldp label-allocation

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 18.3        | Command introduced    |
+-------------+-----------------------+

---

## clear qos counters.rst

clear qos counters
------------------

**Minimum user role:** operator

To clear the QoS counters, use the following command:

**Command syntax: clear qos counters** [interface-name] [direction]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - **Clear qos counters** - clears all QoS counters (including egress-queues stats) on all interfaces

 - **Clear qos counters interface x** - clears all QoS counters on the specified interface

**Parameter table:**

+----------------+------------------------------------------------------------------------------+---------------------------------+---------+
| Parameter      | Description                                                                  | Range                           | Default |
+================+==============================================================================+=================================+=========+
| interface-name | Clears the QoS counters from the specified interface only.                   | ge<interface speed>-<A>/<B>/<C> | \-      |
|                | If you do not specify an [interface-name], all QoS counters will be cleared. |                                 |         |
|                |                                                                              | bundle-<bundle-id>              |         |
|                |                                                                              |                                 |         |
|                |                                                                              | fabm-<f>/<n>/<p>                |         |
|                |                                                                              |                                 |         |
|                |                                                                              | rcym-<f>/<n>/<p>                |         |
|                |                                                                              |                                 |         |
|                |                                                                              | cputx-<f>/<n>/<p>               |         |
|                |                                                                              |                                 |         |
|                |                                                                              | cpurx-<f>/<n>/<p>               |         |
|                |                                                                              |                                 |         |
|                |                                                                              | qppbr-<f>/<n>/<p>               |         |
|                |                                                                              |                                 |         |
|                |                                                                              | pmirr-<f>/<n>/<p>               |         |
+----------------+------------------------------------------------------------------------------+---------------------------------+---------+
| direction      | Clears the QoS counters in the specified direction                           | in                              | \-      |
|                |                                                                              |                                 |         |
|                |                                                                              | out                             |         |
+----------------+------------------------------------------------------------------------------+---------------------------------+---------+


**Example**
::

	dnRouter# clear qos counters
	dnRouter# clear qos counters ge100-1/1/1
	dnRouter# clear qos counters bundle-1
	dnRouter# clear qos counters bundle-1 in


.. **Help line:** clear qos counters attached to interface

**Command History**

+---------+-----------------------------------------------------------------------------------+
| Release | Modification                                                                      |
+=========+===================================================================================+
| 5.1.0   | Command introduced                                                                |
+---------+-----------------------------------------------------------------------------------+
| 9.0     | Command not supported                                                             |
+---------+-----------------------------------------------------------------------------------+
| 11.2    | Command re-introduced as part of the new QoS feature                              |
+---------+-----------------------------------------------------------------------------------+
| 15.0    | Added support for fabm and rcym fabric-multicast interface types and cpu counter  |
+---------+-----------------------------------------------------------------------------------+
| 17.2    | Replaced icpu with cputx and cpurx                                                |
+---------+-----------------------------------------------------------------------------------+
| TBD     | Added support for port mirroring                                                  |
+---------+-----------------------------------------------------------------------------------+
---

## clear netconf counters.rst

clear netconf counters
----------------------

**Minimum user role:** operator

To clear active netconf sessions:

**Command syntax: clear netconf counters** [session-id]

**Command mode:** operation

.. **Hierarchies**

**Note**

- A Command without a specific session-id clears counters per system. With sessions-id clears counters per active session. 

**Parameter table:**

+---------------+------------------------------------------+-------------+-------------+
|               |                                          |             |             |
| Parameter     | Description                              | Range       | Default     |
+===============+==========================================+=============+=============+
|               |                                          | 1 - 2^32 -1 |             |
| session-id    | Enter a specific session ID to clear     |             | \-          |
+---------------+------------------------------------------+-------------+-------------+


**Example**
::

	dnRouter# clear netconf counters
	dnRouter# clear netconf counters 776


.. **Help line:** clear netconf counters per specific session and/or per system.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 15.2        | Command introduced    |
+-------------+-----------------------+
---

## clear services flow-monitoring cache.rst

clear services flow-monitoring cache		
------------------------------------

**Minimum user role:** operator

To clear the flow-monitoring cache:

**Command syntax: clear services flow-monitoring cache** ncp [ncp-id] export

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 -  "clear services flow-monitoring cache" without export parameter, flushes flow-cache tables on all NCPs and do not export the flushed flows.      

 -  "clear services flow-monitoring cache" with export parameter, flushes flow-cache tables on all NCPs and export the flushed flows.        
 
 -  "clear services flow-monitoring cache" without export parameter and with specific NCP-ID flushes flow-cache tables on that specific NCP and do not export the flushed flows of that NCP.     

 -  "clear services flow-monitoring cache" with export parameter and with specific NCP-ID flushes flow-cache tables on that specific NCP and export the flushed flows of that NCP.


**Parameter table:**

+-----------+-----------------------------------------------------------------------+--------+-------------+
| Parameter | Description                                                           | Range  |             |
|           |                                                                       |        | Default     |
+===========+=======================================================================+========+=============+
| ncp-id    | Clears the flow-monitoring cache counters from the specified NCP only | 0..255 | \-          |
+-----------+-----------------------------------------------------------------------+--------+-------------+
| export    | Exports the flushed flows                                             | \-     | \-          |
+-----------+-----------------------------------------------------------------------+--------+-------------+


**Example**		
::		

    dnRouter# clear services flow-monitoring cache ncp 5		
    dnRouter# clear services flow-monitoring cache ncp 2 export		

 
.. **Help line:** clear counters for exported flows by flow-monitoring.		

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.4        | Command introduced    |
+-------------+-----------------------+
---

## clear rsvp statistics all.rst

clear rsvp statistics all
-------------------------

**Minimum user role:** operator

To clear all RSVP statistics on all interfaces and tunnels:

**Command syntax: clear rsvp statistics all**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - auto-bandwidth statistics remain unharmed

.. **Parameter table:**


**Example**
::

	dnRouter# clear rsvp statistics all 

.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+
---

## clear bmp server counters.rst

clear bmp server counters
-------------------------

**Minimum user role:** operator

To reset the bmp session messages counters:

**Command syntax: clear bmp server** [server-id] **counters** neighbor [neighbor-address]

**Command mode:** operation

.. **Hierarchies**

**Note**

- A command without a specific session-id clears counters per all configured bmp servers.

.. - neighbor-address - clear for counters of messages related to a specific neighbor

.. - support auto-complete for configured server-id

**Parameter table:**

+---------------------+--------------------------+-----------------------+-------------+
|                     |                          |                       |             |
| Parameter Name      | Description              | Range                 | Default     |
+=====================+==========================+=======================+=============+
|                     | The id of the bmp server | 0..4                  | \-          |
| server-id           |                          |                       |             |
+---------------------+--------------------------+-----------------------+-------------+
|                     | The neighbor ip address  | A.B.C.D               | \-          |
| neighbor-address    |                          | {ipv6 address format} |             |
+---------------------+--------------------------+-----------------------+-------------+


**Example**
::

	dnRouter# clear bmp server counters
	dnRouter# clear bmp server 0 counters
	dnRouter# clear bmp server counters neighbor 2.2.2.2
	dnRouter# clear bmp server 1 counters neighbor 2.2.2.2


.. **Help line:** Clear bmp session messages counters

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 15.1        | Command introduced    |
+-------------+-----------------------+
---

## clear ospf dynamic-spf counters.rst

clear ospf dynamic-spf counters
-------------------------------

**Minimum user role:** operator

To clear OSPF dynamic-spf statistics:

**Command syntax: clear ospf** instance [ospf-instance-name] **dynamic-spf counters**

**Command mode:** operation

.. **Hierarchies**

.. **Note**

	- use "instance [ospf-instance-name]" to clear information from a specific OSPF instance, when not specified, clear information from all OSPF instances

**Parameter table:**

+--------------------+----------------------------------------------------------------+---------------------------------------+-------------+
|                    |                                                                |                                       |             |
| Parameter          | Description                                                    | Range                                 | Default     |
+====================+================================================================+=======================================+=============+
| ospf-instance-name | clears the ospf information for the specified instance         | configured instances names            | all         |
+--------------------+----------------------------------------------------------------+---------------------------------------+-------------+

**Example**
::

	dnRouter# clear ospf dynamic-spf counters
	dnRouter# clear ospf instance instance1 dynamic-spf counters

.. **Help line:** Clear OSPF dynamic-spf information

**Command History**

+-------------+------------------------+
|             |                        |
| Release     | Modification           |
+=============+========================+
|             |                        |
| 25.2        | Command introduced     |
+-------------+------------------------+

---

## clear vpws counters.rst

clear vpws counters
-------------------

**Minimum user role:** operator

To reset the VPWS service instance counters:

**Command syntax: clear vpws [instance-name] counters**

**Command mode:** operation

.. **Hierarchies**

**Note**

- The Attachment Circuit (AC) counters are not reset.

**Parameter table**

+---------------+-------------------------------+--------+---------+
| Parameter     | Description                   | Range  | Default |
+===============+===============================+========+=========+
| instance-name | The configured VPWS instance. | String | \-      |
|               |                               | 1..255 |         |
+---------------+-------------------------------+--------+---------+

**Example**
::

	dnRouter# clear vpws R15_R16_1 counters


.. **Help line:**

**Command History**

+---------+---------------------------------------------------+
| Release | Modification                                      |
+=========+===================================================+
| 16.1    | Command introduced                                |
+---------+---------------------------------------------------+

---

## clear interfaces management static-route.rst

clear interface management static address-family route next-hop
-------------------------------------------------------------------

**Minimum user role:** operator


To remove the static route from the physical management bond interface:


**Command syntax: clear interfaces management [interface-name] static address-family [address-family] route** [ip-prefix] next-hop **[gateway]**

**Command mode:** operator

**Note:**


**Parameter table:**

+----------------+-------------------------------------------+-------+---------+
| Parameter      | Values                                    | Range | Default |
+================+===========================================+=======+=========+
| interface-name | mgmt-ncc-0, mgmt-ncc-1                    |       | \-      |
+----------------+-------------------------------------------+-------+---------+
| address-family | ipv4 / ipv6                               |       | \-      |
+----------------+-------------------------------------------+-------+---------+
| ip-prefix      | {ipv4-prefix format},{ipv6-prefix format} |       | \-      |
+----------------+-------------------------------------------+-------+---------+
| gateway        | ipv4 / ipv6 addresses                     |       | \-      |
+----------------+-------------------------------------------+-------+---------+


**Example:**
::

	dnRouter# clear interfaces management mgmt-ncc-0 static address-family ipv4 route 1.2.3.4/32 next-hop 4.2.3.1
	

.. **Help line:** Remove static route on management bond interface


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 16.2        | Command introduced    |
+-------------+-----------------------+
| 25.2        | Updated command syntax|
+-------------+-----------------------+
---

## clear netconf session.rst

clear netconf session 
----------------------

**Minimum user role:** operator

To clear active netconf sessions:

**Command syntax: clear netconf session** [session-id]

**Command mode:** operation

.. **Hierarchies**

**Note**

- By default, all sessions removed when session-id is not specified. 

**Parameter table:**

+---------------+-----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+-------------+
|               |                                                                                                                 |                                                                   |             |
| Parameter     | Description                                                                                                     | Range                                                             | Default     |
+===============+=================================================================================================================+===================================================================+=============+
|               |                                                                                                                 | Any active session-id displayed by "show system netconf sessions" |             |
| session-id    | Enter a specific session ID to clear (terminate). If you do not specify an ID, all sessions will be cleared.    |                                                                   | \-          |
+---------------+-----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+-------------+


**Example**
::

	dnRouter# clear netconf session 57
	NETCONF session MyUserName was successfully terminated
	
	dnRouter# clear netconf session 131
	NETCONF session MyUserName2 was successfully terminated
		
	dnRouter# clear netconf session
	NETCONF session MyUserName was successfully terminated
	NETCONF session MyUserName2 was successfully terminated


.. **Help line:** Clear active netconf session

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 10.0        | Command introduced    |
+-------------+-----------------------+
---

## clear system tech-support.rst

clear system tech-support
-------------------------

**Minimum user role:** operator

To stop the current creation of the tech-support file:

**Command syntax: clear system tech-support** 

**Command mode:** operation

.. **Hierarchies**

.. **Note**

.. **Parameter table**


**Example**
::

	dnRouter# clear system tech-support
	Success
	dnRouter#


.. **Help line:** Stops current tech-support file creation

**Command History**

+-------------+------------------------------------+
|             |                                    |
| Release     | Modification                       |
+=============+====================================+
|             |                                    |
| 11.0        | Command introduced                 |
+-------------+------------------------------------+
---

## clear segment-routing pcep counters.rst

clear segment-routing pcep counters
-----------------------------------

**Minimum user role:** operator

To reset the SR-TE PCEP session counters:

**Command syntax: clear segment-routing pcep counters** peer [ipv4-address]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - set "peer [ipv4-address]" to reset counters for a specific peer


**Parameter table:**

+-----------------+----------------------------------------------------+-----------+-------------+
| Parameter       | Description                                        | Range     | Default     |
+=================+====================================================+===========+=============+
| ipv4-address    | Clear PCEP counters for the specified peer only    | A.B.C.D   | \-          |
+-----------------+----------------------------------------------------+-----------+-------------+

**Example**
::

	dnRouter# clear segment-routing pcep counters
	dnRouter# clear segment-routing pcep counters peer 1.1.1.1



**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 16.2        | Command introduced    |
+-------------+-----------------------+
---

## clear system aaa-servers tacacs counters.rst

clear system aaa-servers tacacs counters
----------------------------------------

**Minimum user role:** operator

Clearing the TACACS counters resets the counters to zero and removes the counter information from the database.

To clear the tacacs counters:

**Command syntax: clear system aaa-servers tacacs counters [ip-address]**

**Command mode:** operation

.. **Hierarchies**

**Note**

- The TACACS server IP address is optional. If the IP address is not specified, all TACACS servers are cleared.

**Example**
::

	dnRouter# clear system aaa-servers tacacs counters
	dnRouter# clear system aaa-servers tacacs counters 1.1.1.1


.. **Help line:** clear system aaa-servers tacacs counters

**Command History**

+-------------+---------------------------------------+
|             |                                       |
| Release     | Modification                          |
+=============+=======================================+
|             |                                       |
| 25          | Command introduced                    |
+-------------+---------------------------------------+
---

## clear rsvp tunnels.rst

clear rsvp tunnels
------------------

**Minimum user role:** operator

To clear RSVP tunnels:

**Command syntax: clear rsvp tunnels** { soft \| optimize} {[type] \| [role] \| auto-mesh [template-name]} {destination-address [destination-address] \| name [name] \| state [state]  }

**Command mode:** operation

.. **Hierarchies**

**Note**

- Use destination-address, name or state to apply action to tunnels only matching the filter.


**Parameter table:**

+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| Parameter                 | Description                                                                                                                                                           | Range             |             |
|                           |                                                                                                                                                                       |                   | Default     |
+===========================+=======================================================================================================================================================================+===================+=============+
| no parameter              | Clear all RSVP tunnel sessions                                                                                                                                        | \-                | \-          |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| soft                      | Invokes make-before-break for head tunnels only. Other tunnel types won't reset.                                                                                      | \-                | \-          |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| optimize                  | Invoke optimization for all head tunnels. A tunnel optimized using the clear command is entered to the top of the optimization queue (first in line for optimization) | \-                | \-          |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| type                      | Clear specific tunnel types.                                                                                                                                          | primary           | \-          |
|                           | If the soft or optimize option is set, then setting the type will not affect transit or tail tunnels.                                                                 | bypass            |             |
|                           |                                                                                                                                                                       | auto-bypass       |             |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| role                      | Clear tunnels by role.                                                                                                                                                | head              | \-          |
|                           | Role cannot be used with soft or optimize options.                                                                                                                    | transit           |             |
|                           |                                                                                                                                                                       | tail              |             |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| destination-address       | Clear all RSVP tunnel sessions that match the specified destination-address                                                                                           | A.B.C.D           | \-          |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| name                      | Clear all RSVP tunnel sessions that match the specified tunnel name                                                                                                   | 1..255 characters | \-          |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| state                     | Clear all RSVP tunnel sessions that match the specified tunnel state                                                                                                  | up, down          | \-          |
|                           | Not valid for role transit or tail.                                                                                                                                   |                   |             |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| auto-mesh [template-name] | Clear auto-mesh tunnels by template name                                                                                                                              | \-                | \-          |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+

**Example**
::

	dnRouter# clear rsvp tunnels

	dnRouter# clear rsvp tunnels destination-address 3.3.3.3

	dnRouter# clear rsvp tunnels name TUNNEL_1

	dnRouter# clear rsvp tunnels state down

	dnRouter# clear rsvp tunnels soft

	dnRouter# clear rsvp tunnels optimize

	dnRouter# clear rsvp tunnels optimize auto-mesh PRIORITY_CORE

.. **Help line:**

**Command History**

+---------+---------------------------------------------------+
| Release | Modification                                      |
+=========+===================================================+
| 9.0     | Command introduced                                |
+---------+---------------------------------------------------+
| 10.0    | Added soft clear and clear by type                |
+---------+---------------------------------------------------+
| 11.0    | Added optimization and auto-mesh template options |
+---------+---------------------------------------------------+
| 11.2    | Added the ability to clear by tunnel role.        |
+---------+---------------------------------------------------+
---

## clear priority-flow-control counters.rst

clear priority-flow-control counters
------------------------------------

**Minimum user role:** operator

To clear the PFC counters, use the following command:

**Command syntax: clear priority-flow-control counters** [interface-name]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - **clear priority-flow-control counters** - clears all PFC counters on all interfaces

 - **clear priority-flow-control counters interface x** - clears all PFC counters on the specified interface

**Parameter table:**

+----------------+------------------------------------------------------------------------------+---------------------------------+---------+
| Parameter      | Description                                                                  | Range                           | Default |
+================+==============================================================================+=================================+=========+
| interface-name | Clears the PFC counters from the specified interface only.                   | ge<interface speed>-<A>/<B>/<C> | \-      |
|                | If you do not specify an [interface-name], all PFC counters will be cleared. |                                 |         |
+----------------+------------------------------------------------------------------------------+---------------------------------+---------+


**Example**
::

	dnRouter# clear priority-flow-control counters
	dnRouter# clear priority-flow-control counters ge100-1/1/1
	dnRouter# clear priority-flow-control counters ge100-0/0/0/1


.. **Help line:** clear priority-flow-control counters

**Command History**

+---------+-----------------------------------------------------------------------------------+
| Release | Modification                                                                      |
+=========+===================================================================================+
| 17.1    | Command introduced                                                                |
+---------+-----------------------------------------------------------------------------------+
---

## clear bridge-domain mac-table.rst

clear bridge-domain mac-table
-----------------------------

**Minimum user role:** operator

To remove/flush the learned mac-table entries of a bridge-domain:

**Command syntax: clear bridge-domain mac-table** {instance [instance-name]}
**Command syntax: clear bridge-domain mac-table** {instance [instance-name] interface [interface-name]}
**Command syntax: clear bridge-domain mac-table** {instance [instance-name] interface [interface-name] mac [mac-address]}

**Command mode:** operation

.. **Hierarchies**

**Note**

- Removes the MAC Table entry/entries.

**Parameter table**

+----------------+-----------------------------------------------+-------------------+---------+
| Parameter      | Description                                   | Range             | Default |
+================+===============================================+===================+=========+
| instance-name  | The configured bridge-domain instance.        | String            | \-      |
|                |                                               | 1..255            |         |
+----------------+-----------------------------------------------+-------------------+---------+
| interface-name | The name of the physical or bundle interface. | String            | \-      |
+----------------+-----------------------------------------------+-------------------+---------+
| mac-address    | The mac address to be removed.                | String            | \-      |
|                |                                               | xx:xx:xx:xx:xx:xx |         |
+----------------+-----------------------------------------------+-------------------+---------+

**Example**
::

	dnRouter# clear bridge-domain mac-table

    dnRouter# clear bridge-domain mac-table instance MyBridge1

    dnRouter# clear bridge-domain mac-table instance MyBridge1 interface bundle-10

    dnRouter# clear bridge-domain mac-table instance MyBridge1 interface bundle-10 mac a1:b2:98:21:fe:07

.. **Help line:**

**Command History**

+---------+---------------------------------------------------+
| Release | Modification                                      |
+=========+===================================================+
| 17.2    | Command introduced                                |
+---------+---------------------------------------------------+

---

## clear isis routes.rst

clear isis routes
-----------------

**Minimum user role:** operator

To clear IS-IS routes:

**Command syntax: clear isis** instance [isis-instance-name] **routes** address-family [address-family]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

 - use "instance [isis-instance-name]" to clear from a specific ISIS instance

 - use "address-family [address-family]" to clear specific address family routes


**Parameter table:**

+-----------------------+-------------------------------------------------------------+---------------------+-------------+
|                       |                                                             |                     |             |
| Parameter             | Description                                                 | Range               | Default     |
+=======================+=============================================================+=====================+=============+
|                       |                                                             |                     |             |
| no parameter          | Clear all IS-IS routes                                      | \-                  | \-          |
+-----------------------+-------------------------------------------------------------+---------------------+-------------+
|                       |                                                             |                     | \-          |
| isis-instance-name    | Clear IS-IS routes from the specified IS-IS instance        | 1..255 characters   |             |
+-----------------------+-------------------------------------------------------------+---------------------+-------------+
|                       |                                                             |                     | \-          |
| address-family        | Clear IS-IS routes for the specified address-family only    | IPv4                |             |
|                       |                                                             |                     |             |
|                       |                                                             | IPv6                |             |
+-----------------------+-------------------------------------------------------------+---------------------+-------------+


**Example**
::

	dnRouter# clear isis routes
	dnRouter# clear isis instance INST_A routes
	dnRouter# clear isis instance INST_A routes addres-family ipv4
	dnRouter# clear isis routes addres-family ipv6


.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 10.0        | Command introduced    |
+-------------+-----------------------+

---

## clear system cprl counters.rst

clear system cprl counters
--------------------------

**Minimum user role:** operator

To clear the CPRL matches and drop counters:

**Command syntax: clear system cprl counters** ncp [ncp]

**Command mode:** operation

.. **Hierarchies**

.. **Note**

**Parameter table**

+-----------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Description                                                                                                                                  |
+===========+==============================================================================================================================================+
| ncp-id    | Clear the counters for the specified NCP only.If you do not specify an NCP, the CPRL matches and drop counters for all NCPs will be cleared. |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------+

**Example**
::

	dnRouter# clear system cprl counters ncp 5
	dnRouter# clear system cprl counters


.. **Help line:** clear crpl matches and drop counters

**Command History**

+-------------+---------------------------------------------+
|             |                                             |
| Release     | Modification                                |
+=============+=============================================+
|             |                                             |
| 6.0         | Command introduced                          |
+-------------+---------------------------------------------+
|             |                                             |
| 9.0         | Command not supported                       |
+-------------+---------------------------------------------+
|             |                                             |
| 11.0        | Command reintroduced with new NCP filter    |
+-------------+---------------------------------------------+
---
