You’re part of a backend team maintaining a data pipeline that aggregates event data from multiple services in real time. Two upstream systems independently log event timestamps and forward them to your processing service. Each system guarantees that its own data is ordered chronologically, but the data arrives in two separate batches.

Before downstream services can process the data, the event stream must reflect a consistent view of time — meaning all incoming timestamps must be arranged in proper chronological order, as if they came from a single source.

Your task is to write a function that takes in these two batches of event timestamps and prepares them for the next stage of processing. Each batch is already internally ordered, but the full sequence must be processed in time order.

The system expects this task to run efficiently under load, so avoid unnecessary operations that assume disorder in the inputs.