"""
Parent class for all agents
"""

import typing

from swarmrl.actions.actions import Action
from swarmrl.components.colloid import Colloid


class Agent:
    """
    Parent class for a SwarmRL Agent.
    """

    def compute_agent_state(
        self, colloids: typing.List[Colloid]
    ) -> typing.Tuple[typing.List[Action]]:
        """
        Compute the state of the system based on the current colloid position.

        Returns
        -------
        actions: typing.List[Action]
                Return the action the colloid should take.
        kill_switch : bool
                Flag capable of ending simulation.
        """
        raise NotImplementedError("Implemented in Child class.")
