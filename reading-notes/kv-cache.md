# KVCache


## Meta Info


论文数量: 32

更新时间: 2026-04-14


## Papers


### minicache


**核心思想 (Idea)**


inter-layer kv similarity -> 

merge adjacent layers


**思考与备注**


1.minicache从固定层开始merge，能否动态调整

2.是否有连续多层相似的情况（omni），多层一起merge


---


### xKV


**核心思想 (Idea)**


multiple inter-layer kv merge


**思考与备注**


纯算法


---


### omniKV


**核心思想 (Idea)**


找出attention相似的连续层规律

然后在每个连续相似层的首层取出接下来相似层的attention


---


### AirCache


**核心思想 (Idea)**


多模态（文本+图片），先筛选重要文本token，

与视觉token作attention，按importance和strength进行动态分配每层budget


**来源**: 阿里，iccv25


---


### LLMaaS


**核心思想 (Idea)**


根据token的重要性来动态量化


---


### H2O


**核心思想 (Idea)**


通过attention累加和来找重要token，并驱逐其他token


**来源**: nips23


---


### FastGen


**核心思想 (Idea)**


根据每个attention head的不同

attention模式进行不同的驱逐


**来源**: nips23


---


### StreamingLLM


**核心思想 (Idea)**


local window + 最开始的一些

token


---


### Quest


**核心思想 (Idea)**


Query-aware的kv驱逐策略，让QKV做了一堆没法解释的

计算和reduction，然后莫名其妙就work了


**思考与备注**


让query介入的方法解释性极差

，纯炼丹


**来源**: iclr25，MIT


---


### Attention Drop


**核心思想 (Idea)**


根据每层输入和输出的相似性

来决定是否直接跳过整一层


---


### SimlayerKV


**核心思想 (Idea)**


发现有的层只关注最开始的和最近的token，对这些层只保留最开始的和最近的token

感觉就是layer-level的StreamingLLM


---


### PageAttention


**核心思想 (Idea)**


把KV cache切分成等size的block，

映射到不连续的物理块上，解决了内存碎片的问题


---


### R-KV


**核心思想 (Idea)**


CoT场景下的kv cache驱逐，

观察到CoT大量输出同语义内容

导致互评高attention的问题，在

选择重要token时增加多样性的评价标准


**思考与备注**


场景找的很巧妙，

解决方法也很简单有效


---


### snapKV


**核心思想 (Idea)**


基于observation window来决定重要

token


---


### Look-M


**核心思想 (Idea)**


对图片KV cache根据重要性进行驱逐，

并将被驱逐的kv cache merge到保留下的kv cache上


**思考与备注**


感觉merge的可解释性不是很强，

为什么对两个向量作平均就能保留一部分信息呢，

为什么不需要重新学习


---


### NSA


**核心思想 (Idea)**


可学习的稀疏模式，利用一个门控

网络让模型自己学习需要用哪一种稀疏模式


**思考与备注**


问题在于首先需要重新训练，

其次可选择的模式本身有限


**来源**: deepseek
acl25 best paper


---


### MoBA


**核心思想 (Idea)**


把MoE的思想应用到attention机制上的效果，

即对于一个q，训练一个门控网络确定它需要关注的kv


**来源**: kimi


---


### RetrievalAttention


**核心思想 (Idea)**


一部分KV固定在GPU（静态稀疏模式）另一部分KV offload到CPU

，通过KNN算出重要KV


**思考与备注**


还有一个有意思的点，这篇文章提到了用CPU做attention计算，

这一点记得在flexgen中也有所提及。只能用于decode阶段，可否迁移到prefill阶段？


**来源**: 微软


---


### MagicPig


**核心思想 (Idea)**


提出通过采样的方法（LSH）

而不是Top-K方式找重要KV cache；GPU-CPU共同计算


**思考与备注**


指出了一个Top-K方法的痛点：benchmark只选了"retrieval"类型的，本身就只需要少量上下文，对于内容提取这样的任务，

准确率下降显著。


**来源**: MetaAI


---


### CAKE


**核心思想 (Idea)**


不仅考虑注意力分数的大小，还考虑注意力分数的变化


**思考与备注**


但是使用方差来衡量变化是否合理呢？


---


### NOSA


**核心思想 (Idea)**


结合query无关的token选择机制（相邻decode步骤的token必然相同）和query敏感的token选择机制

提高相邻decode步骤的token相同数量，从而降低通信量


**思考与备注**


看他的说法，通信似乎和计算是不重叠的，

为什么没做重叠


**来源**: 清华


---


### QServe


**核心思想 (Idea)**


M4A8KV4量化，将权重反量化放在运算快的tensor core上，并设计并行反量化，加速性能；

量化范围留有余地，例如INT8量化，不量化到[0, 255]而是量化到[0,250],避免反量化时精度损失造成的溢出；

利用一些数学技巧对K和A做变换消除其中的特别大的值，使其能够更好地被量化到低精度


---


### Oaken


**核心思想 (Idea)**


在LPU上做的一个量化工作，软硬协同优化

在量化算法层面，一是离线确定KV vector内部划分组的threshold，降低在线计算开销；二是通过将两端的值集中到中间来实现更小区间压缩，也就能更低bit压缩；三是使用了内存管理的技巧，将压缩后的离群值的一部分bit塞到非离群值压缩后的空缺中，从而使内存布局更好。

硬件层面主要是在LPU的基础上根据设计的量化算法做了针对性的改进


**思考与备注**


感觉还是挺有深度的一篇，软硬协同

就是能不能在GPU上也做类似的软硬协同的量化优化呢


**来源**: HyperAccel


---


### HeteroCache


**核心思想 (Idea)**


将attn heads从两个维度进行划分：

1. 关注的位置是否稳定；

2. 是否和同一层的其他heads关注的相似。

对于第一个维度，关注位置越稳定的压缩幅度越大；对于第二个维度，与其他heads相似性很低的不压缩，与其他heads有相似的进行聚类，聚类中心保留全部cache，其他heads大幅压缩并在聚类中心关注token的变化大于预先设定的阈值时，进行异步预取，更新其他heads的cache


**思考与备注**


这两个维度的划分不会随输入发生变化吗？

聚类中心head真的能很好的替代其他heads的功能吗？

能不能把这个东西做成一个kernel，再想一点算法上的优化


**来源**: arxive2601
ZJU


---


### KVZip


**核心思想 (Idea)**


repeat prompt恢复context，贡献越大的kv越重要


**来源**: 首尔大学
nips25 oral


---


### cache2cache


**核心思想 (Idea)**


复用多个模型的kv cache，而不用传模型生成的文本，既提高效率也提高质量


**思考与备注**


多模态图片KV cache能这么干吗

RAG文本位置不同，能不能不同模型复用

多agent复用重要token的index


**来源**: 清华大学


---


### solidattention


**核心思想 (Idea)**


kv交替存储，block size不变的情况下，I/O

大小翻倍。原地替换错误kv技术。一些流水线优化，

实际代码是否使用文中的算法存疑


**思考与备注**


能不能动态block size，pipeline能不能再

优化，预测算法能不能优化，kv块的存储方式能不能再改进一下


**来源**: FAST26 交大


---


### FlashVID


**核心思想 (Idea)**


既关注时间局部性，也关注空间局部性；

既关注重要性，也关注多样性


**思考与备注**


基本上又是新瓶装旧酒


**来源**: ICLR26 Oral


---


### QuoKA


**核心思想 (Idea)**


选择有代表性的Q来筛选KV，具体来说

选择与Q的平均值最不相似的来筛选KV


**来源**: ICLR26


---


### FASA


**核心思想 (Idea)**


用RoPE的频域视角来选重要token，

但感觉是奇技淫巧


**来源**: ICLR26 阿里


---


### FlashPrefill


**核心思想 (Idea)**


只用几个特殊的query probe来识别attn模式

水文中的水文


**来源**: arxiv


---


### InfoFlow KV


**核心思想 (Idea)**


RAG场景上对于是否重计算用了H2O的思路，水的一笔


**思考与备注**


RAG重计算和顺序问题感觉都是纯炼丹，灌水重灾区，实在没点子了再往这想吧太水了


**来源**: arxiv


---

