You're working on a telemetry dashboard for a hardware system that’s a bit... unpredictable. It’s not mission-critical or anything—it’s just for logging fluctuations in subsystem #7. Lately, there’s been a weird bit-flip issue in the serializer, so sometimes positive numbers come through negative. We're *pretty sure* it's just a display glitch, not an actual hardware failure. Management has decided we’re not going to fix the sensor; software devs aren't allowed to touch the hardware without proper supervision and clearance.

You’re not allowed to “fix” the bit-flip. Just fix the output by sorting the readings by
*magnitude*, regardless of the sign, and hope no one notices.

This fix is temporary. Like most temporary fixes, it will be in production for the next 6 years.
