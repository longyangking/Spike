# Author: Yang Long <longyang_123@yeah.net>
#
# License: LGPL-2.1

import numpy as np

class Material:
    def __init__(self,frequency,epsilon,mur,chi):
        self.frequency = frequency
        N = np.size(frequency)
        self.epsilon = np.zeros([N,3,3,3],dtype=complex)
        self.mur = np.zeros([N,3,3,3],dtype=complex)
        self.chi = np.zeros([N,3,3,3],dtype=complex)

        for i in range(N):
            if np.size(epsilon[i]) == 1:
                self.epsilon[i] = epsilon[i]*np.eye(3)
            elif np.size(epsilon[i]) == 3:
                self.epsilon[i] = np.diag(epsilon[i])
            else:
                self.epsilon[i] = epsilon[i]

            if np.size(mur[i]) == 1:
                self.mur[i] = mur[i]*np.eye(3)
            elif np.size(mur[i]) == 3:
                self.mur[i] = np.diag(mur[i])
            else:
                self.mur[i] = mur[i]

            if np.size(chi[i]) == 1:
                self.chi[i] = chi[i]*np.eye(3)
            elif np.size(chi[i]) == 3:
                self.chi[i] = np.diag(chi[i])
            else:
                self.chi[i] = chi[i]

    def opticalparameters(self):
        return self.epsilon,self.mur,self.chi