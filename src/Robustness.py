# import numpy as np
#
class Elementary:

    def __init__(self, signal):
        """:parameter signal  -p (signal>=0)"""
        self.signal = signal

    def get_value(self, t):
        return self.signal[t]


# class Until:
#
#     def __init__(self, phi, ksi, time_range: (np.float, np.float)):
#         """
#         phi Until ksi
#         :param phi:
#         :param ksi:
#         """
#         self.phi = phi
#         self.ksi = ksi
#         self.time_range = time_range
#
#     def get_value(self, t):
#         # inf - min
#         # sup - max
#
#         # ρ(φ UI ψ, w, t) = sup        min {ρ(ψ, w, t′), inf ρ(φ, w, t′′)}
#         #                   t′ ∈t + I                    t′′ ∈[t, t′]
#
#         t_hat = t+self.time_range[0]
#
#         pass
