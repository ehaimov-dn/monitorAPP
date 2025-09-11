# System Operational Commands Complete Aggregation

This file contains the complete content from all RST files in:
1. Run Commands folder
2. Misc Commands folder
3. Request Commands folder
4. Recovery Mode Commands folder
5. Set Commands folder
6. GI Mode Commands folder

This comprehensive documentation covers all system operational commands including run commands, miscellaneous commands, request commands, recovery mode operations, set commands, and GI mode commands.


---

# SECTION 1: RUN COMMANDS

Files from Run Commands folder:       35 files

## run commands overview.rst

Run Commands Overview
---------------------
**Minimum user role:** operator

Run commands enable running general system commands, such as monitoring system processes, counters, ping, etc.

To initialize a run command:

**Command syntax: run**

**Command mode:** operation

**Example**
::

    dnRouter# run [argument]




where

[argument] - the specific run command that you want to perform

The following are the available arguments:

+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Argument                   | Description                                                                                                | Reference                             |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| monitor interface counters | Enables to monitor interface counters. The displayed information is refreshed every 1 second.              | run monitor interfaces counters       |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| ping                       | Enables to check the accessibility of a destination interface.                                             | run ping                              |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| traceroute                 | Enables to display the route that packets take to the specified destination address.                       | run traceroute                        |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| ping mpls rsvp             | Enables to check the accessibility of an RSVP tunnel                                                       | run ping mpls rsvp                    |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| ping mpls bgp-lu           | Enables to check the accessibility of a BGP-LU LSP                                                         | run ping mpls bgp-lu                  |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| traceroute mpls rsvp       | Enables to display the route that packets take along an RSVP tunnel                                        | run traceroute mpls rsvp              |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| traceroute mpls bgp-lu     | Enables to display the route that packets take along a BGP-LU LSP                                          | run traceroute mpls bgp-lu            |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| ssh                        | Enables to make a secure connection to another device.                                                     | run ssh                               |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| system datetime            | Manually set the system clock.                                                                             | set system datetime                   |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| timestamp                  | Turn on CLI timestamp.                                                                                     | set cli-timestamp                     |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| system snmp walk           | Retrieve and display the SNMP object values that are associated with the requested object identifier (oid) | run system snmp walk                  |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| system snmp get            | Retrieve and display one or more SNMP object values                                                        | run system snmp get                   |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| system snmp getnext        | Retrieve and display the next SNMP object values                                                           | run system snmp getnext               |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+
| run start shell            | Access the NCC shell                                                                                       | run start shell                       |
+----------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------+


---

## run ethernet-oam cfm on-demand delay-measurement.rst

run ethernet-oam cfm on-demand delay-measurement
------------------------------------------------

**Minimum user role:** operator

The CFM on-demand delay measurement command checks the connectivity, delay and delay variation metrics between MEPs in an L2 service. It uses a series of Y.1731 ETH-DM PDUs to determine whether or not the remote MEP is active, and the round-trip delay in the communication with a remote MEP.

**Command syntax: run ethernet-oam cfm on-demand delay-measurement two-way maintenance-domain [md-name] maintenance-association [ma-name] target {mac-address [dest-mac-address] | mep-id [remote-mep-id]}** interval [interval] count [count] detail

**Command mode:** operation

.. **Note**

	- The CFM on-demand command is one-line format. Meaning - all parameters can be entered in the same line.


.. **Help line:** run CFM on-demand single-ended two-way delay-measurement test


**Parameter table**

The following are the parameters that you can use for the CFM on-demand single-ended two-way delay-measurement command:

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| Parameter        | Description                                                                                                                                                                                                  | Range                                               | Default |
+==================+==============================================================================================================================================================================================================+=====================================================+=========+
| md-name          | Name of an existing CFM maintenance domain.                                                                                                                                                                  | String                                              | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| ma-name          | Name of an existing CFM maintenance association.                                                                                                                                                             | String                                              | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| dest-mac-address | Unicast MAC address of the peer MEP with which to perform CFM ethernet frame delay measurement test.                                                                                                         | XX:XX:XX:XX:XX:XX                                   | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| remote-mep-id    | Numeric identifier of the peer MEP with which to perform the CFM ethernet frame delay measurement test. The discovered MAC address of the peer MEP is used (if available).                                   | 1..8191                                             | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| interval         | Specifies the time in seconds between sending subsequent ETH-DM probes.                                                                                                                                      | 1 / 10 / 60 / 600                                   | 1       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| count            | Specifies the number of frames to send to the specified peer MEP.                                                                                                                                            | 1..65535                                            | 10      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| detail           | Prints a detailed output for every reply received.                                                                                                                                                           | Boolean                                             | false   |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+

The parameters can all be specified in the same command.

**Example**
::

	dnRouter# run ethernet-oam cfm on-demand delay-measurement two-way maintenance-domain MD1 maintenance-association MA1 target mac-address 7c:fe:90:57:73:13 count 10
	
	Two-way ETH-DM request to 7c:fe:90:57:73:13 (MEP-ID 3), from Interface ge100-0/0/0.100 MEP-ID 1 (7c:fe:90:57:73:10)
	Sending 10 Y.1731 ETH-DM probes, PCP: 0, interval: 1 second, timeout: 2 seconds

  	Transmitted DMM PDUs: 10, Received DMR PDUs: 10

	--- Delay measurement statistics ---
	DMM PDUs transmitted: 10, Valid DMR PDUs received: 10, Success rate is 100 percent (10/10)
	Round-trip-delay (min/avg/max): 92/103/122 usec 
	Jitter: 8 usec, Maximum delay variation: 30 usec


	dnRouter# run ethernet-oam cfm on-demand delay-measurement two-way maintenance-domain MD1 maintenance-association MA1 target mep-id 5
	
	Two-way ETH-DM request to 7c:fe:90:57:73:15 (MEP-ID 5), from Interface ge100-0/0/0.100 MEP-ID 1 (7c:fe:90:57:73:10)
	Sending 10 Y.1731 ETH-DM probes, PCP: 3, interval: 1 second, timeout: 2 seconds

  	Transmitted DMM PDUs: 10, Received DMR PDUs: 8

	--- Delay measurement statistics ---
	DMM PDUs transmitted: 10, Valid DMR PDUs received: 8, Success rate is 80 percent (8/10)
	Round-trip-delay (min/avg/max): 92/98/113 usec 
	Jitter: 7 usec, Maximum delay variation: 27 usec


	dnRouter# run ethernet-oam cfm on-demand delay-measurement two-way maintenance-domain MD1 maintenance-association MA1 target mep-id 5 detail
	
	Two-way ETH-DM request to 7c:fe:90:57:73:15 (MEP-ID 5), from Interface ge100-0/0/0.100 MEP-ID 1 (7c:fe:90:57:73:10)
	Sending 10 Y.1731 ETH-DM probes, PCP: 0, interval: 1 second, timeout: 2 seconds

	DMR received: Delay: 100 usec  Delay variation: 0 usec
	DMR received: Delay: 92 usec   Delay variation: 8 usec
	DMR received: Delay: 111 usec  Delay variation: 19 usec
	DMR received: Delay: 110 usec  Delay variation: 1 usec
	DMR received: Delay: 119 usec  Delay variation: 9 usec
	DMR received: Delay: 122 usec  Delay variation: 3 usec
	DMR received: Delay: 92 usec   Delay variation: 30 usec
	DMR received: Delay: 108 usec  Delay variation: 16 usec

	--- Delay measurement statistics ---
	DMM PDUs transmitted: 10, Valid DMR PDUs received: 8, Success rate is 80 percent (8/10)
	Round-trip-delay (min/avg/max): 92/98/113 usec 
	Jitter: 7 usec, Maximum delay variation: 27 usec


**Command History**

+---------+----------------------------------------------------------------------------------------+
| Release | Modification                                                                           |
+=========+========================================================================================+
| 19.3    | Command introduced                                                                     |
+---------+----------------------------------------------------------------------------------------+

---

## run ethernet-oam cfm on-demand linktrace.rst

run ethernet-oam cfm on-demand linktrace
----------------------------------------

**Minimum user role:** operator

Use the CFM on-demand link trace command to discover all hops to an L2 destination, and isolate faults:

**Command syntax: run ethernet-oam cfm on-demand linktrace maintenance-domain [md-name] maintenance-association [ma-name] target {mac-address [dest-mac-address] | mep-id [remote-mep-id]}** max-hops [max-hops] pcp [pcp]

**Command mode:** operation

.. **Note**

	- The CFM on-demand command is one-line format. Meaning - all parameters can be entered in the same line.


.. **Help line:** run CFM on-demand link trace test


**Parameter table**

The following are the parameters that you can use for the CFM on-demand link trace command:

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| Parameter        | Description                                                                                                                                                                                                  | Range                                               | Default |
+==================+==============================================================================================================================================================================================================+=====================================================+=========+
| md-name          | Name of an existing CFM maintenance domain.                                                                                                                                                                  | String                                              | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| ma-name          | Name of an existing CFM maintenance association.                                                                                                                                                             | String                                              | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| dest-mac-address | Unicast MAC address of the target peer MP for the CFM ethernet linktrace test.                                                                                                                               | XX:XX:XX:XX:XX:XX                                   | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| remote-mep-id    | Numeric identifier of the target peer MEP for the CFM ethernet linktrace test. The discovered MAC address of the peer MEP is used (if available).                                                            | 1..8191                                             | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| max-hops         | The maximum number of hops that the CFM ethernet linktrace frames should cross before timeout.                                                                                                               | 1..255                                              | 64      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| pcp              | 802.1p priority value of the CFM ETH-LT request frame. This parameter is not applicable when the source MEP resides on top of an untagged interface.                                                         | 0..7                                                | 0       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+

The parameters can all be specified in the same command.

**Example**
::

	dnRouter# run ethernet-oam cfm on-demand link-trace two-way maintenance-domain MD1 maintenance-association MA1 target mac-address 7c:fe:90:57:73:13

	Tracing the route to 7c:fe:90:57:73:13 (MEP-ID 4) in Maintenance Domain MD1, MD level 3, Maintenance Association MA1
	ETH-LT request sent via Interface ge100-0/0/0.100 MEP-ID 1 (7c:fe:90:57:73:10)
	TTL: 64, PCP: 0, ETH-LT timeout: 5 seconds

	Type ctrl+c to abort

	============================================================================================================================================
	Transaction Identifier: 0000000001
	============================================================================================================================================
	Hop		TTL		Source MAC address		Next hop MAC address		Previous hop MAC address		Ingress/Egress Action		Relay Action
	1		63		00:01:02:03:04:05		00:01:aa:bb:cc:dd			7c:fe:90:57:73:10				IngOk						RlyFDB
	2		62		00:01:aa:bb:cc:dd		00:01:02:cc:dd:ee			00:01:02:03:04:05				IngOk						RlyFDB
	3		61		00:01:02:cc:dd:ee		00:01:02:dd:ee:ff			00:01:aa:bb:cc:dd				IngOK/EgrOK					RlyMPDB
	4		*		*						*							*
	5		59		7c:fe:90:57:73:13		00:00:00:00:00:00			00:01:02:cc:dd:ee				IngOk						RlyHit


**Command History**

+---------+----------------------------------------------------------------------------------------+
| Release | Modification                                                                           |
+=========+========================================================================================+
| 25.1    | Command introduced                                                                     |
+---------+----------------------------------------------------------------------------------------+

---

## run ethernet-oam cfm on-demand loopback.rst

run ethernet-oam cfm on-demand loopback
---------------------------------------

**Minimum user role:** operator

The CFM on-demand loopback command provides a fault verification mechanism. It is the L2 MAC based equivalent of IP ping.

**Command syntax: run ethernet-oam cfm on-demand loopback maintenance-domain [md-name] maintenance-association [ma-name] target {mac-address [dest-mac-address] | mep-id [remote-mep-id]}** interval [interval] count [count] size [size] pcp [pcp]

**Command mode:** operation

.. **Note**

	- The CFM on-demand command is one-line format. Meaning - all parameters can be entered in the same line.

	- Remote MEPs or MIPs within the Maintenance Association which match the unicast destination MAC address will respond to the LBM frames.

	- Lost LBRs are loopback replies with expected sequence number that were not returned to the originator at all, or that arrived after the timeout.

	- Invalid LBRs are loopback replies that arrived with unexpected sequence number or malformed.

	- Out of order LBRs that arrived before timeout are counted as valid replies.

	- Test results:

		- Number of transmitted LBMs and valid received LBRs, and the calculated success rate.


.. **Help line:** run CFM on-demand loopback test


**Parameter table**

The following are the parameters that you can use for the CFM on-demand loopback command:

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| Parameter        | Description                                                                                                                                                                                                  | Range                                               | Default |
+==================+==============================================================================================================================================================================================================+=====================================================+=========+
| md-name          | Name of an existing CFM maintenance domain.                                                                                                                                                                  | String                                              | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| ma-name          | Name of an existing CFM maintenance assocciation.                                                                                                                                                            | String                                              | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| dest-mac-address | Unicast MAC address of the peer MEP or MIP with which to perform CFM ethernet loopback test.                                                                                                                 | XX:XX:XX:XX:XX:XX                                   | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| remote-mep-id    | Numeric identifier of the peer MEP with which to perform the CFM ethernet loopback test. The discovered MAC address of the peer MEP is used (if available).                                                  | 1..8191                                             | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| interval         | Specifies the time in seconds between sending subsequent ETH-LBM probes.                                                                                                                                     | 1..86400                                            | 1       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| count            | Specifies the number of frames to send to the specified target.                                                                                                                                              | 1..65535                                            | 10      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| size             | Specifies the size of LBM PDUs in bytes, excluding the ethernet header. The Data TLV is only included when the requested LBM PDU size is 12-1492 bytes.                                                      | 9..1492                                             | 9       |
|                  | If the specified size is smaller than 12 bytes, then it will default to 9 bytes as by default Data TLV is excluded (End TLV is always accounted for).                                                        |                                                     |         |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| pcp              | 802.1p priority value of the CFM ETH-LB request frame. (Used only for tagged subinterfaces)                                                                                                                  | 0..7                                                | 0       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+

The parameters can all be specified in the same command.

**Example**
::

	dnRouter# run ethernet-oam cfm on-demand loopback maintenance-domain MD1 maintenance-association MA1 target mac-address 7c:fe:90:57:73:13 count 10 interval 1 pcp 3
	
	ETH-LB request to 7c:fe:90:57:73:13 (MEP-ID 3), from interface ge100-0/0/0.100 MEP-ID 1 (7c:fe:90:57:73:10)
	Sending 10 Y.1731 ETH-LB probes, LBM PDU size: 9 bytes, PCP: 3, interval: 1 second, timeout: 2 seconds

	Legend :
	'!' - success, '.' - timeout, 'M' - malformed loopback reply


	Type ctrl+c to abort
	Current time: 2024-11-04 08:21:17.666259 :

	!!!!!.!!M!

	--- Loopback measurement statistics ---
	Transmitted LBM PDUs: 10, Received valid LBR PDUs: 8
	Received LBR PDUs: 9, Lost LBR PDUs: 1, Invalid LBR PDUs: 1
	Success rate is 80.00 percent (8/10)


**Command History**

+---------+----------------------------------------------------------------------------------------+
| Release | Modification                                                                           |
+=========+========================================================================================+
| 25.1    | Command introduced                                                                     |
+---------+----------------------------------------------------------------------------------------+
---

## run ethernet-oam cfm on-demand synthetic-loss-measurement.rst

run ethernet-oam cfm on-demand synthetic-loss-measurement
---------------------------------------------------------

**Minimum user role:** operator

The CFM on-demand synthetic loss measurement command checks the connectivity, and determine the near-end and far-end frame loss between MEPs in an L2 service. It uses a series of Y.1731 ETH-SL PDUs to determine service quality by injecting synthetic test traffic, as opposed to actual customer traffic.

**Command syntax: run ethernet-oam cfm on-demand synthetic-loss-measurement maintenance-domain [md-name] maintenance-association [ma-name] target {mac-address [dest-mac-address] | mep-id [remote-mep-id]}** interval [interval] count [count] pcp [pcp]

**Command mode:** operation

.. **Note**

	- The CFM on-demand command is one-line format. Meaning - all parameters can be entered in the same line.

	- Only remote peer MEPs within the Maintenance Association and matching the unicast destination MAC address will respond to the SLM frames.

	- Test results:

		- Near-end frame loss - frames lost on the way back from the remote node to the ETH-SL test initiator.

		- Far-end frame loss - frames lost on the way to the remote node from the ETH-SL test initiator.

		- Unacknowledged - number of frames without response by the end of ETH-SL test.


.. **Help line:** run CFM on-demand single-ended synthetic-loss-measurement test


**Parameter table**

The following are the parameters that you can use for the CFM on-demand single-ended two-way synthetic-loss-measurement command:

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| Parameter        | Description                                                                                                                                                                                                  | Range                                               | Default |
+==================+==============================================================================================================================================================================================================+=====================================================+=========+
| md-name          | Name of an existing CFM maintenance domain.                                                                                                                                                                  | String                                              | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| ma-name          | Name of an existing CFM maintenance assocciation.                                                                                                                                                            | String                                              | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| dest-mac-address | Unicast MAC address of the peer MEP with which to perform CFM ethernet frame delay measurement test.                                                                                                         | XX:XX:XX:XX:XX:XX                                   | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| remote-mep-id    | Numeric identifier of the peer MEP with which to perform the CFM ethernet frame delay measurement test. The discovered MAC address of the peer MEP is used (if available).                                   | 1..8191                                             | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| interval         | Specifies the time in seconds between sending subsequent ETH-SL probes.                                                                                                                                      | 1 / 10 / 60 / 600                                   | 1       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| count            | Specifies the number of frames to send to the specified peer MEP.                                                                                                                                            | 1..65535                                            | 10      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| pcp              | 802.1p priority value of the CFM ETH-SL request frame. (Used only for tagged subinterfaces)                                                                                                                  | 0..7                                                | 0       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+

The parameters can all be specified in the same command.

**Example**
::

	dnRouter# run ethernet-oam cfm on-demand synthetic-loss-measurement maintenance-domain MD1 maintenance-association MA1 target mac-address 7c:fe:90:57:73:13 count 100 interval 1 pcp 3
	
	Two-way ETH-SL request to 7c:fe:90:57:73:13 (MEP-ID 3), from interface ge100-0/0/0.100 MEP-ID 1 (7c:fe:90:57:73:10)
	Sending 100 Y.1731 ETH-SL probes, PCP: 3, interval: 1 second, timeout: 2 seconds

  	Transmitted SLM PDUs: 100, Received SLR PDUs: 80

	--- Synthetic loss measurement statistics ---
	SLM PDUs transmitted: 100, Remote SLM received: 100, Valid SLR PDUs received: 100, Unacknowledged SLR PDUs: 0
	Local TXFC1 value                : 100
	Local RXFC1 value                : 100
	Last received SLR frame TXFCf(tc): 100
	Last received SLR frame TXFCb(tc): 100

	ETH-SL frame loss:
	Frame loss near-end              : 0 (0.00%)
	Frame loss far-end               : 0 (0.00%)


	dnRouter# run ethernet-oam cfm on-demand synthetic-loss-measurement maintenance-domain MD1 maintenance-association MA1 target mac-address 7c:fe:90:57:73:13
	
	Cannot initiate ETH-SL test, another test is already in progress.


**Command History**

+---------+----------------------------------------------------------------------------------------+
| Release | Modification                                                                           |
+=========+========================================================================================+
| 19.2    | Command introduced                                                                     |
+---------+----------------------------------------------------------------------------------------+

---

## run ipmi shell.rst

run ipmi shell
--------------

**Minimum user role:** admin

To access the HostOS shell of an relevant element/node via the IPMI interface:

**Command syntax: run ipmi shell [node-name] [node-id]**

**Command mode:** operation

.. **Note**

	- "exit" commands reverts back to the DNOS CLI.

**Parameter table**

+-----------+-------------------------------------------------------------+-----------------------------------------------+
| Parameter | Description                                                 | Range                                         |
+===========+=============================================================+===============================================+
| node-name | Specify the node to which you want access to the ipmi shell | NCP                                           |
|           |                                                             | NCF                                           |
|           |                                                             | NCM                                           |
+-----------+-------------------------------------------------------------+-----------------------------------------------+
| node-id   | Specify the ID of the node you want to access               | NCC - 0..1                                    |
|           |                                                             | NCP - 0..(max NCP number per cluster type -1) |
|           |                                                             | NCF - 0..(max NCF number per cluster type -1) |
|           |                                                             | NCM - a0, b0, a1, b1                          |
+-----------+-------------------------------------------------------------+-----------------------------------------------+

**Example**
::

	dnRouter# run ipmi shell ncp 1
	root@wb12315812:/#

	root@wb12315812:/# exit
	dnRouter#

	dnRouter# run ipmi shell ncf 1
	root@wb12315812:/#

	root@wb12315812:/# exit
	dnRouter#

	dnRouter# run ipmi shell ncm a0
	root@wb12315812:/#

	root@wb12315812:/# exit
	dnRouter#

.. **Help line:** access to shell of the NCP/NCF/NCM components

**Command History**

+---------+----------------------------------+
| Release | Modification                     |
+=========+==================================+
| 11.0    | Command introduced               |
+---------+----------------------------------+
| 11.6    | Removed option to access the NCC |
+---------+----------------------------------+



---

## run monitor file.rst

run monitor file 
-----------------

**Minimum user role:** viewer

The run monitor file command enables to monitor live output of a selected file.

**Command syntax: run monitor file** { ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] } **[file-type] [file-name]**

**Command mode:** operation 

**Note**

- If you do not specify an NCE, the file from the active NCC will be monitored.

.. - monitor file should provide access only to specific folders where the files exist

	- The user should not have access to other folders

	- pressing tab should provide the list of available files in the folder

	- Each file type has a different location

	- master log file for each process should have alias name without the file extension ".log. i.e "run monitor file ldp" instead "run monitor file ldp.log". This is relevant ONLY to the master file name of each process (not the rotated files )

	- If no ncc-id/ncp-id/ncf-id was specified, the command relates to the active NCC

	- Each file type has a different location:

	- log - /var/log/dn/

	- traces - /var/log/dn/traces

	- file types to show files on NCCs:

	- log

	- traces - /var/log/dn/traces

	- file types to show files on NCPs/NCFs:

	- log

	- traces - /var/log/dn/traces

**Parameter table**

+-----------+----------------------------------------------------+--------+
| Parameter | Description                                        | Range  |
+===========+====================================================+========+
| ncc-id    | Monitors the file from the specified NCC           | 0..1   |
+-----------+----------------------------------------------------+--------+
| ncp-id    | Monitors the file from the specified NCP           | 0..191 |
+-----------+----------------------------------------------------+--------+
| ncf-id    | Monitors the file from the specified NCF           | 0..12  |
+-----------+----------------------------------------------------+--------+
| file-type | Specify the type of file that you want to monitor. | Log    |
|           |                                                    | Traces |
+-----------+----------------------------------------------------+--------+
| file-name | The name of the file you want to monitor.          | String |
+-----------+----------------------------------------------------+--------+

**Example**
::

	dnRouter# run monitor file log ldp
	
	dnRouter# run monitor file ncp 0 log bfd  
	

.. **Help line:** monitor file

**Command History**

+---------+---------------------------------------------------+
| Release | Modification                                      |
+=========+===================================================+
| 5.1.0   | Command introduced                                |
+---------+---------------------------------------------------+
| 10.0    | Command not supported                             |
+---------+---------------------------------------------------+
| 11.0    | Added option to monitor files from a specific NCE |
+---------+---------------------------------------------------+



---

## run monitor interfaces counters.rst

run monitor interfaces counters
-------------------------------

**Minimum user role:** viewer

This command displays the interface counters similarly to the show interfaces counters command, but with periodic updates allowing to monitor the counters. The displayed information is updated every 3 seconds.

**Command syntax: run monitor interfaces counters** [interface-name-list]

**Command mode:** operation

.. **Note**

	- This command performs "show interfaces counters" with a "watch" interval of 3 sec

	- Take into consideration cases of more than 3 screen output (More than X lines)

	- If list of interfaces is specified, table will be presented per specific list of interfaces only

**Parameter table**

+---------------------+-----------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                     | Range                                                 |
+=====================+=================================================================+=======================================================+
| interface-name-list | Filter the display to a list of interfaces separated by a space | -  ge<interface speed>-<A>/<B>/<C>                    |
|                     |                                                                 |                                                       |
|                     |                                                                 | -  ge<interface speed>-<A>/<B>/<C>.<sub-interface id> |
|                     |                                                                 |                                                       |
|                     |                                                                 | -  bundle-<bundle id>                                 |
|                     |                                                                 |                                                       |
|                     |                                                                 | -  bundle-<bundle id>.<sub-interface id>              |
|                     |                                                                 |                                                       |
|                     |                                                                 | -  mgmt0                                              |
+---------------------+-----------------------------------------------------------------+-------------------------------------------------------+

The following information is displayed per interface:

+-------------+-------------------------------------------------------------------------------------+
| Attribute   | Description                                                                         |
+=============+=====================================================================================+
| Interface   | The name of the interface                                                           |
+-------------+-------------------------------------------------------------------------------------+
| Operational | The state of the link (up/down)                                                     |
+-------------+-------------------------------------------------------------------------------------+
| Rx (Mbps)   | The received Megabits per second:                                                   |
|             | For physical interfaces, the value is derived from the “RX octets” Ethernet counter |
|             | For sub-interfaces, the value is derived from the “RX octets” Forwarding counter    |
+-------------+-------------------------------------------------------------------------------------+
| Tx (Mbps)   | The transmitted Megabits per second:                                                |
|             | For physical interfaces, the value is derived from the “TX octets” Ethernet counter |
|             | For sub-interfaces, the value is derived from the “TX octets” Forwarding counter    |
+-------------+-------------------------------------------------------------------------------------+
| Rx (pkts)   | The received packets:                                                               |
|             | For physical interfaces, the value is derived from the “RX frames” Ethernet counter |
|             | For sub-interfaces, the value is derived from the “RX packets” Forwarding counter   |
+-------------+-------------------------------------------------------------------------------------+
| Tx (pkts)   | The transmitted packets:                                                            |
|             | For physical interfaces, the value is derived from the “TX frames” Ethernet counter |
|             | For sub-interfaces, the value is derived from the “TX packets” Forwarding counter   |
+-------------+-------------------------------------------------------------------------------------+

**Example**
::


	dnRouter# run monitor interfaces counters
	| Interface    | Operational | RX[Mbps] | TX[Mbps]  | RX[pps] | TX[pps] | RX[pkts]  | TX[pkts] |
	+--------------+-------------+----------+-----------+---------+---------+-----------+----------|
	| ge100-1/1/1  | up          |        1 |         1 |    3124 | 10000000| 123456789 | 3124     |
	| bundle-2     | up          |        1 |         1 |    3124 | 12345678| 123456789 | 3124     |
	| bundle-2.100 | down        |        0 |         0 |       0 |        0| 123456789 | 3124     |


	dnRouter# run monitor interfaces counters bundle-2 bundle-2.100
	| Interface    | Operational | RX[Mbps] | TX[Mbps]  | RX[pps] | TX[pps] | RX[pkts]  | TX[pkts] |
	+--------------+-------------+----------+-----------+---------+---------+-----------+----------|
	| bundle-2     | up          |        1 |         1 |    3124 | 12345678| 123456789 | 3124     |
	| bundle-2.100 | down        |        0 |         0 |       0 |        0| 123456789 | 3124     |



.. **Help line:** monitor interface counters

**Command History**

+---------+----------------------------------------------------------------+
| Release | Modification                                                   |
+=========+================================================================+
| 5.1.0   | Command introduced                                             |
+---------+----------------------------------------------------------------+
| 11.2    | Added option to filter the monitoring for a list of interfaces |
+---------+----------------------------------------------------------------+

---

## run mtrace.rst

run mtrace
----------

**Minimum user role:** operator

You can use the command to run Mtrace to trace the route from a destination IP address to the root.

**Command syntax: run mtrace source-ip [source-ip] dest-host-ip [dest-host-ip] dest-ip-group [dest-ip-group]** response-ip [response-ip] ttl [ttl]

**Command mode:** operation 

**Note**

- The mtrace command must be in one-line format where all parameter are entered on the same line.

- The run mtrace source-ip [source-ip] dest-host-ip [dest-host-ip] dest-ip-group [dest-ip-group] runs the mtrace from [source-ip] to [dest-host-ip] via group dest-ip-group.

- The run mtrace source-ip [source-ip] dest-host-ip [dest-host-ip] dest-ip-group [dest-ip-group] response-ip [response-ip] runs the mtrace from [source-ip] to [dest-ip] via group dest-ip-group response to response-ip address.

.. - mtrace command is one-line format. meaning - all parameters should be entered on the same line

	- run mtrace source-ip [source-ip] dest-host-ip [dest-host-ip] dest-ip-group [dest-ip-group] - Run mtrace from [source-ip] to [dest-host-ip] via group dest-ip-group

	- run mtrace source-ip [source-ip] dest-host-ip [dest-host-ip] dest-ip-group [dest-ip-group] response-ip [response-ip] - Run mtrace from [source-ip] to [dest-host-ip] via group dest-ip-group respond to response-ip address

**Parameter table**

+---------------+-----------------------------------------+--------------------------------------------------------+---------+
| Parameter     | Description                             | Range                                                  | Default |
+===============+=========================================+========================================================+=========+
| source-ip     | The IP address of the source            | IPv4-host-address                                      |         |
+---------------+-----------------------------------------+--------------------------------------------------------+---------+
| dest-host-ip  | The IP address of the destination host  | IPv4-host-address                                      |         |
+---------------+-----------------------------------------+--------------------------------------------------------+---------+
| dest-ip-group | The IP address of the destination group | IPv4-multicast-group-address 224.0.1.0-239.255.255.255 |         |
+---------------+-----------------------------------------+--------------------------------------------------------+---------+
| response-ip   | The IP address of the response host     | IPv4-host-address                                      |         |
+---------------+-----------------------------------------+--------------------------------------------------------+---------+
| ttl           | The initial value of the IP header TTL  | 1-255                                                  | 127     |
+---------------+-----------------------------------------+--------------------------------------------------------+---------+

**Example**
::

	dnRouter# run mtrace source-ip 10.0.0.1 dest-host-ip 20.0.0.1 dest-ip-group 239.1.1.1

    Type escape sequence to abort.
	Mtrace from 10.0.0.1 to 20.0.0.1 via group 239.1.1.1
	From source (?) to destination (?)
	Querying full reverse path…

	0  20.0.0.1
	-1  192.168.24.5 PIM  [10.0.0.0/24]
	-2  192.168.24.6 PIM  [10.0.0.0/24]
	-3  192.168.52.5 PIM  [10.0.0.0/24]
	-4  192.168.15.6 PIM  [10.0.0.0/24]
	-5  10.0.0.1

	dnRouter# run mtrace source-ip 12.100.100.1 dest-host-ip 17.17.17.1 dest-ip-group 227.2.2.2 response-ip 12.24.24.1 ttl 4

    Type escape sequence to abort.
	Mtrace from 12.100.100.1 to 17.17.17.1 via group 227.2.2.2
	From source (?) to destination (?)
	Querying full reverse path…

	0  17.17.17.1
	-1  12.62.63.1 PIM  [12.100.100.0/24]
	-2  0.0.0.0 PIM  [12.100.100.0/24]
	-3  12.61.65.1 PIM  [12.100.100.0/24]
	-4  12.100.100.1 PIM  [12.100.100.1/32]

.. **Help line:** Run mtrace

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 12.0    | Command introduced |
+---------+--------------------+



---

## run packet-capture ncc.rst

run packet-capture ncc
----------------------

**Minimum user role:** operator

Packet capture control traffic of active NCC

Packet capture is a tool that helps operators to analyze network traffic and troubleshoot network problems. The packet capture tool captures real-time control and management data packets for monitoring and logging.

Packet capture operates like traffic sampling on the device, except that it captures entire packets including the Layer 2 header and saves the contents to a file in pcap format. Packet capture also captures IP fragments

Use Ctrl+C to stop capture

* Interface - Specify the required interface over the NCC control plane for which packet capture will run. The following interfaces are supported:
    * In-Band interfaces:
		- ge<interface speed>-<A>/<B>/<C>- capture all Rx/Tx packets on physical port
		- geX-<f>/<n>/<p>.<sub-interface id> - capture all Rx/Tx packets on physical sub interface
		- bundle-<id> - capture all Rx/Tx packets on bundle interface
		- bundle-<id>.<vlan-id> - capture all Rx/Tx packets on sub bundle interface
		- gre-tunnel-<x> - capture all Rx/Tx packets on gre-tunnel interface
		- high-scale-vrf-<vrf-id> - <vrf-id> is per vrf id known by “show network services vrf”.
			This interface carries all L3VPN Rx traffic for a specific non-default vrf. L3VPN traffic is traffic received with vpn label and designated to local cpu ("for us") in non-default vrf.

			This interface carries all Tx traffic (i.e from NCC) of specific vrf that the destination doesn’t match a route installed NCC forwarding tables. Which is:

			* RSVP route installed to unicast table
			* ISIS unicast route resolved by tunnel
			* Static-route resolved via mpls
			* BGP routes
			* Route to null0
		- any - capture on all in-band control interfaces for all vrfs. Capture is expected to result in packet duplications as different control interfaces carries the same packets


    * Out-of-band interfaces:
        - mgmt0 - Cluster OOB management interface.
        - mgmt-ncc-0 - Physical NCC0 OOB mgmt port.
        - mgmt-ncc-1 - Physical NCC1 OOB mgmt port.

* in-band-vrf - capture all Tx/Rx traffic of a non-default in-band vrf

* file-name - When specified, write capture to file instead of printing to screen.
	* Files will be named file-name.file_number.pcap. where:
	* file-name - the user requested file name
	* file_number - The rotation file number of the requested capture. A rotated file is created once capture size exceed file-size, start with 1. The first captured file will not have .file_number

* rotation-file-size - maximum size of a single rotation of the captured pcap file. Can only be used when file-name is set.

* verbosity - when capture output is printed to terminal, select verbosity of displayed information - low, medium or high
	* Low - When parsing and printing, produce (slightly more) verbose output. For example, the time to live, identification, total length and options in an IP packet are printed. Also enables additional packet integrity checks such as verifying the IP and ICMP header checksum.
	* Medium - additional fields are printed from NFS reply packets, and SMB packets are fully decoded.
	* High - Example elnet SB ... SE options are printed in full
* count - Support limiting packet-capture duration using count. use "unlimited" value for no count limit

* filter-expressions - Linux string filter expressions. See https://www.tcpdump.org/manpages/pcap-filter.7.html

**Command syntax: run packet-capture ncc { interface [interface-name] | in-band-vrf [non-default-inband-vrf] }** {file-name [file-name] rotation-file-size [rotation-file-size]| verbosity [verbosity]} count [count] filter-expression [filter-expression]

**Command mode:** operation

**Example:**
::

	dnRouter# run packet-capture ncc interface any verbosity low filter-expression 'tcp port 179'
	Listening on any, verbosity low, count 100000
	Type ctrl+c to abort

	15:57:45.103525 IP6 (class 0xc0, flowlabel 0xe6351, hlim 64, next-header TCP (6) payload length: 40) 2001:101::16.45585 > 2001:101:0:1::11f.bgp: Flags [S], cksum 0xbdeb (correct), seq 2986641117, win 36960, options [mss 9240,sackOK,TS val 873953361 ecr 0,nop,wscale 14], length 0
	15:57:45.103567 IP6 (class 0xc0, flowlabel 0xe6351, hlim 64, next-header TCP (6) payload length: 40) 2001:101::16.45585 > 2001:101:0:1::11f.bgp: Flags [S], cksum 0xbdeb (correct), seq 2986641117, win 36960, options [mss 9240,sackOK,TS val 873953361 ecr 0,nop,wscale 14], length 0
	15:57:45.103619 IP (tos 0xc0, ttl 64, id 60191, offset 0, flags [DF], proto TCP (6), length 60)
	    101.0.0.16.34637 > 101.0.1.115.bgp: Flags [S], cksum 0x397c (correct), seq 3375892311, win 37040, options [mss 9260,sackOK,TS val 470490934 ecr 0,nop,wscale 14], length 0
	15:57:45.103630 IP (tos 0xc0, ttl 64, id 60191, offset 0, flags [DF], proto TCP (6), length 60)
	    101.0.0.16.34637 > 101.0.1.115.bgp: Flags [S], cksum 0x397c (correct), seq 3375892311, win 37040, options [mss 9260,sackOK,TS val 470490934 ecr 0,nop,wscale 14], length 0
	15:57:45.103724 IP6 (class 0xc0, flowlabel 0x87c64, hlim 64, next-header TCP (6) payload length: 40) 2001:101::16.38689 > 2001:101:0:1::130.bgp: Flags [S], cksum 0x717d (correct), seq 1109688338, win 36960, options [mss 9240,sackOK,TS val 2186348560 ecr 0,nop,wscale 14], length 0
	15:57:45.103735 IP6 (class 0xc0, flowlabel 0x87c64, hlim 64, next-header TCP (6) payload length: 40) 2001:101::16.38689 > 2001:101:0:1::130.bgp: Flags [S], cksum 0x717d (correct), seq 1109688338, win 36960, options [mss 9240,sackOK,TS val 2186348560 ecr 0,nop,wscale 14], length 0
	15:57:45.103773 IP6 (class 0xc0, flowlabel 0x0c4cd, hlim 64, next-header TCP (6) payload length: 40) 2001:101::16.38145 > 2001:101:0:3::210.bgp: Flags [S], cksum 0x541a (correct), seq 323249823, win 36960, options [mss 9240,sackOK,TS val 4096392491 ecr 0,nop,wscale 14], length 0
	15:57:45.109344 IP (tos 0xc0, ttl 64, id 26854, offset 0, flags [DF], proto TCP (6), length 60)
	    101.0.0.16.44911 > 101.0.1.128.bgp: Flags [S], cksum 0x3547 (correct), seq 3978069164, win 37040, options [mss 9260,sackOK,TS val 1659376421 ecr 0,nop,wscale 14], length 0
	15:57:45.109357 IP (tos 0xc0, ttl 64, id 26854, offset 0, flags [DF], proto TCP (6), length 60)
	    101.0.0.16.44911 > 101.0.1.128.bgp: Flags [S], cksum 0x3547 (correct), seq 3978069164, win 37040, options [mss 9260,sackOK,TS val 1659376421 ecr 0,nop,wscale 14], length 0
	...



	dnRouter# run packet-capture ncc interface ge100-0/0/1 file-name BGP_Debug  filter-expression 'tcp port 179'
	Listening on ge100-0/0/1, writing to file BGP_Debug, rotation-size 50MB, count 100000
	Type ctrl+c to abort

	^C274 packets captured
	274 packets received by filter
	0 packets dropped by kernel


**Note:**

-  hostname resolution is disabled by default
-  Can only capture on interfaces in Up state
-  Using the packet-capture command can degrade router performance
-  Use Ctrl+C to stop capture.


**Parameter table:**

+------------------------+-------------------------------------------------------+-----------------------------------+
| Parameter              | Values                                                | Default value                     |
+========================+=======================================================+===================================+
| interface-name         | any                                                   |                                   |
|                        |                                                       |                                   |
|                        | ge<interface speed>-<A>/<B>/<C>                       |                                   |
|                        |                                                       |                                   |
|                        | ge<interface speed>-<A>/<B>/<C>.<sub-interface id>    |                                   |
|                        |                                                       |                                   |
|                        | bundle-<bundle id>                                    |                                   |
|                        |                                                       |                                   |
|                        | bundle-<bundle id>.<sub-interface id>                 |                                   |
|                        |                                                       |                                   |
|                        | gre-tunnel-<x>                                        |                                   |
|                        |                                                       |                                   |
|                        | high-scale-vrf-<vrf-id>                               |                                   |
|                        |                                                       |                                   |
|                        | mgmt0                                                 |                                   |
|                        |                                                       |                                   |
|                        | mgmt-ncc-0                                            |                                   |
|                        |                                                       |                                   |
|                        | mgmt-ncc-1                                            |                                   |
+------------------------+-------------------------------------------------------+-----------------------------------+
| non-default-inband-vrf | string                                                |                                   |
|                        |                                                       |                                   |
|                        | length 1..255                                         |                                   |
+------------------------+-------------------------------------------------------+-----------------------------------+
| file-name              | string                                                |                                   |
|                        |                                                       |                                   |
|                        | length 1..255                                         |                                   |
+------------------------+-------------------------------------------------------+-----------------------------------+
| rotation-file-size     | 1-1000 in MB                                          | 50MB                              |
+------------------------+-------------------------------------------------------+-----------------------------------+
| verbosity              | low, medium, high                                     | medium                            |
+------------------------+-------------------------------------------------------+-----------------------------------+
| count                  | 1..5000000 , unlimited                                | 100000                            |
+------------------------+-------------------------------------------------------+-----------------------------------+
| filter-expression      | tcpdump filter-expression string                      |                                   |
|                        |                                                       |                                   |
|                        | length 1..255                                         |                                   |
+------------------------+-------------------------------------------------------+-----------------------------------+


**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 16.2    | Command introduced                           |
+---------+----------------------------------------------+


---

## run ping mpls bgp-lu.rst

run ping mpls bgp-lu
--------------------

**Minimum user role:** operator

You can manually send MPLS-OAM LSP ping probes to check connectivity status of a BGP-LU LSP.

MPLS LSP ping - checks connectivity of LSPs: An MPLS echo request packet is sent through an LSP to validate it. When the packet reaches the end of the path, it is sent to the control plane of the egress LSR. The egress LSR then verifies whether it is indeed an egress for the FEC.

To start sending MPLS-OAM ping echo request probes towards a BGP-LU LSP:

**Command syntax: run ping mpls bgp-lu [target-address]** source-interface [source-interface] next-hop [next-hop-address] destination-address [destination-address] count [count] size [size] interval [interval] exp [exp] force-explicit-null

**Command mode:** operation

**Note**

- The target-address address family dictates the applicable source-interfaces (having IP address of the same AFI) and the valid destination-address range.

- If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

- Round-trip time (RTT) is computed over the successful echo requests only. Jitter is the standard-variation for delay between a source LER and a destination LER, between different echo requests.

.. - if user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), packet size will be the minimum size required and no padding will be used.

	- If packet is sent with MTU packet size bigger than path MTU, then MTU TX error counter will raise as no fragmentation is allowed.

	- Interval between sending echo request probe is the max{interval, min{reply-time, timeout}}

		- Interval - user configured minimum interval

		- reply-time - echo reply receive time

		- timeout - 2 seconds, timeout for waiting for an echo reply

	- If next-hop or egress-interface isn't valid path for the LSP echo request, return code of "no FEC mapping" will be applied.

	- Jitter is the standard-variation for delay between source LER and destination LER, between different echo requests.

	- round-trip-delay is computed over the successful echo requests only.

	- When there are multiple possible nexthops (ECMP) at headend, determined egress interface and outgoing label will be used.

	- User can stop ping requests using Ctrl+c

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                 | Range                                                                                                                                     | Default                                               |
+=====================+=============================================================================================================================================================================================================================================================================================================================================================+===========================================================================================================================================+=======================================================+
| target-address      | An IPv4 or IPv6 destination address FEC for BGP-LU FEC types. If the target-address is not a valid address known by BGP-LU, an error message is displayed.                                                                                                                                                                                                  | A.B.C.D/M                                                                                                                                 | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                             | X:X::X/M                                                                                                                                  |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                  | 1..255 characters (an existing interface name)                                                                                            | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an applicable AFI IP address, an error message is displayed.                                                                                                                                                                                                                                     |                                                                                                                                           |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                   |                                                                                                                                           |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop-address    | Specifies the BGP next hop as an IP address. Used for ECMP cases or if two entries exist in the RIB for the same FEC IP address.                                                                                                                                                                                                                            | A.B.C.D                                                                                                                                   | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                             | X:X::X                                                                                                                                    |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                 | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) or an IPv6 address from the range 0:0:0:0:0:FFFF:7F00:0/104 | 127.0.0.1 or 0:0:0:0:0:FFFF:7F00:1                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| count               | The number of echo requests to send in a single probe.                                                                                                                                                                                                                                                                                                      | 1..1000000                                                                                                                                | 5                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed. | 100..65507                                                                                                                                | packet size is determent according to the used TLVs   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| interval            | The minimum time interval (in seconds) between LSP ping messages. The interval is max{interval, min{reply-time, timeout}. That is, the highest value between the configured interval and either the echo reply receive time or the timeout (2 seconds) in case of no reply.                                                                                 | 1..86400                                                                                                                                  | 1                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IP header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                               | 0..7                                                                                                                                      | 0                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                | \-                                                                                                                                        | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::


	dnRouter# run ping mpls bgp-lu 1.2.3.4/32 count 10
	Sending 10 MPLS Echo requsts, size: 100, target ipv4-address: 1.2.3.4/32
	Timeout is 2 seconds, send interval is 1 second:

  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

	Type ctrl+c to abort
	- Aug 21 12:34:56.123:
	!!!!!.!!.!

	Success rate is 80 percent (8/10)
	Jitter: 1 msec
	Round-trip-delay (min/avg/max): 61/64/71 msec


	dnRouter# run ping mpls bgp-lu 2.2.2.2/32
	Sending 5 MPLS Echo requsts, size: 100, target ipv4-address: 2.2.2.2/32
	Timeout is 2 seconds, send interval is 1 second:

  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

	Type ctrl+c to abort
	- Aug 21 12:34:56.123:
	QQQQQ

	Success rate is 0 percent (0/5)




**Command History**

+---------+------------------------+
| Release | Modification           |
+=========+========================+
| 11.0    | Command introduced     |
+---------+------------------------+
| 15.0    | Updated command legend |
+---------+------------------------+
| 18.2    | Added support for IPv6 |
+---------+------------------------+

---

## run ping mpls evpn-vpws.rst

run ping mpls evpn-vpws
-----------------------

**Minimum user role:** operator

You can manually send MPLS-OAM ping probes to check connectivity status of evpn-vpws or evpn-vpws-seamless-integration service.

MPLS LSP ping - checks connectivity of LSPs: An MPLS echo request packet is sent through an LSP to validate it. When the packet reaches the end of the path, it is sent to the control plane of the egress LSR. The egress LSR then verifies whether it is indeed an egress for the FEC.

To start sending MPLS-OAM ping echo request probes towards evpn-vpws service:

**Command syntax: run ping mpls evpn-vpws instance [evpn-vpws-name]** source-interface [source-interface] next-hop [next-hop-address] destination-address [destination-address] count [count] size [size] interval [interval] exp [exp] target-address [target-address] sweep sweep-params[min-mtu,max-mtu,step-size] reply-mode [application-level-control-channel | ip-udp]

**Command mode:** operation 

**Note**

- If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

- Round-trip time (RTT) is computed over the successful echo requests only. Jitter is the standard-variation for delay between a source LER and a destination LER, between different echo requests.

.. -  If the user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), then packet size will be the minimum size required and no padding will be used.

	- If a packet is sent with packet size bigger than path MTU, then MTU TX error counter will raise as no fragmentation is allowed.

	- Interval between sending echo request probe is the max{interval, min{reply-time, timeout}}

	- Interval - user configured minimum interval

	- reply-time - echo reply receive time

	- timeout - 2 seconds, timeout for waiting for an echo reply

	- Jitter is the standard-variation for delay between source LER and destination LER, between different echo requests

	- round-trip-delay is computed over the successful echo requests only.

	- If next-hop or destination address is not valid path for the LSP echo request, then output code F ("no FEC mapping") will be printed.

	- If next-hop is invalid or specified with address-family different than destination address-family ip address, then error code Q will be printed, and message will be displayed on the screen notifying: “no route to host via specified next-hop”.

	- When there are multiple possible nexthops (ECMP) at headend, always the first learn nexthop is chosen.

	- Sweep - Used to determine the size of the maximum transmission unit (MTU) of the LSP. Uses lion in the desert algorithm between minimum-mtu and maximum-mtu which are optional parameters in sweep option.

	- User can stop ping requests using ctrl+c.

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                 | Range                                                                         | Default                                               |
+=====================+=============================================================================================================================================================================================================================================================================================================================================================+===============================================================================+=======================================================+
| evpn-vpws-name      | The name of the evpn-vpws instance. Can be either evpn-vpws instance or evpn-vpws-seamless-integration one. If the evpn-vpws instance doesn't exist or is not up, an error message is displayed.                                                                                                                                                            | 1..255 characters (an existing evpn-vpws instance name)                       | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| target-address      | The IPv4 address of the remote PE to ping. Used in multi-homing case.                                                                                                                                                                                                                                                                                       | A.B.C.D                                                                       | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                  | 1..255 characters (an existing interface name)                                | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an IPv4 address, an error message is displayed.                                                                                                                                                                                                                                                  |                                                                               |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                   |                                                                               |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop-address    | Specifies the next hop as an IP address. Used for ECMP cases or if two entries exist in the RIB for the same instance.                                                                                                                                                                                                                                      | A.B.C.D                                                                       | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                             | X:X::X                                                                        |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                 | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) | 127.0.0.1                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| count               | The number of echo requests to send in a single probe.                                                                                                                                                                                                                                                                                                      | 1..1000000                                                                    | 5                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed. | 100..9300                                                                     | packet size is determent according to the used TLVs   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| interval            | The minimum time interval (in seconds) between LSP ping messages. The interval is max{interval, min{reply-time, timeout}. That is, the highest value between the configured interval and either the echo reply receive time or the timeout (2 seconds) in case of no reply.                                                                                 | 1..86400                                                                      | 1                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IPv4 header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                             | 0..7                                                                          | 0                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| sweep               | Determine the size of the maximum transmission unit (MTU) of the LSP. Uses [min-mtu] and [max-mtu] as the sweep size range with [step-size] within the range.                                                                                                                                                                                               |                                                                               | sweep is not used by default. when using sweep:       |
|                     |                                                                                                                                                                                                                                                                                                                                                             |                                                                               | min-mtu - 100 (bytes)  max-mtu - 9300 (bytes)         |
|                     |                                                                                                                                                                                                                                                                                                                                                             |                                                                               | step-size - 4 (Bytes)                                 |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| sweep-params        | Define [min-mtu], [max-mtu] and [step-size] for case when sweep is selected                                                                                                                                                                                                                                                                                 | min-mtu 100..9300                                                             | All values should be divisible by 4.                  |
|                     |                                                                                                                                                                                                                                                                                                                                                             | min-mtu 100..9300                                                             |                                                       |
|                     |                                                                                                                                                                                                                                                                                                                                                             | step-size range  - 4..256 (bytes)                                             |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| reply-mode          | Reply mode for the ping request. can be either reply using an IPv4 or IPv6 UDP packet or reply using an application level control channel.                                                                                                                                                                                                                  | application-level-control-channel | ip-udp                                    | ip-udp                                                |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::

	dnRouter# run ping mpls evpn-vpws MyInstance count 10
	Sending 10 MPLS Echo requsts, size: 100, target: MyInstance
	Timeout is 2 seconds, send interval is 1 second:

  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code, 'C' - connection is down

	Type ctrl+c to abort
	- Aug 21 12:34:56.123:
	!!!!!.!!.!

	Success rate is 80 percent (8/10)
	Jitter: 1 msec
	Round-trip-delay (min/avg/max): 61/64/71 msec


	dnRouter# run ping mpls evpn-vpws MyInstance 
	Sending 5 MPLS Echo requsts, size: 100, target: MyInstance
	Timeout is 2 seconds, send interval is 1 second:

  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code, 'C' - connection is down

	Type ctrl+c to abort
	- Aug 21 12:34:56.123:
	CCCCC

	Success rate is 0 percent (0/5)

	dnRouter# run ping mpls evpn-vpws MyInstance sweep
	Sending 5 MPLS Echo requsts, size: sweep, target: MyInstance
	Timeout is 2 seconds, send interval is 1 second:

	Legend:
	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code, 'C' - connection is down

	Type ctrl+c to abort
	- Aug 21 12:34:56.123:
	100!9300.4700.2400.1250!1825.1537.1393!1465!1501.1483!1492!1496!
	--- lsp ping sweep result---
	Maximum Transmission Unit (MTU) is 1496 bytes

**Command History**

+---------+--------------------------------------+
| Release | Modification                         |
+=========+======================================+
| TBD     | Command introduced                   |
+---------+--------------------------------------+



---

## run ping mpls generic.rst

run ping mpls generic
---------------------

**Minimum user role:** operator

You can manually send MPLS-OAM LSP ping probes to check connectivity status of an LSP, regardless of protocol.

MPLS LSP ping - checks connectivity of LSPs: An MPLS echo request packet is sent through an LSP to validate it. When the packet reaches the end of the path, it is sent to the control plane of the egress LSR. The egress LSR then verifies whether it is indeed an egress for the FEC.

To start sending MPLS-OAM ping echo request probes towards LSP:

**Command syntax: run ping mpls generic [target-address]** source-interface [source-interface] next-hop [next-hop-address] destination-address [destination-address] count [count] size [size] interval [interval] exp [exp] force-explicit-null

**Command mode:** operation

**Note**

- The target-address address family dictates the applicable source-interfaces (having IP address of the same AFI) and the valid destination-address range.

- If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

- Round-trip time (RTT) is computed over the successful echo requests only. Jitter is the standard-variation for delay between a source LER and a destination LER, between different echo requests.

.. - if user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), packet size will be the minimum size required and no padding will be used.

	- If packet is sent with MTU packet size bigger than path MTU, then MTU TX error counter will raise as no fragmentation is allowed.

	- Interval between sending echo request probe is the max{interval, min{reply-time, timeout}}

		- Interval - user configured minimum interval

		- reply-time - echo reply receive time

		- timeout - 2 seconds, timeout for waiting for an echo reply

	- If next-hop or egress-interface isn't valid path for the LSP echo request, return code of "no FEC mapping" will be applied.

	- Jitter is the standard-variation for delay between source LER and destination LER, between different echo requests

	- round-trip-delay is computed over the successful echo requests only.

	- When there are multiple possible nexthops (ECMP) at headend, determined egress interface and outgoing label will be used.

	- User can stop ping requests using Ctrl+c

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                 | Range                                                                                                                                     | Default                                               |
+=====================+=============================================================================================================================================================================================================================================================================================================================================================+===========================================================================================================================================+=======================================================+
| target-address      | An IPv4 or IPv6 destination address FEC for generic FEC type (regardless of advertising routing protocol). If the target-address is not a valid address, an error message is displayed.                                                                                                                                                                     | A.B.C.D/M                                                                                                                                 | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                             | X:X::X/M                                                                                                                                  |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                  | 1..255 characters (an existing interface name)                                                                                            | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an applicable AFI IP address, an error message is displayed.                                                                                                                                                                                                                                     |                                                                                                                                           |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                   |                                                                                                                                           |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop-address    | Specifies the next hop as an IP address. Used for ECMP cases or if two entries exist in the RIB for the same FEC IP address.                                                                                                                                                                                                                                | A.B.C.D                                                                                                                                   | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                             | X:X::X                                                                                                                                    |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                 | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) or an IPv6 address from the range 0:0:0:0:0:FFFF:7F00:0/104 | 127.0.0.1 or 0:0:0:0:0:FFFF:7F00:1                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| count               | The number of echo requests to send in a single probe.                                                                                                                                                                                                                                                                                                      | 1..1000000                                                                                                                                | 5                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed. | 100..65507                                                                                                                                | packet size is determent according to the used TLVs   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| interval            | The minimum time interval (in seconds) between LSP ping messages. The interval is max{interval, min{reply-time, timeout}. That is, the highest value between the configured interval and either the echo reply receive time or the timeout (2 seconds) in case of no reply.                                                                                 | 1..86400                                                                                                                                  | 1                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IP header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                               | 0..7                                                                                                                                      | 0                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                | \-                                                                                                                                        | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::


	dnRouter# run ping mpls generic 1.2.3.4/32 count 10
	Sending 10 MPLS Echo requsts, size: 100, target ipv4-address: 1.2.3.4/32
	Timeout is 2 seconds, send interval is 1 second:

  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

	Type ctrl+c to abort
	- Aug 21 12:34:56.123:
	!!!!!.!!.!

	Success rate is 80 percent (8/10)
	Jitter: 1 msec
	Round-trip-delay (min/avg/max): 61/64/71 msec


	dnRouter# run ping mpls generic 2.2.2.2/32
	Sending 5 MPLS Echo requsts, size: 100, target ipv4-address: 2.2.2.2/32
	Timeout is 2 seconds, send interval is 1 second:

  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

	Type ctrl+c to abort
	- Aug 21 12:34:56.123:
	QQQQQ

	Success rate is 0 percent (0/5)




**Command History**

+---------+------------------------+
| Release | Modification           |
+=========+========================+
| 15.1    | Command introduced     |
+---------+------------------------+
| 18.2    | Added support for IPv6 |
+---------+------------------------+
---

## run ping mpls isis.rst

run ping mpls isis
-----------------------------

**Minimum user role:** operator

You can manually send MPLS-OAM LSP ping probes to check connectivity status across SR LSP set by the ISIS protocol.

MPLS LSP ping - checks connectivity of LSPs: An MPLS echo request packet is sent through an LSP to validate it. When the packet reaches the end of the path, it is sent to the control plane of the egress LSR. The egress LSR then verifies whether it is indeed an egress for the FEC.

To start sending MPLS-OAM ping echo request probes:

**Command syntax: run ping mpls isis [target-address]** source-interface [source-interface] next-hop [next-hop-address] destination-address [destination-address] count [count] size [size] interval [interval] exp [exp] stitched-protocol [stitched-protocol] force-explicit-null

**Command mode:** operation

**Note**

- The target-address address family dictates the applicable source-interfaces (having IP address of the same AFI) and the valid destination-address range.

- If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

- Round-trip time (RTT) is computed over the successful echo requests only. Jitter is the standard-variation for delay between a source LER and a destination LER, between different echo requests.

.. - If the user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), then packet size will be the minimum size required and no padding will be used.

  - If a packet is sent with packet size bigger than path MTU, then MTU TX error counter will raise as no fragmentation is allowed.

	- Interval between sending echo request probe is the max{interval, min{reply-time, timeout}}

  	- Interval - user configured minimum interval

  	- reply-time - echo reply receive time

  	- timeout - 2 seconds, timeout for waiting for an echo reply

  - Jitter is the standard-variation for delay between source LER and destination LER, between different echo requests

  - round-trip-delay is computed over the successful echo requests only.

  - If next-hop or destination address is not valid path for the LSP echo request, then output code F ("no FEC mapping") will be printed.

  - If next-hop is invalid or specified with address-family different than destination address-family ip address, then error code Q will be printed, and message will be displayed on the screen notifying: “no route to host via specified next-hop”.

  - When there are multiple possible nexthops (ECMP) at headend, determi
  ned egress interface and outgoing label will be used.

  - User can stop ping requests using ctrl+c.

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                 | Range                                                                                                                                     | Default                                               |
+=====================+=============================================================================================================================================================================================================================================================================================================================================================+===========================================================================================================================================+=======================================================+
| target-address      | An IPv4 or IPv6 destination address FEC for SR IS-IS FEC types. If the target-address is not a valid address known by IS-IS, an error message is displayed.                                                                                                                                                                                                 | A.B.C.D/M                                                                                                                                 | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                             | X:X::X/M                                                                                                                                  |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                  | 1..255 characters (an existing interface name)                                                                                            | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an applicable AFI IP address, an error message is displayed.                                                                                                                                                                                                                                     |                                                                                                                                           |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                   |                                                                                                                                           |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop-address    | Specifies the IS-IS next hop as an IP address. Used for ECMP cases or if two entries exist in the RIB for the same FEC IP address.                                                                                                                                                                                                                          | A.B.C.D                                                                                                                                   | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                             | X:X::X                                                                                                                                    |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                 | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) or an IPv6 address from the range 0:0:0:0:0:FFFF:7F00:0/104 | 127.0.0.1 or 0:0:0:0:0:FFFF:7F00:1                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| count               | The number of echo requests to send in a single probe.                                                                                                                                                                                                                                                                                                      | 1..1000000                                                                                                                                | 5                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed. | 100..65507                                                                                                                                | packet size is determent according to the used TLVs   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| interval            | The minimum time interval (in seconds) between LSP ping messages. The interval is max{interval, min{reply-time, timeout}. That is, the highest value between the configured interval and either the echo reply receive time or the timeout (2 seconds) in case of no reply.                                                                                 | 1..86400                                                                                                                                  | 1                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IP header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                               | 0..7                                                                                                                                      | 0                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                | \-                                                                                                                                        | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::


  dnRouter# run ping mpls isis 1.2.3.4/32 count 10
  Sending 10 MPLS echo requests, size: 100, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds, send interval is 1 second:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort
  - Aug 21 12:34:56.123:
  !!!!!.!!.!

  Success rate is 80 percent (8/10)
  Jitter: 1 msec
  Round-trip-delay (min/avg/max): 61/64/71 msec


  dnRouter# run ping mpls isis 2.2.2.2/32
  Sending 5 MPLS echo requests, size: 100, target ipv4-address: 2.2.2.2/32
  Timeout is 2 seconds, send interval is 1 second:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort
  - Aug 21 12:34:56.123:
  QQQQQ

  Success rate is 0 percent (0/5)



**Command History**

+---------+--------------------------------------+
| Release | Modification                         |
+=========+======================================+
| 15.0    | Command introduced                   |
+---------+--------------------------------------+
| 15.1    | Added support for protocol stitching |
+---------+--------------------------------------+
| 18.2    | Added support for IPv6               |
+---------+--------------------------------------+

---

## run ping mpls ldp.rst

run ping mpls ldp
-----------------

**Minimum user role:** operator

You can manually send MPLS-OAM LDP ping probes to check connectivity status across LSP set by the LDP protocol.

MPLS LSP ping - checks connectivity of LSPs: An MPLS echo request packet is sent through an LSP to validate it. When the packet reaches the end of the path, it is sent to the control plane of the egress LSR. The egress LSR then verifies whether it is indeed an egress for the FEC.

To start sending MPLS-OAM ping echo request probes:

**Command syntax: run ping mpls ldp [target-address]** source-interface [source-interface] next-hop [next-hop-address] destination-address [destination-address] count [count] size [size] interval [interval] exp [exp] stitched-protocol [stitched-protocol] force-explicit-null

**Command mode:** operation 

**Note**

- If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

- Round-trip time (RTT) is computed over the successful echo requests only. Jitter is the standard-variation for delay between a source LER and a destination LER, between different echo requests.

.. -  If the user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), then packet size will be the minimum size required and no padding will be used.

	- If a packet is sent with packet size bigger than path MTU, then MTU TX error counter will raise as no fragmentation is allowed.

	- Interval between sending echo request probe is the max{interval, min{reply-time, timeout}}

	- Interval - user configured minimum interval

	- reply-time - echo reply receive time

	- timeout - 2 seconds, timeout for waiting for an echo reply

	- Jitter is the standard-variation for delay between source LER and destination LER, between different echo requests

	- round-trip-delay is computed over the successful echo requests only.

	- If next-hop or destination address is not valid path for the LSP echo request, then output code F ("no FEC mapping") will be printed.

	- If next-hop is invalid or specified with address-family different than destination address-family ip address, then error code Q will be printed, and message will be displayed on the screen notifying: “no route to host via specified next-hop”.

	- When there are multiple possible nexthops (ECMP) at headend, always the first learn nexthop is chosen.

	- User can stop ping requests using ctrl+c.

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                 | Range                                                                         | Default                                               |
+=====================+=============================================================================================================================================================================================================================================================================================================================================================+===============================================================================+=======================================================+
| target-address      | An IPv4 destination address FEC for LDP types. If the target-address is not a valid address known by IS-IS, an error message is displayed.                                                                                                                                                                                                                  | A.B.C.D/M                                                                     | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                  | 1..255 characters (an existing interface name)                                | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an IPv4 address, an error message is displayed.                                                                                                                                                                                                                                                  |                                                                               |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                   |                                                                               |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop-address    | Specifies the IP address of the next hop LDP peer interface. Used for ECMP cases or if two entries exist in the RIB for the same FEC IPv4.                                                                                                                                                                                                                  | A.B.C.D                                                                       | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                 | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) | 127.0.0.1                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| count               | The number of echo requests to send in a single probe.                                                                                                                                                                                                                                                                                                      | 1..1000000                                                                    | 5                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed. | 100..9300                                                                     | packet size is determent according to the used TLVs   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| interval            | The minimum time interval (in seconds) between LSP ping messages. The interval is max{interval, min{reply-time, timeout}. That is, the highest value between the configured interval and either the echo reply receive time or the timeout (2 seconds) in case of no reply.                                                                                 | 1..86400                                                                      | 1                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IPv4 header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                             | 0..7                                                                          | 0                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| stitched-protocol   | The protocol stitched on an intermediate node. Specifying the stitched protocol is required in stitching scenarios as the transit LSR does not provide LSP ping replies with downstream information to report FEC stack change.                                                                                                                             | ISIS                                                                          |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                | \-                                                                            | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::

	dnRouter# run ping mpls ldp 1.2.3.4/32 count 10
	Sending 10 MPLS Echo requsts, size: 100, target ipv4-address: 1.2.3.4/32
	Timeout is 2 seconds, send interval is 1 second:

  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

	Type ctrl+c to abort
	- Aug 21 12:34:56.123:
	!!!!!.!!.!

	Success rate is 80 percent (8/10)
	Jitter: 1 msec
	Round-trip-delay (min/avg/max): 61/64/71 msec


	dnRouter# run ping mpls ldp 2.2.2.2/32
	Sending 5 MPLS Echo requsts, size: 100, target ipv4-address: 2.2.2.2/32
	Timeout is 2 seconds, send interval is 1 second:

  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

	Type ctrl+c to abort
	- Aug 21 12:34:56.123:
	QQQQQ

	Success rate is 0 percent (0/5)

**Command History**

+---------+--------------------------------------+
| Release | Modification                         |
+=========+======================================+
| 15.0    | Command introduced                   |
+---------+--------------------------------------+
| 15.1    | Added support for protocol stitching |
+---------+--------------------------------------+


---

## run ping mpls nil-fec.rst

run ping mpls nil-fec
---------------------

**Minimum user role:** operator

You can manually send MPLS-OAM LSP ping probes to check connectivity status of an LSP.

MPLS LSP ping - checks connectivity of LSPs: An MPLS echo request packet is sent through an LSP to validate it. When the packet reaches the end of the path, it is sent to the control plane of the egress LSR. The egress LSR then verifies whether it is indeed an egress for the FEC.

To start sending MPLS-OAM ping echo request probes towards LSP:

**Command syntax: run ping mpls nil-fec { labels [labels-stack] egress-interface [egress-interface] next-hop [next-hop-address] | policy [policy-name] }** source-interface [source-interface] destination-address [destination-address] count [count] size [size] interval [interval] exp [exp] force-explicit-null

**Command mode:** operation

**Note**

- The next-hop-address address family dictates the applicable source-interfaces (having IP address of the same AFI) and the valid destination-address range.

- If the next-hop or the egress-interface are not valid paths for the LSP echo request, a "no FEC mapping" return code is applied.

- Round-trip time (RTT) is computed over the successful echo requests only. Jitter is the standard-variation for delay between a source LER and a destination LER, between different echo requests.

.. - if user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), packet size will be the minimum size required and no padding will be used.

	- If packet is sent with MTU packet size bigger than path MTU, then MTU TX error counter will raise as no fragmentation is allowed.

	- Interval between sending echo request probe is the max{interval, min{reply-time, timeout}}

		- Interval - user configured minimum interval

		- reply-time - echo reply receive time

		- timeout - 2 seconds, timeout for waiting for an echo reply

	- If next-hop or egress-interface isn't valid path for the LSP echo request, return code of "no FEC mapping" will be applied.

	- Jitter is the standard-variation for delay between source LER and destination LER, between different echo requests

	- round-trip-delay is computed over the successful echo requests only.

	- When there are multiple possible nexthops (ECMP) at headend, determined egress interface and outgoing label will be used.

	- User can stop ping requests using Ctrl+c

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                 | Range                                                                                                                                     | Default                                               |
+=====================+=============================================================================================================================================================================================================================================================================================================================================================+===========================================================================================================================================+=======================================================+
| label-stack         | The label-stack to be sent. Specified as incoming labels for the responding nodes. Multiple labels are separated by commas, from top to bottom of stack.                                                                                                                                                                                                    | MPLS labels                                                                                                                               | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| policy-name         | The SR-TE policy name, from which the labels-stack to be sent is derived. Available policies will be listed for the user. If specified policy does not exist, then an error will be printed to the user.                                                                                                                                                    | 1..255 characters (an existing SR-TE policy name)                                                                                         | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                  | 1..255 characters (an existing interface name)                                                                                            | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an IP address matching next-hop AFI, an error message is displayed.                                                                                                                                                                                                                              |                                                                                                                                           |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                   |                                                                                                                                           |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| egress-interface    | Specifies the egress-interface from which the outgoing MPLS echo request is to be sent. Available interfaces under the VRF will be listed for the user.                                                                                                                                                                                                     | 1..255 characters (an existing interface name)                                                                                            | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop-address    | Specifies the next hop as an IP address. Used for ECMP cases or if two entries exist in the RIB for the same FEC IP address.                                                                                                                                                                                                                                | A.B.C.D                                                                                                                                   | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                             | X:X::X                                                                                                                                    |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                 | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) or an IPv6 address from the range 0:0:0:0:0:FFFF:7F00:0/104 | 127.0.0.1 or 0:0:0:0:0:FFFF:7F00:1                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| count               | The number of echo requests to send in a single probe.                                                                                                                                                                                                                                                                                                      | 1..1000000                                                                                                                                | 5                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed. | 100..65507                                                                                                                                | packet size is determent according to the used TLVs   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| interval            | The minimum time interval (in seconds) between LSP ping messages. The interval is max{interval, min{reply-time, timeout}. That is, the highest value between the configured interval and either the echo reply receive time or the timeout (2 seconds) in case of no reply.                                                                                 | 1..86400                                                                                                                                  | 1                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IP header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                               | 0..7                                                                                                                                      | 0                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                | \-                                                                                                                                        | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::


	dnRouter# run ping mpls nil-fec labels 16005,16007 egress-interface ge100-0/0/7 next-hop 10.1.1.1 count 10
	Sending 10 MPLS Echo requests with Nil FEC labels [16005,16007], size: 100
	Timeout is 2 seconds, send interval is 1 second:

  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

	Type ctrl+c to abort
	- Aug 21 12:34:56.123:
	!!!!!!!!!!

	Success rate is 100 percent (10/10)
	Jitter: 1 msec
	Round-trip-delay (min/avg/max): 61/64/71 msec


	dnRouter# run ping mpls nil-fec policy Policy1 count 10
	Sending 10 MPLS Echo requests with Nil FEC for SR-TE policy Policy1, size: 100
	Timeout is 2 seconds, send interval is 1 second:

  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

	Type ctrl+c to abort
	- Aug 21 12:34:56.123:
	!!!!!.!!.!

	Success rate is 80 percent (8/10)
	Jitter: 1 msec
	Round-trip-delay (min/avg/max): 61/64/71 msec




**Command History**

+---------+------------------------+
| Release | Modification           |
+=========+========================+
| 15.1    | Command introduced     |
+---------+------------------------+
| 18.2    | Added support for IPv6 |
+---------+------------------------+
---

## run ping mpls ospf.rst

run ping mpls ospf
-------------------

**Minimum user role:** operator

You can manually send MPLS-OAM LSP ping probes to check connectivity status across an SR LSP set by the OSPF protocol.

MPLS LSP ping - checks connectivity of LSPs: An MPLS echo request packet is sent through an LSP to validate it. When the packet reaches the end of the path, it is sent to the control plane of the egress LSR. The egress LSR then verifies whether it is indeed an egress for the FEC.

To start sending MPLS-OAM ping echo request probes:

**Command syntax: run ping mpls ospf [target-address]** source-interface [source-interface] next-hop [next-hop] destination-address [destination-address] count [count] size [size] interval [interval] exp [exp] force-explicit-null

**Command mode:** operation

**Note**

- If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

- Round-trip time (RTT) is computed over the successful echo requests only. Jitter is the standard-variation for delay between a source LER and a destination LER, between different echo requests.

.. - If the user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), then packet size will be the minimum size required and no padding will be used.

  - If a packet is sent with packet size bigger than path MTU, then MTU TX error counter will raise as no fragmentation is allowed.

	- Interval between sending echo request probe is the max{interval, min{reply-time, timeout}}

  	- Interval - user configured minimum interval

  	- reply-time - echo reply receive time

  	- timeout - 2 seconds, timeout for waiting for an echo reply

  - Jitter is the standard-variation for delay between source LER and destination LER, between different echo requests

  - round-trip-delay is computed over the successful echo requests only.

  - If next-hop or destination address is not valid path for the LSP echo request, then output code F ("no FEC mapping") will be printed.

  - If next-hop is invalid or specified with address-family different than destination address-family ip address, then error code Q will be printed, and message will be displayed on the screen notifying: “no route to host via specified next-hop”.

  - When there are multiple possible nexthops (ECMP) at headend, determi
  ned egress interface and outgoing label will be used.

  - User can stop ping requests using ctrl+c.

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                 | Range                                                                         | Default                                               |
+=====================+=============================================================================================================================================================================================================================================================================================================================================================+===============================================================================+=======================================================+
| target-address      | An IPv4 destination address FEC for SR OSPF types. If the target-address is not a valid address known by OSPF, an error message is displayed.                                                                                                                                                                                                               | A.B.C.D/M                                                                     | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                  | 1..255 characters (an existing interface name)                                | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an IPv4 address, an error message is displayed.                                                                                                                                                                                                                                                  |                                                                               |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                   |                                                                               |                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop            | Specifies the OSPF next hop as an IP address. Used for ECMP cases or if two entries exist in the RIB for the same FEC IPv4.                                                                                                                                                                                                                                 | A.B.C.D                                                                       | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                 | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) | 127.0.0.1                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| count               | The number of echo requests to send in a single probe.                                                                                                                                                                                                                                                                                                      | 1..1000000                                                                    | 5                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed. | 100..9300                                                                     | packet size is determent according to the used TLVs   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| interval            | The minimum time interval (in seconds) between LSP ping messages. The interval is max{interval, min{reply-time, timeout}. That is, the highest value between the configured interval and either the echo reply receive time or the timeout (2 seconds) in case of no reply.                                                                                 | 1..86400                                                                      | 1                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IPv4 header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                             | 0..7                                                                          | 0                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                | \-                                                                            | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::


  dnrouter# run ping mpls ospf 1.2.3.4/32 count 10
  Sending 10 MPLS echo requests, size: 100, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds, send interval is 1 second:

  Legend:
   '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface,
  'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping,
  'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown,
  'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry,
  'P' - no receive interface label protocol, 'p' - premature termination of the LSP
  'l' - label switched with FEC stack change, 'd' - see DDMAP for return code,
  'X' - undefined return code, 'x' - no return code,

  Type ctrl+c to abort
  - Aug 21 12:34:56.123:
  !!!!!.!!.!

  Success rate is 80 percent (8/10)
  Jitter: 1 msec
  Round-trip-delay (min/avg/max): 61/64/71 msec


  dnrouter# run ping mpls ospf 2.2.2.2/32
  Sending 5 MPLS echo requests, size: 100, target ipv4-address: 2.2.2.2/32
  Timeout is 2 seconds, send interval is 1 second:

  Legend:
   '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface,
  'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping,
  'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown,
  'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry,
  'P' - no receive interface label protocol, 'p' - premature termination of the LSP
  'l' - label switched with FEC stack change, 'd' - see DDMAP for return code,
  'X' - undefined return code, 'x' - no return code,

  Type ctrl+c to abort
  - Aug 21 12:34:56.123:
  QQQQQ

  Success rate is 0 percent (0/5)



**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## run ping mpls rsvp.rst

run ping mpls rsvp
------------------

**Minimum user role:** operator

You can manually send MPLS-OAM LSP ping probes to check connectivity status of an RSVP tunnel.

MPLS LSP ping - checks connectivity of LSPs: An MPLS echo request packet is sent through an LSP to validate it. When the packet reaches the end of the path, it is sent to the control plane of the egress LSR. The egress LSR then verifies whether it is indeed an egress for the FEC.

To start sending MPLS-OAM ping echo request probes towards an RSVP tunnel tail end:

**Command syntax: run ping mpls rsvp [tunnel-name]** destination-address [destination-address] count [count] size [size] interval [interval] exp [exp] force-explicit-null

**Command mode:** operation 

**Note**

- If you run the command on a tunnel that does not exist, or if the tunnel is down, an error message is displayed.

- Round-trip time (RTT) are computed over the successful echo requests only. Jitter is the standard-variation of a tunnel head to a tunnel tail destination delay between different echo requests.

.. - if user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), packet size will be the minimum size required and no padding will be used.

	- If packet is sent with mtu packet size bigger than path mtu, then MTU TX error counter will raise as no fragmentation is allowed.

	- Interval between sending echo request probe is the max{interval, min{reply-time, timeout}}

		- Interval - user configured minimum interval

		- reply-time. echo reply receive time

		- timeout - 2 seconds, timeout for waiting to an echo reply

	- In case the user uses a non-existing tunnel, the following message will be displayed: "no tunnel exists"

	- In case tunnel is down, an echo request will not be sent, and the following message will be displayed "no tunnel exists". The packet count is incremented.

	- Jitter is the standard-variation of Tunnel head to Tunnel tail destination delay between different echo requests

	- round-trip-delay is computed over the successful echo requests only. 

	- User can stop ping requests using Ctrl+c

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                 | Range                                                                         | Default                                             |
+=====================+=============================================================================================================================================================================================================================================================================================================================================================+===============================================================================+=====================================================+
| tunnel-name         | The name of an existing tunnel to ping. You can ping any tunnel type: primary, bypass, auto-bypass, auto-mesh.                                                                                                                                                                                                                                              | 1..255 characters                                                             | \-                                                  |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                 | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) | 127.0.0.1                                           |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| count               | The number of echo requests to send in a single probe.                                                                                                                                                                                                                                                                                                      | 1..1000000                                                                    | 5                                                   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed. | 100..65507                                                                    | packet size is determent according to the used TLVs |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| interval            | The minimum time interval (in seconds) between LSP ping messages. The interval is max{interval, min{reply-time, timeout}. That is, the highest value between the configured interval and either the echo reply receive time or the timeout (2 seconds) in case of no reply.                                                                                 | 1..86400                                                                      | 1                                                   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IPv4 header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                             | 0..7                                                                          | 0                                                   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                | \-                                                                            | \-                                                  |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+

**Example**
::

	
	dnRouter# run ping mpls rsvp TUNNEL_1
	Sending 5 MPLS Echo requests, size: 100, target rsvp tunnel: TUNNEL_1
	Timeout is 2 seconds, send interval is 1 second: 
	
  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code
	
	
	Type ctrl+c to abort 
	- Aug 21 12:34:56.123: 
	!.!!! 
	
	Success rate is 80 percent (4/5)
	Jitter: 1 msec
	Round-trip-delay (min/avg/max): 61/64/71 msec


	dnRouter# run ping mpls rsvp TUNNEL_2
	Sending 5 MPLS Echo requests, size: 100, target rsvp tunnel: TUNNEL_2
	Timeout is 2 seconds, send interval is 1 second: 
	
  	Legend:
  	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code
	
	
	Type ctrl+c to abort 
	- Aug 21 12:34:56.123: 
	QQQQQ
	
	Success rate is 0 percent (0/5)
	

**Command History**

+---------+------------------------+
| Release | Modification           |
+=========+========================+
| 11.0    | Command introduced     |
+---------+------------------------+
| 15.0    | Updated command legend |
+---------+------------------------+


---

## run ping multicast.rst

run ping multicast
------------------

**Minimum user role:** operator

You can use the command to ping a multicast destination IP address. If the source IP or source interface is not specified the an arbitrary IP address of one of the router interfaces is selected by default.

**Command syntax:run ping multicast [group-ip-address]**  {source-interface [source-interface] \| source-ip [source-address]} interval [interval] ttl [ttl] size [size] count [count] dscp [dscp] df

**Command mode:** operation

**Note**

- The ping command must be in one-line format where all parameter are entered on the same line.

- The run ping [group-ip-address] source-interface[source-interface] command - the ping packet must be sent with the indicated source interface IPv4 address.

.. - ping command is one-line format. meaning - all parameters can be entered on the same line

	- run ping [group-ip-address] source-interface [source-interface] - The ping packet should be sent with the indicated source interface IPv4 address.

	- ttl - the initial value of the IP header TTL.

	- Count - number or probe sequences per command

	- dscp - DSCP value

	- Size - ICMP payload

	- Df - don't fragment - flag which specifies that outgoing packet shouldn't be fragmented and should be sent as is with original size. If size exceeds the egress interface mtu, then the packet will be dropped, by default, fragmentation is performed automatically

**Parameter table**

The following are the parameters for this command:

+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| Parameter        | Description                                                                                                                                                                                                                                                                 | Range                                              | Default |
+==================+=============================================================================================================================================================================================================================================================================+====================================================+=========+
| group-ip-address | IPv4-multicast-address                                                                                                                                                                                                                                                      | A.B.C.D                                            | \-      |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| source-interface | ge<interface speed>-<A>/<B>/<C>                                                                                                                                                                                                                                             | ge<interface speed>-<A>/<B>/<C>                    | \-      |
|                  | ge<interface speed>-<A>/<B>/<C>.<sub-interface id>                                                                                                                                                                                                                          | ge<interface speed>-<A>/<B>/<C>.<sub-interface id> |         |
|                  | bundle-<bundle id>                                                                                                                                                                                                                                                          | bundle-<bundle id>                                 |         |
|                  | bundle-<bundle id>.<sub-interface id>                                                                                                                                                                                                                                       | bundle-<bundle id>.<sub-interface id>              |         |
|                  | lo<lo-interface id>                                                                                                                                                                                                                                                         | lo<lo-interface id>                                |         |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| source-address   | Source IPv4 address                                                                                                                                                                                                                                                         | A.B.C.D                                            | \-      |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| interval         | The wait time between sending packets                                                                                                                                                                                                                                       | 1-86,400 (seconds)                                 | 1       |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| ttl              | The initial value of the IP header TTL                                                                                                                                                                                                                                      | 1-255                                              | 30      |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| size             | The ICMP payload                                                                                                                                                                                                                                                            | 1-65507                                            | 56      |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| count            | Number or probe sequences per command                                                                                                                                                                                                                                       | 1-1,000,000                                        | 5       |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| dscp             | DSCP value                                                                                                                                                                                                                                                                  | 0-56                                               | 0       |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| df               | Don't fragment - use this flag to specify that the outgoing packet shouldn't be fragmented and should be sent as is with its original size. If the size exceeds the egress interface MTU, the packet will be dropped. By default, fragmentation is performed automatically. | Boolean                                            | \-      |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+

**Example**
::

	dnRouter# run ping multicast 224.1.1.20 source-interface lo0 ttl 30 size 1000 count 5

	Type escape sequence to abort.
	Sending 5, 100-byte ICMP Echos to 224.1.1.20, timeout is 2 seconds:
	Packet sent with a source address of 1.1.1.1

	 [<- 10.0.48.1]224.1.1.20 : [0], 1028 bytes, 0.34 ms (0.34 avg, 0% loss)
	 [<- 10.0.57.1]224.1.1.20 : [0], 1028 bytes, 0.35 ms (0.34 avg, 0% loss)
	 [<- 10.0.48.1]224.1.1.20 : [1], 1028 bytes, 0.30 ms (0.32 avg, 0% loss)
	 [<- 10.0.57.1]224.1.1.20 : [1], 1028 bytes, 0.30 ms (0.32 avg, 0% loss)
	 [<- 10.0.48.1]224.1.1.20 : [2], 1028 bytes, 0.39 ms (0.34 avg, 0% loss)
	 [<- 10.0.57.1]224.1.1.20 : [2], 1028 bytes, 0.39 ms (0.34 avg, 0% loss)
	 [<- 10.0.48.1]224.1.1.20 : [3], 1028 bytes, 0.38 ms (0.35 avg, 0% loss)
	 [<- 10.0.57.1]224.1.1.20 : [3], 1028 bytes, 0.38 ms (0.35 avg, 0% loss)
	 [<- 10.0.48.1]224.1.1.20 : [4], 1028 bytes, 0.40 ms (0.36 avg, 0% loss)

	 224.1.1.20 : xmt/rcv/%loss = 5/5/0%, min/avg/max = 0.30/0.36/0.40

	dnRouter# run ping multicast 227.1.1.1 source-ip 12.1.21.1 ttl 30 size 1000 count 5

	Type escape sequence to abort.
	Sending 5, 100-byte ICMP Echos to 224.1.1.20, timeout is 2 seconds:
	Packet sent with a source address of 12.1.21.1

	 [<- 10.0.48.1]224.1.1.20 : [0], 1028 bytes, 0.34 ms (0.34 avg, 0% loss)
	 [<- 10.0.57.1]224.1.1.20 : [0], 1028 bytes, 0.35 ms (0.34 avg, 0% loss)
	 [<- 10.0.48.1]224.1.1.20 : [1], 1028 bytes, 0.30 ms (0.32 avg, 0% loss)
	 [<- 10.0.57.1]224.1.1.20 : [1], 1028 bytes, 0.30 ms (0.32 avg, 0% loss)
	 [<- 10.0.48.1]224.1.1.20 : [2], 1028 bytes, 0.39 ms (0.34 avg, 0% loss)
	 [<- 10.0.57.1]224.1.1.20 : [2], 1028 bytes, 0.39 ms (0.34 avg, 0% loss)
	 [<- 10.0.48.1]224.1.1.20 : [3], 1028 bytes, 0.38 ms (0.35 avg, 0% loss)
	 [<- 10.0.57.1]224.1.1.20 : [3], 1028 bytes, 0.38 ms (0.35 avg, 0% loss)
	 [<- 10.0.48.1]224.1.1.20 : [4], 1028 bytes, 0.40 ms (0.36 avg, 0% loss)

	 224.1.1.20 : xmt/rcv/%loss = 5/5/0%, min/avg/max = 0.30/0.36/0.40

.. **Help line:** run ping for multicast

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 12.0    | Command introduced |
+---------+--------------------+

---

## run ping.rst

run ping
--------

**Minimum user role:** viewer

The ping command checks the accessibility of a destination interface. It uses a series of Internet Control Message Protocol (ICMP) Echo messages to determine whether or not the remote host is active, the round-trip delay in the communication with the host, and packet loss.

**Command syntax: run ping [dest-ip]** vrf [vrf-name] source-interface [source-interface] interval [interval] size [size] count [count] dscp [dscp] df skip-source-check
**Command syntax: run ping [host-name]** vrf [vrf-name] source-interface [source-interface] interval [interval] size [size] count [count] dscp [dscp] df skip-source-check

**Command mode:** operation

**Note**

- The NCC handles ICMP packets. Therefore, ping to a remote host should be done from the NCC and not from the NCPs.

- All VRFs in the system are listed and made available, including the 4 system-default VRFs (default, mgmt0, mgmt-ncc-0 and mgmt-ncc-1). Unless a valid VRF is explicitly specified, the default VRF is used.

- The run ping command may include the source-interface. When a VRF is specified, only relevant source-interfaces attached to that VRF will be listed under it and made available. Otherwise, only interfaces under the default VRF are listed.

..
	- The ping command is one-line format. meaning - all parameters can be entered on the same line

		- dscp - ipv4/6 dscp value

		- Count - number or probe sequences per command

		- Size - ICMP payload

   		- Interval - resolution of 0.001 seconds

		- Df - don't fragment - a flag which specifies that outgoing packet shouldn't be fragmented and should be sent as is with original size. If size exceeds the egress interface mtu, then the packet will be dropped, by default, fragmentation is performed automatically. This option is only valid for IPv4 addresses.

	- By default source-address should be assigned based on RIB resolution of egress-interface towards the destination

	- If ping is initiated towards BGP-VPN prefix, then a random source-address will be assigned based on any attached UP interface with configured IP address inside the VRF. If no interface is attached, error message should be printed stating: "Cannot assign source address"

	- DNS resolution for ping command requested with host-name address within a VRF is done per system based on DNS servers priorities

	- If the IP destination address is a Link-Local address, then an applicable source interface will be chosen and link-local source address will be used (or retrieved from source-interface). If the IP destination address is a Global Unicast address, then an applicable source interface will be chosen and a global unicast source address will be used (or retrieved from source-interface)


.. **Help line:** run ICMP ping request


**Parameter table**

The following are the parameters that you can use for the ping command:

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| Parameter        | Description                                                                                                                                                                                                  | Range                                               | Default |
+==================+==============================================================================================================================================================================================================+=====================================================+=========+
| dest-ip          | The IPv4/IPv6 address of the target host to ping                                                                                                                                                             | A.B.C.D                                             | \-      |
|                  |                                                                                                                                                                                                              | x:x::x:x                                            |         |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| host-name        | The name of the target host to ping                                                                                                                                                                          | String                                              | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| vrf-name         | The name of the target VRF                                                                                                                                                                                   | String                                              | default |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| source-interface | Sends the ping packets with the defined IP address of the source interface                                                                                                                                   | ge<interface speed>-<A>/<B>/<C>                     | \-      |
|                  |                                                                                                                                                                                                              |                                                     |         |
|                  |                                                                                                                                                                                                              | ge<interface speed>-<A>/<B>/<C>.<sub-interface id>  |         |
|                  |                                                                                                                                                                                                              |                                                     |         |
|                  |                                                                                                                                                                                                              | bundle-<bundle id>                                  |         |
|                  |                                                                                                                                                                                                              |                                                     |         |
|                  |                                                                                                                                                                                                              | bundle-<bundle id>.<sub-interface id>               |         |
|                  |                                                                                                                                                                                                              |                                                     |         |
|                  |                                                                                                                                                                                                              | lo<lo-interface id>                                 |         |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| interval         | Specifies the time in seconds between sending ping packets (resolution of 0.001 seconds)                                                                                                                     | 0.001..86,400                                       | 1       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| size             | Specifies the number of data bytes to be added to the ping packet                                                                                                                                            | 1..65507                                            | 56      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| count            | Specifies the number of ping packets that will be sent                                                                                                                                                       | 1..1,000,000                                        | 5       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| dscp             | The IPv4/IPv6 DSCP value                                                                                                                                                                                     | 0..56                                               | 0       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| df               | Do not fragment - a flag specifying that outgoing packets must not be fragmented. The packets will be sent in their original size. If the size exceeds the egress interface MTU, the packet will be dropped  | Boolean                                             | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| skip-source-check| Skip source address check. This option allows pinging without verifying the source address of the reply packets                                                                                              | Boolean                                             | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+

The parameters can all be specified in the same command.

**Example**
::

	dnRouter# run ping 1.1.1.1
	dnRouter# run ping google.com
	dnRouter# run ping 2001:1234::1
	dnRouter# run ping 10.0.0.1 source-interface lo0
	dnRouter# run ping 1.1.1.1 skip-source-check
	dnRouter# run ping 1.1.1.1 count 200
	dnRouter# run ping 1.1.1.1 interval 2
	dnRouter# run ping 1.1.1.1 size 1500
	dnRouter# run ping 1.1.1.1 interval 2 size 1000 dscp 40
	dnRouter# run ping 1.1.1.1 vrf mgmt0 count 20
	dnRouter# run ping 1.1.1.1 vrf mgmt-ncc-0 count 20
	dnRouter# run ping 1.1.1.1 vrf mgmt-ncc-1 source-interface mgmt-ncc-1 size 600
	dnRouter# run ping 1.1.1.1 vrf MyVrf1 df


**Command History**

+---------+----------------------------------------------------------------------------------------+
| Release | Modification                                                                           |
+=========+========================================================================================+
| 5.1.0   | Command introduced                                                                     |
+---------+----------------------------------------------------------------------------------------+
| 11.0    | Removed VRF filter, added option to ping a host-name, dscp, and option to not fragment |
+---------+----------------------------------------------------------------------------------------+
| 13.0    | Updated interval parameter values                                                      |
+---------+----------------------------------------------------------------------------------------+
| 13.1    | Added support for host VRF                                                             |
+---------+----------------------------------------------------------------------------------------+
| 13.3    | Updated interval parameter values from 0.1 seconds to 0.001 seconds                    |
+---------+----------------------------------------------------------------------------------------+
| 16.1    | Removed egress-interface knob                                                          |
+---------+----------------------------------------------------------------------------------------+
| 25.2    | Command syntax change                                                                  |
+---------+----------------------------------------------------------------------------------------+
---

## run remote-loopback-check.rst

run remote-loopback-check
-------------------------

**Minimum user role:** operator

You can manually send probes to verify fiber and SFP functionality TX to RX.

Fiber loop verification is performed using ping. Echo packets are sent over looped interface (patch Tx to Rx) to validate the fiber and SFP by transmission and reciept of packets.

To run the fiber loop verification:

**Command syntax: run remote-loopback-check interface [interface-name]** count [count] interval [interval] size [size] timeout [timeout]

**Command mode:** operation

**Note**

- If a packet is sent with packet size bigger than path MTU, then MTU TX error counter will raise as no fragmentation is allowed.

- The minimum time interval (in seconds) between ping messages. The interval is max{interval, min{reply-time, timeout}}. That is, the highest value between the configured interval and either the echo reply receive time or the timeout (2 seconds) in case of no reply.

- Jitter is the standard-variation for delay between different echo requests.

- Round-trip-delay is computed over the successful echo requests only.

- User can stop ping requests using ctrl+c.

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                 | Range                                                                         | Default                                               |
+=====================+=============================================================================================================================================================================================================================================================================================================================================================+===============================================================================+=======================================================+
| interface-name      | The interface from which to trigger the fiber verification test                                                                                                                                                                                                                                                                                             | 1..255 characters (an existing interface name)                                | \-                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| count               | The number of echo requests to send in a single probe.                                                                                                                                                                                                                                                                                                      | 1..1000000                                                                    | 1000                                                  |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| interval            | The minimum time interval (in seconds) between ping messages. The interval is max{interval, min{reply-time, timeout}. That is, the highest value between the configured interval and either the echo reply receive time or the timeout (2 seconds) in case of no reply.                                                                                     | 1..86400                                                                      | 1 millisecond                                         |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum value, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed.                       | 1..65507                                                                      | 100 bytes                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| timeout             | The time to wait before declaring an echo request as lost.                                                                                                                                                                                                                                                                                                  | 1..86400                                                                      | 2000 milliseconds                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+


**Example**
::

	dnRouter# run remote-loopback-check interface ge100-0/0/15 timeout 10
	Sending 1000 Echo requests, size: 100, interface: ge100-0/0/15
	Timeout is 10 milliseconds, send interval is 1 millisecond:

	Legend:
	'!' - success, '.' - timeout

	Type ctrl+c to abort
	-2022-06-28 11:26:16.837322:

	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!.!!!.!!!!.!!!.!!!.!!!!.!!!.!!!!!.!!!!.!!!.!!!!.!!!!.!!!!!.!!!!.!!!.!!!!.!!!.!!!!.!!!!!.!!!.!!!!.!!!.!!!!.!!!!.!!!!!.!!!.!!!!.!!!.!!!!.!!!.!!!!!.!!!!.!!!.!!!!.!!!!.!!!.!!!!!.!!!!.!!!.!!!!.!!!.!!!!.!!!!!.!!!.!!!!.!!!.!!!!.!!!.!!!!!.!!!!.!!!.!!!!.!!!.!!!!!.!!!!.!!!.!!!!.!!!!.!!!.!!!!!.!!!!.!!!!.!!!.!!!!.!!!.!!!!!.!!!!.!!!.!!!.!!!!.!!!!.!!!!!.!!!.!!!!.!!!!.!!!.!!!!.!!!!!.!!!!.!!!.!!!!.!!!!.!!!.!!!!!.!!!.!!!!.!!!.!!!!.!!!.!!!!!.!!!!.!!!!.!!!.!!!!.!!!.!!!!!.!!!!.!!!.!!!!.!!!.!!!!!.!!!!.!!!.!!!!.!!!.!!!!.!!!!!.!!!.!!!!.!!!.!!!!.!!!.!!!!!.!!!!.!!!.!!!!.!!!.!!!!.!!!!!.!

	Success rate is 88.10 percent (881/1000)
	Jitter: 0.01 msec
	Round-trip-delay (min/avg/max): 0.09/0.10/0.49 msec


	dnRouter# run remote-loopback-check interface ge100-0/0/1 count 10
	Sending 10 Echo requests, size: 100, interface: ge100-0/0/1
	Timeout is 2 milliseconds, send interval is 1 millisecond:

	Legend:
	'!' - success, '.' - timeout

	Type ctrl+c to abort
	-2022-06-22 12:58:37.347470:

	..........

	Success rate is 0.00 percent (0/10)
	Jitter: - msec
	Round-trip-delay (min/avg/max): -/-/- msec


	dnRouter# run remote-loopback-check interface ge100-0/0/1.250
	ERROR: Cannot set source interface 'ge100-0/0/0.250'. The source interface does not exist.


	dnRouter# run remote-loopback-check interface ge100-0/0/1
	ERROR: Cannot set source interface 'ge100-0/0/1'. Source interface must have admin-state enabled.


	dnRouter# run remote-loopback-check interface ge100-0/0/1
	ERROR: Cannot set source interface 'ge100-0/0/1'. Source interface must have an IPv4 address configured.

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## run ssh.rst

run ssh
-------

**Minimum user role:** viewer

The run ssh command enables to make a secure connection from the system to another device. This command is supported for default/non-default VRF interfaces and for mgmt0 out-of-band interfaces.

If you do not specify either an egress-interface or source-address, the SSH packets will be generated via the in-band management channel with a source IP address according to the default VRF routing table.

**Command syntax: run ssh [user-name]@[dest-ip]|[host-name]** {vrf [vrf-name] \| {egress-interface [egress-interface] | source-address [source-address] } }

**Command mode:** operation 

.. **Note**

	- ssh command is one-line format. meaning - all parameters can be entered on the same line

	- run ssh[dest-ip]egress-interface  `[egress-interface] <https://drivenets.atlassian.net/wiki/display/DV/source-ip>`__- defines source IP of the packet to IP address of the egress interface. If "egress-interface"=mgmt0, linux command "ssh [ip-address]" should be run in a context of default NS, i.e. SSH will run in out-of-band.

	- run ssh [dest-ip] source-address [source-address] - set source ip-address for SSH packets.

	- If neither egress-interface nor source-address parameter was set, SSH packets are generated via in-band management channel with source IP address according to default VRF routing table
	
	- If both egress-interface and source-address parameters were set, egress-interface will overrule source-address and the source IP of the packet will be the IP address of the egress interface

    - If vrf is specified the connection will be established over the specified VRF, and the egress-interface will be allowed only from the selected VRF.

	- ability to specify host-name instead of dest-ip address is supported starting from v11.2 only

**Parameter table**

+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+---------+
| Parameter           | Description                                                                                                                                                                                                                                  | Range                                | Default |
+=====================+==============================================================================================================================================================================================================================================+======================================+=========+
| user-name@dest-ip   | The IPv4 or IPv6 host address of the device to which to connect. The user-name indicates the current user.                                                                                                                                   | A.B.C.D                              | \-      |
|                     |                                                                                                                                                                                                                                              | x:x::x:x                             |         |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+---------+
| user-name@host-name | The host-name of the device to which to connect. The user-name indicates the current user.                                                                                                                                                   | A partial or full domain name.       | \-      |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+---------+
| source-address      | Sends the SSH packets with the defined ip address as a source address.                                                                                                                                                                       | A.B.C.D                              | \-      |
|                     |                                                                                                                                                                                                                                              | xx:xx::xx:xx                         |         |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+---------+
| egress-interface    | Sets the IP address of the egress-interface as the source IP address of outgoing SSH packets. If the egress interface is mgmt0, the SSH packets are sent via the OOB management network (i.e. they are transmitted via the mgmt0 interface). | All default VRF interfaces and mgmt0 | \-      |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+---------+
| vrf-name            | The name of the VRF through which the connect will be established.                                                                                                                                                                           | The VRF name                         | \-      |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+---------+

**Example**
::

	dnRouter# run ssh user@1.1.1.1
	dnRouter# run ssh user@1.1.1.1 egress-interface lo0
	dnRouter# run ssh user@1.1.1.1 source-address 5.5.5.5
	dnRouter# run ssh user@dnCoreRouter-2
	dnRouter# run ssh user@1.1.1.1 egress-interface irb4 vrf my-vrf
	

.. **Help line:** run ssh

**Command History**

+---------+---------------------------------------------------------+
| Release | Modification                                            |
+=========+=========================================================+
| 5.1.0   | Command introduced                                      |
+---------+---------------------------------------------------------+
| 11.5    | Added option to connect to a device using the host-name |
+---------+---------------------------------------------------------+
| 19.1    | Added non default inband management VRF support         |
+---------+---------------------------------------------------------+


---

## run start shell.rst

run start shell
---------------

**Minimum user role:** admin

To access a node's shell container:

**Command syntax: run start shell** {ncc [ncc-id] \| ncp [ncp-id]} container [container-name]
**Command syntax: run start shell ncc active** container [container-name]
**Command syntax: run start shell ncf [ncf-id]**
**Command syntax: run start shell ncm [ncm-id]**

**Command mode:** operation

**Note**

- TACACS+ AAA (recovery mode) is allowed for local users only.

- The command in recovery mode provides access to the shell of the active NCC only.

- root@node-manager - an NCC prompt. The prompt varies depending on the accessed NCE .

.. - "exit" commands reverts back to the DNOS CLI.

	bfd-master - access ncp that holds all non uBFD, BFD sessions

**Parameter table**

+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Parameter      | Description                                                                                            | Range                                                                        |
+================+========================================================================================================+==============================================================================+
| ncc-id         | Provides access to the shell of the specified NCC                                                      | 0..1                                                                         |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ncp-id         | Provides access to the shell of the specified NCP                                                      | 0..(max NCP number per cluster type -1), bfd-master                          |
|                | bfd-master - provides access to the ncp that holds all non uBFD, BFD sessions.                         |                                                                              |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ncf-id         | Provides access to the shell of the specified NCF                                                      | 0..(max NCF number per cluster type -1)                                      |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| container-name | Provides access to the container within the specified node.                                            | A container from the process list that applicable to the specified node name |
|                | The container option is not applicable to NCMs.                                                        |                                                                              |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ncm-id         | Provides access to the shell of the specified NCM                                                      | a0, b0, a1, b1                                                               |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ncc active     | Provides access to containers in the current active NCC. When set, a container name must be specified. | \-                                                                           |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+

If you do not provide a node name and ID, you will be granted access to the active NCC's shell.

If you do not specify a container within the node, you will be granted access to the following containers by default:

+-----------+--------------------------+
| Node Type | Default Container        |
+===========+==========================+
| NCC       | routing-engine container |
+-----------+--------------------------+
| NCP       | datapath container       |
+-----------+--------------------------+
| NCF       | fabric container         |
+-----------+--------------------------+

To return to the DNOS CLI, use the exit command.

**Example**
::

	dnRouter# run start shell
	root@routing-engine:/#

	root@routing-engine:/# exit
	dnRouter#

	dnRouter# run start shell ncc 0 container routing-engine
	root@routing-engine:/#

	root@routing-engine:/# exit
	dnRouter#

	dnRouter# run start shell ncc active container node-manager
	root@node-manager:/#

	root@node-manager:/# exit
	dnRouter#

	dnRouter# run start shell ncf 1
	root@fabric-engine:/#

	root@fabric-engine:/# exit
	dnRouter#

	dnRouter# run start shell ncm a1
	root@ncm:/#

	root@ncm:/# exit
	dnRouter#

.. **Help line:** access to shell of the NCC/NCP/NCF/NCM components

**Command History**

+---------+-----------------------------------------------------+
| Release | Modification                                        |
+=========+=====================================================+
| 10.0    | Command introduced                                  |
+---------+-----------------------------------------------------+
| 11.0    | Command added to recovery mode                      |
+---------+-----------------------------------------------------+
| 11.5    | Added option to access containers of the active NCC |
+---------+-----------------------------------------------------+
| 13.0    | Added new ncp option for command - bfd-master       |
+---------+-----------------------------------------------------+
| 25.2    | Command syntax change                               |
+---------+-----------------------------------------------------+
---

## run system snmp get.rst

run system snmp get
-------------------

**Minimum user role:** viewer

To retrieve and display one or more SNMP object values:

**Command syntax: run system snmp get {[oid] \| [mib-name]}** {[oid] \| [mib-name]}.. {full \| numerical} log [log-file-name]

**Command mode:** operation 

**Note**

- This command is executed using a specific community (v2) named dn_community, which has a "view" configuration attached, named view_default. The output will be displayed within the scope of the supported configured view for the community. This view is restricted only from inside the system (local host). No Lawful Interception (LI) MIBs are exported.

.. - Restricted view response:

	- No LI mibs are exported

	- Linux implementation examples:

	- For SNMP v2c configuration:

	- snmpget -v 2c -c dn_community <local-host address> <mib-oid/name>

	- for logging: snmpget -v 2c -c dn_community <local-host address> <mib-oid/name> -Lf <log-file>

**Parameter table**

The parameters are:

+---------------+------------------------------------------------------------------------------------------------+
| Parameter     | Description                                                                                    |
+===============+================================================================================================+
| OID           | Reference the command using a specific object identifier.                                      |
+---------------+------------------------------------------------------------------------------------------------+
| MIB name      | Reference the command using a specific object MIB name                                         |
+---------------+------------------------------------------------------------------------------------------------+
| Full          | Include the full list of MIB objects when displaying an OID                                    |
+---------------+------------------------------------------------------------------------------------------------+
| Numerical     | Controls whether you want to display enumerated lists numerically or with textual translations |
+---------------+------------------------------------------------------------------------------------------------+
| Log file name | Give a meaningful name to the log file                                                         |
|               | Minimum user role:                                                                             |
|               |                                                                                                |
|               | Operator                                                                                       |
+---------------+------------------------------------------------------------------------------------------------+

**Example**
::

	dnRouter# run system snmp get sysDescr.0
	SNMPv2-MIB::sysDescr.0 = STRING: DRIVENETS LTD. Virtual Router, DNOS [5.1.1.97], Copyright 2017 DRIVENETS LTD.
	
	dnRouter# run system snmp get sysDescr.0 sysName.0
	SNMPv2-MIB::sysDescr.0 = STRING: DRIVENETS LTD. Virtual Router, DNOS [5.1.1.97], Copyright 2017 DRIVENETS LTD.
	SNMPv2-MIB::sysName.0 = STRING: dnRouter	
	

.. **Help line:** run snmp get over mib name or oid

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 5.1.0   | Command introduced |
+---------+--------------------+



---

## run system snmp getnext.rst

run system snmp getnext
-----------------------

**Minimum user role:** viewer

To retrieve and display the next SNMP object values:

**Command syntax: run system snmp getnext {[oid] \| [mib-name]}** {full \| numerical} log [log-file-name]

**Command mode:** operation 

**Note**

- This command is executed using a specific community (v2) named dn_community, which has a "view" configuration attached, named view_default. The output will be displayed within the scope of the supported configured view for the community. This view is restricted only from inside the system (local host). No Lawful Interception (LI) MIBs are exported.

.. - Restricted view response:

	- No LI mibs are exported

	- Linux implementation examples:

	- For SNMP v2c configuration:

	- snmpgetnext -v 2c -c dn_community <local-host address> <mib-oid/name>

	- for logging: snmpgetnext -v 2c -c dn_community <local-host address> <mib-oid/name> -Lf <log-file>

**Parameter table**

The parameters are:

+---------------+------------------------------------------------------------------------------------------------+
| Parameter     | Description                                                                                    |
+===============+================================================================================================+
| OID           | Reference the command using a specific object identifier.                                      |
+---------------+------------------------------------------------------------------------------------------------+
| MIB name      | Reference the command using a specific object MIB name                                         |
+---------------+------------------------------------------------------------------------------------------------+
| Full          | Include the full list of MIB objects when displaying an OID                                    |
+---------------+------------------------------------------------------------------------------------------------+
| Numerical     | Controls whether you want to display enumerated lists numerically or with textual translations |
+---------------+------------------------------------------------------------------------------------------------+
| Log file name | Give a meaningful name to the log file                                                         |
|               | Minimum user role:                                                                             |
|               |                                                                                                |
|               | Operator                                                                                       |
+---------------+------------------------------------------------------------------------------------------------+

**Example**
::

	dnRouter# run system snmp getnext sysContact.0
	SNMPv2-MIB::sysName.0 = STRING: dnRouter
	dnRouter# run system snmp getnext 1.3.6.1
	SNMPv2-MIB::sysDescr.0 = STRING: DRIVENETS LTD. Virtual Router, DNOS [5.1.1.97], Copyright 2017 DRIVENETS LTD.
	

.. **Help line:** run snmp getnext over mib name or oid

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 5.1.0   | Command introduced |
+---------+--------------------+



---

## run system snmp walk.rst

run system snmp walk
--------------------

**Minimum user role:** viewer

To retrieve and display the SNMP object values that are associated with the requested object identifier (oid):

**Command syntax: run system snmp walk {[oid] \| [mib-name]}** {full \| numerical} log [log-file-name]

**Command mode:** operation 

**Note**

- This command is executed using a specific community (v2) named dn_community, which has a "view" configuration attached, named view_default. The output will be displayed within the scope of the supported configured view for the community. This view is restricted only from inside the system (local host). No Lawful Interception (LI) MIBs are exported.

.. - Restricted view response:

	- No LI mibs are exported

	- Linux implementation examples:

	- For SNMP v2c configuration:

	- snmpwalk -v 2c -c dn_community <local-host address> <mib-oid/name>

	- for logging: snmpwalk -v 2c -c dn_community <local-host address> <mib-oid/name> -Lf <log-file>

**Parameter table**

The parameters are:

+---------------+------------------------------------------------------------------------------------------------+
| Parameter     | Description                                                                                    |
+===============+================================================================================================+
| OID           | Reference the command using a specific object identifier.                                      |
+---------------+------------------------------------------------------------------------------------------------+
| MIB name      | Reference the command using a specific object MIB name                                         |
+---------------+------------------------------------------------------------------------------------------------+
| Full          | Include the full list of MIB objects when displaying an OID                                    |
+---------------+------------------------------------------------------------------------------------------------+
| Numerical     | Controls whether you want to display enumerated lists numerically or with textual translations |
+---------------+------------------------------------------------------------------------------------------------+
| Log file name | Give a meaningful name to the log file                                                         |
|               | Minimum user role:                                                                             |
|               |                                                                                                |
|               | Operator                                                                                       |
+---------------+------------------------------------------------------------------------------------------------+

**Example**
::

	dnRouter# run system snmp walk  1.3.6.1.2.1.1
	SNMPv2-MIB::sysDescr.0 = STRING: DRIVENETS LTD. Virtual Router, DNOS [5.1.1.97], Copyright 2017 DRIVENETS LTD.
	SNMPv2-MIB::sysObjectID.0 = OID: SNMPv2-SMI::enterprises.49739
	DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysContact.0 = STRING: support@drivenets.com
	SNMPv2-MIB::sysName.0 = STRING: dnRouter
	SNMPv2-MIB::sysLocation.0 = STRING: Undefined
	SNMPv2-MIB::sysORLastChange.0 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORID.1 = OID: SNMP-MPD-MIB::snmpMPDCompliance
	SNMPv2-MIB::sysORID.2 = OID: SNMP-USER-BASED-SM-MIB::usmMIBCompliance
	SNMPv2-MIB::sysORID.3 = OID: SNMP-FRAMEWORK-MIB::snmpFrameworkMIBCompliance
	SNMPv2-MIB::sysORID.4 = OID: SNMP-VIEW-BASED-ACM-MIB::vacmBasicGroup
	SNMPv2-MIB::sysORID.5 = OID: TCP-MIB::tcpMIB
	SNMPv2-MIB::sysORID.6 = OID: UDP-MIB::udpMIB
	SNMPv2-MIB::sysORID.7 = OID: SNMP-NOTIFICATION-MIB::snmpNotifyFullCompliance
	SNMPv2-MIB::sysORID.8 = OID: NOTIFICATION-LOG-MIB::notificationLogMIB
	SNMPv2-MIB::sysORDescr.1 = STRING: The MIB for Message Processing and Dispatching.
	SNMPv2-MIB::sysORDescr.2 = STRING: The management information definitions for the SNMP User-based Security Model.
	SNMPv2-MIB::sysORDescr.3 = STRING: The SNMP Management Architecture MIB.
	SNMPv2-MIB::sysORDescr.4 = STRING: View-based Access Control Model for SNMP.
	SNMPv2-MIB::sysORDescr.5 = STRING: The MIB module for managing TCP implementations
	SNMPv2-MIB::sysORDescr.6 = STRING: The MIB module for managing UDP implementations
	SNMPv2-MIB::sysORDescr.7 = STRING: The MIB modules for managing SNMP Notification, plus filtering.
	SNMPv2-MIB::sysORDescr.8 = STRING: The MIB module for logging SNMP Notifications.
	SNMPv2-MIB::sysORUpTime.1 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.2 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.3 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.4 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.5 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.6 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.7 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.8 = Timeticks: (0) 0:00:00.00
	
	dnRouter# run system snmp walk SNMPv2-MIB
	SNMPv2-MIB::sysDescr.0 = STRING: DRIVENETS LTD. Virtual Router, DNOS [5.1.1.97], Copyright 2017 DRIVENETS LTD.
	SNMPv2-MIB::sysObjectID.0 = OID: SNMPv2-SMI::enterprises.49739
	DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysContact.0 = STRING: support@drivenets.com
	SNMPv2-MIB::sysName.0 = STRING: dnRouter
	SNMPv2-MIB::sysLocation.0 = STRING: Undefined
	SNMPv2-MIB::sysORLastChange.0 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORID.1 = OID: SNMP-MPD-MIB::snmpMPDCompliance
	SNMPv2-MIB::sysORID.2 = OID: SNMP-USER-BASED-SM-MIB::usmMIBCompliance
	SNMPv2-MIB::sysORID.3 = OID: SNMP-FRAMEWORK-MIB::snmpFrameworkMIBCompliance
	SNMPv2-MIB::sysORID.4 = OID: SNMP-VIEW-BASED-ACM-MIB::vacmBasicGroup
	SNMPv2-MIB::sysORID.5 = OID: TCP-MIB::tcpMIB
	SNMPv2-MIB::sysORID.6 = OID: UDP-MIB::udpMIB
	SNMPv2-MIB::sysORID.7 = OID: SNMP-NOTIFICATION-MIB::snmpNotifyFullCompliance
	SNMPv2-MIB::sysORID.8 = OID: NOTIFICATION-LOG-MIB::notificationLogMIB
	SNMPv2-MIB::sysORDescr.1 = STRING: The MIB for Message Processing and Dispatching.
	SNMPv2-MIB::sysORDescr.2 = STRING: The management information definitions for the SNMP User-based Security Model.
	SNMPv2-MIB::sysORDescr.3 = STRING: The SNMP Management Architecture MIB.
	SNMPv2-MIB::sysORDescr.4 = STRING: View-based Access Control Model for SNMP.
	SNMPv2-MIB::sysORDescr.5 = STRING: The MIB module for managing TCP implementations
	SNMPv2-MIB::sysORDescr.6 = STRING: The MIB module for managing UDP implementations
	SNMPv2-MIB::sysORDescr.7 = STRING: The MIB modules for managing SNMP Notification, plus filtering.
	SNMPv2-MIB::sysORDescr.8 = STRING: The MIB module for logging SNMP Notifications.
	SNMPv2-MIB::sysORUpTime.1 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.2 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.3 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.4 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.5 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.6 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.7 = Timeticks: (0) 0:00:00.00
	SNMPv2-MIB::sysORUpTime.8 = Timeticks: (0) 0:00:00.00
	

.. **Help line:** run snmp walk over mib name or oid

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 5.1.0   | Command introduced |
+---------+--------------------+



---

## run telnet.rst

run telnet
-----------

**Minimum user role:** viewer

The run telnet command checks the accessibility of a destination interface.

**Command syntax: run telnet [dest-ip]|[host-name]** {egress-interface [egress-interface] \| source-address [source-address]}

**Command mode:** operation 

**Note**

- The command is supported only for default VRF interfaces and for mgmt0 out-of-band interface.

- The parameters can all be specified in the same command.

.. - telnet command is one-line format. meaning - all parameters can be entered on the same line

	- run telnet [dest-ip] egress-interface - defines source IP of the packet to IP address of the egress interface. If "egress-interface"=mgmt0, linux command "telnet [ip-address]" should be run in a context of default NS, i.e. Telnet will run in out-of-band.

	- run telnet [dest-ip] source-address [source-address] - set source ip-address for Telnet packets.

	- If neither egress-interface nor source-address parameter was set, Telnet packets are generated via in-band management channel with source IP address according to default VRF routing table

	- ability to specify host-name instead of dest-ip address is supported 

	- in case telnet client disable - shall print error msg: please activate telnet client ...

**Parameter table**

The following are the parameters that you can use for the telnet command:

+------------------+--------------------------------------------------------+------------------------------------------------+
| Parameter        | Description                                            | Range                                          |
+==================+========================================================+================================================+
| dest-ip          | The IP address of the target host.                     | A.B.C.D                                        |
|                  |                                                        | x:x::x:x                                       |
+------------------+--------------------------------------------------------+------------------------------------------------+
| host-name        | The full or partial name of the target host to telnet. | String                                         |
+------------------+--------------------------------------------------------+------------------------------------------------+
| egress-interface | The name of the interface                              | All default VRF interfaces and mgmt0 interface |
+------------------+--------------------------------------------------------+------------------------------------------------+
| source-address   | IP address of the source                               | A.B.C.D                                        |
|                  |                                                        | x:x::x:x                                       |
+------------------+--------------------------------------------------------+------------------------------------------------+

**Example**
::

	dnRouter# run telnet 1.1.1.1
	dnRouter# run telnet 1.1.1.1 egress-interface lo0
	dnRouter# run telnet 1.1.1.1 source-address 5.5.5.5
	dnRouter# run telnet dnCoreRouter-2
	

.. **Help line:** run telnet

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 13.1    | Command introduced |
+---------+--------------------+



---

## run traceroute mpls bgp-lu.rst

run traceroute mpls bgp-lu
--------------------------

**Minimum user role:** operator

You can manually run traceroute to a remote host for a BGP-LU LSP.

MPLS traceroute - used for hop-by-hop fault localization and/or path tracing: A packet is sent to the control plane of each transit LSR. The transit LSR performs various checks to confirm that it is indeed a transit LSR for this path; this LSR also returns additional information that helps check the control plane against the data plane.

The interval between probes is min{reply-time, timeout}. That is, either the echo reply receive time or the timeout (2 seconds) in case of no reply.

To start a traceroute for a BGP-LU LSP:

**Command syntax: run traceroute mpls bgp-lu [target-address]** multipath destination-address [destination-address] next-hop [next-hop-address] source-interface [source-interface] size [size] exp [exp] max-hops [max-hops] force-explicit-null ddmap detail

**Command mode:** operation

**Note**

..  - If user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), packet size will be the minimum size required and no padding shall be used.

    - If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

    - The target-address address family dictates the applicable source-interfaces (having IP address of the same AFI) and the valid destination-address range.

    - If packet is sent with MTU packet size bigger than path MTU, then MTU TX error counter will rise as no fragmentation is allowed.

    - Echo requests are sent by default with the DSMAP TLV, but DDMAP can be forced instead.

    - In the event that the user uses an unknown IP prefix, then the following message will be displayed: "no route exists" and traceroute action will stop.

    - If the multipath knob is used and there are multiple possible nexthops (ECMP), each possibe ECMP path and subsequent reported paths matching filters used will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies.

    - If the multipath knob is not used, echo request will be sent with the valid determined information, contingent on information provided by the operator, necessary to probe a single path, and no multipath information will be printed in CLI.

    - If next-hop is invalid or specified with address-family different than destination address-family ip address, then output code Q will be printed and error message will be displayed on the screen notifying: “no route to host via specified next-hop”.

    - User can stop traceroute requests using ctrl+c.

    - Total Time Elapsed in multipath traceroute represents the total time the traceroute operation took from start to finish.

    - In multipath traceroute each reported path is determined to be 'Found', 'Unexplorable' or 'Broken'. Found paths are valid paths for verified LSPs all the way to the egress LER; Unexplorable paths are discovered paths that could not be verified end-to-end for various reasons, inter alia, because the 127/8 destination IP address range used for the LSP selection has been exhausted, or due to disruptions along the LSP such as consecutive timeouts that break the trace (as opposed to certain non-compliant LSRs that are skipped) or TTL expiration; Broken paths indicate that the LSP is broken, meaning that traffic will not be sent across this path and may be discarded.

    - For multipath traceroute hops that timeout will be indicated in the summary of each path, but not in the detailed per-hop output.

    - FEC stack sent shows FEC stack from top to bottom of stack, left to right.

**Parameter table**

+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                                        | Range                                                                                                                                     | Default                                               |
+=====================+====================================================================================================================================================================================================================================================================================================================================================================================+===========================================================================================================================================+=======================================================+
| multipath           | Validates all reported paths.                                                                                                                                                                                                                                                                                                                                                      | \-                                                                                                                                        | \-                                                    |
|                     | If the multipath knob is used and there are multiple possible nexthops (ECMP), each possible ECMP path, and subsequent reported paths, that match used filters will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies. |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| target-address      | An IPv4 or IPv6 destination address FEC for BGP-LU FEC types. If the target-address is not a valid address known by BGP-LU, an error message is displayed.                                                                                                                                                                                                                         | A.B.C.D/M                                                                                                                                 | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                                                    | X:X::X/M                                                                                                                                  |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                                         | 1..255 characters (an existing interface name)                                                                                            | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an applicable AFI IP address, an error message is displayed.                                                                                                                                                                                                                                                            |                                                                                                                                           |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                                          |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop-address    | Specifies the next hop as an IP address. Can be used for ECMP cases or if two entries exist in the RIB for the same IP FEC.                                                                                                                                                                                                                                                        | A.B.C.D                                                                                                                                   | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                                                    | X:X::X                                                                                                                                    |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                                        | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) or an IPv6 address from the range 0:0:0:0:0:FFFF:7F00:0/104 | 127.0.0.1 or 0:0:0:0:0:FFFF:7F00:1                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed.                        | 100..9300                                                                                                                                 | packet size is determent according to the used TLVs   |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IP header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                                                      | 0..7                                                                                                                                      | 0                                                     |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| max-hops            | The maximum number of hops before the traceroute action is terminated (the maximum TTL value for the traceroute probe)                                                                                                                                                                                                                                                             | 1..255                                                                                                                                    | 30                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                                       | \-                                                                                                                                        | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| ddmap               | Forces the Downstream Detailed Mapping TLV instead of the deprecated DSMAP TLV.                                                                                                                                                                                                                                                                                                    | \-                                                                                                                                        | -                                                     |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| detail              | Prints a detailed output for every reply received.                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::


  dnRouter# run traceroute mpls bgp-lu 1.2.3.4/32
  Tracing MPLS LSP, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort

   output interface ge100-0/0/5 nexthop 10.1.17.7
   source 1.1.1.1 destination 127.0.0.1
    0 1.1.1.1 10.1.17.7 MPLS-MTU 1500 [Labels: 24002 Exp: 0]
  L 1 10.1.17.7 10.1.75.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] round-trip-delay 3 msec
  ! 2 10.1.75.5 round-trip-delay 4 msec


  dnRouter# run traceroute mpls bgp-lu 2.2.2.2/32 multipath
  Tracing MPLS LSP, target ipv4-address: 2.2.2.2/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort

  LL....
  Path 1 Unexplorable,
   output interface ge100-0/0/0 nexthop 10.1.1.13
   source 10.1.1.2 destination 127.0.0.64
    0 10.1.1.2 10.1.1.13 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  L 1 10.1.1.13 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec
  L 2 10.1.1.10 10.1.91.10 MPLS-MTU 1500 [Labels: 802809 Exp: 0] multipaths 3 round-trip-delay 4 msec

  LL!
  Path 2 Found,
   output interface ge100-0/0/2 nexthop 10.1.1.1
   source 10.1.1.17 destination 127.0.1.64
    0 10.1.1.2 10.1.1.1 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  L 1 10.1.1.1 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec
  L 2 10.1.1.10 0.1.91.6 MPLS-MTU 1500 [Labels: 802809 Exp: 0] multipaths 3 round-trip-delay 4 msec
  ! 3 10.1.64.5 multipaths 0 round-trip-delay 5 msec

  B
  Path 3 Broken,
   output interface ge100-0/0/2 nexthop 10.1.1.1
   source 10.1.1.17 destination 127.0.1.66
    0 10.1.1.17 10.1.1.22 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  B 1 10.1.1.22 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec

  Paths (found/broken/unexplored) (1/1/1)
   Echo Request (sent/fail) (10/0)
   Echo Reply (received/timeout) (6/4)
   Total Time Elapsed 34 ms


  dnRouter# run traceroute mpls bgp-lu 1.2.3.4/32 multipath detail
  Tracing MPLS LSP, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort

  L!
  Path 1 Found,
   output interface ge100-0/0/5 nexthop 10.1.17.7
   source 1.1.1.1 destination 127.0.0.64
    0 1.1.1.1 10.1.17.7 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.17.7 10.1.75.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 1 round-trip-delay 3 msec
      Target FEC stack sent: [0] BGP-LU 1.2.3.4
      FEC-change received: push-RSVP (2.2.2.2)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.75.5 round-trip-delay 4 msec

  L!
  Path 2 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.64
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.85.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 2 round-trip-delay 8 msec
      Target FEC stack sent: [0] BGP-LU 1.2.3.4
      FEC-change received: push-RSVP (2.2.2.2)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.85.5 round-trip-delay 20 msec

  !
  Path 3 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.66
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.58.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 2 round-trip-delay 20 msec
      Target FEC stack sent: [0] BGP-LU 1.2.3.4
      FEC-change received: push-RSVP (2.2.2.2)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.58.5 round-trip-delay 43 msec

  Paths (found/broken/unexplored) (3/0/0)
   Echo Request (sent/fail) (5/0)
   Echo Reply (received/timeout) (5/0)
   Total Time Elapsed 67 ms


**Command History**

+---------+-----------------------------------------------------------+
| Release | Modification                                              |
+=========+===========================================================+
| 11.0    | Command introduced                                        |
+---------+-----------------------------------------------------------+
| 15.0    | Updated command syntax to support 'multipath' and 'ddmap' |
+---------+-----------------------------------------------------------+
| 15.1    | Updated command syntax to support detailed output         |
+---------+-----------------------------------------------------------+
| 18.2    | Added support for IPv6                                    |
+---------+-----------------------------------------------------------+

---

## run traceroute mpls generic.rst

run traceroute mpls generic
---------------------------

**Minimum user role:** operator

You can manually run traceroute to a remote host for an LSP, regardless of protocol.

MPLS traceroute - used for hop-by-hop fault localization and/or path tracing: A packet is sent to the control plane of each transit LSR. The transit LSR performs various checks to confirm that it is indeed a transit LSR for this path; this LSR also returns additional information that helps check the control plane against the data plane.

The interval between probes is min{reply-time, timeout}. That is, either the echo reply receive time or the timeout (2 seconds) in case of no reply.

To start a traceroute for an LSP:

**Command syntax: run traceroute mpls generic [target-address]** multipath destination-address [destination-address] next-hop [next-hop-address] source-interface [source-interface] size [size] exp [exp] max-hops [max-hops] force-explicit-null ddmap detail

**Command mode:** operation

**Note**

..  - If user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), packet size will be the minimum size required and no padding shall be used.

    - If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

    - The target-address address family dictates the applicable source-interfaces (having IP address of the same AFI) and the valid destination-address range.

    - If packet is sent with MTU packet size bigger than path MTU, then MTU TX error counter will rise as no fragmentation is allowed.

    - Echo requests are sent by default with the DSMAP TLV, but DDMAP can be forced instead.

    - In the event that the user uses an unknown IP prefix, then the following message will be displayed: "no route exists" and traceroute action will stop.

    - If the multipath knob is used and there are multiple possible nexthops (ECMP), each possibe ECMP path and subsequent reported paths matching filters used will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies.

    - If the multipath knob is not used, echo request will be sent with the valid determined information, contingent on information provided by the operator, necessary to probe a single path, and no multipath information will be printed in CLI.

    - If next-hop is invalid or specified with address-family different than destination address-family ip address, then output code Q will be printed and error message will be displayed on the screen notifying: “no route to host via specified next-hop”.

    - User can stop traceroute requests using ctrl+c.

    - Total Time Elapsed in multipath traceroute represents the total time the traceroute operation took from start to finish.

    - In multipath traceroute each reported path is determined to be 'Found', 'Unexplorable' or 'Broken'. Found paths are valid paths for verified LSPs all the way to the egress LER; Unexplorable paths are discovered paths that could not be verified end-to-end for various reasons, inter alia, because the 127/8 destination IP address range used for the LSP selection has been exhausted, or due to disruptions along the LSP such as consecutive timeouts that break the trace (as opposed to certain non-compliant LSRs that are skipped) or TTL expiration; Broken paths indicate that the LSP is broken, meaning that traffic will not be sent across this path and may be discarded.

    - For multipath traceroute hops that timeout will be indicated in the summary of each path, but not in the detailed per-hop output.

    - FEC stack sent shows FEC stack from top to bottom of stack, left to right.

**Parameter table**

+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                                        | Range                                                                                                                                     | Default                                               |
+=====================+====================================================================================================================================================================================================================================================================================================================================================================================+===========================================================================================================================================+=======================================================+
| multipath           | Validates all reported paths.                                                                                                                                                                                                                                                                                                                                                      | \-                                                                                                                                        | \-                                                    |
|                     | If the multipath knob is used and there are multiple possible nexthops (ECMP), each possible ECMP path, and subsequent reported paths, that match used filters will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies. |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| target-address      | An IPv4 or IPv6 destination address FEC for generic FEC type (regardless of advertising routing protocol). If the target-address is not a valid address, an error message is displayed.                                                                                                                                                                                            | A.B.C.D/M                                                                                                                                 | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                                                    | X:X::X/M                                                                                                                                  |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                                         | 1..255 characters (an existing interface name)                                                                                            | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an applicable AFI IP address, an error message is displayed.                                                                                                                                                                                                                                                           |                                                                                                                                            |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                                          |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop-address    | Specifies the next hop as an IP address. Can be used for ECMP cases or if two entries exist in the RIB for the same IP FEC.                                                                                                                                                                                                                                                        | A.B.C.D                                                                                                                                   | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                                                    | X:X::X                                                                                                                                    |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                                        | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) or an IPv6 address from the range 0:0:0:0:0:FFFF:7F00:0/104 | 127.0.0.1 or 0:0:0:0:0:FFFF:7F00:1                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed.                        | 100..9300                                                                                                                                 | packet size is determent according to the used TLVs   |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IP header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                                                      | 0..7                                                                                                                                      | 0                                                     |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| max-hops            | The maximum number of hops before the traceroute action is terminated (the maximum TTL value for the traceroute probe)                                                                                                                                                                                                                                                             | 1..255                                                                                                                                    | 30                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                                       | \-                                                                                                                                        | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| ddmap               | Forces the Downstream Detailed Mapping TLV instead of the deprecated DSMAP TLV.                                                                                                                                                                                                                                                                                                    | \-                                                                                                                                        | -                                                     |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| detail              | Prints a detailed output for every reply received.                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::


  dnRouter# run traceroute mpls generic 1.2.3.4/32
  Tracing MPLS LSP, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort

   output interface ge100-0/0/5 nexthop 10.1.17.7
   source 1.1.1.1 destination 127.0.0.1
    0 1.1.1.1 10.1.17.7 MPLS-MTU 1500 [Labels: 24002 Exp: 0]
  L 1 10.1.17.7 10.1.75.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] round-trip-delay 3 msec
  ! 2 10.1.75.5 round-trip-delay 4 msec


  dnRouter# run traceroute mpls generic 2.2.2.2/32 multipath
  Tracing MPLS LSP, target ipv4-address: 2.2.2.2/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort

  LL....
  Path 1 Unexplorable,
   output interface ge100-0/0/0 nexthop 10.1.1.13
   source 10.1.1.2 destination 127.0.0.64
    0 10.1.1.2 10.1.1.13 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  L 1 10.1.1.13 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec
  L 2 10.1.1.10 10.1.91.10 MPLS-MTU 1500 [Labels: 802809 Exp: 0] multipaths 3 round-trip-delay 4 msec

  LL!
  Path 2 Found,
   output interface ge100-0/0/2 nexthop 10.1.1.1
   source 10.1.1.17 destination 127.0.1.64
    0 10.1.1.2 10.1.1.1 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  L 1 10.1.1.1 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec
  L 2 10.1.1.10 0.1.91.6 MPLS-MTU 1500 [Labels: 802809 Exp: 0] multipaths 3 round-trip-delay 4 msec
  ! 3 10.1.64.5 multipaths 0 round-trip-delay 5 msec

  B
  Path 3 Broken,
   output interface ge100-0/0/2 nexthop 10.1.1.1
   source 10.1.1.17 destination 127.0.1.66
    0 10.1.1.17 10.1.1.22 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  B 1 10.1.1.22 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec

  Paths (found/broken/unexplored) (1/1/1)
   Echo Request (sent/fail) (10/0)
   Echo Reply (received/timeout) (6/4)
   Total Time Elapsed 34 ms


  dnRouter# run traceroute mpls generic 1.2.3.4/32 multipath detail
  Tracing MPLS LSP, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort

  L!
  Path 1 Found,
   output interface ge100-0/0/5 nexthop 10.1.17.7
   source 1.1.1.1 destination 127.0.0.64
    0 1.1.1.1 10.1.17.7 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.17.7 10.1.75.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 1 round-trip-delay 3 msec
      Target FEC stack sent: [0] Generic 1.2.3.4
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.75.5 round-trip-delay 4 msec

  L!
  Path 2 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.64
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.85.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 2 round-trip-delay 8 msec
      Target FEC stack sent: [0] Generic 1.2.3.4
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.85.5 round-trip-delay 20 msec

  !
  Path 3 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.66
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.58.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 2 round-trip-delay 20 msec
      Target FEC stack sent: [0] Generic 1.2.3.4
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.58.5 round-trip-delay 43 msec

  Paths (found/broken/unexplored) (3/0/0)
   Echo Request (sent/fail) (5/0)
   Echo Reply (received/timeout) (5/0)
   Total Time Elapsed 67 ms


**Command History**

+---------+-----------------------------------------------------------+
| Release | Modification                                              |
+=========+===========================================================+
| 15.1    | Command introduced                                        |
+---------+-----------------------------------------------------------+
| 18.2    | Added support for IPv6                                    |
+---------+-----------------------------------------------------------+

---

## run traceroute mpls isis.rst

run traceroute mpls isis
-----------------------------------

**Minimum user role:** operator

You can manually run traceroute to a remote host for an IS-IS LSP.

MPLS traceroute - used for hop-by-hop fault localization and/or path tracing: A packet is sent to the control plane of each transit LSR. The transit LSR performs various checks to confirm that it is indeed a transit LSR for this path; this LSR also returns additional information that helps check the control plane against the data plane.

The interval between probes is min{reply-time, timeout}. That is, either the echo reply receive time or the timeout (2 seconds) in case of no reply.

To start a traceroute for a IS-IS LSP:

**Command syntax: run traceroute mpls isis [target-address]** multipath destination-address [destination-address] next-hop [next-hop-address] source-interface [source-interface] size [size] exp [exp] max-hops [max-hops] force-explicit-null detail

**Command mode:** operation

.. **Note**

  - If packet is sent with MTU packet size bigger than path MTU, then MTU TX error counter will rise as no fragmentation is allowed.

  - If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

  - The target-address address family dictates the applicable source-interfaces (having IP address of the same AFI) and the valid destination-address range.

  - Echo requests are sent with the DDMAP TLV.

  - In the event that the user uses an unknown IP prefix, then the following message will be displayed: "no route exists" and traceroute action will stop.

  - If the multipath knob is used and there are multiple possible nexthops (ECMP), each possibe ECMP path and subsequent reported paths matching filters used will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies.

  - If the multipath knob is not used, echo request will be sent with the valid determined information, contingent on information provided by the operator, necessary to probe a single path, and no multipath information will be printed in CLI.

  - If next-hop is invalid or specified with address-family different than destination address-family ip address, then output code Q will be printed and error message will be displayed on the screen notifying: “no route to host via specified next-hop”.

  - User can stop traceroute requests using ctrl+c.

  - Total Time Elapsed in multipath traceroute represents the total time the traceroute operation took from start to finish.

  - In multipath traceroute each reported path is determined to be 'Found', 'Unexplorable' or 'Broken'. Found paths are valid paths for verified LSPs all the way to the egress LER; Unexplorable paths are discovered paths that could not be verified end-to-end for various reasons, inter alia, because the 127/8 destination IP address range used for the LSP selection has been exhausted, or due to disruptions along the LSP such as consecutive timeouts that break the trace (as opposed to certain non-compliant LSRs that are skipped) or TTL expiration; Broken paths indicate that the LSP is broken, meaning that traffic will not be sent across this path and may be discarded.

  - For multipath traceroute hops that timeout will be indicated in the summary of each path, but not in the detailed per-hop output.

  - If user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), packet size will be the minimum size required and no padding shall be used.

  - FEC stack sent shows FEC stack from top to bottom of stack, left to right.


**Parameter table**

+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                                        | Range                                                                                                                                     | Default                                               |
+=====================+====================================================================================================================================================================================================================================================================================================================================================================================+===========================================================================================================================================+=======================================================+
| multipath           | Validates all reported paths.                                                                                                                                                                                                                                                                                                                                                      | \-                                                                                                                                        | \-                                                    |
|                     | If the multipath knob is used and there are multiple possible nexthops (ECMP), each possible ECMP path, and subsequent reported paths, that match used filters will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies. |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| target-address      | An IPv4 or IPv6 destination address FEC for SR IS-IS FEC types. If the target-address is not a valid address known by IS-IS, an error message is displayed.                                                                                                                                                                                                                        | A.B.C.D/M                                                                                                                                 | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                                                    | X:X::X/M                                                                                                                                  |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                                         | 1..255 characters (an existing interface name)                                                                                            | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an applicable AFI IP address, an error message is displayed.                                                                                                                                                                                                                                                            |                                                                                                                                           |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                                          |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop-address    | Specifies the next hop as an IP address. Can be used for ECMP cases or if two entries exist in the RIB for the same IP FEC.                                                                                                                                                                                                                                                        | A.B.C.D                                                                                                                                   | \-                                                    |
|                     |                                                                                                                                                                                                                                                                                                                                                                                    | X:X::X                                                                                                                                    |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                                        | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) or an IPv6 address from the range 0:0:0:0:0:FFFF:7F00:0/104 | 127.0.0.1 or 0:0:0:0:0:FFFF:7F00:1                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed.                        | 100..9300                                                                                                                                 | packet size is determent according to the used TLVs   |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IP header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                                                      | 0..7                                                                                                                                      | 0                                                     |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| max-hops            | The maximum number of hops before the traceroute action is terminated (the maximum TTL value for the traceroute probe)                                                                                                                                                                                                                                                             | 1..255                                                                                                                                    | 30                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                                       | \-                                                                                                                                        | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| ddmap               | Forces the Downstream Detailed Mapping TLV instead of the deprecated DSMAP TLV.                                                                                                                                                                                                                                                                                                    | \-                                                                                                                                        | -                                                     |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| detail              | Prints a detailed output for every reply received.                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::

  dnRouter# run traceroute mpls isis 1.2.3.4/32
  Tracing MPLS LSP, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort

   output interface ge100-0/0/5 nexthop 10.1.17.7
   source 1.1.1.1 destination 127.0.0.1
    0 1.1.1.1 10.1.17.7 MPLS-MTU 1500 [Labels: 24002 Exp: 0]
  L 1 10.1.17.7 10.1.75.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] round-trip-delay 3 msec
  ! 2 10.1.75.5 round-trip-delay 4 msec


  dnRouter# run traceroute mpls isis 2.2.2.2/32 multipath
  Tracing MPLS LSP, target ipv4-address: 2.2.2.2/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort

  LL....
  Path 1 Unexplorable,
   output interface ge100-0/0/0 nexthop 10.1.1.13
   source 10.1.1.2 destination 127.0.0.64
    0 10.1.1.2 10.1.1.13 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  L 1 10.1.1.13 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec
  L 2 10.1.1.10 10.1.91.10 MPLS-MTU 1500 [Labels: 802809 Exp: 0] multipaths 3 round-trip-delay 4 msec

  LL!
  Path 2 Found,
   output interface ge100-0/0/2 nexthop 10.1.1.1
   source 10.1.1.17 destination 127.0.1.64
    0 10.1.1.2 10.1.1.1 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  L 1 10.1.1.1 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec
  L 2 10.1.1.10 0.1.91.6 MPLS-MTU 1500 [Labels: 802809 Exp: 0] multipaths 3 round-trip-delay 4 msec
  ! 3 10.1.64.5 multipaths 0 round-trip-delay 5 msec

  B
  Path 3 Broken,
   output interface ge100-0/0/2 nexthop 10.1.1.1
   source 10.1.1.17 destination 127.0.1.66
    0 10.1.1.17 10.1.1.22 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  B 1 10.1.1.22 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec

  Paths (found/broken/unexplored) (1/1/1)
   Echo Request (sent/fail) (10/0)
   Echo Reply (received/timeout) (6/4)
   Total Time Elapsed 34 ms


  dnRouter# run traceroute mpls isis 1.2.3.4/32 multipath detail
  Tracing MPLS LSP, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort

  L!
  Path 1 Found,
   output interface ge100-0/0/5 nexthop 10.1.17.7
   source 1.1.1.1 destination 127.0.0.64
    0 1.1.1.1 10.1.17.7 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.17.7 10.1.75.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 1 round-trip-delay 3 msec
      Target FEC stack sent: [0] ISIS 1.2.3.4
      FEC-change received: pop-ISIS (1.2.3.4), push-LDP (1.2.3.4)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.75.5 round-trip-delay 4 msec

  L!
  Path 2 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.64
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.85.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 2 round-trip-delay 8 msec
      Target FEC stack sent: [0] ISIS 1.2.3.4
      FEC-change received: pop-ISIS (1.2.3.4), push-LDP (1.2.3.4)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.85.5 round-trip-delay 20 msec

  !
  Path 3 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.66
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.58.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 2 round-trip-delay 20 msec
      Target FEC stack sent: [0] ISIS 1.2.3.4
      FEC-change received: pop-ISIS (1.2.3.4), push-LDP (1.2.3.4)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.58.5 round-trip-delay 43 msec

  Paths (found/broken/unexplored) (3/0/0)
   Echo Request (sent/fail) (5/0)
   Echo Reply (received/timeout) (5/0)
   Total Time Elapsed 67 ms


**Command History**

+---------+-----------------------------------------------------------+
| Release | Modification                                              |
+=========+===========================================================+
| 15.0    | Command introduced                                        |
+---------+-----------------------------------------------------------+
| 15.1    | Updated command syntax to support detailed output         |
+---------+-----------------------------------------------------------+
| 18.2    | Added support for IPv6                                    |
+---------+-----------------------------------------------------------+

---

## run traceroute mpls ldp.rst

run traceroute mpls ldp
-----------------------

**Minimum user role:** operator

You can manually run traceroute to a remote host for an LDP LSP.

MPLS traceroute - used for hop-by-hop fault localization and/or path tracing: A packet is sent to the control plane of each transit LSR. The transit LSR performs various checks to confirm that it is indeed a transit LSR for this path; this LSR also returns additional information that helps check the control plane against the data plane.

The interval between probes is min{reply-time, timeout}. That is, either the echo reply receive time or the timeout (2 seconds) in case of no reply.

To start a traceroute for a LDP LSP:

**Command syntax: run traceroute mpls ldp [target-address]** multipath destination-address [destination-address] next-hop [next-hop-address] source-interface [source-interface] max-hops [max-hops] size [size] exp [exp] force-explicit-null ddmap detail

**Command mode:** operation 

.. **Note**

  - If user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), packet size will be the minimum size required and no padding shall be used.

  - If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

  - If packet is sent with MTU packet size bigger than path MTU, then MTU TX error counter will rise as no fragmentation is allowed.

  - Echo requests are sent by default with the DSMAP TLV, but DDMAP can be forced instead.

  - In the event that the user uses an unknown IPv4 prefix, then the following message will be displayed: "no route exists" and traceroute action will stop.

  - If the multipath knob is used and there are multiple possible nexthops (ECMP), each possibe ECMP path and subsequent reported paths matching filters used will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies.

  - If the multipath knob is not used, echo request will be sent with the valid determined information, contingent on information provided by the operator, necessary to probe a single path, and no multipath information will be printed in CLI.

  - If next-hop is invalid or specified with address-family different than destination address-family ip address, then output code Q will be printed and error message will be displayed on the screen notifying: “no route to host via specified next-hop”.

  - User can stop traceroute requests using ctrl+c.

  - Total Time Elapsed in multipath traceroute represents the total time the traceroute operation took from start to finish.

  - In multipath traceroute each reported path is determined to be 'Found', 'Unexplorable' or 'Broken'. Found paths are valid paths for verified LSPs all the way to the egress LER; Unexplorable paths are discovered paths that could not be verified end-to-end for various reasons, inter alia, because the 127/8 destination IP address range used for the LSP selection has been exhausted, or due to disruptions along the LSP such as consecutive timeouts that break the trace (as opposed to certain non-compliant LSRs that are skipped) or TTL expiration; Broken paths indicate that the LSP is broken, meaning that traffic will not be sent across this path and may be discarded.

  - For multipath traceroute hops that timeout will be indicated in the summary of each path, but not in the detailed per-hop output.

  - FEC stack sent shows FEC stack from top to bottom of stack, left to right.

**Parameter table**

+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                                        | Range                                                                         | Default                                               |
+=====================+====================================================================================================================================================================================================================================================================================================================================================================================+===============================================================================+=======================================================+
| multipath           | Validates all reported paths.                                                                                                                                                                                                                                                                                                                                                      | \-                                                                            | \-                                                    |
|                     | If the multipath knob is used and there are multiple possible nexthops (ECMP), each possible ECMP path, and subsequent reported paths, that match used filters will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies. |                                                                               |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| target-address      | An IPv4 destination address FEC for LDP FEC types. If the target-address is not a valid address known by LDP, an error message is displayed.                                                                                                                                                                                                                                       | A.B.C.D/M                                                                     | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                                         | 1..255 characters (an existing interface name)                                | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an IPv4 address, an error message is displayed.                                                                                                                                                                                                                                                                         |                                                                               |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                                          |                                                                               |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop-address    | Specifies the next hop as an IP address. Can be used for ECMP cases or if two entries exist in the RIB for the same IPv4 FEC.                                                                                                                                                                                                                                                      | A.B.C.D                                                                       | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                                        | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) | 127.0.0.1                                             |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed.                        | 100..9300                                                                     | packet size is determent according to the used TLVs   |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IPv4 header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                                                    | 0..7                                                                          | 0                                                     |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| max-hops            | The maximum number of hops before the traceroute action is terminated (the maximum TTL value for the traceroute probe)                                                                                                                                                                                                                                                             | 1..255                                                                        | 30                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                                       | \-                                                                            | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| ddmap               | Forces the Downstream Detailed Mapping TLV instead of the deprecated DSMAP TLV.                                                                                                                                                                                                                                                                                                    | \-                                                                            | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| detail              | Prints a detailed output for every reply received.                                                                                                                                                                                                                                                                                                                                 |                                                                               |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::

  dnRouter# run traceroute mpls ldp 1.2.3.4/32
  Tracing MPLS LSP, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort
  
   output interface ge100-0/0/5 nexthop 10.1.17.7
   source 1.1.1.1 destination 127.0.0.1
    0 1.1.1.1 10.1.17.7 MPLS-MTU 1500 [Labels: 24002 Exp: 0]
  L 1 10.1.17.7 10.1.75.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] round-trip-delay 3 msec
  ! 2 10.1.75.5 round-trip-delay 4 msec
  

  dnRouter# run traceroute mpls ldp 2.2.2.2/32 multipath
  Tracing MPLS LSP, target ipv4-address: 2.2.2.2/32
  Timeout is 2 seconds: 
  
  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code
  
  Type ctrl+c to abort

  LL....
  Path 1 Unexplorable,
   output interface ge100-0/0/0 nexthop 10.1.1.13
   source 10.1.1.2 destination 127.0.0.64
    0 10.1.1.2 10.1.1.13 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  L 1 10.1.1.13 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec
  L 2 10.1.1.10 10.1.91.10 MPLS-MTU 1500 [Labels: 802809 Exp: 0] multipaths 3 round-trip-delay 4 msec
  
  LL!
  Path 2 Found,
   output interface ge100-0/0/2 nexthop 10.1.1.1
   source 10.1.1.17 destination 127.0.1.64
    0 10.1.1.2 10.1.1.1 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  L 1 10.1.1.1 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec
  L 2 10.1.1.10 0.1.91.6 MPLS-MTU 1500 [Labels: 802809 Exp: 0] multipaths 3 round-trip-delay 4 msec
  ! 3 10.1.64.5 multipaths 0 round-trip-delay 5 msec
  
  B
  Path 3 Broken,
   output interface ge100-0/0/2 nexthop 10.1.1.1
   source 10.1.1.17 destination 127.0.1.66
    0 10.1.1.17 10.1.1.22 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  B 1 10.1.1.22 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec
  
  Paths (found/broken/unexplored) (1/1/1)
   Echo Request (sent/fail) (10/0)
   Echo Reply (received/timeout) (6/4)
   Total Time Elapsed 34 ms


  dnRouter# run traceroute mpls ldp 1.2.3.4/32 multipath detail
  Tracing MPLS LSP, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds: 
  
  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code
  
  Type ctrl+c to abort
  
  L!
  Path 1 Found,
   output interface ge100-0/0/5 nexthop 10.1.17.7
   source 1.1.1.1 destination 127.0.0.64
    0 1.1.1.1 10.1.17.7 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.17.7 10.1.75.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 1 round-trip-delay 3 msec
      Target FEC stack sent: [0] LDP 1.2.3.4
      FEC-change received: pop-LDP (1.2.3.4), push-ISIS (1.2.3.4)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.75.5 round-trip-delay 4 msec
  
  L!
  Path 2 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.64
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.85.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 2 round-trip-delay 8 msec
      Target FEC stack sent: [0] LDP 1.2.3.4
      FEC-change received: pop-LDP (1.2.3.4), push-ISIS (1.2.3.4)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.85.5 round-trip-delay 20 msec
  
  !
  Path 3 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.66
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.58.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 2 round-trip-delay 20 msec
      Target FEC stack sent: [0] LDP 1.2.3.4
      FEC-change received: pop-LDP (1.2.3.4), push-ISIS (1.2.3.4)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.58.5 round-trip-delay 43 msec
 
  Paths (found/broken/unexplored) (3/0/0)
   Echo Request (sent/fail) (5/0)
   Echo Reply (received/timeout) (5/0)
   Total Time Elapsed 67 ms
    

**Command History**

+---------+-----------------------------------------------------------+
| Release | Modification                                              |
+=========+===========================================================+
| 15.0    | Command introduced                                        |
+---------+-----------------------------------------------------------+
| 15.1    | Updated command syntax to support detailed output         |
+---------+-----------------------------------------------------------+


---

## run traceroute mpls nil-fec.rst

run traceroute mpls nil-fec
---------------------------

**Minimum user role:** operator

You can manually run traceroute to a remote host for an LSP.

MPLS traceroute - used for hop-by-hop fault localization and/or path tracing: A packet is sent to the control plane of each transit LSR. The transit LSR performs various checks to confirm that it is indeed a transit LSR for this path; this LSR also returns additional information that helps check the control plane against the data plane.

The interval between probes is min{reply-time, timeout}. That is, either the echo reply receive time or the timeout (2 seconds) in case of no reply.

To start a traceroute for an LSP:

**Command syntax: run traceroute mpls nil-fec { labels [labels-stack] egress-interface [egress-interface] next-hop [next-hop-address] | policy [policy-name] }** multipath destination-address [destination-address] source-interface [source-interface] max-hops [max-hops] size [size] exp [exp] force-explicit-null ddmap detail

**Command mode:** operation

.. **Note**

  - If user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), packet size will be the minimum size required and no padding shall be used.

  - If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

  - The next-hop-address address family dictates the applicable source-interfaces (having IP address of the same AFI) and the valid destination-address range.

  - If packet is sent with MTU packet size bigger than path MTU, then MTU TX error counter will rise as no fragmentation is allowed.

  - Echo requests are sent by default with the DSMAP TLV, but DDMAP can be forced instead.

  - In the event that the user uses an unknown IP prefix, then the following message will be displayed: "no route exists" and traceroute action will stop.

  - If the multipath knob is used and there are multiple possible nexthops (ECMP), each possibe ECMP path and subsequent reported paths matching filters used will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies.

  - If the multipath knob is not used, echo request will be sent with the valid determined information, contingent on information provided by the operator, necessary to probe a single path, and no multipath information will be printed in CLI.

  - If next-hop is invalid or specified with address-family different than destination address-family ip address, then output code Q will be printed and error message will be displayed on the screen notifying: “no route to host via specified next-hop”.

  - User can stop traceroute requests using ctrl+c.

  - Total Time Elapsed in multipath traceroute represents the total time the traceroute operation took from start to finish.

  - In multipath traceroute each reported path is determined to be 'Found', 'Unexplorable' or 'Broken'. Found paths are valid paths for verified LSPs all the way to the egress LER; Unexplorable paths are discovered paths that could not be verified end-to-end for various reasons, inter alia, because the 127/8 destination IP address range used for the LSP selection has been exhausted, or due to disruptions along the LSP such as consecutive timeouts that break the trace (as opposed to certain non-compliant LSRs that are skipped) or TTL expiration; Broken paths indicate that the LSP is broken, meaning that traffic will not be sent across this path and may be discarded.

  - For multipath traceroute hops that timeout will be indicated in the summary of each path, but not in the detailed per-hop output.

  - FEC stack sent shows FEC stack from top to bottom of stack, left to right.

**Parameter table**

+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                                        | Range                                                                                                                                     | Default                                               |
+=====================+====================================================================================================================================================================================================================================================================================================================================================================================+===========================================================================================================================================+=======================================================+
| multipath           | Validates all reported paths.                                                                                                                                                                                                                                                                                                                                                      | \-                                                                                                                                        | \-                                                    |
|                     | If the multipath knob is used and there are multiple possible nexthops (ECMP), each possible ECMP path, and subsequent reported paths, that match used filters will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies. |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| label-stack         | The label-stack to be sent. Specified as incoming labels for the responding nodes. Multiple labels are separated by commas, from top to bottom of stack.                                                                                                                                                                                                                           | MPLS labels                                                                                                                               | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| policy-name         | The SR-TE policy name, from which the labels-stack to be sent is derived. Available policies will be listed for the user. If specified policy does not exist, then an error will be printed to the user.                                                                                                                                                                           | 1..255 characters (an existing SR-TE policy name)                                                                                         | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                                         | 1..255 characters (an existing interface name)                                                                                            | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an applicable AFI IP address, an error message is displayed.                                                                                                                                                                                                                                                            |                                                                                                                                           |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                                          |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| egress-interface    | Specifies the egress-interface from which the outgoing MPLS echo request is to be sent. Available interfaces under the VRF will be listed for the user.                                                                                                                                                                                                                            | 1..255 characters (an existing interface name)                                                                                            | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop-address    | Specifies the next hop as an IP address. Can be used for ECMP cases or if two entries exist in the RIB for the same IP FEC.                                                                                                                                                                                                                                                        | A.B.C.D                                                                                                                                   | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                                        | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) or an IPv6 address from the range 0:0:0:0:0:FFFF:7F00:0/104 | 127.0.0.1 or 0:0:0:0:0:FFFF:7F00:1                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed.                        | 100..9300                                                                                                                                 | packet size is determent according to the used TLVs   |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IP header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                                                      | 0..7                                                                                                                                      | 0                                                     |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| max-hops            | The maximum number of hops before the traceroute action is terminated (the maximum TTL value for the traceroute probe)                                                                                                                                                                                                                                                             | 1..255                                                                                                                                    | 30                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                                       | \-                                                                                                                                        | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| ddmap               | Forces the Downstream Detailed Mapping TLV instead of the deprecated DSMAP TLV.                                                                                                                                                                                                                                                                                                    | \-                                                                                                                                        | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| detail              | Prints a detailed output for every reply received.                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                           |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::

  dnRouter# run traceroute mpls nil-fec labels 16005,3 multipath ddmap detail
  Tracing MPLS LSP with Nil FEC with labels [16005,3]
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort

  L!
  Path 1 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.64
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 16005/implicit-null/explicit-null Exp: 0/0/0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.85.5 MPLS-MTU 1500 [Labels: implicit-null/implicit-null/explicit-null Exp: 0/0/0] multipaths 2 round-trip-delay 8 msec
      Target FEC stack sent: [0] Nil-FEC (explicit-null)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.85.5 round-trip-delay 20 msec

  !
  Path 2 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.66
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 16005/implicit-null/explicit-null Exp: 0/0/0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.58.5 MPLS-MTU 1500 [Labels: implicit-null/implicit-null/explicit-null Exp: 0/0/0] multipaths 2 round-trip-delay 20 msec
      Target FEC stack sent: [0] Nil-FEC (explicit-null)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.58.5 round-trip-delay 43 msec

  Paths (found/broken/unexplored) (2/0/0)
   Echo Request (sent/fail) (3/0)
   Echo Reply (received/timeout) (3/0)
   Total Time Elapsed 67 ms


  dnRouter# run traceroute mpls nil-fec policy-name Policy1
  Tracing MPLS LSP with Nil FEC for SR-TE policy Policy1
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code

  Type ctrl+c to abort

   output interface ge100-0/0/5 nexthop 10.1.17.7
   source 1.1.1.1 destination 127.0.0.1
    0 1.1.1.1 10.1.17.7 MPLS-MTU 1500 [Labels: 16005/explicit-null Exp: 0/0]
  L 1 10.1.17.7 10.1.75.5 MPLS-MTU 1500 [Labels: implicit-null/explicit-null Exp: 0/0] round-trip-delay 3 msec
  ! 2 10.1.75.5 round-trip-delay 4 msec


**Command History**

+---------+-----------------------------------------------------------+
| Release | Modification                                              |
+=========+===========================================================+
| 15.1    | Command introduced                                        |
+---------+-----------------------------------------------------------+
| 18.2    | Added support for IPv6                                    |
+---------+-----------------------------------------------------------+

---

## run traceroute mpls ospf.rst

run traceroute mpls ospf
-------------------------

**Minimum user role:** operator

You can manually run traceroute to a remote host for an OSPF LSP.

MPLS traceroute - used for hop-by-hop fault localization and/or path tracing: A packet is sent to the control plane of each transit LSR. The transit LSR performs various checks to confirm that it is indeed a transit LSR for this path; this LSR also returns additional information that helps check the control plane against the data plane.

The interval between probes is min{reply-time, timeout}. That is, either the echo reply receive time or the timeout (2 seconds) in case of no reply.

To start a traceroute for a OSPF LSP:

**Command syntax: run traceroute mpls ospf [target-address]** multipath destination-address [destination-address] next-hop [next-hop] source-interface [source-interface] size [size] exp [exp] max-hops [max-hops] force-explicit-null detail

**Command mode:** operation

.. **Note**

  - If packet is sent with MTU packet size bigger than path MTU, then MTU TX error counter will rise as no fragmentation is allowed.

  - If the next-hop-address is not a valid path for the LSP echo request, a "no FEC mapping" return code is applied.

  - Echo requests are sent with the DDMAP TLV.

  - In the event that the user uses an unknown IPv4 prefix, then the following message will be displayed: "no route exists" and traceroute action will stop.

  - If the multipath knob is used and there are multiple possible nexthops (ECMP), each possibe ECMP path and subsequent reported paths matching filters used will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies.

  - If the multipath knob is not used, echo request will be sent with the valid determined information, contingent on information provided by the operator, necessary to probe a single path, and no multipath information will be printed in CLI.

  - If next-hop is invalid or specified with address-family different than destination address-family ip address, then output code Q will be printed and error message will be displayed on the screen notifying: “no route to host via specified next-hop”.

  - User can stop traceroute requests using ctrl+c.

  - Total Time Elapsed in multipath traceroute represents the total time the traceroute operation took from start to finish.

  - In multipath traceroute each reported path is determined to be 'Found', 'Unexplorable' or 'Broken'. Found paths are valid paths for verified LSPs all the way to the egress LER; Unexplorable paths are discovered paths that could not be verified end-to-end for various reasons, inter alia, because the 127/8 destination IP address range used for the LSP selection has been exhausted, or due to disruptions along the LSP such as consecutive timeouts that break the trace (as opposed to certain non-compliant LSRs that are skipped) or TTL expiration; Broken paths indicate that the LSP is broken, meaning that traffic will not be sent across this path and may be discarded.

  - For multipath traceroute hops that timeout will be indicated in the summary of each path, but not in the detailed per-hop output.

  - If user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), packet size will be the minimum size required and no padding shall be used.

  - FEC stack sent shows FEC stack from top to bottom of stack, left to right.


**Parameter table**

+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                                        | Range                                                                         | Default                                               |
+=====================+====================================================================================================================================================================================================================================================================================================================================================================================+===============================================================================+=======================================================+
| target-address      | An IPv4 destination address FEC for SR OSPF FEC types. If the target-address is not a valid address known by OSPF, an error message is displayed.                                                                                                                                                                                                                                  | A.B.C.D/M                                                                     | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| multipath           | Validates all reported paths.                                                                                                                                                                                                                                                                                                                                                      | \-                                                                            | \-                                                    |
|                     | If the multipath knob is used and there are multiple possible nexthops (ECMP), each possible ECMP path, and subsequent reported paths, that match used filters will be validated end-to-end using the determined information as derived internally (egress interface, outgoing labels, destination address, etc.); or by downstream objects returned within the MPLS echo replies. |                                                                               |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| source-interface    | The interface from which the source IP is taken for the MPLS echo request.                                                                                                                                                                                                                                                                                                         | 1..255 characters (an existing interface name)                                | source-interface to egress-interface according to FIB |
|                     | If the source-interface is used but is not configured with an IPv4 address, an error message is displayed.                                                                                                                                                                                                                                                                         |                                                                               |                                                       |
|                     | If source-interface is not used, the source address of the egress interface from which the MPLS echo request is transmitted will be used.                                                                                                                                                                                                                                          |                                                                               |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| next-hop            | Specifies the next hop as an IP address. Can be used for ECMP cases or if two entries exist in the RIB for the same IPv4 FEC.                                                                                                                                                                                                                                                      | A.B.C.D                                                                       | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can send separate pings with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                                                        | within 127/8 ipv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) | 127.0.0.1                                             |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed.                        | 100..9300                                                                     | packet size is determent according to the used TLVs   |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IPv4 header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                                                    | 0..7                                                                          | 0                                                     |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| max-hops            | The maximum number of hops before the traceroute action is terminated (the maximum TTL value for the traceroute probe)                                                                                                                                                                                                                                                             | 1..255                                                                        | 30                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP ping to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                                                       | \-                                                                            | \-                                                    |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+
| detail              | Prints a detailed output for every reply received.                                                                                                                                                                                                                                                                                                                                 |                                                                               |                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------+

**Example**
::

  dnRouter# run traceroute mpls ospf 1.2.3.4/32
  Tracing MPLS LSP, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface,
  'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping,
  'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown,
  'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry,
  'P' - no receive interface label protocol, 'p' - premature termination of the LSP
  'l' - label switched with FEC stack change, 'd' - see DDMAP for return code,
  'X' - undefined return code, 'x' - no return code,

  Type ctrl+c to abort

   output interface ge100-0/0/5 nexthop 10.1.17.7
   source 1.1.1.1 destination 127.0.0.1
    0 1.1.1.1 10.1.17.7 MPLS-MTU 1500 [Labels: 24002 Exp: 0]
  L 1 10.1.17.7 10.1.75.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] round-trip-delay 3 msec
  ! 2 10.1.75.5 round-trip-delay 4 msec


  dnRouter# run traceroute mpls ospf 2.2.2.2/32 multipath
  Tracing MPLS LSP, target ipv4-address: 2.2.2.2/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface,
  'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping,
  'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown,
  'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry,
  'P' - no receive interface label protocol, 'p' - premature termination of the LSP
  'l' - label switched with FEC stack change, 'd' - see DDMAP for return code,
  'X' - undefined return code, 'x' - no return code,

  Type ctrl+c to abort

  LL....
  Path 1 Unexplorable,
   output interface ge100-0/0/0 nexthop 10.1.1.13
   source 10.1.1.2 destination 127.0.0.64
    0 10.1.1.2 10.1.1.13 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  L 1 10.1.1.13 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec
  L 2 10.1.1.10 10.1.91.10 MPLS-MTU 1500 [Labels: 802809 Exp: 0] multipaths 3 round-trip-delay 4 msec

  LL!
  Path 2 Found,
   output interface ge100-0/0/2 nexthop 10.1.1.1
   source 10.1.1.17 destination 127.0.1.64
    0 10.1.1.2 10.1.1.1 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  L 1 10.1.1.1 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec
  L 2 10.1.1.10 0.1.91.6 MPLS-MTU 1500 [Labels: 802809 Exp: 0] multipaths 3 round-trip-delay 4 msec
  ! 3 10.1.64.5 multipaths 0 round-trip-delay 5 msec

  B
  Path 3 Broken,
   output interface ge100-0/0/2 nexthop 10.1.1.1
   source 10.1.1.17 destination 127.0.1.66
    0 10.1.1.17 10.1.1.22 MPLS-MTU 1500 [Labels: 24023 Exp: 0] multipaths 0
  B 1 10.1.1.22 10.1.1.10 MPLS-MTU 1500 [Labels: 18809 Exp: 0] multipaths 1 round-trip-delay 2 msec

  Paths (found/broken/unexplored) (1/1/1)
   Echo Request (sent/fail) (10/0)
   Echo Reply (received/timeout) (6/4)
   Total Time Elapsed 34 ms


  dnRouter# run traceroute mpls ospf 1.2.3.4/32 multipath detail
  Tracing MPLS LSP, target ipv4-address: 1.2.3.4/32
  Timeout is 2 seconds:

  Legend:
  '!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface,
  'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping,
  'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown,
  'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry,
  'P' - no receive interface label protocol, 'p' - premature termination of the LSP
  'l' - label switched with FEC stack change, 'd' - see DDMAP for return code,
  'X' - undefined return code, 'x' - no return code,

  Type ctrl+c to abort

  L!
  Path 1 Found,
   output interface ge100-0/0/5 nexthop 10.1.17.7
   source 1.1.1.1 destination 127.0.0.64
    0 1.1.1.1 10.1.17.7 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.17.7 10.1.75.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 1 round-trip-delay 3 msec
      Target FEC stack sent: [0] ospf 1.2.3.4
      FEC-change received: pop-ospf (1.2.3.4), push-LDP (1.2.3.4)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.75.5 round-trip-delay 4 msec

  L!
  Path 2 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.64
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.85.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 2 round-trip-delay 8 msec
      Target FEC stack sent: [0] ospf 1.2.3.4
      FEC-change received: pop-ospf (1.2.3.4), push-LDP (1.2.3.4)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.85.5 round-trip-delay 20 msec

  !
  Path 3 Found,
   output interface ge100-0/0/6 nexthop 10.1.18.8
   source 1.1.1.1 destination 127.0.0.66
    0 1.1.1.1 10.1.18.8 MPLS-MTU 1500 [Labels: 24002 Exp: 0] multipaths 0
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  L 1 10.1.18.8 10.1.58.5 MPLS-MTU 1500 [Labels: implicit-null Exp: 0] multipaths 2 round-trip-delay 20 msec
      Target FEC stack sent: [0] ospf 1.2.3.4
      FEC-change received: pop-ospf (1.2.3.4), push-LDP (1.2.3.4)
      Multipath type: bit-masked IP, base address: 127.0.0.64, mask: FFFFFFFF
  ! 2 10.1.58.5 round-trip-delay 43 msec

  Paths (found/broken/unexplored) (3/0/0)
   Echo Request (sent/fail) (5/0)
   Echo Reply (received/timeout) (5/0)
   Total Time Elapsed 67 ms


**Command History**

+---------+-----------------------------------------------------------+
| Release | Modification                                              |
+=========+===========================================================+
| 17.1    | Command introduced                                        |
+---------+-----------------------------------------------------------+

---

## run traceroute mpls rsvp.rst

run traceroute mpls rsvp
------------------------

**Minimum user role:** operator

You can manually run traceroute to a remote host for an RSVP tunnel.

MPLS traceroute - used for hop-by-hop fault localization and/or path tracing: A packet is sent to the control plane of each transit LSR. The transit LSR performs various checks to confirm that it is indeed a transit LSR for this path; this LSR also returns additional information that helps check the control plane against the data plane.

The interval between probes is min{reply-time, timeout}. That is, either the echo reply receive time or the timeout (2 seconds) in case of no reply.

To start a traceroute for an RSVP tunnel:

**Command syntax: run traceroute mpls rsvp [tunnel-name]** destination-address [destination-address] max-hops [max-hops] size [size] exp [exp] force-explicit-null ddmap detail

**Command mode:** operation 

**Note**

- If you run the command on a tunnel that does not exist, or if the tunnel is down, an error message is displayed.

.. - if user set packet size to be smaller than the minimum size required to carry the mandatory TLVs (without padding), packet size will be the minimum size required and no padding will be used.

	- If packet is sent with MTU packet size bigger than path MTU, then MTU TX error counter will raise as no fragmentation is allowed.

	- Echo requests are sent by default with the DSMAP TLV, but DDMAP can be forced instead.

	- In case the user uses a non-existing tunnel, the following message will be displayed: "no tunnel exists" and traceroute action will stop.

	- In case tunnel is down, an echo request will not be sent, and the following message will be displayed "no tunnel exists" and traceroute action will stop.

	- User can stop traceroute requests using Ctrl+c

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| Parameter           | Description                                                                                                                                                                                                                                                                                                                                                 | Range                                                                         | Default                                             |
+=====================+=============================================================================================================================================================================================================================================================================================================================================================+===============================================================================+=====================================================+
| tunnel-name         | The name of an existing tunnel on which to run the traceroute. You can run traceroute on any tunnel type: primary, bypass, auto-bypass, auto-mesh.                                                                                                                                                                                                          | 1..255 characters                                                             | \-                                                  |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| destination-address | A local host destination address. When the LSP has ECMP, you can run separate traceroutes with different destination addresses in order to change the packet flow and cover the different paths.                                                                                                                                                            | within 127/8 IPv4 subnet addresses (127.x.y.z with subnet masks from 8 to 32) | 127.0.0.1                                           |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| max-hops            | The maximum number of hops before the traceroute action is terminated (the maximum TTL value for the traceroute probe)                                                                                                                                                                                                                                      | 1..255                                                                        | 30                                                  |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| size                | The size of echo request packets. If you set a size that is smaller than the minimum required to support of TLVs, then the echo request packets will not be padded and the default size will be used instead. If packets are sent with an MTU packet size larger than the path MTU, the MTU TX error counter will increment as no fragmentation is allowed. | 100..65507                                                                    | packet size is determent according to the used TLVs |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| exp                 | MPLS experimental field value in the MPLS header for echo requests. All inner layers will also be set with a matching CoS value, including the IP precedence field of the IPv4 header. The MPLS echo reply is always sent with IP precedence 6.                                                                                                             | 0..7                                                                          | 0                                                   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| force-explicit-null | Forces an unsolicited explicit null label to be added to the MPLS label stack and allows LSP traceroute to be used to detect LSP breakages at the penultimate hop.                                                                                                                                                                                          | \-                                                                            | \-                                                  |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| ddmap               | Forces the Downstream Detailed Mapping TLV instead of the deprecated DSMAP TLV                                                                                                                                                                                                                                                                              | \-                                                                            | \-                                                  |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
| detail              | Prints a detailed output for every reply received.                                                                                                                                                                                                                                                                                                          |                                                                               |                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+

**Example**
::

	
	dnRouter# run traceroute mpls rsvp TUNNEL_1 
	Tracing MPLS LSP, target rsvp tunnel: TUNNEL_1
	Timeout is 2 seconds: 
	
	Legend:
	'!' - success, '.' - timeout, 'Q' - request not sent, 'L' - labeled output interface, 'M' - malformed echo request, 'm' - TLVs not understood, 'F' - no FEC mapping, 'D' - downstream Mapping Mismatch, 'I' - upstream Interface Index Unknown, 'B' - unlabeled output interface, 'f' - FEC mismatch, 'N' - no label entry, 'P' - no receive interface label protocol, 'p' - premature termination of the LSP, 'l' - label switched with FEC stack change, 'd' - see DDMAP for return code, 'X' - undefined return code, 'x' - no return code
	
	Type ctrl+c to abort 
	Destination address 127.0.0.1
	     0 10.131.191.230 MPLS-MTU 1500 [Labels: 19 Exp: 0]
	L 1 10.131.159.226 MPLS-MTU 1504 [implicit-null] round-trip-delay 20 msec
	! 2 10.131.159.225 rtt 40 msec
	
	

**Command History**

+---------+----------------------------------------------------+
| Release | Modification                                       |
+=========+====================================================+
| 11.0    | Command introduced                                 |
+---------+----------------------------------------------------+
| 15.0    | Updated command syntax                             |
+---------+----------------------------------------------------+
| 15.1    | Updated command syntax to support ddmap and detail |
+---------+----------------------------------------------------+


---

## run traceroute.rst

run traceroute
--------------

**Minimum user role:** viewer

The run traceroute command displays the route that packets take to the specified destination address. When enabled, the router sends out a number of probes (UDP packets) set by the count parameter to the destination IP. This command is useful to locate points of failure in the network.

**Command syntax: run traceroute dest-ip** vrf [vrf-name] source-interface [source-interface] dscp [dscp] max-hops [max-hops] dns-resolve df
**Command syntax: run traceroute host-name** vrf [vrf-name] source-interface [source-interface] dscp [dscp] max-hops [max-hops] dns-resolve df
**Command syntax: run traceroute** vrf [vrf-name] source-interface [source-interface] dscp [dscp] max-hops [max-hops] dns-resolve df

**Command mode:** operation

**Note**

- The NCC handles ICMP packets. Therefore, traceroute to a remote host should be done from the NCC and not from the NCPs.

.. - The traceroute command is one-line format. meaning - all parameters can be entered on the same line

	 - run traceroute [dest-ip]source-interface [source-interface] - The traceroute packet should be sent with the defined ip address of the source interface.

	 - When using dns-resolve, we should remove the "-n" option

	 - Any VRF in the system will be listed and made available, including the four system-default VRFs (default, mgmt0, mgmt-ncc-0 and mgmt-ncc-1). Unless a valid VRF is explicitly specified, the default VRF will be used

	 - The run traceroute command may include source-interface. When a VRF is specified, only relevant source-interfaces attached to that VRF will be listed under it and made available. Otherwise, only interfaces under the default VRF will be listed

	 - By default, source-address should be assigned based on RIB resolution of egress-interface towards the destination

	 - If traceroute is initiated towards BGP-VPN prefix, then a random source-address will be assigned based on any attached UP interface with configured IP address inside the VRF. If no interface is attached, error message should be printed stating: "Cannot assign source address"

	 - DNS resolution for traceroute command requested with host-name address within a VRF is done per system based on DNS servers priorities

	 - If the IP destination address is a Link-Local address, then an applicable source interface will be chosen and link-local source address will be used (or retrieved from source-interface). If the IP destination address is Global Unicast address, then an applicable source interface will be chosen and global unicast source address will be used (or retrieved from source-interface)

**Parameter table**

The following are the parameters for this command:

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| Parameter        | Description                                                                                                                                                                                                  | Range                                              | Default |
+==================+==============================================================================================================================================================================================================+====================================================+=========+
| dest-ip          | The IPv4 or IPv6 address of the remote host to trace                                                                                                                                                         | x.x.x.x                                            | \-      |
|                  |                                                                                                                                                                                                              | x:x::x:x                                           |         |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| host-name        | The name of the target host to trace                                                                                                                                                                         | String                                             | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| vrf-name         | The name of the target VRF                                                                                                                                                                                   | String                                             | default |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| source-interface | Sends the traceroute packets with the defined IP address of the source interface                                                                                                                             | ge<interface speed>-<A>/<B>/<C>                    | \-      |
|                  |                                                                                                                                                                                                              |                                                    |         |
|                  |                                                                                                                                                                                                              | ge<interface speed>-<A>/<B>/<C>.<sub-interface id> |         |
|                  |                                                                                                                                                                                                              |                                                    |         |
|                  |                                                                                                                                                                                                              | bundle-<bundle id>                                 |         |
|                  |                                                                                                                                                                                                              |                                                    |         |
|                  |                                                                                                                                                                                                              | bundle-<bundle id>.<sub-interface id>              |         |
|                  |                                                                                                                                                                                                              |                                                    |         |
|                  |                                                                                                                                                                                                              | lo<lo-interface id>                                |         |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| dscp             | The IPv4/IPv6 DSCP value                                                                                                                                                                                     | 0..56                                              | 0       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| max-hops         | The maximum number of hops that the trace packet should cross before timeout                                                                                                                                 | 1..255                                             | 30      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| dns-resolve      | Queries the DNS server to resolve the IP addresses of the next hops. By default, only the IP address is returned, unless dns-resolve is explicitly specified                                                 | \-                                                 | \-      |
|                  | Note, using the dns-resolve option may significantly slow down the response time                                                                                                                             |                                                    |         |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| df               | Do not fragment - a flag specifying that outgoing packets must not be fragmented. The packets will be sent in their original size. If the size exceeds the egress interface MTU, the packet will be dropped  | Boolean                                            | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+

The parameters can all be specified in the same command.

**Example**
::

	dnRouter# run traceroute 1.1.1.1
	dnRouter# run traceroute 2001:1234::1
	dnRouter# run traceroute source-interface lo0
	dnRouter# run traceroute 1.1.1.1 max-hops 2
	dnRouter# run traceroute 1.1.1.1 dscp 4
	dnRouter# run traceroute 1.1.1.1 dns-resolve
	dnRouter# run traceroute 1.1.1.1 vrf mgmt0
	dnRouter# run traceroute 1.1.1.1 vrf mgmt-ncc-0 max-hops 9
	dnRouter# run traceroute 1.1.1.1 vrf mgmt-ncc-1 source-interface mgmt-ncc-1
	dnrouter# run traceroute google.com vrf MyVrf1

.. **Help line:** run traceroute request

**Command History**

+---------+------------------------------------------------------------------------------------------------------------+
| Release | Modification                                                                                               |
+=========+============================================================================================================+
| 5.1.0   | Command introduced                                                                                         |
+---------+------------------------------------------------------------------------------------------------------------+
| 10.0    | Removed dns-resolve option                                                                                 |
+---------+------------------------------------------------------------------------------------------------------------+
| 11.0    | Removed VRF filter, added option to trace a host-name, added dscp dns-resolve, and option to not fragment  |
+---------+------------------------------------------------------------------------------------------------------------+
| 11.2    | Removed size from the syntax                                                                               |
+---------+------------------------------------------------------------------------------------------------------------+
| 13.1    | Added support for host VRF                                                                                 |
+---------+------------------------------------------------------------------------------------------------------------+
| 16.1    | Removed egress-interface knob                                                                              |
+---------+------------------------------------------------------------------------------------------------------------+
| 25.2    | Command syntax change                                                                                      |
+---------+------------------------------------------------------------------------------------------------------------+


---


---

# SECTION 2: MISC COMMANDS

Files from Misc Commands folder:        6 files

## load merge.rst

load merge
----------

**Minimum user role:** operator

You can load a saved configuration file to replace the current running configuration. This command is useful for reverting to a previous configuration, transferring a configuration from one server to another, and for systematically adding or removing configurations.

To load a saved configuration, use the following command:

**Command syntax: load merge** user-specific **[file-name]**

**Command mode:** configuration

.. **Note**

	- The operation is load-merge - could be for a partial config

	- If user-specific is set, the configuration is loaded from the config directory of the current user. This directory can be accessed by this user only

	- NCC config located at:

	- config - /config/

	- user-specific config - /home/[user]/config/

	- rollback - /rollback

	- Configuration files are saved and loaded from the active NCC.

**Parameter table**

+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------+
| Parameter     | Description                                                                                                                                | Range             | Default |
+===============+============================================================================================================================================+===================+=========+
| file-name     | The name of the saved file in the configuration folder. Enter the file name as it appears in the configuration folder.                     | 1..255 characters | \-      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------+
| user-specific | When specified, the configuration is loaded from the config directory of the current user. This directory is accessible to this user only. | \-                | \-      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------+

Configuration files are saved and loaded from the active NCC at:

- config - /config/

- rollback - /rollback/

- user-specific config - /home/[user]/config/

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# load merge MyConfig.txt

	dnRouter# configure
	dnRouter(cfg)# load merge user-specific MyConfig.txt



.. **Help line:** merge the file content with the candidate configuration

**Command History**

+---------+--------------------------------------------------+
| Release | Modification                                     |
+=========+==================================================+
| 5.1.0   | Command introduced                               |
+---------+--------------------------------------------------+
| 6.0     | Changed to a configuration command               |
+---------+--------------------------------------------------+
| 11.0    | Added option to load from "user-specific" folder |
+---------+--------------------------------------------------+



---

## load override golden-config.rst

load override golden-config
---------------------------

**Minimum user role:** admin

To replace the current configuration with the golden-config content:

**Command syntax: load override golden-config**

**Command mode:** configuration

**Note**

- Command requires a valid golden-config file saved to the system.

.. - After issuing the command the system will replace all configurations with the golden-config settings and will reboot.

	**Internal Note**
	- Yes/no validation should be added
	- Command should fail with proper indication in CLI on all non NCP6 Ufispace Q2C+ (Emux) platforms

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# load override golden-config
	Warning: Are you sure you want to remove existing configuration and reboot with golden-config settings? (Yes/No) [No]
	Commit succeeded by ADMIN at 27-Jan-2024 12:21:00 UTC


	dnRouter# configure
	dnRouter(cfg)# load override golden-config
	Command not supported on platform

.. **Help line:** replace current configuration with golden-config file content and reboot the system

**Command History**

+---------+--------------------------------------------------+
| Release | Modification                                     |
+=========+==================================================+
| 19.1    | Command introduced                               |
+---------+--------------------------------------------------+

---

## load override.rst

load override
-------------

**Minimum user role:** operator

To replace the candidate configuration with the file content:

**Command syntax: load override {[file-name] \| factory-default \| golden-config}**

**Command mode:** configuration

**Note**

- You must perform commit after the load override operation for the candidate configuration to take effect.

.. - User should perform "commit" command after load override operation for the candidate configuration to be committed.

	- If user-specific is set, the configuration is loaded from the config directory of the current user. This directory can be accessed by this user only

	- Loaded file can be only config file.

	- NCC config located at:

	- config - /config/

	- user-specific config - /home/[user]/config/

	- rollback - /rollback

	- Configuration files are saved and loaded from the active NCC.

**Parameter table**

+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------+
| Parameter       | Description                                                                                                                                                      | Range             | Default |
+=================+==================================================================================================================================================================+===================+=========+
| file-name       | The name of the file with which to replace the configuration. Only configuration files.                                                                          | 1..255 characters | \-      |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------+
| factory-default | Replaces the candidate configuration with the default configuration.                                                                                             | \-                | \-      |
|                 | This option removes all configuration, including all users, passwords, and cluster NCPs. Removing the cluster NCPs will cause the network interfaces to go down. |                   |         |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------+
| user-specific   | When specified, the configuration is loaded from the config directory of the current user. This directory is accessible to this user only.                       | \-                | \-      |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------+

Configuration files are saved and loaded from the active NCC at:

- config - /config/

- rollback - /rollback/

- user-specific config - /home/[user]/config/

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# load override MyConfig.txt
	configuration load complete

	dnRouter(cfg)# load override user-specific MyConfig.txt
	configuration load complete

	dnRouter# configure
	dnRouter(cfg)# load override factory-default
	configuration load complete


.. **Help line:** replace the candidate configuration with the file content

**Command History**

+---------+--------------------------------------------------+
| Release | Modification                                     |
+=========+==================================================+
| 6.0     | Command introduced                               |
+---------+--------------------------------------------------+
| 11.0    | Added option to load from "user-specific" folder |
+---------+--------------------------------------------------+
| 25.2    | Command syntax changed                           |
+---------+--------------------------------------------------+


---

## pipe commands.rst

pipe commands
-------------

**Minimum user role:** viewer

Pipe commands filter the output of show commands. The supported pipe commands are:

no-more: show all CLI output without the "more" option.

include: filter the results that include a requested parameter (whole word or part of a word). Can be used in combination with "leading [value]" or "trailing [value]" to provide context (up to 1000 lines) for the match:

- trailing <num> - Print the number of lines of trailing context after the matching line.

- leading <num> - Print the number of lines of leading context before the matching line.

find - The first occurrence of the object treated. The command will “find” the first line in the output that meets the criteria and display all of the output until the end of. The operator can use trailing, leading or both for any given “find”. The maximum number of lines to be found for leading and trailing is limited to 1000. The regex option can be combined in find. Match is case-insensitive. To run a case-sensitive match, use "case-sensitive" after <text>.

exclude: filter the results that exclude the requested parameter (whole word or part of a word).

case-sensitive: By default, all pattern match are case-insensitive, to run a case-sensitive match, use "case-sensitive" after <text> for "include", "exclude", "find" request, including "regex" option.

regex: filter the results using regular expression. Can be used with include , exclude or find commands.

display-headers: use for displaying table headers. By default, the table headers are not displayed when using pipe commands.

monitor: an augmented flag to show command for displaying CLI output at regular intervals. The command output is refreshed compared to the previous output at regular configured intervals. The filters are applied to the entries only, not including the table headers.

You can use the monitor command in combination with the following commands:

- interval: set the interval time (in seconds) between CLI command output refreshes. Range: 1..3600 seconds; Default: 3

- diff: highlights the difference from the previous CLI command output refresh.

count: count and display the number of lines in the output. The count option should be the last pipe, and will count the output lines after all other filtering options such as include/exclude/regex. There may be 3 pipes combined and the output will show the total number of lines. An empty output will result in 0 lines.

tail - The command will show the last <num> of lines from the file. If <num> is not provided, the last 100 lines will be displayed by default.

The pipe command follows the show command and is separated by the pipe character (|). Pipe commands can be concatenated to further filter the displayed output:

**Command syntax: show** parameter [parameter-value] **\| pipe-command** \| pipe-command .

**Command mode:** operational

**Example**

The pipe commands are demonstrated here on the show interfaces ip command. The following is the output of this command without any pipe command:

::

	dnRouter# show interfaces ip | monitor
	dnRouter# show interfaces ip | no-more
	dnRouter# show interfaces ip | include [value]
	dnRouter# show interfaces ip | include regex [value]
	dnRouter# show interfaces ip | exclude [value]
	dnRouter# show interfaces ip | exclude regex [value]
	dnRouter# show interfaces ip | include [value] display-headers
	dnRouter# show interfaces ip | find "[value]" trailing [value] leading [value]
	dnRouter# show interfaces ip | tail [value]
	dnRouter# show interfaces ip | count

	dnRouter# show interfaces ip | include down trailing 1
	dnRouter# show interfaces ip | include down trailing 1 leading 4

	dnRouter# show interfaces ip

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| bundle-3        | enabled  | up          | 30.1.1.1/30    | 2001:1234::1/122               |
	| bundle-3.200    | enabled  | up          | 30.4.4.1/30    | 1006:abcd:12::2/128            |
	| ge100-2/1/1     | disabled | down        | 30.2.2.1/30    | 1001:abcd:12::2/128            |
	| ge100-2/1/1.100 | enabled  | up          |                |                                |
	| ge100-3/1/1     | enabled  | up          |                |                                |
	| lo1             | disabled | down 	   | 1.1.1.1/32     | 2001::0001:0001:0001:0001/128  |

	dnRouter# show interfaces ip | find "ge100"

	| ge100-2/1/1     | disabled | down        | 30.2.2.1/30    | 1001:abcd:12::2/128            |
	| ge100-2/1/1.100 | enabled  | up          |                |                                |
	| ge100-3/1/1     | enabled  | up          |                |                                |
	| lo1             | disabled | down 	   | 1.1.1.1/32     | 2001::0001:0001:0001:0001/128  |

	dnRouter# show interfaces ip | find "bundle" trailing 2 | tail 1

	| ge100-2/1/1     | disabled | down        | 30.2.2.1/30    | 1001:abcd:12::2/128            |

	dnRouter# show interfaces ip | find "lo1" leading 2

	| ge100-2/1/1.100 | enabled  | up          |                |                                |
	| ge100-3/1/1     | enabled  | up          |                |                                |
	| lo1             | disabled | down 	   | 1.1.1.1/32     | 2001::0001:0001:0001:0001/128  |

	dnRouter# show interfaces ip | include bundle-3 display-headers

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| bundle-3        | enabled  | up          | 30.1.1.1/30    | 2001:1234::1/122               |
	| bundle-3.200    | enabled  | up          | 30.4.4.1/30    | 1006:abcd:12::2/128            |

	dnRouter# show rsvp tunnels | include To-XRV1 case-sensitive

	1.1.1.1         5.5.5.5         head     down    -       -        2h45m36s         To-XRV1


	dnRouter# show interfaces ip | include bundle-3 | count

	lines: 2

	dnRouter# show interfaces ip | include bundle-3 display-headers | count

	lines: 4

	dnRouter# show interfaces ip | include regex ge\d+ display-headers

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| ge100-2/1/1     | disabled | down        | 30.2.2.1/30    | 1001:abcd:12::2/128            |
	| ge100-2/1/1.100 | enabled  | up          |                |                                |
	| ge100-3/1/1     | enabled  | up          |                |                                |

	dnRouter# show interfaces ip | include bundle-3 | include abcd display-headers

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| bundle-3.200    | enabled  | up          | 30.4.4.1/30    | 1006:abcd:12::2/128            |

	dnRouter# show interfaces ip | include bundle-3 | exclude abcd display-headers

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| bundle-3        | enabled  | up          | 30.1.1.1/30    | 2001:1234::1/122               |


	dnRouter# show interfaces ip | include regex bundle-3|abcd display-headers

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| bundle-3.200    | enabled  | up          | 30.4.4.1/30    | 1006:abcd:12::2/128            |

	dnRouter# show interfaces ip | include regex bundle-3|abcd

	| bundle-3.200    | enabled  | up          | 30.4.4.1/30    | 1006:abcd:12::2/128            |

	dnRouter# show interfaces ip | exclude bundle-3 display-headers

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| ge100-2/1/1     | disabled | down        | 30.2.2.1/30    | 1001:abcd:12::2/128            |
	| ge100-2/1/1.100 | enabled  | up          |                |                                |
	| ge100-3/1/1     | enabled  | up          |                |                                |
	| lo1             | disabled | down        | 1.1.1.1/32     | 2001::0001:0001:0001:0001/128  |

	dnRouter# show interfaces ip | exclude regex ge\d+ display-headers

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| bundle-3        | enabled  | up          | 30.1.1.1/30    | 2001:1234::1/122               |
	| bundle-3.200    | enabled  | up          | 30.4.4.1/30    | 1006:abcd:12::2/128            |
	| lo1             | disabled | down        | 1.1.1.1/32     | 2001::0001:0001:0001:0001/128  |

	dnRouter# show interfaces ip | exclude regex bundle-3|ge100 display-headers

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| lo1             | disabled | down        | 1.1.1.1/32     | 2001::0001:0001:0001:0001/128  |

	dnRouter# show interfaces ip | exclude regex bundle-3|ge100

	| lo1             | disabled | down        | 1.1.1.1/32     | 2001::0001:0001:0001:0001/128  |

	dnRouter# show interfaces ip | monitor

	Every 3s: show interfaces ip                                               2020-01-23 16:08:27

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| bundle-3        | enabled  | up          | 30.1.1.1/30    | 2001:1234::1/122               |
	| bundle-3.200    | enabled  | up          | 30.4.4.1/30    | 1006:abcd:12::2/128            |
	| ge100-2/1/1     | disabled | down        | 30.2.2.1/30    | 1001:abcd:12::2/128            |
	| ge100-2/1/1.100 | enabled  | up          |                |                                |
	| ge100-3/1/1     | enabled  | up          |                |                                |
	| lo1             | disabled | down        | 1.1.1.1/32     | 2001::0001:0001:0001:0001/128  |

	dnRouter# show interfaces ip | monitor

	Every 3s: show interfaces ip                                               2020-01-23 16:08:27

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| bundle-3        | enabled  | up          | 30.1.1.1/30    | 2001:1234::1/122               |
	| bundle-3.200    | enabled  | up          | 30.4.4.1/30    | 1006:abcd:12::2/128            |
	| ge100-2/1/1     | disabled | down        | 30.2.2.1/30    | 1001:abcd:12::2/128            |
	| ge100-2/1/1.100 | enabled  | up          |                |                                |
	| ge100-3/1/1     | enabled  | up          |                |                                |
	| lo1             | disabled | down        | 1.1.1.1/32     | 2001::0001:0001:0001:0001/128  |

	Press CTRL+C to quit

	dnRouter# show interfaces ip | monitor interval 10 diff

	Every 10s: show interfaces ip                                              2020-01-23 16:08:27

	| Interface       | Admin    | Operational | IPv4 Address   | IPv6 Address                   |
	+-----------------+----------+-------------+----------------+--------------------------------+
	| bundle-3        | enabled  | up          | 30.1.1.1/30    | 2001:1234::1/122               |
	| bundle-3.200    | enabled  | down        | 30.4.4.1/30    | 1006:abcd:12::2/128            |
	| ge100-2/1/1     | disabled | down        | 30.2.2.1/30    | 1001:abcd:12::2/128            |
	| ge100-2/1/1.100 | enabled  | up          |                |                                |
	| ge100-3/1/1     | enabled  | up          |                |                                |
	| lo1             | disabled | down        | 1.1.1.1/32     | 2001::0001:0001:0001:0001/128  |


	Press CTRL+C to quit

	dnRouter# show interfaces ip | include down trailing 1
	| bundle-263.1264      | disabled | down            | 1.12.51.0/31       | 2001:12:51::/127                            |
	| bundle-263.2702      | enabled  | up              | 6.12.90.0/31       | 2006:12:90::/127                            |
	--
	| bundle-1112          | enabled  | down            | 1.11.12.1/31       | 2001:11:12::1/127                           |
	| bundle-1213          | enabled  | down            | 1.12.13.0/31       | 2001:12:13::/127                            |
	| bundle-1215          | disabled | down            | 1.12.15.0/31       | 2001:12:15::/127                            |
	| bundle-1216          | enabled  | up              | 1.12.16.0/31       | 2001:12:16::/127                            |
	--
	| bundle-1230          | disabled | down            | 1.12.30.0/31       | 2001:12:30::/127                            |
	| ge10-0/0/11/0        | disabled | down            |                    |                                             |
	| ge10-0/0/11/1        | enabled  | down            |                    |                                             |
	| ge10-0/0/11/2        | enabled  | down            |                    |                                             |
	| ge10-0/0/11/3        | enabled  | down            |                    |                                             |
	| ge100-0/0/0          | enabled  | down            |                    |                                             |
	| ge100-0/0/1          | enabled  | down            |                    |                                             |
	| ge100-0/0/2          | disabled | down            |                    |                                             |
	| ge100-0/0/3          | disabled | down            |                    |                                             |
	| ge100-0/0/4          | enabled  | down            |                    |                                             |
	| ge100-0/0/5          | enabled  | down            |                    |                                             |
	| ge100-0/0/6          | enabled  | down            |                    |                                             |
	| ge100-0/0/7          | enabled  | down            |                    |                                             |
	| ge100-0/0/8          | enabled  | down            |                    |                                             |
	| ge100-0/0/9          | disabled | down            |                    |                                             |
	| ge100-0/0/10         | disabled | down            |                    |                                             |
	| ge100-0/0/11         | disabled | not-present     |                    |                                             |

	dnRouter# show interfaces ip | include down trailing 1 leading 4
	| bundle-252.1348      | enabled  | up              | 5.12.93.246/31     | 2005:12:93::f6/127                          |
	| bundle-252.1349      | enabled  | up              | 5.12.93.248/31     | 2005:12:93::f8/127                          |
	| bundle-253           | enabled  | up              |                    |                                             |
	| bundle-263           | enabled  | up              |                    |                                             |
	| bundle-263.1264      | disabled | down            | 1.12.51.0/31       | 2001:12:51::/127                            |
	| bundle-263.2702      | enabled  | up              | 6.12.90.0/31       | 2006:12:90::/127                            |
	--
	--
	| bundle-263.2702      | enabled  | up              | 6.12.90.0/31       | 2006:12:90::/127                            |
	| bundle-263.2703      | enabled  | up              | 7.12.90.0/31       | 2007:12:90::/127                            |
	| bundle-1112          | enabled  | down            | 1.11.12.1/31       | 2001:11:12::1/127                           |
	| bundle-1213          | enabled  | down            | 1.12.13.0/31       | 2001:12:13::/127                            |
	| bundle-1215          | disabled | down            | 1.12.15.0/31       | 2001:12:15::/127                            |
	| bundle-1216          | enabled  | up              | 1.12.16.0/31       | 2001:12:16::/127                            |
	--
	--
	| bundle-1216          | enabled  | up              | 1.12.16.0/31       | 2001:12:16::/127                            |
	| bundle-1218          | enabled  | up              | 1.12.18.0/31       | 2001:12:18::/127                            |
	| bundle-1230          | disabled | down            | 1.12.30.0/31       | 2001:12:30::/127                            |
	| ge10-0/0/11/0        | disabled | down            |                    |                                             |
	| ge10-0/0/11/1        | enabled  | down            |                    |                                             |
	| ge10-0/0/11/2        | enabled  | down            |                    |                                             |
	| ge10-0/0/11/3        | enabled  | down            |                    |                                             |
	| ge100-0/0/0          | enabled  | down            |                    |                                             |
	| ge100-0/0/1          | enabled  | down            |                    |                                             |
	| ge100-0/0/2          | disabled | down            |                    |                                             |
	| ge100-0/0/3          | disabled | down            |                    |                                             |
	| ge100-0/0/4          | enabled  | down            |                    |                                             |
	| ge100-0/0/5          | enabled  | down            |                    |                                             |
	| ge100-0/0/6          | enabled  | down            |                    |                                             |
	| ge100-0/0/7          | enabled  | down            |                    |                                             |
	| ge100-0/0/8          | enabled  | down            |                    |                                             |
	| ge100-0/0/9          | disabled | down            |                    |                                             |
	| ge100-0/0/10         | disabled | down            |                    |                                             |
	| ge100-0/0/11         | disabled | not-present     |                    |                                             |

**Command History**

+---------+------------------------------------------------------------------+
| Release | Modification                                                     |
+=========+==================================================================+
| 5.1.0   | Command introduced                                               |
+---------+------------------------------------------------------------------+
| 9.0     | Updated available pipe commands                                  |
+---------+------------------------------------------------------------------+
| 11.5    | Added ability to display table-headers                           |
+---------+------------------------------------------------------------------+
| 13.2    | Updated available pipe commands                                  |
+---------+------------------------------------------------------------------+
| 13.3    | Added leading and trailing options for "include" pipe operations |
+---------+------------------------------------------------------------------+
| 18.2    | Updated support for regex match for find                         |
|         | Updated support for case-sensitive match for regex usage         |
+---------+------------------------------------------------------------------+

---

## remark.rst

# remark
--------

You can add remarks in operation as well as in configuration commands by specifying a hash sign (#) before the remark. When copying the configuration using external tools/scripts, the remarks will be copied as well, but only during the configuration session and while the remarks are visible on screen.

**Command syntax: #** remark sentence

**Command mode:** operational

**Note**

- The remark is not saved to the configuration file and is not visible in any show command.

**Example**
::

	dnRouter# # user comment
	dnRouter(cfg)# # user comment
	




---

## save.rst

save
----

**Minimum user role:** operator

You can save the running configuration of the main CLI to a file using the following command:

**Command syntax: save [file-name]**

**Command mode:** configuration

**Note**

- "factory-default" and "golden-config" are reserved names.

- NCC config located at: ``/config/``

The saved file has a predefined structure:

- config start

- version

- last commit user

**Parameter table**

+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------+
| Parameter | Description                                                                                                                                                                                                                       | Range             | Default |
+===========+===================================================================================================================================================================================================================================+===================+=========+
| file-name | The file will be saved in the configuration files folder. If the file name already exists, the save will overwrite it (a warning message will be displayed). The file is saved in text format. A suffix (.txt, .cfg) is optional. | 1..255 characters | \-      |
+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------+


**Example**
::

	dnRouter# configure
	dnRouter(cfg)#
	dnRouter(cfg)# save MySavedConfig.txt

	file content:
	# dnRouter config-start [04-Jun-2024 04:27:05 UTC]

	# VERSION DNOS [19.2.0.0], Copyright 2024 DRIVENETS LTD.
	# USER admin
	configuration..


.. **Help line:** save configuration to a file

**Command History**

+---------+------------------------------------+
| Release | Modification                       |
+=========+====================================+
| 5.1.0   | Command introduced                 |
+---------+------------------------------------+
| 6.0     | Changed to a configuration command |
+---------+------------------------------------+



---


---

# SECTION 3: REQUEST COMMANDS

Files from Request Commands folder:       60 files

## request commands overview.rst

Request Commands Overview
-------------------------
Request commands enable to make system-level requests. To enter a system level request, use one of the following command syntax:

::

	dnRouter# request system [argument]

	or

	dnRouter# request file-[operation]

**Command mode:** operation

where

request system - the command that you enter to request a system-level action

The following are the available system arguments:

+------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| Argument                                 | Description                                                                                       | Reference                                             |
+------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| restart                                  | Restarts the system                                                                               | request system restart                                |
+------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| restart process                          | Restarts the specified process                                                                    | request system process restart                        |
+------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| restart recovery                         | Restarts the system and enters recovery mode                                                      | request system restart recovery                       |
+------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| restart factory-default                  | Restarts the system and deletes the database. Applicable to recovery mode only.                   | request system restart factory-default                |
+------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| tech-support                             | Generates a tech-support file with logs, configuration, database files and system output commands | request system tech-support                           |
+------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| traffic-engineering pcep activate-server | Reconnects idle PCEs                                                                              | request mpls traffic-engineering pcep activate-server |
+------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| traffic-engineering pcep delegate peer   | Manually delegate all tunnels to a specific PCE                                                   | request mpls traffic-engineering pcep delegate peer   |
+------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| traffic-engineering pcep revoke          | Manually revoke tunnel delegation                                                                 | request mpls traffic-engineering pcep revoke          |
+------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------+

The following are the operations that you can perform on a file:

+-------------+----------------------------------------------------------+-----------------------+
| Operation   | Description                                              | Reference             |
+-------------+----------------------------------------------------------+-----------------------+
| upload      | Copy file from the DN cloud server to an external server | request file upload   |
+-------------+----------------------------------------------------------+-----------------------+
| download    | Copy file to the DN cloud server from an external server | request file download |
+-------------+----------------------------------------------------------+-----------------------+
| file-delete | Delete a file from the DN cloud server                   | request file delete   |
+-------------+----------------------------------------------------------+-----------------------+

The following paragraphs describe each system request.
---

## request fabric state init.rst

request fabric state init
-------------------------

**Minimum user role:** operator

Initiate fabric connectivity configuration on fabric element devices

**Command syntax: request fabric state init** { ncf [ncf-id] }

**Command mode:** operational

**Note:**

- Command only applicable when dynamic fabric connectivity state is enabled.

- Validation : User Yes/No question.

**Parameter table:**

+---------------------------+-----------------------------------------------+---------------+
| Parameter                 | Values                                        | Default value |
+===========================+===============================================+===============+
| ncf-id                    | integer                                       | \-            |
+---------------------------+-----------------------------------------------+---------------+

**Example**
::

	dnRouter# request fabric state init
	Are you sure fabric connectivity configuration should be initialized? (Yes/No) [No]?


**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 25.1    | Command introduced                  |
+---------+-------------------------------------+

---

## request file copy.rst

request file copy
--------------------

**Minimum user role:** admin

Copy the file from the local directory to the destination.

**Command syntax: request file copy** { ncc [ncc-id] } **[file-type] [source_file_absolute_path] [destination_folder]** | force

**Command mode:** operational

**Note:**

- Validation : User Yes/No question with the specified file name.

- Only `integrity-report-retrieves` is supported currently starting with v18.2.1.

- The destination directory for `integrity-report-retrieves` has a limit of maximum 10 files.

- File types locations:

 -  integrity-report-retrieves - /core/integrity_report_retrieves

- File types to copy from the NCCs:

 -  integrity-report-retrieves

**Parameter table:**

+---------------------------+-----------------------------------------------+---------------+
| Parameter                 | Values                                        | Default value |
+===========================+===============================================+===============+
| file-type                 | integrity-report-retrieves                    | \-            |
+---------------------------+-----------------------------------------------+---------------+
| ncc-id                    | 0-1                                           | \-            |
+---------------------------+-----------------------------------------------+---------------+
| container                 | cluster-engine / dnos-agent / host            | \-            |
|                           | / management-engine / ncc-conducto            |               |
|                           | / node-manager / policy-executor / redis      |               |
|                           | / redis_config / routing-engine               |               |
+---------------------------+-----------------------------------------------+---------------+
| source-file-absolute-path |                                               | \-            |
+---------------------------+-----------------------------------------------+---------------+
| destination-folder        | integrity_report_retrieves                    | \-            |
+---------------------------+-----------------------------------------------+---------------+
| force                     | \-                                            | disabled      |
+---------------------------+-----------------------------------------------+---------------+

**Example**
::

	dnRouter# request file copy integrity-report-retrieves /define_notif_net.sh
	File /define_notif_net.sh was copied successfully


	dnRouter# request file copy integrity-report-retrieves /define_notif_net.sh
	File /define_notif_net.sh already exists
	Do you want to overwrite it? (Yes/No) [No]?


**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 18.2.1  | Command introduced                  |
+---------+-------------------------------------+

---

## request file delete integrity-report.rst

request file delete integrity-report
-------------------------------------

**Minimum user role:** admin

**Command syntax: request file delete integrity-report**  **[file-name]**

**Description:** Delete the named integrity-report file.

**Example:**
::

	dnRouter# request file delete integrity-report integrity_report_dnRouter_20231019_045439.json.gz

	Warning: Are you sure you want to delete integrity_report_dnRouter_20231019_045439.json.gz? (yes/no) [no]? yes
	File integrity_report_dnRouter_20231019_045439.json.gz has been deleted successfully

**Command mode:** operational

**Note:**

- Validation : User Yes/no question with the specified file name.

**Help line:** Files from the integrity-report directory

**Parameter table:**

+-----------+------------------------------------------+---------------+
| Parameter | Values                                   | Default value |
+===========+==========================================+===============+
| file-name | Name of integrity-report file to delete. |               |
+-----------+------------------------------------------+---------------+

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 18.3    | Command introduced                  |
+---------+-------------------------------------+

---

## request file delete.rst

request file delete
--------------------

**Minimum user role:** admin

Delete the file from the local directory.

**Command syntax: request file delete** { ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] \| ncm [ncm-id]} **[file-type] [file-name]**

**Command mode:** operational

**Note:**

- Validation : User Yes/no question with the specified file name.

- User cannot delete the current in use log file (log.0).

- If no ncc-id/ncp-id/ncf-id/ncm-id was specified, the command relates to the active NCC.

- File types locations:

 -  config - /config/

 -  log - /var/log/dn/

 -  core - /core/

 -  tech-support - /techsupport/

 -  certificate -  /security/cert/

 -  key -  /security/key/

 -  event-policy - /event-manager/event-policy/scripts/

 -  periodic-policy - /event-manager/periodic-policy/scripts/

 -  generic-policy - /event-manager/generic-policy/scripts/

 -  packet-capture - /packet-capture/

 -  integrity-report-retrieves - /core/integrity_report_retrieves

- File types to delete from the NCCs:

 -  config

 -  log

 -  traces

 -  core

 -  tech-support

 -  security

 -  event-policy

 -  periodic-policy

 -  generic-policy

 -  packet-capture

 -  integrity-report-retrieves

- File types to delete from the NCPs/NCFs:

 -  log

 -  traces

 -  core

- File types to delete files on the NCMs:

 -  log

 -  config

 -  core

 -  tech-support

- For file type "packet-capture", support for the active NCC only.

**Parameter table:**

+-----------+-----------------------------------------------+---------------+
| Parameter | Values                                        | Default value |
+===========+===============================================+===============+
| file-type | log / traces / config / core / tech-support / |               |
|           | integrity-report-retrieves                    |               |
|           |                                               |               |
|           | security - supported in v11.1                 |               |
|           | / event-policy / periodic-policy              |               |
|           | / generic-policy / packet-capture             |               |
+-----------+-----------------------------------------------+---------------+
| file-name | string. Including sub-directory (/)           |               |
+-----------+-----------------------------------------------+---------------+
| ncc-id    | 0-1                                           |               |
+-----------+-----------------------------------------------+---------------+
| ncp-id    | 0-191                                         |               |
+-----------+-----------------------------------------------+---------------+
| ncf-id    | 0-12                                          |               |
+-----------+-----------------------------------------------+---------------+
| ncm       | a0, b0, a1, b1                                |               |
+-----------+-----------------------------------------------+---------------+

**Example**
::

	dnRouter# request file delete config MyConfig.txt
	Are you sure you want to delete MyConfig.txt (Yes/No) [No]?


	dnRouter# request file delete packet-capture BGP_Debug.1.pcap
	Are you sure you want to delete BGP_Debug.1.pcap (Yes/No) [No]?



**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1.0   | Command Introduced                                                 |
+---------+--------------------------------------------------------------------+
| 10.0    | Removed forwarding-id                                              |
+---------+--------------------------------------------------------------------+
| 11.0    | Added option to upload to a specific NCE                           |
+---------+--------------------------------------------------------------------+
| 11.2    | Added security certificates                                        |
+---------+--------------------------------------------------------------------+
| 13.1    | Added file types - Event-policy / Periodic-policy / Generic-policy |
+---------+--------------------------------------------------------------------+

---

## request file download.rst

request file download
----------------------

**Minimum user role:** operator

To copy file to the Network Cloud server from an external server:

**Command syntax: request file download** [user-name]@ **[url] [file-type] [file-name]** {protocol [protocol]} out-of-band

**Command mode:** operational

**Note**

- Each file type resides in a different location in the server:

	- Log - /var/log/dn/

	- Core - /core/

	- Tech-support - /techsupport/

	- Config - /config/

	- Rollback - /rollback/

	- Traces - /var/log/dn/traces

	- Certificate - /security/cert/

	- Key - /security/key/

	- Event-policy - /event-manager/event-policy/scripts/

	- Periodic-policy - /event-manager/periodic-policy/scripts/

	- Generic-policy - /event-manager/generic-policy/scripts/

- The default file transfer protocol used is SFTP. SCP can be used for backward compatibility but is not recommended due to security reasons.

**Parameter table**

+-----------+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+------------------+
| Parameter | Description                                                                                                                                    | Range                  | Default          |
+===========+================================================================================================================================================+========================+==================+
| user-name | Optional. The name of the user performing the operation. By default, this will be the current user.                                            | String                 | The current user |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+------------------+
| url       | The location and new file name. Specifying a filename that is different from the source file name, renames the file in the destination folder. | host://source-filename | \-               |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+------------------+
| file-type | The type of file to download                                                                                                                   | log                    | \-               |
|           |                                                                                                                                                | core                   |                  |
|           |                                                                                                                                                | tech-support           |                  |
|           |                                                                                                                                                | config                 |                  |
|           |                                                                                                                                                | certificate            |                  |
|           |                                                                                                                                                | key                    |                  |
|           |                                                                                                                                                | event-policy           |                  |
|           |                                                                                                                                                | periodic-policy        |                  |
|           |                                                                                                                                                | generic-policy         |                  |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+------------------+
| file-name | The name of the file being downloaded, including suffixes.                                                                                     | String                 | \-               |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+------------------+
| protocol  | The name of the file transfer protocol user for file download.                                                                                 | sftp                   | sftp             |
|           |                                                                                   				                             | scp                    |                  |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+------------------+

**Example**
::

	dnRouter# request file download user@192.168.1.1://myConfig myLocalConfig
	File loading ...100%

.. **Help line:** download file from remote location

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1.0   | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 6.0     | Syntax change                                                      |
+---------+--------------------------------------------------------------------+
| 11.0    | Added support for file types                                       |
+---------+--------------------------------------------------------------------+
| 11.2    | Added security certificate                                         |
+---------+--------------------------------------------------------------------+
| 11.6    | Added source-interface                                             |
+---------+--------------------------------------------------------------------+
| 13.1    | Added file types - Event-policy / Periodic-policy / Generic-policy |
+---------+--------------------------------------------------------------------+
| 25.2    | Support for SFTP                                                   |
+---------+--------------------------------------------------------------------+
| 25.2    | Command syntax change                                              |
+---------+--------------------------------------------------------------------+
---

## request file extract.rst

request file extract
--------------------

**Minimum user role:** operator

Extract file in local directory according to file type.

**Command syntax: request file extract** { ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] } **[file-type] [file-name]**

**Command mode:** operational

**Note:**

- Validation : User Yes/no question with the specified file name.

- According to the file type, if the requested file is password protected, the user should be prompted to provide a password.

- The certificate file type supports p12 and pfx file extensions only.

- PKCS#12 files are extracted into /security/cert and /security/key directories.

- If no ncc-id/ncp-id/ncf-id is specified, the command relates to the active NCC.

- PKCS#12 file location: /security/cert/

**Parameter table:**

+-----------+-----------------------------------------------+---------------+
| Parameter | Values                                        | Default value |
+===========+===============================================+===============+
| file-type | certificate                                   |               |
+-----------+-----------------------------------------------+---------------+
| file-name | string. Including sub-directory (/)           |               |
+-----------+-----------------------------------------------+---------------+
| ncc-id    | integer                                       |               |
+-----------+-----------------------------------------------+---------------+
| ncp-id    | integer                                       |               |
+-----------+-----------------------------------------------+---------------+
| ncf-id    | integer                                       |               |
+-----------+-----------------------------------------------+---------------+

**Example**
::

	dnRouter# request file extract certificate /security/cert/cert_key_bundle.p12
	Are you sure you want to extract cert_key_bundle.p12 (Yes/No) [No]? Yes
	Enter password: ********
	File cert_key_bundle.p12 extracted successfully

	dnRouter# request file extract certificate /security/cert/cert_key_bundle.p12
	Are you sure you want to extract cert_key_bundle.p12 (Yes/No) [No]? Yes
	Enter password: ********
	Error, unable to extract file. Please verify the provided file name and password

	dnRouter# request file extract certificate /security/cert/cert_key_bundle.zip
	Are you sure you want to extract cert_key_bundle.zip (Yes/No) [No]? Yes
	File type zip is not supported


**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 25.1    | Command Introduced                                                 |
+---------+--------------------------------------------------------------------+

---

## request file upload integrity-report.rst

request file upload integrity-report
-------------------------------------

**Minimum user role:** operator

**Command syntax: request file upload integrity-report**  **[file-name]** [user-name]@ **[destination-file-path] [url]**

**Description:** Upload the named integrity-report file.

**Example:**
::

	dnRouter# request file upload integrity-report integrity_report_dnRouter_20231019_045439.json.gz

**Command mode:** operational

**Help line:** Files from the integrity-report directory

**Parameter table:**

+-----------+----------------------------------------------------------------------+
| Parameter             | Values                                   | Default value |
+=======================+==========================================+===============+
| file-name             | Name of integrity-report file to upload. |               |
+-----------+------------------------------------------------------+---------------+
| User-name             | string                                   |               |
+-----------------------+------------------------------------------+---------------+
| destination-file-path | string                                   |               |
+-----------------------+------------------------------------------+---------------+
| url                   | user@host://destination-filename         |               |
+-----------------------+------------------------------------------+---------------+

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.2    | Command introduced                  |
+---------+-------------------------------------+

---

## request file upload rollback.rst

request file upload rollback
-------------------------------------

**Minimum user role:** operator

**Command syntax: request file upload rollback**  **[rollback-id]** [user-name]@ **[destination-file-path] [url]**

**Description:** Upload the file generated from rollback.

**Example:**
::

	dnRouter# request file upload rollback 5 user@192.168.1.1://rollback_5

**Command mode:** operational

**Parameter table:**

+-----------+----------------------------------------------------------------------+
| Parameter             | Values                                   | Default value |
+=======================+==========================================+===============+
| rollback-id           | Id of the rollback config                |               |
+-----------+------------------------------------------------------+---------------+
| User-name             | string                                   |               |
+-----------------------+------------------------------------------+---------------+
| destination-file-path | string                                   |               |
+-----------------------+------------------------------------------+---------------+
| url                   | user@host://destination-filename         |               |
+-----------------------+------------------------------------------+---------------+

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 11      | Command introduced                  |
+---------+-------------------------------------+

---

## request file upload.rst

request file upload
--------------------

**Minimum user role:** operator

Upload file to remote location

**Command syntax: request file upload** { ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] \| ncm [ncm-id]} **[file-type] [file-name]** [user-name]@ **[destination-file-path] [url]** { protocol [protocol] } out-of-band | source-interface [source-interface]

**Command mode:** operational

**Note:**

File upload should provide a progress-bar or percentage while uploading (default Linux scp should be fine)

Source-address [source-address] - set source ip-address for SSH packets. If the source-interface is set, the source IP address shall be derived from the set source interface. Otherwise, the source IP address shall be derived from the interface the packet was forwarded from (according to the default VRF routing table)

Each file type has a different location. The user cannot upload files from any location other than the predetermined ones (not even if he knows the exact path on the guest os).



The command relates to the active NCC if no ncc-id/ncp-id/ncf-id/ncm-id was specified.

File types locations:

-  config - /config/

-  log - /var/log/dn/

-  traces - /var/log/dn/traces

-  core - /core/

-  tech-support - /techsupport/

-  rollback - /rollback/

-  certificate -  /security/cert/

-  measured-boot - /security/measured-boot/

-  golden-config - /golden_config/

-  event-policy - /event-manager/event-policy/scripts/

-  periodic-policy - /event-manager/periodic-policy/scripts/

-  generic-policy - /event-manager/generic-policy/scripts/

-  packet-capture - /packet-capture/

file types to upload from NCCs:

-  config

-  log

-  traces

-  core

-  certificate

-  golden-config

-  tech-support - possible for active NCC only

-  rollback - possible for active NCC only

-  ssh-keys - possible for active NCC only

-  event-policy - possible for active NCC only

-  periodic-policy - possible for active NCC only

-  generic-policy - possible for active NCC only

-  packet-capture - possible for active NCC only

file types to upload from NCPs/NCFs:

-  log

-  traces

-  core

file types to upload files on NCMs:

-  log

-  config

-  core

-  tech-support

If the requested file does not exist, the following error message will be displayed "Requested file not found"

It is not possible to upload techsupport file from Standby NCC while connected to Active NCC

The default file transfer protocol used is SFTP. SCP can be used for backward compatibility but is not recommended due to security reasons.

**Parameter table:**

+-----------------------+--------------------------------------------------------+---------------+
| Parameter             | Values                                                 | Default value |
+=======================+========================================================+===============+
| file-type             | log / config / core / tech-support / rollback / traces |               |
|                       | / ssh-keys                                             |               |
|                       | / certificate / golden-config                          |               |
|                       | / event-policy / periodic-policy                       |               |
|                       | / generic-policy / packet-capture                      |               |
+-----------------------+--------------------------------------------------------+---------------+
| file-name             | string. Including sub-directory (/).                   |               |
+-----------------------+--------------------------------------------------------+---------------+
| destination-file-path | string                                                 |               |
+-----------------------+--------------------------------------------------------+---------------+
| url                   | user@host://destination-filename                       |               |
+-----------------------+--------------------------------------------------------+---------------+
| User-name             | string                                                 | Current user  |
+-----------------------+--------------------------------------------------------+---------------+
| ncc-id                | 0..1                                                   |               |
+-----------------------+--------------------------------------------------------+---------------+
| ncp-id                | 0..249                                                 |               |
+-----------------------+--------------------------------------------------------+---------------+
| ncf-id                | 0-611                                                  |               |
+-----------------------+--------------------------------------------------------+---------------+
| ncm-id                | a0, b0, a1, b1                                         |               |
+-----------------------+--------------------------------------------------------+---------------+
| source-interface      | Any interface in the global VRF with IPv4 address      |               |
|                       | except GRE tunnel interfaces                           |               |
+-----------------------+--------------------------------------------------------+---------------+
| protocol              | sftp, scp                                              | sftp          |
+-----------------------+--------------------------------------------------------+---------------+

**Example**
::

	dnRouter# request file upload tech-support MyTS-14-Jan-2017.tar.gz user@192.168.1.1://MyTS.tar.gz
	File loading ...100%

	dnRouter# request file upload log bgp.log user@192.168.1.1://bgp.log
	File loading ...100%

	dnRouter# request file upload forwarding-engine 1 log cheetah.log user@192.168.1.1://bgp.log
	File loading ...100%

	dnRouter# request file upload core bgpd-core.tar.gz user@192.168.1.1://bgpd-core.tar.gz
	File loading ...100%

	dnRouter# request file upload config MyConfig user@192.168.1.1://MyConfig protocol scp
	File loading ...100%

	dnRouter# request file upload rollback rollback_5 user@192.168.1.1://rollback_5
	File loading ...100%

	dnRouter# request file upload packet-capture BGP_Debug_.1.pcap
	File loading ...100%

	dnRouter# request file upload measured-boot ak.pub user@192.168.1.1://config/mb
	File loading ...100%

	dnRouter# request file upload measured-boot tpm_event_log user@192.168.1.1://config/mb
	File loading ...100%

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 5.1.0   | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
| 10.0	  | Removed forwarding-id                                              |
+---------+--------------------------------------------------------------------+
| 11.0    | Added option to upload to a specific NCE.                          |
+---------+--------------------------------------------------------------------+
| 11.2	  | Added security certificate                                         |
+---------+--------------------------------------------------------------------+
| 11.6	  | Added source-interface                                             |
+---------+--------------------------------------------------------------------+
| 13.1	  | Added file types - Event-policy / Periodic-policy / Generic-policy |
+---------+--------------------------------------------------------------------+
| 25.1    | Measured boot files support                                        |
+---------+--------------------------------------------------------------------+
| 25.2    | Support for SFTP                                                   |
+---------+--------------------------------------------------------------------+

---

## request mpls traffic-engineering pcep activate-server.rst

request mpls traffic-engineering pcep activate-server
-----------------------------------------------------

**Minimum user role:** operator

To reconnect idle peers (PCEs):

**Command syntax: request mpls traffic-engineering pcep activate-server** peer [ipv4-address]

**Command mode:** operational

**Parameter table**

+--------------+-------------------------------------------------------------+---------+
| Parameter    | Description                                                 | Range   |
+==============+=============================================================+=========+
| No parameter | The command will cause the system to reconnect to all PCEs. | \-      |
+--------------+-------------------------------------------------------------+---------+
| ipv4-address | The system will reconnect to a specific PCE                 | A.B.C.D |
+--------------+-------------------------------------------------------------+---------+

**Example**
::

	dnRouter# request mpls traffic-engineering pcep activate-server peer 1.1.1.1
	
	dnRouter# request mpls traffic-engineering pcep activate-server 
	

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

## request mpls traffic-engineering pcep delegate peer.rst

request mpls traffic-engineering pcep delegate peer
---------------------------------------------------

**Minimum user role:** operator

Manually delegate all tunnels to the stated peer. This command applies only for LSPs that are configured with delegation enabled.

This request command is non-persistent. When the PCEP session with the requested PCE server is closed, the delegation will return to the normal behavior, according to the configuration, and PCE best priority.

If the tunnel's state changes to down, the tunnel maintains the operational delegation to the requested PCE.

To manually delegate tunnels to a specific PCE peer:

**Command syntax: request mpls-traffic-engineering pcep delegate peer [ipv4-address]**

**Command mode:** operational

**Note**

- Changing the tunnel delegation configuration from enabled to disabled will also remove the delegation that was set due to the request command.

- The request delegation only affects existing tunnels. New tunnels that are configured with delegation will be delegated to the request PCE server and not according to the configuration.


**Parameter table**

+--------------+-------------------------------------------------------------+---------+
| Parameter    | Description                                                 | Range   |
+==============+=============================================================+=========+
| ipv4-address | The system will delegate all tunnels to the specified peer. | A.B.C.D |
+--------------+-------------------------------------------------------------+---------+

**Example**
::

	dnRouter# request mpls traffic-engineering pcep delegate peer 1.1.1.1


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

## request mpls traffic-engineering pcep revoke.rst

request mpls traffic-engineering pcep revoke
--------------------------------------------

**Minimum user role:** operator

To manually revoke delegation from tunnels:

**Command syntax: request mpls traffic-engineering pcep revoke** tunnel [tunnel-name]

**Command mode:** operational

**Note**

- This is a non-persistent change

- The "revoke" command for a tunnel that is not configured with delegation will stop the operational delegation.

**Parameter table**

+--------------+---------------------------------------------------------------+--------+
| Parameter    | Description                                                   | Range  |
+==============+===============================================================+========+
| No parameter | All tunnel delegations will be revoked.                       | \-     |
+--------------+---------------------------------------------------------------+--------+
| tunnel-name  | The delegation will be revoked from the specified tunnel only | String |
+--------------+---------------------------------------------------------------+--------+

**Example**
::

	dnRouter# request mpls-traffic-engineering pcep revoke 
	
	dnRouter# request mpls-traffic-engineering pcep revoke tunnel TUNNEL_A

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

## request retry-install flowspec-local-policy-rules.rst

request retry-install flowspec-local-policy-rules
--------------------------------------------------

**Minimum user role:** operator

To install any uninstalled Flowspec Local Policy rules:

**Command syntax: request retry-install flowspec-local-policy-rules** {[address-family]}

**Command mode:** operation

.. **Hierarchies**

**Note**

- When the address-family is not provided then the retry-install command will be applied to both the IPv4 and the IPv6 installed rules.

**Parameter table:**


+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+
|                   |                                                                                                                                                     |                     |             |
| Parameter         | Description                                                                                                                                         | Range               | Default     |
+===================+=====================================================================================================================================================+=====================+=============+
|                   |                                                                                                                                                     |                     |             |
| address-family    | Attempts to install any rules that were not yet installed for the specified address-family. When the address-family is not specified,               | IPv4                | both        |
|                   | the command will apply to both IPv4 and IPv6.                                                                                                       |                     |             |
|                   |                                                                                                                                                     | IPv6                |             |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+


**Example**
::

	dnRouter# request retry-install flowspec-local-policy-rules
	dnRouter# request retry-install flowspec-local-policy-rules ipv4
	dnRouter# request retry-install flowspec-local-policy-rules ipv6


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

## request rsvp auto-bandwidth adjust.rst

request rsvp auto-bandwidth adjust
----------------------------------

**Minimum user role:** operator

To manually perform auto-bandwidth adjustments:

**Command syntax: request rsvp auto-bandwidth adjust** tunnel [tunnel-name] bandwidth [bandwidth]

**Command mode:** operational

**Note**

- The general command (request rsvp auto-bandwidth adjust) performs adjustments to all tunnels with auto-bandwidth enabled. The adjustments are made based on the current adjustment interval and maximum average traffic rate. The action will reset the relevant adjust timer and adjust-threshold. See "rsvp auto-bandwidth for details".

**Parameter table**

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Parameter   | Description                                                                                                                                                                                   | Range                    |
+=============+===============================================================================================================================================================================================+==========================+
| tunnel-name | Manually performs auto-bandwidth adjustments to the specified tunnel only.                                                                                                                    | String 1..255 characters |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| bandwidth   | Manually perform auto-bandwidth adjustment with the specified bandwidth value as the average traffic rate. The specified bandwidth value is compared to the tunnel auto-bandwidth thresholds. | 0..42949672950 kbps      |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+

**Example**
::

	dnRouter# request rsvp auto-bandwidth adjust
	dnRouter# request rsvp auto-bandwidth adjust tunnel TUNNEL_A
	dnRouter# request rsvp auto-bandwidth adjust bandwidth 500000
	dnRouter# request rsvp auto-bandwidth adjust tunnel TUNNEL_A bandwidth 500000 

.. **Help line:**

**Command History**

+-------------+------------------------+
|             |                        |
| Release     | Modification           |
+=============+========================+
|             |                        |
| 11.0        | Command introduced     |
+-------------+------------------------+
| 18.2.5      | Bandwidth range update |
+-------------+------------------------+
---

## request rsvp protection-distribution.rst

request rsvp protection-distribution
------------------------------------

**Minimum user role:** operator

To run immediate protected bandwidth distribution:

**Command syntax: request rsvp protection-distribution**

**Command mode:** operational

**Note**

- Bypass tunnels that are protecting the same interface and have the same destination will balance which primary LSPs they protect, in order to balance the aggregated protected-bw between bypasses.


**Example**
::

	dnRouter# request rsvp protection-distribution


.. **Help line:** Run immidiate protected-bw balancing

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.2        | Command introduced    |
+-------------+-----------------------+
---

## request security certificate reload.rst

request security certificate reload
-----------------------------------

**Minimum user role:** operator

Reload of certificates and keys used by security services on the system.

When executing the command, already opened sessions might be disconnected.

**Command syntax: request security certificate reload service [service]**

**Command mode:** operational

**Parameter table**

+-----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| Parameter | Description                                                                                               | Range                                               | Default |
+===========+===========================================================================================================+=====================================================+=========+
| service   | The security service requested to reload certificate or key                                               | ssh, netconf, grpc                                  | \-      |
+-----------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+

**Example**
::

   dnRouter# request security certificate reload service ssh

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 25.1        | Command introduced    |
+-------------+-----------------------+
---

## request security generate self-signed-certificate.rst

request security generate self-signed-certificate
-------------------------------------------------

**Minimum user role:** operator

A self-signed certificate is a certificate that was signed by the same authority that created it and not by a CA (Certificate Authority). A self-signed certificate can be generated to encrypt the communication between DNOS and DNOR. Once the certificate is generated, it is uploaded to DNOR, and applied to the NCR. The generated certificate is stored in the system directory /security/cert/ and the generated private key file is stored in the directory /security/key/. To generate a self-signed server certificate:

**Command syntax: request security generate self-signed-server-certificate [name] dn [dn]** type [type] size [size]

**Command mode:** operational

**Parameter table**

+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| Parameter | Description                                                                                                                                                                                                                     | Range                                               | Default |
+===========+=================================================================================================================================================================================================================================+=====================================================+=========+
| name      | Name of the certificate.                                                                                                                                                                                                        | \-                                                  | \-      |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| type      | An algorithm used for message authentication.                                                                                                                                                                                   | RSA, ECDSA                                          | RSA     |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| size      | The bit length used to encrypt the session. The higher the bit length the greater the encryption.                                                                                                                               | 1024, 2048, 4096                                    | 2048    |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| dn        | DN (Distinguished Names) include information used to identify the certificate owner. Distinguished Names are separated by comma (,). When using values with a space, enclose the value in double quotes (e.g., "San Francisco") | DN (Distinguished Names) may include the following: | \-      |
|           |                                                                                                                                                                                                                                 | CN - Common Name                                    |         |
|           |                                                                                                                                                                                                                                 | OU - Organizational Unit name                       |         |
|           |                                                                                                                                                                                                                                 | O - Organization name                               |         |
|           |                                                                                                                                                                                                                                 | S - State (2 letters code)                          |         |
|           |                                                                                                                                                                                                                                 | C - Country                                         |         |
|           |                                                                                                                                                                                                                                 | L - City                                            |         |
|           |                                                                                                                                                                                                                                 | MAIL - e-mail address                               |         |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+

**Example**
::

   dnRouter# request security generate self-signed-server-certificate myCert dn CN=hostname,OU=Support,O=DRIVENETS,ST=CA,C=US,L=San Francisco,MAIL=john.smith@drivenets.com
   
   Generate TLS key myCert.key
   Generate Self-Signed Certificate myCert.crt
   
   -----BEGIN CERTIFICATE-----
   MIIC9jCCAd6gAwIBAgIJAPONTEWmmGnVMA0GCSqGSIb3DQEBCwUAMBAxDjAMBgNV
   BAMMBXlvdGFtMB4XDTE5MDkyMjIwMzgwNVoXDTI0MDkyMDIwMzgwNVowEDEOMAwG
   A1UEAwwFeW90YW0wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC5avqh
   57s8Afi6SJTKdjfy1Wax8YcXsXdGqCZffloHcZlDvU7Yqrm8nhP/OIRfikfWqYeT
   w2/HaIaL64/wjKA1mhp+gtomn/l9xE15d6iTtoAiPkhhUC/P4zfPyPd7MVGLvctE
   vz+K2w1rbPgiYjjv8aQeEa4THPm9SEgjt4ojU84JYANgu08Mp+reFtSwGtRmq55K
   f5q/5FZY/Md0H2FOoKsufBtbjxhUlgItH3MxGENo0h6UAI2IbWyI1LoM9dSAwfmt
   nSSTgOL894tncTruZan/RGm9vPEpp1bsnwiOCzpoS463FxIu4hkexnH0sBi+bw+1
   cgvhH0EqttlzUMLxAgMBAAGjUzBRMB0GA1UdDgQWBBT+eVAzyTd5vogTgT6idlvT
   moTpQjAfBgNVHSMEGDAWgBT+eVAzyTd5vogTgT6idlvTmoTpQjAPBgNVHRMBAf8E
   BTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQC156dU8tLUlSjCd4b5oo8Lu6Znudto
   T5M2bwYBHPsYn7GvjEuUgBw6UDVIvasKvlhZfdlIufutpZq6R11x62qA1rldJqMq
   W+E3RE9vmKYZ4lPSV+Gh7CTUxBTEcErzKiU9T4EpiNV7v1iLp1QyIQ9X1+xJ4rhG
   3KBkX3i+PJsSzXrce6bNwXy6a/Clo7ZnGKZ/eRRWo8FjNvW89J5KePVN70Svcpl2
   nSHNpq+mJaN/RTrtyBts15QzdMQPr53z6HwUhnKhBgq38n2EqVS0S9rMCRGdvNql
   NzJzctYyP6AwTwGW/WhaZ+bl+UKD5g+o7Z5CGWupsw0WxhntuW0i0ttp
   -----END CERTIFICATE-----

.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.2        | Command introduced    |
+-------------+-----------------------+
---

## request segment-routing mpls policy admin-state disable.rst

request segment-routing mpls policy admin-state enable
------------------------------------------------------

**Minimum user role:** operator


To disable the admin-state of SR-TE policy:


**Command syntax: request segment-routing mpls policy [policy-name] admin-state disable**

**Command mode:** operator

**Note:**

- This action does not affect the configuration and it is not persistent.

**Parameter table:**

+-------------+---------------------------------------------------------+
| Parameter   | Description                                             |
+=============+=========================================================+
| policy-name | Enable admin-state for the specified policy.            |
+-------------+---------------------------------------------------------+


**Example:**
::

	dnRouter# request segment-routing mpls policy Auto_c_0_dest_5.5.5.5 admin-state disable


.. **Help line:** Disable the admin-state of SR-TE policy


**Command History**

+-----------+-----------------------+
| Release   | Modification          |
+===========+=======================+
| 18.2      | Command introduced    |
+-----------+-----------------------+

---

## request segment-routing mpls policy admin-state enable.rst

request segment-routing mpls policy admin-state enable
------------------------------------------------------

**Minimum user role:** operator


To enable the admin-state of SR-TE policy:


**Command syntax: request segment-routing mpls policy [policy-name] admin-state enable**

**Command mode:** operator

**Note:**

- This action does not affect the configuration and it is not persistent.

**Parameter table:**

+-------------+---------------------------------------------------------+
| Parameter   | Description                                             |
+=============+=========================================================+
| policy-name | Enable admin-state for the specified policy.            |
+-------------+---------------------------------------------------------+


**Example:**
::

	dnRouter# request segment-routing mpls policy Auto_c_0_dest_5.5.5.5 admin-state enable


.. **Help line:** Enable the admin-state of SR-TE policy


**Command History**

+-----------+-----------------------+
| Release   | Modification          |
+===========+=======================+
| 18.2      | Command introduced    |
+-----------+-----------------------+

---

## request segment-routing mpls reoptimize.rst

request segment-routing mpls reoptimize
---------------------------------------

**Minimum user role:** operator

Paths may become invalid in time due to topology changes. When a policy has multiple path options and a better priority path becomes invalid, the system will use the next preferred priority path. The policy will continue using the lower priority path even if the higher priority path is available again. To fix this, you can globally set a policy reoptimization interval that will cause the system to instruct all segment-routing policies that are not on the best path to attempt to use a better priority path (see "segment-routing mpls policy-reoptimization").

To manually invoke segment-routing policy reoptimization:

**Command syntax: request segment-routing mpls reoptimize {all | policy [name]}**

**Command mode:** operational

**Note**

- The action will not reset the periodic reoptimization timer

**Parameter table**

+-------------+---------------------------------------------------------+
| Parameter   | Description                                             |
+=============+=========================================================+
| all         | Perform the optimization action on all policies         |
+-------------+---------------------------------------------------------+
| policy-name | Perform the optimization action on the specified policy |
+-------------+---------------------------------------------------------+

**Example**
::

	dnRouter# request segment-routing mpls reoptimize all
	dnRouter# request segment-routing mpls reoptimize policy SR_POLICY_A

.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 15.0        | Command introduced    |
+-------------+-----------------------+
---

## request segment-routing mpls switch-to-path.rst

request segment-routing mpls switch-to-path
-------------------------------------------

**Minimum user role:** operator

Invoke path validation for path with requested priority of requested SR-TE policy.
In case path is found to be valid, install path as active, regardless of active path prioty and if it has lock

In case path found as invalid (due to no routing solution or bfd depended and bfd timeout) request is revoke and forgotten


To invoke SR-TE policy candidate path switch:


**Command syntax: request segment-routing mpls switch-to-path policy [policy-name] path-priority [priority]**

**Command mode:** operator

**Note:**

- This action does not affect the configuration and it is not persistent.
- Next policy reoptimization may result in replacing the requested path with new active path
- In case the requested path is already installed backup path, switching it to become active will also trigger new path selection for the backup path
- Once requested path is installed as active, lock logic will apply for it, if such was configured to path




**Parameter table:**

+---------------+---------------------------------------------------------+
| Parameter     | Description                                             |
+===============+=========================================================+
| policy-name   | Select SR-TE policy to switch active path               |
+---------------+---------------------------------------------------------+
| path-priority | the path priority value for which switching is desired  |
+---------------+---------------------------------------------------------+


**Example:**
::

	dnRouter# request segment-routing mpls switch-to-path policy MY_SR_TE_POLICY path-priority 3

.. **Help line:** Switch policy active path to requested SR-TE candidate path


**Command History**

+-----------+-----------------------+
| Release   | Modification          |
+===========+=======================+
| 18.3      | Command introduced    |
+-----------+-----------------------+

---

## request segment-routing pcep activate-server.rst

request segment-routing pcep activate-server
--------------------------------------------

**Minimum user role:** operator

To reconnect idle Segement-routing PCEs peers:

**Command syntax: request segment-routing pcep activate-server** peer [ipv4-address]

**Command mode:** operational

**Parameter table**

+--------------+-------------------------------------------------------------+---------+
| Parameter    | Description                                                 | Range   |
+==============+=============================================================+=========+
| No parameter | This will cause the system to reconnect to all PCEs.        | \-      |
+--------------+-------------------------------------------------------------+---------+
| ipv4-address | The system will reconnect to a specific PCE                 | A.B.C.D |
+--------------+-------------------------------------------------------------+---------+

**Example**
::

	dnRouter# request segment-routing pcep activate-server peer 1.1.1.1

	dnRouter# request segment-routing pcep activate-server


.. **Help line:**

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## request segment-routing pcep delegate peer.rst

request segment-routing pcep delegate peer
------------------------------------------

**Minimum user role:** operator

The command allows you to manually delegate all sr-te policies to the stated PCE peer.
This applies for policies that are not configured with delegation enabled as well.
The request is non-persistent. When the PCEP session with the requested PCE server is closed, the delegation will return to the normal behavior, according to the configuration.

If the policy's state changes to down, the policy maintains the operational delegation to the requested PCE.

To manually delegate policies to a specific PCE peer:

**Command syntax: request segment-routing pcep delegate peer [ipv4-address]**

**Command mode:** operational

**Note**

- Changing the policy delegation configuration from enabled to disabled will also remove the delegation that was set due to the request command.

- The request delegation affects all policies. New policies that are configured with delegation will be delegated to the request PCE server and not according to the configuration.


**Parameter table**

+--------------+-------------------------------------------------------------+---------+
| Parameter    | Description                                                 | Range   |
+==============+=============================================================+=========+
| ipv4-address | The system will delegate all tunnels to the specified peer  | A.B.C.D |
+--------------+-------------------------------------------------------------+---------+

**Example**
::

	dnRouter# request segment-routing pcep delegate peer 1.1.1.1


.. **Help line:**

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## request segment-routing pcep pce-initiated remove.rst

request segment-routing pcep pce-initiated remove
-------------------------------------------------

**Minimum user role:** operator

The command allows you to manually invoke removal of PCE initiated SR-TE policies from local device (PCC). 
PCC will reflect removal with PCRpt message and will clear any local information related to the removed SR-TE policies

To manually remove PCE initiated SR-TE policies:

**Command syntax: request segment-routing pcep pce-initiated remove** {name [policy-name] | stale} 

**Command mode:** operational

**Note**

- Command only applies to PCE initiated SR-TE policies. I.e, if provided name is not of PCE initiated SR-TE policy, no modification will be expected to that policy

- There is no prevation that after policy is removed PCE will re-initiate the policy on the PCC


**Parameter table**

+--------------+-------------------------------------------------------------+---------+
| Parameter    | Description                                                 | Range   |
+==============+=============================================================+=========+
| name         | remove specific SR-TE policy by name                        | string  |
+--------------+-------------------------------------------------------------+---------+
| stale        | remove all PCE initiated SR-TE policies that are in stale   | string  |
|              | state (not claimed by PCE)                                  |         |
+--------------+-------------------------------------------------------------+---------+

**Example**
::

	dnRouter#  request segment-routing pcep pce-initiated remove

    dnRouter#  request segment-routing pcep pce-initiated remove name INITIATED_POLICY_1

    dnRouter#  request segment-routing pcep pce-initiated remove stale


.. **Help line:**

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.2    | Command introduced |
+---------+--------------------+

---

## request system alarms clear alarm all.rst

request system alarms clear alarm all
-------------------------------------

**Minimum user role:** operator

**Command syntax: request system alarms clear alarm all**

**Description:** To clear all clearable alarms from the active alarms list and moves them to the alarm history:

**Command mode:** operator

**Example**
::

	dnRouter# request system alarms clear alarm all

.. **Help line:**


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 18.2        | Command introduced    |
+-------------+-----------------------+
---

## request system alarms clear alarm.rst

request system alarms clear-alarm
---------------------------------

**Minimum user role:** operator

**Command syntax: request system alarms clear alarm [alarm-operator-id]**

**Description:** Clears clearable alarms from the active alarms and moves them to the alarm history.

**Command mode:** operator

**Note:**

-  alarm-operator-id a unique id per alarm, presented under show system alarms details.

**Parameter table:**

+----------------------+------------------------------------------+----------------------------------------------+---------------+
| Parameter            | Description                              |  Values                                      | Default value |
+======================+==========================================+==============================================+===============+
| alarm-operator-id    | The alarm id                             |  Random generated number                     | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+


**Example**
::

	dnRouter# request system alarms clear alarm 1313

	dnRouter# request system alarms clear alarm 1312
    ERROR: alarm 1312 is not manual clearable
	dnRouter# request system alarms clear alarm 9999
    ERROR: Unknown id: 9999


.. **Help line:**


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 18.2        | Command introduced    |
+-------------+-----------------------+
---

## request system alarms history purge.rst

request system alarms history purge
-----------------------------------

**Minimum user role:** operator


To delete the alarms history:


**Command syntax: request system alarms history purge** before-time [datetime]

**Command mode:** operator

**Note:**

- If the before-time is provided, the alarm history will clear all the generated alarm records before the specified time.

**Parameter table:**

+---------------+-------------------------------------------------------------------------------------------+------------------------+
|               |                                                                                           |                        |
| Parameter     | Description                                                                               | Range                  |
+===============+===========================================================================================+========================+
| datetime      | The alarm history will clear all the generated alarm records before the specified time.   | yyyy-mm-ddThh:mm:ss    |
+---------------+-------------------------------------------------------------------------------------------+------------------------+

**Example**
::

	dnRouter# request system alarms history purge before-time 2022-11-13T17:59:59
    Done.
	dnRouter#
	dnRouter# request system alarms history purge
    Done.
	dnRouter#


.. **Help line:** deleting alarms history till the specified time or all in case not specified.


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
| 18.0        | Command introduced    |
+-------------+-----------------------+

---

## request system container restart.rst

request system container restart 
---------------------------------

**Minimum user role:** admin

To restart the containers of cluster components:

**Command syntax: request system container restart** {ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id]} **[container-name]**

**Command mode:** operational

**Note**

- You will be prompted to confirm the restart.

- If you do not specify a node, the container(s) on the active NCC will be restarted.

..
	**Internal Note**

	- Yes/no validation should exist for container restart operations

	- Warning should be displayed for container start.

	- datapath reset should shut down physical interfaces during the reset operation on the relevant NCP

	- Datapath reset on NCF should also result in shutting down the physical interfaces on all NCP when resetting NCF in a small cluster.

	- In bigger clusters when resetting the NCF datapath container shutting down the physical interfaces on NCP should take place if the NCF resets reduces the number of fabric interfaces below preconfigured minimum threshold.

**Parameter table**

+-------------------+---------------------------------------------------------------+-------------------------------------------------------------+
|                   |                                                               |                                                             |
| Parameter         | Description                                                   | Range                                                       |
+===================+===============================================================+=============================================================+
|                   |                                                               |                                                             |
| ncc-id            | Restarts a container in the specified NCC                     | 0..1                                                        |
+-------------------+---------------------------------------------------------------+-------------------------------------------------------------+
|                   |                                                               |                                                             |
| ncp-id            | Restarts a container in the specified NCP                     | 0..max number of NCP per cluster type -1                    |
+-------------------+---------------------------------------------------------------+-------------------------------------------------------------+
|                   |                                                               |                                                             |
| ncf-id            | Restarts a container in the specified NCF                     | 0..max number of NCF per cluster type -1                    |
+-------------------+---------------------------------------------------------------+-------------------------------------------------------------+
|                   |                                                               |                                                             |
| container-name    | Specify the name of the container in the NCE to   restart.    | A container in the NCE. See "show   system" for details.    |
+-------------------+---------------------------------------------------------------+-------------------------------------------------------------+

**Example**
::

	dnRouter# request system container restart ncc 0 routing-engine 
	Warning: Are you sure you want to perform a container restart? (Yes/No) [No]? 
	
	dnRouter# request system container restart ncp 2 forwarding-engine 
	Warning: Are you sure you want to perform a container restart? (Yes/No) [No]? 

.. **Help line:** request system operations

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+
---

## request system delete.rst

request system delete
-----------------------

**Minimum user role:** admin

Deletes the DNOS router system.

- Stops DNOS services.

- Deletes DNOS database, keys, certificates, logs.


**Command syntax: request system delete**

**Command mode:** operational

**Example**
::

	dnRouter# request system delete
	DNOS router will be stopped, its database, keys and logs will be deleted.
	Do you want to continue? (Yes/No) [No]?

	Press Ctrl C to exit progress show, deletion will run in background.
	Started system deletion
	Stopped DNOS on NCP 0...
	Deleted DNOS files on NCP 0...
	Stopped DNOS on NCP 1...
	Deleted DNOS files on NCP 1...
	Stopped DNOS on NCF1 0...
	Deleted DNOS files on NCF 0...
	...
	Stopped DNOS on NCC 1...
	Stopping DNOS on NCC 0...



**Note:**

-  Yes/no validation should exist for the operation.

.. **Help line:** Delete DNOS router.

.. **Parameter table:**

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 16.1        | Command introduced    |
+-------------+-----------------------+

---

## request system event-manager restart policy-type.rst

request system event-manager restart policy-type
------------------------------------------------

**Minimum user role:** admin

Use this command to reset statistics counters for the specified policy type and stop its running policies. Any policies within the specified type with an admin-state "enabled" are started again and their operational state changes to active. The policies that have an admin-state "disabled" will remain in the operational-state "inactive". You can also reset a specific policy under a specific policy type.

**Command syntax: request system event-manager restart policy-type [policy-type]** policy-name [policy-name]

**Command mode:** operational

**Parameter table**

+----------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
|                |                                                     |                                                                                                               |
| Parameter      | Description                                         | Range                                                                                                         |
+================+=====================================================+===============================================================================================================+
|                |                                                     |                                                                                                               |
| Policy-type    | Specify to   restart all policies of the same type. | Policy types:                                                                                                 |
|                |                                                     |                                                                                                               |
|                |                                                     | event-policy - policy that will be executed upon   matching trigger of registered system event.               |
|                |                                                     |                                                                                                               |
|                |                                                     | periodic-policy - a recurrent policy according to   the scheduled configuration, with limited execution time. |
|                |                                                     |                                                                                                               |
|                |                                                     | generic-policy - policy that will be executed   only once and unlimited in execution time.                    |
+----------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
|                |                                                     |                                                                                                               |
| Policy-name    | Specify to   restart a specific policy.             | String                                                                                                        |
+----------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------+

**Example**

To restart all policies of a specific type:
::

    dnRouter#
    dnRouter# request system event-manager restart policy-type periodic-policy
    dnRouter#

To restart a specific policy, such as the generic-policy named get-cnt:
::

    dnRouter# request system event-manager restart policy-type generic-policy policy-name test
    dnRouter#

.. **Help line:** this action will restart all policies according to policy type, and delete policies operational-data.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.1        | Command introduced    |
+-------------+-----------------------+
---

## request system event-manager restart.rst

request system event-manager restart
------------------------------------

**Minimum user role:** admin

Use this command to reset statistics counters for all policy types and stop running policies. Any policies with an admin-state "enabled" are restarted and their operational state changes to active. Any policies that have a "disabled" admin-state will remain in the operational-state "inactive".

To restart a specific policy type, use the policy-type command:

**Command syntax: request system event-manager restart** policy-type [policy-type]

**Command mode:** operational

**Parameter table**

+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
|                |                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                               |
| Parameter      | Description                                                                                                                                                                                                                                                                                                                                                                          | Range                                                                                                         |
+================+======================================================================================================================================================================================================================================================================================================================================================================================+===============================================================================================================+
|                |                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                               |
| Policy-type    | Specify to   restart all policies of the same type.                                                                                                                                                                                                                                                                                                                                  | Policy types:                                                                                                 |
|                |                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                               |
|                | If you don’t   specify a policy-type, all policies will be restarted. Statistics counters will   be zeroed, existing policies executions will stop. Any policy with   admin-state "enabled" will be re-lunched and its operational state   will be changed to “active”. The policies of current type that are in   admin-state disable will stay in operational-state "inactive".    | event-policy - policy that will be executed upon   matching trigger of registered system event.               |
|                |                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                               |
|                |                                                                                                                                                                                                                                                                                                                                                                                      | periodic-policy - a recurrent policy according to   the scheduled configuration, with limited execution time. |
|                |                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                               |
|                |                                                                                                                                                                                                                                                                                                                                                                                      | generic-policy - policy that will be executed   only once and unlimited in execution time.                    |
+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+

**Example**

To restart all policy types:
::

    dnRouter#
    dnRouter# request system event-manager restart
    dnRouter#

To restart a specific policy type, such as the periodic-policy
::

    dnRouter# request system event-manager restart policy-type periodic-policy
    dnRouter#

.. **Help line:** Restart all policies according to policy type, and delete policies operational-data

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.1        | Command introduced    |
+-------------+-----------------------+
---

## request system generate golden-config.rst

request system generate golden-config
-------------------------------------

**Minimum user role:** admin

Create a golden configuration file based on current system configuration.

**Command syntax: request system generate golden-config**

**Command mode:** operational

**Note**
	- The golden-config file allows the user to revert the system to the saved configuration.
	- Existing golden-config file will be overwritten by this command.

..
	**Internal Note**
	- Yes/no validation should be added
	- Command should fail with proper indication in CLI on all non NCP6 Ufispace Q2C+ (Emux) platforms

**Example**
::

	dnRouter# request system generate golden-config
	Warning: Existing golden-config file will be overwritten. Are you sure you want to proceed? (Yes/No) [No]?

	dnRouter# request system generate golden-config
	Command not supported on platform

.. **Help line:** Retry software/firmware installation on a failed node.

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 19.1        | Command introduced    |
+-------------+-----------------------+

---

## request system install abort.rst

request system install abort
----------------------------

**Minimum user role:** admin

Command to abort the initiated install flow and cancel ongoing system upgrades.


**Command syntax: request system install abort**

**Command mode:** operational

**Example**
::

	dnRouter# request system install abort
	Warning: Are you sure you want to abort the install? (Yes/No) [No]? Yes

	dnRouter# request system install abort
	Warning: Are you sure you want to abort the install? (Yes/No) [No]? Yes
	Error: installation abort is unavailable or cannot be performed at this stage!


**Note:**

- Install abort is supported in specific install flows and according to the system's current execution phase.

- Install abort is supported only on NMW (No maintenance-window) upgrades.

.. **Help line:** Abort software installation flow execution.

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 25.2        | Command introduced    |
+-------------+-----------------------+

---

## request system install retry.rst

request system install retry
----------------------------

**Minimum user role:** admin

Retries software/firmware installation on a node where a previous installation attempt failed.

**Command syntax: request system install retry [nmw] { ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] \| ncm [ncm-id] }**

**Command mode:** operational

**Example**
::

	dnRouter# request system install retry ncp 3
	Error: installation retry is unavailable!

	dnRouter# request system install retry ncp 4
	The following software or firmware will be installed:
	   Firmware: version 4.6-ab for HW platform S9700-23DJ, revision 2
	   BaseOS 2.304
	   DNOS 16.0.1

	dnRouter# request system install retry ncp 5
	The following software or firmware will be installed:
	   DNOS 16.0.1

	dnRouter# request system install retry ncp 5
	Warning: Retry flow execution may require node reset. Are you sure you want to proceed? (Yes/No) [No]? Yes
	The following software or firmware will be installed:
	   DNOS 25.0.1

**Note:**

- Retry is available for nodes in one of the following states: dnos-deployment(failed) / nos-upgrade(failed) / baseos-upgrade(failed) / firmware-upgrade(failed) / onie-upgrade(failed) / gi-upgrade(failed) / baseos-revert(failed).

- Retry could be performed when the system is down for maintenance, or when supported, retry install without maintenance down could be attempted using the nmw flag.

- When the retry command is executed following a no maintenance-window upgrade, user should be warned and prompted to approve operation since node may get reset and updated using the normal GI-based upgrade flow.

.. **Help line:** Retry software/firmware installation on a failed node.

**Parameter table:**

+----------------+--------------------------------+------------------------------------+---------------+
| Parameter      | Description                    | Range                              | Default value |
+================+================================+====================================+===============+
| ncc-id         | The id of the NCC              | 0-1                                | \-            |
+----------------+--------------------------------+------------------------------------+---------------+
| ncp-id         | The id of the NCP              | 0..(Cluster type max NCP number-1) | \-            |
+----------------+--------------------------------+------------------------------------+---------------+
| ncf-id         | The id of the NCF              | 0..(Cluster type max NCF number-1) | \-            |
+----------------+--------------------------------+------------------------------------+---------------+
| ncm-id         | The id of the NCM              | A0, B0, A1, B1                     | \-            |
+----------------+--------------------------------+------------------------------------+---------------+
| nmw            | No maintenance-window upgrade  | nmw                                | \-            |
|                | type flag                      |                                    |               |
+----------------+--------------------------------+------------------------------------+---------------+

**Command History**

+-------------+-------------------------+
| Release     | Modification            |
+=============+=========================+
| 16.1        | Command introduced      |
+-------------+-------------------------+
| 25.2        | Updated for NMW support |
+-------------+-------------------------+

---

## request system integrity-report.rst

request system integrity-report
--------------------------------

**Minimum user role:** admin

Generates a system integrity report. The integrity report contains metadata about files in the system that should not be modified as part of normal operation. The metadata includes: path, type, permission, ownership, sha256 hash of the file content and last modified time.

This command runs in the background.


**Command syntax: request system integrity report**

**Command mode:** operational

**Note**

- Start a background job to collect the integrity report.
- Immediately after using this command the prompt returns to enable the user to continue using the CLI while the report is being generated.


**Example**
::

	dnRouter# request system integrity-report


.. **Help line:** Generate system integrity-report file

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
| 19.1        | Command introduced    |
+-------------+-----------------------+

---

## request system logging generate-event.rst

request system logging generate-event 
-------------------------------------

**Minimum user role:** operator

You can request the system to generate system events, for example for testing purposes. The system will generate a single instance of the requested events. If events are bound to SNMP traps, the system will also send SNMP traps according to the system configuration. However, system configuration, such as SNMP trap suppression or logging events suppression, have priority over the event generation. Therefore, if an event or trap is suppressed according to the configuration, it won't be sent even if it was generated successfully using the request command.

You can view the required event-attributes by typing "?" after the event-name. When specifying multiple event-attributes, the help command ("?") only shows the remaining available attributes.

To set the system to generate system events:


**Command syntax: request system logging generate-event group [event-group] event [event-name]** event-attribute [event-attribute]

**Command mode:** operational

**Note**

- You must specified all the required attributes defined in the system event for the event to be generated. There are no default values per generated event.

* System configurations such as snmp trap suppression or logging events suppression have priority over the event generation. This means that if an event or trap is suppressed by configuration, it won't be sent **even if it was generated successfully by this command**.


..
	**Internal Note**

	- System shall generate auto-complete attributes (for the user to fill) according the output in "show system logging system-events group".

	- System shall validate the types of each attribute (i.e uint32 cannot get string type or negative integer), if validation fails, user will get an error message.

	- System shall **not** perform logical context validation (i.e user can send linkUp event with Admin Status down parameter)


**Parameter table**

+--------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
|                    |                                                                                                                                    |                                                         |
| Parameter          | Description                                                                                                                        | Range                                                   |
+====================+====================================================================================================================================+=========================================================+
|                    |                                                                                                                                    |                                                         |
| event-group        | The event group                                                                                                                    | See the SNMP Traps and   System Logs Reference Guide    |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
|                    |                                                                                                                                    |                                                         |
| event-name         | The name of the event that you want to generate                                                                                    | Any event in the specified event-group                  |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
|                    |                                                                                                                                    |                                                         |
| event-attribute    | You must specify all the required attributes   defined in the system event. There are no default values for generated   events.    | \-                                                      |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+

**Example**
::

	dnRouter# request system logging generate-event group interfaces event if_link_state_change_up ?

	if_admin_status          An integer value for if_admin_status
	if_index                 An integer value for if_index
	if_name                  A string value for if_name
	if_oper_status           An integer value for if_oper_status
	new_state                A string value for new_state

	dnRouter# request system logging generate-event group interfaces event if_link_state_change_up new_state up if_name bundle-1.800 if_index 123 ?

	if_admin_status          An integer value for if_admin_status
	if_oper_status           An integer value for if_oper_status

	dnRouter# request system logging generate-event group interfaces event if_link_state_change_up new_state up if_name bundle-1.800 if_index 123 if_admin_status 1 if_oper_status 1

	system event if_link_state_change_up was generated successfully
	snmp trap linkUp was generated successfully

	dnRouter# request system logging generate-event group interfaces event if_link_state_change_up new_state up if_name spoofed-interface if_index 123 if_admin_status 1 if_oper_status 1

	system event if_link_state_change_up was generated successfully
	snmp trap linkUp was generated successfully

	dnRouter# request system logging generate-event group interfaces event if_link_state_change_up new_state up 

	Error: Incomplete command

	dnRouter# request system logging generate-event group interfaces event if_link_state_change_up new_state up if_name spoofed-interface if_index abc if_admin_status 1 if_oper_status 1

	Error: Invalid argument for if_index

	dnRouter# request system logging generate-event group system event ncp_state_change ?

	ncp_id             An integer value for ncp_id
	new_state          A string value for new_state
	old_state          A string value for old_state

	dnRouter# request system logging generate-event group system event ncp_state_change old_state down new_state up ncp_id 3000

	system event ncp_state_change was generated successfully
	snmp trap entConfigChange was generated successfully

	dnRouter# request system logging generate-event group system event ncp_state_change old_state down new_state A ncp_id 3000

	system event ncp_state_change was generated successfully
	snmp trap entConfigChange was generated successfully

	dnRouter# request system logging generate-event group system event system_cold_start

	system event system_cold_start was generated successfully
	snmp trap coldStart was generated successfully

	dnRouter# request system logging generate-event group isis event isis_neighbor_adjacency_up ?

	if_index                    An integer value for if_index
	if_name                     A string value for if_name
	instance                    A string value for instance
	level                       An enumeration for level
	link_state_pdu_id           A binary value for link_state_pdu_id
	neighbor_system_id          A string value for neighbor_system_id
	state                       An enumeration for state

	dnRouter# request system logging generate-event group isis event isis_neighbor_adjacency_up instance foo neighbor_system_id foo if_name foo if_index 123 level 1 link_state_pdu_id 0 state 3

	system event isis_neighbor_adjacency_up was generated successfully
	snmp trap isisAdjacencyChange was generated successfully

.. **Help line:** request system to generate system events

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 12.0        | Command introduced    |
+-------------+-----------------------+
---

## request system ncc repository sync.rst

request system ncc repository sync
----------------------------------------

**Minimum user role:** admin

When the NCCs' repository sync fails, you can retry the sync operation by executing this command.

- If a sync operation is already in progress, the system will display a message indicating that the operation is in progress.

- If the repository is already in sync, the system will display a message indicating that the repository is already in sync.

- If the deployment is a standalone NCC, the system will display a message indicating that the operation is not supported.

- If the root NCC is not stable, the system will display a message indicating that the operation is not applicable.

- If the root NCC's repository is not stable, the system will display a message indicating that the operation is not applicable.

To trigger a repository between the active NCC and the standby NCC:

**Command syntax: request system ncc repository sync**

**Command mode:** operational

..**Note**


**Example**
::

	dnRouter# request system ncc repository sync
	Repository sync started
	dnRouter#

	dnRouter# request system ncc repository sync
	Error: Repository sync is already in progress
	dnRouter#

.. **Help line:** retry repository sync operation

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 19.3    | Command introduced                  |
+---------+-------------------------------------+

---

## request system ncc switchover.rst

request system ncc switchover
-----------------------------

**Minimum user role:** admin

When performing a switchover to the standby NCC, you will be prompted to confirm the switchover request. After the request is confirmed, the system will check if the standby NCC is ready for switchover:

- If the NCC is ready for switchover, the switchover will take place and a confirmation message will display. This will terminate all active SSH sessions. After the switchover process finishes, you will need to start a new CLI session.

- If the NCC is not ready for switchover, a failure message is displayed.


To trigger a switchover between the active NCC and the standby NCC:

**Command syntax: request system ncc switchover**

**Command mode:** operational

**Note**

- The switchover operation will terminate all SSH sessions. User will have to reconnect CLI session after the switchover has completed.


**Example**
::

	dnRouter# request system ncc switchover
	Warning: Are you sure you want to perform NCC switchover (Yes/No) [No]? Y
	Standby NCC is not ready for switchover, operation was aborted
	dnRouter#
	
	dnRouter# request system ncc switchover
	Warning: Are you sure you want to perform NCC switchover (Yes/No) [No]? Yes
	Switchover operation was initiated, all CLI sessions are terminated.

.. **Help line:** switchover from active NCC to standby one

**Command History**

+-------------+--------------------------+
|             |                          |
| Release     | Modification             |
+=============+==========================+
|             |                          |
| 6.0         | Command introduced       |
+-------------+--------------------------+
|             |                          |
| 9.0         | Command not supported    |
+-------------+--------------------------+
|             |                          |
| 11.0        | Command reintroduced     |
+-------------+--------------------------+
---

## request system process restart.rst

request system process restart 
-------------------------------

**Minimum user role:** admin

You can restart a process in the NCP or NCC. Some processes cannot be restarted specifically; in this case, running the command will cause the entire container to restart.

Datapath restart will cause the physical interfaces on the NCP to shut down during the restart operation.

To restart the operation of a specific process:


**Command syntax: request system process restart** {ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id]} **[container-name]** [process-name]

**Command mode:** operational

**Note**

- You will be prompted to confirm the restart.

- If you do not specify a node, the process(es) on the active NCC will be restarted.

..
	**Internal Note**

	- Yes/no validation should exist for process restart operations

	- Warning should be displayed for process start. For non-restartable processes, the operation will reset the entire container after process restart.

	- datapath reset should shut down physical interfaces during the reset operation on the relevant NCP


**Parameter table**

+-------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
|                   |                                                                                                                          |                                             |
| Parameter         | Description                                                                                                              | Range                                       |
+===================+==========================================================================================================================+=============================================+
|                   |                                                                                                                          |                                             |
| ncp-id            | The unique identifier of the NCP                                                                                         | 0..max number of NCP per cluster type -1    |
+-------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
|                   |                                                                                                                          |                                             |
| ncc-id            | The unique identifier of the NCC                                                                                         | 0..1                                        |
+-------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
|                   |                                                                                                                          |                                             |
| ncf-id            | The unique identifier of the NCF                                                                                         | 0..max number of NCF per cluster type -1    |
+-------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
|                   |                                                                                                                          |                                             |
| container-name    | The container in which the process runs.                                                                                 | See "show system"                           |
+-------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
|                   |                                                                                                                          |                                             |
| process-name      | The name of the process to restart. If you do not   specify a process, all process within the container will restart.    | See "show system"                           |
+-------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+

**Example**
::

	dnRouter# request system process restart ncp 0 forwarding-engine
	Warning: Are you sure you want to perform a process restart? (Yes/No) [No]? 
	
	
	dnRouter# request system process restart ncp 0 forwarding-engine sshd
	Warning: Are you sure you want to perform a process restart? (Yes/No) [No]? 
	
	dnRouter# request system process restart ncc 0 management-engine transaction_manager
	Warning: Are you sure you want to perform a process restart? this process restart will cause container restart (Yes/No) [No]? 
	

.. **Help line:** request system operations

**Command History**

+-------------+-------------------------------------------------+
|             |                                                 |
| Release     | Modification                                    |
+=============+=================================================+
|             |                                                 |
| 6.0         | Command introduced                              |
+-------------+-------------------------------------------------+
|             |                                                 |
| 9.0         | Command not supported                           |
+-------------+-------------------------------------------------+
|             |                                                 |
| 10.0        | Command reintroduced                            |
+-------------+-------------------------------------------------+
|             |                                                 |
| 11.0        | Added option to restart a process in the NCF    |
+-------------+-------------------------------------------------+
---

## request system process stop.rst

request system process stop
---------------------------

**Minimum user role:** admin

You can stop a running process in an NCC, NCP, or NCF. The system does not consider a process that has stopped as a failure event and so does not try to recover the process automatically. To start a process, run the command "request system process restart".

To stop the operation of a specific process:


**Command syntax: request system process stop {ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id]} [container-name] [process-name]**

**Command mode:** operational

**Note**

- You will be prompted to confirm the process you want to stop.

- Stopping a process is the responsiblity of the user. The system may not function correctly when processes are stopped.

..
	**Internal Note**
	- Yes/no validation should exist for process restart operations

**Parameter table**

+-------------------+-----------------------------------------------------------------------+---------------------------------------------+----------------+
|                   |                                                                       |                                             |                |
| Parameter         | Description                                                           | Range                                       | Default        |
+===================+=======================================================================+=============================================+================+
|                   |                                                                       |                                             |                |
| ncp-id            | The unique identifier of the NCP.                                     | 0..max number of NCP per cluster type -1    | /-             |
+-------------------+-----------------------------------------------------------------------+---------------------------------------------+----------------+
|                   |                                                                       |                                             |                |
| ncc-id            | The unique identifier of the NCC.                                     | 0..1                                        | /-             |
+-------------------+-----------------------------------------------------------------------+---------------------------------------------+----------------+
|                   |                                                                       |                                             |                |
| ncf-id            | The unique identifier of the NCF.                                     | 0..max number of NCF per cluster type -1    | /-             |
+-------------------+-----------------------------------------------------------------------+---------------------------------------------+----------------+
|                   |                                                                       |                                             |                |
| container-name    | The container in which the process runs.                              | See "show system"                           | /-             |
+-------------------+-----------------------------------------------------------------------+---------------------------------------------+----------------+
|                   |                                                                       |                                             |                |
| process-name      | The name of the process to stop.                                      | See "show system"                           | /-             |
+-------------------+-----------------------------------------------------------------------+---------------------------------------------+----------------+

**Example**
::

	dnRouter# request system process stop ncc 0 routing-engine routing:pimd
	Warning: Are you sure you want to perform a process stop? (Yes/No) [No]?


.. **Help line:** request system operations

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## request system restart - supported in v11 5.rst

request system restart - supported in v11.5
-------------------------------------------

**Minimum user role:** admin

request system restart operation

-  By default, preform cold restart, meaning power reset for all elements in the cluster.

-  specify node type and id to restart specific node in cluster

-  warm - restart DNOS software (applicative containers) only.

**Command syntax: request system process stop {ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id]} [container-name] [process-name]**
		
**Command mode:** operational

**Note:**

-  Yes/no validation should exist for system restart operation.

-  Request system restart warm performs applicative containers restart across all the system.

   -  Applicative containers are Management-engine, Routing-engine, Forwarding-engine and selector.

-  In order to cold restart the standby NCC, there must be connectivity for standby NCC

-  For "request system restart warm" NCM will not reset. Cannot choose warm restart for node type of ncm

*Parameter table:**

+-----------+----------------+---------------+
| Parameter | Values         | Default value |
+===========+================+===============+
| ncc-id    | 0-1            |               |
+-----------+----------------+---------------+
| ncp       | 0-249          |               |
+-----------+----------------+---------------+
| ncf       | 0-611          |               |
+-----------+----------------+---------------+
| ncm-id    | a0, b0, a1, b1 |               |
+-----------+----------------+---------------+


**Example**
::

	dnRouter# request system restart
	Warning: Are you sure you want to perform a system restart? (Yes/No) [No]? 
	
	dnRouter# request system restart warm
	Warning: Are you sure you want to perform a system restart? (Yes/No) [No]? 
	
	dnRouter# request system restart ncc 1
	Warning: Are you sure you want to perform a system restart? (Yes/No) [No]? 
	
	dnRouter# request system restart ncp 3 warm
	Warning: Are you sure you want to perform a system restart? (Yes/No) [No]? 
	
	dnRouter# request system restart ncm a1
	Warning: Are you sure you want to perform a system restart? (Yes/No) [No]? 
	
		

---

## request system restart recovery.rst

request system restart recovery 
--------------------------------

**Minimum user role:** techsupport

Use this command to enter recovery mode. 

In recovery mode, you can perform the following commands:

- "request system restart"

- "request system restart factory-default"

- "request system restart rollback"

**Command syntax: request system restart** recovery

**Command mode:** operational

**Note**

- Exiting recovery mode requires system restart.


..
	**Internal Note**

	- Yes/no validation should exist for system restart operations

**Example**
::

	dnRouter# request system restart recovery
	Warning: Are you sure you want to switch to recovery mode? Operation will cause system restart (Yes/No) [No]? 
 
.. **Help line:** request system to enter recovery mode

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 6.0         | Command introduced    |
+-------------+-----------------------+
---

## request system restart.rst

request system restart
----------------------

**Minimum user role:** admin

Use this command to do a system wide restart, or a node restart. When requesting a system-wide restart, the network interfaces on the NCPs are shut down so no further traffic can be sent or received. With the interfaces down, external devices stop forwarding traffic to the device. Then, the cluster nodes are restarted one by one.

When the system is in recovery mode, the system restart command is used to exit recovery mode. This will restart all the system containers (management engine, forwarding engine, routing engine, and selector). You will be prompted to confirm the action. If you are sure you want to restart the system, type ‘yes’.

To restart the system, use the following command. 

**Command syntax: request system restart** {ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] \| ncm [ncm-id]} warm force

**Command mode:** operational

**Note**

- To perform a cold restart to a standby NCC, connectivity to it must be available.

..
	**Internal Note**

	-  Yes/no validation should exist for system restart operation.

	-  Request system restart warm performs applicative containers restart across all the system.

	   -  Applicative containers are Management-engine, Routing-engine, Forwarding-engine and selector.

	-  For "request system restart warm" NCM will not reset. Cannot choose warm restart for node type of ncm

**Parameter table**

+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+
|               |                                                                                                                                                                                                                                                                  |                                 |
| Parameter     | Description                                                                                                                                                                                                                                                      | Comment                         |
+===============+==================================================================================================================================================================================================================================================================+=================================+
|               |                                                                                                                                                                                                                                                                  |                                 |
| ncc-id        | Restart only the specified NCC                                                                                                                                                                                                                                   | 0..1                            |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+
|               |                                                                                                                                                                                                                                                                  |                                 |
| ncp-id        | Restart only the specified NCP                                                                                                                                                                                                                                   | 0..47                           |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+
|               |                                                                                                                                                                                                                                                                  |                                 |
| ncf-id        | Restart only the specified NCF                                                                                                                                                                                                                                   | 0..12                           |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+
|               |                                                                                                                                                                                                                                                                  |                                 |
| ncm-id        | Restart only the specified NCM                                                                                                                                                                                                                                   | a0, b0, a1, b1                  |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+
|               |                                                                                                                                                                                                                                                                  |                                 |
| warm          | By default, a cold restart is done, meaning that   the power is reset for all cluster elements. By specifying warm, only the   DNOS software is restarted (the applicative containers: management-engine,   routing-engine, forwarding-engine, and selector).    | Not applicable to NCM           |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+
|               |                                                                                                                                                                                                                                                                  |                                 |
| force         | Remotely enforce a cold restart using IPMI   connectivity.                                                                                                                                                                                                       | Not applicable to NCM or NCC    |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+

**Example**
::

	dnRouter# request system restart
	Warning: Are you sure you want to perform a system restart? (Yes/No) [No]? 
	
	dnRouter# request system restart warm
	Warning: Are you sure you want to perform a system restart? (Yes/No) [No]? 
	
	dnRouter# request system restart ncc 1
	Warning: Are you sure you want to perform a system restart? (Yes/No) [No]? 
	
	dnRouter# request system restart ncp 3 warm
	Warning: Are you sure you want to perform a system restart? (Yes/No) [No]? 
	
	dnRouter# request system restart ncm a1
	Warning: Are you sure you want to perform a system restart? (Yes/No) [No]? 

	dnRouter# request system restart ncp 0 force
	Warning: Are you sure you want to perform a system restart? (Yes/No) [No]? 
	

.. **Help line:**

**Command History**

+-------------+---------------------------------------------------------------------+
|             |                                                                     |
| Release     | Modification                                                        |
+=============+=====================================================================+
|             |                                                                     |
| 5.1.0       | Command introduced                                                  |
+-------------+---------------------------------------------------------------------+
|             |                                                                     |
| 11.0        | Added support for all cluster elements (NCC, NCP,   NCF and NCM     |
+-------------+---------------------------------------------------------------------+
|             |                                                                     |
| 11.4        | Added ability to warm restart the DNOS software.                    |
+-------------+---------------------------------------------------------------------+
|             |                                                                     |
| 15.0        | Added the ability to force a cold restart to the   DNOS software    |
+-------------+---------------------------------------------------------------------+
---

## request system revert-stack install.rst

request system revert-stack install
------------------------------------

**Minimum user role:** admin

Reverts the system software to versions in the revert stack.

**Command syntax: request system revert-stack install [nmw]**

**Command mode:** operational

**Parameter table:**

+----------------------+------------------------------------------+----------------------------------------------+---------------+
| Parameter            | Description                              |  Values                                      | Default value |
+======================+==========================================+==============================================+===============+
| nmw                  | No maintenance-window upgrade type flag  | nmw                                          | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+

**Example**
::

	dnRouter# request system revert-stack install
	The system will revert to the following software:
	   NCM NOS 12.1, affected nodes: NCM A0, A1
	Warning: Do you want to continue? (Yes/No) [No]?

	WARNING! NO NCM REDUNDANCY - NCM B0 IS NOT IN UP STATE!
	WARNING! SYSTEM BACKPLANE CONTROL CONNECTIVITY ISSUE!
		NCM-A0: NCF 1,2, NCP 2 connection state is not "ok"!
	Warning: Do you want to continue? (Yes/No) [No]?

	dnRouter# request system revert-stack install
	The following software or firmware will be installed:
	   OS Packages 1.100
	Warning: Installing the downloaded packages requires performing a system restart.
	         Do you want to continue? (Yes/No) [No]?

**Note:**

- nmw (No Maintenance-Window Upgrade) perform pre-check for no maintenance-window upgrade type.

- Firmware and ONIE are not reverted.

- Not supported when the system is updating or reverting any software on any node.

- Shows progress until node reboot or until user presses Ctrl+C which stops the show. The process continues in the background.

- Yes/no validation should exist for the operation.

- Double confirmation should be requested if NCMs in "up" state are not redundant, or if backplane control connectivity of enabled NCP/F node is not "ok".


.. **Help line:** Revert system software to versions in the revert stack.

.. **Parameter table:**

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 16.1        | Command introduced    |
+-------------+-----------------------+
| 25.2        | Add nmw flag          |
+-------------+-----------------------+

---

## request system revert-stack pre-check.rst

request system revert-stack pre-check
-------------------------------------

**Minimum user role:** admin

Pre-checks revert stack packages compatibility before upgrade/deployment.

**Command syntax: request system revert-stack pre-check [nmw]**

**Command mode:** operational

**Note:**

- nmw (No Maintenance-Window Upgrade) perform pre-check for no maintenance-window upgrade type.

**Example**
::

    dnRouter# request system revert-stack pre-check

    Status: OK

    dnRouter# request system revert-stack pre-check

    Status: Error
    Reason: NCM A0 FW wrong revision

    dnRouter# request system revert-stack pre-check nmw

    Status: OK



    dnRouter# request system revert-stack pre-check
    Warning: Installing the downloaded packages requires performing a system restart.

    Status: OK

.. **Help line:** Validates revert stack packages compatibility.

**Parameter table:**

+----------------------+------------------------------------------+----------------------------------------------+---------------+
| Parameter            | Description                              |  Values                                      | Default value |
+======================+==========================================+==============================================+===============+
| Status               | The status of the revert-stack pre-check | OK, Error                                    | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+
| Reason               | The reason of the error                  | String - in case of status Error             | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+
| nmw                  | No maintenance-window upgrade type flag  | nmw                                          | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 16.1        | Command introduced    |
+-------------+-----------------------+
| 25.2        | Add nmw flag          |
+-------------+-----------------------+

---

## request system stack abort.rst

request system stack abort
--------------------------

**Minimum user role:** admin

- Request to abort an ongoing upgrade flow

- If possible, pending on the state of the operation, the upgrade operation will be canceled as result of this request.

- Command fails if the abort is not possible due to the upgrade flow state in which the command has been issued.

**Command syntax: request system stack abort**

**Command mode:** operational

**Example**
::

	dnRouter# request system stack abort
	Warning: Are you sure upgrade should be aborted? (Yes/No) [No]? No

	dnRouter# request system stack abort
	Warning: Are you sure upgrade should be aborted? (Yes/No) [No]? Yes
	Upgrade aborted successfully

	dnRouter# request system stack abort
	Warning: Are you sure upgrade should be aborted? (Yes/No) [No]? Yes
	Error, failed to abort upgrade operation

**Note:**

-  Yes/no validation should exist for the operation.

.. **Help line:** Attempt to abort software upgrade flow.

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 25.2        | Command introduced    |
+-------------+-----------------------+

---

## request system target-stack clear.rst

request system target-stack clear
----------------------------------

**Minimum user role:** admin

Removes all the software from system target-stack for any node type in system

- Not supported when the system is upgrading or reverting.

- Not supported when a package is being added or removed.

**Command syntax: request system target-stack clear**

**Command mode:** operational

**Example**
::

	dnRouter# request system target-stack clean
	Warning: Are you sure you want to remove all the software from the target stack? (Yes/No) [No]?

	# Removed all software from the target stack
    dnRouter#

**Note:**

-  Yes/no validation should exist for the operation.

.. **Help line:** Remove all software from the system target-stack.

.. **Parameter table:**

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 16.1        | Command introduced    |
+-------------+-----------------------+

---

## request system target-stack install.rst

request system target-stack install
------------------------------------

**Minimum user role:** admin

Updates software/firmware on system nodes to versions in the target stack.

- On each node updates software relevant to the node:
	- DNOS and BaseOS on NCC/NCP/NCF nodes
	- NCM-NOS on NCM nodes
	- GI image on NCC/NCP/NCF nodes
	- ONIE and firmware on the nodes of the HW model and revision specified in the package metadata, or by a user.

**Note:**

- nmw (No Maintenance-Window Upgrade) perform pre-check for no maintenance-window upgrade type.

- Not supported if the update might violate any version dependency, e.g. if the target DNOS cannot run on the target BaseOS, or if there is no target BaseOS and target GI image cannot run on current BaseOS.

- Not supported when the system is updating or reverting any software on any node.

- Not supported when the system is changing target stack or syncing it to any node.

- Shows progress. Pressing Ctrl+C stops the show and returns prompt; the process continues in background.

**Command syntax: request system target-stack install [nmw]**

**Command mode:** operational

**Parameter table:**

+----------------------+------------------------------------------+----------------------------------------------+---------------+
| Parameter            | Description                              |  Values                                      | Default value |
+======================+==========================================+==============================================+===============+
| nmw                  | No maintenance-window upgrade type flag  | nmw                                          | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+

**Example**
::

	dnRouter# request system target-stack install
	The following software or firmware will be installed:
	   Firmware:
	   	HW platform: S9700-53DX, revision 1, version 4.5, affected nodes: NCP 1,5,10-40
	   	HW platform: S9700-23DJ, revision 2, version 4.6-ab, affected nodes: NCP 0,2-4,6-9,41-47
	   NCM NOS:
	   	Version 12.1, affected nodes: NCM A0, A1
	Do you want to continue? (Yes/No) [No]?

	WARNING! NO NCM REDUNDANCY - NCM B0 IS NOT IN UP STATE!
	WARNING! SYSTEM BACKPLANE CONTROL CONNECTIVITY ISSUE!
		NCM-A0: NCF 1, NCP 2,3 connection state is not "ok"!
	Warning: Do you want to continue? (Yes/No) [No]?


	dnRouter# request system target-stack install
	The following software or firmware will be installed:
	   OS Packages 1.200
	Warning: Installing the downloaded packages requires performing a system restart.
	         Do you want to continue? (Yes/No) [No]?

.. **Help line:** Install software target stack on the system.

.. **Parameter table:**

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 16.1        | Command introduced    |
+-------------+-----------------------+
| 25.2        | Add nmw flag          |
+-------------+-----------------------+
---

## request system target-stack load.rst

request system target-stack load
--------------------------------

**Minimum user role:** admin

Loads packages via HTTP(s) GET from remote location and adds it to the target stack.

- A package can contain software of one of the following types, or it can be a bundle of few such packages:
	- DNOS
	- BaseOS
	- NCM NOS
	- Firmware for specific HW models and revisions
	- ONIE image for specific HW model and revision
	- GI image
	- OS packages

- After a package is untared, inspect package metadata to understand which software it contains.

- For firmware and ONIE packages a user may set the intended HW model and revision instead of those specified in the package metadata. Revision may be "default", meaning all the revisions of this HW model for which no package is set explicitly. For other package types HW model/revision parameters are ignored.

- Command fails if a bundle package contains a few packages of the same type.

- Each package replaces the previous package of the same type in the target stack, if exists.

- Verifies Drivenets signature on a package.

- If a firmware package was delivered directly by the HW vendor without the a Drivenets signature, a user may provide the MD5 hash for verification; otherwise the package won't be verified. It's highly recommended to provide a hash received from the HW vendor to ensure package integrity and authenticity. Installing an unverified package may compromise system security. Corrupted firmware may cause HW malfunction.

- In a cluster, the active NCC replicates a target stack to the standby NCC.

- In a cluster, the active NCC syncs a target stack to all the connected nodes - copies DNOS, BaseOS, GI images to all the NCP/NCF nodes, NCM NOS to all the NCMs, firmware and ONIE to all the nodes of the HW model/revision set for the package.

- Not supported when the system is upgrading or reverting.

- Not supported when the system is changing target stack.

**Command syntax: request system target-stack load {[url] \| inband [url]}** hw-model [hw-model] \| hw-revision [hw-revision]

**Command mode:** operational

**Example**
::
dnRouter# request system target-stack load http://172.16.100.12/packages/drivenets_stratax_1.1.0.tar

Package http://172.16.100.12/packages/drivenets_stratax_1.1.0.tar will be downloaded and added to target stack.
Warning: Do you want to continue? (Yes/No) [No]?
started target-stack load NCC 0, task ID = 99

dnRouter# request system target-stack load http://172.16.100.12/packages/ufi-wbx-fw-17-0 hardware-model S9700-53DX hardware-revision 4

Package http://172.16.100.12/packages/ufi-wbx-fw-17-0 will be downloaded and added to target stack for HW model S9700-53DX, revision 4.
Warning: Do you want to continue? (Yes/No) [No]?
started target-stack load NCC 0, task ID = 100

dnRouter# request system target-stack load inband http://172.16.100.12/packages/drivenets_stratax_1.1.0.tar

Package http://172.16.100.12/packages/drivenets_stratax_1.1.0.tar will be downloaded and added to target stack.
Warning: Do you want to continue? (Yes/No) [No]?
started target-stack load NCC 0, task ID = 99

dnRouter# request system target-stack load http://172.16.100.12/packages/drivenets_baseos_packages_1.200.tar

Package http://172.16.100.12/packages/drivenets_baseos_packages_1.200.tar will be downloaded and added to target stack.
Warning: Do you want to continue? (Yes/No) [No]?
started target-stack load NCC 0, task ID = 99

**Note:**

-  User input must start with "http://" to invoke HTTP GET
	- If user entered url without expected "http://",  display error message: "ERROR: Unknown word."
	- If http fail to connect, display error message: "ERROR: The connection has timed out"

-  Yes/no validation should exist for the operation.

-  If a node connects, system syncs target stack to the node (only software which is relevant to the node type and HW).

-  In case inband is used, the target stack will be downloaded over the in-band management VRF as were set by the "system in-band-management dnor-server-vrf" command
    - in case "system in-band-management dnor-server-vrf" is configured with non-default IB management VRF, the source-interface that will be used is according to the interface that is configured under "network-services vrf instance in-band-management source-interface" of the same non-default IB management VRF

.. **Help line:** Load software/firmware to target stack.

**Parameter table:**

+----------------------+-----------------------------------------------+-------------+---------------+
| Parameter            | Description                                   | Ranges      | Default value |
+======================+===============================================+=============================+
| url                  | Package URL (will start with http:// prefix)  |             | \-            |
+----------------------+-----------------------------------------------+-------------+---------------+
| hw-model             | Hardware model for ONIE/firmware package      |             | \-            |
+----------------------+-----------------------------------------------+-------------+---------------+
| hw-revision          | Hardware revision for ONIE/firmware package   |             |      default  |
+----------------------+-----------------------------------------------+-------------+---------------+
| inband               | Indicates if the download will be done via IB |             |               |
+----------------------+-----------------------------------------------+-------------+---------------+

**Command History**

+----------+-------------------------+
| Release  | Modification            |
+==========+=========================+
| 16.1     | Command introduced      |
+----------+-------------------------+
| 25.1     | Remove file load option |
+----------+-------------------------+
| 25.2     | Command syntax change   |
+----------+-------------------------+

---

## request system target-stack pre-check.rst

request system target-stack pre-check
-------------------------------------

**Minimum user role:** admin

Pre-checks target stack packages compatibility before upgrade/deployment.

**Command syntax: request system target-stack pre-check [nmw]**

**Command mode:** operational

**Note:**

-  nmw (No Maintenance-Window Upgrade) perform pre-check for no maintenance-window upgrade type.

**Example**
::
dnRouter# request system target-stack pre-check

Status: OK


dnRouter# request system target-stack pre-check

Status: Error
Reason: NCM A0 FW wrong revision

dnRouter# request system target-stack pre-check nmw

Status: OK

dnRouter# request system target-stack pre-check
Warning: Installing the downloaded packages requires performing a system restart.

Status: OK

.. **Help line:** Validates target stack packages compatibility.

**Parameter table:**

+----------------------+------------------------------------------+----------------------------------------------+---------------+
| Parameter            | Description                              |  Values                                      | Default value |
+======================+==========================================+==============================================+===============+
| Status               | The status of the target-stack pre-check | OK, Error                                    | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+
| Reason               | The reason of the error                  | String - in case of status Error             | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+
| nmw                  | No maintenance-window upgrade type flag  | nmw                                          | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 16.1        | Command introduced    |
+-------------+-----------------------+
| 25.2        | Add nmw flag          |
+-------------+-----------------------+

---

## request system target-stack remove.rst

request system target-stack remove
----------------------------------

**Minimum user role:** admin

Removes packages from the target stack.

- Deletes DNOS, BaseOS, NCM NOS, GI or OS update package from the target stack for all node types in a cluster

- For ONIE and firmware package, deletes target stack entries with the specified HW model/revision. Deletes the package from matching HW nodes.
 	- If HW model not specified, deletes all existing ONIE/firmware packages in target stack
	- If HW revision not specified, deletes all matching HW model ONIE/firmware packages existing in target stack

- Not supported when the system is upgrading or reverting.

- Not supported when the system is changing target stack.

- Asynchronous, shows progress.

**Command syntax: request system target-stack remove dnos** {hardware-model [hw-model] | hardware-model [hw-model] hardware-revision [hw-revision]}
**Command syntax: request system target-stack remove baseos** {hardware-model [hw-model] | hardware-model [hw-model] hardware-revision [hw-revision]}
**Command syntax: request system target-stack remove ncm-nos** {hardware-model [hw-model] | hardware-model [hw-model] hardware-revision [hw-revision]}
**Command syntax: request system target-stack remove gi** {hardware-model [hw-model] | hardware-model [hw-model] hardware-revision [hw-revision]}
**Command syntax: request system target-stack remove onie** {hardware-model [hw-model] | hardware-model [hw-model] hardware-revision [hw-revision]}
**Command syntax: request system target-stack remove firmware** {hardware-model [hw-model] | hardware-model [hw-model] hardware-revision [hw-revision]}
**Command syntax: request system target-stack remove os-packages** {hardware-model [hw-model] | hardware-model [hw-model] hardware-revision [hw-revision]} }

**Command mode:** operational

**Example**
::

    dnRouter# request system target-stack remove ncm-nos
	NCM-NOS 12.1 package will be removed from target stack.
	Warning: Do you want to continue? (Yes/No) [No]?
	Removed NCM NOS package from target stack

	dnRouter# request system target-stack remove firmware hardware-model S9700-53DX hardware-revision 4
	Firmware for HW model S9700-53DX revision 4 will be removed from target stack
	Warning: Do you want to continue? (Yes/No) [No]?
	Removed firmware package for S9700-53DX revision 4 from target stack


**Note:**

-  Yes/no validation should exist for the operation.

.. **Help line:** Remove package from target stack.


**Parameter table:**

+----------------------+------------------------------------------+----------------------------------------------+---------------+
| Parameter            | Description                              |  Values                                      | Default value |
+======================+==========================================+==============================================+===============+
| hw-model             | The Hardware model                       |                                              | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+
| hw-revision          | The Hardware revision                    |                                              | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 16.1        | Command introduced    |
+-------------+-----------------------+
| 25.2        | Command syntax change |
+-------------+-----------------------+
---

## request system target-stack reset.rst

request system target-stack reset
----------------------------------

**Minimum user role:** admin

Align all the software from system target-stack with the software in system current-stack for any node type in system.

- Not supported when a package is being added or removed.

**Command syntax: request system target-stack reset**

**Command mode:** operational

**Example**
::

	dnRouter# request system target-stack reset
	Warning: Are you sure you want to reset all the software from the target stack? (Yes/No) [No]?

	# Reset all software from the target stack to match the current stack
    dnRouter#

**Note:**

-  Yes/no validation should exist for the operation.

.. **Help line:** Reset all software from the system target-stack.

.. **Parameter table:**

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 18.2.1        | Command introduced  |
+-------------+-----------------------+
---

## request system tech-support.rst

request system tech-support
---------------------------

**Minimum user role:** operator

You can generate a file with all the logs, configuration, database files and system output commands that you can save for later use (for example, when opening a customer support case).

After running the command, you will regain full CLI control while the system is generating the tech-support file in the background.

The system can handle only one request to generate a tech-support file at a time. If the system is already creating a tech-support file while you enter another request, an error message will be displayed.

By default, the tech-support file is generated with information from the last 24 hours for rotated logs (end with .1, .2, date, etc.) and always includes the latest version of the main logs (logs that are currently being written to) regardless if they were modified in the past 24 hours.

The Tech-support files are generated on the active NCC node in the /techsupport/ folder. Only one file is stored at a time. When you generate a tech-support file, any previous file is deleted to make room for the new file.

After generating the tech-support file, you can upload it to a location you can access (see "request file upload").

To generate the tech-support file:


**Command syntax: request system tech-support [file-name]** component [component] {ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] \| ncm [ncm-id]} inclusive after [after-time] before [before-time] password force include {[info-type], [info-type], ...}

**Command mode:** operational

..
	**Internal Note**

	- The tech-support files are generated with user provided filename_HH:MM:SS_DD-MM-YY.tar.gz

	-   - generate tech-support with core files from both NCCs and all NCPs (under /core)

	-  ncp-id - generate tech-support specific NCCs, NCPs and NCMs only.

	-  Only single techsupport request can be handled by DNOS at the same moment. If another request is given while a different tech-support file is currently created, the following message will be displayed "Cannot produce a new techsupport file, another process is already running"

	-  Only single techsupport file can be stored at /techsupport at a given moment. Generation of new techsupport file will require deletion of old file.

	-  [Node name] [node-id] - generate tech-support file with information of a specific node in the cluster.

  - By default, generate tech-support file that covers all cluster nodes

	-  Component - Select DNOS components for which information will be included in tech-support file

	   -  all - Generate tech-support on all components. default behavior

	   -  datapath - Generate tech-support on datapath components only

	   -  infra - Generate tech-support on infra components only

	   -  management - Generate tech-support on management components only

	   -  routing - Generate tech-support on routing components only

	   -  monilogs - Generate tech-support on monilogs only

	-  inclusive - Generate tech-support file including asic commands which may be service affecting

	-  after - Gather information generated after the specified time.

	  - By default, Generate tech-support with information from the last 24 hours for rotated logs (logs ending in .1, .2, .date etc.) and always
	     the latest version for the main logs (logs that are being currently into and do not have a .1, .2, .date etc. suffix),  regardless if they were modified in the last 24 hours or not

	-  before - Gather information generated after the specified time

	  - By default, Generate tech-support with information from the last 24 hours for rotated logs (logs ending in .1, .2, .date etc.) and always
	     the latest version for the main logs (logs that are being currently into and do not have a .1, .2, .date etc. suffix),  regardless if they were modified in the last 24 hours or not

	-  password - generate tech-support with passwords. By default, passwords are removed from the output

	-  force - automatically delete previous techsupport file. by default user is prompt to choose whether to delete previous techsupport file in order to complete techsupport generation or to cancel operation.

	- info-type - specify types of files to be included in tech-support info

		- basic - include all textual log files

		-  core-dumps - prcoesses binary core dump files.

			- By default, core dumps files are not included in the tech-support tar.

		- journal-files - binary output of Active NCC Base-OS journal files, which are the in memory process logs

			- By default, journal files files are not included in the tech-support tar.


**Parameter table**

+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| Parameter      | Description                                                                                                                                                                                                                                     | Range                                                                                             | Default          |
+================+=================================================================================================================================================================================================================================================+===================================================================================================+==================+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| file-name      | Provide a name for the file.                                                                                                                                                                                                                    | \-                                                                                                | \-               |
|                | A date suffix is added to the user provided name: _HH:MM:SS_DD-MM-YY.tar                                                                                                                                                                        |                                                                                                   |                  |
|                | A prefix is also added  `ts_`                                                                                                                                                                                                                   |                                                                                                   |                  |
|                | The file_name:                                                                                                                                                                                                                                  |                                                                                                   |                  |
|                | - Starts with an alphanumeric character                                                                                                                                                                                                         |                                                                                                   |                  |
|                | - Has a total length of at least 2 characters                                                                                                                                                                                                   |                                                                                                   |                  |
|                | - Have a maximum total length of 228 characters (1 + 227).                                                                                                                                                                                      |                                                                                                   |                  |
|                | - Only contain letters, digits, dots, underscores, or hyphens.                                                                                                                                                                                  |                                                                                                   |                  |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| component      | Include information from the specified DNOS component.                                                                                                                                                                                          | All - generate file with information from all components                                          | All              |
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
|                |                                                                                                                                                                                                                                                 | Datapath - generate file with information from datapath components only                           |                  |
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
|                |                                                                                                                                                                                                                                                 | Infra - generate file with information from infrastructure components only                        |                  |
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
|                |                                                                                                                                                                                                                                                 | Management - generate file with information from management components only                       |                  |
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
|                |                                                                                                                                                                                                                                                 | Monilogs - generate file with information from monilogs components only                           |                  |
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
|                |                                                                                                                                                                                                                                                 | Routing - generate file with information from routing components only                             |                  |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| password       | Generates the tech-support file with passwords. By default, passwords are removed from the output.                                                                                                                                              | \-                                                                                                | \-               |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| force          | Automatically delete a previous tech-support file. By default, you will be prompted to choose whether to delete a previous tech-support file in order to complete the generation of the tech-support   file, or to cancel the operation.        | \-                                                                                                | \-               |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| ncc-id         | Generate the tech-support file with information from the specified NCC only.                                                                                                                                                                    | 0..1                                                                                              | \-               |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| ncp-id         | Generate the tech-support file with information from the specified NCP only.                                                                                                                                                                    | 0..47                                                                                             | \-               |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| ncf-id         | Generate the tech-support file with information from the specified NCF only.                                                                                                                                                                    | 0..12                                                                                             | \-               |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| ncm-id         | Generate the tech-support file with information from specific NCCs , NCMs, and NCPs.                                                                                                                                                            | 0A, 0B, 1A, 1B                                                                                    | \-               |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| info-type      | Specifies the type of files to be included ion tech-support info                                                                                                                                                                                | basic - include all textual log files                                                             |  \-              |
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
|                |                                                                                                                                                                                                                                                 | core-dumps - process binary core dump files (not included by default)                             |                  |
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
|                |                                                                                                                                                                                                                                                 | journal-files - binary output of Active NCC Base-OS journal files (not included by default).      |                  |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| inclusive      | The tech-support file will include information generated for deep interfaces diagnostics for NCP and NCF only.                                                                                                                                  | \-                                                                                                |  \-              |
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
|                | **This option is considered traffic-affecting and requires system restart after completed.**                                                                                                                                                    |                                                                                                   |                  |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| before-time    | The tech-support file will only include information generated before the specified time.                                                                                                                                                        | yyyy-mm-ddThh:mm:ss[.sss]                                                                         | Last 24 hours    |
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
|                | Can be used in combination with "after" to create a range of dates.                                                                                                                                                                             |                                                                                                   |                  |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
| after-time     | The tech-support file will only include information generated after the specified time.                                                                                                                                                         | yyyy-mm-ddThh:mm:ss[.sss]                                                                         | Last 24 hours    |
|                |                                                                                                                                                                                                                                                 |                                                                                                   |                  |
|                | Can be used in combination with "before" to create a range of dates.                                                                                                                                                                            |                                                                                                   |                  |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+------------------+

**Example**
::

	dnRouter# request system tech-support MyTechSupportFile
	13:32:00_30-01-2018 System is generating Tech-support file
	dnRouter#

	Tech-support request: Tech-support ts_MyTechSupportFile_13_35_07_30-01-2018.tar successfully generated on 30-Jan-2018 13:57:56


	dnRouter# request system tech-support MyTechSupportFile include core-dumps
	13:32:00_30-01-2018 System is generating Tech-support file
	dnRouter#
	Tech-support request: Tech-support ts_MyTechSupportFile_13_35_07_30-01-2018.tar successfully generated on 30-Jan-2018 13:57:56

	dnRouter# request system tech-support MyTechSupportFile include basic, core-dumps
	13:32:00_30-01-2018 System is generating Tech-support file
	dnRouter#
	Tech-support request: Tech-support ts_MyTechSupportFile_13_35_07_30-01-2018.tar successfully generated on 30-Jan-2018 13:57:56

	dnRouter# request system tech-support MyTechSupportFile component infra ncc 1
	13:32:00_30-01-2018 System is generating Tech-support file
	dnRouter#
	Tech-support request: Tech-support ts_MyTechSupportFile_13_35_07_30-01-2018.tar successfully generated on 30-Jan-2018 13:57:56

	dnRouter# request system tech-support MyTechSupportFile ncc 0 after 2020-01-02T07:35:00 force
	13:32:00_30-01-2018 System is generating Tech-support file
	dnRouter#
	Tech-support request: Tech-support ts_MyTechSupportFile_13_35_07_30-01-2018.tar successfully generated on 30-Jan-2018 13:57:56

	dnRouter# request system tech-support MyTechSupportFile component routing
	Warning: Previous techsupport files exist. Are you sure you want to erase?  (Yes/No) [No]?
	Tech-support request: Tech-support ts_MyTechSupportFile_13_35_07_30-01-2018.tar successfully generated on 30-Jan-2018 13:57:56

	dnRouter# request system tech-support MyTechSupportFile ncp 1 inclusive
	Warning: This command may be service-affecting, and as such is considered disruptive.
	/** ENSURE THE ELEMENT IS NOT CARRYING TRAFFIC **/
	Please restart the system once it is completed!
	Are you sure you want to proceed? (Yes/No) [No]?
	Tech-support request: Tech-support ts_MyTechSupportFile_13_35_07_30-01-2018.tar successfully generated on 30-Jan-2018 13:57:56

.. **Help line:**

**Command History**

+-------------+--------------------------------------------------------------------------------------------------------------------------------------+
|             |                                                                                                                                      |
| Release     | Modification                                                                                                                         |
+=============+======================================================================================================================================+
| 5.1.0       | Command introduced                                                                                                                   |
+-------------+--------------------------------------------------------------------------------------------------------------------------------------+
| 6.0         | Added forwarder-id option                                                                                                            |
+-------------+--------------------------------------------------------------------------------------------------------------------------------------+
| 10.0        | Updated syntax to new architecture                                                                                                   |
+-------------+--------------------------------------------------------------------------------------------------------------------------------------+
| 11.0        | Added the command to recovery mode, updated the   syntax of the operation mode to include type, component, and force                 |
+-------------+--------------------------------------------------------------------------------------------------------------------------------------+
| 11.5        | Added option to include files before and/or after   a specific date. Removed the command from recovery mode (was not implemented)    |
+-------------+--------------------------------------------------------------------------------------------------------------------------------------+
| 13.1        | Updated parameter values                                                                                                             |
+-------------+--------------------------------------------------------------------------------------------------------------------------------------+
| 18.1        | Added inclusive parameter for deep interfaces diagnostics for single NCP and NCF only                                                |
+-------------+--------------------------------------------------------------------------------------------------------------------------------------+
| 18.3        | Added a new component - monilogs. Collects the monilogs from the node                                                                |
+-------------+--------------------------------------------------------------------------------------------------------------------------------------+
---

## request system ztp start.rst

request system ztp start
------------------------

**Minimum user role:** admin

To start the Zero Touch Provisioning (ZTP) process in the event that the ZTP was previously stopped by the user, use the following command:

**Command syntax:** request system ztp start

**Command mode:** operational

**Note**

- If ZTP is already running, executing this command will have no effect.
- In case the ZTP process is stopped, the ZTP process will immediately restart after executing this command.
- In case ZTP already completed, the ZTP process will not restart.
- At the time these commands are introduced, the output is the same for each case and does not vary according to the actual state.

**Example**
::

	dnRouter# request system ztp start
	Warning: Are you sure you want to start ztp process? (Yes/No) [No]?
	Attempted to start ZTP procedure

.. **Hidden Note:**

 - Yes/no validation should exist for the operation.


.. **Parameter table:**


.. **Help line:** 

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 19.3    | Command introduced                  |
+---------+-------------------------------------+

---

## request system ztp stop.rst

request system ztp stop
-----------------------

**Minimum user role:** admin

To stop the Zero Touch Provisioning (ZTP) process, use the following command:

**Command syntax:** request system ztp stop

**Command mode:** operational

**Note**

- If ZTP is already stopped, executing this command will have no effect.
- In case the ZTP process is active, the ZTP process will stop after completing the current task.
- At the time these commands are introduced, the output is the same for each case and does not vary according to the actual state.

**Example**
::

	dnRouter# request system ztp stop
	Warning: Are you sure you want to stop ztp process? (Yes/No) [No]? Yes
	Attempted to stop ZTP procedure

.. **Hidden Note:**

 - Yes/no validation should exist for the operation.


.. **Parameter table:**


.. **Help line:**

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 19.3    | Command introduced                  |
+---------+-------------------------------------+

---

## request system ztp terminate.rst

request system ztp terminate
----------------------------

**Minimum user role:** admin

To terminate the Zero Touch Provisioning (ZTP) process, use the following command:

**Command syntax:** request system ztp terminate

**Command mode:** operational

**Note**

- Once the ZTP process is terminated, The user wont be able to rerun ZTP without deleting of DNOS router system.
- In case ZTP already terminated or completed, the command will have no effect.
- At the time these commands are introduced, the output is the same for each case and does not vary according to the actual state.

**Example**
::

	dnRouter# request system ztp terminate
	Warning: Termination is irreversible. Are you sure you want to terminate ztp process? (Yes/No) [No]? Yes
	Attempted to terminate ZTP procedure

.. **Hidden Note:**

 - Yes/no validation should exist for the operation.


.. **Parameter table:**


.. **Help line:**

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 19.3    | Command introduced                  |
+---------+-------------------------------------+

---

## request uefi key add.rst

request uefi key add
--------------------

**Minimum user role:** admin

Add a key to the specified UEFI key list.

**Command syntax: request uefi key add** { ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] \| ncm [ncm-id]} **[user-name]@ [url] [key-type]**

**Command mode:** operational

**Note:**

- Validation : User Yes/no question with the specified key file name.

- Adding keys to UEFI is supported only while in Setup mode.

- Adding a Platform Key will switch UEFI into User mode and switching back into Setup mode requires a noPK.auth file signed with the PK private key.

- If no ncc-id/ncp-id/ncf-id/ncm-id is specified, the command will address the active NCC.

- An error message is returned when the specified node type or node id are unavailable or not supported.

- Key types:

 -  pk - platform key

 -  kek - key exchange key

 -  db - authorized database key

 -  dbx - forbidden database key

**Parameter table:**

+-----------------------+--------------------------------------------------------+---------------+
| Parameter             | Values                                                 | Default value |
+=======================+========================================================+===============+
| ncc-id                | 0-1                                                    |               |
+-----------------------+--------------------------------------------------------+---------------+
| ncp-id                | integer                                                |               |
+-----------------------+--------------------------------------------------------+---------------+
| ncf-id                | integer                                                |               |
+-----------------------+--------------------------------------------------------+---------------+
| ncm                   | a0, b0, a1, b1                                         |               |
+-----------------------+--------------------------------------------------------+---------------+
| user-name             | string                                                 | Current user  |
+-----------------------+--------------------------------------------------------+---------------+
| url                   | user@host://filename                                   |               |
+-----------------------+--------------------------------------------------------+---------------+
| key-type              | pk / kek / db / dbx                                    |               |
+-----------------------+--------------------------------------------------------+---------------+

**Example**
::

	dnRouter# request uefi key add user@192.168.1.1://keys/pk.auth pk
	Are you sure you want to add pk key (Yes/No) [No]? Yes
	Key successfully added.

	dnRouter# request uefi key add user@192.168.1.1://keys/pk.auth pk
	Are you sure you want to add pk key (Yes/No) [No]? Yes
	Error: failed to add key.

	dnRouter# request uefi key add ncp 0 user@192.168.1.1://keys/kek.auth kek
	Are you sure you want to add kek key (Yes/No) [No]?

	dnRouter# request uefi key add ncp 1 user@192.168.1.1://keys/kek.auth kek
	Error: node type or node id unavailable or not supported.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 25.1    | Command introduced                  |
+---------+-------------------------------------+


---

## request uefi key delete.rst

request uefi key delete
-----------------------

**Minimum user role:** admin

Delete the key from the UEFI key list.

**Command syntax: request uefi key delete** { ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] \| ncm [ncm-id]} **[user-name]@ [url] [key-type]**

**Command mode:** operational

**Note:**

- Validation : User Yes/no question with the specified key file name.

- Platform Key deletion requires a noPK.auth file signed using the private PK part. PK deletion will switch UEFI into Setup mode.

- Keys cannot be deleted from UEFI when UEFI in User mode.

- If no ncc-id/ncp-id/ncf-id/ncm-id is specified, the command will address the active NCC.

- An error message is returned when the specified node type or node id are unavailable or not supported.

- Key types:

 -  pk - platform key

 -  kek - key exchange key

 -  db - authorized database key

 -  dbx - forbidden database key

**Parameter table:**

+-----------------------+--------------------------------------------------------+---------------+
| Parameter             | Values                                                 | Default value |
+=======================+========================================================+===============+
| ncc-id                | 0-1                                                    |               |
+-----------------------+--------------------------------------------------------+---------------+
| ncp-id                | integer                                                |               |
+-----------------------+--------------------------------------------------------+---------------+
| ncf-id                | integer                                                |               |
+-----------------------+--------------------------------------------------------+---------------+
| ncm                   | a0, b0, a1, b1                                         |               |
+-----------------------+--------------------------------------------------------+---------------+
| user-name             | string                                                 | Current user  |
+-----------------------+--------------------------------------------------------+---------------+
| url                   | user@host://filename                                   |               |
+-----------------------+--------------------------------------------------------+---------------+
| key-type              | pk / kek / db / dbx                                    |               |
+-----------------------+--------------------------------------------------------+---------------+

**Example**
::

	dnRouter# request uefi key delete user@192.168.1.1://keys/kek.crt kek
	Are you sure you want to delete kek key (Yes/No) [No]? Yes
	Key successfully deleted.

	dnRouter# request uefi key delete user@192.168.1.1://keys/noPK.auth pk
	Are you sure you want to delete pk key (Yes/No) [No]? Yes
	Key successfully deleted.

	dnRouter# request uefi key delete user@192.168.1.1://keys/db.crt db
	Are you sure you want to delete db key (Yes/No) [No]? Yes
	Key successfully deleted.

	dnRouter# request uefi key delete user@192.168.1.1://keys/pk.cer pk
	Are you sure you want to delete pk key (Yes/No) [No]? Yes
	Error: failed to delete key.

	dnRouter# request uefi key delete ncp 0 user@192.168.1.1://keys/kek.crt kek
	Are you sure you want to delete kek key (Yes/No) [No]?

	dnRouter# request uefi key delete ncp 1 user@192.168.1.1://keys/kek.crt kek
	Error: node type or node id unavailable or not supported.


**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 25.1    | Command introduced                  |
+---------+-------------------------------------+
---

## request uefi key read.rst

request uefi key read
---------------------

**Minimum user role:** admin

Read out specified key-list.

**Command syntax: request uefi key read** { ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] \| ncm [ncm-id]} **[user-name]@ [url] [key-type]**

**Command mode:** operational

**Note:**

- If no ncc-id/ncp-id/ncf-id/ncm-id is specified, the command will address the active NCC.

- An error message is returned when the specified node type or node id are unavailable or not supported.

- Key type:

 -  pk - platform key

 -  kek - key exchange key

 -  db - authorized database key list

 -  dbx - forbidden database key list

**Parameter table:**

+-----------------------+-----------------------------------------------+---------------+
| Parameter             | Values                                        | Default value |
+=======================+===============================================+===============+
| ncc-id                | 0-1                                           |               |
+-----------------------+-----------------------------------------------+---------------+
| ncp-id                | integer                                       |               |
+-----------------------+-----------------------------------------------+---------------+
| ncf-id                | integer                                       |               |
+-----------------------+-----------------------------------------------+---------------+
| ncm                   | a0, b0, a1, b1                                |               |
+-----------------------+-----------------------------------------------+---------------+
| user-name             | string                                        | Current user  |
+-----------------------+-----------------------------------------------+---------------+
| url                   | user@host://destination-filename              |               |
+-----------------------+-----------------------------------------------+---------------+
| key-type              | pk / kek / db / dbx                           |               |
+-----------------------+-----------------------------------------------+---------------+

**Example**
::

	dnRouter# request uefi key read user@192.168.1.1://keys/pk.esl pk
	Key successfully read.

	dnRouter# request uefi key read user@192.168.1.1://keys/pk.esl pk
	Error: failed to read key list.

	dnRouter# request uefi key read ncp 0 user@192.168.1.1://keys/dbx.esl dbx
	Key successfully read.

	dnRouter# request uefi key read ncp 1 user@192.168.1.1://keys/kek.esl kek
	Error: node type or node id unavailable or not supported.

**Command History**

+---------+--------------------------------------------------------------------+
| Release | Modification                                                       |
+=========+====================================================================+
| 25.1    | Command introduced                                                 |
+---------+--------------------------------------------------------------------+
---


---

# SECTION 4: RECOVERY MODE COMMANDS

Files from Recovery Mode Commands folder:        8 files

## recovery mode commands.rst

Recovery Mode Commands
----------------------

**Minimum user role:** techsupport

When you log in to a system in recovery mode, a banner indicating that the system is in recovery mode is displayed:

When the system is in recovery mode, the following commands are available:

+---------------------------------+----------------------------------------+
| Command                         | Reference                              |
+=================================+========================================+
| request system restart          | request system restart                 |
+---------------------------------+----------------------------------------+
| request system factory-default  | request system restart factory-default |
+---------------------------------+----------------------------------------+
| request system restart rollback | request system restart rollback        |
+---------------------------------+----------------------------------------+
| request system tech-support     | request system tech-support            |
+---------------------------------+----------------------------------------+
| show rollback                   | show rollback                          |
+---------------------------------+----------------------------------------+
| run start shell                 | run start shell                        |
+---------------------------------+----------------------------------------+

**Command mode:** recovery

**Note**

- These commands are not logged or accounted by TACACS.

- You have a single attempt to enter a valid password.

.. - User will have a single attempt to enter password

**Example**
::

	user@user-1:~/HOME$ ssh 0 -p 2223 -l dnroot
	System is in Recovery mode!
	dnroot@0's password:




---

## recovery- request system tech-support.rst

recovery: request system tech-support
-------------------------------------

**Minimum user role:** operator

You can generate a file with all the logs, configuration, database files and system output commands that you can save for later use (for example, when opening a customer support case).

After running the command, you will regain full CLI control while the system is generating the tech-support file in the background.

The system can handle only one request to generate a tech-support file at a time. If the system is already creating a tech-support file while you enter another request, an error message will be displayed.

To generate the tech-support file:

**Command syntax: request system tech-support [file-name]** component [component] {ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] \| ncm [ncm-id]} after [after-time] before [before-time] password force include {[info-type], [info-type], ...}

**Command mode:** operation 

**Note**

- By default, generate tech-support with information from the last 24 hours for rotated logs (end with .1, .2, date, etc.) and always include the latest version of the main logs (logs that are currently being written to) regardless if they were modified in the past 24 hours.

- The Tech-support files are generated on the active NCC node at /techsupport/ Only one file is stored at a time.

- When you generate a tech-support file, a previous file will be deleted to make room for the new file.

.. - User gets back cli prompt after invoking "request system tech-support" user have full CLI support while techsupport is being generated in the background.

	- Tech-support files are generated on active NCC node at /techsupport/

	- tech-support files are generated with user provided filename_HH:MM:SS_DD-MM-YY.tar.gz

	- extended - generate tech-support with core files from both NCCs and all NCPs (under /core)

	- ncp-id - generate tech-support from NCCs and specific NCP only.

	- Only single techsupport request can be handled by DNOS at the same moment. If another request is given while a different tech-support file is currently created, the following message will be displayed "Cannot produce a new techsupport file, another process is already running"

	- Only single techsupport file can be stored at /techsupport at a given moment. Generation of new techsupport file will require deletion of old file.

**Parameter table**

+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| Parameter   | Description                                                                                                                                                                                                                            | Range                                                                                        | Default       |
+=============+========================================================================================================================================================================================================================================+==============================================================================================+===============+
| file-name   | Provide a name for the file. A date suffix is added to the user provided name: _HH:MM:SS_DD-MM-YY.tar                                                                                                                                  | \-                                                                                           | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| component   | Include information from the specified DNOS component.                                                                                                                                                                                 | All - generate file with information from all components                                     | All           |
|             |                                                                                                                                                                                                                                        | Datapath - generate file with information from datapath components only                      |               |
|             |                                                                                                                                                                                                                                        | Infra - generate file with information from infrastructure components only                   |               |
|             |                                                                                                                                                                                                                                        | Management - generate file with information from management components only                  |               |
|             |                                                                                                                                                                                                                                        | Routing - generate file with information from routing components only                        |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| password    | Generates the tech-support file with passwords. By default, passwords are removed from the output.                                                                                                                                     | \-                                                                                           | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| force       | Automatically delete a previous tech-support file. By default, you will be prompted to choose whether to delete a previous tech-support file in order to complete the generation of the tech-support file, or to cancel the operation. | \-                                                                                           | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncc-id      | Generate the tech-support file with information from the specified NCC only.                                                                                                                                                           | 0..1                                                                                         | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncp-id      | Generate the tech-support file with information from the specified NCP only.                                                                                                                                                           | 0..47                                                                                        | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncf-id      | Generate the tech-support file with information from the specified NCF only.                                                                                                                                                           | 0..12                                                                                        | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncm-id      | Generate the tech-support file with information from specific NCCs , NCMs, and NCPs.                                                                                                                                                   | 0A, 0B, 1A, 1B                                                                               | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| info-type   | Specifies the type of files to be included ion tech-support info                                                                                                                                                                       | basic - include all textual log files                                                        |               |
|             |                                                                                                                                                                                                                                        | core-dumps - process binary core dump files (not included by default)                        |               |
|             |                                                                                                                                                                                                                                        | journal-files - binary output of Active NCC Base-OS journal files (not included by default). |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| before-time | The tech-support file will only include information generated before the specified time.                                                                                                                                               | yyyy-mm-ddThh:mm:ss[.sss]                                                                    | Last 24 hours |
|             | Can be used in combination with "after" to create a range of dates.                                                                                                                                                                    |                                                                                              |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| after-time  | The tech-support file will only include information generated after the specified time.                                                                                                                                                | yyyy-mm-ddThh:mm:ss[.sss]                                                                    | Last 24 hours |
|             | Can be used in combination with "before" to create a range of dates.                                                                                                                                                                   |                                                                                              |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+

**Example**
::

	dnRouter(RECOVERY)# request system tech-support MyTechSupportFile
	13:32:00_30-01-2018 System is generating Tech-support file
	dnRouter(RECOVERY)#

	Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar
	


	dnRouter(RECOVERY)# request system tech-support MyTechSupportFile include core-dumps
	13:32:00_30-01-2018 System is generating Tech-support file
	dnRouter(RECOVERY)#
	Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar

	dnRouter(RECOVERY)# request system tech-support MyTechSupportFile include basic, core-dumps
	13:32:00_30-01-2018 System is generating Tech-support file
	dnRouter(RECOVERY)#
	Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar

	dnRouter(RECOVERY)# request system tech-support MyTechSupportFile component infra ncc-all
	13:32:00_30-01-2018 System is generating Tech-support file
	dnRouter(RECOVERY)#
	Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar

	dnRouter(RECOVERY)# request system tech-support MyTechSupportFile ncc 0 after 2020-01-02T07:35:00 force
	13:32:00_30-01-2018 System is generating Tech-support file
	dnRouter(RECOVERY)#
	Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar

	dnRouter(RECOVERY)# request system tech-support MyTechSupportFile  component routing
	Warning: Previous techsupport files exist. Are you sure you want to erase?  (Yes/No) [No]?
	Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar

**Command History**

+---------+---------------------------------------------------------------------------------------------------------------------------------+
| Release | Modification                                                                                                                    |
+=========+=================================================================================================================================+
| 5.1.0   | Command introduced                                                                                                              |
+---------+---------------------------------------------------------------------------------------------------------------------------------+
| 6.0     | Added forwarder-id option                                                                                                       |
+---------+---------------------------------------------------------------------------------------------------------------------------------+
| 10.0    | Updated syntax to new architecture                                                                                              |
+---------+---------------------------------------------------------------------------------------------------------------------------------+
| 11.0    | Added the command to recovery mode, updated the syntax of the operation mode to include type, component, and force              |
+---------+---------------------------------------------------------------------------------------------------------------------------------+
| 11.5    | Added option to include files before and/or after a specific date. Removed the command from recovery mode (was not implemented) |
+---------+---------------------------------------------------------------------------------------------------------------------------------+
| 13.1    | Updated parameter values                                                                                                        |
+---------+---------------------------------------------------------------------------------------------------------------------------------+



---

## request system restart factory-default.rst

request system restart factory-default
--------------------------------------

**Minimum user role:** admin

By default, factory default does a new commit by applying the system default configuration.

Use the force option to wipe the configuration and operational database (management engine, forwarding engine, routing engine, and selector), including all rollback information. The system will return to first deployment state. restarts the system and clears the system database (management engine, forwarding engine, routing engine, and selector). All configuration including rollback information is deleted. Persistent files, e.g. log files, saved configuration files, etc. are not deleted.

**Command syntax: request system restart factory-default** force

**Command mode:** recovery

**Note**

- This operation removes all configuration, including users, passwords, and cluster NCPs. Removing the cluster NCPs causes the network interfaces to go down.

.. - Yes/no validation should exist for system restart factory-default operation.

	- Request system restart performs applicative containers restart across all the system.

	- Applicative containers are Management-engine, Routing-engine, Forwarding-engine and selector.

	- By default, Factory-default preform a new commit by applying the system default configuartion.

	- Factory-default force clears all database configuration. Including rollback information. Any persistent files (i.e log files, saved configuration files etc) remain not deleted.

**Example**
::

	dnRouter(RECOVERY)# request system restart factory-default
	Warning: Are you sure you want to perform restart factory-default? Operation will erase all system database (Yes/No) [No]?

**Command History**

+---------+-----------------------------------------------------------------+
| Release | Modification                                                    |
+=========+=================================================================+
| 9.0     | Command introduced                                              |
+---------+-----------------------------------------------------------------+
| 11.5    | Added option to wipe the configuration and operational database |
+---------+-----------------------------------------------------------------+



---

## request system restart rollback.rst

request system restart rollback
-------------------------------

**Minimum user role:** operator

You can generate a file with all the logs, configuration, database files and system output commands that you can save for later use (for example, when opening a customer support case).

After running the command, you will regain full CLI control while the system is generating the tech-support file in the background.

The system can handle only one request to generate a tech-support file at a time. If the system is already creating a tech-support file while you enter another request, an error message will be displayed.

To generate the tech-support file:

**Command syntax: request system restart rollback [rollback-id]**

**Command mode:** operation 

**Note**

- By default, generate tech-support with information from the last 24 hours for rotated logs (end with .1, .2, date, etc.) and always include the latest version of the main logs (logs that are currently being written to) regardless if they were modified in the past 24 hours.

- The Tech-support files are generated on the active NCC node at /techsupport/ Only one file is stored at a time. 

- When you generate a tech-support file, a previous file will be deleted to make room for the new file.

.. - Request system restart performs applicative containers restart across all the system.

	- Applicative containers are Management-engine, Routing-engine, Forwarding-engine and selector.

**Parameter table**

+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| Parameter   | Description                                                                                                                                                                                                                            | Range                                                                                        | Default       |
+=============+========================================================================================================================================================================================================================================+==============================================================================================+===============+
| file-name   | Provide a name for the file. A date suffix is added to the user provided name: _HH:MM:SS_DD-MM-YY.tar                                                                                                                                  | \-                                                                                           | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| component   | Include information from the specified DNOS component.                                                                                                                                                                                 | All - generate file with information from all components                                     | All           |
|             |                                                                                                                                                                                                                                        | Datapath - generate file with information from datapath components only                      |               |
|             |                                                                                                                                                                                                                                        | Infra - generate file with information from infrastructure components only                   |               |
|             |                                                                                                                                                                                                                                        | Management - generate file with information from management components only                  |               |
|             |                                                                                                                                                                                                                                        | Routing - generate file with information from routing components only                        |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| password    | Generates the tech-support file with passwords. By default, passwords are removed from the output.                                                                                                                                     | \-                                                                                           | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| force       | Automatically delete a previous tech-support file. By default, you will be prompted to choose whether to delete a previous tech-support file in order to complete the generation of the tech-support file, or to cancel the operation. | \-                                                                                           | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncc-id      | Generate the tech-support file with information from the specified NCC only.                                                                                                                                                           | 0..1                                                                                         | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncp-id      | Generate the tech-support file with information from the specified NCP only.                                                                                                                                                           | 0..47                                                                                        | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncf-id      | Generate the tech-support file with information from the specified NCF only.                                                                                                                                                           | 0..12                                                                                        | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncm-id      | Generate the tech-support file with information from specific NCCs , NCMs, and NCPs.                                                                                                                                                   | 0A, 0B, 1A, 1B                                                                               | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| info-type   | Specifies the type of files to be included ion tech-support info                                                                                                                                                                       | basic - include all textual log files                                                        |               |
|             |                                                                                                                                                                                                                                        | core-dumps - process binary core dump files (not included by default)                        |               |
|             |                                                                                                                                                                                                                                        | journal-files - binary output of Active NCC Base-OS journal files (not included by default). |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| before-time | The tech-support file will only include information generated before the specified time.                                                                                                                                               | yyyy-mm-ddThh:mm:ss[.sss]                                                                    | Last 24 hours |
|             | Can be used in combination with "after" to create a range of dates.                                                                                                                                                                    |                                                                                              |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| after-time  | The tech-support file will only include information generated after the specified time.                                                                                                                                                | yyyy-mm-ddThh:mm:ss[.sss]                                                                    | Last 24 hours |
|             | Can be used in combination with "before" to create a range of dates.                                                                                                                                                                   |                                                                                              |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+

**Example**
::

	dnRouter(RECOVERY)# request system restart rollback 2
	

**Command History**

+---------+---------------------------------------------------------------------------------------------------------------------------------+
| Release | Modification                                                                                                                    |
+=========+=================================================================================================================================+
| 5.1.0   | Command introduced                                                                                                              |
+---------+---------------------------------------------------------------------------------------------------------------------------------+
| 6.0     | Added forwarder-id option                                                                                                       |
+---------+---------------------------------------------------------------------------------------------------------------------------------+
| 10.0    | Updated syntax to new architecture                                                                                              |
+---------+---------------------------------------------------------------------------------------------------------------------------------+
| 11.0    | Added the command to recovery mode, updated the syntax of the operation mode to include type, component, and force              |
+---------+---------------------------------------------------------------------------------------------------------------------------------+
| 11.5    | Added option to include files before and/or after a specific date. Removed the command from recovery mode (was not implemented) |
+---------+---------------------------------------------------------------------------------------------------------------------------------+
| 13.1    | Updated parameter values                                                                                                        |
+---------+---------------------------------------------------------------------------------------------------------------------------------+




---

## request system restart.rst

request system restart
----------------------

**Minimum user role:** admin

Use this command to do a system wide restart, or a node restart. When requesting a system-wide restart, the network interfaces on the NCPs are shut down so no further traffic can be sent or received. With the interfaces down, external devices stop forwarding traffic to the device. Then, the cluster nodes are restarted one by one.

To restart the system, use the following command.

**Command syntax: request system restart**

**Command mode:** recovery 

**Note**

- To perform a cold restart to a standby NCC, connectivity to it must be available.

.. - Request system restart performs applicative containers restart across all the system.

	- Applicative containers are Management-engine, Routing-engine, Forwarding-engine and selector.

**Parameter table**

+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| Parameter | Description                                                                                                                                                                                                                                             | Comment                      |
+===========+=========================================================================================================================================================================================================================================================+==============================+
| ncc-id    | Restart only the specified NCC                                                                                                                                                                                                                          | 0..1                         |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| ncp-id    | Restart only the specified NCP                                                                                                                                                                                                                          | 0..47                        |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| ncf-id    | Restart only the specified NCF                                                                                                                                                                                                                          | 0..12                        |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| ncm-id    | Restart only the specified NCM                                                                                                                                                                                                                          | a0, b0, a1, b1               |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| warm      | By default, a cold restart is done, meaning that the power is reset for all cluster elements. By specifying warm, only the DNOS software is restarted (the applicative containers: management-engine, routing-engine, forwarding-engine, and selector). | Not applicable to NCM        |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| force     | Remotely enforce a cold restart using IPMI connectivity.                                                                                                                                                                                                | Not applicable to NCM or NCC |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+

When the system is in recovery mode, the system restart command is used to exit recovery mode:

**Example**
::

	dnRouter(RECOVERY)# request system restart
	

**Command History**

+---------+----------------------------------------------------------------+
| Release | Modification                                                   |
+=========+================================================================+
| 5.1.0   | Command introduced                                             |
+---------+----------------------------------------------------------------+
| 11.0    | Added support for all cluster elements (NCC, NCP, NCF and NCM  |
+---------+----------------------------------------------------------------+
| 11.4    | Added ability to warm restart the DNOS software.               |
+---------+----------------------------------------------------------------+
| 15.0    | Added the ability to force a cold restart to the DNOS software |
+---------+----------------------------------------------------------------+



---

## run start shell.rst

run start shell
---------------

**Minimum user role:** admin

To access a node's shell container:

**Command syntax: run start shell** {ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] \| ncm [ncm-hostname]}

**Command mode:** recovery

**Note**

- root@node-manager - an NCC prompt. The prompt varies depending on the accessed NCE .

- TACACS+ AAA (recovery mode) is allowed for local users only.

- The command in recovery mode provides access to the shell of the active NCC only.

.. - No TACACS AAA (Recovery mode), should be allowed for local users only

	- "exit" commands reverts back to the Recovery Mode CLI.

**Parameter table**

+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Parameter      | Description                                                                                            | Range                                                                        |
+================+========================================================================================================+==============================================================================+
| ncc-id         | Provides access to the shell of the specified NCC                                                      | 0..1                                                                         |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ncp-id         | Provides access to the shell of the specified NCP                                                      | 0..(max NCP number per cluster type -1), bfd-master                          |
|                | bfd-master - provides access to the ncp that holds all non uBFD, BFD sessions.                         |                                                                              |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ncf-id         | Provides access to the shell of the specified NCF                                                      | 0..(max NCF number per cluster type -1)                                      |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| container-name | Provides access to the container within the specified node.                                            | A container from the process list that applicable to the specified node name |
|                | The container option is not applicable to NCMs.                                                        |                                                                              |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ncm-id         | Provides access to the shell of the specified NCM                                                      | a0, b0, a1, b1                                                               |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ncc active     | Provides access to containers in the current active NCC. When set, a container name must be specified. | \-                                                                           |
+----------------+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+

If you do not provide a node name and ID, you will be granted access to the active NCC's shell.

If you do not specify a container within the node, you will be granted access to the following containers by default:

+-----------+--------------------------+
| Node Type | Default Container        |
+===========+==========================+
| NCC       | routing-engine container |
+-----------+--------------------------+
| NCP       | datapath container       |
+-----------+--------------------------+
| NCF       | fabric container         |
+-----------+--------------------------+

To return to the DNOS CLI, use the exit command.

**Example**
::

	dnRouter(RECOVERY)#  run start shell
	root@routing_engine:/#

	root@routing_engine:/# exit
	dnRouter(RECOVERY)#

.. **Help line:** access to shell of the NCC/NCP/NCF/NCM components

**Command History**

+---------+-----------------------------------------------------+
| Release | Modification                                        |
+=========+=====================================================+
| 10.0    | Command introduced                                  |
+---------+-----------------------------------------------------+
| 11.0    | Command added to recovery mode                      |
+---------+-----------------------------------------------------+
| 11.5    | Added option to access containers of the active NCC |
+---------+-----------------------------------------------------+
| 13.0    | Added new ncp option for command - bfd-master       |
+---------+-----------------------------------------------------+

---

## show rollback.rst

show rollback
-------------

**Minimum user role:** viewer

To view the configuration of the transaction file:

**Command syntax: show rollback** [rollback-id]

**Command mode:** recovery 

**Parameter table**

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+-------+
| Parameter   | Description                                                                                                                                   | Range |
+=============+===============================================================================================================================================+=======+
| rollback-id | The rollback-id of the commit transaction file. If you do not specify a rollback-id, all rollbacks available in the system will be displayed. | 0..50 |
|             | A value of 0 will display the current configuration.                                                                                          |       |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+-------+

**Example**
::

	dnRouter(RECOVERY)# show rollback 1
	#dnRouter config-start [27-Jun-2017 22:05:01]
	# version 6
	# user ADMIN
	# user logged something for this rollback
	system name dnRouter
	system login user RootUser 
	system login user RootUser description MyrootUser
	.
	
	.
	
	.
	
	#dnRouter config-end
	
	dnRouter(RECOVERY)# show rollback
	| Id | Time                 | Via     | Log                                         |
	|----|----------------------+---------+---------------------------------------------|
	|  1 | 27-Jun-2017 22:05:01 | cli     | user logged something for this rollback     |
	|  2 | 27-Jun-2017 22:05:01 | cli     |                                             |
	|  3 | 27-Jun-2017 22:05:01 | cli     | Successful commit! Created by MyName2.      |
	|    |                      |         | Update bgp configuration                    |

	

**Command History**

+---------+-----------------------------------------------------------------------+
| Release | Modification                                                          |
+=========+=======================================================================+
| 6.0     | Command introduced                                                    |
+---------+-----------------------------------------------------------------------+
| 11.0    | Command added to recovery mode                                        |
+---------+-----------------------------------------------------------------------+
| 13.1    | Added display of the transaction's origin (CLI/netconf) to the output |
+---------+-----------------------------------------------------------------------+



---

## show system tech-support status.rst

show system tech-support status
-------------------------------

**Minimum user role:** viewer

To display the generation status of the tech-support file while in recovery mode:

**Command syntax: show system tech-support status**

**Command mode:** recovery

**Note**

If no tech-support file is currently being generated, information on the last generated tech-support file is displayed.

The file generation progress includes these steps:

- step 1/5 - preparing

- step 2/5 - discovering containers

- step 3/5 - running scripts on containers

- step 4/5 - collecting files on containers

- step 5/5 - creating archive

.. -  If no tech-support file currently generated, display last created tech-support file information

	-  Possible steps:

	- 1/5 preparing

	- 2/5 discovering containers

	- 3/5 running scripts on containers

	- 4/5 collecting files on containers

	- 5/5 creating archive

**Example**
::

	dnRouter# show system tech-support status

	Tech-support file generation in progress
	Tech-support file generation started at 13:32:00_30-01-2017, by User_1, running for 5 min
	File name MyTechSupportFile_13:32:00_30-01-2017.tar.gz
	Tech-support partition: total 98761166848, used: 11645157376, free: 87116009472, pct: 11.8% used
	Progress: step 3/5 - running scripts on containers

**Command History**

+---------+--------------------------------+
| Release | Modification                   |
+=========+================================+
| 11.2    | Command introduced             |
+---------+--------------------------------+
| 11.5    | Command added to recovery mode |
+---------+--------------------------------+



---


---

# SECTION 5: SET COMMANDS

Files from Set Commands folder:       15 files

## set alarm operator state.rst

set alarm operator state
---------------------------

**Minimum user role:** viewer

Used by the operator to update the alarm operator state, used to acknowledge/close the alarm.

**Command syntax: set alarm operator state**

**Command mode:** operational

**Parameter table:**

+----------------------+---------------------------------------------+---------------+
| Parameter            | Values                                      | Default value |
+======================+=============================================+===============+
| state                | ack, closed                                 |  -/           |
+----------------------+---------------------------------------------+---------------+
| alarm-unique-id      | random generated number                     |  -/           |
+----------------------+---------------------------------------------+---------------+
| description          | string                                      |  -/           |
+----------------------+---------------------------------------------+---------------+

**Note**
-  The alarm-unique-id is a unique id per alarm, presented under show system alarms.
-  State - set by the operator as part of the alarm handling process.
-  Description is a text in quotation marks, length 1..255.


**Example**
::

	dnRouter# set alarm operator state ack alarm 1278605535506855

	dnRouter# set alarm operator state closed alarm 1278605535506855 description "handled the adjacency on the peer"

.. **Help line:** Configure DNOR servers.


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
| 18.0        | Command introduced    |
+-------------+-----------------------+

---

## set cli-ansi-color-disabled.rst

set cli-ansi-color-disabled 
---------------------------

**Minimum user role:** viewer

By default, some of the show outputs of cli commands are displayed with colors. 

You can use this command to disable the ansi coloring in the show output of CLI commands. This functionality allows scripts that automate CLI interaction with DNOS to easily parse the returned output (the coloring in the output adds extra characters to the output, therefore occasionally it needs to be removed). It doesn't influence the coloring in the presentation of log/trace files and is set per individual session.


**Command syntax: set cli-ansi-color-disabled**
**Command syntax: unset cli-ansi-color-disabled**

**Command mode:** operational

**Note**


**Example**
::

	dnRouter# set cli-ansi-color-disabled


**Removing Configuration**

To return the system to the default value (coloring enabled):
::

	dnRouter# unset cli-ansi-color-disabled


.. **Help line:** Disable ansi colouring in CLI commands output

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 15.0        | Command introduced    |
+-------------+-----------------------+
| 25.2        | Command syntax change |
+-------------+-----------------------+
---

## set cli-no-confirm.rst

set cli-no-confirm
------------------

**Minimum user role:** operator

Use this command to enable bypassing confirmation prompts for request commands that require user confirmation. When enabled, request commands that prompt for confirmation will execute immediately without requiring user input.

**Command syntax: set cli-no-confirm**
**Command syntax: unset cli-no-confirm**

**Command mode:** operational

**Note**

- When cli-no-confirm is set, all request commands requiring confirmation will execute without prompts.
- This setting is session-specific and does not persist across sessions.
- Use with caution as it skips safety prompts.

**Example**
::

    dnRouter# request system ncc switchover
    Warning: Are you sure you want to perform NCC switchover (Yes/No) [No]? Y
    Standby NCC is not ready for switchover, operation was aborted

    dnRouter# set cli-no-confirm

    dnRouter# request system ncc switchover
    Standby NCC is not ready for switchover, operation was aborted
    dnRouter#

**Removing Configuration**

To return the system to the default behavior (confirmation required):
::

    dnRouter# unset cli-no-confirm

.. **Help line:** Enable or disable bypassing of confirmation prompts for request commands

**Command History**

+-------------+-------------------------+
| Release     | Modification            |
+=============+=========================+
| 25.1        | Command introduced      |
+-------------+-------------------------+
| 25.2        | Command syntax change   |
+-------------+-------------------------+
---

## set cli-terminal-length.rst

set cli-terminal-length 
-----------------------

**Minimum user role:** viewer

You can set the amount of lines that will be displayed before the "more" option is shown, per cli session. In order to completely disable pagination (equivalent to "no-more" pipe), set 0 for terminal-length.

**Command syntax: set cli-terminal-length [terminal-length]**
**Command syntax: unset cli-terminal-length**

**Command mode:** operational

**Note**

- If the terminal-length is set with N number of lines the 'no more' command will take precedence over the number of lines N.

**Parameter table**

+--------------------+---------------------------------------------------------------------------------------------+------------+-------------+
|                    |                                                                                             |            |             |
| Parameter          | Description                                                                                 | Range      | Default     |
+====================+=============================================================================================+============+=============+
|                    |                                                                                             |            |             |
| terminal-length    | Pagination - The number of lines to display per   cli session, before the 'more' option.    | 0..1023    | \-          |
+--------------------+---------------------------------------------------------------------------------------------+------------+-------------+

**Example**

To set the number of lines:
::

	dnRouter# set cli-terminal-length 200



**Removing Configuration**

To disable pagination:
::

	dnRouter# set cli-terminal-length 0

To remove the cli-terminal-length setting for the session:
::

	dnRouter# unset cli-terminal-length

.. **Help line:** Set the amount of lines that will be displayed before "more" option will be shown

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.2        | Command introduced    |
+-------------+-----------------------+
| 25.2        | Command syntax change |
+-------------+-----------------------+
---

## set cli-timestamp.rst

set cli-timestamp 
------------------

**Minimum user role:** viewer

By default, commands displayed in the CLI do not show a timestamp. To turn on timestamp so that each entered command will be displayed with a timestamp:

**Command syntax: set cli-timestamp**
**Command syntax: unset cli-timestamp**

**Command mode:** operational

**Example**
::

	dnRouter# set cli-timestamp
	
	dnRouter(cfg 08-Aug-2017-17:16:08)# show system version
	
	System Name: dnRouter
	Version: DNOS [4.1]
	
	dnRouter(08-Aug-2017-17:16:08)# show system version
	
	System Name: dnRouter
	Version: DNOS [4.1]
	
	dnRouter(cfg 08-Aug-2017-17:16:08)# system name my_name
	my_name(cfg)#	

**Removing Configuration**

To disable the CLI timestamp:
::

	dnRouter# unset cli-timestamp


.. **Help line:** Set timestamp to the CLI prompt

**Command History**

+-------------+----------------------------------------------+
|             |                                              |
| Release     | Modification                                 |
+=============+==============================================+
|             |                                              |
| 5.1.0       | Command introduced                           |
+-------------+----------------------------------------------+
|             |                                              |
| 6.0         | Changed from run command to set command      |
+-------------+----------------------------------------------+
|             |                                              |
| 10.0        | Changed the syntax from disabled to unset    |
+-------------+----------------------------------------------+
| 25.2        | Command syntax change                        |
+-------------+----------------------------------------------+
---

## set clock lockout.rst

set clock lockout
-----------------

**Minimum user role:** admin

Support set/unset lockout of one of the clock reference source interfaces.

It is possible to temporarily remove a timing source as available synchronization source for the selection process. This is controlled by the lockout commands.

Lockout commands are accepted for synchronization sources that are not disabled of each selection process.

NOTE: A locked out source is still nominated to the selection process and retains its synchronization source priority but no longer considered available for selection.

The unset lockout command causes this input to be considered available again by the selection process.

When performing a clock lockout, you will be prompted to confirm the request. After the request is confirmed, the system will perform the change.

In case the source is already locked-out or the interface is not part of defined input sources, the command should not take any affect.

To set a clock reference source as locked-out:

**Command syntax: set clock lockout {ncp [ncp-id]} interface [interface-name]**
**Command syntax: unset clock lockout {ncp [ncp-id]} interface [interface-name]**

**Command mode:** operational

**Note**

- This command is only applicable to NCP nodes.


**Parameter table**

+------------------+----------------------------------------------------------------------+---------------------------------+
|                  |                                                                      |                                 |
| Parameter        | Description                                                          | Range                           |
+==================+======================================================================+=================================+
| ncp-id           | The unique id of the node whose ref. source you want locked out.     | NCP: 0..191                     |
+------------------+----------------------------------------------------------------------+---------------------------------+
| interface-name   | Reference source interface name                                      | ge<interface speed>-<A>/<B>/<C> |
|                  |                                                                      | smb-10mhz                       |
+------------------+----------------------------------------------------------------------+---------------------------------+

**Example**
::

	dnRouter# set clock lockout ncp 0 interface ge400-0/0/0

	dnRouter# set clock lockout ncp 0 interface smb-10mhz

	dnRouter# set clock lockout ncp 0 interface ge400-0/0/1
	ERROR: Unknown word: 'ge400-0/0/1'.

**Removing Configuration**

To clear the interface lockout state:
::

	dnRouter# unset clock lockout ncp 0 interface ge400-0/0/0

.. **Help line:** clock reference source lockout and clear command support

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 17.2        | Command introduced    |
+-------------+-----------------------+
| 25.2        | Command syntax change |
+-------------+-----------------------+
---

## set commands overview.rst


Set Commands Overview
----------------------
The following set commands are available:

+----------------------+---------------------------------------------------------------------+--------------------------+
| Command              | Description                                                         | Reference                |
+----------------------+---------------------------------------------------------------------+--------------------------+
| cli-timestamp        | Turn on timestamp for commands                                      | set cli-timestamp        |
+----------------------+---------------------------------------------------------------------+--------------------------+
| debug                | Enables non-persistent debug logging                                | Debug Commands           |
+----------------------+---------------------------------------------------------------------+--------------------------+
| interfaces led-flash | Causes an interface's LED to blink                                  | set interfaces led-flash |
+----------------------+---------------------------------------------------------------------+--------------------------+
| logging terminal     | Sends non-persistent system-events to the terminal (console or ssh) | set logging terminal     |
+----------------------+---------------------------------------------------------------------+--------------------------+
| system datetime      | Manually set the system clock                                       | set system datetime      |
+----------------------+---------------------------------------------------------------------+--------------------------+
| system led-flash     | Causes all the cluster interfaces' LEDs (or per node) to blink      | set system led-flash     |
+----------------------+---------------------------------------------------------------------+--------------------------+

---

## set evpn mac-suppression.rst

set evpn mac-suppression
------------------------

**Minimum user role:** operator

To set suppression on a mac-address of an evpn service instance:

**Command syntax: set evpn mac-suppression** service [instance-name] mac [mac-address]

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

	dnRouter# set evpn mac-suppression service evpn1 mac  a2:76:b0:08:9e:02


.. **Help line:**

**Command History**

+---------+---------------------------------------------------+
| Release | Modification                                      |
+=========+===================================================+
| 18.3    | Command introduced                                |
+---------+---------------------------------------------------+

---

## set interfaces led-flash.rst

set interfaces led-flash
------------------------

**Minimum user role:** viewer

When working with a large setup with many interfaces, you may need help in locating the interface that you are configuring in the physical rack. Setting led-flash will cause the LED on the physical port to light.

To enable the LED flash on a physical port:


**Command syntax: set interfaces led-flash [interface-name]**
**Command syntax: unset interfaces led-flash [interface-name]**

**Command mode:** operational

**Note**

- The command is applicable to physical interfaces.


**Parameter table**

+-------------------+------------------------------------------------------------------------------+---------------------------------+
|                   |                                                                              |                                 |
| Parameter         | Description                                                                  | Range                           |
+===================+==============================================================================+=================================+
|                   |                                                                              |                                 |
| interface-name    | Specify the name of the physical interface whose   LED you want lit.         | ge<interface speed>-<A>/<B>/<C> |
|                   |                                                                              |                                 |
|                   | If you do not specify an interface, all cluster   interfaces will be lit.    | fab-ncpX-Y/Z/W                  |
|                   |                                                                              |                                 |
|                   |                                                                              | fab-ncfX-Y/Z/W                  |
+-------------------+------------------------------------------------------------------------------+---------------------------------+

**Example**
::

	dnRouter# set interfaces led-flash ge100-1/0/2


**Removing Configuration**

To turn off the LEDs lit by led-flash:
::

	dnRouter# unset interfaces led-flash ge100-1/0/2


.. **Help line:** interfaces led-flash

**Command History**

+-------------+------------------------------------------------+
|             |                                                |
| Release     | Modification                                   |
+=============+================================================+
|             |                                                |
| 6.0         | Command introduced                             |
+-------------+------------------------------------------------+
|             |                                                |
| 7.0         | Moved command from request mode to set mode    |
+-------------+------------------------------------------------+
|             |                                                |
| 9.0         | Command not supported                          |
+-------------+------------------------------------------------+
|             |                                                |
| 11.2        | Command reintroduced                           |
+-------------+------------------------------------------------+
| 25.2        | Command syntax change                          |
+-------------+------------------------------------------------+
---

## set logging terminal.rst

set logging terminal 
--------------------

**Minimum user role:** viewer

To send non-persistent system-events to the terminal (console or ssh):

**Command syntax: set logging terminal**
**Command syntax: unset logging terminal**

**Command mode:** operational

**Example**
::

	dnRouter# 
	dnRouter# set logging terminal

**Removing Configuration**

To stop sending the events to the terminal:
::

	dnRouter# unset logging terminal


.. **Help line:** Set non persistent system-events messages to the terminal (console or ssh)

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 11.0        | Command introduced    |
+-------------+-----------------------+
| 25.2        | Command syntax change |
+-------------+-----------------------+
---

## set mgmt dnor-server.rst

set mgmt dnor-server
--------------------

**Command syntax: set mgmt dnor-server [address-list]**

**Description:** Configures DNOR servers IP/FQDN.


**CLI example:**
::

	dnRouter# set mgmt dnor-server 172.16.45.23

	dnRouter# set mgmt dnor-server 172.16.45.23,172.16.45.24,72.16.45.23

	dnRouter# set mgmt dnor-server dnor1.mydomain.com,dnor2.mydomain.com


		
**Command mode:** operational

**Note:**

-  if DHCP/DHCPv6 is enabled on the whitebox mgmt interface, whitebox may get additional DNOR address in DHCP option 66 or DHCPv6 option 59.

**Help line:** Configure DNOR servers.

**Parameter table:**

+----------------------+---------------------------------------------+---------------+
| Parameter            | Values                                      | Default value |
+======================+=============================================+===============+
| address-list         | list of up to 3 FQDNs or ipv4/ipv6          |               |
|                      |                                             |               | 
|                      | addresses, separated by comma               |               |
+----------------------+---------------------------------------------+---------------+

**Command History**

+-------------+----------------------------------------------+
|             |                                              |
| Release     | Modification                                 |
+=============+==============================================+
|             |                                              |
| 16.1        | Command introduced                           |
+-------------+----------------------------------------------+
| 19.1        | Added IPv6 support                           |
+-------------+----------------------------------------------+

---

## set rsvp auto-bandwidth sample.rst

set rsvp auto-bandwidth sample
----------------------------------

**Minimum user role:** operator

Manually set the average-traffic-rate value, which is sampled by the tunnel on every auto-bandwidth sampling-interval. Upon the requested sampled value all auto-bandwidth logic will apply. The tunnel for which average-traffic-rate sample will be modified can be specified. The sampled average-traffic-rate will remain the requested value until running the "unset rsvp auto-bandwidth sample" command or until the rsvp process restarts.

To set the rsvp auto-bandwidth tunnel:

**Command syntax: set rsvp auto-bandwidth sample tunnel [tunnel-name] bandwidth [bandwidth]**
**Command syntax: unset rsvp auto-bandwidth sample {tunnel [tunnel-name]}**

**Command mode:** operational

**Parameter table**

+-------------+----------------------------------+----------------+
| Parameter   | Description                      | Range          |
+=============+==================================+================+
| tunnel-name | The name of the specific tunnel  | string         |
+-------------+----------------------------------+----------------+
| bandwidth   | The set bandwidth for the tunnel | 0..42949672950 |
+-------------+----------------------------------+----------------+

**Example**
::

	dnRouter# set rsvp auto-bandwidth sample tunnel TUNNEL_A bandwidth 500000


**Removing Configuration**

To clear the average-rate traffic for all tunnels:
::

	dnRouter# unset rsvp auto-bandwidth sample

To clear the average-rate traffic for a specific tunnel:
::

	dnRouter# unset rsvp auto-bandwidth sample tunnel TUNNEL_A

.. **Help line:**

**Command History**

+-------------+------------------------+
|             |                        |
| Release     | Modification           |
+=============+========================+
|             |                        |
| 13.2        | Command introduced     |
+-------------+------------------------+
| 18.2.5      | Bandwidth range update |
+-------------+------------------------+
| 25.2        | Command syntax change  |
+-------------+------------------------+
---

## set system datetime.rst

set system datetime
-------------------

**Minimum user role:** viewer

To manually set the clock to the correct time, use the set system datetime command. You can set the current date and the time of day, as follows:

**Command syntax: set system datetime** [datetime]

**Command mode:** operational

**Note**

- Make sure that system timing mode is set to "manual" to disable the NTP functionality. See "system timing-mode".

..
	**Internal Note**

	- Validation:

	If system timing-mode is set to "ntp", set system datetime command is rejected and the following message is presented:

	"Timing mode is set to NTP, local time setting is unavailable".

**Parameter table**

+---------------+-------------------------------------------------------------------------------------+------------------------------+
|               |                                                                                     |                              |
| Parameter     | Description                                                                         | Range                        |
+===============+=====================================================================================+==============================+
|               |                                                                                     |                              |
| datetime      | Sets the system local time of day. You can optionally   set a millisecond value.    | dd-mm-yyyyThh:mm:ss[.sss]    |
+---------------+-------------------------------------------------------------------------------------+------------------------------+

**Example**
::

	dnRouter# set system datetime 2017-11-13T17:59:59

	dnRouter# set system datetime 2017-11-13T17:59:59.999
	Timing mode is set to NTP, manual time setting is unavailable.

.. **Help line:** Set manual system datetime

**Command History**

+-------------+----------------------------------------------+
|             |                                              |
| Release     | Modification                                 |
+=============+==============================================+
|             |                                              |
| 5.1.0       | Command introduced                           |
+-------------+----------------------------------------------+
|             |                                              |
| 6.0         | Changed   from run command to set command    |
+-------------+----------------------------------------------+
---

## set system led-flash.rst

set system led-flash
--------------------

**Minimum user role:** viewer

When working with large setups with many elements, you may need help in locating a specific machine. Setting the led-flash will cause all of the port LEDs on the specified element to blink.

To locate a machine using the LED-flash:

**Command syntax: set system led-flash** [node-name] [node-id]
**Command syntax: unset system led-flash** [node-name] [node-id]

**Command mode:** operational

**Note**

- This command is not applicable to NCC and NCM.

- If you do not specify an NCE, the LEDs of all the cluster's NCP and NCF will blink.

**Parameter table**

+---------------+----------------------------------------------------------------------+---------------+
| Parameter     | Description                                                          | Range         |
+===============+======================================================================+===============+
| node-name     | Specify the NCE whose port LEDs you want lit.                        | NCP           |
|               |                                                                      | NCF           |
|               |                                                                      | NCM           |
+---------------+----------------------------------------------------------------------+---------------+
| node-id       | The unique identifier of the node whose port LEDs   you want lit.    | NCP: 0..191   |
|               |                                                                      | NCF: 0..12    |
|               |                                                                      | NCM: a0,b0    |
+---------------+----------------------------------------------------------------------+---------------+

**Example**
::

	dnRouter# set system led-flash
	dnRouter# set system led-flash ncp 0
	dnRouter# set system led-flash ncf 1
	dnRouter# set system led-flash ncm a0

**Removing Configuration**

To stop the blinking on all nodes:
::

	dnRouter# unset system led-flash

To stop the blinking on a specific node:
::

	dnRouter# unset system led-flash ncp 0


.. **Help line:** interface led-flash

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 11.0        | Command introduced    |
+-------------+-----------------------+
| 25.1        | NCM nodes support     |
+-------------+-----------------------+
| 25.2        | Command syntax change |
+-------------+-----------------------+
---

## set system-type.rst

set system-type
---------------

**Minimum user role:** viewer

Set the NC-AI cluster formation with which the node is associated. To configure the NC-AI node system-type:

**Command syntax: set system-type [system-type]**

**Command mode:** operational

.. **Note**

**Example**
::

	dnRouter# set system-type CL-AI-8K-400G

**Parameter table:**

.. **Help line:** Configure nc-ai node system-type.

+-------------+-------------------------------------------+-----------+---------+
|   Parameter | Description                               |     Range | Default |
+=============+===========================================+===========+=========+
| system-type | The cluster type the node is associated.  | \-        | \-      |
+-------------+-------------------------------------------+-----------+---------+

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 19.10   | Command introduced                  |
+---------+-------------------------------------+

---


---

# SECTION 6: GI MODE COMMANDS

Files from GI Mode Commands folder:       43 files

## request interfaces management description.rst

request interface management description
-------------------------------------------------------------------

**Minimum user role:** operator


To set a textual interface description for the management physical interfaces:


**Command syntax: request interfaces management [interface-name] description [description]**

**Command mode:** GI

.. **Note:**


**Parameter table:**

+------------------+----------------------------------------------------------------------------------+---------------+---------+
| Parameter        | Values                                                                           | Range         | Default |
+==================+==================================================================================+===============+=========+
| interface-name   | mgmt-ncc-0, mgmt-ncc-1, mgmt-ncc-0/0, mgmt-ncc-0/1, mgmt-ncc-1/0, mgmt-ncc-1/1   |               | \-      |
+------------------+----------------------------------------------------------------------------------+---------------+---------+


**Example:**
::

	dnRouter# request interfaces management mgmt-ncc-0 description MyInterfaceDescription


.. **Help line:** Set interface  description for management physical or management bond interface


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 16.2        | Command introduced    |
+-------------+-----------------------+

---

## request interfaces management disable.rst

request interface management disable
-------------------------------------------------------------------

**Minimum user role:** operator


To disable the management physical or management bond interface:


**Command syntax: request interfaces management [interface-name] disable**

**Command mode:** GI

.. **Note:**


**Parameter table:**

+------------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter        | Values                                                                           | Range   | Default |
+==================+==================================================================================+=========+=========+
| interface-name   | mgmt-ncc-0, mgmt-ncc-1, mgmt-ncc-0/0, mgmt-ncc-0/1, mgmt-ncc-1/0, mgmt-ncc-1/1   |         | \-      |
+------------------+----------------------------------------------------------------------------------+---------+---------+


**Example:**
::

	dnRouter# request interfaces management mgmt-ncc-0 disable


.. **Help line:** Disabling management physical or management bond interface


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 16.2        | Command introduced    |
+-------------+-----------------------+

---

## request interfaces management enable.rst

request interface management enable
-------------------------------------------------------------------

**Minimum user role:** operator


To enable the management physical or management bond interface:


**Command syntax: request interfaces management [interface-name] enable**

**Command mode:** GI

.. **Note:**


**Parameter table:**

+------------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter        | Values                                                                           | Range | Default |
+==================+==================================================================================+=======+=========+
| interface-name   | mgmt-ncc-0, mgmt-ncc-1, mgmt-ncc-0/0, mgmt-ncc-0/1, mgmt-ncc-1/0, mgmt-ncc-1/1   |       | \-      |
+------------------+----------------------------------------------------------------------------------+-------+---------+


**Example:**
::

	dnRouter# request interfaces management mgmt-ncc-0 enable


.. **Help line:** Disabling management physical or management bond interface


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 16.2        | Command introduced    |
+-------------+-----------------------+

---

## request interfaces management ipv4-address.rst

request interface management ipv4-address
-------------------------------------------------------------------

**Minimum user role:** operator


To configure the ipv4-address on the management bond interface:


**Command syntax: request interfaces management [interface-name] ipv4-address {[ipv4-address] \| dhcp}**

**Command mode:** GI

.. **Note:**


**Parameter table:**

+------------------+----------------------------------------------+-------+---------+
| Parameter        | Values                                       | Range | Default |
+==================+==============================================+=======+=========+
| interface-name   | mgmt-ncc-0, mgmt-ncc-1                       |       | \-      |
+------------------+----------------------------------------------+-------+---------+
| ipv4-address     | A.B.C.D/X                                    |       | \-      |
+------------------+----------------------------------------------+-------+---------+


**Example:**
::

	dnRouter# request interfaces management mgmt-ncc-0 ipv4-address 1.2.3.4/32
	dnRouter# request interfaces management mgmt-ncc-0 ipv4-address dhcp
	

.. **Help line:** Configure ipv4-address on management bond interface


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 16.2        | Command introduced    |
+-------------+-----------------------+

---

## request interfaces management ipv6-address.rst

request interface management ipv6-address
-------------------------------------------------------------------

**Minimum user role:** operator


To configure the ipv6-address on the management bond interface:


**Command syntax: request interfaces management [interface-name] ipv6-address {[ipv6-address] \| dhcp}**

**Command mode:** GI

.. **Note:**


**Parameter table:**

+------------------+----------------------------------------------+--------+---------+
| Parameter        | Values                                       | Range  | Default |
+==================+==============================================+========+=========+
| interface-name   | mgmt-ncc-0, mgmt-ncc-1                       |        | \-      |
+------------------+----------------------------------------------+--------+---------+
| ipv6-address     | {ipv6-address format}                        |        | \-      |
+------------------+----------------------------------------------+--------+---------+

**Example:**
::

	dnRouter# request interfaces management mgmt-ncc-0 ipv6-address 2001:ab12::1/127
	dnRouter# request interfaces management mgmt-ncc-0 ipv6-address dhcp


.. **Help line:** Configure ipv6-address on management bond interface


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 16.2        | Command introduced    |
+-------------+-----------------------+

---

## request interfaces management mac-address.rst

request interface management mac-address
-------------------------------------------------------------------

**Minimum user role:** operator


To configure the mac-address on the management bond interface:


**Command syntax: request interfaces management [interface-name] mac-address [mac-address]**

**Command mode:** GI

.. **Note:**


**Parameter table:**

+------------------+----------------------------------------------+--------+---------+
| Parameter        | Values                                       | Range  | Default |
+==================+==============================================+========+=========+
| interface-name   | mgmt-ncc-0, mgmt-ncc-1                       |        | \-      |
+------------------+----------------------------------------------+--------+---------+
| mac-address      | xx:xx:xx:xx:xx:xx                            |        | \-      |
+------------------+----------------------------------------------+--------+---------+


**Example:**
::

	dnRouter# request interfaces management mgmt-ncc-0 mac-address 10:22:33:44:55:00
	

.. **Help line:** Configure mac-address on management bond interface


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 16.2        | Command introduced    |
+-------------+-----------------------+

---

## request interfaces management static-route.rst

request interface management static address-family route next-hop
-------------------------------------------------------------------

**Minimum user role:** operator


To configure the static route on the physical management bond interface:


**Command syntax: request interfaces management [interface-name] static address-family [address-family] route** [ip-prefix] next-hop [gateway]**

**Command mode:** GI

.. **Note:**


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

	dnRouter# request interfaces management mgmt-ncc-0 static address-family ipv4 route 1.2.3.4/32 next-hop 4.2.3.1
	

.. **Help line:** Request adding static route on management bond


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 16.2        | Command introduced    |
+-------------+-----------------------+

---

## request system ai-deploy.rst

request system ai-deploy
------------------------

**Minimum user role:** viewer

Deploys AI SA router with provided system type and name.

**Command syntax: request system ai-deploy system-type [system-type] name [name] node-type [node-type] node-id [node-id] ncc-id [ncc-id]** oob-mgmt-ipv4 {dhcp \| [ipv4-address] [ipv4-default-gateway] \| disabled} oob-mgmt-ipv6 {dhcp \| [ipv6-address] [ipv6-default-gateway] \| disabled } gnmi-port [gnmi-port] netconf-port [netconf-port]

**Command mode:** GI

**Note**

 - Supports cluster system-type (CL-AI-X) on NCP/NCF HW node.

 - Auto-generates router's system-id.

 - Auto-generates router's default self-signed TLS certificate for gRPC/gNMI server.

 - As par tof the deployment user must provide 'node-id' matching existing/planned NCP/NCF cabling.

 - oob-mgmt-ipv4  - apply out-of-band management interface ipv4 settings, options are:
    -  dhcp - retrieve ipv4 local address and default-gateway from DHCP server. Default behavior
    -  ipv4-address - statically set the local ipv4 address and subnet. Must be set together with ipv4-default-gateway
    -  ipv4-default-gateway - statically set the default-gateway ipv4 address. Must be set together with ipv4-address
    -  disabled - disable ipv4 connectivity on the out-of-band management interface

 - node-id - Define the requested ID for the NCP/NCF depending on the node-type. The node-id must comply with NCP/NCF connectivity.

 - ncc-id - Define the requested ID for the NCC. only 0 is an available choice for AI deployment

 - oob-mgmt-ipv6  - apply out-of-band management interface ipv6 settings, options are:
    -  dhcp - retrieve ipv6 local address and default-gateway from DHCP server. Default behavior
    -  ipv6-address - statically set the local ipv6 address and subnet. Must be set together with ipv4-default-gateway
    -  ipv6-default-gateway - statically set the default-gateway ipv4 address. Must be set together with ipv6-address
    -  disabled - disable ipv6 connectivity on the out-of-band management interface

 - Validation: the command shall fail in case both oob-mgmt-ipv4 and oob-mgmt-ipv6 are disabled


**Example**
::

	gi# request system ai-deploy system-type CL-AI-8K-400G name SYS_1 node-type ncf node-id 0
	The following software or firmware will be installed:
	   DNOS 18.2.40
	Warning: Do you want to continue? (Yes/No) [No]?

	gi# request system ai-deploy system-type CL-AI-8K-400G name SYS_1 node-type ncp node-id 1 oob-mgmt-ipv4 ipv4-address 5.5.5.2/24 5.5.5.1 oob-mgmt-ipv6 disabled
	The following software or firmware will be installed:
	   DNOS 18.2.40
	Warning: Do you want to continue? (Yes/No) [No]?

    gi# request system ai-deploy system-type CL-AI-8K-400G name SYS_1 node-type ncf node-id 0 oob-mgmt-ipv4 disabled oob-mgmt-ipv6 disabled
    Error: at least one oob-mgmt-ip address configuration shall exist!


.. **Hidden Note:**

 -  Yes/no validation should exist for the operation.


**Parameter table:**

+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
|       Parameter      | Description                                                                |                    Range                   | Default |
+======================+============================================================================+============================================+=========+
| system-type          | The type of NCR                                                            | CL-AI-8K-400G                              | \-      |
|                      |                                                                            | AI-216-800G-2                              |         |
|                      |                                                                            | AI-72-800G-2                               |         |
|                      |                                                                            | AI-2016-800G-2                             |         |
|                      |                                                                            | AI-2304-800G-2                             |         |
|                      |                                                                            | AI-8192-400G-2                             |         |
|                      |                                                                            | AI-768-400G-1                              |         |
|                      |                                                                            | AI-576-800G-2                              |         |
|                      |                                                                            | AI-1152-800G-2                             |         |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| name                 | The name of the system                                                     | string, 1-32 characters                    | \-      |
|                      |                                                                            | allowed characters: alphanumeric, "-", "_" |         |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| oob-mgmt-ipv4        | The ipv4 management address address allocation mode of the system          | dhcp, A.B.C.D/X, disabled                  | dhcp    |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| ipv4-address         | The ipv4 address of the system                                             | A.B.C.D/X                                  | \-      |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| ipv4-default-gateway | The ipv4 default gateway address of the system                             | A.B.C.D                                    | \-      |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| oob-mgmt-ipv6        | The ipv6 management address address allocation mode of the system          | dhcp, {ipv6-address and prefix format},    | dhcp    |
|                      |                                                                            | disabled                                   |         |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| ipv6-address         | The ipv6 address of the system                                             | {ipv6-address and prefix format}           | \-      |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| ipv6-default-gateway | The ipv6 default gateway address of the system                             | {ipv6-address format}                      | \-      |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| node-id              | The ID number of the node, ncp/ncf                                         | NCPs - 0..255                              | \-      |
|                      |                                                                            | NCFs - 0..611                              |         |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| node-type            | The type of the node                                                       | ncp, ncf,                                  | \-      |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| gnmi-port            | The gNMI port the server will listen after deployment                      | 50051, 9339                                | 50051   |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| netconf-port         | The NETCONF port the server will listen after deployment                   | 830, 22                                    | 830     |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+

.. **Help line:** Create DNOS router.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+
| 19.10   | Added support for AI                |
+---------+-------------------------------------+

---

## request system delete.rst

request system delete
---------------------

**Minimum user role:** viewer

Deletes DNOS databases, keys, certificates and logs on the node. To delete a DNOS router on the node:

**Command syntax: request system delete**

**Command mode:** GI

.. **Note**

 - Yes/no validation should exist for the operation.

**Parameter table**


**Example**
::

	gi# request system delete
	DNOS router database, keys and logs will be deleted from this node.
	Warning: Do you want to continue? (Yes/No) [No]?

	Deleting database...
	Deleting files...
	Done.


.. **Help line:** Delete DNOS router

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+

---

## request system deploy.rst

request system deploy
---------------------

**Minimum user role:** viewer

Deploys DNOS router with provided system type and name.

**Command syntax: request system deploy system-type [system-type] name [name] ncc-id [ncc-id]** oob-mgmt-ipv4 {dhcp \| [ipv4-address] [ipv4-default-gateway] \| disabled} oob-mgmt-ipv6 {dhcp \| [ipv6-address] [ipv6-default-gateway] \| disabled } gnmi-port [gnmi-port] netconf-port [netconf-port]

**Command mode:** GI

**Note**

 - Supports stanalone system-type (SA_X) on NCP HW node, cluster system-type (CL_X) on NCC HW node.

 - Auto-generates router's system-id.

 - Auto-generates router's default self-signed TLS certificate for gRPC/gNMI server.

 - For cluster user must provide NCC-ID matching existing/planned NCC cabling towards NCMs (NCC-0 connects to NCM port 48, NCC-1 connects to NCM port 49).

 - oob-mgmt-ipv4  - apply out-of-band management interface ipv4 settings, options are:
    -  dhcp - retrieve ipv4 local address and default-gateway from DHCP server. Default behavior
    -  ipv4-address - statically set the local ipv4 address and subnet. Must be set together with ipv4-default-gateway
    -  ipv4-default-gateway - statically set the default-gateway ipv4 address. Must be set together with ipv4-address
    -  disabled - disable ipv4 connectivity on the out-of-band management interface

 - ncc-id - Define the requested ID for the NCC, either 0 or 1. The ncc-id must comply with NCC connectivity to the NCM.
    ID 0 NCC is connected to NCMs port 48, ID 1 NCC is connected to NCMs port 49.
    When the NCC is not connected to any NCM, user may set either ID 0 or ID 1, which will define the NCC ID once DNOS starts

 - oob-mgmt-ipv6  - apply out-of-band management interface ipv6 settings, options are:
    -  dhcp - retrieve ipv6 local address and default-gateway from DHCP server. Default behavior
    -  ipv6-address - statically set the local ipv6 address and subnet. Must be set together with ipv4-default-gateway
    -  ipv6-default-gateway - statically set the default-gateway ipv4 address. Must be set together with ipv6-address
    -  disabled - disable ipv6 connectivity on the out-of-band management interface

 - Validation: the command shall fail in case both oob-mgmt-ipv4 and oob-mgmt-ipv6 are disabled


**Example**
::

	gi# request system deploy system-type SA-40C name SYS_1 ncc-id 0
	The following software or firmware will be installed:
	   DNOS 17.2
	Warning: Do you want to continue? (Yes/No) [No]?

	gi# request system deploy system-type SA-40C name SYS_1 ncc-id 1 oob-mgmt-ipv4 ipv4-address 5.5.5.2/24 5.5.5.1 oob-mgmt-ipv6 disabled
	The following software or firmware will be installed:
	   DNOS 17.2
	Warning: Do you want to continue? (Yes/No) [No]?

    gi# request request system deploy system-type SA-40C name SYS_1 ncc-id 1 oob-mgmt-ipv4 disabled oob-mgmt-ipv6 disabled
    Error: at least one oob-mgmt-ip address configuration shall exist!


.. **Hidden Note:**

 -  Yes/no validation should exist for the operation.


**Parameter table:**

+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
|       Parameter      | Description                                                                |                    Range                   | Default |
+======================+============================================================================+============================================+=========+
| system-type          | The type of NCR                                                            | SA-40C                                     | \-      |
|                      |                                                                            | SA-10CD                                    |         |
|                      |                                                                            | CL-16                                      |         |
|                      |                                                                            | CL-32                                      |         |
|                      |                                                                            | CL-48                                      |         |
|                      |                                                                            | CL-64                                      |         |
|                      |                                                                            | CL-96                                      |         |
|                      |                                                                            | CL-134                                     |         |
|                      |                                                                            | CL-192                                     |         |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| name                 | The name of the system                                                     | string, 1-32 characters                    | \-      |
|                      |                                                                            | allowed characters: alphanumeric, "-", "_" |         |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| oob-mgmt-ipv4        | The ipv4 management address address allocation mode of the system          | dhcp, A.B.C.D/X, disabled                  | dhcp    |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| ipv4-address         | The ipv4 address of the system                                             | A.B.C.D/X                                  | \-      |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| ipv4-default-gateway | The ipv4 default gateway address of the system                             | A.B.C.D                                    | \-      |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| oob-mgmt-ipv6        | The ipv6 management address address allocation mode of the system          | dhcp, {ipv6-address and prefix format},    | dhcp    |
|                      |                                                                            | disabled                                   |         |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| ipv6-address         | The ipv6 address of the system                                             | {ipv6-address and prefix format}           | \-      |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| ipv6-default-gateway | The ipv6 default gateway address of the system                             | {ipv6-address format}                      | \-      |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| ncc-id               | The ID number of the ncc                                                   | 0,1                                        | \-      |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| gnmi-port            | The gNMI port the server will listen after deployment                      | 50051, 9339                                | 50051   |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+
| netconf-port         | The NETCONF port the server will listen after deployment                   | 830, 22                                    | 830     |
+----------------------+----------------------------------------------------------------------------+--------------------------------------------+---------+

.. **Help line:** Create DNOS router.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+

---

## request system install retry.rst

request system install retry
----------------------------

**Minimum user role:** viewer

To invoke current stack re-installation on a specific node, for all stack packages:

**Command syntax: request system install retry { ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] }**

**Command mode:** GI

**Note**

- In the event of installing a DNOS package on an active NCC, the DNOS in a cluster will continue the update of other HW nodes.

- Shows progress until node reboot or until user presses Ctrl+C which stops the show. The process continues in the background.


**Example**
::

	gi# request system install retry ncc 0
	The following software or firmware will be installed:
	   BaseOS 1.687
	   DNOS 17.2
	Warning: Do you want to continue? (Yes/No) [No]?

	Press Ctrl C to exit progress show, installation will run in background.
	Started target stack installation, task ID = 8.
	Started BaseOS installation on NCC 0, task ID = 81
	Rebooting...

.. **Hidden Note:**

 - Yes/no validation should exist for the operation.


.. **Parameter table:**


.. **Help line:** Reinstall current stack on a specific node

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+

---

## request system ncc repository sync.rst

request system ncc repository sync
----------------------------------------

**Minimum user role:** admin

When the NCCs' repository sync fails, you can retry the sync operation by executing this command.

- If a sync operation is already in progress, the system will display a message indicating that the operation is in progress.

- If the repository is already in sync, the system will display a message indicating that the repository is already in sync.

- If the deployment is a standalone NCC, the system will display a message indicating that the operation is not supported.

- If the root NCC is not stable, the system will display a message indicating that the operation is not applicable.

- If the root NCC's repository is not stable, the system will display a message indicating that the operation is not applicable.

To trigger a repository between the active NCC and the standby NCC:

**Command syntax: request system ncc repository sync**

**Command mode:** operational

..**Note**


**Example**
::

	gi# request system ncc repository sync
	Repository sync started
	gi#

	gi# request system ncc repository sync
	Error: Repository sync is already in progress
	gi#

.. **Help line:** retry repository sync operation

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 19.3    | Command introduced                  |
+---------+-------------------------------------+

---

## request system revert-stack install.rst

request system revert-stack install
-----------------------------------

**Minimum user role:** viewer

Reverts the system software to a version in the revert stack.

**Command syntax: request system revert-stack install**

**Command mode:** GI

**Note**

- Firmware and ONIE are not reverted.

- Not supported when the system is updating or reverting any software.

- Shows progress until node reboot or until the user presses Ctrl+C which stops the show. The process continues in the background.


**Example**
::

	gi# request system revert-stack install
	The system will revert to the following software:
	   NCM NOS 12.1
	   BaseOS 1.687
	   DNOS 17.2
	Warning: Do you want to continue? (Yes/No) [No]?

	Press Ctrl C to exit progress show, installation will run in background.
	Started revert stack installation, task ID = 8.
	Started BaseOS revert on NCC 0, task ID = 81
	Rebooting...

	gi# request system revert-stack install
	The system will revert to the following software:
	   DNOS 17.2
	Warning:  Do you want to continue? (Yes/No) [No]?

	Press Ctrl C to exit progress show, installation will run in background.
	Started revert stack installation, task ID = 8.
	Started DNOS deployment on NCC 0, task ID = 81
	Finished DNOS deployment on NCC 0, task ID = 81
	Entering DNOS mode.

	gi# request system revert-stack install
	The system will revert to the following software:
	   OS Packages 1.100
	Warning: Installing the downloaded packages requires performing a system restart.
	         Do you want to continue? (Yes/No) [No]?

.. **Hidden Note:**

 - Yes/no validation should exist for the operation.


.. **Parameter table:**


.. **Help line:** Revert system software to versions in the revert stack.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+

---

## request system target-stack clear.rst

request system target-stack clear
---------------------------------

**Minimum user role:** viewer

Reverts all software/firmware from the target stack.

**Command syntax: request system target-stack clear**

**Command mode:** GI

**Note**

- Not supported when the system is upgrading or reverting.

- Not supported when the target stack is modified.


**Example**
::

	gi# request system target-stack clear
	Warning: Are you sure you want to remove all the software from the target stack? (Yes/No) [No]?

	# Removed all software from the target stack
	gi#


.. **Hidden Note:**

 -  Yes/no validation should exist for the operation.


.. **Parameter table:**


.. **Help line:** Clear target-stack.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+

---

## request system target-stack install.rst

request system target-stack install
-----------------------------------

**Minimum user role:** viewer

Updates the system software/firmware to versions in the target stack.

**Command syntax: request system target-stack install**

**Command mode:** GI

**Note**

- Updates DNOS, BaseOS, GI, ONIE, OS packages and firmware on the node.

- Starts DNOS which in cluster should continue update of other HW nodes.

- Not supported if the update would violate any version dependency, e.g. if target DNOS cannot run on target BaseOS, or if there is no target BaseOS and target GI image cannot run on current BaseOS.

- Not supported when the system is updating or reverting any software.

- Not supported when the system is changing target stack.

- Shows progress until node reboot or until user presses Ctrl C which stops the show. The process continues in background.


**Example**
::

	gi# request system target-stack install
	The following software or firmware will be installed:
	   Firmware:
	   	HW platform: S9700-53DX, revision 1, version 4.5
	   	HW platform: S9700-23DJ, revision 2, version 4.6-ab
	   NCM NOS 12.1
	   BaseOS 1.687
	   DNOS 17.2
	Warning: Do you want to continue? (Yes/No) [No]?

	Press Ctrl C to exit progress show, installation will run in background.
	Started target stack installation, task ID = 8.
	Started BaseOS installation on NCC 0, task ID = 81
	Rebooting...

	gi# request system target-stack install
	The following software or firmware will be installed:
	   DNOS 17.2
	Warning: Do you want to continue? (Yes/No) [No]?

	Press Ctrl C to exit progress show, installation will run in background.
	Started target stack installation, task ID = 8.
	Started DNOS deployment on NCC 0, task ID = 81
	Finished DNOS deployment on NCC 0, task ID = 81
	Entering DNOS mode.

	gi# request system target-stack install
	The following software or firmware will be installed:
	   OS Packages 1.200
	Warning: Installing the downloaded packages requires performing a system restart.
	         Do you want to continue? (Yes/No) [No]?

.. **Hidden Note:**

 - Yes/no validation should exist for the operation.


.. **Parameter table:**


.. **Help line:** Install target stack on the system.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+

---

## request system target-stack load.rst

request system target-stack load
--------------------------------

**Minimum user role:** viewer

Loads a package via a HTTP(s) GET from a remote location and adds it to the target stack.

A Package can contain software of one of the following types, or it can be a bundle of a few such packages:

- DNOS

- BaseOS

- NCM NOS

- Firmware for specific HW models and revisions

- ONIE image for specific HW model and revision

- GI image

- OS packages

**Command syntax: request system target-stack load url** hardware-model [hw-model] hardware-revision [hw-revision]

**Command mode:** GI

**Note**

- User input must start with "http://" to invoke HTTP GET

 - If the user enters url without the expected "http://",  an error message is displayed: "ERROR: Unknown word: <url>"
 - If http fails to connect, an error message is displayed: "ERROR: The connection has timed out"

-  Yes/no validation should exist for the operation.

-  If a node connects, the system syncs the target stack to the node (only software which is relevant to the node type and HW)

**Example**
::

 gi# request system target-stack load http://172.16.100.12/packages/drivenets_stratax_1.1.0.tar

	Package http://172.16.100.12/packages/drivenets_stratax_1.1.0.tar will be downloaded and added to target stack.
	Warning: Do you want to continue? (Yes/No) [No]?
	started target-stack load NCC 0, task ID = 99

	Press Ctrl C to exit progress show, operation will run in background.
	Download in progress ...
	Download finished...
	Added NCM NOS version 1.1.0 to target stack.


.. **Hidden Note:**

 - After a package is untared, the package metadata is inspected to understand which software it contains.

 - For firmware and ONIE packages a user may set the intended HW model and revision instead of those specified in the package metadata. Revision may be "default", meaning all the revisions of this HW model for which no package is set explicitly. For other package types, HW model/revision parameters are ignored.

 - The command will fail if a bundle package contains multiple packages of the same type.

 - Each package replaces a previous package of the same type in the target stack, if exists.

 - Verifies Drivenets signature on a package.

 - If firmware package was delivered directly by the HW vendor without Drivenets signature, a user may provide MD5 hash for verification; otherwise the package won't be verified. It's highly recommended to provide a hash received from the HW vendor to ensure package integrity and authenticity. Installing an unverified package may compromise system security. Corrupted firmware may cause HW malfunction.

 - In a cluster, the active NCC replicates the target stack to the standby NCC.

 - In a cluster, the active NCC syncs the target stack to all the connected nodes - copies DNOS, BaseOS, GI images to all the NCP/NCF nodes, NCM NOS to all the NCMs, firmware and ONIE to all the nodes of the HW model/revision set for the package.

 - Not supported when the system is upgrading or reverting.

 - Not supported when the system is changing target stack.

 - Shows progress. Pressing Ctrl+C stops the show and returns prompt, the process continues in background.


**Parameter table:**

+-------------+-------------------------------------------------+--------------------------------+---------+
|  Parameter  | Description                                     |              Range             | Default |
+=============+=================================================+================================+=========+
| url         | The URL of the package                          | Will start with http:// prefix | /-      |
+-------------+-------------------------------------------------+--------------------------------+---------+
| hw-model    | The hardware model for ONIE/firmware package    |                                | /-      |
+-------------+-------------------------------------------------+--------------------------------+---------+
| hw-revision | The hardware revision for ONIE/firmware package |                                | default |
+-------------+-------------------------------------------------+--------------------------------+---------+

.. **Help line:** Load software/firmware to target stack.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+
| 25.1    | Remove file load option             |
+---------+-------------------------------------+
---

## request system target-stack remove.rst

request system target-stack remove
----------------------------------

**Minimum user role:** admin

Removes packages from the target stack.

- Deletes DNOS, BaseOS, NCM NOS, GI or OS update package from the target stack for all node types in a cluster

- For ONIE and firmware package, deletes target stack entries with the specified HW model/revision. Deletes the package from matching HW nodes.
 	- If HW model not specified, deletes all existing ONIE/firmware packages in target stack
	- If HW revision not specified, deletes all matching HW model ONIE/firmware packages existing in target stack

- Not supported when the system is upgrading or reverting.

- Not supported when the system is changing target stack.

- Asynchronous, shows progress.

**Command syntax: request system target-stack remove {dnos \| baseos \| ncm-nos \| gi  \| os-packages \| { {onie \| firmware}** {hardware-model [hw-model] | hardware-model [hw-model] hardware-revision [hw-revision]} }


**Command mode:** GI


**Example**
::

    dnRouter# request system target-stack remove ncm-nos
	NCM-NOS 12.1 package will be removed from target stack.
	Warning: Do you want to continue? (Yes/No) [No]?
	Removed NCM NOS package from target stack

	dnRouter# request system target-stack remove firmware hardware-model S9700-53DX hardware-revision 4
	Firmware for HW model S9700-53DX revision 4 will be removed from target stack
	Warning: Do you want to continue? (Yes/No) [No]?
	Removed firmware package for S9700-53DX revision 4 from target stack


**Note:**

-  Yes/no validation should exist for the operation.

.. **Help line:** Remove package from target stack.


**Parameter table:**

+----------------------+------------------------------------------+----------------------------------------------+---------------+
| Parameter            | Description                              |  Values                                      | Default value |
+======================+==========================================+==============================================+===============+
| hw-model             | The Hardware model                       |                                              | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+
| hw-revision          | The Hardware revision                    |                                              | \-            |
+----------------------+------------------------------------------+----------------------------------------------+---------------+

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 16.1        | Command introduced    |
+-------------+-----------------------+
---

## request system target-stack reset.rst

request system target-stack reset
---------------------------------

**Minimum user role:** viewer

Resets all the software/firmware from the target stack.

**Command syntax: request system target-stack reset**

**Command mode:** GI

**Note**

- Not supported when the target stack is modified.


**Example**
::

	gi# request system target-stack reset
	Warning: Are you sure you want to reset all the software from the target stack? (Yes/No) [No]?

	# Reset all software from the target stack to match the current stack
	gi#


.. **Hidden Note:**

 -  Yes/no validation should exist for the operation.


.. **Parameter table:**


.. **Help line:** Reset target-stack.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 18.2.1    | Command introduced                |
+---------+-------------------------------------+
---

## request system tech-support.rst

request system tech-support
---------------------------

**Minimum user role:** operator

You can generate a file with all the logs, configuration, database files and system output commands that you can save for later use (for example, when opening a customer support case).

After running the command, you will regain full CLI control while the system is generating the tech-support file in the background.

The system can handle only one request to generate a tech-support file at a time. If the system is already creating a tech-support file while you enter another request, an error message will be displayed.

To generate the tech-support file:

**Command syntax: request system tech-support [file-name]** {ncc [ncc-id] \| ncp [ncp-id] \| ncf [ncf-id] \| ncm [ncm-id]} after [after-time] before [before-time] password force include {[info-type], [info-type], ...}

**Command mode:** GI

**Note**

- By default, generate tech-support with information from the last 24 hours for rotated logs (end with .1, .2, date, etc.) and always include the latest version of the main logs (logs that are currently being written to) regardless if they were modified in the past 24 hours.

- The Tech-support files are generated on the active NCC node at /techsupport/ Only one file is stored at a time.

- When you generate a tech-support file, a previous file will be deleted to make room for the new file.

.. - User gets back cli prompt after invoking "request system tech-support" user have full CLI support while techsupport is being generated in the background.

	- Tech-support files are generated on active NCC node at /techsupport/

	- tech-support files are generated with user provided filename_HH:MM:SS_DD-MM-YY.tar

	- extended - generate tech-support with core files from both NCCs and all NCPs (under /core)

	- ncp-id - generate tech-support from NCCs and specific NCP only.

	- Only single techsupport request can be handled by DNOS at the same moment. If another request is given while a different tech-support file is currently created, the following message will be displayed "Cannot produce a new techsupport file, another process is already running"

	- Only single techsupport file can be stored at /techsupport at a given moment. Generation of new techsupport file will require deletion of old file.

**Parameter table**

+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| Parameter   | Description                                                                                                                                                                                                                            | Range                                                                                        | Default       |
+=============+========================================================================================================================================================================================================================================+==============================================================================================+===============+
| file-name   | Provide a name for the file.                                                                                                                                                                                                           | \-                                                                                           | \-            |
|             | A date suffix is added to the user provided name: _HH:MM:SS_DD-MM-YY.tar                                                                                                                                                               |                                                                                              |               |
|             | A prefix is also added  `ts_`                                                                                                                                                                                                          |                                                                                              |               |
|             | The file_name:                                                                                                                                                                                                                         |                                                                                              |               |
|             | - Starts with an alphanumeric character                                                                                                                                                                                                |                                                                                              |               |
|             | - Has a total length of at least 2 characters                                                                                                                                                                                          |                                                                                              |               |
|             | - Have a maximum total length of 228 characters (1 + 227).                                                                                                                                                                             |                                                                                              |               |
|             | - Only contain letters, digits, dots, underscores, or hyphens.                                                                                                                                                                         |                                                                                              |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| password    | Generates the tech-support file with passwords. By default, passwords are removed from the output.                                                                                                                                     | \-                                                                                           | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| force       | Automatically delete a previous tech-support file. By default, you will be prompted to choose whether to delete a previous tech-support file in order to complete the generation of the tech-support file, or to cancel the operation. | \-                                                                                           | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncc-id      | Generate the tech-support file with information from the specified NCC only.                                                                                                                                                           | 0..1                                                                                         | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncp-id      | Generate the tech-support file with information from the specified NCP only.                                                                                                                                                           | 0..47                                                                                        | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncf-id      | Generate the tech-support file with information from the specified NCF only.                                                                                                                                                           | 0..12                                                                                        | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| ncm-id      | Generate the tech-support file with information from specific NCCs , NCMs, and NCPs.                                                                                                                                                   | 0A, 0B, 1A, 1B                                                                               | \-            |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| info-type   | Specifies the type of files to be included ion tech-support info                                                                                                                                                                       | basic - include all textual log files                                                        |               |
|             |                                                                                                                                                                                                                                        | core-dumps - process binary core dump files (not included by default)                        |               |
|             |                                                                                                                                                                                                                                        | journal-files - binary output of Active NCC Base-OS journal files (not included by default). |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| before-time | The tech-support file will only include information generated before the specified time.                                                                                                                                               | yyyy-mm-ddThh:mm:ss[.sss]                                                                    | Last 24 hours |
|             | Can be used in combination with "after" to create a range of dates.                                                                                                                                                                    |                                                                                              |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+
| after-time  | The tech-support file will only include information generated after the specified time.                                                                                                                                                | yyyy-mm-ddThh:mm:ss[.sss]                                                                    | Last 24 hours |
|             | Can be used in combination with "before" to create a range of dates.                                                                                                                                                                   |                                                                                              |               |
+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------+

**Example**
::

	gi# request system tech-support MyTechSupportFile
	13:32:00_30-01-2018 System is generating a Tech-support file
	gi#

	GI# Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar

	gi# request system tech-support MyTechSupportFile include core-dumps
	13:32:00_30-01-2018 System is generating Tech-support file
	gi#
	GI# Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar

	gi# request system tech-support MyTechSupportFile include basic, core-dumps
	13:32:00_30-01-2018 System is generating Tech-support file
	gi#
	GI# Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar

	gi# request system tech-support MyTechSupportFile ncc-all
	13:32:00_30-01-2018 System is generating Tech-support file
	gi#
	GI# Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar

	gi# request system tech-support MyTechSupportFile ncc 0 after 2020-01-02T07:35:00 force
	13:32:00_30-01-2018 System is generating Tech-support file
	gi#
	GI# Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar

	gi# request system tech-support MyTechSupportFile
	Warning: Previous techsupport files exist. Are you sure you want to erase?  (Yes/No) [No]? Yes
	GI# Tech-support request: Done: /techsupport/ts_MyTechSupportFile_13_35_07_30-01-2018.tar

**Command History**

+---------+---------------------------------------------------------------------------------------------------------------------------------+
| Release | Modification                                                                                                                    |
+=========+=================================================================================================================================+
| 16.1    | Command introduced                                                                                                              |
+---------+---------------------------------------------------------------------------------------------------------------------------------+

---

## request system ztp start.rst

request system ztp start
------------------------

**Minimum user role:** viewer

To start the Zero Touch Provisioning (ZTP) process in case the ZTP was previously stopped by the user, use the following command:

**Command syntax:** request system ztp start

**Command mode:** GI

**Note**

- If ZTP is already running, executing this command will have no effect.
- In case the ZTP process is stopped, the ZTP process will immediately restart after executing this command.
- In case ZTP already completed, the ZTP process will not restart.
- At the time these commands are introduced, the output is the same for each case and does not vary according to the actual state.

**Example**
::

	gi# request system ztp start
	Warning: Are you sure you want to start ztp process? (Yes/No) [No]? Yes
	Attempting to start ZTP procedure

.. **Hidden Note:**

 - Yes/no validation should exist for the operation.


.. **Parameter table:**


.. **Help line:**

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 19.3    | Command introduced                  |
+---------+-------------------------------------+

---

## request system ztp stop.rst

request system ztp stop
-----------------------

**Minimum user role:** viewer

To stop the Zero Touch Provisioning (ZTP) process, use the following command:

**Command syntax:** request system ztp stop

**Command mode:** GI

**Note**

- If ZTP is already stopped, executing this command will have no effect.
- In case the ZTP process is active, the ZTP process will stop after completing the current task.
- At the time these commands are introduced, the output is the same for each case and does not vary according to the actual state.

**Example**
::

	gi# request system ztp stop
	Warning: Are you sure you want to stop ztp process? (Yes/No) [No]? Yes
	Attempting to stop ZTP procedure

.. **Hidden Note:**

 - Yes/no validation should exist for the operation.


.. **Parameter table:**


.. **Help line:**

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 19.3    | Command introduced                  |
+---------+-------------------------------------+

---

## request system ztp terminate.rst

request system ztp terminate
----------------------------

**Minimum user role:** viewer

To terminate the Zero Touch Provisioning (ZTP) process, use the following command:

**Command syntax:** request system ztp terminate

**Command mode:** GI

**Note**

- Once the ZTP process is terminated, The user wont be able to rerun ZTP without request system delete
- In case ZTP already terminated or completed, the command will have no effect.
- At the time these commands are introduced, the output is the same for each case and does not vary according to the actual state.

**Example**
::

	gi# request system ztp terminate
	Warning: Are you sure you want to terminate ztp process? (Yes/No) [No]? Yes
	Attempting to terminate ZTP procedure

.. **Hidden Note:**

 - Yes/no validation should exist for the operation.


.. **Parameter table:**


.. **Help line:**

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 19.3    | Command introduced                  |
+---------+-------------------------------------+

---

## run ping.rst

run ping
--------

**Minimum user role:** viewer

The ping command checks the accessibility of a destination interface. It uses a series of Internet Control Message Protocol (ICMP) Echo messages to determine whether or not the remote host is active, the round-trip delay in the communication with the host, and packet loss.

**Command syntax: run ping [dest-ip \| host-name]** source-interface [source-interface] interval [interval] size [size] count [count] df

**Command mode:** GI

**Note**

- The NCC handles ICMP packets. Therefore, ping to a remote host should be done from the NCC and not from the NCPs.

..
	- The ping command is one-line format. meaning - all parameters can be entered on the same line

		- The run ping command may include the source-interface. The source-interface must be of type mgmt-ncc-X.

		- Count - number or probe sequences per command

		- Size - ICMP payload

		- Interval - resolution of 0.001 seconds

		- Df - don't fragment - a flag which specifies that outgoing packet shouldn't be fragmented and should be sent as is with original size. by default, fragmentation is performed automatically. This option is only valid for IPv4 addresses.

.. **Help line:** run ICMP ping request


**Parameter table**

The following are the parameters that you can use for the ping command:

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| Parameter        | Description                                                                                                                                                                                                  | Range                                               | Default |
+==================+==============================================================================================================================================================================================================+=====================================================+=========+
| dest-ip          | The IPv4/IPv6 address of the target host to ping                                                                                                                                                             | A.B.C.D                                             | \-      |
|                  |                                                                                                                                                                                                              | x:x::x:x                                            |         |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| host-name        | The name of the target host to ping                                                                                                                                                                          | String                                              | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| source-interface | Sends the ping packets with the defined IP address of the source interface                                                                                                                                   | mgmt-ncc-X                                          | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| interval         | Specifies the time in seconds between sending ping packets (resolution of 0.001 seconds)                                                                                                                     | 0.001..86,400                                       | 1       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| size             | Specifies the number of data bytes to be added to the ping packet                                                                                                                                            | 1..65507                                            | 56      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| count            | Specifies the number of ping packets that will be sent                                                                                                                                                       | 1..1,000,000                                        | 5       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| df               | Do not fragment - a flag specifying that outgoing packets must not be fragmented.                                                                                                                            | Boolean                                             | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+

The parameters can all be specified in the same command.

**Example**
::

	GI# run ping 1.1.1.1
	GI# run ping 2001:1234::1
	GI# run ping 10.0.0.1 source-interface mgmt-ncc-0
	GI# run ping 1.1.1.1 count 200
	GI# run ping 1.1.1.1 interval 2
	GI# run ping 1.1.1.1 size 1500
	GI# run ping 1.1.1.1 interval 2 size 1000


**Command History**

+---------+----------------------------------------------------------------------------------------+
| Release | Modification                                                                           |
+=========+========================================================================================+
| 18.3    | Command introduced                                                                     |
+---------+----------------------------------------------------------------------------------------+

---

## run start shell.rst

run start shell
---------------

**Minimum user role:** viewer

Provides access to the white box shell.

**Command syntax: run start shell**

**Command mode:** GI

.. **Note**

 - The "exit" command reverts to GI Mode.

**Example**
::

	dnRouter(GI)# run start shell
	root@WDV1947700016:/#

	root@WDV1947700016:/# exit
	dnRouter(GI)#



.. **Hidden Note:**

.. **Parameter table:**

.. **Help line:** Access white box shell.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+

---

## run traceroute.rst

run traceroute
--------------

**Minimum user role:** viewer

The run traceroute command displays the route that packets take to the specified destination address. When enabled, the router sends out a number of probes (UDP packets) set by the count parameter to the destination IP. This command is useful to locate points of failure in the network.

**Command syntax: run traceroute [dest-ip \| host-name]** source-interface [source-interface] max-hops [max-hops] df

**Command mode:** GI

**Note**

- The NCC handles ICMP packets. Therefore, traceroute to a remote host should be done from the NCC and not from the NCPs.

.. - The traceroute command is one-line format. meaning - all parameters can be entered on the same line

	 - run traceroute [dest-ip]source-interface [source-interface] - The traceroute packet should be sent with the defined ip address of the source interface.

	 - The run traceroute command may include the source-interface. The source-interface must be of type mgmt-ncc-X.

**Parameter table**

The following are the parameters for this command:

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| Parameter        | Description                                                                                                                                                                                                  | Range                                              | Default |
+==================+==============================================================================================================================================================================================================+====================================================+=========+
| dest-ip          | The IPv4 or IPv6 address of the remote host to trace                                                                                                                                                         | x.x.x.x                                            | \-      |
|                  |                                                                                                                                                                                                              | x:x::x:x                                           |         |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| host-name        | The name of the target host to trace                                                                                                                                                                         | String                                             | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| source-interface | Sends the ping packets with the defined IP address of the source interface                                                                                                                                   | mgmt-ncc-X                                         | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| max-hops         | The maximum number of hops that the trace packet should cross before timeout                                                                                                                                 | 1..255                                             | 30      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+
| df               | Do not fragment - a flag specifying that outgoing packets must not be fragmented.                                                                                                                            | Boolean                                            | \-      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------+

The parameters can all be specified in the same command.

**Example**
::

	GI# run traceroute 1.1.1.1
	GI# run traceroute 2001:1234::1
	GI# run traceroute source-interface mgmt-ncc-1
	GI# run traceroute 1.1.1.1 max-hops 2

.. **Help line:** run traceroute request

**Command History**

+---------+------------------------------------------------------------------------------------------------------------+
| Release | Modification                                                                                               |
+=========+============================================================================================================+
| 18.3    | Command introduced                                                                                         |
+---------+------------------------------------------------------------------------------------------------------------+

---

## set gi grpc server listen port.rst

set gi grpc server listen port
------------------------------

**Minimum user role:** viewer

To configure the GI gRPC server listen port:

**Command syntax: set gi grpc server listen port [listen-port]**

**Command mode:** GI

**Note**

- The GI gRPC server listen port configuration can be set by the ZTP process through DHCP option 67.

**Example**
::

	gi# set gi grpc server listen port 52433

**Parameter table:**

.. **Help line:** Configure gi grpc server listen port.

+-------------+-----------------------------+-----------+---------+
|   Parameter | Description                 |     Range | Default |
+=============+=============================+===========+=========+
| listen-port | A single listen port number | <1..65535>| 52433   |
+-------------+-----------------------------+-----------+---------+

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 18.2    | Command introduced                  |
+---------+-------------------------------------+

---

## set mgmt dnor-server.rst

set mgmt dnor-server
--------------------

**Minimum user role:** viewer

To configure DNOR servers:

**Command syntax: set mgmt dnor-server [address-list]**

**Command mode:** GI

**Note**

- If DHCP/DHCPv6 is enabled on the white box mgmt interface, the white box may get an additional DNOR address in DHCP option 66 or DHCPv6 option 59.

**Example**
::

	gi# set mgmt dnor-server 172.16.45.23

	gi# set mgmt dnor-server 172.16.45.23,172.16.45.24,72.16.45.23

	gi# set mgmt dnor-server dnor1.mydomain.com,dnor2.mydomain.com


.. **Hidden Note:**

**Parameter table:**

.. **Help line:** Configure DNOR servers.

+--------------+---------------------------------------------------------------------+--------------+---------+
|   Parameter  | Description                                                         |     Range    | Default |
+==============+=====================================================================+==============+=========+
| address-list | A list of up to 3 FQDNs or IPv4 addresses, separated by whitespaces | FQDN address | /-      |
|              |                                                                     | A.B.C.D      |         |
+--------------+---------------------------------------------------------------------+--------------+---------+

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+

---

## set system-type.rst

set system-type
---------------

**Minimum user role:** viewer

Set the NC-AI cluster formation with which the node is associated. To configure the NC-AI node system-type:

**Command syntax: set system-type [system-type]**

**Command mode:** GI

.. **Note**

**Example**
::

	gi# set system-type CL-AI-8K-400G

**Parameter table:**

.. **Help line:** Configure nc-ai node system-type.

+-------------+-------------------------------------------+-----------+---------+
|   Parameter | Description                               |     Range | Default |
+=============+===========================================+===========+=========+
| system-type | The cluster type the node is associated.  | \-        | \-      |
+-------------+-------------------------------------------+-----------+---------+

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 19.10   | Command introduced                  |
+---------+-------------------------------------+

---

## show interfaces management arp.rst

show arp
------------------------------

**Minimum user role:** viewer

The command displays the ARP tables of management interfaces. To filter the display to show the ARP table of a specific interface by specifying the interface-name and/or ipv4-address:

**Command syntax: show arp** {interface [interface-name] \| ipv4-address [ipv4-address]

**Command mode:** operational


..
	**Internal Note**

	-  When a user selects a specific interface/ipv4-address it will filter according to it

	-  Age column displays a dynamic ARP entry's age

	-  Entries of local origin are not valid ARP entries, but merely list an interface's local IPv4 and MAC addresses for convenience.

**Parameter table**

+----------------+----------------------------------------------------------------+----------------------------+-----------------+
| Parameter      | Description                                                    | Range                      | Default value   |
+================+================================================================+============================+=================+
| interface-name | Filter the ARP entries according to the specified interface    | An existing interface name | /-              |
+----------------+----------------------------------------------------------------+----------------------------+-----------------+
| ipv4-address   | Filter the ARP entries according to the specified IPv4 address | A.B.C.D                    | /-              |
+----------------+----------------------------------------------------------------+----------------------------+-----------------+

The following information is displayed:

+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter    | Description                                                                                                                                                                                                     | Options                                                                                                                                                                                                                                                 |
+==============+=================================================================================================================================================================================================================+=========================================================================================================================================================================================================================================================+
| IPv4 Address | The IPv4 address for the ARP entry                                                                                                                                                                              | A.B.C.D                                                                                                                                                                                                                                                 |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MAC Address  | The MAC address corresponding to the IPv4 address                                                                                                                                                               | xx:xx:xx:xx:xx:xx                                                                                                                                                                                                                                       |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |                                                                                                                                                                                                                 | Static - the entry was added manually                                                                                                                                                                                                                   |
| Origin       | Displays how the ARP entry was acquired.                                                                                                                                                                        | Dynamic - see Dynamic ARP                                                                                                                                                                                                                               |
|              |                                                                                                                                                                                                                 | Local - shows an interface's local IPv4 and MAC addresses for convenience (not a valid ARP entry).                                                                                                                                                      |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| State        | Indicates the state of the ARP cache entry:                                                                                                                                                                     | Static - the entry was manually added to the ARP table (see interfaces arp); static entries do not age out.                                                                                                                                             |
|              | All states except "static", are for dynamically learned entries.                                                                                                                                                | Incomplete - an ARP request was sent but the MAC address is still unknown.                                                                                                                                                                              |
|              |                                                                                                                                                                                                                 | Reachable - normal entry expiration                                                                                                                                                                                                                     |
|              |                                                                                                                                                                                                                 | Stale - the ARP entry has expired but needs verification (it is still usable)                                                                                                                                                                           |
|              |                                                                                                                                                                                                                 | Delay - schedule an ARP request                                                                                                                                                                                                                         |
|              |                                                                                                                                                                                                                 | Probe - sending an ARP request                                                                                                                                                                                                                          |
|              |                                                                                                                                                                                                                 | Failed - entries for which ARP requests were sent, but ARP replies were not received. ARP entries from “INCOMPLETE” and “DELAY” state can become “FAILED” if no ARP replies were received.                                                              |
|              |                                                                                                                                                                                                                 | Noarp - ARP requests are never sent to verify expired ARP entries. If an interface is set to “NOARP” mode, all the ARP entries in “REACHABLE” state become “NOARP” after ARP stale timeout. DNOS does not provide “NOARP” interface mode configuration. |
|              |                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                         |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Age          | The amount of time that the entry exists in the ARP table. The age is displayed for dynamic entries only.                                                                                                       | days, HH:MM:SS                                                                                                                                                                                                                                          |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Interface    | The name of the interface from which the entry was learned.                                                                                                                                                     | mgmt-ncc-x                                                                                                                                                                                                                                              |
|              | When selecting the interface mgmt-ncc-0 or mgmt-ncc-1, the NDP entries are displayed for only mgmt-ncc-0 or mgmt-ncc-1 correspondingly.                                                                         |                                                                                                                                                                                                                                                         |
|              |                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                         |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example**
::

	dnRouter# show arp

	Interface: mgmt-ncc-0
	| IPv4 Address | MAC Address       | Origin  | State          | Age              | Interface    |
	+--------------+-------------------+---------+----------------+------------------+--------------|
	| 30.1.1.4     | 7c:ae:90:57:73:82 | dynamic | reachable      | 0 days, 00:00:04 | mgmt-ncc-0   |
	| 30.1.1.5     | 7c:ae:90:57:73:82 | dynamic | reachable      | 0 days, 00:00:04 | mgmt-ncc-0   |

	Interface: mgmt-ncc-1
	| IPv4 Address | MAC Address       | Origin  | State          | Age              | Interface    |
	+--------------+-------------------+---------+----------------+------------------+--------------|
	| 30.1.1.4     | 7c:ae:90:57:73:82 | dynamic | reachable      | 0 days, 00:00:04 | mgmt-ncc-0   |
	| 30.1.1.5     | 7c:ae:90:57:73:82 | dynamic | reachable      | 0 days, 00:00:04 | mgmt-ncc-0   |

	dnRouter# show arp interface mgmt-ncc-0

	VRF: mgmt-ncc-0
	| IPv4 Address | MAC Address       | Origin  | State          | Age              | Interface    |
	+--------------+-------------------+---------+----------------+------------------+--------------|
	| 30.1.1.4     | 7c:ae:90:57:73:82 | dynamic | reachable      | 0 days, 00:00:04 | mgmt-ncc-0   |
	| 30.1.1.5     | 7c:ae:90:57:73:82 | dynamic | reachable      | 0 days, 00:00:04 | mgmt-ncc-0   |

.. **Help line:** show arp information

**Command History**

+---------+---------------------------------------------------------+
| Release | Modification                                            |
+=========+=========================================================+
| 17.1    | Command introduced                                      |
+---------+---------------------------------------------------------+

---

## show interfaces management configuration.rst

show interfaces management configuration
----------------------------------------

**Minimum user role:** viewer

To display the configuration of the physical management interfaces:

**Command syntax: show interfaces management configuration**

**Command mode:** operational

**Parameter table**

The following information is displayed for each interface:

+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                              |
| Parameter            | Description                                                                                                                                  |
+======================+==============================================================================================================================================+
|                      |                                                                                                                                              |
| Admin-state          | Displays whether   the interface/port is enabled or disabled.                                                                                |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                              |
| Description          | The configured description   for the interface/port                                                                                          |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                              |
| MAC Address          | The interface’s   MAC address                                                                                                                |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                              |
| MTU                  | The configured MTU   for the interface                                                                                                       |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                              |
| IPv4/IPv6 Address    | The static IPv4   or IPv6 address configured for the interface. DHCP indicates that the IP address   is obtained dynamically through DHCP    |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
|                      |                                                                                                                                              |
| IPv4 routes          | The installed routes   for packet forwarding                                                                                                 |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

**Note**

- This command is applicable to the mgmt-ncc interfaces.

**Example**
::

	dnRouter# show interfaces management configuration
	Interface mgmt-ncc-0
	Admin state: enabled
	Description:
	MAC Address: 06:6f:87:c9:67:2f
	MTU: 1500
	IPv4 Address: 100.64.6.37/20
	IPv6 Address: DHCP
	IPv4 routes:
		1.2.3.4/32 next-hop 4.2.3.1
		6.6.6.6/32 next-hop 4.2.3.1
	IPv6 routes:
		N/A
		
	Interface mgmt-ncc-0/0
		Admin state: enabled
		Description:
	
	Interface mgmt-ncc-0/1
		Admin state: enabled
		Description:

	Interface mgmt-ncc-1
	Admin state: enabled
	Description:
	MAC Address: 06:6f:87:c9:67:2f
	MTU: 1500
	IPv4 Address: DHCP
	IPv6 Address: DHCP
	IPv4 routes:
		N/A
	IPv6 routes:
		N/A
		
	Interface mgmt-ncc-1/0
		Admin state: enabled
		Description:
	
	Interface mgmt-ncc-1/1
		Admin state: enabled
		Description:


.. **Help line: show interfaces management configuration**

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## show interfaces management ndp.rst

show ndp
------------------------------

**Minimum user role:** viewer

The command displays the NDP tables of management interfaces. To filter the display to show the NDP table of a specific interface by specifying the interface-name and/or ipv6-address:

**Command syntax: show ndp** {interface [interface-name] \| ipv6-address [ipv6-address]

**Command mode:** operational


..
	**Internal Note**

	- [interface-name] | [ipv6-address]: filter the NDP entries according to a specific interface-name, and/or a specific IPv6-address.

	-  When a user selects a specific interface/ipv6-address it will filter according to it

	- Age column displays a dynamic NDP entry's age

**Parameter table**

The following information is displayed:

+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter    | Description                                                                                                                                                                                                     | Options                                                                                                                                                                                                                                                 |
+==============+=================================================================================================================================================================================================================+=========================================================================================================================================================================================================================================================+
| IPv6 Address | The IPv6 address for the NDP entry                                                                                                                                                                              | x:x::x:x                                                                                                                                                                                                                                                |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MAC Address  | The MAC address corresponding to the IPv6 address                                                                                                                                                               | xx:xx:xx:xx:xx:xx                                                                                                                                                                                                                                       |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Origin       | Displays how the NDP entry was acquired                                                                                                                                                                         | Static - the entry was added manually                                                                                                                                                                                                                   |
|              |                                                                                                                                                                                                                 | Dynamic - see Dynamic ARP                                                                                                                                                                                                                               |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| State        | Indicates the state of the NDP cache entry.                                                                                                                                                                     | Static - the entry was manually added to the NDP table (see interfaces ndp)                                                                                                                                                                             |
|              | All states except "static", are for dynamically learned entries.                                                                                                                                                | Incomplete - an NDP request was sent but the MAC address is still unknown.                                                                                                                                                                              |
|              |                                                                                                                                                                                                                 | Reachable - normal entry expiration                                                                                                                                                                                                                     |
|              |                                                                                                                                                                                                                 | Stale - the entry has expired but needs verification (it is still usable)                                                                                                                                                                               |
|              |                                                                                                                                                                                                                 | Delay - schedule an NDP request                                                                                                                                                                                                                         |
|              |                                                                                                                                                                                                                 | Probe - sending an NDP request                                                                                                                                                                                                                          |
|              |                                                                                                                                                                                                                 | Failed - entries for which NDP requests were sent, but NDP replies were not received. NDP entries from “INCOMPLETE” and “DELAY” state can become “FAILED” if no NDP replies were received.                                                              |
|              |                                                                                                                                                                                                                 | Noarp - NDP requests are never sent to verify expired NDP entries. If an interface is set to “NOARP” mode, all the NDP entries in “REACHABLE” state become “NOARP” after the stale timeout. DNOS does not provide “NOARP” interface mode configuration. |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Age          | The amount of time that the entry exists in the NDP table. The age is displayed for dynamic entries only.                                                                                                       | days, HH:MM:SS                                                                                                                                                                                                                                          |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Interface    | The name of the interface from which the entry was learned. The NDP entry will be distributed to the interface's broadcast domain.                                                                              | This command is applicable to the following interfaces:                                                                                                                                                                                                 |
|              | When selecting the interface mgmt-ncc-0 or mgmt-ncc-1, the NDP entries are displayed for only mgmt-ncc-0 or mgmt-ncc-1 correspondingly.                                                                         | mgmt-ncc-0, mgmt-ncc-1                                                                                                                                                                                                                                  |
|              |                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                         |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Type         | The neighbor type                                                                                                                                                                                               | router                                                                                                                                                                                                                                                  |
|              |                                                                                                                                                                                                                 | host                                                                                                                                                                                                                                                    |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example**
::

	dnRouter# show ndp

	Interface: mgmt-ncc-0
	| IPv6 Address      | MAC Address       | Origin  | State          | Age               | Interface    | Type      |
	|-------------------+-------------------+---------+----------------+-------------------+--------------+-----------|
	| 2001:1234::1      | 7c:fe:90:57:73:81 | dynamic | reachable      | 0 days, 00:00:24  | mgmt-ncc-0   | Host      |
	| 2001:1234:3333::1 | 7c:fe:90:57:73:82 | dynamic | reachable      | 0 days, 00:02:48  | mgmt-ncc-0   | Host      |

	Interface: mgmt-ncc-1
	| IPv6 Address      | MAC Address       | Origin  | State          | Age               | Interface    | Type      |
	|-------------------+-------------------+---------+----------------+-------------------+--------------+-----------|
	| 2001:1234::1      | 7c:fe:90:57:73:81 | dynamic | reachable      | 0 days, 00:00:24  | mgmt-ncc-1   | Host      |
	| 2001:1234:3333::1 | 7c:fe:90:57:73:82 | dynamic | reachable      | 0 days, 00:02:48  | mgmt-ncc-1   | Host      |

	dnRouter# show ndp interface mgmt-ncc-0
	
	Interface: mgmt-ncc-0
	| IPv6 Address      | MAC Address       | Origin  | State          | Age               | Interface    | Type      |
	|-------------------+-------------------+---------+----------------+-------------------+--------------+-----------|
	| 2001:1234::1      | 7c:fe:90:57:73:81 | dynamic | reachable      | 0 days, 00:00:24  | mgmt-ncc-0   | Host      |
	| 2001:1234:3333::1 | 7c:fe:90:57:73:82 | dynamic | reachable      | 0 days, 00:02:48  | mgmt-ncc-0   | Host      |

.. **Help line:** show ndp information

**Command History**

+---------+---------------------------------------------------------+
| Release | Modification                                            |
+=========+=========================================================+
| 16.2    | Command introduced                                      |
+---------+---------------------------------------------------------+

---

## show interfaces management.rst

show interfaces management
--------------------------

**Minimum user role:** viewer

To display a list of the management interfaces:

**Command syntax: show interfaces management** [interface-name]

**Command mode:** operational

**Note**

- The command is applicable to the following interface types:

	- mgmt.


- If the node is not yet configured or is not connected to the NCC, the operational state of its interfaces will display as "not-exist".

- The operational state relates to the link-state (laser state). The uptime for management interfaces is with a "watch" interval of 1 second and is displayed for interfaces with an operational state "up", otherwise the uptime is "0".

- For console interfaces, the serial interface parameters are displayed.

**Parameter table**

+----------------+----------------------------------------------------------------------+-----------------+---------+
| Parameter      | Description                                                          | Range           | Default |
+================+======================================================================+=================+=========+
| interface-name | Optionally filter the displayed information to a specific interface. | mgmt-ncp-x/     | \-      |
|                |                                                                      | mgmt-ncf-x/y    |         |
|                |                                                                      | mgmt-ncc-x      |         |
|                |                                                                      | mgmt-ncc-x/y    |         |
+----------------+----------------------------------------------------------------------+-----------------+---------+

The following information is displayed per interface:

+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| Field                      | Description                                                                                                                                                                                                                  | Options             | Default |
+============================+==============================================================================================================================================================================================================================+=====================+=========+
| Interface                  | The name of the interface                                                                                                                                                                                                    | String              |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| Admin                      | The administrative status, indicates whether or not the interface is currently enabled.                                                                                                                                      | Enabled             |         |
|                            | System-down means that the port was shut down by the system (and not by a user).                                                                                                                                             | Disabled            |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| Operational                | The operational state of the interface, indicates whether the link is currently up or down. For physical interfaces, the operational state relates to the link-state (lasar state)                                           | Up                  |         |
|                            | Not-present: the port was pre-provisioned (the NCP is configured but not yet connected to the NCC), or the port was removed due to breakout.                                                                                 | Down                |         |
|                            |                                                                                                                                                                                                                              | Not-present         |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| Uptime                     | The amount of time that the interface is up consecutively, with a polling time every 1 second..Uptime relates to physical, Loopback,bundle and subinterface interface types. Uptime resets to zero if the interface is down. | D days, HH:MM:SS    |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| Description                | The description provided for the interface.                                                                                                                                                                                  | String              |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| MAC Address                | The MAC Address of the interface. The MAC address is for physical interfaces only.                                                                                                                                           | MAC address format  |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| Speed                      | The interface's speed                                                                                                                                                                                                        |                     |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| Duplex                     | The directionality of data transmission                                                                                                                                                                                      | Full                |         |
|                            |                                                                                                                                                                                                                              | Half                |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| IPv4 Address               | The configured IPv4 address of the interface. Secondary IPv4 addresses are also listed.                                                                                                                                      | A.B.C.D/x           |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| IPv6 Address               | The configured IPv6 address(es) of the interface. IPv6 addresses are marked as suspended (s) if they are have a 'Tentative' or 'Duplicate' status. (Applicable to IPv6 addresses going through a DAD procedure).             | x:x::x:x/x          |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| ipv6-address-status        | Inaccessible/Unknown/Tentative/Duplicate/Preferred                                                                                                                                                                           |                     |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| ipv6 admin-state           | The administrative state of IPv6 on the interface                                                                                                                                                                            | Enabled             | Enabled |
|                            |                                                                                                                                                                                                                              | Disabled            |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| Encapsulation              | The encapsulation that is currently activated on the interface.                                                                                                                                                              | Ethernet            |         |
|                            |                                                                                                                                                                                                                              | 802.1Q              |         |
|                            |                                                                                                                                                                                                                              | QinQ                |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| Access-list IPv4/IPv6      | The name of the access list that is applied to the interface.                                                                                                                                                                | String              | \-      |
|                            | "ACL mode disabled" is displayed when the general ACL mode is disabled.                                                                                                                                                      |                     |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| IPv4/IPv6 DHCP             | The administrative status of DHCP on the interface.                                                                                                                                                                          | Enabled             | Enabled |
|                            |                                                                                                                                                                                                                              | Disabled            |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| MTU                        | The configured L2 and L3 maximum transmission unit (MTU), which defines the largest packet size, in bytes, for this interface. L2 MTU default value is 1514, IPv4/IPv6 default values are 1500.                              | Bytes               |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| ARP-timeout                | The configured amount of time (in seconds) that an ARP entry will remain in the ARP cache.                                                                                                                                   | Integer             | 3600    |
|                            |                                                                                                                                                                                                                              | 60..14400 (seconds) |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| NDP-timeout                | The configured amount of time (in seconds) that an NDP entry will remain in the NDP cache.                                                                                                                                   | Integer             | 3600    |
|                            |                                                                                                                                                                                                                              | 60..14400 (seconds) |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| SNMP ifindex               | SNMP Management Information Base (MIB) uses Interface Index (ifIndex) to assign a unique value to each interface.                                                                                                            | Integer             |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| VRF                        | The VRF associated with the interface.                                                                                                                                                                                       | String              |         |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
| Member State               | The operational state of the bundle member.                                                                                                                                                                                  | Up                  | \-      |
|                            |                                                                                                                                                                                                                              | Down                |         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+
| Reason for last down state | Displays the reason why the physical interface went down                                                                                                                                                                     | string              | \-      |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+---------+

**Example**
::

	
	dnRouter# show interfaces management
	
	| Interface         | Admin    | Operational   | IPv4 Address   | IPv6 Address                   | MTU  | VRF        |
	+-------------------+----------+---------------+----------------+--------------------------------+------|------------|
	| mgmt-ncc-0        |          | not-exist     | 200.1.1.3/32   | 1006:abcd:12::1/128            | 1514 | mgmt-ncc-0 |
	| mgmt-ncc-1        | enabled  | up            | 200.1.1.4/32   | 1006:abcd:12::2/128            | 1514 | mgmt-ncc-1 |
	| mgmt-ncc-1/0      | enabled  | up            |                |                                |      | mgmt-ncc-1 |
	| mgmt-ncc-1/0      | enabled  | up            |                |                                |      | mgmt-ncc-1 |
	
	
	dnRouter# show interfaces management mgmt-ncc-0
	
	Interface mgmt-ncc-0
	  SNMP ifindex: 1234
	  Admin state: enabled, Operational state: up, Uptime: 0 days, 00:01:30
	  Description: internal mgmt.
	  MAC Address: 7c:fe:90:57:73:81 (HW: 7c:fe:90:57:73:81)
	  Speed: 1Gbps, Duplex: full
	  L2 MTU: 1514
	  IPv4 Address: 10.1.1.1/32 (DHCP)
	  IPv6 local: fe80::6a05:caff:fe38:6f68/64
	  IPv6 Address: 2010::0001:0001:0001:0020/128
	  IPv4 DHCP: enabled, IPv6 DHCP: enabled
	  ARP Timeout: 3600 seconds
	  NDP Timeout: 3600 seconds 
	  Encapsulation: Ethernet
	  Access-list IPv4: In: N/A
	  Access-list IPv6: In: N/A
	  Reason for last down state: link-down on mgmt-ncc-1/0
	  Members Information:
		| Interface    | Member State  |
		|--------------+---------------+
		| mgmt-ncc-0/0 | up            |
		| mgmt-ncc-0/1 | up            |

	
	dnRouter# show interfaces management mgmt-ncc-1/0

	Interface mgmt-ncc-1/0
	  SNMP ifindex: 1234, VRF: mgmt-ncc-1
	  Admin state: enabled, Operational state: up, Uptime: 0 days, 00:01:30
	  Speed: 100Gbps, Duplex: FULL
	  Encapsulation: Ethernet
	

.. **Help line:** show interface list

**Command History**

+---------+---------------------------------------------------------------------------------------+
| Release | Modification                                                                          |
+=========+=======================================================================================+
| 11.0    | Command introduced                                                                    |
+---------+---------------------------------------------------------------------------------------+
| 16.2    | Moved all management interfaces to this command and exposed management bundle members |
+---------+---------------------------------------------------------------------------------------+


---

## show system gi grpc server listen port.rst

GI gRPC server listening port
-----------------------------

**Minimum user role:** viewer

To display the active GI gRPC server listening port.

**Command syntax: show gi grpc server listen port**

**Command mode:** GI

.. **Note:**

**Example**
::

	gi# show gi grpc server listen port


	 	| GI gRPC server listen port  |
		+-----------------------------+
		| 80                          |

.. **Help line:** Show the active GI gRPC server listening port.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 18.2    | Command introduced                  |
+---------+-------------------------------------+

---

## show system nodes stack.rst

show system nodes stack 
-----------------------

**Minimum user role:** operator

Displays detailed information about packages in current, revert and target stacks relevant per each node in the cluster.

**Command syntax: show system nodes stack**

**Command mode:** operational

**Example:**
::

	gi# show system nodes stack 
	
	Current stack:
	
    | Node | ID | Component       | HW Model      | HW Revision   | Version     | Package name                         | Size    | Authenticity        | MD5           |
    |------+----|-----------------+---------------+---------------+-------------+--------------------------------------+---------+---------------------+---------------|
    | NCC  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_14.0.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCC  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.304.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCC  | 0  | BaseOS packages |     -         |     -         | 1.100       | drivenets_baseos_packages_1.100.tar  | 0.7 GB  | signature-verified  | 5437asdghfs   |
    | NCM  | A0 | NCM-NOS         |     -         |     _         | 3.0.0       | drivenets_stratax_3.0.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   |
    | NCP  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_14.0.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCP  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.304.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCP  | 0  | Firmware        | S9700-53DX    | 1             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674   |
    | NCF  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_14.0.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCF  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.304.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCF  | 0  | Firmware        | S9700-23D-J   | 3             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674   |
	 
	Target stack:
	
    | Node | ID | Component       | HW Model      | HW Revision   | Version     | Package name                         | Size    | Authenticity        | MD5           |
    |------+----|-----------------+---------------+---------------+-------------+--------------------------------------+---------+---------------------+---------------|
    | NCC  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_16.1.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCC  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.506.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCC  | 0  | BaseOS packages |     -         |     -         | 1.100       | drivenets_baseos_packages_1.200.tar  | 0.7 GB  | signature-verified  | 5437asdghfs   |
    | NCM  | A0 | NCM-NOS         |     -         |     _         | 3.0.0       | drivenets_stratax_3.0.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   |
    | NCP  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_16.1.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCP  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.506.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCP  | 0  | Firmware        | S9700-53DX    | 1             | 7.80        | ufi-wbx-fw-8.10                      | 40 MB   | hash-verified       | jhsdgsdj674   |
    | NCF  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_16.1.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCF  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.506.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
	
	
	Revert stack:
	
    | Node | ID | Component       | HW Model      | HW Revision   | Version     | Package name                         | Size    | Authenticity        | MD5           |
    |------+----|-----------------+---------------+---------------+-------------+--------------------------------------+---------+---------------------+---------------|
    | NCC  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_13.0.2.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCC  | 0  | BaseOS packages |     -         |     -         | 1.100       | drivenets_baseos_packages_1.100.tar  | 0.6 GB  | signature-verified  | 54322234hfs   |
    | NCM  | A0 | NCM-NOS         |     -         |     _         | 2.0.0       | drivenets_stratax_2.0.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   |
    | NCP  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_13.0.2.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCP  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.304.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCP  | 0  | Firmware        | S9700-53DX    | 1             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674   |
    | NCF  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_13.0.2.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCF  | 0  | Firmware        | S9700-23D-J   | 3             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674     

**Outputs table:**

+----------------------+-------------------------+----------+
| Parameter            | Values                  | Comments |
+======================+=========================+==========+
| Authenticity         | signature-verified      |          |
|                      | hash-verified           |          |
|                      | unverified              |          |
+----------------------+-------------------------+----------+

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## show system revert-stack pre-check history.rst

show system revert-stack pre-check history
-------------------------------------------

**Minimum user role:** viewer

To display the result of the last 50 revert-stack pre-check commands.

**Command syntax: show system revert-stack pre-check history**

**Command mode:** GI

**Note**

- If no revert-stack pre-check command was conducted prior to the show command, it will display an empty output.

**Example**
::

    Pre-check history:

    | Task ID       | Task Status   | Task Start Time     | Task Finish Time    | Pre-Check Result   |
    |---------------+---------------+---------------------+---------------------+--------------------|
    | 1688987412517 | DONE          | 2023-07-10 11:10:12 | 2023-07-10 11:10:12 | Failed             |
    | 1688987333867 | DONE          | 2023-07-10 11:08:53 | 2023-07-10 11:08:53 | Failed             |

    Details:

    Task ID:		    1688987412517
    Task status:		DONE
    Task start time:	2023-07-10 11:10:12
    Task finish time:	2023-07-10 11:10:12
    Pre-check result:	Failed
    Tests info:

    | Test Name            | Test Result   | Message                                                                                 |
    |----------------------+---------------+-----------------------------------------------------------------------------------------|
    | Disk Partition       | Failed        | ncc0: Partition 'docker' is lacking space: required: 500.00MB, available: 9B            |
    |                      |               | ncc1: Partition 'docker' is lacking space: required: 500.00MB, available: 9B            |
    | Packages Signature   | Failed        | Package: dnos_mock_package_1, authenticity: integrity-failed                            |
    | Versioning Readiness | Passed        | Verified cluster readiness:                                                             |
    |                      |               |    Secondary NCC, if present, is ready and operational.                                 |
    |                      |               |    The cluster is not currently performing any other versioning operation.              |
    | Download In-Progress | Passed        | Verified packages download status:                                                      |
    |                      |               |    There are no packages that are being downloaded to the cluster.                      |
    | DNOS Target Version  | Passed        | Verified DNOS target version validity:                                                  |
    |                      |               |    DNOS target version is higher than current installed version                         |
    | Stack Validity       | Passed        | Verified stack validity:                                                                |
    |                      |               |    Stack is not empty.                                                                  |
    |                      |               |    Revert stack will not cause DNOS deletion.                                           |
    |                      |               |    All stack components' dependencies are met.                                          |
    | Repo Replication     | Passed        | Verified repository synchronization:                                                    |
    |                      |               |    The standby NCC, if present, is synchronized over stack configurations and packages. |
    | Packages Validity    | Passed        | Verified packages validity:                                                             |
    |                      |               |    Stack packages' integrity checksum was verified.                                     |


    Task ID:		    1688987333867
    Task status:		DONE
    Task start time:	2023-07-10 11:08:53
    Task finish time:	2023-07-10 11:08:53
    Pre-check result:	Failed
    Tests info:

    | Test Name            | Test Result   | Message                                                                                            |
    |----------------------+---------------+----------------------------------------------------------------------------------------------------|
    | Versioning Readiness | Passed        | Verified cluster readiness:                                                                        |
    |                      |               |    Secondary NCC, if present, is ready and operational.                                            |
    |                      |               |    The cluster is not currently performing any other versioning operation.                         |
    | Download In-Progress | Passed        | Verified packages download status:                                                                 |
    |                      |               |    There are no packages that are being downloaded to the cluster.                                 |
    | DNOS Target Version  | Passed        | Verified DNOS target version validity:                                                             |
    |                      |               |    DNOS target version is higher than current installed version                                    |
    | Stack Validity       | Failed        | Revert stack is empty                                                                              |
    | Disk Partition       | Passed        | Verified disk space and mount:                                                                     |
    |                      |               |    Cluster's nodes have enough space to perform versioning operations and all of them are mounted. |
    | Repo Replication     | Passed        | Verified repository synchronization:                                                               |
    |                      |               |    The standby NCC, if present, is synchronized over stack configurations and packages.            |
    | Packages Validity    | Passed        | Verified packages validity:                                                                        |
    |                      |               |    Stack packages' integrity checksum was verified.                                                |
    | Packages Signature   | Passed        | Verified packages signature:                                                                       |
    |                      |               |    DN-signed stack packages' have been verified to be sourced from DN.                             |

.. **Help line:** Displays the result of the last 50 revert stack pre-check commands.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 18.2.1  | Command introduced                  |
+---------+-------------------------------------+

---

## show system revert-stack pre-check.rst

show system revert-stack pre-check
-------------------------------------

**Minimum user role:** viewer

To display the result of the last revert-stack pre-check command.

**Command syntax: show system revert-stack pre-check**

**Command mode:** GI

**Note**

- If no revert-stack pre-check command was conducted prior to the show command, it will display an empty output.

**Example**
::

    Task ID:		    1688992839666
    Task status:		DONE
    Task start time:	2023-07-10 12:40:39
    Task finish time:	2023-07-10 12:40:39
    Pre-check result:	Failed
    Tests info:

    | Test Name            | Test Result   | Message                                                                                            |
    |----------------------+---------------+----------------------------------------------------------------------------------------------------|
    | Versioning Readiness | Passed        | Verified cluster readiness:                                                                        |
    |                      |               |    Secondary NCC, if present, is ready and operational.                                            |
    |                      |               |    The cluster is not currently performing any other versioning operation.                         |
    | Download In-Progress | Passed        | Verified packages download status:                                                                 |
    |                      |               |    There are no packages that are being downloaded to the cluster.                                 |
    | DNOS Target Version  | Passed        | Verified DNOS target version validity:                                                             |
    |                      |               |    DNOS target version is higher than current installed version                                    |
    | Stack Validity       | Failed        | Revert stack is empty                                                                              |
    | Disk Partition       | Passed        | Verified disk space and mount:                                                                     |
    |                      |               |    Cluster's nodes have enough space to perform versioning operations and all of them are mounted. |
    | Repo Replication     | Passed        | Verified repository synchronization:                                                               |
    |                      |               |    The standby NCC, if present, is synchronized over stack configurations and packages.            |
    | Packages Validity    | Passed        | Verified packages validity:                                                                        |
    |                      |               |    Stack packages' integrity checksum was verified.                                                |
    | Packages Signature   | Passed        | Verified packages signature:                                                                       |
    |                      |               |    DN-signed stack packages' have been verified to be sourced from DN.                             | 

.. **Help line:** Displays the result of the last revert stack pre-check command.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 18.2.1  | Command introduced                  |
+---------+-------------------------------------+

---

## show system stack detail.rst

show system stack detail
------------------------

**Minimum user role:** viewer

To display detailed information about packages in Current, Revert and Target stacks.

**Command syntax: show system stack detail**

**Command mode:** GI

.. **Note:**

**Example**
::

	gi# show system stack detail

	Current stack:

	  | Component       | HW Model      | HW Revision   | Version     | Package name                         | Size    | Authenticity        | MD5           | Estimated Time |
	  |-----------------+---------------+---------------+-------------+--------------------------------------+---------+---------------------+---------------|----------------|
	  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_14.0.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   | 0:16:40        |
	  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.304.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   | 0:16:40        |
	  | BaseOS packages |     -         |     -         | 1.100       | drivenets_baseos_packages_1.100.tar  | 0.7 GB  | signature-verified  | 5437asdghfs   | 0:15:40        |
	  | NCM-NOS         |     -         |     _         | 3.0.0       | drivenets_stratax_3.0.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   | 0:16:40        |
	  | Firmware        | S9700-53DX    | 1             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674   | 0:16:40        |
	  | Firmware        | S9700-23D-J   | 3             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674   | 0:16:40        |


	Target stack
	  | Component       | HW Model      | HW Revision   | Version     | Package name                         | Size    | Authenticity        | MD5           | Estimated Time |
	  |-----------------+---------------+---------------+-------------+--------------------------------------+---------+---------------------+---------------|----------------|
	  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_15.1.0.tar            | 2.8 GB  | signature-verified  | azn32564asv   | 0:16:40        |
	  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.506.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   | 0:16:40        |
	  | BaseOS packages |     -         |     -         | 1.100       | drivenets_baseos_packages_1.200.tar  | 0.7 GB  | signature-verified  | 5437asdghfs   | 0:15:40        |
	  | NCM-NOS         |     -         |     _         | 3.50        | drivenets_stratax_4.0.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   | 0:16:40        |
	  | Firmware        | S9700-53DX    | 1             | 8.0         | ufi-wbx-fw-8.0                       | 40 MB   | hash-verified       | jhsdgsdj674   | 0:16:40        |
	  | Firmware        | S9700-23D-J   | 3             | 8.0         | ufi-wbx-fw-8.0                       | 50 MB   | unverified          | hkdfddhsfk7   | 0:16:40        |

	Revert stack:

	  | Component       | Version     | Package name                         | Size    | Authenticity        | MD5           | Estimated Time |
	  |-----------------+-------------+--------------------------------------+---------+---------------------+---------------|----------------|
	  | DNOS            | 13.0.2      | drivenets_dnos_v13.0.2.tar           | 2.8 GB  | signature-verified  | azn32564asv   | 0:16:40        |
	  | BaseOS          | 1.507       | drivenets_baseos_1.507.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   | 0:16:40        |
	  | BaseOS packages | 1.100       | drivenets_baseos_packages_1.100.tar  | 0.6 GB  | signature-verified  | 54322234hfs   | 0:15:40        |
	  | NCM-NOS         | 2.1.0       | drivenets_stratax_2.1.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   | 0:16:40        |

The following is a description of the authenticity column in the output table:

+----------------------+-------------------------+----------+
| Parameter            | Values                  | Comments |
+======================+=========================+==========+
| Authenticity         | signature-verified      |          |
|                      | hash-verified           |          |
|                      | unverified              |          |
+----------------------+-------------------------+----------+

.. **Help line:** Show details about packages in current, revert and target stacks.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+
| 18.2.1  | Added estimated time                |
+---------+-------------------------------------+
---

## show system stack.rst

show system stack
-----------------

**Minimum user role:** viewer

To display Current, Revert and Target stacks.

**Command syntax: show system stack**

**Command mode:** GI

.. **Note:**

**Example**
::

	gi# show system stack


	  | Component       | HW Model      | HW Revision   | Revert      | Current     | Target        |
	  |-----------------+---------------+---------------+-------------+-------------+---------------|
	  | DNOS            |     -         |     -         | 13.0.2      | 14.0.1      | 15.1.0        |
	  | BaseOS          |     -         |     -         | 1.507       | 2.304       | 2.506         |
	  | BaseOS packages |     -         |     -         | 1.100       | 1.150       | 1.200         |
	  | NCM-NOS         |     -         |     _         | 2.1.0       | 3.0.0       | 4.0.0         |
	  | Firmware        | S9700-53DX    | 1             | -           | 7.80        | 8.0           |
	  | Firmware        | S9700-23D-J   | 3             | -           | 7.80        | 8.0           |

.. **Help line:** Show current, revert and target stacks.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+

---

## show system target-stack load history.rst

show system target-stack load history
-------------------------------------

**Minimum user role:** viewer

To display target stacks load history

**Command syntax: show system target-stack load history**

**Command mode:** GI

**Example**
::

    gi# show system target-stack load history

    url:                http://172.16.100.12/packages/ufi-wbx-fw-17-0.tar
    Task ID:            140
    Task status:        complete
    Task start time:    11-Dec-2019 13:58:14 UTC
    Task elapsed time:  02:10:00
    Finish time:        11-Dec-2019 16:08:14 UTC

    url:                http://172.16.100.12/packages/drivenets_stratax_1.1.0.tar
    Task ID:            144
    Task status:        complete
    Task start time:    11-Dec-2019 13:44:14 UTC
    Task elapsed time:  02:20:00
    Finish time:        11-Dec-2019 16:04:14 UTC


.. **Note:**

.. **Help line:** Displays system target stack load progress history.

The following is a description of the the output table:

+----------------------+-------------------------+----------+
| Parameter            | Values                  | Comments |
+======================+=========================+==========+
| Task status          | in-progress             |          |
|                      | completed               |          |
|                      | failed                  |          |
|                      | canceled                |          |
+----------------------+-------------------------+----------+

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+

---

## show system target-stack load.rst

show system target-stack load
-----------------------------

**Minimum user role:** viewer

To display current target stacks load progress

**Command syntax: show system target-stack load**

**Command mode:** GI

**Example**
::

    dnRouter# show system target-stack load

    url:                http://172.16.100.12/packages/ufi-wbx-fw-17-0.tar
    Task ID:            140
    Task status:        in-progress
    Task start time:    11-Dec-2019 13:58:14 UTC
    Task elapsed time:  01:42:37

    url:                http://172.16.100.12/packages/drivenets_stratax_1.1.0.tar
    Task ID:            144
    Task status:        in-progress
    Task start time:    11-Dec-2019 13:44:14 UTC
    Task elapsed time:  01:56:37


.. **Note:**

.. **Help line:** Displays system target stack load progress.

The following is a description of the the output table:

+----------------------+-------------------------+----------+
| Parameter            | Values                  | Comments |
+======================+=========================+==========+
| Task status          | in-progress             |          |
|                      | completed               |          |
|                      | failed                  |          |
|                      | canceled                |          |
+----------------------+-------------------------+----------+

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 16.1    | Command introduced                  |
+---------+-------------------------------------+

---

## show system target-stack pre-check history.rst

show system target-stack pre-check history
-------------------------------------------

**Minimum user role:** viewer

To display the result of the last 50 target-stack pre-check commands.

**Command syntax: show system target-stack pre-check history**

**Command mode:** GI

**Note**

- If no target-stack pre-check command was conducted prior to the show command, it will display an empty output.

**Example**
::

    Pre-check history:

    | Task ID       | Task Status   | Task Start Time     | Task Finish Time    | Pre-Check Result   |
    |---------------+---------------+---------------------+---------------------+--------------------|
    | 1688987412517 | DONE          | 2023-07-10 11:10:12 | 2023-07-10 11:10:12 | Failed             |
    | 1688987333867 | DONE          | 2023-07-10 11:08:53 | 2023-07-10 11:08:53 | Failed             |

    Details:

    Task ID:		    1688987412517
    Task status:		DONE
    Task start time:	2023-07-10 11:10:12
    Task finish time:	2023-07-10 11:10:12
    Pre-check result:	Failed
    Tests info:

    | Test Name            | Test Result   | Message                                                                                 |
    |----------------------+---------------+-----------------------------------------------------------------------------------------|
    | Disk Partition       | Failed        | ncc0: Partition 'docker' is lacking space: required: 500.00MB, available: 9B            |
    |                      |               | ncc1: Partition 'docker' is lacking space: required: 500.00MB, available: 9B            |
    | Packages Signature   | Failed        | Package: dnos_mock_package_1, authenticity: integrity-failed                            |
    | Versioning Readiness | Passed        | Verified cluster readiness:                                                             |
    |                      |               |    Secondary NCC, if present, is ready and operational.                                 |
    |                      |               |    The cluster is not currently performing any other versioning operation.              |
    | Download In-Progress | Passed        | Verified packages download status:                                                      |
    |                      |               |    There are no packages that are being downloaded to the cluster.                      |
    | DNOS Target Version  | Passed        | Verified DNOS target version validity:                                                  |
    |                      |               |    DNOS target version is higher than current installed version                         |
    | Stack Validity       | Passed        | Verified stack validity:                                                                |
    |                      |               |    Stack is not empty.                                                                  |
    |                      |               |    Target stack will not cause DNOS deletion.                                           |
    |                      |               |    All stack components' dependencies are met.                                          |
    | Repo Replication     | Passed        | Verified repository synchronization:                                                    |
    |                      |               |    The standby NCC, if present, is synchronized over stack configurations and packages. |
    | Packages Validity    | Passed        | Verified packages validity:                                                             |
    |                      |               |    Stack packages' integrity checksum was verified.                                     |


    Task ID:	        1688987333867
    Task status:		DONE
    Task start time:	2023-07-10 11:08:53
    Task finish time:	2023-07-10 11:08:53
    Pre-check result:	Failed
    Tests info:

    | Test Name            | Test Result   | Message                                                                                            |
    |----------------------+---------------+----------------------------------------------------------------------------------------------------|
    | Versioning Readiness | Passed        | Verified cluster readiness:                                                                        |
    |                      |               |    Secondary NCC, if present, is ready and operational.                                            |
    |                      |               |    The cluster is not currently performing any other versioning operation.                         |
    | Download In-Progress | Passed        | Verified packages download status:                                                                 |
    |                      |               |    There are no packages that are being downloaded to the cluster.                                 |
    | DNOS Target Version  | Passed        | Verified DNOS target version validity:                                                             |
    |                      |               |    DNOS target version is higher than current installed version                                    |
    | Stack Validity       | Failed        | Target stack is empty                                                                              |
    | Disk Partition       | Passed        | Verified disk space and mount:                                                                     |
    |                      |               |    Cluster's nodes have enough space to perform versioning operations and all of them are mounted. |
    | Repo Replication     | Passed        | Verified repository synchronization:                                                               |
    |                      |               |    The standby NCC, if present, is synchronized over stack configurations and packages.            |
    | Packages Validity    | Passed        | Verified packages validity:                                                                        |
    |                      |               |    Stack packages' integrity checksum was verified.                                                |
    | Packages Signature   | Passed        | Verified packages signature:                                                                       |
    |                      |               |    DN-signed stack packages' have been verified to be sourced from DN.                             |

.. **Help line:** Displays the result of the last 50 target stack pre-check commands.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 18.2.1  | Command introduced                  |
+---------+-------------------------------------+

---

## show system target-stack pre-check.rst

show system target-stack pre-check
-------------------------------------

**Minimum user role:** viewer

To display the result of the last target-stack pre-check command.

**Command syntax: show system target-stack pre-check**

**Command mode:** GI

**Note**

- If no target-stack pre-check command was conducted prior to the show command, it will display an empty output.

**Example**
::

    Task ID:		    1688987412517
    Task status:		DONE
    Task start time:	2023-07-10 11:10:12
    Task finish time:	2023-07-10 11:10:12
    Pre-check result:	Failed
    Tests info:

    | Test Name            | Test Result   | Message                                                                                 |
    |----------------------+---------------+-----------------------------------------------------------------------------------------|
    | Disk Partition       | Failed        | ncc0: Partition 'docker' is lacking space: required: 500.00MB, available: 9B            |
    |                      |               | ncc1: Partition 'docker' is lacking space: required: 500.00MB, available: 9B            |
    | Packages Signature   | Failed        | Package: dnos_mock_package_1, authenticity: integrity-failed                            |
    | Versioning Readiness | Passed        | Verified cluster readiness:                                                             |
    |                      |               |    Secondary NCC, if present, is ready and operational.                                 |
    |                      |               |    The cluster is not currently performing any other versioning operation.              |
    | Download In-Progress | Passed        | Verified packages download status:                                                      |
    |                      |               |    There are no packages that are being downloaded to the cluster.                      |
    | DNOS Target Version  | Passed        | Verified DNOS target version validity:                                                  |
    |                      |               |    DNOS target version is higher than current installed version                         |
    | Stack Validity       | Passed        | Verified stack validity:                                                                |
    |                      |               |    Stack is not empty.                                                                  |
    |                      |               |    Target stack will not cause DNOS deletion.                                           |
    |                      |               |    All stack components' dependencies are met.                                          |
    | Repo Replication     | Passed        | Verified repository synchronization:                                                    |
    |                      |               |    The standby NCC, if present, is synchronized over stack configurations and packages. |
    | Packages Validity    | Passed        | Verified packages validity:                                                             |
    |                      |               |    Stack packages' integrity checksum was verified.                                     |

.. **Help line:** Displays the result of the last target stack pre-check command.

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 18.2.1  | Command introduced                  |
+---------+-------------------------------------+

---

## show system tech-support status.rst

show system tech-support status
-------------------------------

**Minimum user role:** viewer

To display the generation status of the tech-support file while in recovery mode:

**Command syntax: show system tech-support status**

**Command mode:** recovery

**Note**

If no tech-support file is currently being generated, information on the last generated tech-support file is displayed.

The file generation progress includes these steps:

- step 1/5 - preparing

- step 2/5 - discovering containers

- step 3/5 - running scripts on containers

- step 4/5 - collecting files on containers

- step 5/5 - creating archive

.. -  If no tech-support file currently generated, display last created tech-support file information

	-  Possible steps:

	- 1/5 preparing

	- 2/5 discovering containers

	- 3/5 running scripts on containers

	- 4/5 collecting files on containers

	- 5/5 creating archive

**Example**
::

	dnRouter# show system tech-support status

	Tech-support file generation in progress
	Tech-support file generation started at 13:32:00_30-01-2017, by User_1, running for 5 min
	File name MyTechSupportFile_13:32:00_30-01-2017.tar.gz
	Tech-support partition: total 98761166848, used: 11645157376, free: 87116009472, pct: 11.8% used
	Progress: step 3/5 - running scripts on containers

**Command History**

+---------+--------------------------------+
| Release | Modification                   |
+=========+================================+
| 11.2    | Command introduced             |
+---------+--------------------------------+
| 11.5    | Command added to recovery mode |
+---------+--------------------------------+
| 16.1    | Command added to gi mode       |
+---------+--------------------------------+


---


---

Total files:      167
