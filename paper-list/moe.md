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

