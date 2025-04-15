from estimator import *
schemes.Kyber512
LWE.primal_usvp(schemes.Kyber512)
r = LWE.estimate.rough(schemes.Kyber512)
r = LWE.estimate(schemes.Kyber512)

schemes.Falcon512_SKR
r = NTRU.estimate.rough(schemes.Falcon512_SKR)
r = NTRU.estimate(schemes.Falcon512_SKR)