# MoE


## Meta Info


论文数量: 5

更新时间: 2026-04-14


## Papers


### MoD


**核心思想 (Idea)**


每层选择一定数量的

token作处理


---


### MoE++


**核心思想 (Idea)**


利用zero、copy、replace expert，

每层激活动态数量的expert，使用residual routing


---


### AdaMoE


**核心思想 (Idea)**


利用zero expert，

每层激活动态数量的expert


---


### MoLE


**核心思想 (Idea)**


训练时专家输入改为id，推理时将专家重参数化

为查表的形式


**思考与备注**


训练开销？


---


### MoE-APEX


**核心思想 (Idea)**


端侧MoE


---

### FineMoE(Eurosys26) \[[Paper](https://arxiv.org/abs/2502.05370)] \[[Code](https://github.com/IntelliSys-Lab/FineMoE-EuroSys26)] 

**核心思想**
* 迭代级别的专家驱逐与预取
* 对于每个迭代，保存输入和所有层的专家选取概率，称为expert map
* 前d层用输入来匹配expert map，据此预取前d层所有专家
* 后L-d=l层用前l-d层的专家概率来匹配
* expert map的空间有限制，超限时进行驱逐

**思考**
* 第一层的预取没法提前做，而且感觉有较大的匹配开销
* 会不会出现所有expert map相似度都低的情况，这种情况下预取命中率肯定低