Legend
======

The following excerpt from ``man (1) sar``

Report I/O and transfer rate statistics
---------------------------------------

tps
  Total number of transfers per second that were issued to physical devices.
  A transfer is an I/O request to a physical device. Multiple logical
  requests can be combined into a single I/O request to the device.
  A transfer is of indeterminate size.

rtps
  Total number of read requests per second issued to physical devices.

wtps
  Total number of write requests per second issued to physical devices.

bread/s
  Total amount of data read from the devices in blocks per second.
  Blocks are equivalent to sectors with 2.4 kernels and newer
  and therefore have a size of 512 bytes. With older kernels, a block is of
  indeterminate size.

bwrtn/s
  Total amount of data written to devices in blocks per second.


Report paging statistics
------------------------

pgpgin/s
  Total number of kilobytes the system paged in from disk per second.
  Note: With old kernels (2.2.x) this value is a number of blocks per
  second (and not kilobytes).

pgpgout/s
  Total number of kilobytes the system paged out to disk per second.
  Note: With old kernels (2.2.x) this value is a number of blocks per
  second (and not kilobytes).

fault/s
  Number of page faults (major + minor) made by the system per second.
  This is not a count of page faults that generate I/O, because some page
  faults can be resolved without I/O.

majflt/s
  Number of major faults the system has made per second, those which
  have required loading a memory page from disk.

pgfree/s
  Number of pages placed on the free list by the system per second.

pgscank/s
  Number of pages scanned by the kswapd daemon per second.

pgscand/s
  Number of pages scanned directly per second.

pgsteal/s
  Number of pages the system has reclaimed from cache (pagecache and
  swapcache) per second to satisfy its memory demands.

%vmeff
  Calculated as pgsteal / pgscan, this is a metric of the efficiency of
  page reclaim. If it is near 100% then almost every page coming off the
  tail of the inactive list is being reaped. If it gets too low (e.g. less
  than 30%) then the virtual memory is having some difficulty.
  This field is displayed as zero if no pages have been scanned during the
  interval of time.


Report activity for each block device
-------------------------------------

tps
  Indicate the number of transfers per second that were issued to the device.
  Multiple logical requests can be combined into a single I/O request to the
  device. A transfer is of indeterminate size.

rd_sec/s
  Number of sectors read from the device. The size of a sector is 512 bytes.

wr_sec/s
  Number of sectors written to the device. The size of a sector is 512 bytes.

avgrq-sz
  The average size (in sectors) of the requests that were issued to the device.

avgqu-sz
  The average queue length of the requests that were issued to the device.

await
  The average time (in milliseconds) for I/O requests issued to the device
  to be served. This includes the time spent by the requests in queue and
  the time spent servicing them.

svctm
  The average service time (in milliseconds) for I/O requests that were issued
  to the device.

%util
  Percentage of CPU time during which I/O requests were issued to the device
  (bandwidth utilization for the device). Device saturation occurs when this
  value is close to 100%.


Report power management statistics
----------------------------------

MHz
  CPU clock frequency in MHz.


Report network statistics
-------------------------

IFACE
  Name of the network interface for which statistics are reported.

rxpck/s
  Total number of packets received per second.

txpck/s
  Total number of packets transmitted per second.

rxkB/s
  Total number of kilobytes received per second.

txkB/s
  Total number of kilobytes transmitted per second.

rxcmp/s
  Number of compressed packets received per second (for cslip etc.).

txcmp/s
  Number of compressed packets transmitted per second.

rxmcst/s
  Number of multicast packets received per second.

rxerr/s
  Total number of bad packets received per second.

txerr/s
  Total number of errors that happened per second while transmitting packets.

coll/s
  Number of collisions that happened per second while transmitting packets.

rxdrop/s
  Number of received packets dropped per second because of a lack of space in 
  linux buffers.

txdrop/s
  Number of transmitted packets dropped per second because of a lack of space in
  linux buffers.

txcarr/s
  Number of carrier-errors that happened per second while transmitting packets.

rxfram/s
  Number of frame alignment errors that happened per second on received packets.

rxfifo/s
  Number of FIFO overrun errors that happened per second on received packets.

txfifo/s
  Number of FIFO overrun errors that happened per second on transmitted packets.

call/s
  Number of RPC requests made per second.

retrans/s
  Number of RPC requests per second, those which needed to be retransmitted 
  (for example because of a server timeout).

read/s
  Number of 'read' RPC calls made per second.

write/s
  Number of 'write' RPC calls made per second.

access/s
  Number of 'access' RPC calls made per second.

getatt/s
  Number of 'getattr' RPC calls made per second.

scall/s
  Number of RPC requests received per second.

badcall/s
  Number of bad RPC requests received per second, those whose processing 
  generated an error.

packet/s
  Number of network packets received per second.

udp/s
  Number of UDP packets received per second.

tcp/s
  Number of TCP packets received per second.

hit/s
  Number of reply cache hits per second.

miss/s
  Number of reply cache misses per second.

sread/s
  Number of 'read' RPC calls received per second.

swrite/s
  Number of 'write' RPC calls received per second.

saccess/s
  Number of 'access' RPC calls received per second.

sgetatt/s
  Number of 'getattr' RPC calls received per second.

totsck
  Total number of sockets used by the system.

tcpsck
  Number of TCP sockets currently in use.

udpsck
  Number of UDP sockets currently in use.

rawsck
  Number of RAW sockets currently in use.

ip-frag
  Number of IP fragments currently in use.

tcp-tw
  Number of TCP sockets in TIME_WAIT state.

irec/s
  The total number of input datagrams received from interfaces per second, 
  including those received in error [ipInReceives].

fwddgm/s
  The number of input datagrams per second, for which this entity was not
  their final IP destination, as a result of which an attempt
  was made to find a route to forward them to that final
  destination [ipForwDatagrams].

idel/s
  The total number of input datagrams successfully delivered per second
  to IP user-protocols (including ICMP) [ipInDelivers].

orq/s
  The total number of IP datagrams which local IP user-protocols (including ICMP)
  supplied per second to IP in requests for transmission [ipOutRequests].
  Note that this counter does not include any datagrams counted in fwddgm/s.

asmrq/s
  The number of IP fragments received per second which needed to be
  reassembled at this entity [ipReasmReqds].

asmok/s
  The number of IP datagrams successfully re-assembled per second [ipReasmOKs].

fragok/s
  The number of IP datagrams that have been successfully
  fragmented at this entity per second [ipFragOKs].

fragcrt/s
  The number of IP datagram fragments that have been
  generated per second as a result of fragmentation at this entity [ipFragCreates].

ihdrerr/s
  The number of input datagrams discarded per second due to errors in
  their IP headers, including bad checksums, version number
  mismatch, other format errors, time-to-live exceeded, errors
  discovered in processing their IP options, etc. [ipInHdrErrors]

iadrerr/s
  The number of input datagrams discarded per second because the IP
  address in their IP header's destination field was not a
  valid address to be received at this entity. This count
  includes invalid addresses (e.g., 0.0.0.0) and addresses of
  unsupported Classes (e.g., Class E). For entities which are
  not IP routers and therefore do not forward datagrams, this
  counter includes datagrams discarded because the destination
  address was not a local address [ipInAddrErrors].

iukwnpr/s
  The number of locally-addressed datagrams received
  successfully but discarded per second because of an unknown or
  unsupported protocol [ipInUnknownProtos].

idisc/s
  The number of input IP datagrams per second for which no problems were
  encountered to prevent their continued processing, but which
  were discarded (e.g., for lack of buffer space) [ipInDiscards].
  Note that this counter does not include any datagrams discarded while
  awaiting re-assembly.

odisc/s
  The number of output IP datagrams per second for which no problem was
  encountered to prevent their transmission to their
  destination, but which were discarded (e.g., for lack of
  buffer space) [ipOutDiscards].
  Note that this counter would include
  datagrams counted in fwddgm/s if any such packets met
  this (discretionary) discard criterion.

onort/s
  The number of IP datagrams discarded per second because no route could
  be found to transmit them to their destination [ipOutNoRoutes].
  Note that this counter includes any packets counted in fwddgm/s
  which meet this 'no-route' criterion.
  Note that this includes any datagrams which a host cannot route because all
  of its default routers are down.

asmf/s
  The number of failures detected per second by the IP re-assembly
  algorithm (for whatever reason: timed out, errors, etc) [ipReasmFails].
  Note that this is not necessarily a count of discarded IP
  fragments since some algorithms can lose track of the number of
  fragments by combining them as they are received.

fragf/s
  The number of IP datagrams that have been discarded per second because
  they needed to be fragmented at this entity but could not
  be, e.g., because their Don't Fragment flag was set [ipFragFails].

imsg/s
  The total number of ICMP messages which the entity
  received per second [icmpInMsgs].
  Note that this counter includes all those counted by ierr/s.

omsg/s
  The total number of ICMP messages which this entity
  attempted to send per second [icmpOutMsgs].
  Note that this counter includes all those counted by oerr/s.

iech/s
  The number of ICMP Echo (request) messages received per second [icmpInEchos].

iechr/s
  The number of ICMP Echo Reply messages received per second [icmpInEchoReps].

oech/s
  The number of ICMP Echo (request) messages sent per second [icmpOutEchos].

oechr/s
  The number of ICMP Echo Reply messages sent per second [icmpOutEchoReps].

itm/s
  The number of ICMP Timestamp (request) messages received per second [icmpInTimestamps].

itmr/s
  The number of ICMP Timestamp Reply messages received per second [icmpInTimestampReps].

otm/s
  The number of ICMP Timestamp (request) messages sent per second [icmpOutTimestamps].

otmr/s
  The number of ICMP Timestamp Reply messages sent per second [icmpOutTimestampReps].

iadrmk/s
  The number of ICMP Address Mask Request messages received per second [icmpInAddrMasks].

iadrmkr/s
  The number of ICMP Address Mask Reply messages received per second [icmpInAddrMaskReps].

oadrmk/s
  The number of ICMP Address Mask Request messages sent per second [icmpOutAddrMasks].

oadrmkr/s
  The number of ICMP Address Mask Reply messages sent per second [icmpOutAddrMaskReps].

ierr/s
  The number of ICMP messages per second which the entity received but
  determined as having ICMP-specific errors (bad ICMP
  checksums, bad length, etc.) [icmpInErrors].

oerr/s
  The number of ICMP messages per second which this entity did not send
  due to problems discovered within ICMP such as a lack of buffers [icmpOutErrors].

idstunr/s
  The number of ICMP Destination Unreachable messages
  received per second [icmpInDestUnreachs].

odstunr/s
  The number of ICMP Destination Unreachable messages sent per second [icmpOutDestUnreachs].

itmex/s
  The number of ICMP Time Exceeded messages received per second [icmpInTimeExcds].

otmex/s
  The number of ICMP Time Exceeded messages sent per second [icmpOutTimeExcds].

iparmpb/s
  The number of ICMP Parameter Problem messages received per second [icmpInParmProbs].

oparmpb/s
  The number of ICMP Parameter Problem messages sent per second [icmpOutParmProbs].

isrcq/s
  The number of ICMP Source Quench messages received per second [icmpInSrcQuenchs].

osrcq/s
  The number of ICMP Source Quench messages sent per second [icmpOutSrcQuenchs].

iredir/s
  The number of ICMP Redirect messages received per second [icmpInRedirects].

oredir/s
  The number of ICMP Redirect messages sent per second [icmpOutRedirects].

active/s
  The number of times TCP connections have made a direct
  transition to the SYN-SENT state from the CLOSED state per second [tcpActiveOpens].

passive/s
  The number of times TCP connections have made a direct
  transition to the SYN-RCVD state from the LISTEN state per second [tcpPassiveOpens].

iseg/s
  The total number of segments received per second, including those
  received in error [tcpInSegs].  This count includes segments received on
  currently established connections.

oseg/s
  The total number of segments sent per second, including those on
  current connections but excluding those containing only
  retransmitted octets [tcpOutSegs].

atmptf/s
  The number of times per second TCP connections have made a direct
  transition to the CLOSED state from either the SYN-SENT
  state or the SYN-RCVD state, plus the number of times per second TCP
  connections have made a direct transition to the LISTEN
  state from the SYN-RCVD state [tcpAttemptFails].

estres/s
  The number of times per second TCP connections have made a direct
  transition to the CLOSED state from either the ESTABLISHED
  state or the CLOSE-WAIT state [tcpEstabResets].

retrans/s
  The total number of segments retransmitted per second - that is, the
  number of TCP segments transmitted containing one or more
  previously transmitted octets [tcpRetransSegs].

isegerr/s
  The total number of segments received in error (e.g., bad
  TCP checksums) per second [tcpInErrs].

orsts/s
  The number of TCP segments sent per second containing the RST flag [tcpOutRsts].

idgm/s
  The total number of UDP datagrams delivered per second to UDP users [udpInDatagrams].

odgm/s
  The total number of UDP datagrams sent per second from this entity [udpOutDatagrams].

noport/s
  The total number of received UDP datagrams per second for which there
  was no application at the destination port [udpNoPorts].


idgmerr/s
  The number of received UDP datagrams per second that could not be
  delivered for reasons other than the lack of an application
  at the destination port [udpInErrors].

tcp6sck
  Number of TCPv6 sockets currently in use.


udp6sck
  Number of UDPv6 sockets currently in use.

raw6sck
  Number of RAWv6 sockets currently in use.

ip6-frag
  Number of IPv6 fragments currently in use.

irec6/s
  The total number of input datagrams received from
  interfaces per second, including those received in error
  [ipv6IfStatsInReceives].

fwddgm6/s
  The number of output datagrams per second which this
  entity received and forwarded to their final
  destinations [ipv6IfStatsOutForwDatagrams].

idel6/s
  The total number of datagrams successfully
  delivered per second to IPv6 user-protocols (including ICMP)
  [ipv6IfStatsInDelivers].

orq6/s
  The total number of IPv6 datagrams which local IPv6
  user-protocols (including ICMP) supplied per second to IPv6 in
  requests for transmission [ipv6IfStatsOutRequests].
  Note that this counter
  does not include any datagrams counted in fwddgm6/s.

asmrq6/s
  The number of IPv6 fragments received per second which needed
  to be reassembled at this interface [ipv6IfStatsReasmReqds].

asmok6/s
  The number of IPv6 datagrams successfully
  reassembled per second [ipv6IfStatsReasmOKs].

imcpck6/s
  The number of multicast packets received per second
  by the interface [ipv6IfStatsInMcastPkts].

omcpck6/s
  The number of multicast packets transmitted per second
  by the interface [ipv6IfStatsOutMcastPkts].

fragok6/s
  The number of IPv6 datagrams that have been
  successfully fragmented at this output interface per second
  [ipv6IfStatsOutFragOKs].

fragcr6/s
  The number of output datagram fragments that have
  been generated per second as a result of fragmentation at
  this output interface [ipv6IfStatsOutFragCreates].

ihdrer6/s
  The number of input datagrams discarded per second due to
  errors in their IPv6 headers, including version
  number mismatch, other format errors, hop count
  exceeded, errors discovered in processing their
  IPv6 options, etc. [ipv6IfStatsInHdrErrors]

iadrer6/s
  The number of input datagrams discarded per second because
  the IPv6 address in their IPv6 header's destination
  field was not a valid address to be received at
  this entity. This count includes invalid
  addresses (e.g., ::0) and unsupported addresses
  (e.g., addresses with unallocated prefixes). For
  entities which are not IPv6 routers and therefore
  do not forward datagrams, this counter includes
  datagrams discarded because the destination address
  was not a local address [ipv6IfStatsInAddrErrors].

iukwnp6/s
  The number of locally-addressed datagrams
  received successfully but discarded per second because of an
  unknown or unsupported protocol [ipv6IfStatsInUnknownProtos].

i2big6/s
  The number of input datagrams that could not be
  forwarded per second because their size exceeded the link MTU
  of outgoing interface [ipv6IfStatsInTooBigErrors].

idisc6/s
  The number of input IPv6 datagrams per second for which no
  problems were encountered to prevent their
  continued processing, but which were discarded
  (e.g., for lack of buffer space)
  [ipv6IfStatsInDiscards]. Note that this
  counter does not include any datagrams discarded
  while awaiting re-assembly.

odisc6/s
  The number of output IPv6 datagrams per second for which no
  problem was encountered to prevent their
  transmission to their destination, but which were
  discarded (e.g., for lack of buffer space)
  [ipv6IfStatsOutDiscards]. Note
  that this counter would include datagrams counted
  in fwddgm6/s if any such packets
  met this (discretionary) discard criterion.

inort6/s
  The number of input datagrams discarded per second because no
  route could be found to transmit them to their
  destination [ipv6IfStatsInNoRoutes].

onort6/s
  The number of locally generated IP datagrams discarded per second
  because no route could be found to transmit them to their
  destination [unknown formal SNMP name].

asmf6/s
  The number of failures detected per second by the IPv6
  re-assembly algorithm (for whatever reason: timed
  out, errors, etc.) [ipv6IfStatsReasmFails].
  Note that this is not
  necessarily a count of discarded IPv6 fragments
  since some algorithms
  can lose track of the number of fragments
  by combining them as they are received.

fragf6/s
  The number of IPv6 datagrams that have been
  discarded per second because they needed to be fragmented
  at this output interface but could not be
  [ipv6IfStatsOutFragFails].

itrpck6/s
  The number of input datagrams discarded per second because
  datagram frame didn't carry enough data
  [ipv6IfStatsInTruncatedPkts].

imsg6/s
  The total number of ICMP messages received
  by the interface per second which includes all those
  counted by ierr6/s [ipv6IfIcmpInMsgs].
 
omsg6/s
  The total number of ICMP messages which this
  interface attempted to send per second [ipv6IfIcmpOutMsgs].

iech6/s
  The number of ICMP Echo (request) messages
  received by the interface per second [ipv6IfIcmpInEchos].

iechr6/s
  The number of ICMP Echo Reply messages received
  by the interface per second [ipv6IfIcmpInEchoReplies].


oechr6/s
  The number of ICMP Echo Reply messages sent
  by the interface per second [ipv6IfIcmpOutEchoReplies].

igmbq6/s
  The number of ICMPv6 Group Membership Query
  messages received by the interface per second
  [ipv6IfIcmpInGroupMembQueries].

igmbr6/s
  The number of ICMPv6 Group Membership Response messages
  received by the interface per second
  [ipv6IfIcmpInGroupMembResponses].

ogmbr6/s
  The number of ICMPv6 Group Membership Response
  messages sent per second
  [ipv6IfIcmpOutGroupMembResponses].

igmbrd6/s
  The number of ICMPv6 Group Membership Reduction messages
  receved by the interface per second
  [ipv6IfIcmpInGroupMembReductions].

ogmbrd6/s
  The number of ICMPv6 Group Membership Reduction
  messages sent per second
  [ipv6IfIcmpOutGroupMembReductions].

irtsol6/s
  The number of ICMP Router Solicit messages
  received by the interface per second
  [ipv6IfIcmpInRouterSolicits].

ortsol6/s
  The number of ICMP Router Solicitation messages
  sent by the interface per second
  [ipv6IfIcmpOutRouterSolicits].

irtad6/s
  The number of ICMP Router Advertisement messages
  received by the interface per second
  [ipv6IfIcmpInRouterAdvertisements].

inbsol6/s
  The number of ICMP Neighbor Solicit messages
  received by the interface per second
  [ipv6IfIcmpInNeighborSolicits].

onbsol6/s
  The number of ICMP Neighbor Solicitation
  messages sent by the interface per second
  [ipv6IfIcmpOutNeighborSolicits].

inbad6/s
  The number of ICMP Neighbor Advertisement
  messages received by the interface per second
  [ipv6IfIcmpInNeighborAdvertisements].

onbad6/s
  The number of ICMP Neighbor Advertisement
  messages sent by the interface per second
  [ipv6IfIcmpOutNeighborAdvertisements].

ierr6/s
  The number of ICMP messages per second which the interface
  received but determined as having ICMP-specific
  errors (bad ICMP checksums, bad length, etc.)
  [ipv6IfIcmpInErrors]

idtunr6/s
  The number of ICMP Destination Unreachable
  messages received by the interface per second
  [ipv6IfIcmpInDestUnreachs].

odtunr6/s
  The number of ICMP Destination Unreachable
  messages sent by the interface per second
  [ipv6IfIcmpOutDestUnreachs].

itmex6/s
  The number of ICMP Time Exceeded messages
  received by the interface per second
  [ipv6IfIcmpInTimeExcds].

otmex6/s
  The number of ICMP Time Exceeded messages sent
  by the interface per second
  [ipv6IfIcmpOutTimeExcds].

iprmpb6/s
  The number of ICMP Parameter Problem messages
  received by the interface per second
  [ipv6IfIcmpInParmProblems].

oprmpb6/s
  The number of ICMP Parameter Problem messages
  sent by the interface per second
  [ipv6IfIcmpOutParmProblems].

iredir6/s
  The number of Redirect messages received
  by the interface per second
  [ipv6IfIcmpInRedirects].

oredir6/s
  The number of Redirect messages sent by
  the interface by second
  [ipv6IfIcmpOutRedirects].

ipck2b6/s
  The number of ICMP Packet Too Big messages
  received by the interface per second
  [ipv6IfIcmpInPktTooBigs].

opck2b6/s
  The number of ICMP Packet Too Big messages sent
  by the interface per second
  [ipv6IfIcmpOutPktTooBigs].

idgm6/s
  The total number of UDP datagrams delivered per second to UDP users
  [udpInDatagrams].

odgm6/s
  The total number of UDP datagrams sent per second from this
  entity [udpOutDatagrams].

noport6/s
  The total number of received UDP datagrams per second for which there
  was no application at the destination port [udpNoPorts].

idgmer6/s
  The number of received UDP datagrams per second that could not be
  delivered for reasons other than the lack of an application
  at the destination port [udpInErrors].


Report queue length and load averages
-------------------------------------

runq-sz
  Run queue length (number of tasks waiting for run time). 

plist-sz
  Number of tasks in the task list.

ldavg-1
  System load average for the last minute.
  The load average is calculated as the average number of runnable or
  running tasks (R state), and the number of tasks in uninterruptible
  sleep (D state) over the specified interval.

ldavg-5
  System load average for the past 5 minutes.

ldavg-15
  System load average for the past 15 minutes.


Report memory utilization statistics
------------------------------------

kbmemfree
  Amount of free memory available in kilobytes.

kbmemused
  Amount of used memory in kilobytes. This does not take into account memory
  used by the kernel itself.

%memused
  Percentage of used memory.

kbbuffers
  Amount of memory used as buffers by the kernel in kilobytes.

kbcached
  Amount of memory used to cache data by the kernel in kilobytes.

kbcommit
  Amount of memory in kilobytes needed for current workload. This is an estimate
  of how much RAM/swap is needed to guarantee that there never is out of memory.

%commit
  Percentage of memory needed for current workload in relation to the total 
  amount of memory (RAM+swap). This number may be greater than 100% because 
  the kernel usually overcommits memory.


Report memory statistics
------------------------

frmpg/s
  Number of memory pages freed by the system per second.
  A negative value represents a number of pages allocated by the system.
  Note that a page has a size of 4 kB or 8 kB according to the machine architecture.

bufpg/s
  Number of additional memory pages used as buffers by the system per second.
  A negative value means fewer pages used as buffers by the system.

campg/s
  Number of additional memory pages cached by the system per second.
  A negative value means fewer pages in the cache.


Report swap space utilization statistics
----------------------------------------

kbswpfree
  Amount of free swap space in kilobytes.

kbswpused
  Amount of used swap space in kilobytes.

%swpused
  Percentage of used swap space.

kbswpcad
  Amount of cached swap memory in kilobytes. This is memory that once was 
  swapped out, is swapped back in but still also is in the swap area 
  (if memory is needed it doesn't need to be swapped out again because it is 
  already in the swap area. This saves I/O).

%swpcad
  Percentage of cached swap memory in relation to the amount of used swap space.


Report CPU utilization
----------------------

%user
  Percentage of CPU utilization that occurred while executing at the user
  level (application). Note that this field includes time spent running
  virtual processors.

%usr
  Percentage of CPU utilization that occurred while executing at the user
  level (application). Note that this field does NOT include time spent
  running virtual processors.

%nice
  Percentage of CPU utilization that occurred while executing at the user
  level with nice priority.

%system
  Percentage of CPU utilization that occurred while executing at the system
  level (kernel). Note that this field includes time spent servicing
  hardware and software interrupts.

%sys
  Percentage of CPU utilization that occurred while executing at the system
  level (kernel). Note that this field does NOT include time spent servicing
  hardware or software interrupts.

%iowait
  Percentage of time that the CPU or CPUs were idle during which
  the system had an outstanding disk I/O request.

%steal
  Percentage of time spent in involuntary wait by the virtual CPU
  or CPUs while the hypervisor was servicing another virtual processor.

%irq
  Percentage of time spent by the CPU or CPUs to service hardware interrupts.

%soft
  Percentage of time spent by the CPU or CPUs to service software interrupts.

%guest
  Percentage of time spent by the CPU or CPUs to run a virtual processor.

%idle
  Percentage of time that the CPU or CPUs were idle and the system
  did not have an outstanding disk I/O request.


Report status of inode, file and other kernel tables.
----------------------

dentunusd
  Number of unused cache entries in the directory cache.

file-nr
  Number of file handles used by the system.

inode-nr
  Number of inode handlers used by the system.

pty-nr
  Number of pseudo-terminals used by the system.


Report task creation and system switching activity
--------------------------------------------------

proc/s
  Total number of tasks created per second.

cswch/s
  Total number of context switches per second.


Report swapping statistics
--------------------------

pswpin/s
  Total number of swap pages the system brought in per second.

pswpout/s
  Total number of swap pages the system brought out per second.

Report TTY device activity
--------------------------

rcvin/s
  Number of receive interrupts per second for current serial line. Serial line 
  number is given in the TTY column.

xmtin/s
  Number of transmit interrupts per second for current serial line.

framerr/s
  Number of frame errors per second for current serial line.

prtyerr/s
  Number of parity errors per second for current serial line.

brk/s
  Number of breaks per second for current serial line.

ovrun/s
  Number of overrun errors per second for current serial line.
