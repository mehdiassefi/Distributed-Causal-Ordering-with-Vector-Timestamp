# Distributed-Causal-Ordering-with-Vector-Timestamp
In this project, we focus on designing and implementing a distributed concurrency control system for IFTTT. 
In order to implement a distributed concurrency control to be used in IFTTT systems, we propose to use a distributed causal ordering with vector timestamp and also using the Lamport's timestamp. 
Using causal multicast, we make sure that for any pair of events that are not concurrent, we obey the causal ordering. 
By using the Lamport's timestamp, we make sure that there is a right ordering for concurrent events. 