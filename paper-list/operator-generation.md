# 算子生成


## Meta Info


论文数量: 3

更新时间: 2026-04-14


## Papers


### the ai cuda engineer


**核心思想 (Idea)**


KernelBench健壮性不足，模型容易硬编码或考虑输入情况不足，且没有考虑反向传播

提出了新的benchmark

消融实验的启发：

多模型同时sample效果更好；

prompt中如何排列和组织经验对结果有影响，例如论文中从性能低到高排列经验效果最好。


**来源**: arxiv2509


---


### cuda-llm


**核心思想 (Idea)**


总结、迭代的

kernel generation agent雏形


**来源**: arxiv2506


---


### gpu kernel scitentist


**核心思想 (Idea)**


构建经验有一个值得参考的idea：

不仅是总结上限最高的经验，还总结下限最高的经验和最稳定的经验


**来源**: arxiv2508


---

