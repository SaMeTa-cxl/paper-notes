# 训推一体


本页面收集了 训推一体 相关的论文及其核心思想。


总共 3 篇论文


---


### LLMStation


1.prefill时抢占training，decode和forward融合，

decode与backward并行；

2.根据时延预测器或历史时延预测时延，进而计算出最大的满足SLO的并行度

3.使用协程来实现可暂停的反向传播


*来源: ATC25 ETH*


### Sirius


空分复用，动态调整training的batch size。如何快速调整，并重新分配显存？直接丢弃正在计算的batch，等待正在更新权重的batch。如何解决GPU kernel的异步执行？由CPU来维护执行一个队列。


*来源: ATC25 IPADS*


### FlexLLM


token-level finetune 

mechanism


*来源: NSDI2026 CMU、Stanford、Purdue*

