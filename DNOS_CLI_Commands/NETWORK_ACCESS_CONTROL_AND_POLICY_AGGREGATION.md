# Network Access Control and Policy Complete Aggregation

This file contains the complete content from all RST files in the following folders:
1. access-list (including subdirectories)
2. Access-lists  
3. Policy
4. Prefix-list

Total files: 45

These folders contain documentation for network access control, filtering policies, and routing prefix lists.


---

# SECTION 1: ACCESS-LIST

## Files from access-list folder and subdirectories

Files in this section: 11

### eth/embed-acl.rst

access-lists eth embed-acl
--------------------------

**Minimum user role:** operator

When you are required to create many rules that are common to many access-lists, the task of entering each rule individually for each access-list is extremely time-consuming. 
With the embedded functionality, you have the option to create an access-list with the common rules, and apply those rules to different access-lists, then use them in different interfaces across the system. 
By importing the embedded access-lists, the rules of the embedded access-list will be added at a preference matching the embedded rule-id + offset.
The default rules of embedded access-lists are not imported.
In the event of conflicting rules (where the rule-id of the imported embedded access-list overlaps a configured rule of the exclusive access-list), the exclusive access-list rules take precedence and will be installed in the datapath.

**Command syntax: embed-acl [acl-name]** offset [offset]

**Command mode:** config

**Hierarchies**

- access-lists eth

**Parameter table**

+-----------+----------------------------------------------------------------------------+---------+---------+
| Parameter | Description                                                                | Range   | Default |
+===========+============================================================================+=========+=========+
| acl-name  | embeded acl name                                                           | \-      | \-      |
+-----------+----------------------------------------------------------------------------+---------+---------+
| offset    | offset within the exclusive acl where the embedded acl rules will be added | 0-65434 | 0       |
+-----------+----------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# access-list
    dnRouter(cfg-acl)# eth eth_acl
    dnRouter(cfg-acl-eth)# embed-acl MY_EMBED_ACL

    dnRouter(cfg-acl-eth)# embed-acl MY_EMBED_ACL offset 3


**Removing Configuration**

To remove embed-acl:
::

    dnRouter(cfg-acl-eth)# no embed-acl MY_EMBED_ACL

To revert offset to default behavior:
::

    dnRouter(cfg-acl-eth)# no embed-acl MY_EMBED_ACL offset

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

### eth/eth.rst

access-lists eth
----------------

**Minimum user role:** operator

To configure an Ethernet access-list:

**Command syntax: eth [ethernet acl name]**

**Command mode:** config

**Hierarchies**

- access-lists

**Parameter table**

+-------------------+-----------------------------------------------------+-------+---------+
| Parameter         | Description                                         | Range | Default |
+===================+=====================================================+=======+=========+
| ethernet acl name | Reference to the configured name of the access-list | \-    | \-      |
+-------------------+-----------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# access-list
    dnRouter(cfg-acl)# eth eth_acl
    dnRouter(cfg-acl-eth)#


**Removing Configuration**

To remove eth acl:
::

    dnRouter(cfg-acl)# no eth eth_acl

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

### eth/rule_description.rst

access-lists eth rule description
---------------------------------

**Minimum user role:** operator

Add a description for the access-list rule. 
The description is for information only. 
It is not installed in the data plane.

To add a rule description:

**Command syntax: rule [rule id] description [description]**

**Command mode:** config

**Hierarchies**

- access-lists eth

**Parameter table**

+-------------+----------------------------------------------------------+------------------+---------+
| Parameter   | Description                                              | Range            | Default |
+=============+==========================================================+==================+=========+
| rule id     | Specify ACL rule index , lower index get higher priority | 1-65434          | \-      |
+-------------+----------------------------------------------------------+------------------+---------+
| description | Description text for description rules                   | | string         | \-      |
|             |                                                          | | length 1-256   |         |
+-------------+----------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# access-list
    dnRouter(cfg-acl)# eth eth_acl
    dnRouter(cfg-acl-eth)# rule 1 description "my acl description"


**Removing Configuration**

To remove rule:
::

    dnRouter(cfg-acl-eth)# no rule 1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

### eth/rule/description.rst

access-lists eth rule description
---------------------------------

**Minimum user role:** operator

To configure a destination for a specific allow / deny rule:

**Command syntax: description [rule-description]**

**Command mode:** config

**Hierarchies**

- access-lists eth rule

**Parameter table**

+------------------+-----------------------------------------+------------------+---------+
| Parameter        | Description                             | Range            | Default |
+==================+=========================================+==================+=========+
| rule-description | Description text for an allow/deny rule | | string         | \-      |
|                  |                                         | | length 1-256   |         |
+------------------+-----------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# access-list
    dnRouter(cfg-acl)# eth eth_acl
    dnRouter(cfg-acl-eth)# rule 1 deny
    dnRouter(cfg-acl-eth-rule-1)# description "DENY ALL"


**Removing Configuration**

To remove description
::

    dnRouter(cfg-acl-eth-rule-1)# no description

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

### eth/rule/dest-mac.rst

access-lists eth rule dest-mac
------------------------------

**Minimum user role:** operator

To configure a destination MAC address match condition:

**Command syntax: dest-mac [destination-mac-address]**

**Command mode:** config

**Hierarchies**

- access-lists eth rule

**Parameter table**

+-------------------------+--------------------------------------------------------------------------+-----------+---------+
| Parameter               | Description                                                              | Range     | Default |
+=========================+==========================================================================+===========+=========+
| destination-mac-address | Destination IEEE 802 MAC address. Destination IEEE 802 MAC address mask. | \-/[1-48] | \-/\-   |
+-------------------------+--------------------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# access-list
    dnRouter(cfg-acl)# eth eth_acl
    dnRouter(cfg-acl-eth)# rule 1 deny
    dnRouter(cfg-acl-eth-rule-1)# dest-mac 10:22:33:44:55:00/48

    dnRouter(cfg-acl-eth)# rule 2 allow
    dnRouter(cfg-acl-eth-rule-2)# dest-mac 10:22:33:44:00:00/32


**Removing Configuration**

To remove dest-mac
::

    dnRouter(cfg-acl-eth-rule-1)# no dest-mac

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

### eth/rule/ether-type.rst

access-lists eth rule ether-type
--------------------------------

**Minimum user role:** operator

Ethernet type reflects the upper layer protocol within the Ethernet frame (regardless of vlan tagging).
To configure destination mac address match condition:

**Command syntax: ether-type [ether-type]**

**Command mode:** config

**Hierarchies**

- access-lists eth rule

**Parameter table**

+------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter  | Description                                                                      | Range | Default |
+============+==================================================================================+=======+=========+
| ether-type | The Ethernet Type (or Length) value represented in the canonical order defined   | \-    | \-      |
|            | by IEEE 802. The canonical representation uses lowercase characters. It          |       |         |
|            | represent the carried protocol within the ethernet frame.  Note: This is not the |       |         |
|            | most ideal way to define ether-types. Ether-types are well known types and are   |       |         |
|            | registered with RAC in IEEE. So they should well defined types with values. For  |       |         |
|            | now this model is defining it as a string. There is a note out to IEEE that      |       |         |
|            | needs to be turned into a liaison statement asking them to define all            |       |         |
|            | ether-types for the industry to use.                                             |       |         |
+------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# access-list
    dnRouter(cfg-acl)# eth eth_acl
    dnRouter(cfg-acl-eth)# rule 1 allow
    dnRouter(cfg-acl-eth-rule-1)# ether-type ipv4_0x0800


**Removing Configuration**

To remove ether-type match:
::

    dnRouter(cfg-acl-eth-rule-1)# no ether-type

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

### eth/rule/inner-vlan.rst

access-lists eth rule inner-vlan
--------------------------------

**Minimum user role:** operator

To match per inner vlan (C tag) value:

**Command syntax: inner-vlan [inner-vlan]**

**Command mode:** config

**Hierarchies**

- access-lists eth rule

**Note**

- When the inner-vlan match condition is required, a packet must be double-tagged or more to match. Commit validation is expected in the event that packet-type is untagged or single-tagged.

**Parameter table**

+------------+------------------------------+--------+---------+
| Parameter  | Description                  | Range  | Default |
+============+==============================+========+=========+
| inner-vlan | Source IEEE 802 MAC address. | 1-4094 | \-      |
+------------+------------------------------+--------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# access-list
    dnRouter(cfg-acl)# eth eth_acl
    dnRouter(cfg-acl-eth)# rule 1 allow
    dnRouter(cfg-acl-eth-rule-1)# innver-vlan 100


**Removing Configuration**

To remove inner-vlan
::

    dnRouter(cfg-acl-eth-rule-1)# no inner-vlan

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

### eth/rule/outer-vlan.rst

access-lists eth rule outer-vlan
--------------------------------

**Minimum user role:** operator

To match per outer vlan (S tag) value:

**Command syntax: outer-vlan [outer-vlan]**

**Command mode:** config

**Hierarchies**

- access-lists eth rule

**Note**

- When the outer-vlan match condition is required, a packet must be double-tagged or more to match. Commit validation is expected in the event that packet-type is untagged or single-tagged.

**Parameter table**

+------------+------------------------------+--------+---------+
| Parameter  | Description                  | Range  | Default |
+============+==============================+========+=========+
| outer-vlan | Source IEEE 802 MAC address. | 1-4094 | \-      |
+------------+------------------------------+--------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# access-list
    dnRouter(cfg-acl)# eth eth_acl
    dnRouter(cfg-acl-eth)# rule 1 allow
    dnRouter(cfg-acl-eth-rule-1)# outer-vlan 100


**Removing Configuration**

To remove outer-vlan
::

    dnRouter(cfg-acl-eth-rule-1)# no outer-vlan

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

### eth/rule/packet-type.rst

access-lists eth rule packet-type
---------------------------------

**Minimum user role:** operator

Enter the packet type: untagged, single-tagged, double-tagged.

**Command syntax: packet-type [packet-type]**

**Command mode:** config

**Hierarchies**

- access-lists eth rule

**Parameter table**

+-------------+-----------------------------------+-------------------+---------+
| Parameter   | Description                       | Range             | Default |
+=============+===================================+===================+=========+
| packet-type | packet-type of the recieved frame | | untagged        | \-      |
|             |                                   | | single-tagged   |         |
|             |                                   | | double-tagged   |         |
+-------------+-----------------------------------+-------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# access-list
    dnRouter(cfg-acl)# eth eth_acl
    dnRouter(cfg-acl-eth)# rule 1 allow
    dnRouter(cfg-acl-eth-rule-1)# packet-type single-tagged


**Removing Configuration**

To remove allow
::

    no allow

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

### eth/rule/rule.rst

access-lists eth rule
---------------------

**Minimum user role:** operator

Enter rule configuration hierarchy.

**Command syntax: rule [rule id] [rule-type]**

**Command mode:** config

**Hierarchies**

- access-lists eth

**Parameter table**

+-----------+------------------------------------------------------------+-----------------+---------+
| Parameter | Description                                                | Range           | Default |
+===========+============================================================+=================+=========+
| rule id   | Specify ACL rule index , lower index get higher priority   | 1-65434         | \-      |
+-----------+------------------------------------------------------------+-----------------+---------+
| rule-type | Action that will be done upon rule match (e.g. deny/allow) | | allow         | \-      |
|           |                                                            | | deny          |         |
|           |                                                            | | description   |         |
+-----------+------------------------------------------------------------+-----------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# access-list
    dnRouter(cfg-acl)# eth eth_acl
    dnRouter(cfg-acl-eth)# rule 1 allow
    dnRouter(cfg-acl-eth-rule-1)#


**Removing Configuration**

To remove rule:
::

    dnRouter(cfg-acl-eth)# no rule 1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

### eth/rule/src-mac.rst

access-lists eth rule src-mac
-----------------------------

**Minimum user role:** operator

To configure source mac address match condition:

**Command syntax: src-mac [source-mac-address]**

**Command mode:** config

**Hierarchies**

- access-lists eth rule

**Parameter table**

+--------------------+----------------------------------------------------------------+-----------+---------+
| Parameter          | Description                                                    | Range     | Default |
+====================+================================================================+===========+=========+
| source-mac-address | Source IEEE 802 MAC address. Source IEEE 802 MAC address mask. | \-/[1-48] | \-/\-   |
+--------------------+----------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# access-list
    dnRouter(cfg-acl)# eth eth_acl
    dnRouter(cfg-acl-eth)# rule 1 allow
    dnRouter(cfg-acl-eth-rule-1)# src-mac 10:22:33:44:55:00/48

    dnRouter(cfg-acl-eth)# rule 2 allow
    dnRouter(cfg-acl-eth-rule-2)# src-mac 10:22:33:44:00:00/32


**Removing Configuration**

To remove source mac address match condition
::

    dnRouter(cfg-acl-eth-rule-1)# no src-mac

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---


# SECTION 2: ACCESS-LISTS

## Files from Access-lists folder

Files in this section: 24

### access-list rule commands.rst

access-list rule commands
-------------------------
An access-list is an ordered set of rules for filtering traffic. Each rule specifies conditions that a packet must satisfy for the rule to apply. There are two types of rules: "allow" and "deny". The system examines each packet against the conditions of all rules in each access-list. If it finds no match, it applies the default rule (deny). If it finds a match, it acts according to the rule: it allows packets that match an "allow" rule and drops packets that match a "deny" rule.
You can use access lists to protect your network by controlling which traffic to allow to which part of your internal network, or to an external network.
DNOS supports IPv4 and IPv6 access-lists for security traffic filtering.
Access-lists commands are hierarchical. You can create multiple access-lists with multiple rules in each access-list. To configure an access-list:
1.	Create an access list. See access-lists.
2.	Create rules. See access-lists rule.
3.	Attach the access-list to an interface. See interfaces access-list.
The following table summarizes the rule commands available:

+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| Commands      | IPv4 in | IPv4 out | IPv6 in | IPv6 out | CP IPv4 | CP IPv6  |  Global in IPv4 | Global in IPv6  |
+===============+=========+==========+=========+==========+=========+==========+=================+=================+
| src-ip        | \+      | \+       | \+      | \+       | \+      | \+       | \+              | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| src-port      | \+      | \+       | \+      | \+       | \+      | \+       | \+              | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| dest-ip       | \+      | \+       | \+      | \+       | \+      | \+       | \+              | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| dst-ip        | \+      | \+       | \+      | \+       | \+      | \+       | \+              | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| dscp          | \+      | \+       | \+      | \+       | \+      | \+       | \+              | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| protocol      | \+      | \+       | \+      | \+       | \+      |          | \+              | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| icmp          | \+      | \+       |         |          |         | \+       | \+              |                 |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| ipv6-icmp     |         |          | \+      | \+       |         |          |                 | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| tcp-flag      | \+      | \+       | \+      |          | \+      | \+       | \+              | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| fragmented    | \+      | \+       | \+      |          | \+      | \+       | \+              | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| ipv4-option   | \+      | \+       |         |          | \+      |          | \+              |                 |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| next-hop1     | \+      |          | \+      |          |         |          | \+              | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| next-table    | \+      |          | \+      |          |         |          | \+              | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| vrf           |         |          |         |          | \+      | \+       |                 |                 |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| Packet Length | \+      |          | \+      |          | \+      | \+       | \+              | \+              |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| set-qos       | \+      |          | \+      |          |         |          |                 |                 |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| log           | \+      |          | \+      |          | \+      | \+       |                 |                 |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+
| rate          | \+      | \+       | \+      | \+       |         |          |                 |                 |
+---------------+---------+----------+---------+----------+---------+----------+-----------------+-----------------+



---

### access-list rule rate.rst

access-lists rule rate
----------------------

**Minimum user role:** operator

An access list rule can be configured with rate limit and burst to police the traffic which is matched against the rule.
Rate limit action is relevant to allow rules only and is not applicable for management interfaces access lists (in-band and OOB).

To configure the rate action:

**Command syntax: rule [rule-id] allow** rate [rate-limit] burst [burst-size]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**
- rate action is allowed only for allow rules under ingress and egress access-list (not for in-band-management access-list).
- rate units are killo bits per second.
- rate units are killo bytes.


**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                            |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range                      | Default     |
+=====================+=================================================================================================================================================================================================================================================+============================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                            |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000                  | 131071      |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any".                                                                                                                                                             |                            |             |
|                     |                                                                                                                                                                                                                                                 |                            |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                            |             |
|                     |                                                                                                                                                                                                                                                 |                            |             |
|                     | You can configure up to 2000 rules per access-list and up to 250,000 rules altogether per system.                                                                                                                                               |                            |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------+-------------+
|                     | Defines whether the traffic matching the rule conditions   are to be allowed or denied.                                                                                                                                                         |                            |             |
| rule-type           |                                                                                                                                                                                                                                                 | allow                      | \-          |
|                     |                                                                                                                                                                                                                                                 |                            |             |
|                     |                                                                                                                                                                                                                                                 | deny                       |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                            |             |
| rate                | Define rate in killo bits per second to police the traffic matched against this rule.                                                                                                                                                           | 64..1000000000             | \-          |
|                     |                                                                                                                                                                                                                                                 |                            |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                            |             |
| burst               | Define burst-size in killo bytes for the policer configured on the rule.                                                                                                                                                                        | 50-255000                  | 200         |
|                     |                                                                                                                                                                                                                                                 |                            |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 100 allow src-ip 1.1.1.1/32 rate 1000 burst 200 
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow src-ip 2001:abcd::0/127 rate 1000

**Removing Configuration**

To remove the rule configuration:
::

	dnRouter(cfg-acl-ipv4)# no rule 102 allow src-ip 1.1.1.1/32 rate

.. **Help line:** Configure access-lists rate action.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
| 19.3        | Command introduced    |
+-------------+-----------------------+

---

### access-lists embed-acl.rst

access-lists embed-acl
----------------------

**Minimum user role:** operator


When you are required to create many rules that are common to many access-lists, the task of entering each rule individually to each access-list is extremely time-consuming. With the embedded functionality, you have the option to create an access-list with the common rules and apply those rules to a different access-lists and then use them in different interfaces across the system. By importing the embedded access-list, the rules of the embedded access-list will be added at a preference matching the embedded rule-id + offset.

The default rules of embedded access-list are not imported.

In-case of conflicting rules (where the rule-id of the imported embedded access-list overlaps a configured rule of the exclusive access-list), the exclusive access-list rules take precedence and will be installed in the datapath.

**Command syntax: embed-acl [access-list-name]** offset [offset]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule 

- access-lists ipv6 rule

**Note**

- The embedded access-list must match the type of the exclusive access-list (IPv4, IPv6). 

.. - Upon auto-complete, only matching type ACL will be shown. Commit validation is required

- Only one embedded access-list can be imported to an exclusive access-list.

- An embedded access-list that is imported to an exclusive access-list cannot have an embedded access-list called within it.

.. - required the following commit validation - the embedded-acl maximum configured rule-id + offset within the given exclusive ACL must be smaller than default rule-id. I.e: embedded-acl maximum configured rule-id + offset < 130001

- The embedded-acl maximum configured rule-id + the offset value within the exclusive ACL must be smaller than the default rule-id.


**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------+-------------+-------------+
|                     |                                                                                           |             |             |
| Parameter           | Description                                                                               | Range       | Default     |
+=====================+===========================================================================================+=============+=============+
|                     |                                                                                           |             |             |
| access-list-name    | The configured ACL name.                                                                  | String      | \-          |
+---------------------+-------------------------------------------------------------------------------------------+-------------+-------------+
|                     |                                                                                           |             |             |
| offset              | Allows inserting an embedded ACL in the middle of an already existing list of rules.      | 0..130000   | 0           |
+---------------------+-------------------------------------------------------------------------------------------+-------------+-------------+


**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# embed-acl MY_EMBEDDED_IPV4_ACL
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# embed-acl MY_EMBEDDED_IPV6_ACL offset 100
	dnRouter(cfg-acl-ipv6)# exit


**Removing Configuration**

To remove the embedded access-list from the exclusive access-list configuration:
::

	dnRouter(cfg-acl-ipv4)# no embed-acl MY_EMBEDDED_IPV4_ACL

To revert the embedded access-list's offset to the default value:
::

	dnRouter(cfg-acl-ipv6)# no embed-acl MY_EMBEDDED_IPV6_ACL offset 100

.. **Help line:** Set an embedded ACL

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 15.1        | Command introduced    |
+-------------+-----------------------+

---

### access-lists rule allow_deny description.rst

access-lists rule allow/deny description
----------------------------------------

**Minimum user role:** operator

Add a description for the access-list action rule. The description is for information only. It is not installed in the data plane.

To add a rule description:

**Command syntax: rule [rule-id] [rule-type]** [description]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- The description rule occupies rule-id. It cannot share a rule-id with another allow/deny rule.


**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                   |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range             | Default     |
+=====================+=================================================================================================================================================================================================================================================+===================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                   |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000         | 131071      |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any".                                                                                                                                                             |                   |             |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                   |             |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     | You can configure up to 2000 rules per access-list and up to 250,000 rules altogether per system.                                                                                                                                               |                   |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| rule-type           |                                                                                                                                                                                                                                                 |                   |             |
|                     | Defines whether the traffic matching the rule   conditions are to be allowed or denied.                                                                                                                                                         | allow             | \-          |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     |                                                                                                                                                                                                                                                 | deny              |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                   |             |
| description         | Add a description for the access-list rule.                                                                                                                                                                                                     | 256 characters    | \-          |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     | Enter free-text description with spaces in   between quotation marks. If you do not use quotation marks, do not use   spaces. For example:                                                                                                      |                   |             |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     | ... description "My long   description"                                                                                                                                                                                                         |                   |             |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     | ... description   My_long_description                                                                                                                                                                                                           |                   |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+



**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 allow description "this is allow-all rule"
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv4)# rule 200 deny description this_is_deny_all_rule



**Removing Configuration**

To remove the description:
::

	dnRouter(cfg-acl-ipv6)# rule 200 deny description


.. **Help line:** Configure description rule

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 19.2        | Command introduced    |
+-------------+-----------------------+

---

### access-lists rule description.rst

access-lists rule description
-----------------------------

**Minimum user role:** operator

Add a description for the access-list rule. The description is for information only. It is not installed in the data plane.

To add a rule description:

**Command syntax: rule [rule-id] description [description]** 

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- The description rule occupies rule-id. It cannot share a rule-id with another allow/deny rule.
- Description rules does not count for ACL scale limit


**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                   |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range             | Default     |
+=====================+=================================================================================================================================================================================================================================================+===================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                   |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000         | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                   |             |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                   |             |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                   |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| rule-type           |                                                                                                                                                                                                                                                 |                   |             |
|                     | Defines whether the traffic matching the rule   conditions are to be allowed or denied.                                                                                                                                                         | allow             | \-          |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     |                                                                                                                                                                                                                                                 | deny              |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                   |             |
| description         | Add a description for the access-list rule.                                                                                                                                                                                                     | 256 characters    | \-          |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     | Enter free-text description with spaces in   between quotation marks. If you do not use quotation marks, do not use   spaces. For example:                                                                                                      |                   |             |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     | ... description "My long   description"                                                                                                                                                                                                         |                   |             |
|                     |                                                                                                                                                                                                                                                 |                   |             |
|                     | ... description   My_long_description                                                                                                                                                                                                           |                   |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+



**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 description "this is my first ACL"
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv4)# rule 200 description this_is_my_second_ACL



**Removing Configuration**

To remove the description:
::

	dnRouter(cfg-acl-ipv6)# no rule 100 description


.. **Help line:** Configure description rule

**Command History**

+-------------+-------------------------------+
|             |                               |
| Release     | Modification                  |
+=============+===============================+
|             |                               |
| 11.0        | Command introduced            |
+-------------+-------------------------------+
|             |                               |
| 19.2        | Fix rule-type documentation   |
+-------------+-------------------------------+
|             |                               |
| 19.3        | Updated rule-id range         |
+-------------+-------------------------------+
---

### access-lists rule dest-ip.rst

access-lists rule dest-ip
-------------------------

**Minimum user role:** operator

To create an access-list for the destination IP:

**Command syntax: rule [rule-id] [rule-type]** dest-ip [dest-ip]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- IPv6 inverse mask is not supported on Broadcom J3-AI based platforms.
- The destination IP address type format must match the access-list type (IPv4/IPv6).
- When mask is provided for dest-ip, mask is handled as inverse-mask. In inverse-mask, a mask 0 value bit reflect a bit in the ip address which value must be matched. A mask 1 value bit reflect a  a bit in the ip address which can be of either value.
-  Example: 

::
	dest-ip 10.10.10.10/0.0.4.0 will match both 10.10.10.10 and 10.10.14.10 source ip addresses
	dest-ip 2006:18:91::2/1:: will match both 2006:18:91::2 and 2007:18:91::2 source ip addresses

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                    |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range              | Default     |
+=====================+=================================================================================================================================================================================================================================================+====================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                    |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000          | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                    |             |
|                     |                                                                                                                                                                                                                                                 |                    |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                    |             |
|                     |                                                                                                                                                                                                                                                 |                    |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                    |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                    |             |
| rule-type           | Defines whether the traffic matching the rule   conditions are to be allowed or denied.                                                                                                                                                         | allow              | \-          |
|                     |                                                                                                                                                                                                                                                 |                    |             |
|                     |                                                                                                                                                                                                                                                 | deny               |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                    |             |
| dest-ip             | The source IPs. Can be a specific host, a network or group of hosts, or any host.                                                                                                                                                               | A.B.C.D/x          | any         |
|                     |                                                                                                                                                                                                                                                 | A.B.C.D/X.Y.Z.W    |             |
|                     |                                                                                                                                                                                                                                                 | x:x::x:x/m         |             |
|                     |                                                                                                                                                                                                                                                 | x:x::x:x/m:m::m:m  |             |
|                     |                                                                                                                                                                                                                                                 | any                |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+


**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 allow dest-ip 1.2.3.4/20
	dnRouter(cfg-acl-ipv4)# rule 102 deny dest-ip 1.1.1.1/32
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow dest-ip 2001:abcd::0/127

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_3
	dnRouter(cfg-acl-ipv6)# rule 200 allow dest-ip 2006:18:91::2/1::


**Removing Configuration**

To delete a rule configuration:
::

	dnRouter(cfg-acl-ipv6)# no rule 200 allow dest-ip


.. **Help line:** Configure access-lists rule destination IP

**Command History**

+-------------+--------------------------+
|             |                          |
| Release     | Modification             |
+=============+==========================+
|             |                          |
| 5.1.0       | Command introduced       |
+-------------+--------------------------+
|             |                          |
| 6.0         | Applied new hierarchy    |
+-------------+--------------------------+
|             |                          |
| 19.3        | Updated rule-id range    |
+-------------+--------------------------+
|             |                          |
| 25.2        | Add inverse-mask support |
+-------------+--------------------------+
---

### access-lists rule dest-ports.rst

access-lists rule dest-ports
----------------------------

**Minimum user role:** operator

To create an access-list for the destination ports:

**Command syntax: rule [rule-id] [rule-type] protocol [protocol]** dest-ports [dest-ports]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- Destination ports can be configured as a range.

- Destination ports are supported only on protocol type tcp/udp.

- You can't configure more than 8 different ingress IPv4 ACL destination port ranges across all attached ACLs.

- You can't configure more than 8 different ingress IPv6 ACL destination port ranges across all attached ACLs.

- You can't configure more than 8 different IPv4 in-band-managment ACL destination port ranges.

- You can't configure more than 8 different IPv6 in-band-managment ACL destination port ranges.

- For egress IPv4 ACL, you can't configure more than 24 unique combinations of SrcPortMin, SrcPortMax, DstPortMin, DstPortMax.

- Destination port range is not supported for egress IPv6 ACL

- If you remove the protocol field, the ports field will be removed.

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range                | Default     |
+=====================+=================================================================================================================================================================================================================================================+======================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                      |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000            | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                      |             |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                      |             |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                      |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
| rule-type           |                                                                                                                                                                                                                                                 |                      |             |
|                     | Defines whether the traffic matching the rule   conditions are to be allowed or denied.                                                                                                                                                         | allow                | \-          |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     |                                                                                                                                                                                                                                                 | deny                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| protocol            | The protocol used for the traffic.                                                                                                                                                                                                              | See protocol list    | \-          |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | You can enter the protocol name or use the protocol ID. The protocol ID is displayed in hexadecimal next to each protocol.                                                                                                                      |                      |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| dest-ports          | The destination ports.                                                                                                                                                                                                                          | 0..65535             | Any         |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | Destination ports can be configured as a range.                                                                                                                                                                                                 |                      |             |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | Destination ports are supported only for protocol   TCP and UDP.                                                                                                                                                                                |                      |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 allow dest-ip 1.2.3.4/20 protocol tcp(0x06) dest-ports 123
	dnRouter(cfg-acl-ipv4)# rule 102 deny protocol tcp(0x06) dest-ports 300
	dnRouter(cfg-acl-ipv4)# rule 103 deny protocol 0x11 dest-ports 123
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow protocol udp(0x11) dest-ports 100-200
	dnRouter(cfg-acl-ipv6)# rule 300 deny src-ip 2001::1 protocol udp(0x11) dest-ports 179
	dnRouter(cfg-acl-ipv6)# rule 400 deny protocol 0x11 dest-ports 179

**Removing Configuration**

To delete a rule configuration:
::

	dnRouter(cfg-acl-ipv6)# no rule 300 allow dest-ports


.. **Help line:** Configure access-lists destination ports

**Command History**

+-------------+--------------------------+
|             |                          |
| Release     | Modification             |
+=============+==========================+
|             |                          |
| 5.1.0       | Command introduced       |
+-------------+--------------------------+
|             |                          |
| 6.0         | Applied new hierarchy    |
+-------------+--------------------------+
|             |                          |
| 19.3        | Updated rule-id range    |
+-------------+--------------------------+

---

### access-lists rule dscp.rst

access-lists rule dscp
----------------------

**Minimum user role:** operator

To create an access-list to match a specific DSCP value:

**Command syntax: rule [rule-id] [rule-type]** dscp [dscp]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule


**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
|                     |                                                                                                                                                                                                                                                 |             |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range       | Default     |
+=====================+=================================================================================================================================================================================================================================================+=============+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |             |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000   | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |             |             |
|                     |                                                                                                                                                                                                                                                 |             |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |             |             |
|                     |                                                                                                                                                                                                                                                 |             |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |             |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
|                     | Defines whether the traffic matching the rule conditions are to be allowed or denied.                                                                                                                                                           |             |             |
| rule-type           |                                                                                                                                                                                                                                                 | allow       | \-          |
|                     |                                                                                                                                                                                                                                                 |             |             |
|                     |                                                                                                                                                                                                                                                 | deny        |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
|                     |                                                                                                                                                                                                                                                 |             |             |
| dscp                | Used to configure an access-list rule to match a   specific DSCP value.                                                                                                                                                                         | 0..63       | Any         |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 100 allow dscp 56
	dnRouter(cfg-acl-ipv4)# rule 101 allow src-ip 1.2.3.4/20 dscp 48
	dnRouter(cfg-acl-ipv4)# rule 102 deny dest-ip 1.1.1.1/32 dscp 32 protocol tcp src-ports 100-200


	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 10 deny src-ip 2001::1 dscp 56

**Removing Configuration**

To delete a rule configuration:
::

	dnRouter(cfg-acl-ipv4)# no rule 101 allow dscp


.. **Help line:** Configure access-lists rule dscp

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.0        | Command introduced    |
+-------------+-----------------------+
|             |                       |
| 19.3        | Updated rule-id range |
+-------------+-----------------------+

---

### access-lists rule fragmented.rst

access-lists rule fragmented
----------------------------

**Minimum user role:** operator

To create an access-list to match fragmented packets:

**Command syntax: rule [rule-id] [rule-type]** fragmented

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- This command is applicable to access-list-type IPv4 or IPv6. For IPv6, when setting a match for fragmented and IP protocol, protocol must be either tcp(0x06) or udp(0x11).

- A fragmented keyword can only be configured when an L4 header is not explicitly configured in an access-list.

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+-------------+
|                     |                                                                                                                                                                                                                                                 |               |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range         | Default     |
+=====================+=================================================================================================================================================================================================================================================+===============+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |               |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000     | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |               |             |
|                     |                                                                                                                                                                                                                                                 |               |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |               |             |
|                     |                                                                                                                                                                                                                                                 |               |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |               |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+-------------+
|                     | Defines whether the traffic matching the rule conditions are to be allowed or denied.                                                                                                                                                           |               |             |
| rule-type           |                                                                                                                                                                                                                                                 | allow         | \-          |
|                     |                                                                                                                                                                                                                                                 |               |             |
|                     |                                                                                                                                                                                                                                                 | deny          |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+-------------+
|                     |                                                                                                                                                                                                                                                 |               |             |
| fragmented          | Used to configure an access-list rule to match   fragmented packets.                                                                                                                                                                            | fragmented    | \-          |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+-------------+


**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 allow protocol icmp(0x01) icmp echo-reply ttl 0-10 fragmented


**Removing Configuration**

To delete a rule configuration:
::

	dnRouter(cfg-acl-ipv4)# no rule 101 allow fragmented


.. **Help line:** Configure access-lists fragmented flag

**Command History**

+-------------+-----------------------------+
|             |                             |
| Release     | Modification                |
+=============+=============================+
|             |                             |
| 5.1.0       | Command introduced          |
+-------------+-----------------------------+
|             |                             |
| 6.0         | Applied new hierarchy       |
+-------------+-----------------------------+
|             |                             |
| 13.0        | Updated support for IPv6    |
+-------------+-----------------------------+
|             |                             |
| 19.3        | Updated rule-id range       |
+-------------+-----------------------------+

---

### access-lists rule icmp.rst

access-lists rule icmp
-----------------------

**Minimum user role:** operator

To create an access-list for the ICMP protocol, use the following command:

**Command syntax: rule [rule-id] [rule-type] protocol icmp(0x01)** icmp-type [message-type]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- ICMP message-type are available only for ICMP (ipv4) protocol


**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                             |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range                       | Default     |
+=====================+=================================================================================================================================================================================================================================================+=============================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                             |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000                   | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                             |             |
|                     |                                                                                                                                                                                                                                                 |                             |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                             |             |
|                     |                                                                                                                                                                                                                                                 |                             |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                             |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+-------------+
|                     | Defines whether the traffic matching the rule conditions are to be allowed or denied.                                                                                                                                                           |                             |             |
| rule-type           |                                                                                                                                                                                                                                                 | allow                       | \-          |
|                     |                                                                                                                                                                                                                                                 |                             |             |
|                     |                                                                                                                                                                                                                                                 | deny                        |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                             |             |
| icmp                | Used to configure an access-list rule to match a specific ICMP message type.                                                                                                                                                                    | See ICMP message   types    | \-          |
|                     |                                                                                                                                                                                                                                                 |                             |             |
|                     | Applicable only to ICMP protocol.                                                                                                                                                                                                               |                             |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+-------------+

**ICMP message types**

+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| Keyword (string)                          | RFC type number | RFC code number | Meaning                                                           |
+===========================================+=================+=================+===================================================================+
| echo-reply                                | 0               | 0               | Echo Reply                                                        |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| destination-network-unreachable           | 3               | 0               | Destination unreachable-Destination network unreachable           |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| destination-host-unreachable              | 3               | 1               | Destination unreachable-Destination host unreachable              |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| destination-protocol-unreachable          | 3               | 2               | Destination unreachable-Destination protocol unreachable          |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| destination-port-unreachable              | 3               | 3               | Destination unreachable-Destination port unreachable              |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| fragmentation-required                    | 3               | 4               | Destination unreachable-Fragmentation required                    |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| source-route-failed                       | 3               | 5               | Destination unreachable-Source route failed                       |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| destination-network-unknown               | 3               | 6               | Destination unreachable-Destination network unknown               |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| destination-host-unknown                  | 3               | 7               | Destination unreachable-Destination host unknown                  |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| source-host-isolated                      | 3               | 8               | Destination unreachable-Source host isolated                      |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| network-administratively-prohibited       | 3               | 9               | Destination unreachable-Network administratively prohibited       |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| host-administratively-prohibited          | 3               | 10              | Destination unreachable-Host administratively prohibited          |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| network-unreachable-for-tos               | 3               | 11              | Destination unreachable-Network unreachable for ToS               |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| host-unreachable-for-tos                  | 3               | 12              | Destination unreachable-Host unreachable for ToS                  |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| communication-administratively-prohibited | 3               | 13              | Destination unreachable-Communication administratively prohibited |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| host-precedence-violation                 | 3               | 14              | Destination unreachable-Host Precedence Violation                 |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| precedence-cutoff-in-effect               | 3               | 15              | Destination unreachable-Precedence cutoff in effect               |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| redirect-network                          | 5               | 0               | Redirect Datagram-for the Network                                 |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| redirect-host                             | 5               | 1               | Redirect Datagram-for the Host                                    |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| redirect-tos-network                      | 5               | 2               | Redirect Datagram-for the ToS and network                         |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| redirect-tos-host                         | 5               | 3               | Redirect Datagram-for the ToS and host                            |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| echo-request                              | 8               | 0               | Echo Request                                                      |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| router-advertisement                      | 9               | 0               | Router Advertisement                                              |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| router-solicitation                       | 10              | 0               | Router Solicitation                                               |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| ttl-expired-in-transit                    | 11              | 0               | Time Exceeded-TTL expired in transit                              |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| fragment-reassembly                       | 11              | 1               | Time Exceeded-Fragment reassembly                                 |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| pointer-indicates-error                   | 12              | 0               | Parameter Problem-Pointer indicates error                         |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| missing-required-option                   | 12              | 1               | Parameter Problem-Missing required option                         |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| bad-length                                | 12              | 2               | Parameter Problem-Bad length                                      |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| timestamp                                 | 13              | 0               | Timestamp                                                         |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+
| timestamp-reply                           | 14              | 0               | Timestamp-Reply                                                   |
+-------------------------------------------+-----------------+-----------------+-------------------------------------------------------------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 100 allow protocol icmp(0x01) icmp-type echo-request
	dnRouter(cfg-acl-ipv4)# rule 101 allow protocol icmp(0x01) icmp-type echo-reply



**Removing Configuration**

To delete a rule configuration, the protocol value must be specific:
::

	dnRouter(cfg-acl-ipv4)# no rule 101 allow icmp-type

.. **Help line:** Configure access-lists rule icmp message type

**Command History**

+-------------+----------------------------------+
|             |                                  |
| Release     | Modification                     |
+=============+==================================+
|             |                                  |
| 5.1.0       | Command introduced               |
+-------------+----------------------------------+
|             |                                  |
| 6.0         | Applied new hierarchy            |
+-------------+----------------------------------+
|             |                                  |
| 9.0         | Not supported in this version    |
+-------------+----------------------------------+
|             |                                  |
| 11.0        | Command reintroduced             |
+-------------+----------------------------------+
|             |                                  |
| 19.3        | Updated rule-id range            |
+-------------+----------------------------------+

---

### access-lists rule ipv4-options.rst

access-lists rule ipv4-options
------------------------------

**Minimum user role:** operator

When configured, the ACCESS-LISTS rule validates if the ipv4-options header field exist in the packet IPv4 header. To create an access-list to match the IPv4-options header field:

**Command syntax: rule [rule-id] [rule-type]** ipv4-options

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- The ipv4-options parameter is available only for access-list type IPv4.

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range           | Default     |
+=====================+=================================================================================================================================================================================================================================================+=================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                 |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000       | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     | Defines whether the traffic matching the rule conditions are to be allowed or denied.                                                                                                                                                           |                 |             |
| rule-type           |                                                                                                                                                                                                                                                 | allow           | \-          |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     |                                                                                                                                                                                                                                                 | deny            |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| ipv4-options        | Used to configure an access-list rule to match   the existence of ipv4-options header field in the IPv4 packet's header.                                                                                                                        | IPv4 options    | \-          |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 100 allow ipv4-options
	dnRouter(cfg-acl-ipv4)# rule 101 allow protocol icmp(0x01) ipv4-options


**Removing Configuration**

To delete the access-list rule configuration:
::

	dnRouter(cfg-acl-ipv4)# no rule 101 allow ipv4-options


.. **Help line:** Configure access-lists rule protocol

**Command History**

+-------------+--------------------------+
|             |                          |
| Release     | Modification             |
+=============+==========================+
|             |                          |
| 5.1.0       | Command introduced       |
+-------------+--------------------------+
|             |                          |
| 6.0         | Applied new hierarchy    |
+-------------+--------------------------+
|             |                          |
| 19.3        | Updated rule-id range    |
+-------------+--------------------------+
---

### access-lists rule ipv6-icmp.rst

access-lists rule ipv6-icmp
----------------------------

**Minimum user role:** operator

To create an access-list for the IPv6-ICMP protocol, use the following command:

**Command syntax: rule [rule-id] [rule-type] protocol ipv6-icmp(0x3A)** icmpv6-type [message-type]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- ICMP-v6 messages are available only for ipv6-icmp protocol

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range           | Default     |
+=====================+=================================================================================================================================================================================================================================================+=================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                 |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000       | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     | Defines whether the traffic matching the rule conditions are to be allowed or denied.                                                                                                                                                           |                 |             |
| rule-type           |                                                                                                                                                                                                                                                 | allow           | \-          |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     |                                                                                                                                                                                                                                                 | deny            |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| icmp-v6             | Used to configure an access-list rule to match a   specific IPv6-ICMP message type.                                                                                                                                                             | ICMP v6 list    | \-          |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | Applicable only to IPv6-ICMP protocol.                                                                                                                                                                                                          |                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+


**ICMP-v6 message types**

+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| Keyword (string)                            | RFC type number | RFC code number | Meaning                                                             |
+=============================================+=================+=================+=====================================================================+
| no-route-to-destination                     | 1               | 0               | Destination unreachable-no route to destination                     |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| administratively-prohibited                 | 1               | 1               | Destination unreachable-administratively prohibited                 |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| beyond-scope-of-source-address              | 1               | 2               | Destination unreachable-beyond scope of source address              |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| address-unreachable                         | 1               | 3               | Destination unreachable-address unreachable                         |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| port-unreachable                            | 1               | 4               | Destination unreachable-port unreachable                            |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| source-address-failed-ingress/egress-policy | 1               | 5               | Destination unreachable-source address failed ingress/egress policy |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| reject-route-to-destination                 | 1               | 6               | Destination unreachable-reject route to destination                 |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| error-in-source-routing-header              | 1               | 7               | Destination unreachable-error in Source Routing Header              |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| packet-too-big                              | 2               | 0               | Packet Too Big                                                      |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| hop-limit-exceeded-in-transit               | 3               | 0               | Time Exceeded-hop limit exceeded in transit                         |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| fragment-reassembly-time-exceeded           | 3               | 1               | Time Exceeded-fragment reassembly time exceeded                     |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| erroneous-header-field-encountered          | 4               | 0               | Parameter Problem-erroneous header field encountered                |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| unrecognized-next-header-type-encountered   | 4               | 1               | Parameter Problem-unrecognized Next Header type encountered         |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| unrecognized-ipv6-option-encountered        | 4               | 2               | Parameter Problem-unrecognized IPv6 option encountered              |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| echo-request                                | 128             | 0               | Echo Request                                                        |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| echo-reply                                  | 129             | 0               | Echo Reply                                                          |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| multicast-listener-query                    | 130             | 0               | MLD-Multicast Listener Query                                        |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| multicast-listener-report                   | 131             | 0               | MLD-Multicast Listener Report                                       |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| multicast-listener-done                     | 132             | 0               | MLD-Multicast Listener Done                                         |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| router-solicitation                         | 133             | 0               | NDP-Router Solicitation                                             |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| router-advertisement                        | 134             | 0               | NDP-Router Advertisement                                            |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| neighbor-solicitation                       | 135             | 0               | NDP-Neighbor Solicitation                                           |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| neighbor-advertisement                      | 136             | 0               | NDP-Neighbor Advertisement                                          |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| redirect-message                            | 137             | 0               | NDP-Redirect Message                                                |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| renumbering-command                         | 138             | 0               | Router Renumbering-Command                                          |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| renumbering-result                          | 138             | 1               | Router Renumbering-Result                                           |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| renumbering-sequence-number-reset           | 138             | 255             | Router Renumbering-Sequence Number Reset                            |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| query-ipv6-address                          | 139             | 0               | ICMP Node Information-Query IPv6 address                            |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| query-name                                  | 139             | 1               | ICMP Node Information-Query name                                    |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| query-ipv4-address                          | 139             | 2               | ICMP Node Information-Query IPv4 address                            |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| response-successful                         | 140             | 0               | ICMP Node Information-Response successful                           |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| response-refuse                             | 140             | 1               | ICMP Node Information-Response refuse                               |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| response-unknown                            | 140             | 2               | ICMP Node Information-Response unknown                              |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| solicitation-message                        | 141             | 0               | Inverse Neighbor Discovery-Solicitation Message                     |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| advertisement-message                       | 142             | 0               | Inverse Neighbor Discovery-Advertisement Message                    |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| mldv2-reports                               | 143             |                 | MLDv2-reports                                                       |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| discovery-request-message                   | 144             | 0               | Home Agent Address-Discovery Request Message                        |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| discovery-reply-message                     | 145             | 0               | Home Agent Address-Discovery Reply Message                          |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| mobile-prefix-solicitation                  | 146             | 0               | Mobile Prefix-Solicitation                                          |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| mobile-prefix-advertisement                 | 147             | 0               | Mobile Prefix-Advertisement                                         |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| certification-path-solicitation             | 148             |                 | SEND-Certification Path Solicitation                                |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| certification-path-advertisement            | 149             |                 | SEND-Certification Path Advertisement                               |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| mrd-advertisement                           | 151             |                 | MRD-Advertisement                                                   |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| mrd-solicitation                            | 152             |                 | MRD-Solicitation                                                    |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| mrd-termination                             | 153             |                 | MRD-Termination                                                     |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+
| rpl-control-message                         | 155             |                 | RPL-Control Message                                                 |
+---------------------------------------------+-----------------+-----------------+---------------------------------------------------------------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_1
	dnRouter(cfg-acl-ipv6)# rule 100 allow protocol ipv6-icmp(0x3A) icmpv6-type no-route-to-destination
	dnRouter(cfg-acl-ipv6)# rule 101 allow protocol ipv6-icmp(0x3A) icmpv6-type hop-limit-exceeded-in-transit



**Removing Configuration**

To delete a rule configuration:
::

	dnRouter(cfg-acl-ipv6)# no rule 100 allow icmpv6-type

.. **Help line:** Configure access-lists rule ipv6-icmp message type

**Command History**

+-------------+----------------------------------+
|             |                                  |
| Release     | Modification                     |
+=============+==================================+
|             |                                  |
| 5.1.0       | Command introduced               |
+-------------+----------------------------------+
|             |                                  |
| 6.0         | Applied new hierarchy            |
+-------------+----------------------------------+
|             |                                  |
| 9.0         | Not supported in this version    |
+-------------+----------------------------------+
|             |                                  |
| 11.0        | Command reintroduced             |
+-------------+----------------------------------+
|             |                                  |
| 19.3        | Updated rule-id range            |
+-------------+----------------------------------+

---

### access-lists rule log.rst

access-lists rule log
---------------------

**Minimum user role:** operator

You can configure the system to send a syslog event when there is a match on specfic access list rules. This can be achieved by using the "log" action in access-lists rule configurations. Log action can be added to allow/deny/next-hop rules.

To configure the log action:

**Command syntax: rule [rule-id] [rule-type]** log

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**
- log action is allowed only for ingress access-list and in-band-management access-list.


**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range           | Default     |
+=====================+=================================================================================================================================================================================================================================================+=================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                 |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000       | 131071      |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any".                                                                                                                                                             |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | You can configure up to 2000 rules per access-list and up to 250,000 rules altogether per system.                                                                                                                                               |                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     | Defines whether the traffic matching the rule conditions   are to be allowed or denied.                                                                                                                                                         |                 |             |
| rule-type           |                                                                                                                                                                                                                                                 | allow           | \-          |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     |                                                                                                                                                                                                                                                 | deny            |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| log                 | Define wether to trigger syslog sending for this rule.                                                                                                                                                                                          |                 | \-          |
|                     |                                                                                                                                                                                                                                                 |                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 102 deny src-ip 1.1.1.1/32 log
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 deny src-ip 2001:abcd::0/127 log

**Removing Configuration**

To remove the rule configuration:
::

	dnRouter(cfg-acl-ipv4)# no rule 102 deny src-ip 1.1.1.1/32 log

.. **Help line:** Configure access-lists logging action.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
| 19.2        | Command introduced    |
+-------------+-----------------------+

---

### access-lists rule next-hop.rst

access-lists rule next-hop
--------------------------

**Minimum user role:** operator

You can define to route certain traffic through specific paths other than those defined by routing protocols. This can be achieved by specifying the next-hop address in access-lists configurations, so that the configured next-hop address from the access-list is used for forwarding packets towards its destination. This is instead of routing packet-based destination address lookup. If the configured next-hop is unreachable, the packets matching the rule will be forwarded according to the regular FIB lookup of the destination IP.

Next-hop configuration for forwarding packets is referred to as ACL Based Forwarding (ABF).

To configure the next-hop IP address to which packets matching the rule will be redirected:

**Command syntax: rule [rule-id] allow** next-hop1 [next-hop]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- Next-hop action is allowed only for rule of type allow.

- Next-hop IP address type format is validated against the access-list type (IPv4/IPv6).

- Next-hop IP address must not match any of the router local addresses.

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range           | Default     |
+=====================+=================================================================================================================================================================================================================================================+=================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                 |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000       | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     | Defines whether the traffic matching the rule   conditions are to be allowed or denied.                                                                                                                                                         |                 |             |
| rule-type           |                                                                                                                                                                                                                                                 | allow           | \-          |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     |                                                                                                                                                                                                                                                 | deny            |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| next-hop            | The next-hop IP address to which packets matching the rule are redirected.                                                                                                                                                                      | A.B.C.D         | \-          |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | The next-hop IP address must not match any of the router's local IP addresses.                                                                                                                                                                  | xx:xx::xx:xx    |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 allow next-hop1 1.2.3.4
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow next-hop1 2001:abcd::1

	dnRouter(cfg-acl-ipv4)# no rule 101 allow next-hop1
	dnRouter(cfg-acl-ipv6)# no rule 200 allow next-hop1

**Removing Configuration**

To remove the rule configuration:
::

	dnRouter(cfg-acl-ipv6)# no rule 101 allow next-hop1

.. **Help line:** Configure access-lists rule destination IP

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 13.0        | Command introduced    |
+-------------+-----------------------+
|             |                       |
| 19.3        | Updated rule-id range |
+-------------+-----------------------+

---

### access-lists rule next-table.rst

access-lists rule next-table
-----------------------------

**Minimum user role:** operator

An access list rule can be defined to direct certain traffic to be handled by a different VRF other than that which the interface is associated with. This can be achieved by specifying the next-table vrf in access-lists configurations,
so that the configured vrf in the ACL is used for forwarding packets towards its destination. The result of the lookup of the next-table VRF will determine the next-hop for the packets. In some cases the look-up may result in an unreachable
destination or null0 and lead to the packets being dropped. If the result of the lookup is a static route redirect to yet another VRF the packet will be dropped as
chaining of redirections is not allowed.

Next-table configuration for forwarding packets is referred to as ACL Based Forwarding (ABF).

To configure the next-table VRF to which packets matching the rule will be redirected:

**Command syntax: rule [rule-id] allow** next-table [vrf-name]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- Next-table action is allowed only for rule of type allow.

- Next-table VRF must be an existing VRF and may not be the current VRF or any of the management VRFs: mgmt0, mgmt-ncc-0/0 or mgmt-ncc-1/0.


**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range           | Default     |
+=====================+=================================================================================================================================================================================================================================================+=================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                 |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000       | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     | Defines whether the traffic matching the rule   conditions are to be allowed or denied.                                                                                                                                                         |                 |             |
| rule-type           |                                                                                                                                                                                                                                                 | allow           | \-          |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     |                                                                                                                                                                                                                                                 | deny            |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| next-table          | The next-table VRF name to which packets matching the rule are redirected.                                                                                                                                                                      |  VRF Name       | \-          |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | The Next-table VRF must be an existing VRF and may not be the current VRF or any of the management VRFs: mgmt0, mgmt-ncc-0/0 or mgmt-ncc-1/0.                                                                                                   |                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 allow next-table VRF-1
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow next-table VRF-2

	dnRouter(cfg-acl-ipv4)# no rule 101 allow next-table
	dnRouter(cfg-acl-ipv6)# no rule 200 allow next-table

**Removing Configuration**

To remove the rule configuration:
::

	dnRouter(cfg-acl-ipv6)# no rule 101 allow next-table

.. **Help line:** Configure access-lists rule redirected-to VRF name.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 17.0        | Command introduced    |
+-------------+-----------------------+
|             |                       |
| 19.3        | Updated rule-id range |
+-------------+-----------------------+
---

### access-lists rule packet-length.rst

access-lists rule packet-length
--------------------------------

**Minimum user role:** operator

To create an access-list for the source ports, use the following command:

**Command syntax:** rule [rule-id] [rule-type] packet-length [min-length] [max-length]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- You can't configure more than 16 ingress ACL ranges across all attached ACLs (including IPv4 and IPv6 together) and across all types: source-port, dest-port and packet-length ranges.

- Packet-length match is not supported for egress ACLs.

- For IPv4 packets, in the IPv4 header field, this field is known as the Total Length.

- Total Length is the length of the datagram, measured in octets, including internet header and data.

- In IPv6 header field, this field is known as the Payload Length, the length of the IPv6 payload, i.e. the rest of the packet following the IPv6 header, in octets.

- When only min-length is present, it represents a specific length and eq operator is assumed to be default.

- When both min-length and max-length are specified, it implies a range inclusive of both values.

**Parameter table:**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range                | Default     |
+=====================+=================================================================================================================================================================================================================================================+======================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                      |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000            | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                      |             |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                      |             |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                      |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| rule-type           | Defines whether the traffic matching the rule conditions   are to be allowed or denied.                                                                                                                                                         | allow                | \-          |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     |                                                                                                                                                                                                                                                 | deny                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| min-length          | The minimum value. When only min-length is present, it represents a specific length and eq operator is assumed to be default.                                                                                                                   |  0-65535             | any         |
|                     |                                                                                                                                                                                                                                                 |                      |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| max-length          | The max value.  When both min-length and max-length are specified, it implies a range inclusive of both values.                                                                                                                                 | max-value>=min-value | \-          |
|                     |                                                                                                                                                                                                                                                 | max-value <= 65535   |             |
|                     |                                                                                                                                                                                                                                                 |                      |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 allow dest-ip 1.2.3.4/20 protocol tcp(0x06) src-ports 123 packet-length 100 200
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow protocol tcp(0x06) src-ports 100-200 packet-length 60 150
	dnRouter(cfg-acl-ipv6)# rule 300 deny packet-length 10000 65535
	dnRouter(cfg-acl-ipv6)# rule 300 deny packet-length 64
    dnRouter(cfg-acl-ipv6)# exit

**Removing Configuration**

To delete a rule configuration:
::

	dnRouter(cfg-acl-ipv6)# no rule 200 allow packet-length


.. **Help line:** Configure access-lists rule packet-length [min-length] [max-length]


**Command History**

+-------------+--------------------------+
|             |                          |
| Release     | Modification             |
+=============+==========================+
|             |                          |
| 17.0        | Command introduced       |
+-------------+--------------------------+
|             |                          |
| 19.3        | Updated rule-id range    |
+-------------+--------------------------+

---

### access-lists rule protocol.rst

access-lists rule protocol
--------------------------

**Minimum user role:** operator

To create an access-list for the protocol, use the following command:

**Command syntax: rule [rule-id] [rule-type]** protocol [protocol]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range                | Default     |
+=====================+=================================================================================================================================================================================================================================================+======================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                      |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000            | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                      |             |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                      |             |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                      |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| rule-type           | Defines whether the traffic matching the rule   conditions are to be allowed or denied.                                                                                                                                                         | allow                | \-          |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     |                                                                                                                                                                                                                                                 | deny                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| protocol            | The protocol used for the traffic.                                                                                                                                                                                                              | See protocol list    | \-          |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | You can enter the protocol name or use the protocol ID. The protocol ID is displayed in hexadecimal next to each protocol.                                                                                                                      |                      |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+

**Protocol list**

+---------------+-------------------+----------------------------+
| Decimal Value | Hexadecimal Value | Keyword (string)           |
+===============+===================+============================+
| 0             | 0x00              | hopopt                     |
+---------------+-------------------+----------------------------+
| 1             | 0x01              | icmp                       |
+---------------+-------------------+----------------------------+
| 2             | 0x02              | igmp                       |
+---------------+-------------------+----------------------------+
| 3             | 0x03              | ggp                        |
+---------------+-------------------+----------------------------+
| 4             | 0x04              | ip-in-ip                   |
+---------------+-------------------+----------------------------+
| 5             | 0x05              | St                         |
+---------------+-------------------+----------------------------+
| 6             | 0x06              | tcp                        |
+---------------+-------------------+----------------------------+
| 7             | 0x07              | cbt                        |
+---------------+-------------------+----------------------------+
| 8             | 0x08              | egp                        |
+---------------+-------------------+----------------------------+
| 9             | 0x09              | igp                        |
+---------------+-------------------+----------------------------+
| 10            | 0x0A              | bbn-rcc-mon                |
+---------------+-------------------+----------------------------+
| 11            | 0x0B              | nvp-ii                     |
+---------------+-------------------+----------------------------+
| 12            | 0x0C              | pup                        |
+---------------+-------------------+----------------------------+
| 13            | 0x0D              | argus                      |
+---------------+-------------------+----------------------------+
| 14            | 0x0E              | emcon                      |
+---------------+-------------------+----------------------------+
| 15            | 0x0F              | xnet                       |
+---------------+-------------------+----------------------------+
| 16            | 0x10              | chaos                      |
+---------------+-------------------+----------------------------+
| 17            | 0x11              | udp                        |
+---------------+-------------------+----------------------------+
| 18            | 0x12              | mux                        |
+---------------+-------------------+----------------------------+
| 19            | 0x13              | dcn-meas                   |
+---------------+-------------------+----------------------------+
| 20            | 0x14              | hmp                        |
+---------------+-------------------+----------------------------+
| 21            | 0x15              | prm                        |
+---------------+-------------------+----------------------------+
| 22            | 0x16              | xns-idp                    |
+---------------+-------------------+----------------------------+
| 23            | 0x17              | trunk-1                    |
+---------------+-------------------+----------------------------+
| 24            | 0x18              | trunk-2                    |
+---------------+-------------------+----------------------------+
| 25            | 0x19              | leaf-1                     |
+---------------+-------------------+----------------------------+
| 26            | 0x1A              | leaf-2                     |
+---------------+-------------------+----------------------------+
| 27            | 0x1B              | rdp                        |
+---------------+-------------------+----------------------------+
| 28            | 0x1C              | irtp                       |
+---------------+-------------------+----------------------------+
| 29            | 0x1D              | iso-tp4                    |
+---------------+-------------------+----------------------------+
| 30            | 0x1E              | netblt                     |
+---------------+-------------------+----------------------------+
| 31            | 0x1F              | mfe-nsp                    |
+---------------+-------------------+----------------------------+
| 32            | 0x20              | merit-inp                  |
+---------------+-------------------+----------------------------+
| 33            | 0x21              | dccp                       |
+---------------+-------------------+----------------------------+
| 34            | 0x22              | 3pc                        |
+---------------+-------------------+----------------------------+
| 35            | 0x23              | idpr                       |
+---------------+-------------------+----------------------------+
| 36            | 0x24              | xtp                        |
+---------------+-------------------+----------------------------+
| 37            | 0x25              | ddp                        |
+---------------+-------------------+----------------------------+
| 38            | 0x26              | idpr-cmtp                  |
+---------------+-------------------+----------------------------+
| 39            | 0x27              | tp++                       |
+---------------+-------------------+----------------------------+
| 40            | 0x28              | il                         |
+---------------+-------------------+----------------------------+
| 41            | 0x29              | ipv6                       |
+---------------+-------------------+----------------------------+
| 42            | 0x2A              | sdrp                       |
+---------------+-------------------+----------------------------+
| 43            | 0x2B              | ipv6-route                 |
+---------------+-------------------+----------------------------+
| 44            | 0x2C              | ipv6-frag                  |
+---------------+-------------------+----------------------------+
| 45            | 0x2D              | idrp                       |
+---------------+-------------------+----------------------------+
| 46            | 0x2E              | rsvp                       |
+---------------+-------------------+----------------------------+
| 47            | 0x2F              | gre                        |
+---------------+-------------------+----------------------------+
| 48            | 0x30              | dsr                        |
+---------------+-------------------+----------------------------+
| 49            | 0x31              | bna                        |
+---------------+-------------------+----------------------------+
| 50            | 0x32              | esp                        |
+---------------+-------------------+----------------------------+
| 51            | 0x33              | ah                         |
+---------------+-------------------+----------------------------+
| 52            | 0x34              | i-nlsp                     |
+---------------+-------------------+----------------------------+
| 53            | 0x35              | swipe                      |
+---------------+-------------------+----------------------------+
| 54            | 0x36              | narp                       |
+---------------+-------------------+----------------------------+
| 55            | 0x37              | mobile                     |
+---------------+-------------------+----------------------------+
| 56            | 0x38              | tlsp                       |
+---------------+-------------------+----------------------------+
| 57            | 0x39              | skip                       |
+---------------+-------------------+----------------------------+
| 58            | 0x3A              | ipv6-icmp                  |
+---------------+-------------------+----------------------------+
| 59            | 0x3B              | ipv6-nonxt                 |
+---------------+-------------------+----------------------------+
| 60            | 0x3C              | ipv6-opts                  |
+---------------+-------------------+----------------------------+
| 61            | 0x3D              | any-host                   |
+---------------+-------------------+----------------------------+
| 62            | 0x3E              | cftp                       |
+---------------+-------------------+----------------------------+
| 63            | 0x3F              | any-local-network          |
+---------------+-------------------+----------------------------+
| 64            | 0x40              | sat-expak                  |
+---------------+-------------------+----------------------------+
| 65            | 0x41              | kryptolan                  |
+---------------+-------------------+----------------------------+
| 66            | 0x42              | rvd                        |
+---------------+-------------------+----------------------------+
| 67            | 0x43              | ippc                       |
+---------------+-------------------+----------------------------+
| 68            | 0x44              | any-dist-file-sys          |
+---------------+-------------------+----------------------------+
| 69            | 0x45              | sat-mon                    |
+---------------+-------------------+----------------------------+
| 70            | 0x46              | visa                       |
+---------------+-------------------+----------------------------+
| 71            | 0x47              | ipcu                       |
+---------------+-------------------+----------------------------+
| 72            | 0x48              | cpnx                       |
+---------------+-------------------+----------------------------+
| 73            | 0x49              | cphb                       |
+---------------+-------------------+----------------------------+
| 74            | 0x4A              | wsn                        |
+---------------+-------------------+----------------------------+
| 75            | 0x4B              | pvp                        |
+---------------+-------------------+----------------------------+
| 76            | 0x4C              | br-sat-mon                 |
+---------------+-------------------+----------------------------+
| 77            | 0x4D              | sun-nd                     |
+---------------+-------------------+----------------------------+
| 78            | 0x4E              | wb-mon                     |
+---------------+-------------------+----------------------------+
| 79            | 0x4F              | wb-expak                   |
+---------------+-------------------+----------------------------+
| 80            | 0x50              | iso-ip                     |
+---------------+-------------------+----------------------------+
| 81            | 0x51              | vmtp                       |
+---------------+-------------------+----------------------------+
| 82            | 0x52              | secure-vmtp                |
+---------------+-------------------+----------------------------+
| 83            | 0x53              | vines                      |
+---------------+-------------------+----------------------------+
| 84            | 0x54              | ttp                        |
+---------------+-------------------+----------------------------+
| 84            | 0x54              | iptm                       |
+---------------+-------------------+----------------------------+
| 85            | 0x55              | nsfnet-igp                 |
+---------------+-------------------+----------------------------+
| 86            | 0x56              | dgp                        |
+---------------+-------------------+----------------------------+
| 87            | 0x57              | tcf                        |
+---------------+-------------------+----------------------------+
| 88            | 0x58              | eigrp                      |
+---------------+-------------------+----------------------------+
| 89            | 0x59              | ospf                       |
+---------------+-------------------+----------------------------+
| 90            | 0x5A              | sprite-rpc                 |
+---------------+-------------------+----------------------------+
| 91            | 0x5B              | larp                       |
+---------------+-------------------+----------------------------+
| 92            | 0x5C              | mtp                        |
+---------------+-------------------+----------------------------+
| 93            | 0x5D              | ax.25                      |
+---------------+-------------------+----------------------------+
| 94            | 0x5E              | os                         |
+---------------+-------------------+----------------------------+
| 95            | 0x5F              | micp                       |
+---------------+-------------------+----------------------------+
| 96            | 0x60              | scc-sp                     |
+---------------+-------------------+----------------------------+
| 97            | 0x61              | etherip                    |
+---------------+-------------------+----------------------------+
| 98            | 0x62              | encap                      |
+---------------+-------------------+----------------------------+
| 99            | 0x63              | any-private-encrypt-scheme |
+---------------+-------------------+----------------------------+
| 100           | 0x64              | gmtp                       |
+---------------+-------------------+----------------------------+
| 101           | 0x65              | ifmp                       |
+---------------+-------------------+----------------------------+
| 102           | 0x66              | pnni                       |
+---------------+-------------------+----------------------------+
| 103           | 0x67              | pim                        |
+---------------+-------------------+----------------------------+
| 104           | 0x68              | aris                       |
+---------------+-------------------+----------------------------+
| 105           | 0x69              | scps                       |
+---------------+-------------------+----------------------------+
| 106           | 0x6A              | qnx                        |
+---------------+-------------------+----------------------------+
| 107           | 0x6B              | a/n                        |
+---------------+-------------------+----------------------------+
| 108           | 0x6C              | ipcomp                     |
+---------------+-------------------+----------------------------+
| 109           | 0x6D              | snp                        |
+---------------+-------------------+----------------------------+
| 110           | 0x6E              | compaq-peer                |
+---------------+-------------------+----------------------------+
| 111           | 0x6F              | ipx-in-ip                  |
+---------------+-------------------+----------------------------+
| 112           | 0x70              | vrrp                       |
+---------------+-------------------+----------------------------+
| 113           | 0x71              | pgm                        |
+---------------+-------------------+----------------------------+
| 114           | 0x72              | any-0-hop-protocol         |
+---------------+-------------------+----------------------------+
| 115           | 0x73              | l2tp                       |
+---------------+-------------------+----------------------------+
| 116           | 0x74              | ddx                        |
+---------------+-------------------+----------------------------+
| 117           | 0x75              | iatp                       |
+---------------+-------------------+----------------------------+
| 118           | 0x76              | stp                        |
+---------------+-------------------+----------------------------+
| 119           | 0x77              | srp                        |
+---------------+-------------------+----------------------------+
| 120           | 0x78              | uti                        |
+---------------+-------------------+----------------------------+
| 121           | 0x79              | smp                        |
+---------------+-------------------+----------------------------+
| 122           | 0x7A              | sm                         |
+---------------+-------------------+----------------------------+
| 123           | 0x7B              | ptp                        |
+---------------+-------------------+----------------------------+
| 124           | 0x7C              | is-is-over-ipv4            |
+---------------+-------------------+----------------------------+
| 125           | 0x7D              | fire                       |
+---------------+-------------------+----------------------------+
| 126           | 0x7E              | crtp                       |
+---------------+-------------------+----------------------------+
| 127           | 0x7F              | crudp                      |
+---------------+-------------------+----------------------------+
| 128           | 0x80              | sscopmce                   |
+---------------+-------------------+----------------------------+
| 129           | 0x81              | iplt                       |
+---------------+-------------------+----------------------------+
| 130           | 0x82              | sps                        |
+---------------+-------------------+----------------------------+
| 131           | 0x83              | pipe                       |
+---------------+-------------------+----------------------------+
| 132           | 0x84              | sctp                       |
+---------------+-------------------+----------------------------+
| 133           | 0x85              | fc                         |
+---------------+-------------------+----------------------------+
| 134           | 0x86              | rsvp-e2e-ignore            |
+---------------+-------------------+----------------------------+
| 135           | 0x87              | mobility-header            |
+---------------+-------------------+----------------------------+
| 136           | 0x88              | udplite                    |
+---------------+-------------------+----------------------------+
| 137           | 0x89              | mpls-in-ip                 |
+---------------+-------------------+----------------------------+
| 138           | 0x8A              | manet                      |
+---------------+-------------------+----------------------------+
| 139           | 0x8B              | hip                        |
+---------------+-------------------+----------------------------+
| 140           | 0x8C              | shim6                      |
+---------------+-------------------+----------------------------+
| 141           | 0x8D              | wesp                       |
+---------------+-------------------+----------------------------+
| 142           | 0x8E              | rohc                       |
+---------------+-------------------+----------------------------+
| 143-255       | 0x8F - 0xFF       | for user to configure      |
+---------------+-------------------+----------------------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 100 allow protocol tcp
	dnRouter(cfg-acl-ipv4)# rule 101 allow src-ip 1.2.3.4/20 protocol udp(0x11)
	dnRouter(cfg-acl-ipv4)# rule 102 deny dest-ip 1.1.1.1/32 protocol tcp(0x06)
	dnRouter(cfg-acl-ipv4)# rule 103 deny dest-ip 1.1.1.1/32 protocol 0xFE
	dnRouter(cfg-acl-ipv4)# rule 100 allow protocol any
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow src-ip 2001:abcd::0/127 protocol tcp(0x06)
	dnRouter(cfg-acl-ipv6)# rule 300 deny dest-ip 2001:abcd::0/127 protocol icmp(0x01)
	dnRouter(cfg-acl-ipv6)# rule 400 deny dest-ip 2001:abcd::0/127 protocol 0x02


**Removing Configuration**

To delete a rule configuration:
::

	dnRouter(cfg-acl-ipv6)# no rule 300 allow protocol


.. **Help line:** Configure access-lists rule protocol

**Command History**

+-------------+--------------------------+
|             |                          |
| Release     | Modification             |
+=============+==========================+
|             |                          |
| 5.1.0       | Command introduced       |
+-------------+--------------------------+
|             |                          |
| 6.0         | Applied new hierarchy    |
+-------------+--------------------------+
|             |                          |
| 19.3        | Updated rule-id range    |
+-------------+--------------------------+

---

### access-lists rule set-qos.rst

access-lists rule set-qos
-------------------------

**Minimum user role:** operator

Extend ingress traffic-class-map definition for QoS actions according to access-list IP traffic match qualifiers.
For the matched flow, given the desired traffic-class-map is defined in the QoS ingress policy of the same interface ingress access-list, the flow will be imposed by the QoS behavior requested for that traffic-class-map that is defined in the QoS ingress policy.
Apply “default” to impose the default ingress QoS rule behavior on matched flow.

To configure the seq-qos with which packets matching the rule will be influenced:

**Command syntax: rule [rule-id] allow** {set-qos-traffic-class [traffic-class-map name] | set-qos-default}

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule allow

- access-lists ipv6 rule allow

**Note**
- set-qos-traffic-class <traffic-class-map name> is mutually exclusive with set-qos-default. Setting one will overwrite the other
- no commend will require to match the existing set option
- set-qos action is allowed only for rule of type allow.
- set-qos action is allowed only for ingress access-list.


**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range           | Default     |
+=====================+=================================================================================================================================================================================================================================================+=================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                 |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000       | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                 |             |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     | Defines whether the traffic matching the rule   conditions are to be allowed or denied.                                                                                                                                                         |                 |             |
| rule-type           |                                                                                                                                                                                                                                                 | allow           | \-          |
|                     |                                                                                                                                                                                                                                                 |                 |             |
|                     |                                                                                                                                                                                                                                                 | deny            |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                 |             |
| traffic-class-map   | A configured QoS traffic-class map                                                                                                                                                                                                              |  string         | \-          |
| name                |                                                                                                                                                                                                                                                 |                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 allow set-qos-traffic-class Class0
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow set-qos-default

**Removing Configuration**

To remove the rule configuration:
::

	dnRouter(cfg-acl-ipv4)# no rule 101 allow set-qos-traffic-class
	dnRouter(cfg-acl-ipv6)# no rule 101 allow set-qos-default

.. **Help line:** Configure access-lists rule set-qos.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
| 18.1        | Command introduced    |
+-------------+-----------------------+
|             |                       |
| 19.3        | Updated rule-id range |
+-------------+-----------------------+

---

### access-lists rule src-ip.rst

access-lists rule src-ip
------------------------

**Minimum user role:** operator

To create an access-list for the source IP, use the following command:

**Command syntax: rule [rule-id] [rule-type]** src-ip [src-ip]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note** 

- IPv6 inverse mask is not supported on Broadcom J3-AI based platforms.
- The Source IP address format must match the access-list type (IPv4/IPv6).
- When mask is provided for src-ip, mask is handled as inverse-mask. In inverse-mask, a mask 0 value bit reflect a bit in the ip address which value must be matched. A mask 1 value bit reflect a  a bit in the ip address which can be of either value.
-  Example: 

::
	src-ip 10.10.10.10/0.0.4.0 will match both 10.10.10.10 and 10.10.14.10 source ip addresses
	src-ip 2006:18:91::2/1:: will match both 2006:18:91::2 and 2007:18:91::2 source ip addresses

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                    |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range              | Default     |
+=====================+=================================================================================================================================================================================================================================================+====================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                    |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000          | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                    |             |
|                     |                                                                                                                                                                                                                                                 |                    |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                    |             |
|                     |                                                                                                                                                                                                                                                 |                    |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                    |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                    |             |
| rule-type           | Defines whether the traffic matching the rule   conditions are to be allowed or denied.                                                                                                                                                         | allow              | \-          |
|                     |                                                                                                                                                                                                                                                 |                    |             |
|                     |                                                                                                                                                                                                                                                 | deny               |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                    |             |
| src-ip              | The source IPs. Can be a specific host, a network or group of hosts, or any host.                                                                                                                                                               | A.B.C.D/x          | any         |
|                     |                                                                                                                                                                                                                                                 | A.B.C.D/X.Y.Z.W    |             |
|                     |                                                                                                                                                                                                                                                 | x:x::x:x/m         |             |
|                     |                                                                                                                                                                                                                                                 | x:x::x:x/m:m::m:m  |             |
|                     |                                                                                                                                                                                                                                                 | any                |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+


**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 allow src-ip 1.2.3.4/20
	dnRouter(cfg-acl-ipv4)# rule 102 deny src-ip 1.1.1.1/32
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow src-ip 2001:abcd::0/127

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_3
	dnRouter(cfg-acl-ipv6)# rule 200 allow src-ip 10.10.10.10/0.0.4.0


**Removing Configuration**

To delete a rule configuration:
::

	dnRouter(cfg-acl-ipv6)# no rule 200 allow src-ip

.. **Help line:** Configure access-lists rule source ip

**Command History**

+-------------+--------------------------+
|             |                          |
| Release     | Modification             |
+=============+==========================+
|             |                          |
| 5.1.0       | Command introduced       |
+-------------+--------------------------+
|             |                          |
| 6.0         | Applied new hierarchy    |
+-------------+--------------------------+
|             |                          |
| 19.3        | Updated rule-id range    |
+-------------+--------------------------+
|             |                          |
| 25.2        | Add inverse-mask support |
+-------------+--------------------------+
---

### access-lists rule src-ports.rst

access-lists rule src-ports
---------------------------

**Minimum user role:** operator

To create an access-list for the source ports, use the following command:

**Command syntax: rule [rule-id] [rule-type] protocol [protocol]** src-ports [source-ports]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Note**

- You can't configure more than 8 ingress IPv4 ACL source port ranges across all attached ACLs.

- You can't configure more than 8 ingress IPv6 ACL source port ranges across all attached ACLs.

- You can't configure more than 8 different IPv4 in-band-managment ACL source port ranges.

- You can't configure more than 8 different IPv6 in-band-managment ACL source port ranges

- For egress IPv4 ACL, you can't configure more than 24 unique combinations of SrcPortMin, SrcPortMax, DstPortMin, DstPortMax.

- Source port range is not supported for egress IPv6 ACL.

- If you remove the protocol field, the ports field will be removed.

**Parameter table:**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range                | Default     |
+=====================+=================================================================================================================================================================================================================================================+======================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                      |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000            | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                      |             |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                      |             |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                      |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| rule-type           | Defines whether the traffic matching the rule conditions   are to be allowed or denied.                                                                                                                                                         | allow                | \-          |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     |                                                                                                                                                                                                                                                 | deny                 |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| protocol            | The protocol used for the traffic.                                                                                                                                                                                                              | See protocol list    | \-          |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | You can enter the protocol name or use the protocol ID. The protocol ID is displayed in hexadecimal next to each protocol.                                                                                                                      |                      |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                      |             |
| src-ports           | The source ports.                                                                                                                                                                                                                               | 0..65535             | Any         |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | Source ports can be configured as a range.                                                                                                                                                                                                      |                      |             |
|                     |                                                                                                                                                                                                                                                 |                      |             |
|                     | Source ports are supported only for protocol TCP   and UDP.                                                                                                                                                                                     |                      |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 allow dest-ip 1.2.3.4/20 protocol tcp(0x06) src-ports 123
	dnRouter(cfg-acl-ipv4)# rule 102 deny dest-ip 1.2.3.4/20 protocol 0x06 src-ports 124
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow protocol tcp(0x06) src-ports 100-200
	dnRouter(cfg-acl-ipv6)# rule 300 deny src-ip 2001::1 protocol udp(0x11) src-ports 179
	dnRouter(cfg-acl-ipv6)# rule 400 allow src-ip 2001::2 protocol 0x11 src-ports 179



**Removing Configuration**

To delete a rule configuration:
::

	dnRouter(cfg-acl-ipv6)# no rule 200 allow src-ports


.. **Help line:** Configure access-lists rule source ports


**Command History**

+-------------+--------------------------+
|             |                          |
| Release     | Modification             |
+=============+==========================+
|             |                          |
| 5.1.0       | Command introduced       |
+-------------+--------------------------+
|             |                          |
| 6.0         | Applied new hierarchy    |
+-------------+--------------------------+
|             |                          |
| 19.3        | Updated rule-id range    |
+-------------+--------------------------+
---

### access-lists rule tcp-flag.rst

access-lists rule tcp-flag
--------------------------

**Minimum user role:** operator

To create an access-list to match TCP flags, use the following command:

**Command syntax: rule [rule-id] [rule-type] protocol tcp(0x06)** tcp-flag [list of tcp-flags]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                         |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range                   | Default     |
+=====================+=================================================================================================================================================================================================================================================+=========================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                         |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000               | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                         |             |
|                     |                                                                                                                                                                                                                                                 |                         |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                         |             |
|                     |                                                                                                                                                                                                                                                 |                         |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                         |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                         |             |
| rule-type           | Defines whether the traffic matching the rule   conditions are to be allowed or denied.                                                                                                                                                         | allow                   | \-          |
|                     |                                                                                                                                                                                                                                                 |                         |             |
|                     |                                                                                                                                                                                                                                                 | deny                    |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+
|                     |                                                                                                                                                                                                                                                 | See TCP flag list below |             |
| tcp-flag            | Used to configure an access-list rule to match   specific TCP flags.                                                                                                                                                                            |                         | \-          |
|                     |                                                                                                                                                                                                                                                 |                         |             |
|                     | Multiple tcp-flag can be configured per rule. In   this case all flags must be matched for the rule to apply.                                                                                                                                   |                         |             |
|                     |                                                                                                                                                                                                                                                 |                         |             |
|                     | Available for TCP protocol only.                                                                                                                                                                                                                |                         |             |
|                     |                                                                                                                                                                                                                                                 |                         |             |
|                     | Not supported by egress IPv6 access-lists; the   policy will be rejected if attached in out   direction                                                                                                                                         |                         |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+

**TCP flag table**

+------------------+
| Keyword (string) |
+==================+
| urg              |
+------------------+
| ack              |
+------------------+
| psh              |
+------------------+
| rst              |
+------------------+
| syn              |
+------------------+
| fin              |
+------------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_1
	dnRouter(cfg-acl-ipv6)# rule 101 allow dest-ip 1.2.3.4/20 protocol tcp(0x06) tcp-flag syn
	dnRouter(cfg-acl-ipv6)# rule 102 deny protocol tcp(0x06) dest-ports 300 tcp-flag syn ack
	dnRouter(cfg-acl-ipv6)# rule 102 deny protocol tcp(0x06) dest-ports 300 tcp-flag fin ack


**Remove Configuration**

To delete a rule configuration:
::

	dnRouter(cfg-acl-ipv6)# no rule 102 allow tcp-flag


.. **Help line:** Configure access-list rule tcp-flag

**Command History**

+-------------+--------------------------+
|             |                          |
| Release     | Modification             |
+=============+==========================+
|             |                          |
| 5.1.0       | Command introduced       |
+-------------+--------------------------+
|             |                          |
| 6.0         | Applied new hierarchy    |
+-------------+--------------------------+
|             |                          |
| 19.3        | Updated rule-id range    |
+-------------+--------------------------+

---

### access-lists rule vrf.rst

access-lists rule vrf
---------------------

**Minimum user role:** operator

To create an access-list to match a specific packet VRF context:

**Command syntax: rule [rule-id] [rule-type]** vrf [vrf-name]

**Command mode:** config

**Hierarchies**

- access-lists ipv4 rule

- access-lists ipv6 rule


**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                     |             |
| Rule Parameters     | Description                                                                                                                                                                                                                                     | Range               | Default     |
+=====================+=================================================================================================================================================================================================================================================+=====================+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |                     |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000           | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |                     |             |
|                     |                                                                                                                                                                                                                                                 |                     |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |                     |             |
|                     |                                                                                                                                                                                                                                                 |                     |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |                     |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+
|                     | Defines whether the traffic matching the rule conditions are to be allowed or denied.                                                                                                                                                           |                     |             |
| rule-type           |                                                                                                                                                                                                                                                 | allow               | \-          |
|                     |                                                                                                                                                                                                                                                 |                     |             |
|                     |                                                                                                                                                                                                                                                 | deny                |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+
|                     |                                                                                                                                                                                                                                                 |                     |             |
| vrf-name            | Used to configure an access-list rule to match a configured vrf name                                                                                                                                                                            | string length 1-255 | Any         |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 100 allow vrf IN-BAND-CTRL
	dnRouter(cfg-acl-ipv4)# rule 101 allow src-ip 1.2.3.4/20 vrf CUSTOMER_A

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 10 deny src-ip 2001::1 vrf CUSTOMER_B

**Removing Configuration**

To delete a rule configuration:
::

	dnRouter(cfg-acl-ipv4)# no rule 101 allow vrf


.. **Help line:** Configure access-lists rule vrf

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 16.2        | Command introduced    |
+-------------+-----------------------+
|             |                       |
| 19.3        | Updated rule-id range |
+-------------+-----------------------+

---

### access-lists rule.rst

access-lists rule
-----------------

**Minimum user role:** operator

For every access-list, you can set rules by defining attributes using the following syntax:

**Command syntax: rule [rule-id] [rule-type]**

**Command mode:** config

**Hierarchies**

- access-lists

**Note:**

- Access-list type can be ipv4 or ipv6. By default, rule without parameters relates to any value

- A rule with no parameters relates to any value.

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
|                     |                                                                                                                                                                                                                                                 |             |             |
| Parameter           | Description                                                                                                                                                                                                                                     | Range       | Default     |
+=====================+=================================================================================================================================================================================================================================================+=============+=============+
| rule-id             | The rule's unique identifier within the access-list. It determines the priority of the rule (rules with a low ID number have priority over rules with high ID numbers). You must configure at least one rule in order to create an access-list. |             |             |
|                     |                                                                                                                                                                                                                                                 | 1..130000   | \-          |
|                     | The default ID (131071) is attached to the default access-list which is "Deny any". See the default access-list in "show access-lists" on page 3297.                                                                                            |             |             |
|                     |                                                                                                                                                                                                                                                 |             |             |
|                     | Rule ID 131070 is reserved for default-icmp for IPv4/IPv6 access-lists, which allows protocol type icmp-v4/icmp-v6 on any IP and port.                                                                                                          |             |             |
|                     |                                                                                                                                                                                                                                                 |             |             |
|                     | You can configure up to 250,000 rules altogether per system.                                                                                                                                                                                    |             |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
|                     |                                                                                                                                                                                                                                                 |             |             |
| rule-type           | Defines whether the traffic matching the rule   conditions are to be allowed or denied.                                                                                                                                                         | allow       | \-          |
|                     |                                                                                                                                                                                                                                                 |             |             |
|                     |                                                                                                                                                                                                                                                 | deny        |             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+

For every rule, you set an ID. The ID determines the positioning of the rule within the access-list (i.e. its priority). Every packet is checked against the rules by priority (from the lowest ID to the highest). The first rule that matches is applied. The rule ID is unique per access-list (not between access-lists).

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 101 description the next two rules are default rules
	dnRouter(cfg-acl-ipv4)# rule 102 allow
	dnRouter(cfg-acl-ipv4)# rule 103 deny
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow



**Removing Configuration**

To delete a rule:
::

	dnRouter(cfg-acl-ipv6)# no rule 200

To delete specific rule configuration:
::

	dnRouter(cfg-acl-ipv4)# no rule 102 deny

.. **Help line:** Configure access-lists rule

**Command History**

+-------------+---------------------------------------------------------------------------------------+
|             |                                                                                       |
| Release     | Modification                                                                          |
+=============+=======================================================================================+
|             |                                                                                       |
| 5.1.0       | Command introduced                                                                    |
+-------------+---------------------------------------------------------------------------------------+
|             |                                                                                       |
| 6.0         | Applied new hierarchy                                                                 |
+-------------+---------------------------------------------------------------------------------------+
|             |                                                                                       |
| 11.0        | Support of up to 2000 rules per access-list and   up to 250,000 rules per system.     |
+-------------+---------------------------------------------------------------------------------------+
|             |                                                                                       |
| 19.3        | Updated rule-id range                                                                 |
+-------------+---------------------------------------------------------------------------------------+
---

### access-lists.rst

access-lists
------------

**Minimum user role:** operator

Access-lists commands are hierarchical. You can create multiple access-lists with multiple rules in each access-list. To configure an access-list:

**Command syntax: access-lists [access-list_type] [access-list_name]**

**Command mode:** config

**Hierarchies**

- configuration

**Note**

- You cannot configure an access-lists with a reserved name (e.g., ipv4, ipv6, counters, interface name).

- You cannot delete an access-list that is associated with an interface.

**Parameter table**

+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------+
|                     |                                                                                                                                                                                                                                              |           |             |
| Parameter           | Description                                                                                                                                                                                                                                  | Range     | Default     |
+=====================+==============================================================================================================================================================================================================================================+===========+=============+
|                     |                                                                                                                                                                                                                                              |           |             |
| access-list-type    |  The type of access-list   that you are configuring (IPv4 or IPv6)                                                                                                                                                                           | IPv4      | \-          |
|                     |                                                                                                                                                                                                                                              |           |             |
|                     |                                                                                                                                                                                                                                              | IPv6      |             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------+
|                     |                                                                                                                                                                                                                                              |           |             |
| access-list-name    | The specific access-list that you want to configure. All rules   that are created using the same access-list name belong to the same   access-list. If you use a different access-list name for a rule, a new   access-list will be created. | Text      | \-          |
|                     |                                                                                                                                                                                                                                              |           |             |
|                     | You cannot configure an access-list with a reserved name (ipv4,   ipv6, counters, interface name).                                                                                                                                           |           |             |
|                     |                                                                                                                                                                                                                                              |           |             |
|                     | You can configure up to 10,000 access-lists per system.                                                                                                                                                                                      |           |             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv4 MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# rule 100 allow src-ip any dest-ip any
	dnRouter(cfg-acl-ipv4)# rule 101 allow src-ip 1.2.3.4/20
	dnRouter(cfg-acl-ipv4)# rule 102 deny dest-ip 1.1.1.1/32 protocol tcp(0x06) src-ports 100-200
	dnRouter(cfg-acl-ipv4)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_1
	dnRouter(cfg-acl-ipv6)# rule 100 allow protocol udp(0x11)
	dnRouter(cfg-acl-ipv6)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_2
	dnRouter(cfg-acl-ipv6)# rule 200 allow src-ip 2001:abcd::0/127
	dnRouter(cfg-acl-ipv6)# rule 200 allow protocol tcp
	dnRouter(cfg-acl-ipv6)# exit

	dnRouter(cfg)# access-lists
	dnRouter(cfg-acl)# ipv6 MyAccess_list_3
	dnRouter(cfg-acl-ipv6)# rule 300 deny dest-ip 2001:abcd::0/127
	dnRouter(cfg-acl-ipv6)# exit

	dnRouter(cfg)# no access-lists
	dnRouter(cfg-acl)# no ipv6
	dnRouter(cfg-acl)# no ipv6 MyAccess-list-1

	dnRouter(cfg-acl-ipv4)# MyAccess_list_1
	dnRouter(cfg-acl-ipv4)# no rule 100



**Removing Configuration**

To delete all access-lists:
::

	dnRouter(cfg)# no access-lists

To delete all IPv4 access lists:
::

	dnRouter(cfg)# no ipv4

To delete a specific access list:
::

	dnRouter(cfg)# no ipv4 MyAccess_list_1

..
	validation:

	| if a user tries to remove an access-list while it is attached to an interface the following error should be displayed:
	
	| "Error: failed to remove access-list <access-list-name>. access-list is attached to interface <interface-name>.

	Rule parameters restrictions:

	-  ICMP option is available only for ICMP protocol

	-  ICMP-v6 option is available only for IPv6-ICMP protocol

	-  TCP-flag option is available only for TCP protocol

	-  Hop-limit option is available only for ipv6 access-list type

	-  IPv4-options option is available only for ipv4 access-list type

	-  Src-ports/dest-ports are available only for protocol type TCP or UDP

	for each access-list configuration:

	-  rule id 131071 will be "default" - operation deny on any protocols, ip's and ports. this rule is lowest rule in the table

	-  rule id 131070 will be "default-icmp" for ipv4 type of acl - operation allow on protocol type icmp-v4 on any ip's and ports. this rule is only above "default" rule and below the other rules.

	-  rule id 131070 will be "default-icmp-v6" for ipv6 type of acl - operation allow on protocol type icmp-v6 on any ip's and ports. this rule is only above "default" rule and below the other rules.



	Scale validation:

	-  up to 2K rules per ACL

	-  up to 10K ACLs per system

	-  up to 250K rules per system

	-  up to 50K ingress ACL rules per NCP - ACLs are attached to interfaces (in direction)

	-  up to 20K egress ACL rules per NCP - ACLs are attached to interfaces (out direction) - egress ACL is supported starting from v11.1

	when the limit reached, comit will be rejected and the CLI will prompt (according the limit):

	"Error :Failed to set access-list <name> rule <id>. Number of rules for access-list has reached the maximum limit capacity per ACL"

	"Error :Failed to set access-list <name> rule <id>. Number of rules for access-list has reached the maximum limit capacity for system"

	"Error: Failed to set access-list <name>. Number of access-lists for system has reached the maximum limit capacity for system.

	"Error: Failed to attach access-list <name> to interface <id> direction <direction>. Number of access-list rules for system has reached the maximum limit capacity per NCP.

.. **Help line:** Configure access-lists

**Command History**

+-------------+----------------------------------------------------------------------------+
|             |                                                                            |
| Release     | Modification                                                               |
+=============+============================================================================+
|             |                                                                            |
| 5.1.0       | Command introduced                                                         |
+-------------+----------------------------------------------------------------------------+
|             |                                                                            |
| 6.0         | Applied   new hierarchyReplaced access-list with access-lists in syntax    |
+-------------+----------------------------------------------------------------------------+
---


# SECTION 3: POLICY

## Files from Policy folder

Files in this section: 7

### policy set aigp.rst

policy set aigp
---------------

**Minimum user role:** operator

Within an autonomous system (AS), the distance between two nodes in the interior gateway protocol (IGP) domain is calculated as a sum of all the metric values of links along the path. The IGP selects the shortest path between two nodes based on the calculated distance.

BGP is designed to provide routing over independent ASs with limited or no coordination among respective administrations. BGP does not use metrics in the path selection decisions.

The accumulated interior gateway protocol (AIGP) is an attribute that enables the BGP speakers in a network that is managed by a single administrative domain, but is sub-divided into multiple autonomous systems (AS), to perform best-path selection based on IGP metric, even if the nodes are in different ASs.

In the following image, the network of a single service provider is divided into three contiguous ASs (AS 6660, AS 6661, and AS 6662). The end-to-end service between CE1 and CE2 is MPLS VPN, resulting in the BGP speakers (i.e. PE1 and PE2, and the four border routers (BR P1, BR P2, BR P3, and BR P4) running BGP-LU (labeled unicast). Without AIGP, the PEs and BRs will perform best-path decisions without the IGP metrics inside the different ASs, by basing the interior cost of a route on the calculation of the metric to the next hop for the route. When AIGP is enabled on the PEs and BRs, the IGP metrics in the different ASs are accumulated and the AIGP distance is compared to break a tie, allowing these routers to make better best-path decisions.

<INSERT 04_protocols_bgp>

The set AIGP action depends on the policy attachment point:

+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                  |                                                                                                                                  |                                                                                                                                                                                                                     |                                                                                                                                                                                               |
| Set AIGP Policy Attachment Point                                 | Set AIGP IGP-metric                                                                                                              | Set AIGP [relative] [aigp-value]                                                                                                                                                                                    | Set AIGP [aigp-value]                                                                                                                                                                         |
+==================================================================+==================================================================================================================================+=====================================================================================================================================================================================================================+===============================================================================================================================================================================================+
|                                                                  |                                                                                                                                  |                                                                                                                                                                                                                     |                                                                                                                                                                                               |
| bgp neighbor address-family policy in                            | Set 0 in the AIGP metric                                                                                                         | Add the given [aigp-value] to or deduct it from the AIGP metric attribute before best path selection.                                                                                                               | Set the given [aigp-value] to the AIGP metric attribute before best path selection.                                                                                                           |
|                                                                  |                                                                                                                                  |                                                                                                                                                                                                                     |                                                                                                                                                                                               |
|                                                                  | **This is not the proper usage.**                                                                                                |                                                                                                                                                                                                                     |                                                                                                                                                                                               |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                  |                                                                                                                                  |                                                                                                                                                                                                                     |                                                                                                                                                                                               |
| bgp neighbor address-family policy out                           | Set 0 in the AIGP metric                                                                                                         | Add the given [aigp-value] to or deduct it from the AIGP metric attribute after best path selection.                                                                                                                | Overwrite the AIGP metric value with the specified [aigp-value].                                                                                                                              |
|                                                                  |                                                                                                                                  |                                                                                                                                                                                                                     |                                                                                                                                                                                               |
|                                                                  | **This is not the proper usage.**                                                                                                |                                                                                                                                                                                                                     |                                                                                                                                                                                               |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                  |                                                                                                                                  |                                                                                                                                                                                                                     |                                                                                                                                                                                               |
| bgp address-family unicast redistribute ospf|static|connected    | Set the IGP metric of the redistributed route to BGP AIGP. This will cause the system to be the AIGP originator for the route.   | Add the value to or deduct the value from the AIGP metric attribute of the BGP path. If the attribute does not exist, it will be created. This will cause the system to be the AIGP originator for the route.       | Set a specific value for the BGP AIGP attribute of the BGP path. If the attribute does not exist, it will be created. This will cause the system to be the AIGP originator for the route.     |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                  |                                                                                                                                  |                                                                                                                                                                                                                     |                                                                                                                                                                                               |
| bgp network                                                      | Set the IGP metric of the redistributed route to BGP AIGP. This will cause the system to be the AIGP originator for the route.   | Add the value to or deduct the value from the AIGP metric attribute of the BGP path. If the attribute does not exist, it will be created. This will cause the system to be the AIGP originator for the route.       | Set a specific value for the BGP AIGP attribute of the BGP path. If the attribute does not exist, it will be created. This will cause the system to be the AIGP originator for the route.     |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

To configure AIGP:
1. Create a policy to set the AIGP metric attribute. This command.
2. Enable the AIGP metric with a BGP neighbor. See bgp neighbor address-family aigp.
3. Optional. Set the router to ignore the AIGP metric in best-path calculation. See bgp bestpath aigp-ignore.

To set the AIGP metric attribute:

**Command syntax: set aigp {igp-metric \| [aigp-value] \| [relative] [aigp-value]}**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- BGP neighbor afi must be set with 'aigp enabled', otherwise no aigp attribute is sent or received regardless of the policy set action.


**Parameter table**

+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------+
|                |                                                                                                                                                       |                  | Default |
| Parameter      | Description                                                                                                                                           | Range            |         |
+================+=======================================================================================================================================================+==================+=========+
|                |                                                                                                                                                       |                  | \-      |
| igp-metric     | Sets the metric value as the IGP metric for the   route                                                                                               | \-               |         |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------+
|                |                                                                                                                                                       |                  | \-      |
| relative       | Increase/decrease the current value of the AIGP   metric by [aigp-value]. The resulting value cannot go below 0 or above the   maximum aigp-value.    | \+ /\-           |         |
|                |                                                                                                                                                       |                  |         |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------+
|                |                                                                                                                                                       |                  | \-      |
| aigp-value     | The new value of the AIGP metric that will be   set.                                                                                                  | 0..4294967294    |         |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# policy SET_FULL_ROUTES
	dnRouter(cfg-rpl-policy)# rule 10 allow
	dnRouter(cfg-rpl-policy-rule-10)#set aigp igp-metric

	dnRouter(cfg-rpl-policy)# rule 20 allow
	dnRouter(cfg-rpl-policy-rule-20)#set aigp 300

	dnRouter(cfg-rpl-policy)# rule 30 allow
	dnRouter(cfg-rpl-policy-rule-30)#set aigp + 10

	dnRouter(cfg-rpl-policy)# rule 40 allow
	dnRouter(cfg-rpl-policy-rule-40)#set aigp - 10


**Removing Configuration**

To remove the set entry:
::

	dnRouter(cfg-rpl-policy-rule-10)#no set aigp


.. **Help line:**

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 7.0         | Command introduced    |
+-------------+-----------------------+
| 25.2        | Command syntax changed|
+-------------+-----------------------+
---

### policy set as-path prepend.rst

policy set as-path prepend
---------------------------

**Minimum user role:** operator

To prepend the given string of AS number(s) or last AS to the AS-path:

**Command syntax: set as-path prepend** { **as-number [as-number]**, [as-number], ... \| **last-as [number]** }

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- This action is only relevant as a BGP policy.

- Within the same route policy rule, "set as-path exclude" will be processed and imposed before "set as-path prepend" action

**Parameter table**

+---------------+-------------------------------------------------------------------------------------+------------------+---------+
|               |                                                                                     |                  | Default |
| Parameter     | Description                                                                         | Range            |         |
+===============+=====================================================================================+==================+=========+
|               |                                                                                     |                  | \-      |
| as-number     | The AS number to prepend to the AS-path. You can   specify multiple AS numbers.     | 1..4294967295    |         |
+---------------+-------------------------------------------------------------------------------------+------------------+---------+
|               |                                                                                     |                  | \-      |
| number        | The number of times the last as-number will be added.                               | 1..9             |         |
+---------------+-------------------------------------------------------------------------------------+------------------+---------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# policy SET_FULL_ROUTES
	dnRouter(cfg-rpl-policy)# rule 10 allow
	dnRouter(cfg-rpl-policy-rule-10)# set as-path prepend as-number 23456
	dnRouter(cfg-rpl-policy-rule-10)# exit

	dnRouter(cfg-rpl-policy)# rule 20 allow
	dnRouter(cfg-rpl-policy-rule-20)# set as-path prepend as-number 12956, 23456
	dnRouter(cfg-rpl-policy-rule-20)# exit

	dnRouter(cfg-rpl-policy)# rule 30 allow
	dnRouter(cfg-rpl-policy-rule-30)# set as-path prepend last-as 1
	dnRouter(cfg-rpl-policy-rule-30)# exit

	dnRouter(cfg-rpl-policy)# rule 40 allow
	dnRouter(cfg-rpl-policy-rule-40)# set as-path prepend last-as 7
	dnRouter(cfg-rpl-policy-rule-40)# exit


**Removing Configuration**

To remove the set entry:
::

	dnRouter(cfg-rpl-policy)# rule 20 allow
	dnRouter(cfg-rpl-policy-rule-20)# no set as-path prepend as-number 12956
	dnRouter(cfg-rpl-policy-rule-20)# exit

	dnRouter(cfg-rpl-policy)# rule 40 allow
	dnRouter(cfg-rpl-policy-rule-40)# no set as-path prepend


.. **Help line:** Prepend the given string of AS number(s)

**Command History**

+-------------+----------------------------------------------+
|             |                                              |
| Release     | Modification                                 |
+=============+==============================================+
|             |                                              |
| 6.0         | Command introduced                           |
+-------------+----------------------------------------------+
|             |                                              |
| 9.0         | Changed parameter's range from minimum 1     |
+-------------+----------------------------------------------+
|             |                                              |
| 18.2        | Impose action order within route policy rule |
+-------------+----------------------------------------------+
| 25.2        | Command syntax changed                       |
+-------------+----------------------------------------------+
---

### policy set community.rst

policy set community
--------------------

**Minimum user role:** operator

Use this command to add or remove communities for BGP updates. When you enter multiple entries, they are collected as a list. You can add or remove values to/from the list, and you can do this in separate commits.

To set the specified communities value to BGP updates:

**Command syntax: set community** {**[community]**, [community], ... }
**Command syntax: set community additive {**[community]**, [community], ...} **
**Command syntax: set community none**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- You can set up to 25 different communities or 'none'.

- Within the same route policy rule, "set community-list" will be processed and imposed before "set community" action.

- Running one of these commands will replace whatever was previously configured.


**Parameter table**

+---------------+-------------------------------------------------------------------------------------------------+----------------------------------------------------------+---------------------+
|               |                                                                                                 |                                                          |                     |
| Parameter     | Description                                                                                     | Range                                                    | Comment             |
+===============+=================================================================================================+==========================================================+=====================+
|               |                                                                                                 |                                                          |                     |
| community     | The community value to set to BGP updates.                                                      | The community number (e.g. aa:nn), range (e.g. aa-bb:nn) | AS_number: 1..65535 |
|               |                                                                                                 |                                                          |                     |
|               | The set community [community] command will replace any existing community configuration.        | <AS_number:NN>                                           | ID: 0..65535        |
|               |                                                                                                 |                                                          |                     |
|               |                                                                                                 | <lower_AS_number- upper_AS_number:lower_id-upper-id>     |                     |
|               |                                                                                                 |                                                          |                     |
|               |                                                                                                 | internet                                                 |                     |
|               |                                                                                                 |                                                          |                     |
|               |                                                                                                 | accept-own                                               |                     |
|               |                                                                                                 |                                                          |                     |
|               |                                                                                                 | local-AS                                                 |                     |
|               |                                                                                                 |                                                          |                     |
|               |                                                                                                 | no-export                                                |                     |
|               |                                                                                                 |                                                          |                     |
|               |                                                                                                 | no-advertise                                             |                     |
|               |                                                                                                 |                                                          |                     |
|               |                                                                                                 | no-LLGR                                                  |                     |
|               |                                                                                                 |                                                          |                     |
|               |                                                                                                 | LLGR-stale                                               |                     |
+---------------+-------------------------------------------------------------------------------------------------+----------------------------------------------------------+---------------------+
|               |                                                                                                 |                                                          |                     |
| additive      | Appends the new communities to the existing communities.                                        |  \-                                                      | \-                  |
+---------------+-------------------------------------------------------------------------------------------------+----------------------------------------------------------+---------------------+
|               |                                                                                                 |                                                          |                     |
| none          | Removes the entire communities attribute from BGP updates.                                      |  \-                                                      | \-                  |
|               |                                                                                                 |                                                          |                     |
|               | The set community none will overwrite any existing community with "none".                       |                                                          |                     |
+---------------+-------------------------------------------------------------------------------------------------+----------------------------------------------------------+---------------------+

**Example**

To overwrite the existing route communities with new communities:
::

	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# policy SET_FULL_ROUTES
	dnRouter(cfg-rpl-policy)# rule 10 allow
	dnRouter(cfg-rpl-policy-rule-10)# set community 65000:1918

	dnRouter(cfg-rpl-policy)# rule 20 allow
	dnRouter(cfg-rpl-policy-rule-20)# set community 65000:86, 65000:2010
	dnRouter(cfg-rpl-policy)# rule 30 allow
	dnRouter(cfg-rpl-policy-rule-30)# set community local-AS, 65000:2010, internet

To add new route communities to the existing communities:
::

	dnRouter(cfg-rpl-policy)# rule 50 allow
	dnRouter(cfg-rpl-policy-rule-50)# set community additive 65000:86, 65000:2010

To delete the existing route communities (by overwriting them with "none")
::

	dnRouter(cfg-rpl-policy)# rule 40 allow
	dnRouter(cfg-rpl-policy-rule-40)# set community none

**Removing Configuration**

To remove the set entry:
::

	dnRouter(cfg-rpl-policy-rule-10)# no set community


.. **Help line:** The specified communities value is set to BGP updates.


**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
| 6.0         | Command introduced    |
+-------------+-----------------------+
| 18.2        | Added note for command|
|             | restriction           |
+-------------+-----------------------+
| 18.2        | Impose action order   |
|             | within route policy   |
|             | rule                  |
+-------------+-----------------------+
| 25.2        | Command syntax changed|
+-------------+-----------------------+
---

### policy set large-community.rst

policy set large-community
---------------------------

**Minimum user role:** operator

Use this command to add or remove large communities for BGP updates. When you enter multiple entries, they are collected as a list. You can add or remove values to/from the list, and you can do this in separate commits.

To set the specified communities' values to BGP updates:

**Command syntax: set large-community** {**[large-community]**, [large-community], ... }
**Command syntax: set large-community additive {**[large-community]**, [large-community], ... }
**Command syntax: set large-community none**


**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- You can set up to 25 large-communities or none.

- Within the same route policy rule, "set large-community-list" will be processed and imposed before "set large-community" action.

**Parameter table**

+-----------------+---------------------------------------------------------------------+---------------------------------------------+---------+
|    Parameter    | Description                                                         |                    Range                    | Default |
+=================+=====================================================================+=============================================+=========+
| large-community | The large-community values to set for BGP updates                   | <AS_number:id-1:id-2> :                     | \-      |
|                 |                                                                     | AS_number: 0..4294967295id-1: 0..4294967295 |         |
|                 |                                                                     | id-2: 0..4294967295                         |         |
+-----------------+---------------------------------------------------------------------+---------------------------------------------+---------+
| additive        | Appends the new large-communities to the existing large-communities |                                             | \-      |
+-----------------+---------------------------------------------------------------------+---------------------------------------------+---------+
| none            | Removes the entire large-communities attribute from BGP updates     |                                             | \-      |
+-----------------+---------------------------------------------------------------------+---------------------------------------------+---------+

**Example**

To overwrite the existing route large-communities with new large-communities:
::

	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# policy SET_FULL_ROUTES
	dnRouter(cfg-rpl-policy)# rule 10 allow
	dnRouter(cfg-rpl-policy-rule-10)# set large-community 15562:45:29
	dnRouter(cfg-rpl-policy)# rule 20 allow
	dnRouter(cfg-rpl-policy-rule-20)# set large-community 15562:45:29, 15562:45:50

To add new route large-communities to the existing large-communities:
::

	dnRouter(cfg-rpl-policy)# rule 50 allow
	dnRouter(cfg-rpl-policy-rule-50)# set large-community additive 15562:45:29, 15562:45:50

To delete the existing route large-communities (by overwriting them with "none")
::

	dnRouter(cfg-rpl-policy)# rule 40 allow
	dnRouter(cfg-rpl-policy-rule-40)# set large-community none

**Removing Configuration**

To remove all set large-communities:
::

	dnRouter(cfg-rpl-policy-rule-10)# no set large-community

.. **Help line:** The specified large communities value is set to BGP updates.

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
| 15.1        | Command introduced    |
+-------------+-----------------------+
| 18.1        | Added note for command|
|             | restriction           |
+-------------+-----------------------+
| 18.2        | Impose action order   |
|             | within route policy   |
|             | rule                  |
+-------------+-----------------------+
| 25.2        | Command syntax changed|
+-------------+-----------------------+

---

### policy set local-preference aigp relative.rst

set local-preference aigp relative
----------------------------------

**Minimum user role:** operator

AIGP (Accumulated IGP Metric) is a BGP attribute designed to enhance path selection in networks that span over multiple ASs. It allows BGP to propagate and consider IGP metric across multiple autonomous system, ensuring routing decisions are consistent with the internal network's shortest-path metrics.
In some cases, legacy devices do not support AIGP, or in some cases (like the case at hand) an operator would like to avoid introducing new configuration on legacy networks, in such case, the operator may decide to copy the AIGP value into the Local-Preference value when routes are advertised in a legacy AS, this way the legacy AS devices will select per route the ASBR that can provide the shortest path.
Updating Local-Preference by inbound policy may influence local best-path selection
If no aigp value known , no update to local-preference.

To update Local-Preference value according to offset from known AIGP value by route policy set action:

**Command syntax: set local-preference aigp [relative] [value]** }

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------+---------+
| Parameter | Description                                                                                                                               | Range         | Default |
+===========+===========================================================================================================================================+===============+=========+
| relative  | Sets the desired relative modification (add/substract) for the aigp value. The resulting value must be between 0..4294967295.             | \+/\-         | \-      |
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------+---------+
| value     | Sets an offset for the aigp metric value to be set into local-preference.                                                                 | 0..4294967295 | \-      |
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------+---------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# policy SET_FULL_ROUTES
	dnRouter(cfg-rpl-policy)# rule 10 allow
	dnRouter(cfg-rpl-policy-rule-10)#set local-preference aigp + 10
	dnRouter(cfg-rpl-policy-rule-10)#set local-preference aigp - 5

**Removing Configuration**

To remove the set entry:
::

	dnRouter(cfg-rpl-policy-rule-10)# no set local-preference

	dnRouter(cfg-rpl-policy-rule-10)# no set local-preference aigp

	dnRouter(cfg-rpl-policy-rule-10)# no set local-preference aigp + 10

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 25.2    | Command introduced                           |
+---------+----------------------------------------------+

---

### policy set med aigp relative.rst

policy set med aigp relative
----------------------------

**Minimum user role:** operator

AIGP (Accumulated IGP Metric) is a BGP attribute designed to enhance path selection in networks that span over multiple ASs. It allows BGP to propagate and consider IGP metric across multiple autonomous system, ensuring routing decisions are consistent with the internal network's shortest-path metrics.
in some cases, legacy devices do not support AIGP, or in some cases  (like the case at hand) an operator would like to avoid introducing new configuration on legacy networks, in such case, the operator may decide to copy the AIGP value into the MED value when routes are advertised to a legacy AS, this way the legacy AS devices will select per route the ASBR that can provide the shortest path.
the downside of such solution, is that the path to the ASBR is not taken into consideration when selecting the best path

To update MED value according to offset from known AIGP value by route policy set action:

**Command syntax: set med aigp [relative] [value]** }

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------+---------+
| Parameter | Description                                                                                                                               | Range         | Default |
+===========+===========================================================================================================================================+===============+=========+
| relative  | Sets the desired relative modification (add/substract) for the aigp value. The resulting MED value must be between 0..4294967295.         | \+/\-         | \-      |
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------+---------+
| value     | Sets an offset for the aigp metric value to be set into MED.                                                                              | 0..4294967295 | \-      |
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------+---------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# policy SET_FULL_ROUTES
	dnRouter(cfg-rpl-policy)# rule 10 allow
	dnRouter(cfg-rpl-policy-rule-10)#set med aigp + 10
	dnRouter(cfg-rpl-policy-rule-10)#set med aigp - 5

**Removing Configuration**

To remove the set entry:
::

	dnRouter(cfg-rpl-policy-rule-10)# no set med

	dnRouter(cfg-rpl-policy-rule-10)# no set med aigp

	dnRouter(cfg-rpl-policy-rule-10)# no set med aigp + 10

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 25.2    | Command introduced                           |
+---------+----------------------------------------------+

---

### policy set med.rst

policy set med
--------------

**Minimum user role:** operator

To set the BGP attribute MED:

**Command syntax: set med {igp-cost \| [med-value] \| [relative] [med-value]}**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------+---------+
| Parameter | Description                                                                                                                               | Range         | Default |
+===========+===========================================================================================================================================+===============+=========+
| igp-cost  | Set the MED value to be the metric towards the route bgp next-hop. Usage of igp-cost is only applicable for policy out.                   | \-            | \-      |
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------+---------+
| relative  | Increases or decreases the route's existing MED value by the configured med-value. The resulting MED value must be between 0..4294967295. | \+/\-         | \-      |
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------+---------+
| med-value | Sets a new multi-exit discriminator for best path selection.                                                                              | 0..4294967295 | \-      |
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------+---------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# policy SET_FULL_ROUTES
	dnRouter(cfg-rpl-policy)# rule 10 allow
	dnRouter(cfg-rpl-policy-rule-10)#set med 500


	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# policy PL_OUT
	dnRouter(cfg-rpl-policy)# rule 10 allow
	dnRouter(cfg-rpl-policy-rule-10)#set med igp-cost


	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# policy PL_IN
	dnRouter(cfg-rpl-policy)# rule 10 allow
	dnRouter(cfg-rpl-policy-rule-10)#set med + 30
	dnRouter(cfg-rpl-policy-rule-20)#set med - 5


**Removing Configuration**

To remove the set entry:
::

	dnRouter(cfg-rpl-policy-rule-10)# no set med

.. **Help line:** Set the BGP attribute MED

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 15.2    | 'igp-cost' and 'relative' options were added |
+---------+----------------------------------------------+
| 25.2    | Command syntax changed                       |
+---------+----------------------------------------------+
---


# SECTION 4: PREFIX-LIST

## Files from Prefix-list folder

Files in this section: 3

### routing-policy prefix-list description.rst

routing-policy prefix-list description
--------------------------------------

**Minimum user role:** operator

To add a description for your prefix list:

**Command syntax: description [description]**

**Command mode:** config

**Hierarchies**

- routing-policy prefix-list ipv4
- routing-policy prefix-list ipv6

**Parameter table:**

+----------------+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
|                |                                                                                                                                          |                       |
| Parameter      | Description                                                                                                                              | Range                 |
+================+==========================================================================================================================================+=======================+
|                |                                                                                                                                          |                       |
| description    | Enter a description for the   IP prefix-list.                                                                                            | 1..255 characters     |
|                |                                                                                                                                          |                       |
|                | Enter free-text description with spaces in between quotation   marks. If you do not use quotation marks, do not use spaces. For example: |                       |
|                |                                                                                                                                          |                       |
|                | ... description "My long description"                                                                                                    |                       |
|                |                                                                                                                                          |                       |
|                | ... description My_long_description                                                                                                      |                       |
+----------------+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| rule-type      | Defines whether the traffic matching the rule conditions are to be allowed or denied.                                                    | allow deny            |
+----------------+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# prefix-list ipv4 PL_MARTIANS
	dnRouter(cfg-rpl-pl)# description MyDescription

	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# prefix-list ipv6 PL6_MARTIANS
	dnRouter(cfg-rpl-pl6)# description MyDescription


**Removing Configuration**

To delete the description:
::

	dnRouter(cfg-rpl-pl6)# no description

.. **Help line:** Add description for an ip prefix-list

**Command History**

+-----------+-----------------------+
| Release   | Modification          |
+===========+=======================+
| 6.0       | Command introduced    |
+-----------+-----------------------+

---

### routing-policy prefix-list rule.rst

routing-policy prefix-list rule
-------------------------------

**Minimum user role:** operator

To configure prefix-list entries for IPv4 or IPv6 address family:

**Command syntax: rule [rule-id] [rule-type] [ip-prefix]** matching-len {ge [ge-value] le [le-value] \| eq [eq-value]}

**Command mode:** config

**Hierarchies**

- routing-policy prefix-list ipv4
- routing-policy prefix-list ipv6

**Note:**

Matching-len ge 3 le 32 means range 3-32.

.. Lower rule id is a higher priority rule

.. The rule id of 300000 is a default rule automatically assign by the system to deny any when no match was found.

.. Ip-prefix address-family must match the prefix list address-family

.. use matching-len to tune match for the subnet-mask.

.. must le-value >= ge-value.

.. cannot set le or ge together with eq

.. When configuring already configured rule-id, all of its entry is overwritten

.. The length specified by the range must be equal or longer than the length of the initial prefix.

.. no commands remove a specific rule entry by specifying the rule or by specifying rule sequence

**Parameter table**

+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| Parameter       | Description                                                                                                                                                                                                       | Range                        |
+=================+===================================================================================================================================================================================================================+==============================+
|                 |                                                                                                                                                                                                                   |                              |
| rule-id         | The rule's unique identifier within the prefix-list. It determines   the priority of the rule (rules with a low ID number have priority over rules   with high ID numbers). You must configure at least one rule. | 1..299999                    |
|                 |                                                                                                                                                                                                                   |                              |
|                 | The default ID (300000) is assigned by the system to "Deny   any" when no match is found.                                                                                                                         |                              |
|                 |                                                                                                                                                                                                                   |                              |
|                 | When configuring a rule ID that is already in use, all of the original rules' entries are overwritten.                                                                                                            |                              |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
|                 |                                                                                                                                                                                                                   | allow                        |
| rule-type       | Defines whether the traffic matching the rule conditions are to be allowed or denied.                                                                                                                             | deny                         |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
|                 | IPv4 or IPv6 prefix to match; any matches any prefix. The address family must match the prefix list address-family.                                                                                               | A.B.C.D/x                    |
| ip-prefix       |                                                                                                                                                                                                                   | xx:xx::xx:xx/x               |
|                 |                                                                                                                                                                                                                   | any                          |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
|                 | The range for tuning the match for the subnet mask.                                                                                                                                                               | For all values (ge, le, eq): |
| matching-len    | ge - greater or equal                                                                                                                                                                                             | 0..32 for IPv4               |
|                 | le - lower or equal                                                                                                                                                                                               | 0..128 for IPV6              |
|                 | eq - equal                                                                                                                                                                                                        |                              |
|                 | - le value must be ≥ ge value                                                                                                                                                                                     |                              |
|                 | - You cannot set le or ge together with eq                                                                                                                                                                        |                              |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# prefix-list ipv4 PL_ALLOW_ANY
	dnRouter(cfg-rpl-pl)# rule 4000000 allow any

	dnRouter(cfg-rpl)# prefix-list ipv4 PL_MARTIANS
	dnRouter(cfg-rpl-pl)# rule 10 allow 0.64.0.0/10

	dnRouter(cfg-rpl-pl)# rule 20 allow 192.0.0.0/24
	dnRouter(cfg-rpl-pl)# rule 10 deny 10.0.0.0/24

	dnRouter(cfg-rpl-pl)# rule 30 allow 224.0.0.0/3 matching-len ge 3 le 32
	dnRouter(cfg-rpl-pl)# rule 5 allow 0.0.0.0/0 matching-len ge 24 le 32

	dnRouter(cfg-rpl-pl)# rule 10 allow.0.0.0/8 matching-len eq 24

	dnRouter(cfg-rpl-pl)# rule 30 deny 224.0.0.0/3 matching-len ge 4 le 32
	dnRouter(cfg-rpl-pl)# rule 5 deny 0.0.0.0/0 matching-len ge 24 le 32



**Removing Configuration**

To remove a rule entry:
::

	dnRouter(cfg-rpl)# prefix-list ipv6 PL6_MARTIANS
	dnRouter(cfg-rpl-pl6)# no rule 20

	dnRouter(cfg-rpl)# prefix-list ipv4 PL_ALLOW_ANY
	dnRouter(cfg-rpl-pl)# no rule 20

.. Help line:** Configure prefix-list entry

**Command History**

+-------------+---------------------------------------+
|             |                                       |
| Release     | Modification                          |
+=============+=======================================+
|             |                                       |
| 6.0         | Command introduced                    |
+-------------+---------------------------------------+
|             |                                       |
| 11.0        | Updated matching-len range syntax     |
+-------------+---------------------------------------+
| 17.0        | Updated rule-id to maximum 299999     |
+-------------+---------------------------------------+

---

### routing-policy prefix-list.rst

routing-policy prefix-list
---------------------------

**Minimum user role:** operator

The prefix-list contains one or more ordered entries that are processed sequentially. To create a prefix-list and enter its configuration mode:

**Command syntax: prefix-list ipv4|ipv6 [prefix-list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy

**Note:**

- Notice the change in prompt from dnRouter(cfg-rpl)#  to dnRouter(cfg-rpl-pl)#  (prefix-list configuration mode). When entering IPv6 prefix-list configuration mode, the prompt is dnRouter(cfg-rpl-pl6)#

- You cannot delete a prefix list that is being used by another policy or protocol.

- An empty prefix-list(no rules) would act as MATCH-ALL

..  no commands remove the prefix-list configuration for all prefix-list of specific address-family or for a specific prefix-list

.. validation:

.. if a user tries to remove a prefix-list while it is attached to any policy or protocol, the following error should be displayed:

.. "Error: unable to remove prefix-list <ip-prefix-list-name>. prefix-list is attached to policy <policy-name>".

..   or

.. "Error: unable to remove prefix-list <ip-prefix-list-name>. prefix-list is attached to protocol {BGP,OSPF,LDP} with <configuration> attachment point".

**Parameter table**

+------------------+------------------------------------+--------+---------+
| Parameter        | Description                        | Range  | Default |
+==================+====================================+========+=========+
| prefix-list-name | Provide a name for the prefix list | String | \-      |
|                  |                                    | 1..255 |         |
+------------------+------------------------------------+--------+---------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# routing-policy
	dnRouter(cfg-rpl)# prefix-list ipv4 PL_MARTIANS
	dnRouter(cfg-rpl-pl)#

	dnRouter(cfg-rpl)# prefix-list ipv6 PL_MARTIANS
	dnRouter(cfg-rpl-pl6)#


.. **Help line:** Configure ip prefix-list

**Removing Configuration**

To remove the prefix-list configuration for all prefix lists of a specific address-family:
::

	dnRouter(cfg-rpl)# no prefix-list ipv4

To remove a specific prefix-list:
::

	dnRouter(cfg-rpl)# no prefix-list ipv6 PL_MARTIANS

**Command History**

+-----------+-----------------------+
| Release   | Modification          |
+===========+=======================+
| 6.0       | Command introduced    |
+-----------+-----------------------+
---


---

# ADDITIONAL SECTIONS ADDED Mon Sep  8 10:24:14 IDT 2025

---

# SECTION 5: ROUTING-OPTIONS

Files from Routing-options folder:       43 files

## bgp-vpls-label-block-size.rst

routing-options bgp-vpls-label-block-size
-----------------------------------------

**Minimum user role:** operator

Configure the the BGP-VPLS label block size for BGP-VPLS and BGP-VPWS services

**Command syntax: bgp-vpls-label-block-size [bgp-vpls-label-block-size]**

**Command mode:** config

**Hierarchies**

- routing-options

**Note**

- When bgp-vpls-label-block-size is set, the requested amount of labels will be allocates from the global mpls label pool.

- By default, BGP-VPLS labels will not be allocated unless the user explicitly configured it.

- If the first label was already allocated in the system - a system restart is required in order for the new configuration to take place

- If BGP tries to allocate a label from this pool but no contiguous label base exists - the allocation will fail and a system event will be raised.

**Parameter table**

+---------------------------+--------------------------------------------------+------------+---------+
| Parameter                 | Description                                      | Range      | Default |
+===========================+==================================================+============+=========+
| bgp-vpls-label-block-size | Configuration for bgp vpls/vpws label block size | 128-131072 | \-      |
+---------------------------+--------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# bgp-vpls-label-block-size 131072


**Removing Configuration**

To revert the BGP-VPLS label block size to 0
::

    dnRouter(cfg-routing-options)# no bgp-vpls-label-block-size

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| TBD     | Command introduced |
+---------+--------------------+

---

## admin-state.rst

routing-options bmp server admin-state
--------------------------------------

**Minimum user role:** operator

To enable the BMP server to which the BGP neighbor tables information will be sent.

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- routing-options bmp server

**Parameter table**

+-------------+------------------------+--------------+----------+
| Parameter   | Description            | Range        | Default  |
+=============+========================+==============+==========+
| admin-state | bmp server admin-state | | enabled    | disabled |
|             |                        | | disabled   |          |
+-------------+------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# bmp server 1
    dnRouter(cfg-routing-option-bmp)# admin-state enabled


**Removing Configuration**

To return the admin-state to the default value:
::

    dnRouter(cfg-routing-option-bmp)# no admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## bmp_server.rst

routing-options bmp server
--------------------------

**Minimum user role:** operator

To configure a BMP server to which the bgp monitoring information will be sent.

**Command syntax: bmp server [server-id]**

**Command mode:** config

**Hierarchies**

- routing-options

**Note**

- Up to 5 bmp servers can be configured per neighbor.

**Parameter table**

+-----------+---------------------+-------+---------+
| Parameter | Description         | Range | Default |
+===========+=====================+=======+=========+
| server-id | bmp server local id | 1-5   | \-      |
+-----------+---------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# bmp server 1
    dnRouter(cfg-routing-option-bmp)#


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-routing-option)# no bmp server 1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## class-of-service.rst

routing-options bmp server class-of-service
-------------------------------------------

**Minimum user role:** operator

To set the DSCP value for outgoing BMP packets.

**Command syntax: class-of-service [class-of-service]**

**Command mode:** config

**Hierarchies**

- routing-options bmp server

**Parameter table**

+------------------+-------------------------------------+-------+---------+
| Parameter        | Description                         | Range | Default |
+==================+=====================================+=======+=========+
| class-of-service | dscp value for outgoing BMP packets | 0-56  | 16      |
+------------------+-------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# bmp server 1
    dnRouter(cfg-routing-option-bmp)# class-of-service 48


**Removing Configuration**

To return the DSCP value to the default value:
::

    dnRouter(cfg-routing-option-bmp)# no class-of-service

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## description.rst

routing-options bmp server description
--------------------------------------

**Minimum user role:** operator

To set a description for the BMP server.

**Command syntax: description [description]**

**Command mode:** config

**Hierarchies**

- routing-options bmp server

**Parameter table**

+-------------+------------------------+------------------+---------+
| Parameter   | Description            | Range            | Default |
+=============+========================+==================+=========+
| description | bmp server description | | string         | \-      |
|             |                        | | length 1-255   |         |
+-------------+------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# bmp server 1
    dnRouter(cfg-routing-option-bmp)# description "bmp server running on openBMP"


**Removing Configuration**

To remove the description:
::

    dnRouter(cfg-routing-option-bmp)# no description

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## host.rst

routing-options bmp server host port
------------------------------------

**Minimum user role:** operator

To set the BMP server IP address and remote port for the BMP TCP session establishment.

**Command syntax: host [ip-address] port [dest-port]**

**Command mode:** config

**Hierarchies**

- routing-options bmp server

**Note**

- The host address and port must be configured for a BMP session to be established.

**Parameter table**

+------------+-------------------------------------------------------------------------+--------------+---------+
| Parameter  | Description                                                             | Range        | Default |
+============+=========================================================================+==============+=========+
| ip-address | bmp server ip-address                                                   | | A.B.C.D    | \-      |
|            |                                                                         | | X:X::X:X   |         |
+------------+-------------------------------------------------------------------------+--------------+---------+
| dest-port  | destination tcp port to be used for the tcp session with the bmp server | 1-65535      | \-      |
+------------+-------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# bmp server 2
    dnRouter(cfg-routing-option-bmp)# host 1.1.1.1 port 8000

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# bmp server 1
    dnRouter(cfg-routing-option-bmp)# host 1:1::1:1 port 8000


**Removing Configuration**

To remove the ip address and port configuration:
::

    dnRouter(cfg-routing-option-bmp)# no host

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## adj-in_post-policy.rst

routing-options bmp server route-monitoring adj-in post-policy
--------------------------------------------------------------

**Minimum user role:** operator

Enable exporting BGP neighbor adjacency-in post-policy tables. The configuration applies to all BGP neighbor address-families.

**Command syntax: adj-in post-policy [admin-state]**

**Command mode:** config

**Hierarchies**

- routing-options bmp server route-monitoring

**Parameter table**

+-------------+--------------------------------+--------------+----------+
| Parameter   | Description                    | Range        | Default  |
+=============+================================+==============+==========+
| admin-state | adjecenty in post policy table | | enabled    | disabled |
|             |                                | | disabled   |          |
+-------------+--------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# bmp server 1
    dnRouter(cfg-routing-option-bmp)# route-monitoring
    dnRouter(cfg-routing-option-bmp-rm)# adj-in post-policy enabled


**Removing Configuration**

To return the admin-state to the default value:
::

    dnRouter(cfg-routing-option-bmp)# no adj-in post-policy

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## adj-in_pre-policy.rst

routing-options bmp server route-monitoring adj-in pre-policy
-------------------------------------------------------------

**Minimum user role:** operator

Enable exporting BGP neighbor adjacency-in pre-policy tables. The configuration applies to all BGP neighbor address-families.

**Command syntax: adj-in pre-policy [admin-state]**

**Command mode:** config

**Hierarchies**

- routing-options bmp server route-monitoring

**Parameter table**

+-------------+-------------------------------+--------------+---------+
| Parameter   | Description                   | Range        | Default |
+=============+===============================+==============+=========+
| admin-state | adjecenty in pre policy table | | enabled    | enabled |
|             |                               | | disabled   |         |
+-------------+-------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# bmp server 1
    dnRouter(cfg-routing-option-bmp)# route-monitoring
    dnRouter(cfg-routing-option-bmp-rm)# adj-in pre-policy enabled


**Removing Configuration**

To return the admin-state to the default value:
::

    dnRouter(cfg-routing-option-bmp)# no adj-in pre-policy

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## route-monitoring.rst

routing-options bmp server route-monitoring
-------------------------------------------

**Minimum user role:** operator

To enter the BMP server route-monitoring configuration level. This allows you to define which BGP tables are exported by default to the BMP server.

**Command syntax: route-monitoring**

**Command mode:** config

**Hierarchies**

- routing-options bmp server

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# bmp server 1
    dnRouter(cfg-routing-option-bmp)# route-monitoring
    dnRouter(cfg-routing-option-bmp-rm)#


**Removing Configuration**

To return the route-monitoring to the default value:
::

    dnRouter(cfg-routing-option-bmp)# no route-monitoring

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## source-interface.rst

routing-options bmp server source-interface
-------------------------------------------

**Minimum user role:** operator

To set the interface from which the source IP address for the BMP session will be taken.

**Command syntax: source-interface [source-interface]**

**Command mode:** config

**Hierarchies**

- routing-options bmp server

**Note**

- The source IP type (IPv4 or IPv6) must match the server IP address-family. If one doesn't exist, the session will not open.

**Parameter table**

+------------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter        | Description                                                                      | Range            | Default |
+==================+==================================================================================+==================+=========+
| source-interface | By default , uses the  "system in-band-management source-interface" for the same | | string         | \-      |
|                  | vrf                                                                              | | length 1-255   |         |
+------------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# bmp server 1
    dnRouter(cfg-routing-option-bmp)# source-interface lo0

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# bmp server 2
    dnRouter(cfg-routing-option-bmp)# source-interface ge100-0/0/0


**Removing Configuration**

To return the source IP address to the default:
::

    dnRouter(cfg-routing-option-bmp)# no source-interface

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## fec-statistics.rst

routing-options fec-statistics
------------------------------

**Minimum user role:** operator

To configure the mpls fec-statistics operation mode:

**Command syntax: fec-statistics [fec-statistics]**

**Command mode:** config

**Hierarchies**

- routing-options

**Note**

- Default behavior is to counter per in-label and egress-interface for supported protocols

- Configuration applies to new installed FIB mpls routes only

**Parameter table**

+----------------+------------------------------------------------------------+-------------------------------+---------------------------+
| Parameter      | Description                                                | Range                         | Default                   |
+================+============================================================+===============================+===========================+
| fec-statistics | Configuration for mpls fec-statistics of in-label counters | | in-label-egress-interface   | in-label-egress-interface |
|                |                                                            | | disabled                    |                           |
+----------------+------------------------------------------------------------+-------------------------------+---------------------------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# fec-statistics disabled


**Removing Configuration**

To revert the behavior to its default:
::

    dnRouter(cfg-routing-option)# no fec-statistics

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.1    | Command introduced |
+---------+--------------------+

---

## flow.rst

routing-options load-balancing flow
-----------------------------------

**Minimum user role:** operator

To instruct the router which network headers to use to select one of multiple equal-cost paths to the destination for flow-based routing:

**Command syntax: flow [flow]**

**Command mode:** config

**Hierarchies**

- routing-options load-balancing

**Note**

- For fragmented packets, 3-tuple is used regardless of the configuration.

- Ethernet header is ignored in 3-tuple / 5-tuple based load-balancing for L3 interfaces

- no command returns flow to its default state

**Parameter table**

+-----------+-----------------------------------------------------------+---------------------------------------------------+---------+
| Parameter | Description                                               | Range                                             | Default |
+===========+===========================================================+===================================================+=========+
| flow      | The network headers to use for flow-based load-balancing. | | 3-tuple: Ethernet, MPLS, and IP                 | 5-tuple |
|           |                                                           | | 5-tuple: Ethernet, MPLS, IP, TCP/UDP, and GTP   |         |
+-----------+-----------------------------------------------------------+---------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# load-balancing
    dnRouter(cfg-routing-option-lb)# flow 3-tuple


**Removing Configuration**

To revert to the default values:
::

    dnRouter(cfg-routing-option-lb)# no flow

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.0    | Command introduced |
+---------+--------------------+

---

## load-balancing.rst

routing-options load-balancing
------------------------------

**Minimum user role:** operator

Load balancing is the ability to spread traffic over multiple paths to a destination. Typically, when the router learns multiple paths to
the same network via multiple routing protocols, it installs in its routing table only one route: the route with the lowest administrative distance.
Similarly, when the router learns multiple paths via the same routing protocol (i.e. with the same administrative distance), it selects the path with
the lowest cost to the destination. Load balancing can occur when the router is able to install multiple paths with the same administrative distance
and cost to the destination.


When there are equal-cost paths to a destination, the router runs a hash algorithm that uses the packet's 3-tuple or 5-tuple (configurable)
to select one of the paths for the packet, thus ensuring flow-based routing.


For the router to distribute the traffic over multiple paths, you need to:

-	Configure the protocols' maximum-paths attribute to a value greater than 1. This will allow the protocol to install multiple equal cost paths in the routing table (see bgp address-family maximum-paths and isis instance address-family maximum-paths)
-	Configure the flow type (3-tuple or 5-tuple) to be used for path selection (see routing-options load-balancing flow)


To enter load-balancing configuration mode:

**Command syntax: load-balancing**

**Command mode:** config

**Hierarchies**

- routing-options

**Note**

- Unequal cost and per-prefix load balancing are not supported.

- Notice the change in prompt.

- no command returns all load-balancing configurations to their default state

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# load-balancing
    dnRouter(cfg-routing-option-lb)#


**Removing Configuration**

To revert to all load-balancing configurations to their default value:
::

    dnRouter(cfg-routing-option)# no load-balancing

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.0    | Command introduced |
+---------+--------------------+

---

## mpls-speculative-parsing.rst

routing-options load-balancing mpls-speculative-parsing
-------------------------------------------------------

**Minimum user role:** operator

Enter the mpls-speculative-parsing configuration:

**Command syntax: mpls-speculative-parsing**

**Command mode:** config

**Hierarchies**

- routing-options load-balancing

**Note**

- The configuration is relevant for BRCM based platforms only

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# load-balancing
    dnRouter(cfg-routing-options-lb)# mpls-speculative-parsing
    dnRouter(cfg-routing-options-lb-msp)#


**Removing Configuration**

To revert all mpls-speculative-parsing configuration to its default value:
::

    dnRouter(cfg-routing-options-lb)# no mpls-speculative-parsing

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.1    | Command introduced |
+---------+--------------------+

---

## post-stack-first-nibble-of-zero.rst

routing-options load-balancing mpls-speculative-parsing post-stack-first-nibble-of-zero
---------------------------------------------------------------------------------------

**Minimum user role:** operator

At P Routers, when a Control-Word is sent on the packet only the label stack is used to create the load balancing keys and therefore in
the absence of a FAT or Entropy Label, load balancing is not achieved. Configure mpls-speculative-parsing behavior for case of post-stack-first-nibble
is value of 0x0 in order to speculate mpls payload as control-word with ethernet frame. As a result flow parameters from ethernet frame will be taken for
load-balancing consideration.


To configure post-stack-first-nibble-of-zero:

**Command syntax: post-stack-first-nibble-of-zero [post-stack-first-nibble-of-zero]**

**Command mode:** config

**Hierarchies**

- routing-options load-balancing mpls-speculative-parsing

**Note**
- The configuration is relevant for BRCM based platforms only
- Behavior applies on all NCPs in the cluster (and all units per NCP). Including new enabled NCPs
- Reconfiguration under traffic may lead to  temporary traffic corruption. Operator is advised to reconfigure only when cluster is not forwarding in-band traffic

**Parameter table**

+---------------------------------+----------------------------------------------------------------+--------------------+----------------+
| Parameter                       | Description                                                    | Range              | Default        |
+=================================+================================================================+====================+================+
| post-stack-first-nibble-of-zero | Define how to inyterpret the first nibble after the mpls stack | | no-speculation   | no-speculation |
|                                 |                                                                | | speculate-cw     |                |
+---------------------------------+----------------------------------------------------------------+--------------------+----------------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# load-balancing
    dnRouter(cfg-routing-options-lb)# mpls-speculative-parsing
    dnRouter(cfg-routing-options-lb-msp)# post-stack-first-nibble-of-zero speculate-cw


**Removing Configuration**

To revert all post-stack-first-nibble-of-zero configuration to default value:
::

    dnRouter(cfg-routing-options-lb-msp)# no post-stack-first-nibble-of-zero

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.1    | Command introduced |
+---------+--------------------+

---

## maximum-routes.rst

routing-options maximum-routes
------------------------------

**Minimum user role:** operator

When BGP is connected to multiple external peers it is difficult to control what these peers advertise. Routing polices are used to control what is accepted from a peer.
In cases where peers advertise a large amount of prefixes (more than the system can handle), the system is expected to be able to contain this load and once the issue is handled to resume the normal operation.


BGP protection can prevent this on the neighbor level, however if the scale is from multiple neighbors, there is no limitation in BGP and RIB and this scale can overload the whole system.


You can control the size of the RIB by setting thresholds to generate system event notifications. When a threshold is crossed, a system-event notification is generated allowing you to take action, if necessary.


RIB routes are limited in a 1:1 ratio between IPv4 and IPv6, for IGP routes, and a 4:1 ratio between IPv4 and IPv6 for other route types. When setting the maximum-route maximum value to 2,550,000,
the RIB will install up to 2,025,000 IPv4 routes and 525,000 IPv6 routes to the FIB. By default, limits IGP routes to 50,000 and will not install IGP routes above this limit.


To configure RIB size thresholds:

**Command syntax: maximum-routes [maximum]** threshold [threshold]

**Command mode:** config

**Hierarchies**

- routing-options

**Note**

- Set the maximum-routes to 0 to disable maximum-routes limitation and system-events.

- The thresholds are for IPv4 and IPv6 combined.

- When the number of routes drops below a threshold, a system-event notification is generated.

- Although new routes will still be accepted even if the max-routes limit is reached, you should remove any undesired local routes (e.g. unnecessary static routes), check if all BGP neighbors are justified and verify that the correct policies are used upon receiving a system-event notification that a threshold has been crossed.

- - In the example, the maximum number of routes in the RIB is set to 1,500,000 and the threshold is set to 70%. This means that when the number of routes in the RIB reaches 1,050,000, a system-event notification will be generated that the 70% threshold has been crossed. If you do nothing, you will not receive another notification until the number of routes reaches 1,500,000.

- Reconfiguration behavior:

- - when 'maximum' is reconfigured, resulting that current routes number is now below the new maximum value. over-the-limit routes will be installed upto new maximum value.

- - when 'maximum' is reconfigured, resulting that current routes number is now above the new maximum value. only new routes will be blocked from installment. No affect on existing routes that were already installed.

- no command returns maximum & threshold to their default values

**Parameter table**

+-----------+----------------------------------------------------------------------------------+--------------------+---------+
| Parameter | Description                                                                      | Range              | Default |
+===========+==================================================================================+====================+=========+
| maximum   | The maximum number of routes you want in the RIB.                                | 0, 100000-20000000 | 2550000 |
|           | Set maximum-routes to 0 to disable the maximum-routes limitation and system      |                    |         |
|           | events.                                                                          |                    |         |
+-----------+----------------------------------------------------------------------------------+--------------------+---------+
| threshold | A percentage (%) of max-routes to give you advance notice that the number of     | 1-100              | 75      |
|           | routes in the RIB is reaching the maximum level. When this threshold is crossed, |                    |         |
|           | a system-event notification is generated. You will not be notified again.        |                    |         |
+-----------+----------------------------------------------------------------------------------+--------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# maximum-routes 2000000

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# maximum-routes 1500000 threshold 70

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# maximum-routes 0


**Removing Configuration**

To revert to the default values:
::

    dnRouter(cfg-routing-option)# no maximum-routes

**Command History**

+---------+----------------------------------+
| Release | Modification                     |
+=========+==================================+
| 11.0    | Command introduced               |
+---------+----------------------------------+
| 13.2    | Updated command parameter ranges |
+---------+----------------------------------+

---

## ipv4-min-length.rst

routing-options next-hop-resolution ipv4 min-length
---------------------------------------------------

**Minimum user role:** operator

An operator can set the min-length constraint for the next-hop resolution by RIB. 
A common case is to set a long prefix length to avoid next-hop addresses to be resolved over default-route or summary-route, which may lead to traffic blackholing. 

To configure next-hop-resolution min-length:

**Command syntax: ipv4 min-length [ipv4-min-length]**

**Command mode:** config

**Hierarchies**

- routing-options next-hop-resolution
- network-services vrf instance routing-options next-hop-resolution

**Note**
- For 6PE, mapped IPv6 nexthop addresses ({::ffff:<ipv4-address>}) are handled in RIB as IPv4 address, and will be subjected to IPv4 min-length.

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter       | Description                                                                      | Range | Default |
+=================+==================================================================================+=======+=========+
| ipv4-min-length | Route that resolve a recursive next-hop must comply with the configured prefix   | 1-32  | \-      |
|                 | length minimum value in order to be valid                                        |       |         |
+-----------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# next-hop-resolution
    dnRouter(cfg-routing-option-nh-resolution)# ipv4 min-length 30

    dnRouter# configure
    dnRouter(cfg)# network-services
    dnRouter(cfg-netsrv)# vrf instance customer_vrf_1
    dnRouter(cfg-netsrv-vrf-inst)# routing-options
    dnRouter(cfg-vrf-inst-routing-options)# next-hop-resolution
    dnRouter(cfg-inst-routing-option-nh-resolution)# ipv4 min-length 30


**Removing Configuration**

To remove ipv4 min-length configuration:
::

    dnRouter(cfg-routing-option-nh-resolution)# no ipv4 min-length

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.1    | Command introduced |
+---------+--------------------+

---

## ipv6-min-length.rst

routing-options next-hop-resolution ipv6 min-length
---------------------------------------------------

**Minimum user role:** operator

An operator can set the min-length constraint for next-hop resolution by RIB. 
A common case is to set a long prefix length to avoid next-hop addresses to be resolved over default-route or summary-route, which may lead to traffic blackholing. 

To configure next-hop-resolution min-length:

**Command syntax: ipv6 min-length [ipv6-min-length]**

**Command mode:** config

**Hierarchies**

- routing-options next-hop-resolution
- network-services vrf instance routing-options next-hop-resolution

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter       | Description                                                                      | Range | Default |
+=================+==================================================================================+=======+=========+
| ipv6-min-length | Route that resolve a recursive next-hop must comply with the configured prefix   | 1-128 | \-      |
|                 | length minimum value in order to be valid                                        |       |         |
+-----------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# next-hop-resolution
    dnRouter(cfg-routing-option-nh-resolution)# ipv6 min-length 120

    dnRouter# configure
    dnRouter(cfg)# network-services
    dnRouter(cfg-netsrv)# vrf instance customer_vrf_1
    dnRouter(cfg-netsrv-vrf-inst)# routing-options
    dnRouter(cfg-vrf-inst-routing-options)# next-hop-resolution
    dnRouter(cfg-inst-routing-option-nh-resolution)# ipv6 min-length 120


**Removing Configuration**

To remove ipv6 min-length configuration:
::

    dnRouter(cfg-routing-option-nh-resolution)# no ipv6 min-length

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.1    | Command introduced |
+---------+--------------------+

---

## next-hop-resolution.rst

routing-options next-hop-resolution
-----------------------------------

**Minimum user role:** operator

Routing protocols leverage RIBs to find out how their route next-hop is resolved. This behavior is done via a next-hop-tracking mechanism. 
When a recursive route is installed, RIB resolves the route next-hop over its table to provide full route solution to FIB.  This behavior is known as PIC
An operator can configure a next-hop resolution constraint that will be enforced by the RIB. When a next-hop-resolution constraint is configured, the RIB will enforce that the resolving route of a protocol route nexthop must match required constraint. 
In case no route is found that can meet desired constraints: 
* RIB will reply to client protocol that no solution was found for next-hop tracking registration
* RIB will not install a Route path to the FIB for a nexthop with no valid solution.
To enter the mpls-nh-ipv6 routing table configuration level:

**Command syntax: next-hop-resolution**

**Command mode:** config

**Hierarchies**

- routing-options
- network-services vrf instance routing-options

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# next-hop-resolution
    dnRouter(cfg-routing-option-nh-resolution)#

    dnRouter# configure
    dnRouter(cfg)# network-services
    dnRouter(cfg-netsrv)# vrf instance customer_vrf_1
    dnRouter(cfg-netsrv-vrf-inst)# routing-options
    dnRouter(cfg-vrf-inst-routing-options)# next-hop-resolution
    dnRouter(cfg-inst-routing-option-nh-resolution)#


**Removing Configuration**

To revert all next-hop-resolution configurations to default:
::

    dnRouter(cfg-routing-option)# no next-hop-resolution

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.1    | Command introduced |
+---------+--------------------+

---

## next-hop-resources.rst

routing-options next-hop-resources threshold
--------------------------------------------

**Minimum user role:** operator

To configure the warning threshold for the next-hop resources in use:

**Command syntax: next-hop-resources threshold [threshold]**

**Command mode:** config

**Hierarchies**

- routing-options

**Parameter table**

+-----------+----------------------------------------------------------------------------------+-----------+---------+
| Parameter | Description                                                                      | Range     | Default |
+===========+==================================================================================+===========+=========+
| threshold | percent of max scale for which a syslog event will be sent when crossing         | 0, 50-100 | 75      |
|           | threshold                                                                        |           |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# next-hop-resources threshold 80
    dnRouter(cfg-routing-option)#


**Removing Configuration**

To revert the threshold to its default: 75%
::

    dnRouter(cfg-routing-option)# no next-hop-resources threshold

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## next-hop-resources.rst

routing-options next-hop-resources
----------------------------------

**Minimum user role:** operator

To configure the warning threshold for the next-hop resources in use:

**Command syntax: next-hop-resources**

**Command mode:** config

**Hierarchies**

- routing-options

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# next-hop-resources threshold 80
    dnRouter(cfg-routing-option)#


**Removing Configuration**

To revert the threshold to its default: 75%
::

    dnRouter(cfg-routing-option)# no next-hop-resources threshold

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## threshold.rst

routing-options next-hop-resources threshold
--------------------------------------------

**Minimum user role:** operator

To configure the warning threshold for the next-hop resources in use:

**Command syntax: threshold [threshold]**

**Command mode:** config

**Hierarchies**

- routing-options next-hop-resources

**Parameter table**

+-----------+----------------------------------------------------------------------------------+-----------+---------+
| Parameter | Description                                                                      | Range     | Default |
+===========+==================================================================================+===========+=========+
| threshold | percent of max scale for which a syslog event will be sent when crossing         | 0, 50-100 | 75      |
|           | threshold                                                                        |           |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# next-hop-resources
    dnRouter(cfg-routing-option-nh-resources)# threshold 80
    dnRouter(cfg-routing-option-nh-resources)#


**Removing Configuration**

To revert the threshold to its default: 75%
::

    dnRouter(cfg-routing-option-nh-resources)# no threshold

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## qppb-per-vrf.rst

routing-options qppb-per-vrf
----------------------------

**Minimum user role:** operator

An operator can select that all IP traffic forwarded in the default vrf will be subjected to qppb match, regardless of the traffic ingress interface.
To enable per vrf qppb:

**Command syntax: qppb-per-vrf**

**Command mode:** config

**Hierarchies**

- routing-options

**Note**

- When qppb-per-vrf is set for a given vrf, interfaces that belong to that vrf cannot have a qppb configuration. The user will not be able have either 'qppb enabled' or 'qppb disabled' for interfaces in vrf which has qppb-per-ver.

- Traffic redirected to the default vrf is subjected to qppb logic

- VPN traffic terminated in non-default vrf is not subjected to qppb logic, unless explicitly configured for the vrf instance

- When qppb-per-vrf is set, qppb statistics are provided per qppb rule level without interface granularity.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# qppb-per-vrf enabled


**Removing Configuration**

To revert the behavior to its default:
::

    dnRouter(cfg-routing-option)# no qppb-per-vrf

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.1    | Command introduced |
+---------+--------------------+

---

## router-id.rst

routing-options router-id
-------------------------

**Minimum user role:** operator

To manually set the router-id to be used by the routing protocols:

**Command syntax: router-id [router-id]**

**Command mode:** config

**Hierarchies**

- routing-options

**Note**

- used in default vrf

- no command returns router-id to default value

- When using OSPFv3 or IPv6-based BGP peering within a routing instance, you must explicitly configure a router ID (router-id) for that specific instance.

The main routing instance's router ID is not inherited by other instances. Even if only IPv6 protocols are used, a 32-bit router ID is still required, as IPv6 routing protocols rely on it for establishing adjacencies. The router ID must be a non-zero 32-bit (4-octet) unsigned integer. While it's common to use an IPv4 address as the router ID, this is not mandatory - it doesn’t need to be a valid or routable address, just a unique 32-bit value within the routing domain.

Failing to configure a router ID in an IPv6 OSPF or BGP instance will result in the protocol defaulting to 0.0.0.0, which is invalid. This will prevent adjacency formation and BGP session establishment.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+---------+-------------------------------------------------------------+
| Parameter | Description                                                                      | Range   | Default                                                     |
+===========+==================================================================================+=========+=============================================================+
| router-id | Set the network unique router ID. This ID will serve as the default ID for all   | A.B.C.D | The highest IPv4 address from any active loopback interface |
|           | routing protocols, unless otherwise specified.                                   |         |                                                             |
+-----------+----------------------------------------------------------------------------------+---------+-------------------------------------------------------------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# router-id 1.1.1.1


**Removing Configuration**

To remove the router-id configuration:
::

    dnRouter(cfg-routing-option)# no router-id

**Command History**

+---------+----------------------------------------------------------------------+
| Release | Modification                                                         |
+=========+======================================================================+
| 6.0     | Command introduced                                                   |
+---------+----------------------------------------------------------------------+
| 11.0    | Moved from the Protocols hierarchy to the Routing-options hierarchy. |
+---------+----------------------------------------------------------------------+

---

## routing-options.rst

routing-options
---------------

**Minimum user role:** operator

The routing options configuration hierarchy allows you to filter out routes that are installed in the routing tables based on policies.This is done per routing table.To apply a policy to the routing table follow this general procedure:

Enter the routing-options configuration hierarchy (see below).
Enter the configuration hierarchy for the specific routing table. See routing-options table.
Select the policy to apply to the table. See routing-options table install-policy.
To enter the routing options configuration mode:

**Command syntax: routing-options**

**Command mode:** config

**Note**

- Notice the change in prompt.

- no command returns all routing-options configurations to their default state

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)#


**Removing Configuration**

To revert all routing-options configurations to their default state:
::

    dnRouter(cfg)# no routing-options

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 10.0    | Command introduced |
+---------+--------------------+

---

## admin-state.rst

routing-options rpki server admin-state
---------------------------------------

**Minimum user role:** operator

To set the administrative state of the RPKI cache-server:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- routing-options rpki server

**Parameter table**

+-------------+-------------------------------+--------------+---------+
| Parameter   | Description                   | Range        | Default |
+=============+===============================+==============+=========+
| admin-state | RPKI cache server admin-state | | enabled    | enabled |
|             |                               | | disabled   |         |
+-------------+-------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server 1.1.1.1
    dnRouter(cfg-routing-options-rpki)# admin-state enabled

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server rpkiv.drivenets.com
    dnRouter(cfg-routing-options-rpki)# admin-state disabled


**Removing Configuration**

To return the admin-state to its default value:
::

    dnRouter(cfg-routing-options-rpki)# no admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.2    | Command introduced |
+---------+--------------------+

---

## expire-interval.rst

routing-options rpki server expire-interval
-------------------------------------------

**Minimum user role:** operator

To set the expire-interval value for the RTR session with the BGP RPKI cache server:

**Command syntax: expire-interval [expire-interval]**

**Command mode:** config

**Hierarchies**

- routing-options rpki server

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter       | Description                                                                      | Range      | Default |
+=================+==================================================================================+============+=========+
| expire-interval | Configures the time BGP waits to keep routes from a cache after the cache        | 360-172800 | 7200    |
|                 | session drops. Set expire-interval in seconds.                                   |            |         |
+-----------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server 1.1.1.1
    dnRouter(cfg-routing-options-rpki)# expire-interval 7200


**Removing Configuration**

To revert all rpki configuration to the default values:
::

    dnRouter(cfg-routing-options-rpki)# no expire-interval

**Command History**

+---------+------------------------------------------+
| Release | Modification                             |
+=========+==========================================+
| 15.1    | Command introduced                       |
+---------+------------------------------------------+
| 16.1    | Modified the expire-interval lower bound |
+---------+------------------------------------------+

---

## refresh-interval.rst

routing-options rpki server refresh-interval
--------------------------------------------

**Minimum user role:** operator

To set the refresh-interval value for the RTR session with the BGP RPKI cache server.

**Command syntax: refresh-interval [refresh-interval]**

**Command mode:** config

**Hierarchies**

- routing-options rpki server

**Parameter table**

+------------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter        | Description                                                                      | Range   | Default |
+==================+==================================================================================+=========+=========+
| refresh-interval | Configures the time BGP waits in before next periodic attempt to poll the cache  | 1-86400 | 3600    |
|                  | and between subsequent attempts. Set refresh-interval in seconds.                |         |         |
+------------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server 1.1.1.1
    dnRouter(cfg-routing-options-rpki)# refresh-interval 3600


**Removing Configuration**

To revert all rpki configuration to the default values:
::

    dnRouter(cfg-routing-options-rpki)# no refresh-interval

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## retry-interval.rst

routing-options rpki server retry-interval
------------------------------------------

**Minimum user role:** operator

To set the retry-interval value for the RTR session with the BGP RPKI cache server.

**Command syntax: retry-interval [retry-interval]**

**Command mode:** config

**Hierarchies**

- routing-options rpki server

**Parameter table**

+----------------+----------------------------------------------------------------------------------+--------+---------+
| Parameter      | Description                                                                      | Range  | Default |
+================+==================================================================================+========+=========+
| retry-interval | Configures the time BGP waits for a response after sending a serial or reset     | 1-7200 | 600     |
|                | query. Set retry-interval in seconds.                                            |        |         |
+----------------+----------------------------------------------------------------------------------+--------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server 1.1.1.1
    dnRouter(cfg-routing-options-rpki)# retry-interval 600


**Removing Configuration**

To revert all rpki configuration to the default values:
::

    dnRouter(cfg-routing-options-rpki)# no retry-interval

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## rpki_server.rst

routing-options rpki server
---------------------------

**Minimum user role:** operator

To configure a BGP RPKI cache server and its remote address.

**Command syntax: rpki server [server-address]**

**Command mode:** config

**Hierarchies**

- routing-options

**Note**

- Multiple RPKI cache-servers can be configured for redundancy.

- Sessions are established simultaneously with all the configured RPKI cache-servers.

**Parameter table**

+----------------+------------------------------------------+-------+---------+
| Parameter      | Description                              | Range | Default |
+================+==========================================+=======+=========+
| server-address | RPKI cache server IP address or hotsname | \-    | \-      |
+----------------+------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server 1.1.1.1
    dnRouter(cfg-routing-options-rpki)#

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server 2001:125:125::1
    dnRouter(cfg-routing-options-rpki)#

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server rpkiv.drivenets.com
    dnRouter(cfg-routing-options-rpki)#


**Removing Configuration**

To revert all RPKI cache-server's configuration to the default values:
::

    dnRouter(cfg-routing-options)# no rpki server 1.1.1.1

**Command History**

+---------+------------------------------------------------------+
| Release | Modification                                         |
+=========+======================================================+
| 15.1    | Command introduced                                   |
+---------+------------------------------------------------------+
| 16.2    | Replaced server identifier with the server's address |
+---------+------------------------------------------------------+

---

## source-interface.rst

routing-options rpki server source-interface
--------------------------------------------

**Minimum user role:** operator

To set the interface from which the source IP address for the RTR session with a BGP RPKI cache server will be taken.

**Command syntax: source-interface [source-interface]**

**Command mode:** config

**Hierarchies**

- routing-options rpki server

**Note**

- The source IP address type (IPv4 or IPv6) needs to match the IP address-family of the configured server. If such an address doesn't exist, the session will not open.

**Parameter table**

+------------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter        | Description                                                                      | Range            | Default |
+==================+==================================================================================+==================+=========+
| source-interface | By default the 'system in-band-management source-interface' for the same VRF is  | | string         | \-      |
|                  | used. If both are not configured, then egress-forwarding resolution shall        | | length 1-255   |         |
|                  | determine the interface and source IP address                                    |                  |         |
+------------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server 1.1.1.1
    dnRouter(cfg-routing-options-rpki)# source-interface lo0

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server rpkiv.drivenets.com
    dnRouter(cfg-routing-options-rpki)# source-interface ge100-0/0/0


**Removing Configuration**

To revert all rpki configuration to the default values:
::

    dnRouter(cfg-routing-options-rpki)# no source-interface

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## transport_ssh_password.rst

routing-options rpki server transport ssh password
--------------------------------------------------

**Minimum user role:** operator

To configure the password for the SSH transport session with the BGP RPKI cache-server.

**Command syntax: transport ssh password [ssh-session-password]**

**Command mode:** config

**Hierarchies**

- routing-options rpki server

**Note**

- There's no remove option for the SSH password as it is a mandatory config for the RPKI server when transport SSH is used. The user can only change the assigned SSH password.


- If the authentication secret is not entered with the command, then the user will be prompted to enter a password. The maximum length of this password is 80 characters. It shall then be encrypted and stored into the system.


- The maximum length of the encrypted password stored into the system is 255, as shown in the parameter table below.


**Parameter table**

+----------------------+---------------------------------------------------------------+------------------+---------+
| Parameter            | Description                                                   | Range            | Default |
+======================+===============================================================+==================+=========+
| ssh-session-password | Set a password for the SSH session with the RPKI cache-server | | string         | \-      |
|                      |                                                               | | length 1-255   |         |
+----------------------+---------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server 1.1.1.1
    dnRouter(cfg-routing-options-rpki)# transport ssh password EncryptedPassword

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server rpkiv.drivenets.com
    dnRouter(cfg-routing-options-rpki)# transport ssh password
    Enter password:
    Enter password for verification:

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server rpkiv.drivenets.com
    dnRouter(cfg-routing-options-rpki)# transport ssh password
    Enter password:
    Enter password for verification:
    {'ERROR': 'Invalid secret length!'}
    (Max encrypted length 255 Min secret length 1 Max Clear length 80).


**Removing Configuration**

To remove the configured SSH password:
::

    The SSH password is mandatory when transport SSH is used. You can only change it, not remove it.

**Command History**

+---------+---------------------------------------+
| Release | Modification                          |
+=========+=======================================+
| 15.1    | Command introduced                    |
+---------+---------------------------------------+
| 15.2    | Removed MD5 from the command's syntax |
+---------+---------------------------------------+

---

## transport_ssh_port.rst

routing-options rpki server transport ssh port
----------------------------------------------

**Minimum user role:** operator

To configure the port for the SSH transport session with the BGP RPKI cache-server.

**Command syntax: transport ssh port [ssh-port]**

**Command mode:** config

**Hierarchies**

- routing-options rpki server

**Note**
- There's no remove option for the SSH port as it is a mandatory config for the RPKI server when transport SSH is used. The user can only change the assigned SSH port.


**Parameter table**

+-----------+------------------------------------------------------------------------+---------+---------+
| Parameter | Description                                                            | Range   | Default |
+===========+========================================================================+=========+=========+
| ssh-port  | Destination port to be used for the session with the RPKI cache server | 1-65535 | \-      |
+-----------+------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server 1.1.1.1
    dnRouter(cfg-routing-options-rpki)# transport ssh port 323


**Removing Configuration**

To remove the configured SSH port:
::

    The SSH port is mandatory when transport SSH is used. You can only change it, not remove it.

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## transport_ssh_username.rst

routing-options rpki server transport ssh username
--------------------------------------------------

**Minimum user role:** operator

To configure the username for the SSH transport session with the BGP RPKI cache-server.

**Command syntax: transport ssh username [ssh-username]**

**Command mode:** config

**Hierarchies**

- routing-options rpki server

**Note**
- There's no remove option for the SSH username as it is a mandatory config for the RPKI server when transport SSH is used. The user can only change the assigned SSH username.


**Parameter table**

+--------------+-------------------------------------------------+------------------+---------+
| Parameter    | Description                                     | Range            | Default |
+==============+=================================================+==================+=========+
| ssh-username | Username for SSH session with RPKI cache server | | string         | \-      |
|              |                                                 | | length 1-255   |         |
+--------------+-------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server 1.1.1.1
    dnRouter(cfg-routing-options-rpki)# transport ssh username RPKIValidator


**Removing Configuration**

To remove the configured SSH username:
::

    The SSH username is mandatory when transport SSH is used. You can only change it, not remove it.

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## transport_tcp_port.rst

routing-options rpki server transport tcp port
----------------------------------------------

**Minimum user role:** operator

To configure the port for the TCP transport session with the BGP RPKI cache-server.

**Command syntax: transport tcp port [tcp-port]**

**Command mode:** config

**Hierarchies**

- routing-options rpki server

**Note**
- There's no remove option for the TCP port as it is a mandatory config for the RPKI server when transport TCP is used. The user can only change the assigned TCP port.


**Parameter table**

+-----------+------------------------------------------------------------------------+---------+---------+
| Parameter | Description                                                            | Range   | Default |
+===========+========================================================================+=========+=========+
| tcp-port  | Destination port to be used for the session with the RPKI cache server | 1-65535 | \-      |
+-----------+------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-options)# rpki server 1.1.1.1
    dnRouter(cfg-routing-options-rpki)# transport tcp port 323


**Removing Configuration**

To remove the configured TCP port:
::

    The TCP port is mandatory when transport TCP is used. You can only change it, not remove it.

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## global-block.rst

routing-options segment-routing mpls global-block
-------------------------------------------------

**Minimum user role:** operator

The segment routing global block (SRGB) is a set of labels that are reserved for segment routing and have global significance in the routing protocol domain.
The configured label block is reserved even if not used by any of the segment-routing capable protocols.
By default, the segment-routing capable protocols use the SRGB/SRLB range configured under the routing-options hierarchy level, unless a specific block is configured under the protocol level.

To configure the segment routing global block (SRGB) used by the router:

**Command syntax: global-block [lower-bound] [range]**

**Command mode:** config

**Hierarchies**

- routing-options segment-routing mpls

**Note**

- When changing the configuration, the new block will only apply on the next system restart. To view the configured labels blocks and the currently in used label blocks, use the show mpls label-allocation tables command.

- The base and range together define the block size (i.e. the number of labels in the block) and must be identical for all instances, even if segment-routing is disabled.

- SRGB and SRLB blocks must not overlap.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+-------------+---------+
| Parameter   | Description                                                                      | Range       | Default |
+=============+==================================================================================+=============+=========+
| lower-bound | Lower bound of the global label block. The block is defined to include this      | 256-1036384 | 16000   |
|             | label.                                                                           |             |         |
+-------------+----------------------------------------------------------------------------------+-------------+---------+
| range       | Define the srgb block size. for size of 1, only the lower-bound label exist in   | 1-1000000   | 8000    |
|             | block                                                                            |             |         |
+-------------+----------------------------------------------------------------------------------+-------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# segment-routing mpls
    dnRouter(cfg-routing-option-sr)# global-block 32000 16000


**Removing Configuration**

To revert to the default values: 
::

    dnRouter(cfg-routing-option-sr)# no global-block

**Command History**

+---------+------------------------------------------------------------+
| Release | Modification                                               |
+=========+============================================================+
| 14      | Command introduced                                         |
+---------+------------------------------------------------------------+
| 16.2    | Extened base maximum range to 1036384                      |
+---------+------------------------------------------------------------+
| 18.2    | Increase SRGB range to 400000                              |
+---------+------------------------------------------------------------+
| 18.3    | Increase SRGB lower-bound options and max range to 1000000 |
+---------+------------------------------------------------------------+

---

## local-block.rst

routing-options segment-routing mpls local-block
------------------------------------------------

**Minimum user role:** operator

The segment routing local block (SRLB) is a set of labels that have local significance only.
By default, the segment-routing capable protocols use the SRGB/SRLB range configured under the routing-options hierarchy level, unless a specific block is configured under the protocol level.
To configure the segment routing local block (SRLB) used by the router:

**Command syntax: local-block [lower-bound] [range]**

**Command mode:** config

**Hierarchies**

- routing-options segment-routing mpls

**Note**

- When changing the configuration, the new block will only apply on the next system restart. To view the configured labels blocks and the currently in used label blocks, use the show mpls label-allocation tables command.

- SRGB and SRLB blocks must be identical for all instances and must not overlap.

- SRGB and SRLB blocks must not overlap

**Parameter table**

+-------------+----------------------------------------------------------------------------------+-------------+---------+
| Parameter   | Description                                                                      | Range       | Default |
+=============+==================================================================================+=============+=========+
| lower-bound | Lower bound of the local label block.                                            | 256-1040383 | 8000    |
+-------------+----------------------------------------------------------------------------------+-------------+---------+
| range       | Define the SRLB block size. For size of 1, only the lower bound label exist in   | 1-1000000   | 8000    |
|             | block                                                                            |             |         |
+-------------+----------------------------------------------------------------------------------+-------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# segment-routing mpls
    dnRouter(cfg-routing-option-sr)# local-block 8000 1000


**Removing Configuration**

To revert to the default values: 
::

    dnRouter(cfg-routing-option-sr)# no local-block

**Command History**

+---------+-------------------------------------------------------------------+
| Release | Modification                                                      |
+=========+===================================================================+
| 14      | Command introduced                                                |
+---------+-------------------------------------------------------------------+
| 15      | Updated lower-bound from min 16 to min 256                        |
+---------+-------------------------------------------------------------------+
| 18.3    | Updated lower-bound parameter range and added range configuration |
+---------+-------------------------------------------------------------------+
| TBD     | Updated maximum supported range                                   |
+---------+-------------------------------------------------------------------+

---

## segment-routing.rst

routing-options segment-routing mpls
------------------------------------

**Minimum user role:** operator

Segment routing is a mechanism for source-based packet forwarding, where the source router pre-selects a path to the destination and encodes it
in the packet header as an ordered list of segments. A segment is an instruction consisting of a flat unsigned 20-bit identifier (the segment ID - SID) and is encoded as an MPLS label.

The interior gateway protocol (IGP) distributes two types of segments: prefix SIDs and adjacency SIDs.
The segment routing configuration level allows you to configure the segment routing global block (SRGB) and local block (SRLB) that will be used by the router.
Every node in the domain will receive a node SID from the global block, and every adjacency formed by each router receives a SID from the router's local block.

To enter the global segment routing configuration level:

**Command syntax: segment-routing mpls**

**Command mode:** config

**Hierarchies**

- routing-options

**Note**

- The SRGB and SRLB ranges affect the label pools assigned to other MPLS protocols such as RSVP, BGP, and LDP label pools.

- Notice the change in prompt.

- no command returns all segment-routing mpls configurations to their default state

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# segment-routing mpls
    dnRouter(cfg-routing-option-sr)#


**Removing Configuration**

To revert all segment-routing configurations to the default values:
::

    dnRouter(cfg-routing-option)# no segment-routing

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 14.0    | Command introduced |
+---------+--------------------+

---

## install-policy.rst

routing-options table mpls-nh-ipv6 install-policy
-------------------------------------------------

**Minimum user role:** operator

To set the import policy to apply on routes being installed in the routing table:


**Command syntax: install-policy [install-policy]**

**Command mode:** config

**Hierarchies**

- routing-options table mpls-nh-ipv6

**Note**

- policy only support the following action: match ipv4|ipv6 prefix [prefix-list-name]

- policy rule apply regardless of originating protocol

**Parameter table**

+----------------+---------------------------------------------------------------------------+------------------+---------+
| Parameter      | Description                                                               | Range            | Default |
+================+===========================================================================+==================+=========+
| install-policy | Set import policy to apply on routes being installed in the routing table | | string         | \-      |
|                |                                                                           | | length 1-255   |         |
+----------------+---------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# table mpls-nh-ipv6
    dnRouter(cfg-routing-option-mpls-nh-ipv6)# install-policy MPLS_NH_IPv6_POL


**Removing Configuration**

To remove the import policy:
::

    dnRouter(cfg-routing-option-mpls-nh-ipv6)# no install-policy

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.1    | Command introduced |
+---------+--------------------+

---

## table_mpls-nh-ipv6.rst

routing-options table mpls-nh-ipv6
----------------------------------

**Minimum user role:** operator

To enter the mpls-nh-ipv6 routing table configuration level:


**Command syntax: table mpls-nh-ipv6**

**Command mode:** config

**Hierarchies**

- routing-options

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# table mpls-nh-ipv6
    dnRouter(cfg-routing-option-mpls-nh-ipv6)#


**Removing Configuration**

To revert all table configurations to default:
::

    dnRouter(cfg-routing-option)# no table mpls-nh-ipv6

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 16.1    | Command introduced |
+---------+--------------------+

---

## install-policy.rst

routing-options table mpls-nh install-policy
--------------------------------------------

**Minimum user role:** operator

The install-policy enables to filter out destinations from being installed in the MPLS-NH table according to a predefined prefix-list using a policy. This prevents specific recursive routes from entering the tunnel, regardless of the originating protocol.
To set an import policy to apply on routes being installed in the routing table:

**Command syntax: install-policy [policy-name]**

**Command mode:** config

**Hierarchies**

- routing-options table mpls-nh

**Note**

- policy only support the following action: match ipv4|ipv6 prefix [prefix-list-name]

- policy rule apply regardless of originating protocol (RSVP, LDP, IGP-Shortcuts)

- no command removes the import policy

**Parameter table**

+-------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter   | Description                                                                      | Range            | Default |
+=============+==================================================================================+==================+=========+
| policy-name | The name of the policy that you want applied to installed routes.                | | string         | \-      |
|             | The policy only supports the following action: match ipv4|ipv6 prefix            | | length 1-255   |         |
|             | [prefix-list-name]. See policy match ip prefix.                                  |                  |         |
|             | The policy rule applies regardless of the originating protocol (RSVP, LDP,       |                  |         |
|             | IGP-shortcuts).                                                                  |                  |         |
+-------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# table mpls-nh
    dnRouter(cfg-routing-option-mpls-nh)# install-policy MPLS_NH_IN


**Removing Configuration**

To remove the policy import:
::

    dnRouter(cfg-routing-option-mpls-nh)# no install-policy MPLS_NH_IN

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 10.0    | Command introduced |
+---------+--------------------+

---

## table_mpls-nh.rst

routing-options table mpls-nh
-----------------------------

**Minimum user role:** operator

To enter configuration mode for the routing table to which you want to apply a policy (see explanation in routing-options):

**Command syntax: table mpls-nh**

**Command mode:** config

**Hierarchies**

- routing-options

**Note**

- Notice the change in prompt.

- no command returns all table configurations to their default state

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# table mpls-nh
    dnRouter(cfg-routing-option-mpls-nh)#


**Removing Configuration**

To revert all table configuration to the default values:
::

    dnRouter(cfg-routing-option)# no table mpls-nh

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 10.0    | Command introduced |
+---------+--------------------+

---

## throttle-link-state-changes.rst

routing-options throttle-link-state-changes min-delay max-delay
---------------------------------------------------------------

**Minimum user role:** operator

Use this command to aggregate multiple different interface state-changes to a single event. The routing protocols will treat all state changes as if they occurred at once.

**Command syntax: throttle-link-state-changes min-delay [min-delay] max-delay [max-delay]**

**Command mode:** config

**Hierarchies**

- routing-options

**Note**

- Require max-delay > min-delay

- Reconfiguring throttle-link-state-changes timers will immediately invoke any aggregated events. Any following interface state change will be delayed and aggregated according to new timers.

- no command min-delay & max-delay to their default values

**Parameter table**

+-----------+----------------------------------------------------------------------------------+---------+---------+
| Parameter | Description                                                                      | Range   | Default |
+===========+==================================================================================+=========+=========+
| min-delay | The minimal delay to be added for any interface state-change.                    | 0-5000  | 0       |
|           | A value of 0 will result in no aggregation taking place and the protocol will    |         |         |
|           | react immediately upon interface state change.                                   |         |         |
+-----------+----------------------------------------------------------------------------------+---------+---------+
| max-delay | The maximum delay allowed for any interface state change.                        | 1-60000 | 2000    |
+-----------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-options
    dnRouter(cfg-routing-option)# throttle-link-state-changes min-delay 100 max-delay 2000
    dnRouter(cfg-routing-option)#


**Removing Configuration**

To revert min-delay and max-delay to their default value:
::

    dnRouter(cfg-routing-option)# no throttle-link-state-changes

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

---

# SECTION 6: ROUTING-POLICY

Files from Routing-policy folder:      160 files

## as-path-acl-list.rst

routing-policy as-path-list
---------------------------

**Minimum user role:** operator

When a prefix announcement passes through an AS, that AS adds its AS number to the AS-path attribute. An AS can reject an announcement for a route that it originated, or reject an announcement that contains the local AS number in its AS-path. In this way, the AS-path helps prevent looping announcements.
You can define an access-list rule for an AS-path to use with BGP.
To create an access-list rule for the AS-path and enter its configuration mode:

**Command syntax: as-path-list [as-path-list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy

**Note**

- validation: if a user tries to remove an as-path  *-*  list while it is attached to any policy or protocol, the following error should be displayed:

 Error: unable to remove as-path-list <as-path-acl-name>. as-path-list is attached to policy <policy-name>

**Parameter table**

+-------------------+-------------------------------------+------------------+---------+
| Parameter         | Description                         | Range            | Default |
+===================+=====================================+==================+=========+
| as-path-list-name | Provide a name for the as-path list | | string         | \-      |
|                   |                                     | | length 1-255   |         |
+-------------------+-------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# as-path-list ASP_LOCAL
    dnRouter(cfg-rpl-asp)#


**Removing Configuration**

To remove the as-path rule entry:
::

    dnRouter(cfg-rpl)# no as-path-list

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## rule-passes-through.rst

routing-policy as-path-list rule
--------------------------------

**Minimum user role:** operator

This command matches the BGP AS path using regular expressions.

**Command syntax: rule [rule-id] [rule-type] passes-through [passes-through-as]**

**Command mode:** config

**Hierarchies**

- routing-policy as-path-list

**Note**

- If no match was found, the AS number will be denied.

- Rule 65535 is reserved as default rule of deny any as-number

**Parameter table**

+-------------------+----------------------------------------------------------------------------------+---------------------------+---------+
| Parameter         | Description                                                                      | Range                     | Default |
+===================+==================================================================================+===========================+=========+
| rule-id           | The rule's unique identifier within the as-path list. It determines the priority | 1-65534                   | \-      |
|                   | of the rule (rules with a low ID number have priority over rules with high ID    |                           |         |
|                   | numbers). You must configure at least one rule.                                  |                           |         |
+-------------------+----------------------------------------------------------------------------------+---------------------------+---------+
| rule-type         | Defines whether the traffic matching the rule conditions are to be allowed or    | | allow                   | \-      |
|                   | denied.                                                                          | | deny                    |         |
+-------------------+----------------------------------------------------------------------------------+---------------------------+---------+
| passes-through-as | Verifies if the specified AS numbers match the BGP AS path. The value can be a   | 0..4294967295 x-y (range) | \-      |
|                   | specific AS number (e.g. 7677) or a range (e.g. 65000-65020).                    |                           |         |
+-------------------+----------------------------------------------------------------------------------+---------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# as-path-list ASP_LOCAL
    dnRouter(cfg-rpl-asp)# rule 10 allow passes-through 65060
    dnRouter(cfg-rpl-asp)# rule 20 allow passes-through 65000-65100


**Removing Configuration**

To remove a rule entry:
::

    dnRouter(cfg-rpl-asp)# no rule 10

**Command History**

+---------+------------------------------------------------------------------------------------+
| Release | Modification                                                                       |
+=========+====================================================================================+
| 6.0     | Command introduced                                                                 |
+---------+------------------------------------------------------------------------------------+
| 11.0    | Updated rule-id range to max 65534 as rule 65535 is reserved for the default rule. |
+---------+------------------------------------------------------------------------------------+

---

## rule-regex.rst

routing-policy as-path-list rule
--------------------------------

**Minimum user role:** operator

This command matches the BGP AS path using regular expressions.

**Command syntax: rule [rule-id] [rule-type] regex [regex]**

**Command mode:** config

**Hierarchies**

- routing-policy as-path-list

**Note**

- A lower rule-id results in higher priority

- If no match was found, the AS number will be denied.

- Rule 65535 is reserved as default rule of deny any as-number

**Parameter table**

+-----------+----------------------------------------------------------------------------------+-----------+---------+
| Parameter | Description                                                                      | Range     | Default |
+===========+==================================================================================+===========+=========+
| rule-id   | The rule's unique identifier within the as-path list. It determines the priority | 1-65534   | \-      |
|           | of the rule (rules with a low ID number have priority over rules with high ID    |           |         |
|           | numbers). You must configure at least one rule.                                  |           |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+
| rule-type | Defines whether the traffic matching the rule conditions are to be allowed or    | | allow   | \-      |
|           | denied.                                                                          | | deny    |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+
| regex     | A regular expression defining a search pattern to match communities attribute in | \-        | \-      |
|           | BGP updates.                                                                     |           |         |
|           | See Regular Expressions.                                                         |           |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# as-path-list ASP_LOCAL
    dnRouter(cfg-rpl-asp)# rule 10 allow regex _64[5-9][0-9][0-9]_

    dnRouter(cfg-rpl-asp)# rule 20 allow regex _6555[0-1]_


**Removing Configuration**

To remove a rule entry:
::

    dnRouter(cfg-rpl-asp)# no rule 10

**Command History**

+---------+------------------------------------------------------------------------------------+
| Release | Modification                                                                       |
+=========+====================================================================================+
| 6.0     | Command introduced                                                                 |
+---------+------------------------------------------------------------------------------------+
| 11.0    | Updated rule-id range to max 65534 as rule 65535 is reserved for the default rule. |
+---------+------------------------------------------------------------------------------------+

---

## community-list.rst

routing-policy community-list
-----------------------------

**Minimum user role:** operator

A community list is a user defined communities attribute list that can be used for matching or manipulating the communities attribute in updates. There are two types of community lists:

- Standard community list - defines the communities attribute

- Extended community list - defines the communities attribute string with regular expression

The standard community list is compiled into binary format and is directly compared to the BGP communities attribute in BGP updates. Therefore, the comparison is faster than in the extended community list.

To define a new standard community list and enter its configuration mode:

**Command syntax: community-list [community-list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy

**Note**

- You cannot delete a community list that is attached to a policy.

**Parameter table**

+---------------------+--------------------------------+------------------+---------+
| Parameter           | Description                    | Range            | Default |
+=====================+================================+==================+=========+
| community-list-name | The name of the community-list | | string         | \-      |
|                     |                                | | length 1-255   |         |
+---------------------+--------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# community-list CL_NAME
    dnRouter(cfg-rpl-cl)#


**Removing Configuration**

To delete a community list:
::

    dnRouter(cfg-rpl)# no community-list CL_NAME

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## rule-regex.rst

routing-policy community-list rule
----------------------------------

**Minimum user role:** operator

To configure regex rules for standard community lists:

**Command syntax: rule [rule-id] [rule-type] regex [regex]**

**Command mode:** config

**Hierarchies**

- routing-policy community-list

**Note**

- You can configure multiple communities in a single community list.

- Communities from the 65535:<id> range are reserved as well known communities assigned by IANA.

- You must set at least one community to configure community-list.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+-----------+---------+
| Parameter | Description                                                                      | Range     | Default |
+===========+==================================================================================+===========+=========+
| rule-id   | The rule's unique identifier within the community list. It determines the        | 1-65534   | \-      |
|           | priority of the rule (rules with a low ID number have priority over rules with   |           |         |
|           | high ID numbers). You must configure at least one rule.                          |           |         |
|           | The default ID (65535) is assigned by the system to 'Deny any' when no match is  |           |         |
|           | found.                                                                           |           |         |
|           | When configuring a rule ID that is already in use, all of the original rules'    |           |         |
|           | entries are overwritten.                                                         |           |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+
| rule-type | Defines whether the traffic matching the rule conditions are to be allowed or    | | allow   | \-      |
|           | denied.                                                                          | | deny    |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+
| regex     | A regular expression defining a search pattern to match communities attribute in | \-        | \-      |
|           | BGP updates.                                                                     |           |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# community-list CL_NAME
    dnRouter(cfg-rpl-cl)# rule 10 allow regex 65000:5000|_65000:3[0-9][0-9][0-9][0-9]


**Removing Configuration**

To remove a rule entry:
::

    dnRouter(cfg-rpl-cl)# no rule 10

**Command History**

+---------+---------------------------------------------------------+
| Release | Modification                                            |
+=========+=========================================================+
| 6.0     | Command introduced                                      |
+---------+---------------------------------------------------------+
| 10.0    | Added well-known communities 'no-llgr' and 'llgr-stale' |
+---------+---------------------------------------------------------+
| 11.5    | AS_number range changed from 1..65534 to 1..65535       |
+---------+---------------------------------------------------------+

---

## rule-value.rst

routing-policy community-list rule
----------------------------------

**Minimum user role:** operator

To configure 'value' rules for standard community lists:

**Command syntax: rule [rule-id] [rule-type] value [community-value]**

**Command mode:** config

**Hierarchies**

- routing-policy community-list

**Note**

- You can configure multiple communities in a single community list.

- Communities from the 65535:<id> range are reserved as well known communities assigned by IANA.

- You must set at least one community to configure community-list.

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+-------------------------+---------+
| Parameter       | Description                                                                      | Range                   | Default |
+=================+==================================================================================+=========================+=========+
| rule-id         | The rule's unique identifier within the community list. It determines the        | 1-65534                 | \-      |
|                 | priority of the rule (rules with a low ID number have priority over rules with   |                         |         |
|                 | high ID numbers). You must configure at least one rule.                          |                         |         |
|                 | The default ID (65535) is assigned by the system to 'Deny any' when no match is  |                         |         |
|                 | found.                                                                           |                         |         |
|                 | When configuring a rule ID that is already in use, all of the original rules'    |                         |         |
|                 | entries are overwritten.                                                         |                         |         |
+-----------------+----------------------------------------------------------------------------------+-------------------------+---------+
| rule-type       | Defines whether the traffic matching the rule conditions are to be allowed or    | | allow                 | \-      |
|                 | denied.                                                                          | | deny                  |         |
+-----------------+----------------------------------------------------------------------------------+-------------------------+---------+
| community-value | The community number (e.g. aa:nn), range (e.g. aa-bb:nn)                         | | AS_number: 0..65535   | \-      |
|                 | <AS_number:id>,                                                                  | | ID: 0..65535          |         |
|                 | <lower_AS_number-upper_AS_number:lower_id-upper_id>                              |                         |         |
+-----------------+----------------------------------------------------------------------------------+-------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# community-list CL_NAME
    dnRouter(cfg-rpl-cl)# rule 10 allow value 65000:1000
    dnRouter(cfg-rpl-cl)# rule 20 allow value 8000-9000:2000
    dnRouter(cfg-rpl-cl)# rule 30 allow value 9500:2000-3000
    dnRouter(cfg-rpl-cl)# rule 40 allow value 10000-11000:40-50


**Removing Configuration**

To remove a rule entry:
::

    dnRouter(cfg-rpl-lcl)# no rule 10

**Command History**

+---------+---------------------------------------------------------+
| Release | Modification                                            |
+=========+=========================================================+
| 6.0     | Command introduced                                      |
+---------+---------------------------------------------------------+
| 10.0    | Added well-known communities 'no-llgr' and 'llgr-stale' |
+---------+---------------------------------------------------------+
| 11.5    | AS_number range changed from 1..65534 to 1..65535       |
+---------+---------------------------------------------------------+

---

## rule-well-known-community.rst

routing-policy community-list rule
----------------------------------

**Minimum user role:** operator

To configure rules for reserved well-known standard community lists:

**Command syntax: rule [rule-id] [rule-type] well-known-community [well-known-community]**

**Command mode:** config

**Hierarchies**

- routing-policy community-list

**Note**

- You can configure multiple communities in a single community list.

- Communities from the 65535:<id> range are reserved as well known communities assigned by IANA.

- You must set at least one community to configure community-list.

**Parameter table**

+----------------------+----------------------------------------------------------------------------------+--------------------------------------------------------------------------+---------+
| Parameter            | Description                                                                      | Range                                                                    | Default |
+======================+==================================================================================+==========================================================================+=========+
| rule-id              | The rule's unique identifier within the community list. It determines the        | 1-65534                                                                  | \-      |
|                      | priority of the rule (rules with a low ID number have priority over rules with   |                                                                          |         |
|                      | high ID numbers). You must configure at least one rule.                          |                                                                          |         |
|                      | The default ID (65535) is assigned by the system to 'Deny any' when no match is  |                                                                          |         |
|                      | found.                                                                           |                                                                          |         |
|                      | When configuring a rule ID that is already in use, all of the original rules'    |                                                                          |         |
|                      | entries are overwritten.                                                         |                                                                          |         |
+----------------------+----------------------------------------------------------------------------------+--------------------------------------------------------------------------+---------+
| rule-type            | Defines whether the traffic matching the rule conditions are to be allowed or    | | allow                                                                  | \-      |
|                      | denied.                                                                          | | deny                                                                   |         |
+----------------------+----------------------------------------------------------------------------------+--------------------------------------------------------------------------+---------+
| well-known-community | A reserved well-known community.                                                 | | internet - advertise to all neighbors                                  | \-      |
|                      |                                                                                  | | accept-own - first come first served                                   |         |
|                      |                                                                                  | | Local-AS - cannot be advertised to eBGP neighbors                      |         |
|                      |                                                                                  | | No-export - advertise only to same as neighbors                        |         |
|                      |                                                                                  | | No-advertise - not advertised to any neighbor                          |         |
|                      |                                                                                  | | No-LLGR - marks routes to not be treated according to LLGR rules       |         |
|                      |                                                                                  | | LLGR-Stale - marks stale routes retained for a longer period of time   |         |
+----------------------+----------------------------------------------------------------------------------+--------------------------------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# community-list CL_NAME
    dnRouter(cfg-rpl-cl)# rule 10 allow well-known-community internet
    dnRouter(cfg-rpl-cl)# rule 20 allow well-known-community no-export


**Removing Configuration**

To remove a rule entry:
::

    dnRouter(cfg-rpl-cl)# no rule 10

**Command History**

+---------+---------------------------------------------------------+
| Release | Modification                                            |
+=========+=========================================================+
| 6.0     | Command introduced                                      |
+---------+---------------------------------------------------------+
| 10.0    | Added well-known communities 'no-llgr' and 'llgr-stale' |
+---------+---------------------------------------------------------+
| 11.5    | AS_number range changed from 1..65534 to 1..65535       |
+---------+---------------------------------------------------------+

---

## extcommunity-list.rst

routing-policy extcommunity-list
--------------------------------

**Minimum user role:** operator

A community list is a user defined communities attribute list that can be used for matching or manipulating the communities attribute in updates. There are two types of community lists:

- Standard community list - defines the communities attribute

- Extended community list - defines the communities attribute string with regular expression

The standard community list is compiled into binary format and is directly compared to the BGP communities attribute in BGP updates. Therefore, the comparison is faster than in the extended community list.

You can set multiple extcoummunities in a single extcommunity-list.

To define a new extended community list:

**Command syntax: extcommunity-list [extcommunity-list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy

**Note**

- You cannot delete an extcommunity list that is attached to a policy.

**Parameter table**

+------------------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter              | Description                                                                      | Range            | Default |
+========================+==================================================================================+==================+=========+
| extcommunity-list-name | The name of the extended community-list. The name cannot contain only numbers;   | | string         | \-      |
|                        | it must contain at least one letter.                                             | | length 1-255   |         |
+------------------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# extcommunity-list EXTCL_NAME
    dnRouter(cfg-rpl-extcl)#


**Removing Configuration**

To delete an extended community list:
::

    dnRouter(cfg-rpl)# no extcommunity-list EXTCL_NAME

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## rule_color_value.rst

routing-policy extcommunity-list rule
-------------------------------------

**Minimum user role:** operator

To set a match entry on a color extended community value:

**Command syntax: rule [rule-id] [rule-type] color value [color-value]**

**Command mode:** config

**Hierarchies**

- routing-policy extcommunity-list

**Note**

- option is mutually exclusive (per rule) with rt and soo extcommunity.

**Parameter table**

+-------------+------------------------------------------------------------+--------------+---------+
| Parameter   | Description                                                | Range        | Default |
+=============+============================================================+==============+=========+
| rule-id     | allow or deny the community                                | 1-65534      | \-      |
+-------------+------------------------------------------------------------+--------------+---------+
| rule-type   | Action that will be done upon rule match (e.g. deny/allow) | | allow      | \-      |
|             |                                                            | | deny       |         |
+-------------+------------------------------------------------------------+--------------+---------+
| color-value | extcommunity color value                                   | 0-4294967295 | \-      |
+-------------+------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# extcommunity-list EXTCL_NAME
    dnRouter(cfg-rpl-extcl)# rule 10 allow color value 10


**Removing Configuration**

To delete the rule:
::

    dnRouter(cfg-rpl-extcl)# no  rule 10

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## rule_regex.rst

routing-policy extcommunity-list rule
-------------------------------------

**Minimum user role:** operator

To set a match entry on a color extended community regular expression:

**Command syntax: rule [rule-id] [rule-type] regex [regex]**

**Command mode:** config

**Hierarchies**

- routing-policy extcommunity-list

**Note**

- Regex pattern is match on the Extended Community string as see on 'show bgp route'

- Can match on multiple extcommunity types with same pattern

- If specific extcommunity type is required pattern should include 'RT', 'SoO' or 'Color' to match type in string

- The option is mutually exclusive (per rule) with rt and soo extcommunity.

**Parameter table**

+-----------+------------------------------------------------------------+-----------+---------+
| Parameter | Description                                                | Range     | Default |
+===========+============================================================+===========+=========+
| rule-id   | allow or deny the community                                | 1-65534   | \-      |
+-----------+------------------------------------------------------------+-----------+---------+
| rule-type | Action that will be done upon rule match (e.g. deny/allow) | | allow   | \-      |
|           |                                                            | | deny    |         |
+-----------+------------------------------------------------------------+-----------+---------+
| regex     | extcommunity regular expression                            | \-        | \-      |
+-----------+------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# extcommunity-list EXTCL_NAME
    dnRouter(cfg-rpl-extcl)# rule 10 allow regex 'RT:21{1,4}:100'
    dnRouter(cfg-rpl-extcl)# rule 10 allow regex 'SoO:40:100$'
    dnRouter(cfg-rpl-extcl)# rule 30 allow regex 'RT:21{1,4}:200|SoO:40:300$'
    dnRouter(cfg-rpl-extcl)# rule 10 allow regex 'Color:8000'


**Removing Configuration**

To delete the rule:
::

    dnRouter(cfg-rpl-extcl)# no rule 10

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## rule-value.rst

routing-policy extcommunity-list rule
-------------------------------------

**Minimum user role:** operator

To configure 'value' rules for extended community lists:

**Command syntax: rule [rule-id] [rule-type] [extcommunity-format] value [extcommunity-value]**

**Command mode:** config

**Hierarchies**

- routing-policy extcommunity-list

**Note**

- You can configure multiple communities in a single community list.

- Communities from the 65535:<id> range are reserved as well known communities assigned by IANA.

- Can be set a simple extcommunity value or an extcommunity range.

- Using [as-number-short]l or [as-number-short]L will code as-number-short number in a 32 bit field resulting in a Type1 route-distinguisher.

**Parameter table**

+---------------------+----------------------------------------------------------------------------------+---------------------------------------+---------+
| Parameter           | Description                                                                      | Range                                 | Default |
+=====================+==================================================================================+=======================================+=========+
| rule-id             | The rule's unique identifier within the community list. It determines the        | 1-65534                               | \-      |
|                     | priority of the rule (rules with a low ID number have priority over rules with   |                                       |         |
|                     | high ID numbers). You must configure at least one rule.                          |                                       |         |
|                     | The default ID (65535) is assigned by the system to 'Deny any' when no match is  |                                       |         |
|                     | found.                                                                           |                                       |         |
|                     | When configuring a rule ID that is already in use, all of the original rules'    |                                       |         |
|                     | entries are overwritten.                                                         |                                       |         |
+---------------------+----------------------------------------------------------------------------------+---------------------------------------+---------+
| rule-type           | Defines whether the traffic matching the rule conditions are to be allowed or    | | allow                               | \-      |
|                     | denied.                                                                          | | deny                                |         |
+---------------------+----------------------------------------------------------------------------------+---------------------------------------+---------+
| extcommunity-format | [rt]: A route target is a BGP extended communities attribute that defines which  | | rt                                  | \-      |
|                     | VPN routes are exported and imported on the routers.                             | | soo                                 |         |
|                     | [soo]: BGP site of origin (SoO) is a tag that is appended on BGP updates to      |                                       |         |
|                     | allow to mark a specific peer as belonging to a particular site. By tagging the  |                                       |         |
|                     | route, BGP will check if the peer's site of origin is listed in the community    |                                       |         |
|                     | field. If it is then the route will be filtered. If not, then the route will be  |                                       |         |
|                     | advertised as normal.                                                            |                                       |         |
+---------------------+----------------------------------------------------------------------------------+---------------------------------------+---------+
| extcommunity-value  | Type0:                                                                           | | as-number-short: 0-65535            | \-      |
|                     | <[as-number-short]:[id-long]>                                                    | | as-number-long: (2^16)-4294967295   |         |
|                     | Type1:                                                                           | | id-short: 0-65535                   |         |
|                     | <[as-number-short]l:[id-short]>                                                  | | id-long: 0-4294967295               |         |
|                     | <[as-number-short]L:[id-short]>                                                  | | ipv4-address-prefix: A.B.C.D        |         |
|                     | <[as-number-long]:[id-short]>                                                    |                                       |         |
|                     | Type2:                                                                           |                                       |         |
|                     | <[ipv4-address-prefix]:[id-short]>                                               |                                       |         |
+---------------------+----------------------------------------------------------------------------------+---------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# extcommunity-list EXTCL_NAME
    dnRouter(cfg-rpl-extcl)# rule 10 allow rt value 65000:1000
    dnRouter(cfg-rpl-extcl)# rule 20 allow soo value 65000:2000
    dnRouter(cfg-rpl-extcl)# rule 30 deny rt value 65000l:5000
    dnRouter(cfg-rpl-extcl)# rule 40 deny soo value 9000L:500
    dnRouter(cfg-rpl-extcl)# rule 50 deny soo value 10.170.0.64:500

    dnRouter(cfg-rpl-extcl)# rule 110 allow rt value 4000-5000:1000
    dnRouter(cfg-rpl-extcl)# rule 120 allow soo value 50000-90000L:2000-3000
    dnRouter(cfg-rpl-extcl)# rule 130 deny rt value 10.180.2.64/24:10-50


**Removing Configuration**

To remove a rule entry:
::

    dnRouter(cfg-rpl-lcl)# no rule 10

**Command History**

+---------+-------------------------+
| Release | Modification            |
+=========+=========================+
| 6.0     | Command introduced      |
+---------+-------------------------+
| 17.0    | Remove the regex option |
+---------+-------------------------+

---

## flowspec-local-policies.rst

routing-policy flowspec-local-policies
--------------------------------------

**Minimum user role:** operator

To configure a policy based routing rule:

**Command syntax: flowspec-local-policies**

**Command mode:** config

**Hierarchies**

- routing-policy

**Note**

- Legal string length is 1-255 characters.

- Illegal characters include any whitespace and the following special characters (separated by commas): #,!,',”,\

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)#


**Removing Configuration**

To remove the specified flowspec-local-policies rule:
::

    dnRouter(cfg-rpl)# no flowspec-local-policies

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## apply-policy-to-flowspec.rst

routing-policy flowspec-local-policies ipv4 apply-policy-to-flowspec
--------------------------------------------------------------------

**Minimum user role:** operator

Specifys which of the policies that were defined for IPv4, that should be installed - only one policy may be installed.

**Command syntax: apply-policy-to-flowspec [apply-to-flowspec-policy-name]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4

**Parameter table**

+-------------------------------+----------------------------------------------------------------------------------+--------+---------+
| Parameter                     | Description                                                                      | Range  | Default |
+-------------------------------+----------------------------------------------------------------------------------+--------+---------+
| apply-to-flowspec-policy-name | The name of ipv4 policy to install - only a single ipv4 policy may be installed. | string | \-      |
|                               |                                                                                  | length |         |
|                               |                                                                                  | 1..255 |         |
+-------------------------------+----------------------------------------------------------------------------------+--------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy-based-routing
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# apply-policy-to-flowspec policy-1
    dnRouter(cfg-rpl-flp-ipv4)#


**Removing Configuration**

To remove the policy that was installed.
::

    dnRouter(cfg-flp-ipv4-mc)# no apply-policy-to-flowspec policy-1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## ipv4.rst

routing-policy flowspec-local-policies ipv4
-------------------------------------------

**Minimum user role:** operator

Define the ipv4 address family MCs and rules:

**Command syntax: ipv4**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies

**Example**
::

    dnRouter#
    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)#


**Removing Configuration**

To remove the ipv4 configurations:
::

    dnRouter(cfg-rpl-flp)# no ipv4

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## description.rst

routing-policy flowspec-local-policies ipv4 match-class description
-------------------------------------------------------------------

**Minimum user role:** operator

To add an optional description for the match class:

**Command syntax: description [description]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 match-class

**Parameter table**

+-------------+------------------------------+------------------+---------+
| Parameter   | Description                  | Range            | Default |
+=============+==============================+==================+=========+
| description | ipv4 match class description | | string         | \-      |
|             |                              | | length 1-255   |         |
+-------------+------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)# description "The match class"
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To revert description to default:
::

    dnRouter(cfg-flp-ipv4-mc)# no description

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## dest-ip.rst

routing-policy flowspec-local-policies ipv4 match-class dest-ip
---------------------------------------------------------------

**Minimum user role:** operator

To configure the dest-ip as a match criteria of this match class. All criteria must match, for the match to be made.

**Command syntax: dest-ip [dest-ip]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 match-class

**Parameter table**

+-----------+---------------------------------+-----------+---------+
| Parameter | Description                     | Range     | Default |
+===========+=================================+===========+=========+
| dest-ip   | Destination IPv4 address prefix | A.B.C.D/x | \-      |
+-----------+---------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)# dest-ip 192.168.10.20
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To remove the dest-ip from the match class:
::

    dnRouter(cfg-flp-ipv4-mc)# no dest-ip

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## dest-port.rst

routing-policy flowspec-local-policies ipv4 match-class dest-ports
------------------------------------------------------------------

**Minimum user role:** operator

Configures the destination port as a specific match criteria of this match class. For the match to be made, all the criteria must match.

**Command syntax: dest-ports [dest-ports]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 match-class

**Parameter table**

+------------+--------------------------------------------------------------+---------+---------+
| Parameter  | Description                                                  | Range   | Default |
+============+==============================================================+=========+=========+
| dest-ports | Destination port range or a specific destination port value. | 0-65535 | \-      |
+------------+--------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)# dest-ports 200-250
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To remove the dest-ports from the match class:
::

    dnRouter(cfg-flp-ipv4-mc)# no dest-ports

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## dscp.rst

routing-policy flowspec-local-policies ipv4 match-class dscp
------------------------------------------------------------

**Minimum user role:** operator

Configures the dscp as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: dscp [dscp]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 match-class

**Parameter table**

+-----------+-------------------------------------+-------+---------+
| Parameter | Description                         | Range | Default |
+===========+=====================================+=======+=========+
| dscp      | Differentiated Services Code Point. | 0-63  | \-      |
+-----------+-------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)# dscp 45
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To remove the dscp from the match class:
::

    dnRouter(cfg-flp-ipv4-mc)# no dscp

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## fragmented.rst

routing-policy flowspec-local-policies ipv4 match-class fragmented
------------------------------------------------------------------

**Minimum user role:** operator

Configures the fragmented packets as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: fragmented**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 match-class

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)# fragmented
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To remove fragmented from the match class:
::

    dnRouter(cfg-flp-ipv4-mc)# no fragmented

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## icmp.rst

routing-policy flowspec-local-policies ipv4 match-class icmp
------------------------------------------------------------

**Minimum user role:** operator

Configures the icmp as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: icmp [message-type]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 match-class

**Parameter table**

+--------------+--------------------+-----------------------------------------------+---------+
| Parameter    | Description        | Range                                         | Default |
+==============+====================+===============================================+=========+
| message-type | icmp message type. | | echo-reply                                  | \-      |
|              |                    | | destination-network-unreachable             |         |
|              |                    | | destination-host-unreachable                |         |
|              |                    | | destination-protocol-unreachable            |         |
|              |                    | | destination-port-unreachable                |         |
|              |                    | | fragmentation-required                      |         |
|              |                    | | source-route-failed                         |         |
|              |                    | | destination-network-unknown                 |         |
|              |                    | | destination-host-unknown                    |         |
|              |                    | | source-host-isolated                        |         |
|              |                    | | network-administratively-prohibited         |         |
|              |                    | | host-administratively-prohibited            |         |
|              |                    | | network-unreachable-for-tos                 |         |
|              |                    | | host-unreachable-for-tos                    |         |
|              |                    | | communication-administratively-prohibited   |         |
|              |                    | | host-precedence-violation                   |         |
|              |                    | | precedence-cutoff-in-effect                 |         |
|              |                    | | redirect-network                            |         |
|              |                    | | redirect-host                               |         |
|              |                    | | redirect-tos-network                        |         |
|              |                    | | redirect-tos-host                           |         |
|              |                    | | echo-request                                |         |
|              |                    | | router-advertisement                        |         |
|              |                    | | router-solicitation                         |         |
|              |                    | | ttl-expired-in-transit                      |         |
|              |                    | | fragment-reassembly                         |         |
|              |                    | | pointer-indicates-error                     |         |
|              |                    | | missing-required-option                     |         |
|              |                    | | bad-length                                  |         |
|              |                    | | timestamp                                   |         |
|              |                    | | timestamp-reply                             |         |
+--------------+--------------------+-----------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)# icmp echo-reply
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To remove the icmp from the match class:
::

    dnRouter(cfg-flp-ipv4-mc)# no icmp

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## mc-defns.rst

routing-policy flowspec-local-policies ipv4 match-class
-------------------------------------------------------

**Minimum user role:** operator

To configure an ipv4 match class:

**Command syntax: match-class [mc-name]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4

**Note**

- Legal string length must be 1-255 characters.

- Illegal characters include any whitespaces and the following special characters (separated by commas): #,!,',”,\

**Parameter table**

+-----------+------------------+------------------+---------+
| Parameter | Description      | Range            | Default |
+===========+==================+==================+=========+
| mc-name   | match class name | | string         | \-      |
|           |                  | | length 1-255   |         |
+-----------+------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To remove the specified match class:
::

    dnRouter(cfg-rpl-flp-ipv4)# no match-class mc-1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## packet-length.rst

routing-policy flowspec-local-policies ipv4 match-class packet-length
---------------------------------------------------------------------

**Minimum user role:** operator

Configures the packet-length as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: packet-length [packet-length]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 match-class

**Parameter table**

+---------------+--------------------------------------------------------+---------+---------+
| Parameter     | Description                                            | Range   | Default |
+===============+========================================================+=========+=========+
| packet-length | Packet-length range or a specific packet length value. | 0-65535 | \-      |
+---------------+--------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)# packet-length 200-250
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To remove the packet-length from the match class:
::

    dnRouter(cfg-flp-ipv4-mc)# no packet-length

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## protocol.rst

routing-policy flowspec-local-policies ipv4 match-class protocol
----------------------------------------------------------------

**Minimum user role:** operator

Configures the protocol as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: protocol [protocol]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 match-class

**Parameter table**

+-----------+----------------------------------------------------------------------------------+--------------------------------------+---------+
| Parameter | Description                                                                      | Range                                | Default |
+===========+==================================================================================+======================================+=========+
| protocol  | Protocol that is passed on top of Network layer (i.e. on top of IPv4/IPv6        | | hopopt(0x00)                       | \-      |
|           | header)                                                                          | | icmp(0x01)                         |         |
|           |                                                                                  | | igmp(0x02)                         |         |
|           |                                                                                  | | ggp(0x03)                          |         |
|           |                                                                                  | | ip-in-ip(0x04)                     |         |
|           |                                                                                  | | St(0x05)                           |         |
|           |                                                                                  | | tcp(0x06)                          |         |
|           |                                                                                  | | cbt(0x07)                          |         |
|           |                                                                                  | | egp(0x08)                          |         |
|           |                                                                                  | | igp(0x09)                          |         |
|           |                                                                                  | | bbn-rcc-mon(0x0A)                  |         |
|           |                                                                                  | | nvp-ii(0x0B)                       |         |
|           |                                                                                  | | pup(0x0C)                          |         |
|           |                                                                                  | | argus(0x0D)                        |         |
|           |                                                                                  | | emcon(0x0E)                        |         |
|           |                                                                                  | | xnet(0x0F)                         |         |
|           |                                                                                  | | chaos(0x10)                        |         |
|           |                                                                                  | | udp(0x11)                          |         |
|           |                                                                                  | | mux(0x12)                          |         |
|           |                                                                                  | | dcn-meas(0x13)                     |         |
|           |                                                                                  | | hmp(0x14)                          |         |
|           |                                                                                  | | prm(0x15)                          |         |
|           |                                                                                  | | xns-idp(0x16)                      |         |
|           |                                                                                  | | trunk-1(0x17)                      |         |
|           |                                                                                  | | trunk-2(0x18)                      |         |
|           |                                                                                  | | leaf-1(0x19)                       |         |
|           |                                                                                  | | leaf-2(0x1A)                       |         |
|           |                                                                                  | | rdp(0x1B)                          |         |
|           |                                                                                  | | irtp(0x1C)                         |         |
|           |                                                                                  | | iso-tp4(0x1D)                      |         |
|           |                                                                                  | | netblt(0x1E)                       |         |
|           |                                                                                  | | mfe-nsp(0x1F)                      |         |
|           |                                                                                  | | merit-inp(0x20)                    |         |
|           |                                                                                  | | dccp(0x21)                         |         |
|           |                                                                                  | | 3pc(0x22)                          |         |
|           |                                                                                  | | idpr(0x23)                         |         |
|           |                                                                                  | | xtp(0x24)                          |         |
|           |                                                                                  | | ddp(0x25)                          |         |
|           |                                                                                  | | idpr-cmtp(0x26)                    |         |
|           |                                                                                  | | tp++(0x27)                         |         |
|           |                                                                                  | | il(0x28)                           |         |
|           |                                                                                  | | ipv6(0x29)                         |         |
|           |                                                                                  | | sdrp(0x2A)                         |         |
|           |                                                                                  | | ipv6-route(0x2B)                   |         |
|           |                                                                                  | | ipv6-frag(0x2C)                    |         |
|           |                                                                                  | | idrp(0x2D)                         |         |
|           |                                                                                  | | rsvp(0x2E)                         |         |
|           |                                                                                  | | gre(0x2F)                          |         |
|           |                                                                                  | | dsr(0x30)                          |         |
|           |                                                                                  | | bna(0x31)                          |         |
|           |                                                                                  | | esp(0x32)                          |         |
|           |                                                                                  | | ah(0x33)                           |         |
|           |                                                                                  | | i-nlsp(0x34)                       |         |
|           |                                                                                  | | swipe(0x35)                        |         |
|           |                                                                                  | | narp(0x36)                         |         |
|           |                                                                                  | | mobile(0x37)                       |         |
|           |                                                                                  | | tlsp(0x38)                         |         |
|           |                                                                                  | | skip(0x39)                         |         |
|           |                                                                                  | | ipv6-icmp(0x3A)                    |         |
|           |                                                                                  | | ipv6-nonxt(0x3B)                   |         |
|           |                                                                                  | | ipv6-opts(0x3C)                    |         |
|           |                                                                                  | | any-host(0x3D)                     |         |
|           |                                                                                  | | cftp(0x3E)                         |         |
|           |                                                                                  | | any-local-network(0x3F)            |         |
|           |                                                                                  | | sat-expak(0x40)                    |         |
|           |                                                                                  | | kryptolan(0x41)                    |         |
|           |                                                                                  | | rvd(0x42)                          |         |
|           |                                                                                  | | ippc(0x43)                         |         |
|           |                                                                                  | | any-dist-file-sys(0x44)            |         |
|           |                                                                                  | | sat-mon(0x45)                      |         |
|           |                                                                                  | | visa(0x46)                         |         |
|           |                                                                                  | | ipcu(0x47)                         |         |
|           |                                                                                  | | cpnx(0x48)                         |         |
|           |                                                                                  | | cphb(0x49)                         |         |
|           |                                                                                  | | wsn(0x4A)                          |         |
|           |                                                                                  | | pvp(0x4B)                          |         |
|           |                                                                                  | | br-sat-mon(0x4C)                   |         |
|           |                                                                                  | | sun-nd(0x4D)                       |         |
|           |                                                                                  | | wb-mon(0x4E)                       |         |
|           |                                                                                  | | wb-expak(0x4F)                     |         |
|           |                                                                                  | | iso-ip(0x50)                       |         |
|           |                                                                                  | | vmtp(0x51)                         |         |
|           |                                                                                  | | secure-vmtp(0x52)                  |         |
|           |                                                                                  | | vines(0x53)                        |         |
|           |                                                                                  | | ttp/iptm(0x54)                     |         |
|           |                                                                                  | | nsfnet-igp(0x55)                   |         |
|           |                                                                                  | | dgp(0x56)                          |         |
|           |                                                                                  | | tcf(0x57)                          |         |
|           |                                                                                  | | eigrp(0x58)                        |         |
|           |                                                                                  | | ospf(0x59)                         |         |
|           |                                                                                  | | sprite-rpc(0x5A)                   |         |
|           |                                                                                  | | larp(0x5B)                         |         |
|           |                                                                                  | | mtp(0x5C)                          |         |
|           |                                                                                  | | ax.25(0x5D)                        |         |
|           |                                                                                  | | os(0x5E)                           |         |
|           |                                                                                  | | micp(0x5F)                         |         |
|           |                                                                                  | | scc-sp(0x60)                       |         |
|           |                                                                                  | | etherip(0x61)                      |         |
|           |                                                                                  | | encap(0x62)                        |         |
|           |                                                                                  | | any-private-encrypt-scheme(0x63)   |         |
|           |                                                                                  | | gmtp(0x64)                         |         |
|           |                                                                                  | | ifmp(0x65)                         |         |
|           |                                                                                  | | pnni(0x66)                         |         |
|           |                                                                                  | | pim(0x67)                          |         |
|           |                                                                                  | | aris(0x68)                         |         |
|           |                                                                                  | | scps(0x69)                         |         |
|           |                                                                                  | | qnx(0x6A)                          |         |
|           |                                                                                  | | a/n(0x6B)                          |         |
|           |                                                                                  | | ipcomp(0x6C)                       |         |
|           |                                                                                  | | snp(0x6D)                          |         |
|           |                                                                                  | | compaq-peer(0x6E)                  |         |
|           |                                                                                  | | ipx-in-ip(0x6F)                    |         |
|           |                                                                                  | | vrrp(0x70)                         |         |
|           |                                                                                  | | pgm(0x71)                          |         |
|           |                                                                                  | | any-0-hop-protocol(0x72)           |         |
|           |                                                                                  | | l2tp(0x73)                         |         |
|           |                                                                                  | | ddx(0x74)                          |         |
|           |                                                                                  | | iatp(0x75)                         |         |
|           |                                                                                  | | stp(0x76)                          |         |
|           |                                                                                  | | srp(0x77)                          |         |
|           |                                                                                  | | uti(0x78)                          |         |
|           |                                                                                  | | smp(0x79)                          |         |
|           |                                                                                  | | sm(0x7A)                           |         |
|           |                                                                                  | | ptp(0x7B)                          |         |
|           |                                                                                  | | is-is-over-ipv4(0x7C)              |         |
|           |                                                                                  | | fire(0x7D)                         |         |
|           |                                                                                  | | crtp(0x7E)                         |         |
|           |                                                                                  | | crudp(0x7F)                        |         |
|           |                                                                                  | | sscopmce(0x80)                     |         |
|           |                                                                                  | | iplt(0x81)                         |         |
|           |                                                                                  | | sps(0x82)                          |         |
|           |                                                                                  | | pipe(0x83)                         |         |
|           |                                                                                  | | sctp(0x84)                         |         |
|           |                                                                                  | | fc(0x85)                           |         |
|           |                                                                                  | | rsvp-e2e-ignore(0x86)              |         |
|           |                                                                                  | | mobility-header(0x87)              |         |
|           |                                                                                  | | udplite(0x88)                      |         |
|           |                                                                                  | | mpls-in-ip(0x89)                   |         |
|           |                                                                                  | | manet(0x8A)                        |         |
|           |                                                                                  | | hip(0x8B)                          |         |
|           |                                                                                  | | shim6(0x8C)                        |         |
|           |                                                                                  | | wesp(0x8D)                         |         |
|           |                                                                                  | | rohc(0x8E)                         |         |
|           |                                                                                  | | 0x8F                               |         |
|           |                                                                                  | | 0x90                               |         |
|           |                                                                                  | | 0x91                               |         |
|           |                                                                                  | | 0x92                               |         |
|           |                                                                                  | | 0x93                               |         |
|           |                                                                                  | | 0x94                               |         |
|           |                                                                                  | | 0x95                               |         |
|           |                                                                                  | | 0x96                               |         |
|           |                                                                                  | | 0x97                               |         |
|           |                                                                                  | | 0x98                               |         |
|           |                                                                                  | | 0x99                               |         |
|           |                                                                                  | | 0xA0                               |         |
|           |                                                                                  | | 0xA1                               |         |
|           |                                                                                  | | 0xA2                               |         |
|           |                                                                                  | | 0xA3                               |         |
|           |                                                                                  | | 0xA4                               |         |
|           |                                                                                  | | 0xA5                               |         |
|           |                                                                                  | | 0xA6                               |         |
|           |                                                                                  | | 0xA7                               |         |
|           |                                                                                  | | 0xA8                               |         |
|           |                                                                                  | | 0xA9                               |         |
|           |                                                                                  | | 0xAA                               |         |
|           |                                                                                  | | 0xAB                               |         |
|           |                                                                                  | | 0xAC                               |         |
|           |                                                                                  | | 0xAD                               |         |
|           |                                                                                  | | 0xAE                               |         |
|           |                                                                                  | | 0xAF                               |         |
|           |                                                                                  | | 0xB0                               |         |
|           |                                                                                  | | 0xB1                               |         |
|           |                                                                                  | | 0xB2                               |         |
|           |                                                                                  | | 0xB3                               |         |
|           |                                                                                  | | 0xB4                               |         |
|           |                                                                                  | | 0xB5                               |         |
|           |                                                                                  | | 0xB6                               |         |
|           |                                                                                  | | 0xB7                               |         |
|           |                                                                                  | | 0xB8                               |         |
|           |                                                                                  | | 0xB9                               |         |
|           |                                                                                  | | 0xBA                               |         |
|           |                                                                                  | | 0xBB                               |         |
|           |                                                                                  | | 0xBC                               |         |
|           |                                                                                  | | 0xBE                               |         |
|           |                                                                                  | | 0xBF                               |         |
|           |                                                                                  | | 0xC0                               |         |
|           |                                                                                  | | 0xC1                               |         |
|           |                                                                                  | | 0xC2                               |         |
|           |                                                                                  | | 0xC3                               |         |
|           |                                                                                  | | 0xC4                               |         |
|           |                                                                                  | | 0xC5                               |         |
|           |                                                                                  | | 0xC6                               |         |
|           |                                                                                  | | 0xC7                               |         |
|           |                                                                                  | | 0xC8                               |         |
|           |                                                                                  | | 0xC9                               |         |
|           |                                                                                  | | 0xCA                               |         |
|           |                                                                                  | | 0xCB                               |         |
|           |                                                                                  | | 0xCC                               |         |
|           |                                                                                  | | 0xCD                               |         |
|           |                                                                                  | | 0xCE                               |         |
|           |                                                                                  | | 0xCF                               |         |
|           |                                                                                  | | 0xD0                               |         |
|           |                                                                                  | | 0xD1                               |         |
|           |                                                                                  | | 0xD2                               |         |
|           |                                                                                  | | 0xD3                               |         |
|           |                                                                                  | | 0xD4                               |         |
|           |                                                                                  | | 0xD5                               |         |
|           |                                                                                  | | 0xD6                               |         |
|           |                                                                                  | | 0xD7                               |         |
|           |                                                                                  | | 0xD8                               |         |
|           |                                                                                  | | 0xD9                               |         |
|           |                                                                                  | | 0xDA                               |         |
|           |                                                                                  | | 0xDB                               |         |
|           |                                                                                  | | 0xDC                               |         |
|           |                                                                                  | | 0xDD                               |         |
|           |                                                                                  | | 0xDE                               |         |
|           |                                                                                  | | 0xDF                               |         |
|           |                                                                                  | | 0xE0                               |         |
|           |                                                                                  | | 0xE1                               |         |
|           |                                                                                  | | 0xE2                               |         |
|           |                                                                                  | | 0xE3                               |         |
|           |                                                                                  | | 0xE4                               |         |
|           |                                                                                  | | 0xE5                               |         |
|           |                                                                                  | | 0xE6                               |         |
|           |                                                                                  | | 0xE7                               |         |
|           |                                                                                  | | 0xE8                               |         |
|           |                                                                                  | | 0xE9                               |         |
|           |                                                                                  | | 0xEA                               |         |
|           |                                                                                  | | 0xEB                               |         |
|           |                                                                                  | | 0xEC                               |         |
|           |                                                                                  | | 0xED                               |         |
|           |                                                                                  | | 0xEE                               |         |
|           |                                                                                  | | 0xEF                               |         |
|           |                                                                                  | | 0xF0                               |         |
|           |                                                                                  | | 0xF1                               |         |
|           |                                                                                  | | 0xF2                               |         |
|           |                                                                                  | | 0xF3                               |         |
|           |                                                                                  | | 0xF4                               |         |
|           |                                                                                  | | 0xF5                               |         |
|           |                                                                                  | | 0xF6                               |         |
|           |                                                                                  | | 0xF7                               |         |
|           |                                                                                  | | 0xF8                               |         |
|           |                                                                                  | | 0xF9                               |         |
|           |                                                                                  | | 0xFA                               |         |
|           |                                                                                  | | 0xFB                               |         |
|           |                                                                                  | | 0xFC                               |         |
|           |                                                                                  | | 0xFD                               |         |
|           |                                                                                  | | 0xFE                               |         |
|           |                                                                                  | | 0xFF                               |         |
|           |                                                                                  | | any                                |         |
+-----------+----------------------------------------------------------------------------------+--------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)# protocol tcp(0x06)
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To remove the protocol from the match class:
::

    dnRouter(cfg-flp-ipv4-mc)# no protocol

**Command History**

+---------+-----------------------------+
| Release | Modification                |
+=========+=============================+
| 17.0    | Command introduced          |
+---------+-----------------------------+
| 17.2    | Added 'any' protocol option |
+---------+-----------------------------+

---

## source-ip.rst

routing-policy flowspec-local-policies ipv4 match-class src-ip
--------------------------------------------------------------

**Minimum user role:** operator

Configures the src-ip as a match criteria of this traffic class. For the match to be made, all criteria must match.

**Command syntax: src-ip [src-ip]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 match-class

**Parameter table**

+-----------+----------------------------+-----------+---------+
| Parameter | Description                | Range     | Default |
+===========+============================+===========+=========+
| src-ip    | Source IPv4 address prefix | A.B.C.D/x | \-      |
+-----------+----------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)# src-ip 192.168.10.20
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To remove the src-ip from the match class:
::

    dnRouter(cfg-flp-ipv4-mc)# no src-ip

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## src-port.rst

routing-policy flowspec-local-policies ipv4 match-class src-ports
-----------------------------------------------------------------

**Minimum user role:** operator

Configures the src-ip as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: src-ports [src-ports]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 match-class

**Parameter table**

+-----------+----------------------------------------------------+---------+---------+
| Parameter | Description                                        | Range   | Default |
+===========+====================================================+=========+=========+
| src-ports | Source port range or a specific source port value. | 0-65535 | \-      |
+-----------+----------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)# src-ports 200-250
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To remove the src-ports from the match class:
::

    dnRouter(cfg-flp-ipv4-mc)# no src-ports

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## tcp-flag.rst

routing-policy flowspec-local-policies ipv4 match-class tcp-flag
----------------------------------------------------------------

**Minimum user role:** operator

To add an optional description for the match class:

**Command syntax: tcp-flag [tcp-flag]** [, tcp-flag, tcp-flag]

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 match-class

**Parameter table**

+-----------+----------------+---------+---------+
| Parameter | Description    | Range   | Default |
+===========+================+=========+=========+
| tcp-flag  | TCP flags list | | syn   | \-      |
|           |                | | ack   |         |
|           |                | | urg   |         |
|           |                | | psh   |         |
|           |                | | rst   |         |
|           |                | | fin   |         |
+-----------+----------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# match-class mc-1
    dnRouter(cfg-flp-ipv4-mc)# tcp-flag syn,ack
    dnRouter(cfg-flp-ipv4-mc)#


**Removing Configuration**

To remove the tcp-flag from the match-class:
::

    dnRouter(cfg-flp-ipv4-mc)# no tcp-flag

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## description.rst

routing-policy flowspec-local-policies ipv4 policy description
--------------------------------------------------------------

**Minimum user role:** operator

To add an optional description for the policy.

**Command syntax: description [description]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 policy

**Parameter table**

+-------------+-------------------------+------------------+---------+
| Parameter   | Description             | Range            | Default |
+=============+=========================+==================+=========+
| description | ipv4 policy description | | string         | \-      |
|             |                         | | length 1-255   |         |
+-------------+-------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# policy policy-1
    dnRouter(cfg-flp-ipv4-pl)# description "The policy"
    dnRouter(cfg-flp-ipv4-pl)#


**Removing Configuration**

To revert the description to default:
::

    dnRouter(cfg-flp-ipv4-pl)# no description

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## action_rate_limit.rst

routing-policy flowspec-local-policies ipv4 policy match-class action rate-limit
--------------------------------------------------------------------------------

**Minimum user role:** operator

When matchimg to this match-class, configures that the traffic shall be rate-limited.

**Command syntax: action rate-limit [rate-limit]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 policy match-class

**Parameter table**

+------------+------------------------------------------------------+------------------+---------+
| Parameter  | Description                                          | Range            | Default |
+============+======================================================+==================+=========+
| rate-limit | The rate in kbits per second to limit the traffic to | 0, 64-4294967295 | \-      |
+------------+------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# policy policy-1
    dnRouter(cfg-flp-ipv4-pl)# match-class mc-1
    dnRouter(cfg-ipv4-pl-mc)#  action rate-limit 0
    dnRouter(cfg-ipv4-pl-mc)# exit
    dnRouter(cfg-flp-ipv4-pl)


**Removing Configuration**

To remove the action from the policy:
::

    dnRouter(cfg-ipv4-pl-mc)# no action rate-limit

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## action_redirect-to-vrf.rst

routing-policy flowspec-local-policies ipv4 policy match-class action redirect-to-vrf
-------------------------------------------------------------------------------------

**Minimum user role:** operator

Configures the action of a redirect to another vrf when matching to this match-class.

**Command syntax: action redirect-to-vrf [redirected-to-vrf]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 policy match-class

**Parameter table**

+-------------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter         | Description                                                                      | Range            | Default |
+===================+==================================================================================+==================+=========+
| redirected-to-vrf | redirect-to-vrf target is a reference to another vrf - the next hop should be    | | string         | \-      |
|                   | taken from that vrf                                                              | | length 1-255   |         |
+-------------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# policy policy-1
    dnRouter(cfg-flp-ipv4-pl)# match-class mc-1
    dnRouter(cfg-ipv4-pl-mc)#  action redirect-to-vrf vrf-1
    dnRouter(cfg-ipv4-pl-mc)# exit
    dnRouter(cfg-flp-ipv4-pl)


**Removing Configuration**

To remove the action from the policy:
::

    dnRouter(cfg-ipv4-pl-mc)# no action redirect-to-vrf

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## action.rst

routing-policy flowspec-local-policies ipv4 policy match-class action-type
--------------------------------------------------------------------------

**Minimum user role:** operator

Configure the packet-length as a match criteria of this match class. All criteria must match, for the match to be made.

**Command syntax: action-type [action-type]** vrf [vrf] max-rate [rate-limit]

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 policy match-class

**Parameter table**

+-------------+----------------------------------------------------------------------------------+----------------------------------+---------+
| Parameter   | Description                                                                      | Range                            | Default |
+=============+==================================================================================+==================================+=========+
| action-type | The action to be performed on match of the traffic class.                        | no-action                        | \-      |
|             |                                                                                  | rate-limit                       |         |
|             |                                                                                  | redirect-to-vrf                  |         |
|             |                                                                                  | redirect-to-vrf-and-rate-limit   |         |
+-------------+----------------------------------------------------------------------------------+----------------------------------+---------+
| vrf         | redirect-to target is a reference to another vrf - the next hop should be taken  | string                           | \-      |
|             | from that vrf.                                                                   | length 1..255                    |         |
+-------------+----------------------------------------------------------------------------------+----------------------------------+---------+
| rate-limit  | The rate in kbits per second to limit the traffic to.                            | 0..4294967295                    | \-      |
+-------------+----------------------------------------------------------------------------------+----------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# policy policy-1
    dnRouter(cfg-flp-ipv4-pl)# match-class mc-1
    dnRouter(cfg-ipv4-pl-mc)#  action-type rate-limit max-rate 0
    dnRouter(cfg-ipv4-pl-mc)# exit
    dnRouter(cfg-flp-ipv4-pl)


**Removing Configuration**

To remove the action from the policy
::

    dnRouter(cfg-ipv4-pl-mc)# no action-type

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## match-class.rst

routing-policy flowspec-local-policies ipv4 policy match-class
--------------------------------------------------------------

**Minimum user role:** operator

To assign an ipv4 match class to the policy:

**Command syntax: match-class [mc-name]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4 policy

**Note**

- Legal string length is 1-255 characters.

- Illegal characters include any whitespace and the following special characters (separated by commas): #,!,',”,\

**Parameter table**

+-----------+------------------+------------------+---------+
| Parameter | Description      | Range            | Default |
+===========+==================+==================+=========+
| mc-name   | match class name | | string         | \-      |
|           |                  | | length 1-255   |         |
+-----------+------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# policy policy-1
    dnRouter(cfg-flp-ipv4-pl)# match-class mc-1
    dnRouter(cfg-ipv4-pl-mc)#


**Removing Configuration**

To remove the specified match class:
::

    dnRouter(cfg-flp-ipv4-pl)# no match-class mc-1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## policy.rst

routing-policy flowspec-local-policies ipv4 policy
--------------------------------------------------

**Minimum user role:** operator

To configure an ipv4 policy:

**Command syntax: policy [policy-name]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv4

**Note**

- Legal string length is 1-255 characters.

- Illegal characters include any whitespace and the following special characters (separated by commas): #,!,',”,\

**Parameter table**

+-------------+-------------+------------------+---------+
| Parameter   | Description | Range            | Default |
+=============+=============+==================+=========+
| policy-name | policy name | | string         | \-      |
|             |             | | length 1-255   |         |
+-------------+-------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv4
    dnRouter(cfg-rpl-flp-ipv4)# policy policy-1
    dnRouter(cfg-flp-ipv4-pl)#


**Removing Configuration**

To remove the specified policy:
::

    dnRouter(cfg-rpl-flp-ipv4)# no policy policy-1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## apply-policy-to-flowspec.rst

routing-policy flowspec-local-policies ipv6 apply-policy-to-flowspec
--------------------------------------------------------------------

**Minimum user role:** operator

Specifys which of the policies that were defined for IPv6, that should be installed - only one policy may be installed.

**Command syntax: apply-policy-to-flowspec [apply-to-flowspec-policy-name]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6

**Parameter table**

+-------------------------------+----------------------------------------------------------------------------------+--------+---------+
| Parameter                     | Description                                                                      | Range  | Default |
+-------------------------------+----------------------------------------------------------------------------------+--------+---------+
| apply-to-flowspec-policy-name | The name of ipv6 policy to install - only a single ipv6 policy may be installed. | string | \-      |
|                               |                                                                                  | length |         |
|                               |                                                                                  | 1..255 |         |
+-------------------------------+----------------------------------------------------------------------------------+--------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# apply-policy-to-flowspec policy-1
    dnRouter(cfg-rpl-flp-ipv6)#


**Removing Configuration**

To remove the policy that was installed.
::

    dnRouter(cfg-rpl-flp-ipv6)# no apply-policy-to-flowspec policy-1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## ipv6.rst

routing-policy flowspec-local-policies ipv6
-------------------------------------------

**Minimum user role:** operator

Defines the ipv6 address family MCs and rules.

**Command syntax: ipv6**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies

**Example**
::

    dnRouter#
    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)#


**Removing Configuration**

To remove the ipv6 configurations:
::

    dnRouter(cfg-rpl-flp)# no ipv6

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## description.rst

routing-policy flowspec-local-policies ipv6 match-class description
-------------------------------------------------------------------

**Minimum user role:** operator

To add an optional description for the match class:

**Command syntax: description [description]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 match-class

**Parameter table**

+-------------+------------------------------+------------------+---------+
| Parameter   | Description                  | Range            | Default |
+=============+==============================+==================+=========+
| description | ipv6 match class description | | string         | \-      |
|             |                              | | length 1-255   |         |
+-------------+------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class tc-1
    dnRouter(cfg-flp-ipv6-mc)# description "The match class"
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To revert description to default:
::

    dnRouter(cfg-flp-ipv6-mc)# no description

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## dest-ip.rst

routing-policy flowspec-local-policies ipv6 match-class dest-ip
---------------------------------------------------------------

**Minimum user role:** operator

Configures the dest-ip as a match criteria of this match class. For the match to be made, all the criteria must match.

**Command syntax: dest-ip [dest-ip]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 match-class

**Parameter table**

+-----------+---------------------------------+------------+---------+
| Parameter | Description                     | Range      | Default |
+===========+=================================+============+=========+
| dest-ip   | Destination IPv6 address prefix | X:X::X:X/x | \-      |
+-----------+---------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class mc-1
    dnRouter(cfg-flp-ipv6-mc)# dest-ip 1050::5:620:510c:357c
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To remove the dest-ip from the match class:
::

    dnRouter(cfg-flp-ipv6-mc)# no dest-ip

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## dest-port.rst

routing-policy flowspec-local-policies ipv6 match-class dest-ports
------------------------------------------------------------------

**Minimum user role:** operator

Configures the destination port as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: dest-ports [dest-ports]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 match-class

**Parameter table**

+------------+--------------------------------------------------------------+---------+---------+
| Parameter  | Description                                                  | Range   | Default |
+============+==============================================================+=========+=========+
| dest-ports | Destination port range or a specific destination port value. | 0-65535 | \-      |
+------------+--------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class mc-1
    dnRouter(cfg-flp-ipv6-mc)# dest-ports 200-250
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To remove the dest-ports from the match class:
::

    dnRouter(cfg-flp-ipv6-mc)# no dest-ports

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## fragmented.rst

routing-policy flowspec-local-policies ipv6 match-class fragmented
------------------------------------------------------------------

**Minimum user role:** operator

Configures the fragmented packets as a match criteria of this match class. For the match to be made, all the criteria must match.

**Command syntax: fragmented**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 match-class

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class mc-1
    dnRouter(cfg-flp-ipv6-mc)# fragmented
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To remove fragmented from the match class:
::

    dnRouter(cfg-flp-ipv6-mc)# no fragmented

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## icmp.rst

routing-policy flowspec-local-policies ipv6 match-class icmp
------------------------------------------------------------

**Minimum user role:** operator

Configures the icmp as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: icmp [message-type]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 match-class

**Parameter table**

+--------------+-------------------------+-------------------------------------------------+---------+
| Parameter    | Description             | Range                                           | Default |
+==============+=========================+=================================================+=========+
| message-type | ipv6-icmp message type. | | no-route-to-destination                       | \-      |
|              |                         | | administratively-prohibited                   |         |
|              |                         | | beyond-scope-of-source-address                |         |
|              |                         | | address-unreachable                           |         |
|              |                         | | port-unreachable                              |         |
|              |                         | | source-address-failed-ingress/egress-policy   |         |
|              |                         | | reject-route-to-destination                   |         |
|              |                         | | error-in-source-routing-header                |         |
|              |                         | | packet-too-big                                |         |
|              |                         | | hop-limit-exceeded-in-transit                 |         |
|              |                         | | fragment-reassembly-time-exceeded             |         |
|              |                         | | erroneous-header-field-encountered            |         |
|              |                         | | unrecognized-next-header-type-encountered     |         |
|              |                         | | unrecognized-ipv6-option-encountered          |         |
|              |                         | | echo-request                                  |         |
|              |                         | | echo-reply                                    |         |
|              |                         | | multicast-listener-query                      |         |
|              |                         | | multicast-listener-report                     |         |
|              |                         | | multicast-listener-done                       |         |
|              |                         | | router-solicitation                           |         |
|              |                         | | router-advertisement                          |         |
|              |                         | | neighbor-solicitation                         |         |
|              |                         | | neighbor-advertisement                        |         |
|              |                         | | redirect-message                              |         |
|              |                         | | renumbering-command                           |         |
|              |                         | | renumbering-result                            |         |
|              |                         | | renumbering-sequence-number-reset             |         |
|              |                         | | query-ipv6-address                            |         |
|              |                         | | query-name                                    |         |
|              |                         | | query-ipv4-address                            |         |
|              |                         | | response-successful                           |         |
|              |                         | | response-refuse                               |         |
|              |                         | | response-unknown                              |         |
|              |                         | | solicitation-message                          |         |
|              |                         | | advertisement-message                         |         |
|              |                         | | mldv2-reports                                 |         |
|              |                         | | discovery-request-message                     |         |
|              |                         | | discovery-reply-message                       |         |
|              |                         | | mobile-prefix-solicitation                    |         |
|              |                         | | mobile-prefix-advertisement                   |         |
|              |                         | | certification-path-solicitation               |         |
|              |                         | | certification-path-advertisement              |         |
|              |                         | | mrd-advertisement                             |         |
|              |                         | | mrd-solicitation                              |         |
|              |                         | | mrd-termination                               |         |
|              |                         | | rpl-control-message                           |         |
+--------------+-------------------------+-------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class mc-1
    dnRouter(cfg-flp-ipv6-mc)# icmp echo-reply
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To remove the icmp from the match class:
::

    dnRouter(cfg-flp-ipv6-mc)# no icmp

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## mc-defns.rst

routing-policy flowspec-local-policies ipv6 match-class
-------------------------------------------------------

**Minimum user role:** operator

To configure an ipv6 match class:

**Command syntax: match-class [mc-name]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6

**Note**

- Legal string length must be 1-255 characters.

- Illegal characters include any whitespaces and the following special characters (separated by commas): #,!,',”,\

**Parameter table**

+-----------+------------------+------------------+---------+
| Parameter | Description      | Range            | Default |
+===========+==================+==================+=========+
| mc-name   | match class name | | string         | \-      |
|           |                  | | length 1-255   |         |
+-----------+------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class mc-1
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To remove the specified match class:
::

    dnRouter(cfg-rpl-flp-ipv6)# no match-class mc-1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## packet-length.rst

routing-policy flowspec-local-policies ipv6 match-class packet-length
---------------------------------------------------------------------

**Minimum user role:** operator

Configures the packet-length as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: packet-length [packet-length]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 match-class

**Parameter table**

+---------------+--------------------------------------------------------+---------+---------+
| Parameter     | Description                                            | Range   | Default |
+===============+========================================================+=========+=========+
| packet-length | Packet-length range or a specific packet length value. | 0-65535 | \-      |
+---------------+--------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class mc-1
    dnRouter(cfg-flp-ipv6-mc)# packet-length 2000-2500
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To remove the packet-length from the match class:
::

    dnRouter(cfg-flp-ipv6-mc)# no packet-length

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## protocol.rst

routing-policy flowspec-local-policies ipv6 match-class protocol
----------------------------------------------------------------

**Minimum user role:** operator

Configures the protocol as a match criteria of this match class. For the match to be made. all criteria must match.

**Command syntax: protocol [protocol]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 match-class

**Parameter table**

+-----------+----------------------------------------------------------------------------------+--------------------------------------+---------+
| Parameter | Description                                                                      | Range                                | Default |
+===========+==================================================================================+======================================+=========+
| protocol  | Protocol that is passed on top of Network layer (i.e. on top of IPv4/IPv6        | | hopopt(0x00)                       | \-      |
|           | header)                                                                          | | icmp(0x01)                         |         |
|           |                                                                                  | | igmp(0x02)                         |         |
|           |                                                                                  | | ggp(0x03)                          |         |
|           |                                                                                  | | ip-in-ip(0x04)                     |         |
|           |                                                                                  | | St(0x05)                           |         |
|           |                                                                                  | | tcp(0x06)                          |         |
|           |                                                                                  | | cbt(0x07)                          |         |
|           |                                                                                  | | egp(0x08)                          |         |
|           |                                                                                  | | igp(0x09)                          |         |
|           |                                                                                  | | bbn-rcc-mon(0x0A)                  |         |
|           |                                                                                  | | nvp-ii(0x0B)                       |         |
|           |                                                                                  | | pup(0x0C)                          |         |
|           |                                                                                  | | argus(0x0D)                        |         |
|           |                                                                                  | | emcon(0x0E)                        |         |
|           |                                                                                  | | xnet(0x0F)                         |         |
|           |                                                                                  | | chaos(0x10)                        |         |
|           |                                                                                  | | udp(0x11)                          |         |
|           |                                                                                  | | mux(0x12)                          |         |
|           |                                                                                  | | dcn-meas(0x13)                     |         |
|           |                                                                                  | | hmp(0x14)                          |         |
|           |                                                                                  | | prm(0x15)                          |         |
|           |                                                                                  | | xns-idp(0x16)                      |         |
|           |                                                                                  | | trunk-1(0x17)                      |         |
|           |                                                                                  | | trunk-2(0x18)                      |         |
|           |                                                                                  | | leaf-1(0x19)                       |         |
|           |                                                                                  | | leaf-2(0x1A)                       |         |
|           |                                                                                  | | rdp(0x1B)                          |         |
|           |                                                                                  | | irtp(0x1C)                         |         |
|           |                                                                                  | | iso-tp4(0x1D)                      |         |
|           |                                                                                  | | netblt(0x1E)                       |         |
|           |                                                                                  | | mfe-nsp(0x1F)                      |         |
|           |                                                                                  | | merit-inp(0x20)                    |         |
|           |                                                                                  | | dccp(0x21)                         |         |
|           |                                                                                  | | 3pc(0x22)                          |         |
|           |                                                                                  | | idpr(0x23)                         |         |
|           |                                                                                  | | xtp(0x24)                          |         |
|           |                                                                                  | | ddp(0x25)                          |         |
|           |                                                                                  | | idpr-cmtp(0x26)                    |         |
|           |                                                                                  | | tp++(0x27)                         |         |
|           |                                                                                  | | il(0x28)                           |         |
|           |                                                                                  | | ipv6(0x29)                         |         |
|           |                                                                                  | | sdrp(0x2A)                         |         |
|           |                                                                                  | | ipv6-route(0x2B)                   |         |
|           |                                                                                  | | ipv6-frag(0x2C)                    |         |
|           |                                                                                  | | idrp(0x2D)                         |         |
|           |                                                                                  | | rsvp(0x2E)                         |         |
|           |                                                                                  | | gre(0x2F)                          |         |
|           |                                                                                  | | dsr(0x30)                          |         |
|           |                                                                                  | | bna(0x31)                          |         |
|           |                                                                                  | | esp(0x32)                          |         |
|           |                                                                                  | | ah(0x33)                           |         |
|           |                                                                                  | | i-nlsp(0x34)                       |         |
|           |                                                                                  | | swipe(0x35)                        |         |
|           |                                                                                  | | narp(0x36)                         |         |
|           |                                                                                  | | mobile(0x37)                       |         |
|           |                                                                                  | | tlsp(0x38)                         |         |
|           |                                                                                  | | skip(0x39)                         |         |
|           |                                                                                  | | ipv6-icmp(0x3A)                    |         |
|           |                                                                                  | | ipv6-nonxt(0x3B)                   |         |
|           |                                                                                  | | ipv6-opts(0x3C)                    |         |
|           |                                                                                  | | any-host(0x3D)                     |         |
|           |                                                                                  | | cftp(0x3E)                         |         |
|           |                                                                                  | | any-local-network(0x3F)            |         |
|           |                                                                                  | | sat-expak(0x40)                    |         |
|           |                                                                                  | | kryptolan(0x41)                    |         |
|           |                                                                                  | | rvd(0x42)                          |         |
|           |                                                                                  | | ippc(0x43)                         |         |
|           |                                                                                  | | any-dist-file-sys(0x44)            |         |
|           |                                                                                  | | sat-mon(0x45)                      |         |
|           |                                                                                  | | visa(0x46)                         |         |
|           |                                                                                  | | ipcu(0x47)                         |         |
|           |                                                                                  | | cpnx(0x48)                         |         |
|           |                                                                                  | | cphb(0x49)                         |         |
|           |                                                                                  | | wsn(0x4A)                          |         |
|           |                                                                                  | | pvp(0x4B)                          |         |
|           |                                                                                  | | br-sat-mon(0x4C)                   |         |
|           |                                                                                  | | sun-nd(0x4D)                       |         |
|           |                                                                                  | | wb-mon(0x4E)                       |         |
|           |                                                                                  | | wb-expak(0x4F)                     |         |
|           |                                                                                  | | iso-ip(0x50)                       |         |
|           |                                                                                  | | vmtp(0x51)                         |         |
|           |                                                                                  | | secure-vmtp(0x52)                  |         |
|           |                                                                                  | | vines(0x53)                        |         |
|           |                                                                                  | | ttp/iptm(0x54)                     |         |
|           |                                                                                  | | nsfnet-igp(0x55)                   |         |
|           |                                                                                  | | dgp(0x56)                          |         |
|           |                                                                                  | | tcf(0x57)                          |         |
|           |                                                                                  | | eigrp(0x58)                        |         |
|           |                                                                                  | | ospf(0x59)                         |         |
|           |                                                                                  | | sprite-rpc(0x5A)                   |         |
|           |                                                                                  | | larp(0x5B)                         |         |
|           |                                                                                  | | mtp(0x5C)                          |         |
|           |                                                                                  | | ax.25(0x5D)                        |         |
|           |                                                                                  | | os(0x5E)                           |         |
|           |                                                                                  | | micp(0x5F)                         |         |
|           |                                                                                  | | scc-sp(0x60)                       |         |
|           |                                                                                  | | etherip(0x61)                      |         |
|           |                                                                                  | | encap(0x62)                        |         |
|           |                                                                                  | | any-private-encrypt-scheme(0x63)   |         |
|           |                                                                                  | | gmtp(0x64)                         |         |
|           |                                                                                  | | ifmp(0x65)                         |         |
|           |                                                                                  | | pnni(0x66)                         |         |
|           |                                                                                  | | pim(0x67)                          |         |
|           |                                                                                  | | aris(0x68)                         |         |
|           |                                                                                  | | scps(0x69)                         |         |
|           |                                                                                  | | qnx(0x6A)                          |         |
|           |                                                                                  | | a/n(0x6B)                          |         |
|           |                                                                                  | | ipcomp(0x6C)                       |         |
|           |                                                                                  | | snp(0x6D)                          |         |
|           |                                                                                  | | compaq-peer(0x6E)                  |         |
|           |                                                                                  | | ipx-in-ip(0x6F)                    |         |
|           |                                                                                  | | vrrp(0x70)                         |         |
|           |                                                                                  | | pgm(0x71)                          |         |
|           |                                                                                  | | any-0-hop-protocol(0x72)           |         |
|           |                                                                                  | | l2tp(0x73)                         |         |
|           |                                                                                  | | ddx(0x74)                          |         |
|           |                                                                                  | | iatp(0x75)                         |         |
|           |                                                                                  | | stp(0x76)                          |         |
|           |                                                                                  | | srp(0x77)                          |         |
|           |                                                                                  | | uti(0x78)                          |         |
|           |                                                                                  | | smp(0x79)                          |         |
|           |                                                                                  | | sm(0x7A)                           |         |
|           |                                                                                  | | ptp(0x7B)                          |         |
|           |                                                                                  | | is-is-over-ipv4(0x7C)              |         |
|           |                                                                                  | | fire(0x7D)                         |         |
|           |                                                                                  | | crtp(0x7E)                         |         |
|           |                                                                                  | | crudp(0x7F)                        |         |
|           |                                                                                  | | sscopmce(0x80)                     |         |
|           |                                                                                  | | iplt(0x81)                         |         |
|           |                                                                                  | | sps(0x82)                          |         |
|           |                                                                                  | | pipe(0x83)                         |         |
|           |                                                                                  | | sctp(0x84)                         |         |
|           |                                                                                  | | fc(0x85)                           |         |
|           |                                                                                  | | rsvp-e2e-ignore(0x86)              |         |
|           |                                                                                  | | mobility-header(0x87)              |         |
|           |                                                                                  | | udplite(0x88)                      |         |
|           |                                                                                  | | mpls-in-ip(0x89)                   |         |
|           |                                                                                  | | manet(0x8A)                        |         |
|           |                                                                                  | | hip(0x8B)                          |         |
|           |                                                                                  | | shim6(0x8C)                        |         |
|           |                                                                                  | | wesp(0x8D)                         |         |
|           |                                                                                  | | rohc(0x8E)                         |         |
|           |                                                                                  | | 0x8F                               |         |
|           |                                                                                  | | 0x90                               |         |
|           |                                                                                  | | 0x91                               |         |
|           |                                                                                  | | 0x92                               |         |
|           |                                                                                  | | 0x93                               |         |
|           |                                                                                  | | 0x94                               |         |
|           |                                                                                  | | 0x95                               |         |
|           |                                                                                  | | 0x96                               |         |
|           |                                                                                  | | 0x97                               |         |
|           |                                                                                  | | 0x98                               |         |
|           |                                                                                  | | 0x99                               |         |
|           |                                                                                  | | 0xA0                               |         |
|           |                                                                                  | | 0xA1                               |         |
|           |                                                                                  | | 0xA2                               |         |
|           |                                                                                  | | 0xA3                               |         |
|           |                                                                                  | | 0xA4                               |         |
|           |                                                                                  | | 0xA5                               |         |
|           |                                                                                  | | 0xA6                               |         |
|           |                                                                                  | | 0xA7                               |         |
|           |                                                                                  | | 0xA8                               |         |
|           |                                                                                  | | 0xA9                               |         |
|           |                                                                                  | | 0xAA                               |         |
|           |                                                                                  | | 0xAB                               |         |
|           |                                                                                  | | 0xAC                               |         |
|           |                                                                                  | | 0xAD                               |         |
|           |                                                                                  | | 0xAE                               |         |
|           |                                                                                  | | 0xAF                               |         |
|           |                                                                                  | | 0xB0                               |         |
|           |                                                                                  | | 0xB1                               |         |
|           |                                                                                  | | 0xB2                               |         |
|           |                                                                                  | | 0xB3                               |         |
|           |                                                                                  | | 0xB4                               |         |
|           |                                                                                  | | 0xB5                               |         |
|           |                                                                                  | | 0xB6                               |         |
|           |                                                                                  | | 0xB7                               |         |
|           |                                                                                  | | 0xB8                               |         |
|           |                                                                                  | | 0xB9                               |         |
|           |                                                                                  | | 0xBA                               |         |
|           |                                                                                  | | 0xBB                               |         |
|           |                                                                                  | | 0xBC                               |         |
|           |                                                                                  | | 0xBE                               |         |
|           |                                                                                  | | 0xBF                               |         |
|           |                                                                                  | | 0xC0                               |         |
|           |                                                                                  | | 0xC1                               |         |
|           |                                                                                  | | 0xC2                               |         |
|           |                                                                                  | | 0xC3                               |         |
|           |                                                                                  | | 0xC4                               |         |
|           |                                                                                  | | 0xC5                               |         |
|           |                                                                                  | | 0xC6                               |         |
|           |                                                                                  | | 0xC7                               |         |
|           |                                                                                  | | 0xC8                               |         |
|           |                                                                                  | | 0xC9                               |         |
|           |                                                                                  | | 0xCA                               |         |
|           |                                                                                  | | 0xCB                               |         |
|           |                                                                                  | | 0xCC                               |         |
|           |                                                                                  | | 0xCD                               |         |
|           |                                                                                  | | 0xCE                               |         |
|           |                                                                                  | | 0xCF                               |         |
|           |                                                                                  | | 0xD0                               |         |
|           |                                                                                  | | 0xD1                               |         |
|           |                                                                                  | | 0xD2                               |         |
|           |                                                                                  | | 0xD3                               |         |
|           |                                                                                  | | 0xD4                               |         |
|           |                                                                                  | | 0xD5                               |         |
|           |                                                                                  | | 0xD6                               |         |
|           |                                                                                  | | 0xD7                               |         |
|           |                                                                                  | | 0xD8                               |         |
|           |                                                                                  | | 0xD9                               |         |
|           |                                                                                  | | 0xDA                               |         |
|           |                                                                                  | | 0xDB                               |         |
|           |                                                                                  | | 0xDC                               |         |
|           |                                                                                  | | 0xDD                               |         |
|           |                                                                                  | | 0xDE                               |         |
|           |                                                                                  | | 0xDF                               |         |
|           |                                                                                  | | 0xE0                               |         |
|           |                                                                                  | | 0xE1                               |         |
|           |                                                                                  | | 0xE2                               |         |
|           |                                                                                  | | 0xE3                               |         |
|           |                                                                                  | | 0xE4                               |         |
|           |                                                                                  | | 0xE5                               |         |
|           |                                                                                  | | 0xE6                               |         |
|           |                                                                                  | | 0xE7                               |         |
|           |                                                                                  | | 0xE8                               |         |
|           |                                                                                  | | 0xE9                               |         |
|           |                                                                                  | | 0xEA                               |         |
|           |                                                                                  | | 0xEB                               |         |
|           |                                                                                  | | 0xEC                               |         |
|           |                                                                                  | | 0xED                               |         |
|           |                                                                                  | | 0xEE                               |         |
|           |                                                                                  | | 0xEF                               |         |
|           |                                                                                  | | 0xF0                               |         |
|           |                                                                                  | | 0xF1                               |         |
|           |                                                                                  | | 0xF2                               |         |
|           |                                                                                  | | 0xF3                               |         |
|           |                                                                                  | | 0xF4                               |         |
|           |                                                                                  | | 0xF5                               |         |
|           |                                                                                  | | 0xF6                               |         |
|           |                                                                                  | | 0xF7                               |         |
|           |                                                                                  | | 0xF8                               |         |
|           |                                                                                  | | 0xF9                               |         |
|           |                                                                                  | | 0xFA                               |         |
|           |                                                                                  | | 0xFB                               |         |
|           |                                                                                  | | 0xFC                               |         |
|           |                                                                                  | | 0xFD                               |         |
|           |                                                                                  | | 0xFE                               |         |
|           |                                                                                  | | 0xFF                               |         |
|           |                                                                                  | | any                                |         |
+-----------+----------------------------------------------------------------------------------+--------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class mc-1
    dnRouter(cfg-flp-ipv6-mc)# protocol tcp(0x06)
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To remove the protocol from the match class:
::

    dnRouter(cfg-flp-ipv6-mc)# no protocol

**Command History**

+---------+-----------------------------+
| Release | Modification                |
+=========+=============================+
| 17.0    | Command introduced          |
+---------+-----------------------------+
| 17.2    | Added 'any' protocol option |
+---------+-----------------------------+

---

## source-ip.rst

routing-policy flowspec-local-policies ipv6 match-class src-ip
--------------------------------------------------------------

**Minimum user role:** operator

Configures the src-ip as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: src-ip [src-ip]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 match-class

**Parameter table**

+-----------+----------------------------+------------+---------+
| Parameter | Description                | Range      | Default |
+===========+============================+============+=========+
| src-ip    | Source IPv6 address prefix | X:X::X:X/x | \-      |
+-----------+----------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class mc-1
    dnRouter(cfg-flp-ipv6-mc)# src-ip 1050::5:620:510c:357c
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To remove the source-ipv6 from the match class:
::

    dnRouter(cfg-flp-ipv6-mc)# no source-ipv6

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## src-port.rst

routing-policy flowspec-local-policies ipv6 match-class src-ports
-----------------------------------------------------------------

**Minimum user role:** operator

Configures the src-ip as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: src-ports [src-ports]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 match-class

**Parameter table**

+-----------+----------------------------------------------------+---------+---------+
| Parameter | Description                                        | Range   | Default |
+===========+====================================================+=========+=========+
| src-ports | Source port range or a specific source port value. | 0-65535 | \-      |
+-----------+----------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class mc-1
    dnRouter(cfg-flp-ipv6-mc)# src-ports 200-250
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To remove the src-ports from the match class:
::

    dnRouter(cfg-flp-ipv6-mc)# no src-ports

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## tcp-flag.rst

routing-policy flowspec-local-policies ipv6 match-class tcp-flag
----------------------------------------------------------------

**Minimum user role:** operator

Configures the tcp-flag as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: tcp-flag [tcp-flag]** [, tcp-flag, tcp-flag]

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 match-class

**Parameter table**

+-----------+----------------+---------+---------+
| Parameter | Description    | Range   | Default |
+===========+================+=========+=========+
| tcp-flag  | TCP flags list | | syn   | \-      |
|           |                | | ack   |         |
|           |                | | urg   |         |
|           |                | | psh   |         |
|           |                | | rst   |         |
|           |                | | fin   |         |
+-----------+----------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class mc-1
    dnRouter(cfg-flp-ipv6-mc)# tcp-flag syn,ack
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To remove the tcp-flag from the match-class:
::

    dnRouter(cfg-flp-ipv6-mc)# no tcp-flag

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## traffic-class.rst

routing-policy flowspec-local-policies ipv6 match-class traffic-class
---------------------------------------------------------------------

**Minimum user role:** operator

Configures the Traffic-Class as a match criteria of this match class. For the match to be made, all criteria must match.

**Command syntax: traffic-class [traffic-class]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 match-class

**Parameter table**

+---------------+---------------+-------+---------+
| Parameter     | Description   | Range | Default |
+===============+===============+=======+=========+
| traffic-class | Traffic class | 0-63  | \-      |
+---------------+---------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# match-class mc-1
    dnRouter(cfg-flp-ipv6-mc)# traffic-class 45
    dnRouter(cfg-flp-ipv6-mc)#


**Removing Configuration**

To remove the traffic-class from the match class:
::

    dnRouter(cfg-flp-ipv6-mc)# no traffic-class

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## description.rst

routing-policy flowspec-local-policies ipv6 policy description
--------------------------------------------------------------

**Minimum user role:** operator

To add an optional description for the policy.

**Command syntax: description [description]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 policy

**Parameter table**

+-------------+-------------------------+------------------+---------+
| Parameter   | Description             | Range            | Default |
+=============+=========================+==================+=========+
| description | ipv6 policy description | | string         | \-      |
|             |                         | | length 1-255   |         |
+-------------+-------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# policy policy-1
    dnRouter(cfg-flp-ipv6-pl)# description "The policy"
    dnRouter(cfg-flp-ipv6-pl)#


**Removing Configuration**

To revert description to default:
::

    dnRouter(cfg-flp-ipv4-mc)# no description

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## action_rate_limit.rst

routing-policy flowspec-local-policies ipv6 policy match-class action rate-limit
--------------------------------------------------------------------------------

**Minimum user role:** operator

When matching to this match-class, configures that the traffic shall be rate-limited.

**Command syntax: action rate-limit [rate-limit]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 policy match-class

**Parameter table**

+------------+------------------------------------------------------+------------------+---------+
| Parameter  | Description                                          | Range            | Default |
+============+======================================================+==================+=========+
| rate-limit | The rate in kbits per second to limit the traffic to | 0, 64-4294967295 | \-      |
+------------+------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# policy policy-1
    dnRouter(cfg-flp-ipv6-pl)# match-class mc-1
    dnRouter(cfg-ipv6-pl-mc)#  action rate-limit 0
    dnRouter(cfg-ipv6-pl-mc)# exit
    dnRouter(cfg-flp-ipv6-pl)


**Removing Configuration**

To remove the action from the policy:
::

    dnRouter(cfg-ipv6-pl-mc)# no action rate-limit

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## action_redirect-to-vrf.rst

routing-policy flowspec-local-policies ipv6 policy match-class action redirect-to-vrf
-------------------------------------------------------------------------------------

**Minimum user role:** operator

Configures the action of a redirect to another vrf when matching to this match-class.

**Command syntax: action redirect-to-vrf [redirected-to-vrf]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 policy match-class

**Parameter table**

+-------------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter         | Description                                                                      | Range            | Default |
+===================+==================================================================================+==================+=========+
| redirected-to-vrf | redirect-to-vrf target is a reference to another vrf - the next hop should be    | | string         | \-      |
|                   | taken from that vrf                                                              | | length 1-255   |         |
+-------------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# policy policy-1
    dnRouter(cfg-flp-ipv6-pl)# match-class mc-1
    dnRouter(cfg-ipv6-pl-mc)# action redirect-to-vrf vrf-1
    dnRouter(cfg-ipv6-pl-mc)# exit
    dnRouter(cfg-flp-ipv6-pl)


**Removing Configuration**

To remove the redirect-to-vrf action from the policy:
::

    dnRouter(cfg-ipv6-pl-mc)# no action redirect-to-vrf

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## action.rst

routing-policy flowspec-local-policies ipv6 policy match-class action-type
--------------------------------------------------------------------------

**Minimum user role:** operator

Configures the packet-length as a match criteria of this traffic class. All criteria must match, for the match to be made.

**Command syntax: action-type [action-type]** vrf [vrf] max-rate [rate-limit]

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 policy match-class

**Parameter table**

+-------------+----------------------------------------------------------------------------------+----------------------------------+---------+
| Parameter   | Description                                                                      | Range                            | Default |
+=============+==================================================================================+==================================+=========+
| action-type | The action to be performed on match of the traffic class.                        | no-action                        | \-      |
|             |                                                                                  | rate-limit                       |         |
|             |                                                                                  | redirect-to-vrf                  |         |
|             |                                                                                  | redirect-to-vrf-and-rate-limit   |         |
+-------------+----------------------------------------------------------------------------------+----------------------------------+---------+
| vrf         | redirect-to target is a reference to another vrf - the next hop should be taken  | string                           | \-      |
|             | from that vrf.                                                                   | length 1..255                    |         |
+-------------+----------------------------------------------------------------------------------+----------------------------------+---------+
| rate-limit  | The rate in kbits per second to limit the traffic to.                            | 0..4294967295                    | \-      |
+-------------+----------------------------------------------------------------------------------+----------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# policy policy-1
    dnRouter(cfg-flp-ipv6-pl)# match-class mc-1
    dnRouter(cfg-ipv6-pl-mc)#  action-type rate-limit max-rate 0
    dnRouter(cfg-ipv6-pl-mc)# exit
    dnRouter(cfg-flp-ipv6-pl)


**Removing Configuration**

To remove the action from the policy
::

    dnRouter(cfg-ipv6-pl-mc)# no action-type

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## match-class.rst

routing-policy flowspec-local-policies ipv6 policy match-class
--------------------------------------------------------------

**Minimum user role:** operator

To assign an ipv6 match class to the policy:

**Command syntax: match-class [mc-name]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6 policy

**Note**

- Legal string length must be 1-255 characters.

- Illegal characters include any whitespaces and the following special characters (separated by commas): #,!,',”,\

**Parameter table**

+-----------+------------------+------------------+---------+
| Parameter | Description      | Range            | Default |
+===========+==================+==================+=========+
| mc-name   | match class name | | string         | \-      |
|           |                  | | length 1-255   |         |
+-----------+------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# policy policy-1
    dnRouter(cfg-flp-ipv6-pl)# match-class mc-1
    dnRouter(cfg-ipv6-pl-mc)#


**Removing Configuration**

To remove the specified match class:
::

    dnRouter(cfg-flp-ipv6-pl)# no match-class mc-1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## policy.rst

routing-policy flowspec-local-policies ipv6 policy
--------------------------------------------------

**Minimum user role:** operator

To configure an ipv6 policy:

**Command syntax: policy [policy-name]**

**Command mode:** config

**Hierarchies**

- routing-policy flowspec-local-policies ipv6

**Note**

- Legal string length must be 1-255 characters.

- Illegal characters include any whitespaces and the following special characters (separated by commas): #,!,',”,\

**Parameter table**

+-------------+-------------+------------------+---------+
| Parameter   | Description | Range            | Default |
+=============+=============+==================+=========+
| policy-name | policy name | | string         | \-      |
|             |             | | length 1-255   |         |
+-------------+-------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# flowspec-local-policies
    dnRouter(cfg-rpl-flp)# ipv6
    dnRouter(cfg-rpl-flp-ipv6)# policy policy-1
    dnRouter(cfg-flp-ipv6-pl)#


**Removing Configuration**

To remove the specified policy:
::

    dnRouter(cfg-rpl-flp-ipv6)# no policy policy-1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## large-community-list.rst

routing-policy large-community-list
-----------------------------------

**Minimum user role:** operator

BGP Large Communities are a way to signal information between networks. Large BGP Communities are composed of a 12-byte path attribute constructed from a set of 3 uint32 values. An example of a Large Community is: 2914:65400:38016.
To define a new large community list and enter its configuration mode:

**Command syntax: large-community-list [large-community-list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy

**Note**

- Notice the change in prompt.

**Parameter table**

+---------------------------+--------------------------------------+------------------+---------+
| Parameter                 | Description                          | Range            | Default |
+===========================+======================================+==================+=========+
| large-community-list-name | The name of the large-community-list | | string         | \-      |
|                           |                                      | | length 1-255   |         |
+---------------------------+--------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# large-community-list CL_NAME
    dnRouter(cfg-rpl-lcl)#


**Removing Configuration**

To delete a large community list:
::

    dnRouter(cfg-rpl)# no large-community-list CL_NAME

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## rule-regex.rst

routing-policy large-community-list rule
----------------------------------------

**Minimum user role:** operator

To configure regex rules for large-community lists:

**Command syntax: rule [rule-id] [rule-type] regex [regex]**

**Command mode:** config

**Hierarchies**

- routing-policy large-community-list

**Parameter table**

+-----------+----------------------------------------------------------------------------------+-----------+---------+
| Parameter | Description                                                                      | Range     | Default |
+===========+==================================================================================+===========+=========+
| rule-id   | The rule's unique identifier within the community list. It determines the        | 1-65534   | \-      |
|           | priority of the rule (rules with a low ID number have priority over rules with   |           |         |
|           | high ID numbers). You must configure at least one rule.                          |           |         |
|           | The default ID (65535) is assigned by the system to 'Deny any' when no match is  |           |         |
|           | found.                                                                           |           |         |
|           | When configuring a rule ID that is already in use, all of the original rules'    |           |         |
|           | entries are overwritten.                                                         |           |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+
| rule-type | Defines whether the traffic matching the rule conditions are to be allowed or    | | allow   | \-      |
|           | denied.                                                                          | | deny    |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+
| regex     | A regular expression defining a search pattern to match large communities        | \-        | \-      |
|           | attribute in BGP updates.                                                        |           |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# large-community-list CL_NAME
    dnRouter(cfg-rpl-lcl)# rule 10 allow regex 65000:*:5000


**Removing Configuration**

To remove a rule entry:
::

    dnRouter(cfg-rpl-lcl)# no rule 10

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## rule-value.rst

routing-policy large-community-list rule
----------------------------------------

**Minimum user role:** operator

To configure 'value' rules for large-community lists:

**Command syntax: rule [rule-id] [rule-type] value [large-community-value]**

**Command mode:** config

**Hierarchies**

- routing-policy large-community-list

**Parameter table**

+-----------------------+----------------------------------------------------------------------------------+----------------------------------------------+----------+
| Parameter             | Description                                                                      | Range                                        | Default  |
+=======================+==================================================================================+==============================================+==========+
| rule-id               | The rule's unique identifier within the community list. It determines the        | 1-65534                                      | \-       |
|                       | priority of the rule (rules with a low ID number have priority over rules with   |                                              |          |
|                       | high ID numbers). You must configure at least one rule.                          |                                              |          |
|                       | The default ID (65535) is assigned by the system to 'Deny any' when no match is  |                                              |          |
|                       | found.                                                                           |                                              |          |
|                       | When configuring a rule ID that is already in use, all of the original rules'    |                                              |          |
|                       | entries are overwritten.                                                         |                                              |          |
+-----------------------+----------------------------------------------------------------------------------+----------------------------------------------+----------+
| rule-type             | Defines whether the traffic matching the rule conditions are to be allowed or    | | allow                                      | \-       |
|                       | denied.                                                                          | | deny                                       |          |
+-----------------------+----------------------------------------------------------------------------------+----------------------------------------------+----------+
| large-community-value | <AS_number:id-1:id-2>                                                            | [0-4294967295]:[0-4294967295]:[0-4294967295] | \-:\-:\- |
+-----------------------+----------------------------------------------------------------------------------+----------------------------------------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# large-community-list CL_NAME
    dnRouter(cfg-rpl-lcl)# rule 10 allow value 15562:45:29


**Removing Configuration**

To remove a rule entry:
::

    dnRouter(cfg-rpl-lcl)# no rule 10

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## policy.rst

routing-policy policy
---------------------

**Minimum user role:** operator

Policies provide a means to filter and/or apply actions to a route, thus allowing policies to be applied to routes. The policy includes an ordered list of entries, where each entry may specify the following:

- Matching conditions: the conditions which must be matched if the entry is to be considered further. If no conditions are defined, then the entry is always met. If more than one condition is defined, all conditions must be met.

- Set Actions: a policy entry may optionally specify one or more actions to set or modify attributes of the route. If multiple actions are defined, all actions are performed (if the proper conditions are met).

To create a policy and enter its configuration mode:

**Command syntax: policy [policy-name]**

**Command mode:** config

**Hierarchies**

- routing-policy

**Note**

- You cannot delete a policy that is attached to a BGP or OSPF process.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter   | Description                                                                      | Range            | Default |
+=============+==================================================================================+==================+=========+
| policy-name | Provide a name for the policy. Names with spaces must be enclosed in quotation   | | string         | \-      |
|             | marks. If you do not want to use quotation marks, do not use spaces.             | | length 1-255   |         |
+-------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)#

    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy ANOTHER_POLICY
    dnRouter(cfg-rpl-policy)#


**Removing Configuration**

To remove the policy:
::

    dnRouter(cfg-rpl-policy)# no policy MY_POLICY
    dnRouter(cfg-rpl-policy)# no policy ANOTHER_POLICY

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## call.rst

routing-policy policy rule call
-------------------------------

**Minimum user role:** operator

To jump to another policy after match and set action of this rule:

**Command syntax: call [policy-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-------------+------------------------------------------+------------------+---------+
| Parameter   | Description                              | Range            | Default |
+=============+==========================================+==================+=========+
| policy-name | The name of the policy to which to jump. | | string         | \-      |
|             |                                          | | length 1-255   |         |
+-------------+------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# call ANOTHER_POLICY


**Removing Configuration**

To remove the policy call:
::

    dnRouter(cfg-rpl-policy-rule-10)# no call

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## description.rst

routing-policy policy rule description
--------------------------------------

**Minimum user role:** operator

To add a description for the rule:

**Command syntax: description [description]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter   | Description                                                                      | Range            | Default |
+=============+==================================================================================+==================+=========+
| description | Enter a description for the rule.                                                | | string         | \-      |
|             | Enter free-text description with spaces in between quotation marks. If you do    | | length 1-255   |         |
|             | not use quotation marks, do not use spaces.                                      |                  |         |
|             | For example:                                                                     |                  |         |
|             | ... description 'My long description'                                            |                  |         |
|             | ... description My_long_description                                              |                  |         |
+-------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# description MyDescription_Rule10

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# description MyDescription_Rule20


**Removing Configuration**

To remove the description:
::

    dnRouter(cfg-rpl-policy-rule-10)# no description

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## match_as-path-length.rst

routing-policy policy rule match as-path-length
-----------------------------------------------

**Minimum user role:** operator

To compare the AS numbers in the AS-path of a BGP route:

**Command syntax: match as-path-length [as-path-length-range]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+----------------------+----------------------------------+---------------------+---------+
| Parameter            | Description                      | Range               | Default |
+======================+==================================+=====================+=========+
| as-path-length-range | the number of ASN in the AS-path | 0..1024 (x-y range) | \-      |
+----------------------+----------------------------------+---------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match as-path-length 51-1024

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# match as-path-length 13

    dnRouter(cfg-rpl-policy)# rule 30 allow
    dnRouter(cfg-rpl-policy-rule-30)# match as-path-length 5-10


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match as-path-length

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## match_as-path.rst

routing-policy policy rule match as-path
----------------------------------------

**Minimum user role:** operator

To check whether the route's AS path matches AS paths in the specified AS path access-list:

**Command syntax: match as-path [list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+--------------------------------------------------------------------+------------------+---------+
| Parameter | Description                                                        | Range            | Default |
+===========+====================================================================+==================+=========+
| list-name | The name of the AS-Path access-list with which to match AS path.   | | string         | \-      |
|           | Routes without a matching AS path are ignored.                     | | length 1-255   |         |
+-----------+--------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match as-path LIST-1


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match as-path

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## match_community_all.rst

routing-policy policy rule match-all community
----------------------------------------------

**Minimum user role:** operator

To all-match BGP updates using a community-list:

**Command syntax: match-all community [list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+------------------------------------+------------------+---------+
| Parameter | Description                        | Range            | Default |
+===========+====================================+==================+=========+
| list-name | The community-list's name to match | | string         | \-      |
|           |                                    | | length 1-255   |         |
+-----------+------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match-all community CL_RTBH


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match-all community

**Command History**

+---------+--------------------------------------+
| Release | Modification                         |
+=========+======================================+
| 6.0     | Command introduced                   |
+---------+--------------------------------------+
| 10.0    | Match is done using a community-list |
+---------+--------------------------------------+
| 11.0    | Removed the option for exact-match   |
+---------+--------------------------------------+

---

## match_community.rst

routing-policy policy rule match community
------------------------------------------

**Minimum user role:** operator

To match BGP updates using a community-list:

**Command syntax: match community [list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+------------------------------------+------------------+---------+
| Parameter | Description                        | Range            | Default |
+===========+====================================+==================+=========+
| list-name | The community-list's name to match | | string         | \-      |
|           |                                    | | length 1-255   |         |
+-----------+------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match community CL_RTBH


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match community

**Command History**

+---------+--------------------------------------+
| Release | Modification                         |
+=========+======================================+
| 6.0     | Command introduced                   |
+---------+--------------------------------------+
| 10.0    | Match is done using a community-list |
+---------+--------------------------------------+
| 11.0    | Removed the option for exact-match   |
+---------+--------------------------------------+

---

## match_encap-extcommunity.rst

routing-policy policy rule match encap-extcommunity
---------------------------------------------------

**Minimum user role:** operator

To match path by Encapsulation Extended Community attribute (RFC9012) per desired tunnel-type

**Command syntax: match encap-extcommunity [tunnel-type]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter   | Description                                                                      | Range | Default |
+=============+==================================================================================+=======+=========+
| tunnel-type | match path by Encapsulation Extended Community attribute (RFC9012) per desired   | vxlan | \-      |
|             | tunnel-type                                                                      |       |         |
+-------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match encap-extcommunity vxlan


**Removing Configuration**

To remove match protocols criteria:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match encap-extcommunity

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+

---

## match_evpn-mac-route.rst

routing-policy policy rule match evpn-mac-route
-----------------------------------------------

**Minimum user role:** operator

Match EVPN MAC-IP routes that do not include any IP address, that include only IPv4 addresses or that include only IPv6 addresses.

To check whether the route's EVPN MAC-IP route matches the specified route match:

**Command syntax: match evpn-mac-route [evpn-mac-route]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+----------------+---------------------------------------------------------------+--------------+---------+
| Parameter      | Description                                                   | Range        | Default |
+================+===============================================================+==============+=========+
| evpn-mac-route | Match the EVPN MAC-IP mac route by family (none|ipv4|ipv6).   | | mac-only   | \-      |
|                | Routes with no match are ignored.                             | | mac-ipv4   |         |
|                |                                                               | | mac-ipv6   |         |
+----------------+---------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match evpn-mac-route mac-ipv4

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match evpn-mac-route mac-ipv6

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match evpn-mac-route mac-only


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match evpn-mac-route

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+

---

## match_evpn-route-type.rst

routing-policy policy rule match evpn-route-type
------------------------------------------------

**Minimum user role:** operator

Match EVPN prefix by route type.

To check whether the route's EVPN route type matches the specified route type:

**Command syntax: match evpn-route-type [evpn-route-type]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------------+-----------------------------------------------+-------+---------+
| Parameter       | Description                                   | Range | Default |
+=================+===============================================+=======+=========+
| evpn-route-type | The EVPN route type to match.                 | 1-5   | \-      |
|                 | Routes without a matching type are ignored.   |       |         |
+-----------------+-----------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match evpn-route-type 3


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match evpn-route-type

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+

---

## match_extcommunity_all.rst

routing-policy policy rule match-all extcommunity
-------------------------------------------------

**Minimum user role:** operator

To match BGP updates by extended community list:

**Command syntax: match-all extcommunity [list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+----------------------------------------------+------------------+---------+
| Parameter | Description                                  | Range            | Default |
+===========+==============================================+==================+=========+
| list-name | The extended community-list's name to match. | | string         | \-      |
|           |                                              | | length 1-255   |         |
+-----------+----------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match-all extcommunity XCL_LP90


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match-all extcommunity

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## match_extcommunity.rst

routing-policy policy rule match extcommunity
---------------------------------------------

**Minimum user role:** operator

To match BGP updates by extended community list:

**Command syntax: match extcommunity [list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+----------------------------------------------+------------------+---------+
| Parameter | Description                                  | Range            | Default |
+===========+==============================================+==================+=========+
| list-name | The extended community-list's name to match. | | string         | \-      |
|           |                                              | | length 1-255   |         |
+-----------+----------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match extcommunity XCL_LP90


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match extcommunity

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## match_ipv4_next-hop.rst

routing-policy policy rule match ipv4 next-hop prefix-list
----------------------------------------------------------

**Minimum user role:** operator

To match any IPv4 routes that have the specified next-hop router address or that match a next hop address in the access lists:

**Command syntax: match ipv4 next-hop prefix-list [ipv4-prefix-list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter             | Description                                                                      | Range            | Default |
+=======================+==================================================================================+==================+=========+
| ipv4-prefix-list-name | Matches routes that have a next hop router address in this access list.          | | string         | \-      |
|                       | Prefixes matching a 'deny' rule in the prefix-list (including the default rule)  | | length 1-255   |         |
|                       | are considered as 'no match' in the policy and the next rule in the policy is    |                  |         |
|                       | evaluated.                                                                       |                  |         |
+-----------------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match ipv4 next-hop prefix-list PL_TWAMP


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match ipv4 next-hop

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## match_ipv4_prefix.rst

routing-policy policy rule match ipv4 prefix
--------------------------------------------

**Minimum user role:** operator

To match routes based on IPv4 address entries in the specified prefix-list:

**Command syntax: match ipv4 prefix [prefix-list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+------------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter        | Description                                                                      | Range            | Default |
+==================+==================================================================================+==================+=========+
| prefix-list-name | The name of the prefix list from which to match prefixes.                        | | string         | \-      |
|                  | You can match for multiple IPv4 prefix-lists under the same rule entry.          | | length 1-255   |         |
|                  | The prefix-list type ipv4 must match the IP address family.                      |                  |         |
|                  | Prefixes matching a 'deny' rule in the prefix-list (including the default rule)  |                  |         |
|                  | are considered as 'no match' in the policy and the next rule in the policy is    |                  |         |
|                  | evaluated.                                                                       |                  |         |
+------------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match ipv4 prefix PL_V4


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match ipv4 prefix

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## match_ipv6_next-hop.rst

routing-policy policy rule match ipv6 next-hop prefix-list
----------------------------------------------------------

**Minimum user role:** operator

To match any IPv6 routes that have the specified next-hop router address or that match a next-hop address in the access lists:

**Command syntax: match ipv6 next-hop prefix-list [ipv6-prefix-list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter             | Description                                                                      | Range            | Default |
+=======================+==================================================================================+==================+=========+
| ipv6-prefix-list-name | Matches routes that have a next hop router address in this access list.          | | string         | \-      |
|                       | Prefixes matching a 'deny' rule in the prefix-list (including the default rule)  | | length 1-255   |         |
|                       | are considered as 'no match' in the policy and the next rule in the policy is    |                  |         |
|                       | evaluated.                                                                       |                  |         |
+-----------------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match ipv6 next-hop prefix-list PL6_TWAMP


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match ipv6 next-hop

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## match_ipv6_prefix.rst

routing-policy policy rule match ipv6 prefix
--------------------------------------------

**Minimum user role:** operator

To match routes based on IPv6 address entries in the specified prefix-list:

**Command syntax: match ipv6 prefix [prefix-list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+------------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter        | Description                                                                      | Range            | Default |
+==================+==================================================================================+==================+=========+
| prefix-list-name | The name of the prefix list from which to match prefixes.                        | | string         | \-      |
|                  | You can match for multiple IPv6 prefix-lists under the same rule entry.          | | length 1-255   |         |
|                  | The prefix-list type IPv6 must match the IP address family.                      |                  |         |
|                  | Prefixes matching a 'deny' rule in the prefix-list (including the default rule)  |                  |         |
|                  | are considered as 'no match' in the policy and the next rule in the policy is    |                  |         |
|                  | evaluated.                                                                       |                  |         |
+------------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match ipv6 prefix PL_V6


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match ipv6 prefix

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## match_large-community_all.rst

routing-policy policy rule match-all large-community
----------------------------------------------------

**Minimum user role:** operator

To all-match BGP updates by large-community using a large-community-list:

**Command syntax: match-all large-community [list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+-----------------------------------------+------------------+---------+
| Parameter | Description                             | Range            | Default |
+===========+=========================================+==================+=========+
| list-name | The large-community-list name to match. | | string         | \-      |
|           |                                         | | length 1-255   |         |
+-----------+-----------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match-all large-community LARGE_CL_1


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match-all large-community

**Command History**

+---------+--------------------------------------+
| Release | Modification                         |
+=========+======================================+
| 6.0     | Command introduced                   |
+---------+--------------------------------------+
| 10.0    | Match is done using a community-list |
+---------+--------------------------------------+
| 11.0    | Removed the option for exact-match   |
+---------+--------------------------------------+

---

## match_large-community.rst

routing-policy policy rule match large-community
------------------------------------------------

**Minimum user role:** operator

To match BGP updates by large-community using a large-community-list:

**Command syntax: match large-community [list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+-----------------------------------------+------------------+---------+
| Parameter | Description                             | Range            | Default |
+===========+=========================================+==================+=========+
| list-name | The large-community-list-name to match. | | string         | \-      |
|           |                                         | | length 1-255   |         |
+-----------+-----------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match large-community LARGE_CL_1


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match large-community

**Command History**

+---------+--------------------------------------+
| Release | Modification                         |
+=========+======================================+
| 6.0     | Command introduced                   |
+---------+--------------------------------------+
| 10.0    | Match is done using a community-list |
+---------+--------------------------------------+
| 11.0    | Removed the option for exact-match   |
+---------+--------------------------------------+

---

## match_med.rst

routing-policy policy rule match med
------------------------------------

**Minimum user role:** operator

To match to the multi-exit discriminator metric value:

**Command syntax: match med [med]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+----------------------------------------------+--------------+---------+
| Parameter | Description                                  | Range        | Default |
+===========+==============================================+==============+=========+
| med       | The multi-exit discriminator value to match. | 0-4294967295 | \-      |
+-----------+----------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match med 40000


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match med

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## match_origin.rst

routing-policy policy rule match origin
---------------------------------------

**Minimum user role:** operator

To match the BGP attribute origin-type:

**Command syntax: match origin [type]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+------------------------------------------+----------------+---------+
| Parameter | Description                              | Range          | Default |
+===========+==========================================+================+=========+
| type      | Match the origin of the path information | | igp          | \-      |
|           |                                          | | egp          |         |
|           |                                          | | incomplete   |         |
+-----------+------------------------------------------+----------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match origin igp

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# match origin egp

    dnRouter(cfg-rpl-policy)# rule 30 allow
    dnRouter(cfg-rpl-policy-rule-30)# match origin incomplete


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match origin

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 13.1    | Command introduced |
+---------+--------------------+

---

## match_path-mark-count_eq.rst

routing-policy policy rule match path-mark-count eq
---------------------------------------------------

**Minimum user role:** operator

To match the number of path-marks over all the route paths:

**Command syntax: match path-mark-count eq [eq-value]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- This command works on routes with a path-mark attribute. See "policy set path-mark".

- The number of path-marks is counted over all BGP paths for a given route, not only on the best paths.

- You cannot set eq together with le or ge.

**Parameter table**

+-----------+------------------------------+-------+---------+
| Parameter | Description                  | Range | Default |
+===========+==============================+=======+=========+
| eq-value  | Match to the specified value | 0-32  | \-      |
+-----------+------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match path-mark-count eq 3


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match path-mark-count eq EQ

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 13.0    | Command introduced |
+---------+--------------------+

---

## match_path-mark-count_ge-le.rst

routing-policy policy rule match path-mark-count
------------------------------------------------

**Minimum user role:** operator

To match the number of path-marks over all the route paths:

**Command syntax: match path-mark-count {ge [ge-value], le [le-value]}**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- This command works on routes with a path-mark attribute. See "policy set path-mark".

- The number of path-marks is counted over all BGP paths for a given route, not only on the best paths.

- Use a combination of ge- and le- values to set a range, where le-value is ≥ ge-value.

- The le-value must be greater or equal to the ge-value.

- You cannot set le or ge together with eq.

**Parameter table**

+-----------+-------------------------------------------------------------------+-------+---------+
| Parameter | Description                                                       | Range | Default |
+===========+===================================================================+=======+=========+
| ge-value  | Match to a number that is greater or equal to the specified value | 0-32  | \-      |
+-----------+-------------------------------------------------------------------+-------+---------+
| le-value  | Match to a number that is lower or equal to the specified value   | 0-32  | \-      |
+-----------+-------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match path-mark-count le 5

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# match path-mark-count ge 1

    dnRouter(cfg-rpl-policy)# rule 30 allow
    dnRouter(cfg-rpl-policy-rule-30)# match path-mark-count ge 1 le 5


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match path-mark-count

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 13.0    | Command introduced |
+---------+--------------------+

---

## match_path-type.rst

routing-policy policy rule match path-type
------------------------------------------

**Minimum user role:** operator

To match BGP routes by path-type, i.e., if the route is learned via iBGP or eBGP:

**Command syntax: match path-type [type]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+----------------------------------------------+----------+---------+
| Parameter | Description                                  | Range    | Default |
+===========+==============================================+==========+=========+
| type      | Match the paths that are learned via eBGP.   | | ebgp   | \-      |
|           | Match the paths that are learned via iBGP.   | | ibgp   |         |
+-----------+----------------------------------------------+----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match path-type ebgp

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# match path-type ibgp


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match path-type

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.2    | Command introduced |
+---------+--------------------+

---

## match_prefix-sid.rst

routing-policy policy rule match prefix-sid
-------------------------------------------

**Minimum user role:** operator

To match path by sub-type of prefix-sid attribute

**Command syntax: match prefix-sid [tunnel-type]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-------------+---------------------------------------+--------------------+---------+
| Parameter   | Description                           | Range              | Default |
+=============+=======================================+====================+=========+
| tunnel-type | match path by prefix-sid sub-tlv-type | | srv6-l2          | \-      |
|             |                                       | | srv6-l3          |         |
|             |                                       | | sr-label-index   |         |
+-------------+---------------------------------------+--------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match prefix-sid srv6-l2


**Removing Configuration**

To remove match protocols criteria:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match prefix-sid

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.3    | Command introduced |
+---------+--------------------+

---

## match_protocol.rst

routing-policy policy rule match protocol
-----------------------------------------

**Minimum user role:** operator

Match a prefix by the protocol origin from which the prefix was learned.

**Command syntax: match protocol [match-protocol]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**
Currently this option is only supported for policies applied to RIB-groups and VPN.

**Parameter table**

+----------------+-----------------------------------------------------------------+---------------+---------+
| Parameter      | Description                                                     | Range         | Default |
+================+=================================================================+===============+=========+
| match-protocol | Match a prefix by protocol origin from which prefix was learned | | connected   | \-      |
|                |                                                                 | | static      |         |
|                |                                                                 | | bgp         |         |
|                |                                                                 | | ospf        |         |
|                |                                                                 | | ospfv3      |         |
|                |                                                                 | | isis        |         |
|                |                                                                 | | pim         |         |
|                |                                                                 | | ldp         |         |
|                |                                                                 | | rsvp        |         |
|                |                                                                 | | isis-sr     |         |
|                |                                                                 | | ospf-sr     |         |
|                |                                                                 | | sr-te       |         |
+----------------+-----------------------------------------------------------------+---------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match protocol connected


**Removing Configuration**

To remove match protocols criteria:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match protocol

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## match_rib-has-route.rst

routing-policy policy rule match rib-has-route
----------------------------------------------

**Minimum user role:** operator

To match if a route exist in Routing Information Base (RIB):

**Command syntax: match rib-has-route [match-rib-has-route]** protocol [protocol]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- Match is exact prefix match

- Match is for selected routes only

**Parameter table**

+---------------------+----------------------------------------------------------------------------------+----------------+---------+
| Parameter           | Description                                                                      | Range          | Default |
+=====================+==================================================================================+================+=========+
| match-rib-has-route | Match if a requested route exists in the Routing Information Base (RIB) as       | | A.B.C.D/x    | \-      |
|                     | selected route for FIB installation.                                             | | X:X::X:X/x   |         |
+---------------------+----------------------------------------------------------------------------------+----------------+---------+
| protocol            | Match that route required by rib-has-route was installed to Routing Information  | | bgp          | \-      |
|                     | Base (RIB) by specific protocol                                                  | | connected    |         |
|                     |                                                                                  | | ebgp         |         |
|                     |                                                                                  | | ibgp         |         |
+---------------------+----------------------------------------------------------------------------------+----------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match rib-has-route 1.12.18.4/31
    dnRouter(cfg-rpl-policy-rule-10)# exit
    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# match rib-has-route 2005:100:0:d::/128

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match rib-has-route 223.16.16.6/32 protocol connected


**Removing Configuration**

To remove match rib-has-route criteria:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match rib-has-route

To remove match rib-has-route protocol criteria:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match rib-has-route 223.16.16.6/32 protocol

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.0    | Command introduced |
+---------+--------------------+

---

## match_rpki.rst

routing-policy policy rule match rpki
-------------------------------------

**Minimum user role:** operator

To match advertised prefixes on RPKI state:

**Command syntax: match rpki [rpki-state]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+------------+---------------------------+---------------+---------+
| Parameter  | Description               | Range         | Default |
+============+===========================+===============+=========+
| rpki-state | The RPKI validation state | | valid       | \-      |
|            |                           | | invalid     |         |
|            |                           | | not-found   |         |
+------------+---------------------------+---------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match rpki valid

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# match rpki invalid

    dnRouter(cfg-rpl-policy)# rule 30 allow
    dnRouter(cfg-rpl-policy-rule-30)# match rpki not-found


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match rpki

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## match_tag.rst

routing-policy policy rule match tag
------------------------------------

**Minimum user role:** operator

To match the tag attribute:

**Command syntax: match tag [tag]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+-------------------------+--------------+---------+
| Parameter | Description             | Range        | Default |
+===========+=========================+==============+=========+
| tag       | The tag value to match. | 0-4294967295 | \-      |
+-----------+-------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# match tag 55


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no match tag

**Command History**

+---------+-------------------------------------------------+
| Release | Modification                                    |
+=========+=================================================+
| 6.0     | Command introduced                              |
+---------+-------------------------------------------------+
| 16.1    | Extended tag range to support unit_32 tag value |
+---------+-------------------------------------------------+

---

## on-match_goto.rst

routing-policy policy rule on-match goto
----------------------------------------

**Minimum user role:** operator

To jump to another rule in the policy:

**Command syntax: on-match goto [rule-id]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- goto - jump to a specific rule.



- when the specified rule-id isn't configured, jump to the next higher configured rule



- [rule-id] must be higher than the current rule id. e.g the following configuration is **invalid**

 dnRouter# configure

 dnRouter(cfg)# routing-policy

 dnRouter(cfg-rpl)# policy POL_A

 dnRouter(cfg-rpl-policy)# rule **20** allow

 dnRouter(cfg-rpl-policy-rule- **20**)# goto **10**



- ! can't jump backwards in policies

**Parameter table**

+-----------+----------------------------------------------------------------------------------+---------+---------+
| Parameter | Description                                                                      | Range   | Default |
+===========+==================================================================================+=========+=========+
| rule-id   | Jump to a specific rule. The rule-id must be higher than the current rule.       | 1-65535 | \-      |
|           | Therefore, if you are configuring rule 20, you cannot configure on-match goto    |         |         |
|           | 10.                                                                              |         |         |
+-----------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# on-match goto 30


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-20)# no on-match

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## on-match_next-policy.rst

routing-policy policy rule on-match next-policy
-----------------------------------------------

**Minimum user role:** operator

To jump to evaluate next attached policy:

**Command syntax: on-match next-policy**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 30 allow
    dnRouter(cfg-rpl-policy-rule-30)# on-match next-policy
    dnRouter(cfg-rpl-policy-rule-30)# match tag 10


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no on-match

**Command History**

+---------+------------------------+
| Release | Modification           |
+=========+========================+
| 6.0     | Command introduced     |
+---------+------------------------+
| 17.2    | Next-policy introduced |
+---------+------------------------+

---

## on-match_next.rst

routing-policy policy rule on-match next
----------------------------------------

**Minimum user role:** operator

To jump to the next configured rule:

**Command syntax: on-match next**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# on-match next


**Removing Configuration**

To remove the match entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no on-match

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## rule.rst

routing-policy policy rule
--------------------------

**Minimum user role:** operator

To create a new rule and enter its configuration hierarchy:

**Command syntax: rule [rule-id] [rule-type]**

**Command mode:** config

**Hierarchies**

- routing-policy policy

**Note**

- You cannot configure 'set' actions under a 'deny' rule.

- You can configure multiple different types of match or set under the same entry.

- If more than one match condition is defined, all conditions must be met for the rule to apply.

- Rule-id 65535 is the default rule assigned by the system, configured to deny any route.

- There is no guarantee for the order in which configuration under a rule is applied. If ordering is needed it can be achieved by splitting the configuration into several rules and using the 'on-match next' functionality.

- - for example:

- | dnRouter(cfg-rpl-policy-rule-10)# match as-path LIST-1

- | dnRouter(cfg-rpl-policy-rule-10)# match as-path LIST-2

- |   'match as-path LIST-2' will override the 'match as-path LIST-1' configuration

- | dnRouter(cfg-rpl-policy-rule-10)# set as-path prepend 23456

- | dnRouter(cfg-rpl-policy-rule-10)# set as-path prepend 12956

- |   'set as-path prepend 12956' will override the 'set as-path prepend 23456' configuration

**Parameter table**

+-----------+----------------------------------------------------------------------------------+-----------+---------+
| Parameter | Description                                                                      | Range     | Default |
+===========+==================================================================================+===========+=========+
| rule-id   | The rule's unique identifier within the route map. It determines the priority of | 1-65534   | \-      |
|           | the rule (rules with a low ID number have priority over rules with high ID       |           |         |
|           | numbers). You must configure at least one rule.                                  |           |         |
|           | The default ID (65535) is assigned by the system to 'Deny any' when no match is  |           |         |
|           | found.                                                                           |           |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+
| rule-type | Defines whether the traffic matching the rule conditions are to be allowed or    | | allow   | \-      |
|           | denied.                                                                          | | deny    |         |
+-----------+----------------------------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)#

    dnRouter(cfg-rpl-policy)# rule 20 deny
    dnRouter(cfg-rpl-policy-rule-20)#


**Removing Configuration**

To remove the rule entry:
::

    dnRouter(cfg-rpl-policy)# no rule 10

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## set_aigp_igp-metric.rst

routing-policy policy rule set aigp igp-metric
----------------------------------------------

**Minimum user role:** operator

Sets the metric value as the IGP-metric for the route.

The set AIGP action depends on the policy attachment point:

+---------------------------------------------------------------+------------------------------------------------------------------+
| Set AIGP Policy Attachment Point                              | Set AIGP IGP-metric                                              |
+===============================================================+==================================================================+
| bgp neighbor address-family policy in                         | Set 0 in the AIGP metric                                         |
|                                                               |                                                                  |
|                                                               | **This is not the proper usage.**                                |
+---------------------------------------------------------------+------------------------------------------------------------------+
| bgp neighbor address-family policy out                        | Set 0 in the AIGP metric                                         |
|                                                               |                                                                  |
|                                                               | **This is not the proper usage.**                                |
+---------------------------------------------------------------+------------------------------------------------------------------+
| bgp address-family unicast redistribute ospf|static|connected | Set the IGP metric of the redistributed route to BGP AIGP.       |
|                                                               | This will cause the NCR to be the AIGP originator for the route. |
|                                                               |                                                                  |
+---------------------------------------------------------------+------------------------------------------------------------------+
| bgp network                                                   | Set the IGP metric of the redistributed route to BGP AIGP.       |
|                                                               | This will cause the NCR to be the AIGP originator for the route. |
|                                                               |                                                                  |
+---------------------------------------------------------------+------------------------------------------------------------------+

To set the AIGP metric attribute:

**Command syntax: set aigp igp-metric**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- BGP neighbor afi must be set with 'aigp enabled', otherwise no aigp attribute is sent or received regardless of the policy set action.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set aigp igp-metric


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set aigp

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 7.0     | Command introduced |
+---------+--------------------+

---

## set_aigp_relative.rst

routing-policy policy rule set aigp
-----------------------------------

**Minimum user role:** operator

The set AIGP action depends on the policy attachment point:

+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Set AIGP Policy Attachment Point                              | Set AIGP [relative] [aigp-value]                                                                      |
+===============================================================+=======================================================================================================+
| bgp neighbor address-family policy in                         | Add the given [aigp-value] to or deduct it from the AIGP metric attribute before best path selection. |
|                                                               |                                                                                                       |
|                                                               |                                                                                                       |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| bgp neighbor address-family policy out                        | Add the given [aigp-value] to or deduct it from the AIGP metric attribute after best path selection.  |
|                                                               |                                                                                                       |
|                                                               |                                                                                                       |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| bgp address-family unicast redistribute ospf|static|connected | Add the value to or deduct the value from the AIGP metric attribute of the BGP path.                  |
|                                                               | If the attribute does not exist, it will be created.                                                  |
|                                                               | This will cause the NCR to be the AIGP originator for the route.                                      |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| bgp network                                                   | Add the value to or deduct the value from the AIGP metric attribute of the BGP path.                  |
|                                                               | If the attribute does not exist, it will be created.                                                  |
|                                                               | This will cause the NCR to be the AIGP originator for the route.                                      |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

To set the AIGP metric attribute:

**Command syntax: set aigp [relative] [aigp-value]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- BGP neighbor afi must be set with 'aigp enabled', otherwise no aigp attribute is sent or received regardless of the policy set action.

**Parameter table**

+------------+---------------------------------------------------------------------------+--------------+---------+
| Parameter  | Description                                                               | Range        | Default |
+============+===========================================================================+==============+=========+
| relative   | Increase/decrease the current value of the AIGP metric by [aigp-value].   | | +          | \-      |
|            | The resulting value cannot go below 0 or above the maximum aigp-value.    | | -          |         |
+------------+---------------------------------------------------------------------------+--------------+---------+
| aigp-value | The new value of the AIGP metric that will be set.                        | 0-4294967294 | \-      |
+------------+---------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-30)# set aigp + 10

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-40)# set aigp - 10


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set aigp

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 7.0     | Command introduced |
+---------+--------------------+

---

## set_aigp_value.rst

routing-policy policy rule set aigp
-----------------------------------

**Minimum user role:** operator

The set AIGP action depends on the policy attachment point:

+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Set AIGP Policy Attachment Point                              | Set AIGP [aigp-value]                                                               |
+===============================================================+=====================================================================================+
| bgp neighbor address-family policy in                         | Set the given [aigp-value] to the AIGP metric attribute before best path selection. |
|                                                               |                                                                                     |
|                                                               |                                                                                     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| bgp neighbor address-family policy out                        | Overwrite the AIGP metric value with the specified [aigp-value].                    |
|                                                               |                                                                                     |
|                                                               |                                                                                     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| bgp address-family unicast redistribute ospf|static|connected | Set a specific value for the BGP AIGP attribute of the BGP path.                    |
|                                                               | If the attribute does not exist, it will be created.                                |
|                                                               | This will cause the NCR to be the AIGP originator for the route.                    |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| bgp network                                                   | Set a specific value for the BGP AIGP attribute of the BGP path.                    |
|                                                               | If the attribute does not exist, it will be created.                                |
|                                                               | This will cause the NCR to be the AIGP originator for the route.                    |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+

To set the AIGP metric attribute:

**Command syntax: set aigp [aigp-value]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- BGP neighbor afi must be set with 'aigp enabled', otherwise no aigp attribute is sent or received regardless of the policy set action.

**Parameter table**

+------------+----------------------------------------------------+--------------+---------+
| Parameter  | Description                                        | Range        | Default |
+============+====================================================+==============+=========+
| aigp-value | The new value of the AIGP metric that will be set. | 0-4294967294 | \-      |
+------------+----------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-20)# set aigp 300


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set aigp

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 7.0     | Command introduced |
+---------+--------------------+

---

## set_as-path_exclude_from_to.rst

routing-policy policy rule set as-path exclude from to
------------------------------------------------------

**Minimum user role:** operator

Remove any as number from the as-path that falls in the provided range.
To exclude the specified as-number(s) from the as-path:

**Command syntax: set as-path exclude from [set-as-path-exclude-from] to [set-as-path-exclude-to]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- Within the same route policy rule, "set as-path exclude from to" will be processed and imposed before "set as-path prepend" action.

- Can be set in the same rule with "set as-path exclude <as-path list>". All as numbers requested by the two set cmds will be removed from the as-path.

- The removed as number does not have to be sequential on the as the path, e.g., for as-path = ‘67 65534 100 65533 5 78 89 90’ and imposing "set as-path exclude from 65533 to 65534" the resulting as-path will be ‘67 100 5 78 89 90’.

- Commit validation required that to >= from. Can support set as-path to exclude from X to X to impose specific as-number removal.

**Parameter table**

+--------------------------+----------------------------------------------------------+--------------+---------+
| Parameter                | Description                                              | Range        | Default |
+==========================+==========================================================+==============+=========+
| set-as-path-exclude-from | Starting range for as-numbers to be removed from as-path | 1-4294967295 | \-      |
+--------------------------+----------------------------------------------------------+--------------+---------+
| set-as-path-exclude-to   | End range for as-numbers to be removed from as-path      | 1-4294967295 | \-      |
+--------------------------+----------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set as-path exclude from 65000 to 65535


**Removing Configuration**

To remove set action:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set as-path exclude from

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.2    | Command introduced |
+---------+--------------------+

---

## set_as-path_exclude.rst

routing-policy policy rule set as-path exclude
----------------------------------------------

**Minimum user role:** operator

To exclude the specified as-number(s) from the as-path:

**Command syntax: set as-path exclude [as-number]** [, as-number, as-number]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- Running this command on a rule appends to the list and does not overwrite any previously configured AS number.

- Within the same route policy rule, "set as-path exclude <as-path list>" will be processed and imposed before "set as-path prepend" action.

- Can be set in the same rule with "set as-path exclude from to". All as numbers requested by the two set cmds will be removed from the as-path.

**Parameter table**

+-----------+----------------------------------------------+--------------+---------+
| Parameter | Description                                  | Range        | Default |
+===========+==============================================+==============+=========+
| as-number | The AS-number to exclude from the AS-path.   | 1-4294967295 | \-      |
|           | You can specify multiple AS numbers.         |              |         |
+-----------+----------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)#set as-path exclude 23456
    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)#set as-path exclude 12956, 23456
    dnRouter(cfg-rpl-policy-rule-20)#set as-path exclude 5000


**Removing Configuration**

To remove set action:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set as-path exclude

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 9.0     | Changed parameter's range from minimum 1     |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_as-path_prepend_as-number.rst

routing-policy policy rule set as-path prepend as-number
--------------------------------------------------------

**Minimum user role:** operator

To prepend the given string of AS number(s) to the AS-path:

**Command syntax: set as-path prepend as-number [as-number]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- This action is only relevant as a BGP policy.

- Within the same route policy rule, "set as-path exclude" will be processed and imposed before "set as-path prepend" action

**Parameter table**

+-----------+-------------------------------------------+--------------+---------+
| Parameter | Description                               | Range        | Default |
+===========+===========================================+==============+=========+
| as-number | The AS-number to repend to the AS-path.   | 1-4294967295 | \-      |
|           | You can specify multiple AS numbers.      |              |         |
+-----------+-------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set as-path prepend as-number 23456
    dnRouter(cfg-rpl-policy-rule-10)# exit

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set as-path prepend as-number 12956, 23456
    dnRouter(cfg-rpl-policy-rule-20)# exit


**Removing Configuration**

To remove a specific set-entry:
::

    dnRouter(cfg-rpl-policy-rule-20)# no set as-path prepend

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 9.0     | Changed parameter's range from minimum 1     |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_as-path_prepend_last-as.rst

routing-policy policy rule set as-path prepend last-as
------------------------------------------------------

**Minimum user role:** operator

To prepend the given string of last AS to the AS-path:

**Command syntax: set as-path prepend last-as [number]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- This action is only relevant as a BGP policy.

- Within the same route policy rule, "set as-path exclude" will be processed and imposed before "set as-path prepend" action

**Parameter table**

+-----------+-------------------------------------------------------+-------+---------+
| Parameter | Description                                           | Range | Default |
+===========+=======================================================+=======+=========+
| number    | The number of times the last as-number will be added. | 1-9   | \-      |
+-----------+-------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set as-path prepend last-as 1
    dnRouter(cfg-rpl-policy-rule-10)# exit

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set as-path prepend last-as 7
    dnRouter(cfg-rpl-policy-rule-20)# exit


**Removing Configuration**

To remove a specific set-entry:
::

    dnRouter(cfg-rpl-policy-rule-20)# no set as-path prepend

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 9.0     | Changed parameter's range from minimum 1     |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_atomic-aggregate.rst

routing-policy policy rule set atomic-aggregate
-----------------------------------------------

**Minimum user role:** operator

When applied, BGP speakers alert BGP speakers along the path that some information 
has been lost due to the route aggregation process and that the aggregate path might 
not be the best path to the destination.

To add atomic-aggregate attribute to the BGP update:

**Command syntax: set atomic-aggregate**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set atomic-aggregate


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set atomic-aggregate

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## set_community_additive.rst

routing-policy policy rule set community additive
-------------------------------------------------

**Minimum user role:** operator

Use this command to add communities for BGP updates.
When you enter multiple entries, they are collected as a list. 
You can add values to the list, and you can do this in separate commits.

To add values to the existing communities:

**Command syntax: set community additive [community]** [, community, community]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- You can set up to 25 different communities.

- The command cannot be set together with "set community-list".

- Running this command will append to whatever was previously configured.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+--------------------------------------------------------------+---------+
| Parameter | Description                                                                      | Range                                                        | Default |
+===========+==================================================================================+==============================================================+=========+
| community | The community value to set to BGP updates.                                       | | The community number (e.g. aa:nn), range (e.g. aa-bb:nn)   | \-      |
|           | The set community [community] command will replace any existing community        | | - <AS_number:ID> (AS_number:1..65535, ID:0..65535)         |         |
|           | configuration.                                                                   | | - <lower_AS_number-upper_AS_number:lower_id-upper-id>      |         |
|           |                                                                                  | | - internet                                                 |         |
|           |                                                                                  | | - accept-own                                               |         |
|           |                                                                                  | | - local-AS                                                 |         |
|           |                                                                                  | | - no-export                                                |         |
|           |                                                                                  | | - no-advertise                                             |         |
|           |                                                                                  | | - no-llgr                                                  |         |
|           |                                                                                  | | - llgr-stale                                               |         |
+-----------+----------------------------------------------------------------------------------+--------------------------------------------------------------+---------+

**Example**

To add new route communities to the existing communities:
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set community additive 65000:86, 65000:2010


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set community

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Added note for command restriction           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_community_none.rst

routing-policy policy rule set community none
---------------------------------------------

**Minimum user role:** operator

Use this command to remove communities for BGP updates.
You can remove values from the list, and you can do this in separate commits.

To remove/delete communities value to BGP updates:

**Command syntax: set community none**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- The command cannot be set together with "set community-list".

- Running one of these commands will replace whatever was previously configured.

**Example**

To delete the existing route communities (by overwriting them with 'none')
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set community none


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set community

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Added note for command restriction           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_community-list.rst

routing-policy policy rule set community-list
---------------------------------------------

**Minimum user role:** operator

Modify the communities' values of the BGP route per provided community-list and list-option.

- delete: when the communities' values of the BGP route match the communities in the community-list, the communities' values are deleted. When all the communities' values are removed, the communities' attribute of the BGP update is deleted.

- delete-not-in: when the communities' value of the BGP route DOES NOT match the communities in the community-list, the communities' values are deleted. When all the communities' values are removed, the communities' attribute of the BGP update is deleted.

- replace: replace the communities' value of the BGP route with allowed communities in the community-list.

- additive: update the communities’ value of the BGP route and append the allowed communities in the community-list.

To modify the communities' values from the BGP communities attribute using a community-list:

**Command syntax: set community-list [list-name]** [, list-name, list-name] **[list-option]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- Support well-known communities defined by name.

- The command cannot be set under same rule together with set community.

- For a replace or an additive, the attached community-list does not contain: deny rules, regex rules, and communities defined with ranges.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------+
| Parameter   | Description                                                                      | Range                                                                        | Default |
+=============+==================================================================================+==============================================================================+=========+
| list-name   | The community list against which to match the communities values of the BGP      | 1..255 characters                                                            | \-      |
|             | route                                                                            |                                                                              |         |
+-------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------+
| list-option | Instructs what to do with the communities values                                 | | delete - delete the communities value in the list                          | \-      |
|             |                                                                                  | | delete-not-in - delete communities value not matching the community-list   |         |
|             |                                                                                  | | replace - replace communities value with allowed communities in list       |         |
|             |                                                                                  | | additive - append communities with allowed communities in list             |         |
+-------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set community-list CL_INTERNAL delete

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set community-list CL2_INTERNAL delete-not-in

    dnRouter(cfg-rpl-policy)# rule 30 allow
    dnRouter(cfg-rpl-policy-rule-30)# set community-list CL2_INTERNAL replace

    dnRouter(cfg-rpl-policy)# rule 40 allow
    dnRouter(cfg-rpl-policy-rule-40)# set community-list CL2_INTERNAL additive


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set community-list

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Add replace and additive option              |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_community.rst

routing-policy policy rule set community
----------------------------------------

**Minimum user role:** operator

Use this command to set/replace communities for BGP updates.
When you enter multiple entries, they are collected as a list. 
You can set/replace values to the list, and you can do this in separate commits.

To set the specified communities value to BGP updates:

**Command syntax: set community [community]** [, community, community]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- You can set up to 25 different communities.

- The command cannot be set together with "set community-list".

- Running one of these commands will replace whatever was previously configured.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+--------------------------------------------------------------+---------+
| Parameter | Description                                                                      | Range                                                        | Default |
+===========+==================================================================================+==============================================================+=========+
| community | The community value to set to BGP updates.                                       | | The community number (e.g. aa:nn), range (e.g. aa-bb:nn)   | \-      |
|           | The set community [community] command will replace any existing community        | | - <AS_number:ID> (AS_number:1..65535, ID:0..65535)         |         |
|           | configuration.                                                                   | | - <lower_AS_number-upper_AS_number:lower_id-upper-id>      |         |
|           |                                                                                  | | - internet                                                 |         |
|           |                                                                                  | | - accept-own                                               |         |
|           |                                                                                  | | - local-AS                                                 |         |
|           |                                                                                  | | - no-export                                                |         |
|           |                                                                                  | | - no-advertise                                             |         |
|           |                                                                                  | | - no-llgr                                                  |         |
|           |                                                                                  | | - llgr-stale                                               |         |
+-----------+----------------------------------------------------------------------------------+--------------------------------------------------------------+---------+

**Example**

To overwrite the existing route communities with new communities:
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set community 65000:1918

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set community 65000:86, 65000:2010

    dnRouter(cfg-rpl-policy)# rule 30 allow
    dnRouter(cfg-rpl-policy-rule-30)# set community local-AS, 65000:2010, internet


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set community

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Added note for command restriction           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_extcommunity_color_additive.rst

routing-policy policy rule set extcommunity color additive
----------------------------------------------------------

**Minimum user role:** operator

To append color to the existing extcommunities for the matching routes:

**Command syntax: set extcommunity color additive [color-value]** [, color-value, color-value]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- By default, set will replace any existing extcommunity color value. Use additive to append the extcommunities to existing extcommunities values

- Within the same route policy rule, "set extcommunity-list" will be processed and imposed before "set extcommunity" action

- You can set up to 25 different color-values.

**Parameter table**

+-------------+----------------------------+--------------+---------+
| Parameter   | Description                | Range        | Default |
+=============+============================+==============+=========+
| color-value | Color extcommunity values. | 0-4294967295 | \-      |
+-------------+----------------------------+--------------+---------+

**Example**

To add values to the existing extcommunity color:
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set extcommunity color additive 100


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set extcommunity color additive

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 17.0    | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_extcommunity_color_none.rst

routing-policy policy rule set extcommunity color none
------------------------------------------------------

**Minimum user role:** operator

When none is specified, it removes the entire color extcommunities attribute from BGP updates.

To remove/delete extcommunity color value to BGP updates:

**Command syntax: set extcommunity color none**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- The command cannot be set together with "set extcommunity-list".

- Running one of these commands will replace whatever was previously configured.

**Example**

To delete the existing color extcommunities (by overwriting them with 'none')
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set extcommunity color none


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set extcommunity color

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+

---

## set_extcommunity_color.rst

routing-policy policy rule set extcommunity color
-------------------------------------------------

**Minimum user role:** operator

To set a color extcommunity for the matching routes:

**Command syntax: set extcommunity color [color-value]** [, color-value, color-value]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- By default, set will replace any existing extcommunity color value. Use additive to append the extcommunities to existing extcommunities values

- Within the same route policy rule, "set extcommunity-list" will be processed and imposed before "set extcommunity" action

- You can set up to 25 different color-values.

**Parameter table**

+-------------+----------------------------+--------------+---------+
| Parameter   | Description                | Range        | Default |
+=============+============================+==============+=========+
| color-value | Color extcommunity values. | 0-4294967295 | \-      |
+-------------+----------------------------+--------------+---------+

**Example**

To overwrite the existing extcommunity color with new values:
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set extcommunity color 10

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set extcommunity color 20, 30


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set extcommunity color

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 17.0    | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_extcommunity_route-target_additive.rst

routing-policy policy rule set extcommunity route-target additive
-----------------------------------------------------------------

**Minimum user role:** operator

To append route-target to the existing extcommunities for the matching routes:

**Command syntax: set extcommunity route-target additive [rt-value]** [, rt-value, rt-value]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- You can set up to 25 different route-targets.

- Within the same route policy rule, "set extcommunity-list" will be processed and imposed before "set extcommunity" action.

**Parameter table**

+-----------+-------------------------------------------------------------------+---------------------------------------------------------------------------------+---------+
| Parameter | Description                                                       | Range                                                                           | Default |
+===========+===================================================================+=================================================================================+=========+
| rt-value  | The route-target value to set for matching routes.                | | as-number-short: 0…(2^16 -1)                                                  | \-      |
|           | Type0:                                                            | | as-number-long: (2^16)…(2^32 -1)                                              |         |
|           | <[as-number-short]:[id-long]>                                     | | id-short: 0…(2^16 -1)                                                         |         |
|           | Type1:                                                            | | id-long: 0…(2^32 -1)                                                          |         |
|           | <[as-number-short]l:[id-short]>                                   | | ipv4-address-prefix: A.B.C.D                                                  |         |
|           | <[as-number-short]L:[id-short]>                                   | |                                                                               |         |
|           | <[as-number-long]:[id-short]>                                     | | Note:                                                                         |         |
|           | Type2:                                                            | | - Using [as-number-short]l or [as-number-short]L will code as-number-short    |         |
|           | <[ipv4-address-prefix]:[id-short]>                                | | number in a 32-bit field resulting in a Type1 route-distinguisher.            |         |
|           | You can set multiple route-target values, separated by a comma.   |                                                                                 |         |
+-----------+-------------------------------------------------------------------+---------------------------------------------------------------------------------+---------+

**Example**

To add values to the existing extcommunity route-target:
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set extcommunity route-target additive 65000:1000, 65000:2000


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set extcommunity route-target additive

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 11.4    | Added 'additive' option                      |
+---------+----------------------------------------------+
| 18.2    | Added note for command restriction           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_extcommunity_route-target_none.rst

routing-policy policy rule set extcommunity route-target none
-------------------------------------------------------------

**Minimum user role:** operator

When none is specified, it removes the entire RT extcommunities attribute from BGP updates.

To remove/delete extcommunity route-target value to BGP updates:

**Command syntax: set extcommunity route-target none**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- The command cannot be set together with "set extcommunity-list".

- Running one of these commands will replace whatever was previously configured.

**Example**

To delete the existing route-target communities (by overwriting them with 'none')
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set extcommunity route-target none


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set extcommunity route-target

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+

---

## set_extcommunity_route-target.rst

routing-policy policy rule set extcommunity route-target
--------------------------------------------------------

**Minimum user role:** operator

To set a route-target for the matching routes:

**Command syntax: set extcommunity route-target [rt-value]** [, rt-value, rt-value]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- You can set up to 25 different route-targets.

- Within the same route policy rule, "set extcommunity-list" will be processed and imposed before "set extcommunity" action.

**Parameter table**

+-----------+-------------------------------------------------------------------+---------------------------------------------------------------------------------+---------+
| Parameter | Description                                                       | Range                                                                           | Default |
+===========+===================================================================+=================================================================================+=========+
| rt-value  | The route-target value to set for matching routes.                | | as-number-short: 0…(2^16 -1)                                                  | \-      |
|           | Type0:                                                            | | as-number-long: (2^16)…(2^32 -1)                                              |         |
|           | <[as-number-short]:[id-long]>                                     | | id-short: 0…(2^16 -1)                                                         |         |
|           | Type1:                                                            | | id-long: 0…(2^32 -1)                                                          |         |
|           | <[as-number-short]l:[id-short]>                                   | | ipv4-address-prefix: A.B.C.D                                                  |         |
|           | <[as-number-short]L:[id-short]>                                   | |                                                                               |         |
|           | <[as-number-long]:[id-short]>                                     | | Note:                                                                         |         |
|           | Type2:                                                            | | - Using [as-number-short]l or [as-number-short]L will code as-number-short    |         |
|           | <[ipv4-address-prefix]:[id-short]>                                | | number in a 32-bit field resulting in a Type1 route-distinguisher.            |         |
|           | You can set multiple route-target values, separated by a comma.   |                                                                                 |         |
+-----------+-------------------------------------------------------------------+---------------------------------------------------------------------------------+---------+

**Example**

To overwrite the existing extcommunity route-target with new values:
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set extcommunity route-target 65000:1000

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set extcommunity route-target 65000:1000, 65000:2000


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set extcommunity route-target

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Added note for command restriction           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_extcommunity_soo_additive.rst

routing-policy policy rule set extcommunity soo additive
--------------------------------------------------------

**Minimum user role:** operator

To append source-of-origin(soo) to the existing extcommunities for the matching routes:

**Command syntax: set extcommunity soo additive [extcommunities-additive]** [, extcommunities-additive, extcommunities-additive]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**
 - When setting an extcommunity for Type-1, an L is appended to the AS-number value.

 - Within the same route policy rule, "set extcommunity-list" will be processed and imposed before "set extcommunity" action.

 - You can set up to 25 different soo-values.

 - BGP site of origin (SoO) is a tag that is appended on BGP updates to allow to mark a specific peer as belonging to a particular site. By tagging the route, BGP will check if the peer's site of origin is listed in the community field. If it is then the route will be filtered. If not, then the route will be advertised as normal.

 - You can set multiple soo values, separated by a comma.

 - Using [as-number-short]l or [as-number-short]L will code as-number-short

 - number in a 32-bit field resulting in a Type1 route-distinguisher.

 **Parameter table**

 +-------------------+--------------------------------------------------------+-------------------------------------+-------------+
 | Parameter         | Description                                            | Range                               | Default     |
 +===================+========================================================+=====================================+=============+
 | type0             | <[as-number-short]:[id-long]>                          | as-number-short: 0…65535            |             |
 +-------------------+--------------------------------------------------------+-------------------------------------+-------------+
 | type1             | <[as-number-short]l:[id-short]>                        | as-number-long: (2^16)…4294967295   |             |
 +                   +--------------------------------------------------------+-------------------------------------+-------------+
 |                   | <[as-number-short]L:[id-short]>                        | id-short: 0…65535                   |             |
 +                   +--------------------------------------------------------+-------------------------------------+-------------+
 |                   | <[as-number-long]:[id-short]>                          | id-long: 0…4294967295               |             |
 +-------------------+--------------------------------------------------------+-------------------------------------+-------------+
 | type2             | <[ipv4-address-prefix]:[id-short]>                     | ipv4-address-prefix: A.B.C.D        |             |
 +-------------------+--------------------------------------------------------+-------------------------------------+-------------+
 

**Parameter table**

+-------------------------+------------------------------------------------------------------+-------+---------+
| Parameter               | Description                                                      | Range | Default |
+=========================+==================================================================+=======+=========+
| extcommunities-additive | extcommunities values, to be added ontop existing extcommunities | \-    | \-      |
+-------------------------+------------------------------------------------------------------+-------+---------+

**Example**

To add values to the existing extcommunity soo:
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set extcommunity soo additive 10:1100, 100:100


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set extcommunity soo additive

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 11.4    | Added 'additive' option                      |
+---------+----------------------------------------------+
| 18.2    | Added note for command restriction           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_extcommunity_soo_none.rst

routing-policy policy rule set extcommunity soo none
----------------------------------------------------

**Minimum user role:** operator

When none is specified, it removes the entire SOO extcommunities attribute from BGP updates.

To remove/delete extcommunity soo value to BGP updates:

**Command syntax: set extcommunity soo none**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- The command cannot be set together with "set extcommunity-list".

- Running one of these commands will replace whatever was previously configured.

**Example**

To delete the existing soo extcommunities (by overwriting them with 'none')
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set extcommunity soo none


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set extcommunity soo

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+

---

## set_extcommunity_soo.rst

routing-policy policy rule set extcommunity soo
-----------------------------------------------

**Minimum user role:** operator

To set a source-of-origin(soo) for the matching routes:

**Command syntax: set extcommunity soo [extcommunities]** [, extcommunities, extcommunities]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**
 - When setting an extcommunity for Type-1, an L is appended to the AS-number value.

 - Within the same route policy rule, "set extcommunity-list" will be processed and imposed before "set extcommunity" action.

 - You can set up to 25 different soo-values.

 - BGP site of origin (SoO) is a tag that is appended on BGP updates to allow to mark a specific peer as belonging to a particular site. By tagging the route, BGP will check if the peer's site of origin is listed in the community field. If it is then the route will be filtered. If not, then the route will be advertised as normal.

 - You can set multiple soo values, separated by a comma.

 - Using [as-number-short]l or [as-number-short]L will code as-number-short

 - number in a 32-bit field resulting in a Type1 route-distinguisher.

 **Parameter table**

 +-------------------+--------------------------------------------------------+-------------------------------------+-------------+
 | Parameter         | Description                                            | Range                               | Default     |
 +===================+========================================================+=====================================+=============+
 | type0             | <[as-number-short]:[id-long]>                          | as-number-short: 0…65535            |             |
 +-------------------+--------------------------------------------------------+-------------------------------------+-------------+
 | type1             | <[as-number-short]l:[id-short]>                        | as-number-long: (2^16)…4294967295   |             |
 +                   +--------------------------------------------------------+-------------------------------------+-------------+
 |                   | <[as-number-short]L:[id-short]>                        | id-short: 0…65535                   |             |
 +                   +--------------------------------------------------------+-------------------------------------+-------------+
 |                   | <[as-number-long]:[id-short]>                          | id-long: 0…4294967295               |             |
 +-------------------+--------------------------------------------------------+-------------------------------------+-------------+
 | type2             | <[ipv4-address-prefix]:[id-short]>                     | ipv4-address-prefix: A.B.C.D        |             |
 +-------------------+--------------------------------------------------------+-------------------------------------+-------------+
 

**Parameter table**

+----------------+-----------------------+-------+---------+
| Parameter      | Description           | Range | Default |
+================+=======================+=======+=========+
| extcommunities | extcommunities values | \-    | \-      |
+----------------+-----------------------+-------+---------+

**Example**

To overwrite the existing extcommunity soo with new values:
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set extcommunity soo 10:1100

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set extcommunity soo 10:1100, 40:2300


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set extcommunity soo

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Added note for command restriction           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_extcommunity-list.rst

routing-policy policy rule set extcommunity-list
------------------------------------------------

**Minimum user role:** operator

Modify the extcommunities' values of the BGP route per provided extcommunity-list and the list-option.

- delete: when the extcommunities' values of the BGP route match the extcommunities in the extcommunity-list, the extcommunities' values are deleted. When all the extcommunities' values are removed, the extcommunities' attribute of the BGP update is deleted.

- delete-not-in: when the extcommunities' values of the BGP route DO NOT match the extcommunities in the extcommunity-list, the extcommunities' values are deleted. When all the extommunities' values are removed, the extcommunities' attribute of the BGP update is deleted.

- replace: replace the extcommunities' value of the BGP route with allowed extcommunities in the extcommunity-list.

- additive: update the extcommunities' value of the BGP route and append the allowed extcommunities in the extcommunity-list.

To modify the extcommunities value from the BGP extcommunities attribute using a extcommunity-list:

**Command syntax: set extcommunity-list [list-name]** [, list-name, list-name] **[list-option]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- Expected extcommunity modification will be per modification action {additive | replace} and types of extcommunities specified in the list (color, rt, soo) i.e:

- - replace: for a given type (color, rt, soo) specified in list, replace all extcommunities of same type with the extcommunities matching that type (other extcommunities type are not effected).

- - additive: add the allowed extcommunities in list.

- Within the same route policy rule, "set extcommunity-list" will be processed and imposed before "set extcommunity" action.

- For a replace or an additive, the attached extcommunity-list does not contain: deny rules, regex rules, and extcommunities defined with ranges.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------+
| Parameter   | Description                                                                      | Range                                                                        | Default |
+=============+==================================================================================+==============================================================================+=========+
| list-name   | The extended-community list against which to match the extcommunities values of  | | string                                                                     | \-      |
|             | the BGP route.                                                                   | | length 1-255                                                               |         |
+-------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------+
| list-option | Instructs what to do with the extcommunities values                              | | delete - delete the communities value in the list                          | \-      |
|             |                                                                                  | | delete-not-in - delete communities value not matching the community-list   |         |
|             |                                                                                  | | replace - replace communities value with allowed communities in list       |         |
|             |                                                                                  | | additive - append communities with allowed communities in list             |         |
+-------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set extcommunity-list CL_INTERNAL delete

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set extcommunity-list CL2_INTERNAL delete-not-in

    dnRouter(cfg-rpl-policy)# rule 30 allow
    dnRouter(cfg-rpl-policy-rule-30)# set extcommunity-list CL2_INTERNAL replace

    dnRouter(cfg-rpl-policy)# rule 40 allow
    dnRouter(cfg-rpl-policy-rule-40)# set extcommunity-list CL2_INTERNAL additive


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set extcommunity-list

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 6.0     | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Add replace and additive option              |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_forwarding-action.rst

routing-policy policy rule set forwarding-action urpf-check ignore
------------------------------------------------------------------

**Minimum user role:** operator

This command causes the system to ignore URPF check decision:

**Command syntax: set forwarding-action urpf-check ignore**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set forwarding-action urpf-check ignore


**Removing Configuration**

To remove a specific set-entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set forwarding-action urpf-check ignore

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## set_ipv4_next-hop.rst

routing-policy policy rule set ipv4 next-hop
--------------------------------------------

**Minimum user role:** operator

To set the IPv4 next hop address:

**Command syntax: set ipv4 next-hop [option]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+------------------------------------------------------------------+--------------------+---------+
| Parameter | Description                                                      | Range              | Default |
+===========+==================================================================+====================+=========+
| option    | | - The BGP neighbor IPv4 address to set as the next-hop.        | | - A.B.C.D        | \-      |
|           | | - Set next-hop to local speaker address for outbound policy.   | | - self           |         |
|           | | - Set next-hop to local speaker address for outbound policy    | | - self-force     |         |
|           | |   even when acting as route-reflector.                         | |                  |         |
|           | | - Set next-hop to remote speaker address for inbound policy.   | | - peer-address   |         |
+-----------+------------------------------------------------------------------+--------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set ipv4 next-hop 192.0.2.1

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set ipv4 next-hop self

    dnRouter(cfg-rpl-policy)# rule 40 allow
    dnRouter(cfg-rpl-policy-rule-40)# set ipv4 next-hop self-force

    dnRouter(cfg-rpl-policy)# rule 50 allow
    dnRouter(cfg-rpl-policy-rule-50)# set ipv4 next-hop peer-address


**Removing Configuration**

To remove a set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set ipv4 next-hop

**Command History**

+---------+---------------------------+
| Release | Modification              |
+=========+===========================+
| 6.0     | Command introduced        |
+---------+---------------------------+
| 17.1    | Added self option         |
+---------+---------------------------+
| 17.1    | Added peer-address option |
+---------+---------------------------+

---

## set_ipv6_next-hop.rst

routing-policy policy rule set ipv6 next-hop
--------------------------------------------

**Minimum user role:** operator

To set the next hop to the BGP neighbor IPv6 address:

**Command syntax: set ipv6 next-hop [option]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+------------------------------------------------------------------+--------------------+---------+
| Parameter | Description                                                      | Range              | Default |
+===========+==================================================================+====================+=========+
| option    | | - The BGP neighbor IPv6 address to set as the next-hop.        | | - xx:xx::xx:xx   | \-      |
|           | | - Set next-hop to local speaker address for outbound policy.   | | - self           |         |
|           | | - Set next-hop to local speaker address for outbound policy    | | - self-force     |         |
|           | |   even when acting as route-reflector.                         | |                  |         |
|           | | - Set next-hop to remote speaker address for inbound policy.   | | - peer-address   |         |
+-----------+------------------------------------------------------------------+--------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set ipv6 next-hop ::ffff:192.0.2.1

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set ipv6 next-hop self

    dnRouter(cfg-rpl-policy)# rule 40 allow
    dnRouter(cfg-rpl-policy-rule-40)# set ipv6 next-hop self-force

    dnRouter(cfg-rpl-policy)# rule 50 allow
    dnRouter(cfg-rpl-policy-rule-50)# set ipv6 next-hop peer-address


**Removing Configuration**

To remove a set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set ipv6 next-hop

**Command History**

+---------+---------------------------+
| Release | Modification              |
+=========+===========================+
| 6.0     | Command introduced        |
+---------+---------------------------+
| 17.1    | Added self option         |
+---------+---------------------------+
| 17.1    | Added peer-address option |
+---------+---------------------------+

---

## set_isis-metric.rst

routing-policy policy rule set isis-metric
------------------------------------------

**Minimum user role:** operator

To set an IS-IS metric value:

**Command syntax: set isis-metric [metric]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- The default metric-type is "internal".

**Parameter table**

+-----------+-----------------------------------------------------+------------+---------+
| Parameter | Description                                         | Range      | Default |
+===========+=====================================================+============+=========+
| metric    | The new value of the IS-IS metric that will be set. | 1-16777215 | \-      |
+-----------+-----------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set isis-metric 20


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set isis-metric

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 10.0    | Command introduced |
+---------+--------------------+

---

## set_large_community_additive.rst

routing-policy policy rule set large-community additive
-------------------------------------------------------

**Minimum user role:** operator

Use this command to add large-communities for BGP updates.
When you enter multiple entries, they are collected as a list.
You can add values to the list, and you can do this in separate commits.

To add values to the existing large-communities:

**Command syntax: set large-community additive [large-community]** [, large-community, large-community]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- You can set up to 25 large-communities

- Within the same route policy rule, "set large-community-list" will be processed and imposed before "set large-community" action.

**Parameter table**

+-----------------+---------------------------------------------------+--------------------------------+---------+
| Parameter       | Description                                       | Range                          | Default |
+=================+===================================================+================================+=========+
| large-community | The large-community values to set for BGP updates | | <AS_number:ID-1:ID-2>:       | \-      |
|                 |                                                   | | - AS_number: 0..4294967295   |         |
|                 |                                                   | | - ID-1: 0..4294967295        |         |
|                 |                                                   | | - ID-2: 0..4294967295        |         |
+-----------------+---------------------------------------------------+--------------------------------+---------+

**Example**

To add new route communities to the existing communities:
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set large-community additive 65000:86:1, 65000:2010:2


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set large-community

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 15.1    | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Added note for command restriction           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_large_community_none.rst

routing-policy policy rule set large-community none
---------------------------------------------------

**Minimum user role:** operator

Use this command to remove large-communities for BGP updates.
You can remove values from the list, and you can do this in separate commits.

To remove/delete large-communities values to BGP updates:

**Command syntax: set large-community none**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- Within the same route policy rule, "set large-community-list" will be processed and imposed before "set large-community" action.

**Example**

To delete the existing route large-communities (by overwriting them with 'none')
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set large-community none


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set large-community

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 15.1    | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Added note for command restriction           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_large_community.rst

routing-policy policy rule set large-community
----------------------------------------------

**Minimum user role:** operator

Use this command to set/replace large-communities for BGP updates.
When you enter multiple entries, they are collected as a list.
You can set/replace values to the list, and you can do this in separate commits.

To set the specified large-communities values to BGP updates:

**Command syntax: set large-community [large-community]** [, large-community, large-community]

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- You can set up to 25 large-communities.

- Within the same route policy rule, "set large-community-list" will be processed and imposed before "set large-community" action.

**Parameter table**

+-----------------+---------------------------------------------------+--------------------------------+---------+
| Parameter       | Description                                       | Range                          | Default |
+=================+===================================================+================================+=========+
| large-community | The large-community values to set for BGP updates | | <AS_number:ID-1:ID-2>:       | \-      |
|                 |                                                   | | - AS_number: 0..4294967295   |         |
|                 |                                                   | | - ID-1: 0..4294967295        |         |
|                 |                                                   | | - ID-2: 0..4294967295        |         |
+-----------------+---------------------------------------------------+--------------------------------+---------+

**Example**

To overwrite the existing route large-communities with new large-communities:
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set large-community 15562:45:29

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set large-community 15562:45:29, 15562:45:50


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set large-community

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 15.1    | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Added note for command restriction           |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_large-community-list.rst

routing-policy policy rule set large-community-list
---------------------------------------------------

**Minimum user role:** operator

Modify the large-communities values of the BGP route per provided large-community-list and list-option.

- delete: When the large-communities value of the BGP route matches the large-communities in the large-ommunity-list, the large-ommunities value are deleted. When all the large-communities values are removed, the large-communities attribute of the BGP update is deleted.

- delete-not-in: When the large-communities value of the BGP route DOES NOT matche the large-communities in the large-community-list, the large-communities value are deleted. When all the large-communities values are removed, the large-communities attribute of the BGP update is deleted.

- replace: replace the large-communities value of the BGP route with allowed large-communities in the large-community-list.

- additive: update the large-communities value of the BGP route and append the allowed large-communities in the large-community-list.

To modify the large-communities value from the BGP large-communities attribute using a large-ommunity-list:

**Command syntax: set large-community-list [list-name]** [, list-name, list-name] **[list-option]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- Within the same route policy rule, "set large-community-list" will be processed and imposed before "set large-community" action.

- For a replace or an additive, the attached large-community-list does not contain: deny rules, regex rules, and communities defined with ranges.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------+
| Parameter   | Description                                                                      | Range                                                                        | Default |
+=============+==================================================================================+==============================================================================+=========+
| list-name   | The large-community list against which to match the communities value of the BGP | | string                                                                     | \-      |
|             | route                                                                            | | length 1-255                                                               |         |
+-------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------+
| list-option | Instructs what to do with the large-communities value                            | | delete - delete the communities value in the list                          | \-      |
|             |                                                                                  | | delete-not-in - delete communities value not matching the community-list   |         |
|             |                                                                                  | | replace - replace communities value with allowed communities in list       |         |
|             |                                                                                  | | additive - append communities with allowed communities in list             |         |
+-------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set large-community-list CL_INTERNAL delete

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set large-community-list CL2_INTERNAL delete-not-in

    dnRouter(cfg-rpl-policy)# rule 30 allow
    dnRouter(cfg-rpl-policy-rule-30)# set large-community-list CL2_INTERNAL replace

    dnRouter(cfg-rpl-policy)# rule 40 allow
    dnRouter(cfg-rpl-policy-rule-40)# set large-community-list CL2_INTERNAL additive


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set large-community-list

**Command History**

+---------+----------------------------------------------+
| Release | Modification                                 |
+=========+==============================================+
| 15.1    | Command introduced                           |
+---------+----------------------------------------------+
| 18.2    | Add replace and additive option              |
+---------+----------------------------------------------+
| 18.2    | Impose action order within route policy rule |
+---------+----------------------------------------------+

---

## set_local_preference_aigp_relative.rst

routing-policy policy rule set local-preference aigp
----------------------------------------------------

**Minimum user role:** operator

AIGP (Accumulated IGP Metric) is a BGP attribute designed to enhance path selection in networks that span over multiple ASs. It allows BGP to propagate and consider IGP metric across multiple autonomous system, ensuring routing decisions are consistent with the internal network's shortest-path metrics.
In some cases, legacy devices do not support AIGP, or in some cases (like the case in hand) an operator would like to avoid introducing new configuration on legacy networks, in such case, the operator may decide to copy the AIGP value into the Local-Preference value when routes are advertised in a legacy AS, this way the legacy AS devices will select per route the ASBR that can provide the shortest path.
Updating Local-Preference by inbound policy may influence local best-path selection.
If no aigp value known, no update to local-preference.

To update Local-Preference value according to offset from known AIGP value by route policy set action:

**Command syntax: set local-preference aigp [relative-aigp] [aigp-offset-value]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-------------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter         | Description                                                                      | Range        | Default |
+===================+==================================================================================+==============+=========+
| relative-aigp     | Sets the desired relative modification (add/substract) for the aigp value. The   | | +          | \-      |
|                   | resulting Local-Preference value must be between 0..4294967295.                  | | -          |         |
+-------------------+----------------------------------------------------------------------------------+--------------+---------+
| aigp-offset-value | Sets an offset for the aigp metric value to be set into Local-Preference.        | 0-4294967295 | \-      |
+-------------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy SET_LOCAL_PREF_AIGP
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set local-preference aigp + 10

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set local-preference aigp - 5


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set local-preference

To remove aigp configuration:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set local-preference aigp

To remove specific aigp configuration:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set local-preference aigp + 10

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| TBD     | Command introduced |
+---------+--------------------+

---

## set_local_preference_aigp.rst

routing-policy policy rule set local-preference aigp
----------------------------------------------------

**Minimum user role:** operator

AIGP (Accumulated IGP Metric) is a BGP attribute designed to enhance path selection in networks that span over multiple ASs. It allows BGP to propagate and consider IGP metric across multiple autonomous system, ensuring routing decisions are consistent with the internal network's shortest-path metrics.
In some cases, legacy devices do not support AIGP, or in some cases  (like the case in hand) an operator would like to avoid introducing new configuration on legacy networks, in such case, the operator may decide to copy the AIGP value into the Local-Preference value when routes are advertised in a legacy AS, this way the legacy AS devices will select per route the ASBR that can provide the shortest path.
Updating Local-Preference by inbound policy may influence local best-path selection
If no aigp value known , no update to local-preference

To update Local-Preference value according to known AIGP value by route policy set action:

**Command syntax: set local-preference aigp**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set local-preference aigp


**Removing Configuration**

To remove set local-preference aigp action:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set local-preference aigp

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+

---

## set_local_preference.rst

routing-policy policy rule set local-preference
-----------------------------------------------

**Minimum user role:** operator

Routers in the same AS exchange the local preference attribute in order to indicate to the AS which path is preferred for exiting the AS and reaching a specific network. A path with a higher local preference is preferred more. 

To set a preference value for the BGP local preference:

**Command syntax: set local-preference [metric]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+---------------------------------------------+--------------+---------+
| Parameter | Description                                 | Range        | Default |
+===========+=============================================+==============+=========+
| metric    | Set the local preference value for the path | 0-4294967295 | \-      |
+-----------+---------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set local-preference 90


**Removing Configuration**

To remove set local-preference action:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set local-preference

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## set_local-preference.rst

routing-policy policy rule set local-preference
-----------------------------------------------

**Minimum user role:** operator

Routers in the same AS exchange the local preference attribute in order to indicate to the AS 
which path is preferred for exiting the AS and reaching a specific network. A path with a higher 
local preference is preferred more.

To set a preference value for the BGP local preference:

**Command syntax: set local-preference [metric]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+-----------------------------------+--------------+---------+
| Parameter | Description                       | Range        | Default |
+===========+===================================+==============+=========+
| metric    | Sets a new local preference value | 0-4294967295 | \-      |
+-----------+-----------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set local-preference 90


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set local-preference

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## set_med_aigp_relative.rst

routing-policy policy rule set med aigp
---------------------------------------

**Minimum user role:** operator

AIGP (Accumulated IGP Metric) is a BGP attribute designed to enhance path selection in networks that span over multiple ASs. It allows BGP to propagate and consider IGP metric across multiple autonomous system, ensuring routing decisions are consistent with the internal network's shortest-path metrics.
In some cases, legacy devices do not support AIGP, or in some cases (like the case in hand) an operator would like to avoid introducing new configuration on legacy networks, in such case, the operator may decide to copy the AIGP value into the MED value when routes are advertised to a legacy AS, this way the legacy AS devices will select per route the ASBR that can provide the shortest path.
The downside of such solution is that the path to the ASBR is not taken into consideration when selecting the best path

To update MED value according to offset from known AIGP value by route policy set action:

**Command syntax: set med aigp [relative-aigp] [aigp-offset-value]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-------------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter         | Description                                                                      | Range        | Default |
+===================+==================================================================================+==============+=========+
| relative-aigp     | Sets the desired relative modification (add/substract) for the aigp value. The   | | +          | \-      |
|                   | resulting MED value must be between 0..4294967295.                               | | -          |         |
+-------------------+----------------------------------------------------------------------------------+--------------+---------+
| aigp-offset-value | Sets an offset for the aigp metric value to be set into MED.                     | 0-4294967295 | \-      |
+-------------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy SET_MED_AIGP
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set med aigp + 10

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set med aigp - 5


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set med

To remove aigp configuration:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set med aigp

To remove specific aigp configuration:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set med aigp + 10

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| TBD     | Command introduced |
+---------+--------------------+

---

## set_med_aigp.rst

routing-policy policy rule set med aigp
---------------------------------------

**Minimum user role:** operator

AIGP (Accumulated IGP Metric) is a BGP attribute designed to enhance path selection in networks that span over multiple ASs. It allows BGP to propagate and consider IGP metric across multiple autonomous system, ensuring routing decisions are consistent with the internal network's shortest-path metrics.
in some cases, legacy devices do not support AIGP, or in some cases  (like the case in hand) an operator would like to avoid introducing new configuration on legacy networks, in such case, the operator may decide to copy the AIGP value into the MED value when routes are advertised to a legacy AS, this way the legacy AS devices will select per route the ASBR that can provide the shortest path.
the downside of such solution, is that the path to the ASBR is not taken into consideration when selecting the best path

To update MED value according to known AIGP value by route policy set action:

**Command syntax: set med aigp**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set med aigp


**Removing Configuration**

To remove set med aigp action:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set med aigp

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+

---

## set_med_igp-cost.rst

routing-policy policy rule set med igp-cost
-------------------------------------------

**Minimum user role:** operator

Set the MED value to be the metric towards the route bgp next-hop. Usage of igp-cost is only applicable for policy out.

To set the BGP attribute MED:

**Command syntax: set med igp-cost**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set med igp-cost


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set med

**Command History**

+---------+-------------------------------+
| Release | Modification                  |
+=========+===============================+
| 6.0     | Command introduced            |
+---------+-------------------------------+
| 15.2    | 'igp-cost' options were added |
+---------+-------------------------------+

---

## set_med_relative.rst

routing-policy policy rule set med
----------------------------------

**Minimum user role:** operator

To set the BGP attribute MED:

**Command syntax: set med [relative] [med-offset-value]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+------------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter        | Description                                                                      | Range        | Default |
+==================+==================================================================================+==============+=========+
| relative         | Increases or decreases the route's existing MED value by the configured          | | +          | \-      |
|                  | med-value.                                                                       | | -          |         |
|                  | The resulting MED value must be between 0-4294967295.                            |              |         |
+------------------+----------------------------------------------------------------------------------+--------------+---------+
| med-offset-value | Sets a new multi-exit discriminator for best path selection.                     | 0-4294967295 | \-      |
+------------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set med + 30

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set med - 5


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set med

**Command History**

+---------+-------------------------------+
| Release | Modification                  |
+=========+===============================+
| 6.0     | Command introduced            |
+---------+-------------------------------+
| 15.2    | 'relative' options were added |
+---------+-------------------------------+

---

## set_med_value.rst

routing-policy policy rule set med
----------------------------------

**Minimum user role:** operator

To set the BGP attribute MED:

**Command syntax: set med [med-value]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+--------------------------------------------------------------+--------------+---------+
| Parameter | Description                                                  | Range        | Default |
+===========+==============================================================+==============+=========+
| med-value | Sets a new multi-exit discriminator for best path selection. | 0-4294967295 | \-      |
+-----------+--------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set med 500


**Removing Configuration**

To remove the set entry
::

    dnRouter(cfg-rpl-policy-rule-10)# no set med

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## set_metric-type.rst

routing-policy policy rule set metric-type
------------------------------------------

**Minimum user role:** operator

You can use the following command to set the metric type for OSPFv2/OSPFv3:

**Command syntax: set metric-type [type]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+------------------------------------+------------+---------+
| Parameter | Description                        | Range      | Default |
+===========+====================================+============+=========+
| type      | Sets new metric-type for OSPFv2/3  | | type-1   | \-      |
|           |                                    | | type-2   |         |
+-----------+------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set metric-type type-1


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set metric-type

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.6    | Command introduced |
+---------+--------------------+

---

## set_nhc-entropy-label.rst

routing-policy policy rule set nhc-entropy-label
------------------------------------------------

**Minimum user role:** operator

When set on a given BGP route path nhc-entropy-label disabled, it is required to remove the request for an entropy label. Applicable for ipv4-unicast labeled-unicast and ipv6-unicast labeled-unicast address families.

**Command syntax: set nhc-entropy-label [nhc-entropy-label]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-------------------+---------------------------+----------+---------+
| Parameter         | Description               | Range    | Default |
+===================+===========================+==========+=========+
| nhc-entropy-label | Set the nhc entropy-label | disabled | \-      |
+-------------------+---------------------------+----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set nhc-entropy-label disabled


**Removing Configuration**

To remove set protocols criteria:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set nhc-entropy-label

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.2    | Command introduced |
+---------+--------------------+

---

## set_origin.rst

routing-policy policy rule set origin
-------------------------------------

**Minimum user role:** operator

To set the BGP attribute origin-type:

**Command syntax: set origin [type]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+----------------------------------------+----------------+---------+
| Parameter | Description                            | Range          | Default |
+===========+========================================+================+=========+
| type      | Set the origin of the path information | | igp          | \-      |
|           |                                        | | egp          |         |
|           |                                        | | incomplete   |         |
+-----------+----------------------------------------+----------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set origin igp

    dnRouter(cfg-rpl-policy)# rule 20 allow
    dnRouter(cfg-rpl-policy-rule-20)# set origin egp

    dnRouter(cfg-rpl-policy)# rule 30 allow
    dnRouter(cfg-rpl-policy-rule-30)# set origin incomplete


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set origin

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 13.1    | Command introduced |
+---------+--------------------+

---

## set_ospf-metric.rst

routing-policy policy rule set ospf-metric
------------------------------------------

**Minimum user role:** operator

You can use the following command to set the OSPFv2/OSPFv3 metric value:

**Command syntax: set ospf-metric [metric]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+----------------------------------------+------------+---------+
| Parameter | Description                            | Range      | Default |
+===========+========================================+============+=========+
| metric    | Sets the new metric value for OSPFv2/3 | 0-16777215 | \-      |
+-----------+----------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set ospf-metric 33


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set ospf-metric

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 11.6    | Command introduced |
+---------+--------------------+

---

## set_path-mark.rst

routing-policy policy rule set path-mark
----------------------------------------

**Minimum user role:** operator

This command adds a DNOS internal "path-mark" attribute to the route. This provides a means 
for the BGP ingress policy to count the number of peers from which a certain prefix is learned, 
regardless of whether or not it is the best path. This information can then be used to take action 
on the egress routing policy (e.g. change the local preference attribute when a prefix is learned 
from more than a specific number of peers (see "policy match path-mark-count") so that when the 
number drops below this value, due to link failure or for any other reason, the egress policy 
would change the local preference attribute). This capability is useful to allow downstream BGP peers 
to decide what next-hop to use.

The path-mark attribute is not advertised in BGP.

The path-mark attributes is per prefix. When set as an ingress policy from multiple BGP neighbors, 
multiple path-marks will be set.

To add the path-mark attribute:

**Command syntax: set path-mark**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- To view the path-mark attribute, use the "show bgp" commands.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set path-mark


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set path-mark

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 13.0    | Command introduced |
+---------+--------------------+

---

## set_qppb-dest-class.rst

routing-policy policy rule set qppb-dest-class
----------------------------------------------

**Minimum user role:** operator

To set the Destination Class value for routes that match the match-criteria.

**Command syntax: set qppb-dest-class [qppb-dest-class]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------------+-------------------------------+-------+---------+
| Parameter       | Description                   | Range | Default |
+=================+===============================+=======+=========+
| qppb-dest-class | The QPPB Destination Class Id | 1-128 | \-      |
+-----------------+-------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set qppb-dest-class 25

    dnRouter(cfg-rpl-policy-rule-20)# match community COMMUNITY_LIST_1
    dnRouter(cfg-rpl-policy-rule-10)# set qppb-dest-class 30


**Removing Configuration**

To remove set action:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set qppb-dest-class

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## set_qppb-src-class.rst

routing-policy policy rule set qppb-src-class
---------------------------------------------

**Minimum user role:** operator

To set the Source Class value for routes that match the match-criteria.

**Command syntax: set qppb-src-class [qppb-src-class]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+----------------+--------------------------+-------+---------+
| Parameter      | Description              | Range | Default |
+================+==========================+=======+=========+
| qppb-src-class | The QPPB Source Class Id | 1-128 | \-      |
+----------------+--------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set qppb-src-class 25

    dnRouter(cfg-rpl-policy-rule-20)# match community COMMUNITY_LIST_1
    dnRouter(cfg-rpl-policy-rule-10)# set qppb-src-class 30


**Removing Configuration**

To remove set action:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set qppb-src-class

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## set_resolve-nexthop-in.rst

routing-policy policy rule set resolve-nexthop-in
-------------------------------------------------

**Minimum user role:** operator

When set on a given BGP route path. It is required to resolve the path nexthop in a specific VRF RIB table.

**Command syntax: set resolve-nexthop-in [vrf-name]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+-------------------------------------------------------------+------------------+---------+
| Parameter | Description                                                 | Range            | Default |
+===========+=============================================================+==================+=========+
| vrf-name  | Require to resolve path nexthop in a specific vrf rib table | | string         | \-      |
|           |                                                             | | length 1-255   |         |
+-----------+-------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set resolve-nexthop-in VRF_A


**Removing Configuration**

To remove set protocols criteria:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set resolve-nexthop-in

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## set_rpki.rst

routing-policy policy rule set rpki
-----------------------------------

**Minimum user role:** operator

To set the RPKI state in announcements enabled towards iBGP peers:

**Command syntax: set rpki [rpki-state]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Note**

- The rpki state will affect BGP neighbors for which announce rpki-state is set and as long as extended community is enabled.

**Parameter table**

+------------+---------------------------+---------------+---------+
| Parameter  | Description               | Range         | Default |
+============+===========================+===============+=========+
| rpki-state | The rpki validation state | | valid       | \-      |
|            |                           | | invalid     |         |
|            |                           | | not-found   |         |
+------------+---------------------------+---------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set rpki not-found


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set rpki

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+

---

## set_sr-label-index.rst

routing-policy policy rule set sr-label-index
---------------------------------------------

**Minimum user role:** operator

Add Prefix-SID attribute to the matched prefix.
Prefix-SID attribute will include the Label-Index TLV with index value as set by user
Prefix-SID attribute will only be sent for IPv4/IPv6 Labeled Unicast prefixes
For a given prefix, if Prefix-SID attribute & Label-Index TLV exist and prefix-sid feature is enabled, bgp will allocate local label from Segment-Routing Global Block per required index

Set global-block-origination to add the Originator SRGB TLV (with value equal to local SRGB) for the Prefix-SID attribute resulted in label-index addition/modification

**Command syntax: set sr-label-index [sr-label-index]** global-block-origination

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+--------------------------+----------------------------------------------------------------------------------+-----------+---------+
| Parameter                | Description                                                                      | Range     | Default |
+==========================+==================================================================================+===========+=========+
| sr-label-index           | Add Prefix-SID attribute to the matched prefix. Prefix-SID attribute will        | 0-1048575 | \-      |
|                          | include the Label-Index TLV with index value as set by user                      |           |         |
+--------------------------+----------------------------------------------------------------------------------+-----------+---------+
| global-block-origination | Once enabled, when DNOS adds or update a prefix Prefix-SID attribute, add the    | \-        | \-      |
|                          | Originator SRGB TLV with DNOS local SRGB definition (RFC 8669 TLV 3 of           |           |         |
|                          | Prefix-SID attribute)                                                            |           |         |
+--------------------------+----------------------------------------------------------------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set sr-label-index 10

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set sr-label-index 10 global-block-origination


**Removing Configuration**

To remove set protocols criteria:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set sr-label-index

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.1    | Command introduced |
+---------+--------------------+

---

## set_tag.rst

routing-policy policy rule set tag
----------------------------------

**Minimum user role:** operator

To set the tag attribute:

**Command syntax: set tag [tag]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+--------------------------------+--------------+---------+
| Parameter | Description                    | Range        | Default |
+===========+================================+==============+=========+
| tag       | Sets a new tag attribute value | 0-4294967295 | \-      |
+-----------+--------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set tag 10


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set tag

**Command History**

+---------+-----------------------------------------------------+
| Release | Modification                                        |
+=========+=====================================================+
| 6.0     | Command introduced                                  |
+---------+-----------------------------------------------------+
| 16.1    | Extended the tag range to support unit_32 tag value |
+---------+-----------------------------------------------------+

---

## set_weight.rst

routing-policy policy rule set weight
-------------------------------------

**Minimum user role:** operator

To set the route’s BGP route weight attribute:

**Command syntax: set weight [weight]**

**Command mode:** config

**Hierarchies**

- routing-policy policy rule

**Parameter table**

+-----------+--------------------------------------------------------------+--------------+---------+
| Parameter | Description                                                  | Range        | Default |
+===========+==============================================================+==============+=========+
| weight    | Sets a new weight for the BGP route for best path selection. | 0-4294967295 | \-      |
+-----------+--------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# policy MY_POLICY
    dnRouter(cfg-rpl-policy)# rule 10 allow
    dnRouter(cfg-rpl-policy-rule-10)# set weight 100


**Removing Configuration**

To remove the set entry:
::

    dnRouter(cfg-rpl-policy-rule-10)# no set weight

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

## description.rst

routing-policy prefix-list ipv4 description
-------------------------------------------

**Minimum user role:** operator

To add a description for the rule:

**Command syntax: description [description]**

**Command mode:** config

**Hierarchies**

- routing-policy prefix-list ipv4

**Parameter table**

+-------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter   | Description                                                                      | Range            | Default |
+=============+==================================================================================+==================+=========+
| description | Enter a description for the rule.                                                | | string         | \-      |
|             | Enter free-text description with spaces in between quotation marks. If you do    | | length 1-255   |         |
|             | not use quotation marks, do not use spaces.                                      |                  |         |
|             | For example:                                                                     |                  |         |
|             | ... description 'My long description'                                            |                  |         |
|             | ... description My_long_description                                              |                  |         |
+-------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# prefix-list ipv4 prefix-list1
    dnRouter(cfg-rpl-pl)# description MyDescription_ForPrefixList1

    dnRouter(cfg-rpl)# prefix-list ipv4 prefix-list2
    dnRouter(cfg-rpl-pl)# description MyDescription_ForPrefixList2


**Removing Configuration**

To remove the description:
::

    dnRouter(cfg-rpl-pl)# no description

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| TBD     | Command introduced |
+---------+--------------------+

---

## prefix-list-ipv4.rst

routing-policy prefix-list ipv4
-------------------------------

**Minimum user role:** operator

A community list is a user defined communities attribute list that can be used for matching or manipulating the communities attribute in updates. There are two types of community lists:
- Standard community list - defines the communities attribute
- Extended community list - defines the communities attribute string with regular expression
The standard community list is compiled into binary format and is directly compared to the BGP communities attribute in BGP updates. Therefore, the comparison is faster than in the extended community list.
To define a new standard community list and enter its configuration mode:

**Command syntax: prefix-list ipv4 [prefix-list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy

**Note**

- You cannot delete a prefix list that is attached to a policy.

**Parameter table**

+------------------+-----------------------------+------------------+---------+
| Parameter        | Description                 | Range            | Default |
+==================+=============================+==================+=========+
| prefix-list-name | The name of the prefix-list | | string         | \-      |
|                  |                             | | length 1-255   |         |
+------------------+-----------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# community-list CL_NAME
    dnRouter(cfg-rpl-cl)#


**Removing Configuration**

To delete a community list:
::

    dnRouter(cfg-rpl)# no community-list CL_NAME

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| TBD     | Command introduced |
+---------+--------------------+

---

## rule.rst

routing-policy prefix-list ipv4 rules
-------------------------------------

**Minimum user role:** operator

To add a rule for the prefix list:

**Command syntax: rules [rules]** [, rules, rules]

**Command mode:** config

**Hierarchies**

- routing-policy prefix-list ipv4

**Parameter table**

+-----------+-------------------+-------+---------+
| Parameter | Description       | Range | Default |
+===========+===================+=======+=========+
| rules     | prefix list rules | \-    | \-      |
+-----------+-------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# prefix-list ipv4 prefix-list1
    dnRouter(cfg-rpl-pl)# rule 1 allow any
    dnRouter(cfg-rpl-pl)# rule 2 allow 1.2.3.4/32
    dnRouter(cfg-rpl-pl)# rule 3 deny 5.6.7.8/32


**Removing Configuration**

To remove the rule:
::

    dnRouter(cfg-rpl-pl)# no rule 1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| TBD     | Command introduced |
+---------+--------------------+

---

## description.rst

routing-policy prefix-list ipv6 description
-------------------------------------------

**Minimum user role:** operator

To add a description for the rule:

**Command syntax: description [description]**

**Command mode:** config

**Hierarchies**

- routing-policy prefix-list ipv6

**Parameter table**

+-------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter   | Description                                                                      | Range            | Default |
+=============+==================================================================================+==================+=========+
| description | Enter a description for the rule.                                                | | string         | \-      |
|             | Enter free-text description with spaces in between quotation marks. If you do    | | length 1-255   |         |
|             | not use quotation marks, do not use spaces.                                      |                  |         |
|             | For example:                                                                     |                  |         |
|             | ... description 'My long description'                                            |                  |         |
|             | ... description My_long_description                                              |                  |         |
+-------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# prefix-list ipv4 prefix-list1
    dnRouter(cfg-rpl-pl)# description MyDescription_ForPrefixList1

    dnRouter(cfg-rpl)# prefix-list ipv4 prefix-list2
    dnRouter(cfg-rpl-pl)# description MyDescription_ForPrefixList2


**Removing Configuration**

To remove the description:
::

    dnRouter(cfg-rpl-pl)# no description

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| TBD     | Command introduced |
+---------+--------------------+

---

## prefix-list-ipv6.rst

routing-policy prefix-list ipv6
-------------------------------

**Minimum user role:** operator

A community list is a user defined communities attribute list that can be used for matching or manipulating the communities attribute in updates. There are two types of community lists:
- Standard community list - defines the communities attribute
- Extended community list - defines the communities attribute string with regular expression
The standard community list is compiled into binary format and is directly compared to the BGP communities attribute in BGP updates. Therefore, the comparison is faster than in the extended community list.
To define a new standard community list and enter its configuration mode:

**Command syntax: prefix-list ipv6 [prefix-list-name]**

**Command mode:** config

**Hierarchies**

- routing-policy

**Note**

- You cannot delete a prefix list that is attached to a policy.

**Parameter table**

+------------------+-----------------------------+------------------+---------+
| Parameter        | Description                 | Range            | Default |
+==================+=============================+==================+=========+
| prefix-list-name | The name of the prefix-list | | string         | \-      |
|                  |                             | | length 1-255   |         |
+------------------+-----------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# community-list CL_NAME
    dnRouter(cfg-rpl-cl)#


**Removing Configuration**

To delete a community list:
::

    dnRouter(cfg-rpl)# no community-list CL_NAME

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| TBD     | Command introduced |
+---------+--------------------+

---

## action.rst

routing-policy qppb-policy rule action
--------------------------------------

**Minimum user role:** operator

To configure the actions that should be applied when the rule is matched:


**Command syntax: action**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# action
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action)


**Removing Configuration**

To remove the actions from the rule:
::

    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# no action

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## burst-size.rst

routing-policy qppb-policy rule action burst-size
-------------------------------------------------

**Minimum user role:** operator

Sets the burst-size for the traffic matched by the rule. 
To create a set action:

**Command syntax: burst-size [burst-size] [units]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule action

**Note**

- You can define multiple set actions per rule.

**Parameter table**

+------------+-------------------------------------------------+------------+---------+
| Parameter  | Description                                     | Range      | Default |
+============+=================================================+============+=========+
| burst-size | committed burst size in kilo bytes (1000 bytes) | 50-255000  | 200     |
+------------+-------------------------------------------------+------------+---------+
| units      |                                                 | | kbytes   | kbytes  |
|            |                                                 | | mbytes   |         |
+------------+-------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# action
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action) burst-size 200 mbytes
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action)


**Removing Configuration**

To remove the configuration:
::

    dnRouter(cfg-qppb-policy-PL-1-rule-10-action)# no burst-size

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## drop-tag.rst

routing-policy qppb-policy rule action drop-tag
-----------------------------------------------

**Minimum user role:** operator

Configures the drop-tag that shall be set on the packets that match the rule. 
The drop-tag is mandatory when configuring the qos-tag.

To configure the drop-tag:

**Command syntax: drop-tag [drop-tag]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule action

**Note**

- You can define multiple set actions per rule.

**Parameter table**

+-----------+---------------------+------------+---------+
| Parameter | Description         | Range      | Default |
+===========+=====================+============+=========+
| drop-tag  | Drop priority color | | green    | \-      |
|           |                     | | yellow   |         |
+-----------+---------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# actions
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action) drop-tag yellow
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action)


**Removing Configuration**

To remove the configuration:
::

    dnRouter(cfg-myPolicy1-rule-1-action)# no drop-tag

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## qos-tag.rst

routing-policy qppb-policy rule action qos-tag
----------------------------------------------

**Minimum user role:** operator

Has to be configured together with a drop-tag.
To configure the QoS tag that shall be set on the packets that match the rule:


**Command syntax: qos-tag [qos-tag]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule action

**Parameter table**

+-----------+------------------------+-------+---------+
| Parameter | Description            | Range | Default |
+===========+========================+=======+=========+
| qos-tag   | QoS-tag priority level | 0-7   | \-      |
+-----------+------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# action
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action) qos-tag 5


**Removing Configuration**

To remove the qos-tag from the traffic-class-map:
::

    dnRouter(cfg-qppb-policy-PL-1-rule-10-action)# no qos-tag

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## rate-limit.rst

routing-policy qppb-policy rule action rate-limit
-------------------------------------------------

**Minimum user role:** operator

Sets a rate-limit for the traffic matched by the rule. 
Traffic exceeding the rate-limit will be dropped. 

To set the rate-limit:

**Command syntax: rate-limit [rate-limit] [units]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule action

**Note**

- You can define multiple set actions per rule.

- Rate limit is enforced per NPU core for all traffic received on the given core.

**Parameter table**

+------------+------------------------------------------------------+------------------+---------+
| Parameter  | Description                                          | Range            | Default |
+============+======================================================+==================+=========+
| rate-limit | The rate in kbits per second to limit the traffic to | 0, 64-1000000000 | \-      |
+------------+------------------------------------------------------+------------------+---------+
| units      |                                                      | | kbps           | kbps    |
|            |                                                      | | mbps           |         |
|            |                                                      | | gbps           |         |
+------------+------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# action
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action) rate-limit 1000 kbps


**Removing Configuration**

To remove the configuration:
::

    dnRouter(cfg-qppb-policy-PL-1-rule-10-action)# no rate-limit

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## redirect-to-nexthop-ipv4.rst

routing-policy qppb-policy rule action redirect-to-nexthop-ipv4
---------------------------------------------------------------

**Minimum user role:** operator

When the rule is matched, the redirect-to-next-hop-ipv4 action will direct the matching traffic to the specified IPv4 destination.

To set the redirect action:

**Command syntax: redirect-to-nexthop-ipv4 [redirect-to-nexthop-ipv4]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule action

**Note**

- You can define multiple set actions per rule.

**Parameter table**

+--------------------------+-------------------------------+---------+---------+
| Parameter                | Description                   | Range   | Default |
+==========================+===============================+=========+=========+
| redirect-to-nexthop-ipv4 | ipv4 redirect nexthop address | A.B.C.D | \-      |
+--------------------------+-------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# action
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action) redirect-to-nexthop-ipv4 192.15.87.23
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action)


**Removing Configuration**

To remove the configuration:
::

    dnRouter(cfg-qppb-policy-PL-1-rule-10-action)# no redirect-to-nexthop-ipv4

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## redirect-to-nexthop-ipv6.rst

routing-policy qppb-policy rule action redirect-to-nexthop-ipv6
---------------------------------------------------------------

**Minimum user role:** operator

When the rule is matched, the redirect-to-next-hop-ipv6 action will direct the matching traffic to the specified IPv6 destination.

To set the redirect action:

**Command syntax: redirect-to-nexthop-ipv6 [redirect-to-nexthop-ipv6]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule action

**Note**

- You can define multiple set actions per rule.

**Parameter table**

+--------------------------+-------------------------------+----------+---------+
| Parameter                | Description                   | Range    | Default |
+==========================+===============================+==========+=========+
| redirect-to-nexthop-ipv6 | ipv6 redirect nexthop address | X:X::X:X | \-      |
+--------------------------+-------------------------------+----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# action
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action) redirect-to-nexthop-ipv6 232:22::19:8
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action)


**Removing Configuration**

To remove the redirect-to-next-hop-ipv6 action:
::

    dnRouter(cfg-qppb-policy-PL-1-rule-10-action)# no redirect-to-nexthop-ipv6

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## redirerct-vrf.rst

routing-policy qppb-policy rule action redirect-vrf
---------------------------------------------------

**Minimum user role:** operator

When the rule is matched, the redirect-vrf action will direct the matching traffic to be handled under the specified VRF. 

To set the redirect action:

**Command syntax: redirect-vrf [redirect-to-vrf]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule action

**Note**

- You can define multiple set actions per rule.

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter       | Description                                                                      | Range            | Default |
+=================+==================================================================================+==================+=========+
| redirect-to-vrf | redirect-to-vrf target is a reference to another vrf (not the defined            | | string         | \-      |
|                 | applicable-vrf) - the next hop should be taken from that vrf                     | | length 1-255   |         |
+-----------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# action
    dnRouter(cfg-qppb-policy-PL-1-rule-10-action) redirect-vrf Customer-1-VRF


**Removing Configuration**

To remove the configuration:
::

    dnRouter(cfg-qppb-policy-PL-1-rule-10-action)# no redirect-vrf

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.0    | Command introduced |
+---------+--------------------+

---

## description.rst

routing-policy qppb-policy rule description
-------------------------------------------

**Minimum user role:** operator

To add a meaningful description for a qppb-policy-rule:

**Command syntax: description [description]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule

**Parameter table**

+-------------+---------------------------------------+------------------+---------+
| Parameter   | Description                           | Range            | Default |
+=============+=======================================+==================+=========+
| description | holds a user description for the rule | | string         | \-      |
|             |                                       | | length 1-255   |         |
+-------------+---------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# description "rule that matches Customer-A traffic"
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)#


**Removing Configuration**

To remove the description from the rule
::

    dnRouter(dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# no description

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## applicable-vrf.rst

routing-policy qppb-policy rule match-class applicable-vrf
----------------------------------------------------------

**Minimum user role:** operator

To Configure the VRF that the rule shall be applied to.

**Command syntax: applicable-vrf [applicable-vrf]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule match-class

**Parameter table**

+----------------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter      | Description                                                                      | Range            | Default |
+================+==================================================================================+==================+=========+
| applicable-vrf | applicable vrf defines the vrf to which the src-class and dest-class are         | | string         | default |
|                | applicable                                                                       | | length 1-255   |         |
+----------------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# match-class
    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class) applicable-vrf VRF-1
    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class)


**Removing Configuration**

To restore the applicable-vrf back to its default value - to the default VRF
::

    dnRouter(fg-qppb-policy-PL-1-rule-10-match-class)# no applicable-vrf

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## dest-class.rst

routing-policy qppb-policy rule match-class dest-class
------------------------------------------------------

**Minimum user role:** operator

To Configure a destination class as part of the match criteria of the rule.

**Command syntax: dest-class [dest-class]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule match-class

**Parameter table**

+------------+--------------------------+-----------+---------+
| Parameter  | Description              | Range     | Default |
+============+==========================+===========+=========+
| dest-class | The Destination Class Id | | 1-128   | any     |
|            |                          | | any     |         |
+------------+--------------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# match-class
    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class) dest-class 65
    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class)


**Removing Configuration**

To remove the dest-class from the match-class
::

    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class)# no dest-class

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## ip-version.rst

routing-policy qppb-policy rule match-class ip-version
------------------------------------------------------

**Minimum user role:** operator

Define which ip version packets will be matched by the rule. Default behavior is match "any", i.e either IPv4 or IPv6 packets.

To Configure ip-version:

**Command syntax: ip-version [ip-version]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule match-class

**Note**

- default behavior is match "any", i.e either IPv4 or IPv6 packets

**Parameter table**

+------------+-------------------------------------------------------------+---------+---------+
| Parameter  | Description                                                 | Range   | Default |
+============+=============================================================+=========+=========+
| ip-version | Define which ip version packets will be matched by the rule | | 4     | any     |
|            |                                                             | | 6     |         |
|            |                                                             | | any   |         |
+------------+-------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# match-class
    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class)# ip-version 4
    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class)#


**Removing Configuration**

To remove the ip-version from the match-class
::

    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class)# no ip-version

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## match-class.rst

routing-policy qppb-policy rule match-class
-------------------------------------------

**Minimum user role:** operator

To Configure the match criteria for the rule.

**Command syntax: match-class**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# match-class
    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class)


**Removing Configuration**

To restore the match-class parameters to their defaults
::

    dnRouter(cdnRouter(cfg-rpl-qppb-policy-PL-1-rule-10))# no match-class

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## src-class.rst

routing-policy qppb-policy rule match-class src-class
-----------------------------------------------------

**Minimum user role:** operator

To Configure a soucre class as part of the match criteria of the rule.

**Command syntax: src-class [src-class]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy rule match-class

**Parameter table**

+-----------+---------------------+-----------+---------+
| Parameter | Description         | Range     | Default |
+===========+=====================+===========+=========+
| src-class | The Source Class Id | | 1-128   | any     |
|           |                     | | any     |         |
+-----------+---------------------+-----------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)# match-class
    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class) src-class 100
    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class)


**Removing Configuration**

To remove the src-class from the match-class
::

    dnRouter(cfg-qppb-policy-PL-1-rule-10-match-class)# no src-class

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## qppb-policy-rule.rst

routing-policy qppb-policy rule
-------------------------------

**Minimum user role:** operator

You can create multiple rules per policy. After you create a rule, you enter the rule configuration mode (indicated by the prompt for the rule id) and
you can proceed to add a description and configure actions for the specific rule. See "qppb policy rule description" and "qppb policy rule action".

To create a rule, make sure that you are in QoS policy configuration mode:

**Command syntax: rule [qppb-policy-rule]**

**Command mode:** config

**Hierarchies**

- routing-policy qppb-policy

**Parameter table**

+------------------+---------------------------------------+---------+---------+
| Parameter        | Description                           | Range   | Default |
+==================+=======================================+=========+=========+
| qppb-policy-rule | the unique rule id inside the policy. | 1-65535 | \-      |
+------------------+---------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)# rule 10
    dnRouter(cfg-rpl-qppb-policy-PL-1-rule-10)#


**Removing Configuration**

To delete the qppb rule:
::

    dnRouter(cfg-rpl-qppb-policy-PL-1)# no rule 10 

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## qppb-policy.rst

routing-policy qppb-policy
--------------------------

**Minimum user role:** operator

A QoS qppb policy is a set of rules and is identified by a unique name.

To create a QoS qppb policy:

**Command syntax: qppb-policy [qppb-policy]**

**Command mode:** config

**Hierarchies**

- routing-policy

**Parameter table**

+-------------+------------------+------------------+---------+
| Parameter   | Description      | Range            | Default |
+=============+==================+==================+=========+
| qppb-policy | qppb policy name | | string         | \-      |
|             |                  | | length 1-255   |         |
+-------------+------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)# qppb-policy PL-1
    dnRouter(cfg-rpl-qppb-policy-PL-1)#


**Removing Configuration**

To remove the qppb policy
::

    dnRouter(cfg-rpl)# no qppb-policy

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+

---

## routing-policy.rst

routing-policy
--------------

**Minimum user role:** operator

You can create policies that are used by the various routing protocols.

The following types of policies are supported:

-	AS-path access-list
-	Community-list
-	extcommunity-list
-	large-community-list
-	Policy
-	Prefix-list

To enter routing policy configuration mode:

**Command syntax: routing-policy**

**Command mode:** config

**Note**

- You cannot remove a routing-policy that is being used.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# routing-policy
    dnRouter(cfg-rpl)#


**Removing Configuration**

To remove all policies configuration (all as-path-lists, community-lists, extcommunity-lists, large-community-lists , policies and prefix-lists):
::

    dnRouter(cfg)# no routing-policy

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 6.0     | Command introduced |
+---------+--------------------+

---

---

# SECTION 7: GROUPS

Files from groups folder:        3 files

## apply-groups-exclude.rst

apply-groups-exclude
--------------------

**Minimum user role:** operator

To configure CLI Configuration Groups that needs to be excluded from the hierarchy and below, unless the same group is configured explicitly a hierarchy below with apply-groups.

**Command syntax: apply-groups-exclude [group-name]** [, group-name, group-name]

**Command mode:** config

**Hierarchies**

- group

**Note**

-  The CLI will provide apply-groups-exclude under any CLI hierarchy
-  Any configured group can be excluded, means that group won't be applied in case it was configured as apply-groups at the same hierarchy or above.
-  Starting from current hierarchy and below, the excluded groups won't be applied, unless the configuration is set explicitly with apply-groups in a lower hierarchy.
-  The same group can be assigned multiple times to different hierarchies.
-  Multiple groups can be assigned under the same configuration hierarchy, in case of contradicting config, the first (most left) group takes precedence.
-  In case the same group applied by apply-groups and apply-groups-exclude, the group will be excluded from being applied.
-  Once group is applied under apply-groups-exclude in some hierarchy, the configuration related to the hierarchy the group was applied will be validated, that the ranges and keys are valid.



**Parameter table**

+----------------------+-------------------------------------------------------------------------------------------------+-------+---------+
| Parameter            | Description                                                                                     | Range | Default |
+======================+=================================================================================================+=======+=========+
| apply-groups-exclude | The group names that should be excluded starting from that hierarchy                            | \-    | \-      |
+----------------------+-------------------------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)#
    dnRouter(cfg)# apply-groups-exclude group1, group2
    dnRouter(cfg)# system
    dnRouter(cfg-system)# apply-groups-exclude group2


**Removing Configuration**

To delete apply-groups-exclude:
::

    dnRouter(cfg)# no apply-groups-exclude group1

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| TBD     | Command introduced |
+---------+--------------------+

---

## apply-groups.rst

apply-groups
------------

**Minimum user role:** operator

To apply the CLI Configuration Groups, to a specific CLI hierarchy.

**Command syntax: apply-groups [group-name]** [, group-name, group-name]

**Command mode:** config

**Hierarchies**

- group

**Note**

-  The configured group can be applied at any hierarchy at the CLI.
-  The CLI will provide apply-groups under any CLI hierarchy
-  The same group can be assigned multiple times to different hierarchies.
-  Multiple groups can be assigned under the same configuration hierarchy, in case of contradicting config, the first group takes precedence.
-  In case the same group applied by apply-groups and apply-groups-exclude, the group will be excluded from being applied
-  Once group is applied to some hierarchy, the configuration related to the hierarchy the group was applied to will be validated, that the ranges and keys are valid.

**Parameter table**

+---------------------+-------------------------------------------------------------------------------------------------+-------+---------+
| Parameter           | Description                                                                                     | Range | Default |
+=====================+=================================================================================================+=======+=========+
| apply-groups        | The group names that should be applied starting from that hierarchy and lower                   | \-    | \-      |
+---------------------+-------------------------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)#
    dnRouter(cfg)# apply-groups group1, group2
    dnRouter(cfg)# system
    dnRouter(cfg-system)# apply-groups group2


**Removing Configuration**

To delete apply-groups:
::

    dnRouter(cfg)# no apply-groups

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| TBD     | Command introduced |
+---------+--------------------+

---

## group.rst

group
-----

**Minimum user role:** operator

To configure CLI Configuration Groups, that can be applied to any CLI hierarchy.

**Command syntax: group [group-name]**

**Command mode:** config

**Hierarchies**

- group

**Note**

-  Configuration group need to reach a full configuration path, so it will finish with a command with updates the configuration.
-  as part of the CLI configuration group, regex expressions can be provided, regex expressions shall be wrapped with <>, regular key values will be provided as is.
-  The configured group can be applied at any hierarchy at the CLI.
-  The same group can be assigned multiple times to different hierarchies.
-  Multiple CLI commands can be assigned under the same configuration group.
-  Inheritance
-  Once group config updated, it will be inherited by all applied hierarchies.
-  If inheritance from a group is specified in a lower hierarchy and above the same group is configured with “apply-groups-exclude” than only the lower hierarchy will be subject to inheritance.

-  when a group is applied to a hierarchy and an explicit config exists, the group configuration should be merged with the existing config, in case of collision, the explicit config (none group config) wins over the group config.
-  Groups applied in nested  sections of the config (lower hierarchy), take priority over groups in outer statements1
-
-  Validations:
-  Group name can be any string except: 'global', 'default'
-  Any configuration applied through groups will be validated with CLI validations.
-  Group can be deleted only in case it is not used, means not applied by any apply-groups or apply-groups-exclude configuration
-  Group configuration won't apply the CLI validation on the group keys and values, validation will be performed once the group will be applied.



**Parameter table**

+-----------+----------------------------------------+-------+---------+
| Parameter | Description                            | Range | Default |
+===========+========================================+=======+=========+
| group     | Group name associated with this entry. | \-    | \-      |
+-----------+----------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)#
    dnRouter(cfg)# group group1
    dnRouter(cfg-group-group1)#
      access-lists                Configure access-lists
      debug                       Debug command
      forwarding-options          Configure forwarding options
      interfaces                  Configure interfaces
      multicast                   Configure multicast
      nacm                        Access control model for the netconf protocol
      network-services            Configure network-services
      no                          Negate a command or set its defaults
      protocols                   Configure protocols
      qos                         Configure QOS
      routing-options             Routing options
      routing-policy              Routing policy
      services                    Configure services
      system                      Configure system
      tracking-policy             Configure tracking-policy
    dnRouter(cfg-group-group1)# interfaces <*> description "group1 interface description" speed 9000
    dnRouter(cfg-group-group1)# interfaces <ge-100*> admin-state enabled

    dnRouter(cfg)# group group2 system ssh server admin-state enabled
    dnRouter(cfg-group-group2)#


**Removing Configuration**

To delete all groups:
::

	dnRouter(cfg)# no group

To delete group:
::

    dnRouter(cfg)# no group group1
    dnRouter(cfg)# no group group1 interfaces <ge-100*>
    dnRouter(cfg)# no group group1 interfaces <*> description

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| TBD     | Command introduced |
+---------+--------------------+

---

