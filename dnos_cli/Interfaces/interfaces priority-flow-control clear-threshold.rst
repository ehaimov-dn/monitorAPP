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
