# Implementation of Pass Use Case

In the context of P4, it is important to highlight that no P4 program has been developed for
this specific use case ``Pass``. This steams from the unique nature of P4 programming, where each
program is expected to explicitly define the entire path. P4 programs must indicate outline the
entire processing pipeline with the [``BMV2``](https://github.com/p4lang/behavioral-model) switches. For example, we need to define the datapath
or specific instructions in ``sX-runtime.json`` files when the packets arrive to the [``BMV2``](https://github.com/p4lang/behavioral-model) switches. In
addition, the [``Mininet``](https://github.com/mininet/mininet) environment will be used to execute each scenario such as [``Drop``](../Drop/) , [``Pass``](.), [``Echo Server``](../Echo_server/), [``L3 Forwarding``](../L3_forwarding/) and [``Broadcast``](../Broadcast/). Consequently, there is no direct way to delegate packet
processing in P4, particularly for this specific use case.


