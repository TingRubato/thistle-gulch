from datetime import datetime

from thistle_gulch.bridge import RuntimeBridge
from . import Demo

CATEGORY = "Simulation Commands"


class SetStartTimeDemo(Demo):
    def __init__(self):
        super().__init__(
            name="Set Start Time",
            description="Set the start time of the simulation.",
            category=CATEGORY,
            function=self.set_start_time_demo,
        )

    def set_start_time_demo(self, bridge: RuntimeBridge):
        """
        Set the start time of the simulation.

        :param bridge: The bridge to the runtime.
        """

        datestr = input("Enter the start hour (HH - 24hour)")
        date = datetime(1880, 1, 1, int(datestr))

        async def on_ready(_):
            print(f"Setting the start time of the simulation to {date}")
            await bridge.runtime.api.set_start_date(date)

        print("Registering custom on_ready callback.")
        bridge.on_ready = on_ready