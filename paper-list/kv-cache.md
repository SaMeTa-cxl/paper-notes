# KVCache


本页面收集了 KVCache 相关的论文及其核心思想。


总共 32 篇论文


---


### minicache


inter-layer kv similarity -> 

merge adjacent layers


### xKV


multiple inter-layer kv merge


### omniKV


找出attention相似的连续层规律

然后在每个连续相似层的首层取出接下来相似层的attention


### AirCache


多模态（文本+图片），先筛选重要文本token，

与视觉token作attention，按importance和strength进行动态分配每层budget


*来源: 阿里，iccv25*


### LLMaaS


根据token的重要性来动态量化


### H2O


通过attention累加和来找重要token，并驱逐其他token


*来源: nips23*


### FastGen


根据每个attention head的不同

attention模式进行不同的驱逐


*来源: nips23*


### StreamingLLM


local window + 最开始的一些

token


### Quest


Query-aware的kv驱逐策略，让QKV做了一堆没法解释的

计算和reduction，然后莫名其妙就work了


*来源: iclr25，MIT*


### Attention Drop


根据每层输入和输出的相似性

来决定是否直接跳过整一层


### SimlayerKV


发现有的层只关注最开始的和最近的token，对这些层只保留最开始的和最近的token

感觉就是layer-level的StreamingLLM


### PageAttention


把KV cache切分成等size的block，

映射到不连续的物理块上，解决了内存碎片的问题


### R-KV


CoT场景下的kv cache驱逐，

观察到CoT大量输出同语义内容

导致互评高attention的问题，在

选择重要token时增加多样性的评价标准


### snapKV


基于observation window来决定重要

token


### Look-M


对图片KV cache根据重要性进行驱逐，

并将被驱逐的kv cache merge到保留下的kv cache上


### NSA


可学习的稀疏模式，利用一个门控

网络让模型自己学习需要用哪一种稀疏模式


*来源: deepseek
acl25 best paper*


### MoBA


把MoE的思想应用到attention机制上的效果，

即对于一个q，训练一个门控网络确定它需要关注的kv


*来源: kimi*


### RetrievalAttention


一部分KV固定在GPU（静态稀疏模式）另一部分KV offload到CPU

，通过KNN算出重要KV


*来源: 微软*


### MagicPig


提出通过采样的方法（LSH）

而不是Top-K方式找重要KV cache；GPU-CPU共同计算


*来源: MetaAI*


### CAKE


不仅考虑注意力分数的大小，还考虑注意力分数的变化


### NOSA


结合query无关的token选择机制（相邻decode步骤的token必然相同）和query敏感的token选择机制

提高相邻decode步骤的token相同数量，从而降低通信量


*来源: 清华*


### QServe


M4A8KV4量化，将权重反量化放在运算快的tensor core上，并设计并行反量化，加速性能；

量化范围留有余地，例如INT8量化，不量化到[0, 255]而是量化到[0,250],避免反量化时精度损失造成的溢出；

利用一些数学技巧对K和A做变换消除其中的特别大的值，使其能够更好地被量化到低精度


### Oaken


在LPU上做的一个量化工作，软硬协同优化

在量化算法层面，一是离线确定KV vector内部划分组的threshold，降低在线计算开销；二是通过将两端的值集中到中间来实现更小区间压缩，也就能更低bit压缩；三是使用了内存管理的技巧，将压缩后的离群值的一部分bit塞到非离群值压缩后的空缺中，从而使内存布局更好。

硬件层面主要是在LPU的基础上根据设计的量化算法做了针对性的改进


*来源: HyperAccel*


### HeteroCache


将attn heads从两个维度进行划分：

1. 关注的位置是否稳定；

2. 是否和同一层的其他heads关注的相似。

对于第一个维度，关注位置越稳定的压缩幅度越大；对于第二个维度，与其他heads相似性很低的不压缩，与其他heads有相似的进行聚类，聚类中心保留全部cache，其他heads大幅压缩并在聚类中心关注token的变化大于预先设定的阈值时，进行异步预取，更新其他heads的cache


*来源: arxive2601
ZJU*


### KVZip


repeat prompt恢复context，贡献越大的kv越重要


*来源: 首尔大学
nips25 oral*


### cache2cache


复用多个模型的kv cache，而不用传模型生成的文本，既提高效率也提高质量


*来源: 清华大学*


### solidattention


kv交替存储，block size不变的情况下，I/O

大小翻倍。原地替换错误kv技术。一些流水线优化，

实际代码是否使用文中的算法存疑


*来源: FAST26 交大*


### FlashVID


既关注时间局部性，也关注空间局部性；

既关注重要性，也关注多样性


*来源: ICLR26 Oral*


### QuoKA


选择有代表性的Q来筛选KV，具体来说

选择与Q的平均值最不相似的来筛选KV


*来源: ICLR26*


### FASA


用RoPE的频域视角来选重要token，

但感觉是奇技淫巧


*来源: ICLR26 阿里*


### FlashPrefill


只用几个特殊的query probe来识别attn模式

水文中的水文


*来源: arxiv*


### InfoFlow KV


RAG场景上对于是否重计算用了H2O的思路，水的一笔


*来源: arxiv*

