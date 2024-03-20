import logging
import sys
import fable_saga.server as saga_server

import thistle_gulch.bridge as tg_bridge

from demos import Demo
import demos.override_action_options as action_overrides
import demos.simulation_commands as simulation_commands


def main():
    # Run the bridge.
    bridge = tg_bridge.main(auto_run=False)

    # A list of available demos and the corresponding endpoint they override.
    options = [
        # (saga_server.SagaServer, "actions_endpoint"),
        # (action_overrides.PrintActionsAndPickFirst, "actions_endpoint"),
        # (action_overrides.SkipSagaAlwaysDoTheDefaultAction, "actions_endpoint"),
        # (action_overrides.ReplaceContextWithYamlDump, "actions_endpoint"),
        # (action_overrides.UseLlama2Model, "actions_endpoint"),
        (simulation_commands.SetStartTimeDemo()),
    ]

    # Print the available demos and prompt the user to select one.
    print ("\n -= Available Demos =- ")
    for i, item in enumerate(options):
        print(f"{i}: {item.name}")
    while True:
        try:
            pick = int(input("Pick a demo to run: "))
            if pick >= len(options) or pick < 0:
                print("Invalid input. Please enter a number between 0 and", len(options))
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Set the actions endpoint to the selected demo.
    item = options[pick]
    item.function(bridge)
    #
    # elif item[1] == "actions_endpoint":
    #     tg_bridge.BridgeConfig.actions_endpoint = item[0]()
    bridge.run()


if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                        format='<%(levelname)s> %(asctime)s - %(name)s - %(pathname)s:%(lineno)d\n    %(message)s')
    main()
