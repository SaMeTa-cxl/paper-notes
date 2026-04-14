# 训推一体


## Meta Info


论文数量: 3

更新时间: 2026-04-14


## Papers


### LLMStation


**核心思想 (Idea)**


1.prefill时抢占training，decode和forward融合，

decode与backward并行；

2.根据时延预测器或历史时延预测时延，进而计算出最大的满足SLO的并行度

3.使用协程来实现可暂停的反向传播


**思考与备注**


场景上更符合“训推一体”的

概念


**来源**: ATC25 ETH


---


### Sirius


**核心思想 (Idea)**


空分复用，动态调整training的batch size。如何快速调整，并重新分配显存？直接丢弃正在计算的batch，等待正在更新权重的batch。如何解决GPU kernel的异步执行？由CPU来维护执行一个队列。


**思考与备注**


训练似乎只有单卡上跑小模型，不支持TP？

训练模型和推理模型独立，只是单纯的把两种任务打包在一起打满GPU利用率。


**来源**: ATC25 IPADS


---


### FlexLLM


**核心思想 (Idea)**


token-level finetune 

mechanism


**思考与备注**


需要手动指定PEFT网络，能否自动识别

所需的adapter


**来源**: NSDI2026 CMU、Stanford、Purdue


---

