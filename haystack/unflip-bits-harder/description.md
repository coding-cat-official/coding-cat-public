After initial fixes to sanitize your telemetry data, management decided to upgrade the log format. Now each entry comes with a precise timestamp and a sensor reading. The bit-flip issue persists, so some readings are negative due to transmission glitches.

Your task: reorder the entire log by the absolute value of the readings, while keeping the original relative order for entries that have the same absolute value. The timestamps must stay attached to their readings.

Remember: do **not** fix the bit-flip or alter the readings—just reorder the logs so the dashboard displays them in order of increasing magnitude.

The higher-ups want the logs “cleaner,” but don’t ask questions about the hardware.
