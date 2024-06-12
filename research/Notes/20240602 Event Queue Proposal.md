## Summary

The following research note proposes using an [[Global State-Event Queue|event queue]] for taking care of:

1. The [[Request Ride Wiring|requests for rides]] that are coming up
2. The timing of any [[Complete Ride Wiring|rides be complete]]
3. Potentially some control actions related to the probing of the latest rides or things happening for demand prediction or similar.

## Event Queue Structure

- The [[Global State-Event Queue|event queue]] will be a list of elements with the type of [[Event Queue Element Type]]
- The following is the type definition:
![[Event Queue Element Type]]
- Finally, at all times the queue will be sorted so that the element that is popped out has the minimum date and the event queue is ordered by date in this way
## Event Queue Starting State

- There are three options for starting state:
	- If a parameter is used which fills up the starting state with an event queue that is reasonable. It could be over a timeframe of a month for example and denote every single ride request that is going to happen
	- The [[Request Ride Wiring]] could always append the next ride request each time. This would mean that the starting state of the queue would be just one single ride request and the queue would continue to fill up one at a time after each wiring completes.
	- A combination could be used to do a similar thing by having a parameter fill in the next time each [[rider]] present in the system is going to request a ride, but then use the second method to fill in the next time after it for that specific rider. I.e. if there is N riders in the system then at any time there are exactly N events in the event queue for requesting rides
## Example

An example using the first option might look like this:

1. Initialize the queue with the following items:

<code>[(t=5, action="Request Ride", spaces=({..., ride_time=6})),
(t=10, action="Request Ride", spaces=({..., ride_time=50})),
(t=25, action="Request Ride", spaces=({..., ride_time=10}))]</code>

2. The first item gets popped off and is accepted, now there is a complete ride action added to the queue at t = 5 + 6

<code>[(t=10, action="Request Ride", spaces=({..., ride_time=50})),
(t=11, action="Complete Ride", spaces=({...})),
(t=25, action="Request Ride", spaces=({..., ride_time=10}))]</code>

3. The next action is for requesting a ride, it is accepted and the time for the complete action is 10 + 50

<code>[(t=11, action="Complete Ride", spaces=({...})),
(t=25, action="Request Ride", spaces=({..., ride_time=10})),
(t=60, action="Complete Ride", spaces=({...}))]</code>

4. The ride is completed, this is where potentially the next requested ride is added with some delta time, but for this example we will assume we fed in all requests that will happen so it terminates that action there and does all the mechanisms for finishing a ride

<code>[(t=25, action="Request Ride", spaces=({..., ride_time=10})),
(t=60, action="Complete Ride", spaces=({...}))]</code>

5. A ride is requested at t=25, however it is rejected so no complete queue action is added

<code>[(t=60, action="Complete Ride", spaces=({...}))]</code>

6. The complete ride action is complete, leaving the queue empty

<code>[]</code>

7. The queue is empty so the simulation is complete!