from mininet.topo import Topo
from mininet.link import TCLink


class OController(Topo):

    def build(self):

        # Add the OpenFlow reference controller
        controller = self.addController('c0')

        # Add the central switch
        s1 = self.addSwitch('s1')

        # Connect two hosts to the switch
        h1 = self.addHost("h1")
        h2 = self.addHost("h2")
        self.addLink(s1, h1, cls=TCLink, bw=40, delay='15ms')
        self.addLink(s1, h2, cls=TCLink, bw=40, delay='15ms')

        # Set the controller for the switch
        self.addController(s1, controller)


# the topology accessible to the mn tool's `--topo` flag
# note: if using the Dockerfile, this must be the same as in the Dockerfile
topos = {
    'minimalTopology': (lambda: OController())
}
