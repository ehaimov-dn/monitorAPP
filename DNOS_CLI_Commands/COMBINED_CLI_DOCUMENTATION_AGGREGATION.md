# Combined CLI Documentation Aggregation

This file combines the complete content from three major CLI documentation sections:
1. Accessing the CLI Terminal (9 RST files)
2. CLI Guidelines (8 RST files)
3. Cmd Commands (2 RST files)

Total combined files: 19 RST files

---

# SECTION 1: ACCESSING THE CLI TERMINAL

## Original source: ACCESSING_CLI_TERMINAL_COMPLETE_AGGREGATION.md

# Accessing the CLI Terminal Complete Aggregation

This file contains the complete content from all RST files in the Accessing the CLI Terminal folder.

Total files:        9

---

## Accessing the CLI Terminal.rst

Accessing the CLI Terminal
--------------------------

**Minimum user role:** operator

The DNOS command line interface (CLI) is the primary interface you use to access, configure, and monitor the DriveNets Network Cloud Router. You can access the CLI from a remote location via SSH. DNOS supports up to 10 simultaneous SSH sessions. SSH sessions disconnect automatically after remaining idle for 30 minutes (configurable).

The CLI provides the following major features:

- Operation and configuration modes

- Command completion

- Context-sensitive help

To access the CLI, you need a valid user. Each user is assigned with a role that determines which operations the user can and cannot perform. See “system login user role”.

To access the CLI, log on to the NC system (NCE):

1. From a remote host, open an SSH session to the NCE.

2. At the prompt, enter the username for the server, press Enter.

3. At the prompt, enter the password for the server, press Enter. If login is successful, the server prompt of the main CLI terminal is displayed:

::

 dnRouter# 

4. Enter the necessary commands to complete your tasks.

To log off:

1. At the operation mode prompt, enter the exit command to exit the CLI.
::

 dnRouter# exit

Or enter the following command from any command mode to exit the CLI and close the CLI terminal:
::

 dnRouter(cfg-any-hierarchy)# quit

2. Press Enter.




---

## CLI Notations.rst

CLI Syntax Notations
--------------------

**Minimum user role:** operator

The following table describes the notations used in the CLI syntax. A “keyword” is either a command (e.g., show, run, clear), a hierarchy level (e.g., access-list, protocols), or a paramter (e.g., admin-state, description).

+--------------------------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                      |                                                                                                              |                                                                                                   |
| Typographic Notation                 | Description                                                                                                  | Example                                                                                           |
+======================================+==============================================================================================================+===================================================================================================+
|                                      |                                                                                                              |                                                                                                   |
| bold text                            | A mandatory   keyword                                                                                        | dnRouter(cfg-if-ge100-1/1/1)#   arp host-address [host-ipv4-address] mac-address [mac-address]    |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                      |                                                                                                              |                                                                                                   |
| hyphenated-keyword                   | A single   keyword                                                                                           | access-list                                                                                       |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                      |                                                                                                              |                                                                                                   |
|                                      |                                                                                                              | admin-state   [admin-state]                                                                       |
|                                      |                                                                                                              |                                                                                                   |
| [bracketed-text]                     | A value you   need to enter for the parameter. The square brackets do not appear in the   actual command.    | You must enter   either “enabled” or “disabled”:                                                  |
|                                      |                                                                                                              |                                                                                                   |
|                                      |                                                                                                              | admin-state   enabled                                                                             |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                      |                                                                                                              |                                                                                                   |
| regular text                         | An optional   keyword.                                                                                       | dnRouter(cfg)# interface ge100-1/2/1 admin-state [admin-state]                                    |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                      |                                                                                                              |                                                                                                   |
| Braces with   vertical bars { | }    | A mandatory   choice between options                                                                         | request   interfaces management [interface-name] ipv6-address {[ipv6-address] | dhcp}             |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                                      |                                                                                                              |                                                                                                   |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+






---

## Concatenating Commands.rst

Concatenating Commands
----------------------

**Minimum user role:** operator

You can concatenate show commands in a single command line. The concatenated commands are separated by a semicolon, as follows:

**Example**
dnRouter# <show_command> ; <show_command> ; <show_command>...


.. **Command mode:** configuration

The output will be printed sequentially according to the order of appearance in the command line. Each printed output is prefixed with a hash sign (#) indicating that the following output is for a different command:



**Example**
dnRouter# show interfaces ; show system
# show interfaces
...
# show system
...





---

## Entering Commands.rst

Entering Commands
-----------------

**Minimum user role:** operator

To enter a command, type the command statement as described in this guide and press **Enter**.

.. **Command syntax: 

.. **Command mode:** configuration

**Note**
	If you type a command that is not valid, an error message is displayed.


.. **Parameter table**

**Example**
::

	dnRouter# show system login users
	

.. **Help line:** merge the file content with the candidate configuration

..**Command History**




---

## Entering Remarks in Commands.rst

Entering Remarks in Commands
----------------------------

**Minimum user role:** operator

You can add remarks in operation as well as in configuration commands by specifying a hash sign (#) before the remark. When copying the configuration using external tools/scripts, the remarks will be copied as well, but only during the configuration session and while the remarks are visible on screen.

**Example:**
dnRouter(cfg)# interface bundle-1 mtu 1514
dnRouter(cfg-if)# only comment

**Note**
The remark is not saved to the configuration file and is not visible in any show command.





---

## Examples.rst

Examples
--------

**Minimum user role:** operator

The examples in the DNOS command line interface (CLI) are for illustration purposes only.
This is an example of the system aaa-server radius server command:

**Example:**
::

	dnRouter# configure
	dnRouter(cfg)# system
	dnRouter(cfg-system)# aaa-server
	dnRouter(cfg-system-aaa)# radius
	dnRouter(cfg-system-aaa-radius)# server priority 1 address 192.168.1.1
	dnRouter(cfg-aaa-radius-server)# vrf default
	dnRouter(cfg-aaa-radius-server)# password enc-!@#$%
	dnRouter(cfg-aaa-radius-server)# authentication enabled
	dnRouter(cfg-aaa-radius-server)# port 100
	dnRouter(cfg-aaa-radius-server)# retries 3
	dnRouter(cfg-aaa-radius-server)# retry-interval 20
	dnRouter(cfg-system-aaa-radius)# server priority 2 address 192.168.1.2
	dnRouter(cfg-aaa-radius-server)# vrf mgmt0
	dnRouter(cfg-aaa-radius-server)# password enc-!@#$%
	dnRouter(cfg-aaa-radius-server)# authentication enabled
	dnRouter(cfg-aaa-radius-server)# port 100
	dnRouter(cfg-aaa-radius-server)# retries 5
	dnRouter(cfg-aaa-radius-server)# retry-interval 15
	dnRouter(cfg-system-aaa-radius)# server priority 5 address 1134:1134::1
	dnRouter(cfg-aaa-radius-server)# vrf mgmt0
	dnRouter(cfg-aaa-radius-server)# password enc-!@#$%
	dnRouter(cfg-aaa-radius-server)# authentication enabled
	dnRouter(cfg-aaa-radius-server)# port 100
	dnRouter(cfg-aaa-radius-server)# retries 5
	dnRouter(cfg-aaa-radius-server)# retry-interval 15

---

## Getting Help.rst

Getting Help
------------

**Minimum user role:** operator

The CLI includes context sensitive help that displays a list of options available at the current hierarchy with a short description. To access the context-sensitive help, press ?. You can also use the tab key for assistance.

Use the tab key to:

Show all commands that are available under the current prompt - press tab at the prompt.


**Note**
	Help is not available for user-configured aliases.


**Example**
::

	dnRouter# tab
	clear
	configure
	no
	request
	run
	set
	show
	end
	exit
	quit
	top
	dnRouter#
	
Show available options for a specific command - enter tab after entering a complete command name.

**Example**
::

	dnRouter# show tab
	access-list
	arp
	...
	dnRouter# show

Auto-complete a partially entered command - press tab after entering part of a command name (with no space in between).

**Example**
::

	dnRouter# show inttab
	dnRouter# show interfaces

	If the partially entered command is not unique, auto-complete will not work. You need to enter enough of the command to disambiguate it.

**Example**
::

	Won't work (because ip is used by both ipv4-address and ipv6-address commands):
	dnRouter(cfg)# interfaces ge100-1/1/1 iptab
	dnRouter(cfg)#

	Will work:
	dnRouter(cfg)# interfaces ge100-1/1/1 ipv4tab
	dnRouter(cfg)# interfaces ge100-1/1/1 ipv4-address


In configuration mode, a separator is displayed between the hierarchy specific command items, i.e. the list of commands that are specific to the current hierarchy, and general command items, i.e. the commands that are applicable to all hierarchy levels and are not specific to the current hierarchy.

**Example**
::
	
	SECOND(cfg)# services
	SECOND(cfg-srv)
	flow-monitoring           Configure flow-monitoring
	l2-cross-connect          Enters the context of L2 cross connect service configuration.
	mpls-oam                  Configure mpls-oam profile
	port-mirroring            Configure a new port-mirroring session.
	twamp                     Configure twamp profile
	
	----------------
	
	clear                     Clear command
	commit                    Commit transaction
	dump                      Generate a core dump of BGP process without killing it
	end                       Exit configuration menu
	exit                      Exit current menu
	load                      Load saved configuration
	quit                      Quit DRIVENETS CLI
	request                   Request operations
	rollback                  Rollback transaction
	run                       Run a command
	save                      Save current configuration
	set                       Set temporary configuration
	show                      Displays information about the system and system configuration
	top                       Exit to root configuration menu
	unset                     Unset temporary configuration



---

## Using Keyboard Commands.rst

Using Keyboard Commands
-----------------------

**Minimum user role:** operator

The CLI enables the following keyboard commands:

+------------+--------------------------------------------------------------------------------+
| Parameter  | Description                                                                    |
+------------+--------------------------------------------------------------------------------+
| Enter      | Executes the command                                                           |
+------------+--------------------------------------------------------------------------------+
| Tab        | Completes the command or option                                                |
+------------+--------------------------------------------------------------------------------+
| Up arrow   | Displays the previous command in the history                                   |
+------------+--------------------------------------------------------------------------------+
| Down arrow | Displays the next command in the history                                       |
+------------+--------------------------------------------------------------------------------+
| Ctrl-c     | Aborts the current command                                                     |
+------------+--------------------------------------------------------------------------------+
| !          | Exits one hierarchy up in config mode. This is useful for configuration files. |
+------------+--------------------------------------------------------------------------------+
| ?          | Displays the available options for the current hierarchy.                      |
+------------+--------------------------------------------------------------------------------+


---

## Using Special Characters.rst

Using Special Characters
------------------------

**Minimum user role:** operator

Some characters perform special action in the CLI. When using a special character inside a string (e.g. comment, description, name and regular expressions), enclose the string in double quotes ("string"). This will not change the meaning of the string. The quotes will appear in the "show config" output.

The CLI supported special characters are:

+-----------+---------------+------------------------------------------------------------+
| Character | Name          | Action                                                     |
+-----------+---------------+------------------------------------------------------------+
| ' '       | space         | Separates command parameters and arguments                 |
+-----------+---------------+------------------------------------------------------------+
| '|'       | pipe          | Filter, monitor, disable output paging (see Pipe Commands) |
+-----------+---------------+------------------------------------------------------------+
| '?'       | question mark | Invoke help menu (see Getting Help)                        |
+-----------+---------------+------------------------------------------------------------+
| '#'       | Hash          | Enter user comment (see Entering Remarks in Commands)      |
+-----------+---------------+------------------------------------------------------------+

**Example**
::

	dnRouter(cfg-policy-MyQoSPOlicy1-rule1)# description "real time service"
	dnRouter(cfg-rpl-cl)# rule 70 allow regex "65000:5000|_65000:3[0-9][0-9][0-9]?"	



---


---

# SECTION 2: CLI GUIDELINES

## Original source: CLI_GUIDELINES_COMPLETE_AGGREGATION.md

# CLI Guidelines Complete Aggregation

This file contains the complete content from all RST files in the CLI Guidelines folder.

Total files:        8

---

## action words.rst

Action Words
------------

The help description for menu items always begins with an action word (Configure, Display, Remove, etc.).

The help description for parameters never begins with an action word. It only describes the variable itself.

Example:

propagate-ttl Configure TTL propagation

<enabled> enable TTL propagation

<disabled> disable TTL propagation

The help for the menu item in Configuration mode is: Configure parameter. In the above example the parameter is TTL propagation, so the help for the corresponding menu item is Configure TTL propagation.

+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          | Note that the help for the parameter is just the Parameter name. There is no need to add an action word: Enable or Disable TTL propagation. This is self-evident. |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following are the main action words used:

Clear Clear operations

Configure Configure mode

load Load saved configuration

merge Merge configuration file

no Remove configuration

request Request operations

run Run a command

save Save current configuration

show Display information

Exceptions
~~~~~~~~~~

Sometimes, "configure" is not the correct action word for a menu item, even though the menu item is under the "configure" hierarchy.

Example

configure access-list ipv4 <acl_name> rule <rule_id> <<rule_type>> fragmented

configure Configure mode

access-list Configure access-list

ipv4 Configure IPv4 access-list type

<text> Access-list name (36 characters)

Rule Configure access-list rule

<1-65534> Rule identifier

<allow/deny> Rule type

Fragmented Match fragmented packets

For the menu item "fragmented", "Configure fragmented packets" would be incorrect. In this case, "Match fragmented packets" is accurate.

---

## capitalization.rst

Capitalization
--------------

-  Parameters and menu items (on the left column) are always in lowercase (never capitalized).

-  Help descriptions (on the right column) always begin with a capital letter. The rest follows the regular capitalization rules. Acronyms are fully capitalized (for example, BGP, OSPF).

Example:

dnRouter(cfg)# protocol ?

ldp Configure LDP protocol

mpls Configure MPLS protocol

ospf Configure OSPF protocol

---

## copy paste for show commands.rst

Copy paste for show commands
----------------------------

Multiple copy/paste for show commands are enabled by DNOS cli (for example, copying 10 "show system version" commands will result to 10 outputs of the command).

In case the show command output needs to be paged (for cases the output contains numerous lines), then the pager will start and all following commands will be ignored. Meaning there will not be a way to paste multiple show commands once a command needs a pager.

---

## error messages.rst

Error Messages
--------------

The proper syntax of an error messages is defined in this `Confluence <https://drivenets.atlassian.net/wiki/spaces/VP/pages/367919217/DNOS+CLI+Terminal+messaging>`__ page.

All the messages MUST follow a unified syntax & keyword. An error message typically has 3 parts:

Declaration, failed action, and reason for failure.

-  The "declaration" is followed by a colon

-  The "failed action" is followed by a comma

-  The "reason for failure" is followed by a full stop

**Example**

Error: Unable to configure interface <interface-name>, <interface-name> does not exist.

Warning: Configuringsystem timing-mode manual, may result in system synchronization error with the conductor.

The following cases are identified as **errors**:

- The command syntax is invalid / not-supported

- The parameter syntax is invalid / not-supported

- Faliure to commit the candidate configuration (due to syntax or resource issues)

The following cases are identified as **warnings**:

- Performing an operational command which may result in an intrusive action (such as "request system restart").

- Applying a candidate configuration commit which may result in a non-stable state.

**Capitalization**

Error messages follow the regular capitalization rules:

 - Use a capital letter after a full stop or a colon

- Use capital letters for acronyms

- Use a lowercase letter after a comma

- The "declaration" always begins with a capital letter: **E**  rror:

- The "reason for failure" begins with a lowercase letter (as it follows a comma).

**Example**

Error: Unable to configure interface <interface-name>, <interface-name> does not exist.

Expected output:

Error: Unable to configure interface <interface-name>, ge100-1/2/1 does not exist.

Error: Unable to remove VRF <vrf-name>, interfaces are attached to the VRF.

**Phrasing**

$type: $cause to $action[exact command] ,[reason for faliure]

The "failed action" has the general phrasing: "$cause to $action," ("Unable to do something,"). Always use the adjective Unable. Do not use "Cannot do something" or "Failed to do something". See `Exceptions <#_Exceptions>`__ below.

Avoid using contractions in error messages.

**Example**

Error: Unable to configure interface ge100-1/2/1.100 qos policy out myQoSPolicy1, policy does not exist.

Warning: Configuring system timing-mode manual, may result in system synchronization error with the conductor.

**Exceptions**

The reason for failure may at times be unnecessary.

Error: Bad mask /24 for address 192.168.1.0.

Error: Unauthorized to execute the command.

Error: No TACACS servers are available. Please reconnect to CLI.

Error: Unknown command.

Error: Command not supported by current system.

When entering a wrong value for a paramater, the failed action phrasing should be: Error: Invalid value for [parameter-name], value must be x-y.

**Example**

Error:Invalid value for probe-interval, value must be 1..300.

---

## general.rst

General
-------

Every help line has two columns: the left column lists the parameters/menu items; the right column provides a help description.

"Menu items" refers to static text that is entered verbatim. Example: mpls

"Parameters" refers to variables (dynamic). Example: <vrf_name>

"Help descriptions" refers to the help line for each menu item or parameter.

---

## no commands.rst

No commands
-----------

To distinguish "no" commands from "configure" commands, the help for menu items under the "no" hierarchy begins with the action word: Remove

Example

For the general command: configure no system snmp user <<user_name>> view, the following is the help hierarchy:

Configure Configure mode

no Remove configuration

system Remove system

snmp Remove SNMP

user Remove SNMP user

<text> User name (36 characters)

view Remove system SNMP user view

+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          | Note:                                                                                                                                                                                                                                                                        |
|          |                                                                                                                                                                                                                                                                              |
|          | All menu items under "no" begin with "Remove".                                                                                                                                                                                                                               |
|          |                                                                                                                                                                                                                                                                              |
|          | Parameters under the "no" hierarchy **do not** begin with "Remove" (<text> denoting User name in the example above).                                                                                                                                                         |
|          |                                                                                                                                                                                                                                                                              |
|          | The help line for "no" is: Remove configuration; for subsequent menu items under the "no" hierarchy, there is no need to repeat the word "configuration". Hence, "Remove system" and not "Remove system configuration". We tried to keep the help line as short as possible. |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

---

## parameters.rst

Parameters
----------

Include the units of measurements and default in brackets in the help lines of parameters. Do not mention default if there is no default (e.g. <key_id>). Do not mention unit for identifiers (e.g. <key_id>).

For textual parameters, include the length allowed.

Example

<60-14400> Timeout (seconds, default 3600)

<1-65534> Maximum queue size (packets, default 10000)

<text> User name (36 characters)

<1-65533> Key identifier

<1472-9300> MTU value (bytes, default 9300)

---

## table sorting.rst

Table sorting
-------------

-  In general, all tables in DNOS show commands shall be sorted per key values in ascending matter from low to high values

-  If not mentioned and specified otherwise, the key value should be the key in the data model (yang)

-  For a case with multiple keys (e.g. node name and node ID), the second key will be sorted after the first key and so on for multiple keys unless there is an explicit desired sorting that must be specified.

- Output effecive also on routing show commands

- The specifaction can have unique sorting for specific commands beyond the general guideline. i.e in "show system", the node name shall be sorted manually (NCC -> NCF -> NCP -> NCM) due to importance or any other product/system matter. In addition, the sorting may be different than the key in the data model (specified explicitly)

- Raw data which arranged in type of list which not presented in table, should also be ordered according the table sorting rules

Examples for syntax sorting:

* lexicographically: a -> z, A -> Z, 0 -> 1 (per ASCII definition)

* numbers:  0 -> 1

* ip addresses: 1.1.1.1 -> 1.1.1.2 -> 1.1.2.1

**CLI example:**
::

	dnRouter# show system

	...

	# Type customized first key
	# ID numbered second key

	| Type | Id | Admin    | Operational  | Model      | Uptime           | Description | Serial Number      |
	+------+----+----------+--------------+------------+------------------+-------------+--------------------+
	| NCC  | 0  |          | active-up    | X86        | 0 days, 22:50:07 | dn-ncc-0    | CZ293105J0         |
	| NCC  | 1  |          | standby-up   | X86        | 0 days, 2:10:24  | dn-ncc-1    | CZ293105HZ         |
	| NCF  | 0  | enabled  | up           | NCF-48CD   | 0 days, 22:40:57 | dn-ncf-0    | WEB1947D0003C      |
	| NCF  | 1  | enabled  | up           | NCF-48CD   | 0 days, 22:40:58 | dn-ncf-1    | WEB1947V00001      |
	| NCF  | 2  | enabled  | up           | NCF-48CD   | 0 days, 22:40:58 | dn-ncf-2    | WEB1947300032      |
	| NCF  | 3  | enabled  | up           | NCF-48CD   | 0 days, 22:42:06 | dn-ncf-3    | WEB19B7N00026-P2   |
	| NCF  | 4  | enabled  | up           | NCF-48CD   | 0 days, 22:42:29 | dn-ncf-4    | WEB1977Y0000F-P1   |
	| NCF  | 5  | enabled  | up           | NCF-48CD   | 0 days, 22:42:01 | dn-ncf-5    | WEB1977X0000E-P1   |
	| NCF  | 6  | enabled  | up           | NCF-48CD   | 0 days, 22:42:03 | dn-ncf-6    | WEB1977M00021-P1   |
	| NCF  | 7  | enabled  | up           | NCF-48CD   | 0 days, 22:41:39 | dn-ncf-7    | WEB1977M00013-P1   |
	| NCF  | 8  | enabled  | up           | NCF-48CD   | 0 days, 22:42:02 | dn-ncf-8    | WEB1977N00014-P1   |
	| NCF  | 9  | enabled  | up           | NCF-48CD   | 0 days, 22:41:59 | dn-ncf-9    | WEB1977W00029-P1   |
	| NCF  | 10 | enabled  | up           | NCF-48CD   | 0 days, 22:40:26 | dn-ncf-10   | WEB1947400017      |
	| NCF  | 11 | enabled  | up           | NCF-48CD   | 0 days, 22:42:30 | dn-ncf-11   | WEB1A17S00019-P3   |
	| NCF  | 12 | enabled  | up           | NCF-48CD   | 0 days, 22:40:25 | dn-ncf-12   | WEB1957400010      |
	| NCP  | 0  | enabled  | up           | NCP-10CD   | 0 days, 22:35:44 | dn-ncp-0    | WDV1977M00006-P1   |
	| NCP  | 1  | enabled  | up           | NCP-10CD   | 0 days, 22:35:48 | dn-ncp-1    | WDV1957D0000C      |
	| NCP  | 2  | enabled  | up           | NCP-40C    | 0 days, 22:35:35 | dn-ncp-2    | WDY1957800009      |
	| NCP  | 3  | enabled  | up           | NCP-40C    | 0 days, 22:35:32 | dn-ncp-3    | WDY1977X0001F-P1   |
	| NCP  | 4  | enabled  | up           | NCP-40C    | 0 days, 22:35:30 | dn-ncp-4    | WDY1977J00021-P1   |
	| NCP  | 5  | enabled  | up           | NCP-40C    | 0 days, 22:35:35 | dn-ncp-5    | WDY1977U0002A-P1   |
	| NCP  | 6  | enabled  | up           | NCP-40C    | 0 days, 22:35:39 | dn-ncp-6    | WDY1977W00056-P1   |
	| NCP  | 7  | enabled  | up           | NCP-40C    | 0 days, 22:35:35 | dn-ncp-7    | WDY1977X0003B-P1   |
	| NCP  | 8  | enabled  | up           | NCP-40C    | 0 days, 22:35:38 | dn-ncp-8    | WDY1957A0000B      |
	| NCP  | 9  | enabled  | up           | NCP-40C    | 0 days, 22:35:37 | dn-ncp-9    | WDY1977X0002D-P1   |
	| NCP  | 10 | enabled  | up           | NCP-40C    | 0 days, 22:35:34 | dn-ncp-10   | WDY1977X00057-P1   |
	| NCP  | 11 | enabled  | up           | NCP-40C    | 0 days, 22:35:31 | dn-ncp-11   | WDY1957900050      |
	| NCM  | A0 |          | up           | NCM-48X-6C | 0 days, 22:59:17 | dn-ncm-A0   | AAF1925AADI        |
	| NCM  | A1 |          | up           | NCM-48X-6C | 0 days, 22:59:14 | dn-ncm-A1   | AAF1951AAAN        |

	dnRouter# show system hardware

	...

	# Module Name lexicographically single key

	CPLD Version:

	| Module Name   | Image Version   |
	|---------------+-----------------|
	| CPU CPLD      | v0.29           |
	| MB CPLD1      | v0.62           |
	| MB CPLD2      | v0.12           |
	| MB CPLD3      | v0.12           |

	...

	# CPU lexicographically single key

	CPU Usage:

	| CPU   | Use %   |
	|-------+---------|
	| 0     | 22      |
	| 1     | 19      |
	| 2     | 22      |
	| 3     | 52      |
	| 4     | 55      |
	| 5     | 19      |
	| 6     | 22      |
	| 7     | 31      |
	| 8     | 21      |
	| 9     | 19      |
	| 10    | 16      |
	| 11    | 15      |
	| 12    | 11      |
	| 13    | 19      |
	| 14    | 18      |
	| 15    | 15      |
---


---

# SECTION 3: CMD COMMANDS

## Original source: CMD_COMMANDS_COMPLETE_AGGREGATION.md

# Cmd Commands Complete Aggregation

This file contains the complete content from all RST files in the Cmd Commands folder.

Total files:        2

---

## cmd help.rst

cmd help
---------

**Minimum user role:** operator

Display command help of a specific command.

**Command syntax: cmd help** [full-command]

**Command mode:** operational

**Parameter table:**

+--------------------+-----------------------------------------+-------------------+---------------+
| Parameter          | Description                             | Values            | Default value |
+====================+=========================================+===================+===============+
| full-command       | Full command with params                | String | all      | \-            |
+--------------------+-----------------------------------------+-------------------+---------------+

**Note:**

- Recommended to use 'cmd search' command first to get the full command.

- If no exact match is found, a best match will be displayed.

- If no exact match or best match are found, an error message will be displayed.


**Example**
::

    dnRouter# cmd help "configure protocols bgp <bgp> address-family ipv6-unicast labeled-unicast prefix-sid <<prefix_sid>>"

              Relevant command information will be displayed...

    dnRouter# cmd help "configure protocols bgp dummy"

              * A partial match is found for the command 'onfigure protocols bgp dummy':

              Best match command information will be displayed here...

    dnRouter# cmd help dummy

              No additional information for command: 'dummy'

.. **Help line:** Command help (full command)

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 25.2    | Command introduced                  |
+---------+-------------------------------------+
---

## cmd search.rst

cmd search
----------

**Minimum user role:** operator

Search available commands using keywords.

**Command syntax: cmd search** [word]

**Command mode:** operational

**Parameter table:**

+--------------------+-----------------------------------------+-------------------+---------------+
| Parameter          | Description                             | Values            | Default value |
+====================+=========================================+===================+===============+
| word               | words to search (with quotation marks)  | String | all      | \-            |
+--------------------+-----------------------------------------+-------------------+---------------+

**Note:**

- In order to limit the results, use "include", "include regex" or "exclude".

**Example**
::

    dnRouter# cmd search "protocols bgp" | include "evpn"
    dnRouter# cmd search "protocols bgp" | include "evpn" | exclude "label"  
    dnRouter# cmd search "protocols bgp" | include regex "evpn.label"

.. **Help line:** Command search by keywords

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 25.2    | Command introduced                  |
+---------+-------------------------------------+
---


---

# SECTION 4: TRANSACTIONS

## Original source: Transactions folder

Files from Transactions folder:        8 files

## cli_regex.rst

regular expressions
-------------------

+-------------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Character         | Description                                                                                                                     | Example                                                                         |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| .                 | Stands for a single character.                                                                                                  | 76.7 matches 7607, 7617, 7627, ... 7697                                         |
| (period)          |                                                                                                                                 |                                                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| \                 | Matches the special character following the backslash ignoring any function it may have in regular expressions.                 | 192\.1\.. matches 192.1.5.10 but not 192.10.5.0                                 |
| (backslash)       |                                                                                                                                 | \. allows the period to be matched as a period and not as any single character. |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| [ ]               | Matches the characters or range of characters separated by a hyphen within the square brackets.                                 | [01234a-f] matches 0, 1, 2, b, but not 5, g, or A.                              |
| (square brackets) |                                                                                                                                 |                                                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| ^ (caret)         | Marks the beginning of an input string.                                                                                         | ^123 matches 1234, but not 0123                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| ? (question mark) | Matches one occurrence or no occurrence of the preceding character                                                              | ab?c matches abc and ac                                                         |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| $ (dollar sign)   | Marks the end of an input string                                                                                                | 123$ matches 123 but not 1234                                                   |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| * (asterisk)      | Matches zero or more instances of the immediately preceding string and acts as a wildcard for matching any number of characters | com* matches computer, community, and also control                              |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| + (plus)          | Matches one or more instances of the immediately preceding string                                                               | com+ matches computer, community, but not control                               |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| | (pipe)          | Matches one of the characters that appear on either side of the pipe operator.                                                  | 012|34 matches 0124 and 0134 but not 01234                                      |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+


**Note**

- Special characters (space, question mark, pipe) require quotation marks around the expression.

**Example**
::

    rule 10 deny regex "65500:6667|65500:6680|65500:6683|65500:6691|65500:6692|65500:6693|65500:6694"



---

## commit.rst

commit
------

**Minimum user role:** operator

This command applies candidate configuration changes only. If no changes are made and commit is triggered, no action will be taken and an error message is displayed.
Use the no-warning with the commit command to discard warning output when another session has been committed before this commit action from the same running configuration. The system will merge the last commit.

A successful commit is timestamped with user indication.

Each successful commit generates a rollback-id.

If another user has committed before you and there is a conflict, you will receive a warning and will be prompted to act:

-	commit: both the "commit" and "merge" operations will be performed

-	merge-only: only "merge" will be performed without "commit"

-	abort: no operation will be performed

To apply the changed configuration:

**Command syntax: commit** no-warning

**Command mode:** operational

**Note**

- If you attempt to exit with uncommitted configurations, a warning is issued. Enter:

	- Yes - to commit and exit to root menu

	- No - to remove the candidate configuration ("rollback 0") and exit to root menu

	- Cancel - to remain in the config hierarchy with the candidate configuration as is (do not exit). This is the default option.


..
	**Internal Note**

	commit applies only a changed (candidate) configuration. in case configuration has not changed andcommitis triggered by the user, no action will be made to database & user will be prompt with "commit action is not applicable. no configuration changes were made".

	Successful commit (for each commit type) broadcasted to all logged-in users: "commit succeeded by $user at HH:MM:SS DD-MM-YYYY"

	Commit no-warning: Optional flag added to commit command. If the flag exists, system will discard warning output for the case in other session had been commit before the desired committed action from the same running configuration. System will merge last commit. flag valid also for commit checkcommand

	Each successful commit generates rollback-id, latest (current running configuration) has rollback-id 0. Overall 50 rollbacks supported with FIFO mechanism.

	If there are uncommitted configurations when user exits, CLI output will be: "Warning: Configuration includes uncommitted changes, would you like to commit them before exiting (yes,no,cancel)[cancel]?"

	"yes" - commit and exit to root menu

	"no" - remove the candidate config ("rollback 0") and exit to root menu

	"cancel" - remain in "cfg" menu with the candidate config as is.

	For the case multiple users have committed and there is a conflict, the user will get the following warning:

	Warning: User <name> committed at <time>, your configuration is out of sync. What would you like to do (commit, merge-only, abort) [abort]? "

	"commit" will perform the merge and commit operation

	"merge-only" will perform the merge without commit check operation

	"abort" will not perform any operation

	The default option is cancel


**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interface ge100-1/1/1 mac-address 10:22:33:44:55:00
	dnRouter(cfg)# interface bundle-1 mac-address 00:00:00:00:00:01
	dnRouter(cfg)# commit
	Commit succeeded by ADMIN at 27-Jan-2017 22:11:00 UTC
	
	dnRouter(cfg)# commit
	Commit action is not applicable. no configuration changes were made
	
	dnRouter(cfg)# interface bundle-1 mac-address 00:00:00:00:00:02
	dnRouter(cfg)# no interface bundle-1
	dnRouter(cfg)# commit
	Commit check failed on:
		interface bundle-1

.. **Help line:** Commit the set of changes to the database and cause the changes to take operational effect

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 6.0         | Command introduced    |
+-------------+-----------------------+
---

## rollback.rst

rollback
--------

**Minimum user role:** operator

Each successful commit generates a transaction file with a rollback-id. You
can use this rollback-id to rollback the configuration in a specific
transaction file (undoing subsequent commits).

When a new commit is performed, the new commit (now the new running
configuration) receives the rollback-id 0 and the rollback-id of every
previous commit increases by 1. The system saves 50 rollback files (in
addition to rollback-0, which is the running configuration). When the
rollback-id pool is full, the oldest commit (rolback-id 50) is removed to make
room for the new commit (i.e. first-in-first-out).

<INSERT 02_transactions>

Each rollback file contains the following information:

-	Date and time

-	System version

-	User name (the user who initiated the change)

-	Optional logging comment

The rollback action loads the configuration to the candidate database. It is
not automatically committed.

To roll back to a saved transaction:


**Command syntax: rollback** [rollback-id]

**Command mode:** operational

**Note**

- Rollback 0 returns to the current configuration.

..
	**Internal Note**

	- No broadcasting to other users

**Parameter table**

+----------------+--------------------------------------------------------------+-----------+-------------+
| Parameter      | Description                                                  | Range     | Default     |
+================+==============================================================+===========+=============+
| rollback-id    | The unique identifier for each committed configuration.      | 0..49     | 0           |
+----------------+--------------------------------------------------------------+-----------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# rollback 10
	Configuration rollback complete

.. **Help line:** Rollback to a saved transaction file

**Command History**

+-------------+-----------------------+
| Release     | Modification          |
+=============+=======================+
| 6.0         | Command introduced    |
+-------------+-----------------------+
---

## transaction_overview.rst

Transaction Commands
--------------------

You need to commit your changes to save them to the database and for them to
take operational effect. DNOS supports configuration transactions, enabling
multiple users to simultaneously configure the system. Every transaction
receives a unique identifier. All user performed actions are saved as a
candidate configuration until the configuration is committed. This allows to
verify the configuration without impacting the running configuration. This
also enables to roll back to a previous configuration, even after commit.

<INSERT 01_transactions>

In the above example, the running configuration ID is #1. User A performs
changes to the configuration. The changes are saved to a candidate
configuration 1A. When User A commits the changes, the changes are merged to
the running configuration with a new ID #2.

Each successful commit generates a transaction file with a rollback-id. You
can use this rollback-id to rollback the configuration in a specific
transaction file (undoing subsequent commits).

When a new commit is performed, the new commit (now the new running
configuration) receives the rollback-id 0 and the rollback-id of every
previous commit increases by 1. The system saves 50 rollback files (in
addition to rollback-0, which is the running configuration). When the
rollback-id pool is full, the oldest commit (rolback-id 50) is removed to make
room for the new commit (i.e. first-in-first-out).

<INSERT 02_transactions>

Each rollback file contains the following information:

-	Date and time

-	System version

-	User name (the user who initiated the change)

-	Optional logging comment

The NCC maintains an object relational mapping database (ORM DB) that holds
the configuration. The ORM DB is replicated on the standby NCC and is updated
with new commits. At NCC switchover, the standby NCC (now active ) is ready
with the most recent configuration.

<INSERT 03_transactions>

Changes made by multiple concurrent users are saved in separate candidate
configuration files. The first user to commit will not encounter any conflict
during commit. Subsequent users may encounter such conflict, if their
candidate configuration conflicts with the committed configuration. For
example (see image below), if User A makes configuration changes to its Cand
2A and deletes an interface X while User B changes the IP address of interface
X in Cand 2B and User A commits first, User B's IP change cannot be committed.
In this case, User B will be notified of the conflict and will be prompted to
revise or cancel the configuration. Only after the conflict is resolved, will
User B be allowed to merge the Cand B changes to the v3 running configuration.

<INSERT 04_transactions>

If after User A successfully commits changes, User C begins to make changes to
the configuration (on configuration ID #3) and commits, Cand 3C will not
conflict, even though Cand 2B may not yet be resolved.

<INSERT 05_transactions>

It is good practice to run the show config command or commit check to check
the configuration before committing a new configuration. These commands
trigger the committed changes and you will be notified of any conclicts that
may arise during commit.

You can abort a commit using the Ctrl+C keyboard shortcut. You will be
prompted to confirm the abort operation.

If during the commit a fail occurs that causes the NCC reset, the NCC will be
loaded with the last successfully committed configuration.

**Note:** If the SSH session terminates during the commit, the commit will
proceed.

To save your changes to the configuration, use the "commit" transaction
commands in configuration mode:

+----------+--------------------------------------------------------------------------------------------------------------------------------+
| Option   | Description                                                                                                                    |
+----------+--------------------------------------------------------------------------------------------------------------------------------+
| commit   | Applies changed configuration.                                                                                                 |
+----------+--------------------------------------------------------------------------------------------------------------------------------+
| check    | Verifies that the candidate configuration is syntactically correct, but does not commit the changes.                           |
+----------+--------------------------------------------------------------------------------------------------------------------------------+
| confirm  | Confirms the commit and applies it immediately.                                                                                |
+----------+--------------------------------------------------------------------------------------------------------------------------------+
| and-quit | Commits the configuration and, if the configuration contains no errors and the commit succeeds, exits from configuration mode. |
+----------+--------------------------------------------------------------------------------------------------------------------------------+
| log      | Adds a comment that describes the committed configuration                                                                      |
+----------+--------------------------------------------------------------------------------------------------------------------------------+
---

## commit and-exit.rst

commit and-exit
---------------

**Minimum user role:** operator

To commit the configuration and, if the configuration contains no errors and the commit succeeds, exit configuration mode:

**Command syntax: commit and-exit**

**Command mode:** operational

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interface bundle-1 mac-address 00:00:00:00:00:01
	dnRouter(cfg)# commit and-exit
	Commit succeeded by ADMIN at 27-Jan-2017 22:11:00 UTC
	dnRouter#

.. **Help line:** Commit the configuration and exit from configuration mode

**Command History**

+-------------+----------------------------------------------------------+
|             |                                                          |
| Release     | Modification                                             |
+=============+==========================================================+
|             |                                                          |
| 6.0         | Command introduced                                       |
+-------------+----------------------------------------------------------+
|             |                                                          |
| 11.0        | Command syntax: replaced "and-quit"   with "and-exit"    |
+-------------+----------------------------------------------------------+
---

## commit check.rst

commit check
------------

**Minimum user role:** operator

The system performs the following checks on the candidate configuration:

-	Syntax check

-	System validation checks

-	Resources check (where available) - for data path configuration (QoS, Access-lists, etc.).

You will receive a warning, if another user has committed before you and there is a conflict and will be prompted to act:

-	check-and-merge: both the "merge" and "commit check" operations will be performed

-	merge-only: only "merge" will be performed without "commit check"

-	abort: no operation will be performed

To verify that the candidate configuration is syntactically correct without committing the changes:

**Command syntax: commit check**

**Command mode:** operational

..
	**Internal Note**

	The checks performed:

	- Syntax check

	- System validations, YANG validations, XPath check

	- Resources check (where available). i.e for data path configurations (QoS, ACL etc)

	- For the case multiple users have committed and there is a conflict, the user will get the following warning:

	- Warning: User <name> committed at <time>, your configuration is out of sync. What would you like to do (check-and-merge, merge-only, abort) [abort]? "

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interface ge100-1/1/1 mac-address 10:22:33:44:55:00
	dnRouter(cfg)# interface bundle-1 mac-address 00:00:00:00:00:01
	dnRouter(cfg)# commit check
	Commit check passed successfully
	
	dnRouter(cfg)# interface bundle-1 mac-address 00:00:00:00:00:01
	dnRouter(cfg)# no interface bundle-1
	dnRouter(cfg)# commit check
	Commit check failed on:
		interface bundle-1

.. **Help line:** Verify that the candidate configuration is syntactically correct, but do not commit the changes

**Command History**

+-------------+--------------------------------------------+
|             |                                            |
| Release     | Modification                               |
+=============+============================================+
|             |                                            |
| 6.0         | Command introduced                         |
+-------------+--------------------------------------------+
|             |                                            |
| 11.5        | Updated options for conflicting commits    |
+-------------+--------------------------------------------+
---

## commit confirm.rst

commit confirm
--------------

**Minimum user role:** operator

In order for the commit to permanently apply, you must confirm the commit within the specified time using the commit command. Any user can confirm the commit. If the commit is not confirmed within the allocated time, the configuration automatically rolls back to the pre-commit state.

To confirm the commit:

**Command syntax: commit confirm** [confirm-time]

**Command mode:** operational

**Note**

- If another commit confirm is already running, you will not be able to confirm until the previous confirm is complete.

- To cancel a commit, use the "clear system commit" command.

- You can optionally display the currently pending commit confirm with the remaining time.

**Parameter table**

+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
|                 |                                                                                                                                                                            |             |             |
| Parameter       | Description                                                                                                                                                                | Range       | Default     |
+=================+============================================================================================================================================================================+=============+=============+
|                 |                                                                                                                                                                            |             |             |
| confirm-time    | The time (in minutes) to wait for a commit   confirm following a commit action. After this time, the commit will   automatically roll back if no commit action is done.    | 1..65535    | 10          |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interface bundle-1 mac-address 00:00:00:00:00:01
	dnRouter(cfg)# commit confirm
	Commit confirm will automatically rollback in 10 minutes unless confirmed
	Commit succeeded by ADMIN at 27-Jan-2017 22:11:00 UTC
	dnRouter(cfg)# commit
	Commit confirm
	
	dnRouter(cfg)# interface bundle-1 mac-address 00:00:00:00:00:01
	dnRouter(cfg)# commit confirm 30
	Commit confirm will be automatically rolled back in 30 minutes unless confirmed
	
	...(no commit been made)
	Configuration commit rollback by ADMIN at 27-Jan-2017 22:11:00 UTC

.. **Help line:** Time (in minutes) before the commit will be automatically rollbacked

**Command History**

+-------------+-----------------------+
|             |                       |
| Release     | Modification          |
+=============+=======================+
|             |                       |
| 6.0         | Command introduced    |
+-------------+-----------------------+
---

## commit log.rst

commit log
----------

**Minimum user role:** operator

You can add a description of the committed configuration. The added comment is displayed in the show rollback output to help you identify the content of the commit.

To add a comment that describes the committed configuration:

**Command syntax: commit** [action] log [comment]

**Command mode:** operational

**Note**

- The log flag is applicable only to the "commit" and "commit and-quit" commands.

**Parameter table**
+-----------+-----------------------------------------------+--------------+---------+
| Parameter | Description                                   | Range        | Default |
+-----------+-----------------------------------------------+--------------+---------+
| action    | Enter the commit action that you want to run. | none         | \-      |
|           |                                               | and-exit     |         |
|           |                                               | and-confirm  |         |
+-----------+-----------------------------------------------+--------------+---------+
| comment   | Enter a comment that describes the commit.    | 1..512 bytes | \-      |
+-----------+-----------------------------------------------+--------------+---------+

**Example**
::

	dnRouter# configure
	dnRouter(cfg)# interface bundle-1 mac-address 00:00:00:00:00:01
	dnRouter(cfg)# commit and-quit log my first commit
	Commit succeeded by ADMIN at 27-Jan-2017 22:11:00 UTC
	dnRouter#


.. **Help line:** Add a comment that describes the committed configuration

**Command History**

+---------+-------------------------+
| Release | Modification            |
+---------+-------------------------+
| 10.0    | Command introduced      |
+---------+-------------------------+
| 17.1    | Updated range parameter |
+---------+-------------------------+

---

