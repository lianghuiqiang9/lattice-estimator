from estimator import *

params = LWE.Parameters(n=1024, q=2**32, Xs=ND.DiscreteGaussian(6.4), Xe=ND.DiscreteGaussian(6.4), m=2**25)
print(params)

LWE.estimate(params) #执行全部评估，启用多线程
"""LWE.estimate.rough(params) #遵从某些假设和启发式，粗略估计"""

"然后再选择p，满足最少\sqrt(N)次的加法，失败概率不高于\delta"
"失败概率在哪里呢"


"测试结果表明，这个基本上保证了120比特的安全，没有达到128比特安全吧"