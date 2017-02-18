# Author: Yang Long <longyang_123@yeah.net>
#
# License: LGPL-2.1

import numpy as np

class OpticalTMM:
    def __init__(self,materiallist,heights,frequency):
        self.materiallist = materiallist
        self.heights = heights
        self.frequency = frequency
        
    def opticalbehavoir(self,angle=0,inputmaterial=None,outputmaterial=None,frequency=None):
        if inputmaterial is None:
            N = np.size(self.frequency)
            inputmaterial = Material(self.frequency,np.ones(N),np.ones(N),np.zeros(N))      # Air

        if outputmaterial is None:
            N = np.size(self.frequency)
            outputmaterial = Material(self.frequency,np.ones(N),np.ones(N),np.zeros(N))     # Air
        
        if frequency is None:
            frequency = self.frequency

        N = np.size(frequency)
        t = np.zeros(N,dtype=complex)
        r = np.zeros(N,dtype=complex)
        a = np.zeros(N,dtype=complex)

        # TODO

        return t,r,a

    def bulkbandstructure(self,points=31,maxband=8):
        # All structure will be regarded as a unit cell to calculate the band structure
        a = np.sum(self.heights)
        k = np.pi/a*np.linspace(-1,1,points)
        eigenfrequency = np.zeros([points,maxband])

        maxfrequency = np.max(self.frequency)
        minfrequency = np.min(self.frequency)

        # TODO

        return k,eigenfrequency

    def surfacebandstructure(self,points=31,maxband=8,direction=0,kLB=-1,kUB=1):
        # All structure will be regarded as a unit cell to calculate the band structure
        if direction == 0:
            a = np.sum(self.heights)
            k = np.pi/a*np.linspace(kLB,KUB,points)
        else:
            a = np.sum(self.heights)
            k = np.pi/a*np.linspace(-1,1,points)
        eigenfrequency = np.zeros([points,maxband])

        maxfrequency = np.max(self.frequency)
        minfrequency = np.min(self.frequency)

        # TODO

        return k,eigenfrequency

    def bulkeigenstate(self,frequency):

    def surfaceeigenstate(self,frequency):

    def isofrequencycontour(self,frequency):

    def heatradiation(self):