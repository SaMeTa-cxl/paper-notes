# 推测性解码


## Meta Info


论文数量: 9

更新时间: 2026-04-14


## Papers


### block-wise parallel


**核心思想 (Idea)**


静态预测长度，预测验证重叠

需要再训练


**思考与备注**


预测验证重叠的优化效果真的大吗？

可以做做消融实验

预测只用到了output token的信息，是否信息太少了导致预测成功率不高


---


### specinfer


**核心思想 (Idea)**


构造token树，重新搞了针对于token

这样就可以一次验证整棵树


---


### Fast Inference from Transformers via Speculative Decoding


**核心思想 (Idea)**


第一篇草稿+验证的推理范式

（之前那个blockwise是并行）


---


### Medusa


**核心思想 (Idea)**


通过倒数第二层（feature层）预测

也用了token树，本质上是一个

blockwise并行 + 草稿验证的融合


**思考与备注**


他的问题和blockwise一样，也是需要用n-1预测n,n+1,n+2，也可以出现预测准确率比较低的情况，但是medusa调整了大模型接受的条件，让模型更容易接受，避免了推倒重来，这一部分没有太看懂


---


### Lookahead


---


### EAGLE 1


**核心思想 (Idea)**


features+shifted tokens预测

树形预测


**思考与备注**


MoE优化效果不佳，能否解决？

能否使用预测验证重叠？


---


### SEQUOIA


**核心思想 (Idea)**


树形预测结构优化，使

接受数量随预测树大小的指数增长


**思考与备注**


纯算法


---


### Talon


**核心思想 (Idea)**


动态控制树宽和树深


---


### DFVG


**核心思想 (Idea)**


GPU和FPGA的异构计算

### AdaServe(Eurosys26) \[[Paper](https://arxiv.org/abs/2501.12162)] \[[Code](https://github.com/zikun-li/AdaServe-Artifact-Evaluation?tab=readme-ov-file)]

**核心思想**
* 多SLO场景如何尽量满足所有SLO
* 通过调整推测解码参数（宽度、深度等），动态控制推理速度，从而动态满足不同SLO

**思考**
* 这篇论文相当于把推测解码应用在了一个实际的推理场景下，构建了一个系统
* 能不能把推测解码的思路应用在agent场景呢？
* 比如说推测工具使用？
---

