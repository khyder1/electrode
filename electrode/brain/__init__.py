#!/usr/bin/env python3
"""
Brain module.

The master file for the simulator.
"""

from typing import Tuple
import networkx as nx

from .. import timing
from ..neuron import Neuron
from ..synapse import Synapse


class Brain:
    """
    Brains handle simulator-pools.

    More details inline.
    """

    def __init__(self, **kwargs):
        """
        Create a new Brain object to control neurons.

        Arguments:
            time_resolution (int : 500): Number of ns between "frames"

        """
        # Set defaults.
        # Time resolution is 0.5 millis
        self.time_resolution = kwargs.get('time_resolution', timing.ms(0.5))
        self._graph = nx.Graph()
        self.loaded = False
        self._neurons = []  # type: List[Neuron]
        self._synapses = []  # type: List[Synapse]

    def __getitem__(self, key):
        """
        Get a neuron or segment data.

        Arguments:
            key (str[2]): The index to look up in the network

        Returns:
            Segment

        """
        raise NotImplementedError()

    def compile(self, reduce: bool = True):
        """
        Simplify the graph and load it into the networkx graph.

        Arguments:
            reduce (bool : True): Whether to attempt to reduce degree=2 edges
                to a simplified, more optimized graph.

        Returns:
            None

        """
        self.loaded = True
        self._graph = nx.Graph()
        if reduce:
            self._graph = nx.compose_all([
                neuron for neuron in self._neurons
            ])

            for synapse in self._synapses:
                self._graph.add_edge(
                    synapse[0],
                    synapse[1],
                    synapse[2]
                )

    def run(self) -> bool:
        """
        Begin running the simulation.

        Return True on every step, unless an error is encountered.

        Arguments:
            None

        Returns:
            bool: True when successful, False otherwise.

        """
        raise NotImplementedError()

    def add_neuron(self, neuron):
        """
        Add a new neuron to the network. Adds resultant connections.

        Cannot be run after a call to .compile().

        Arguments:
            neuron (electrode.Neuron): The neuron to add.

        Returns:
            None

        """
        if not isinstance(neuron, Neuron):
            raise TypeError("Neuron must implement electrode.neuron.Neuron.")
        if self.loaded:
            raise RuntimeError(
                "You cannot call `add_neuron` after a call to `compile`."
            )
        self._neurons.append(neuron)

    def add_synapse(
            self,
            synapse: Synapse,
            source: Tuple[str, str],
            sink: Tuple[str, str]
    ):
        """
        Add a new synapse to the network.

        Arguments:
            synapse (electrode.Synapse): The synapse to add
            source (str[2]): The presynaptic segment
            sink (str[2]): The postsynaptic segment

        Returns:
            None

        """
        self._synapses.append(
            source, sink, synapse
        )
        raise NotImplementedError()
