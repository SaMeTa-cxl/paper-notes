# MoE


本页面收集了 MoE 相关的论文及其核心思想。


总共 5 篇论文


---


### MoD


每层选择一定数量的

token作处理


### MoE++


利用zero、copy、replace expert，

每层激活动态数量的expert，使用residual routing


### AdaMoE


利用zero expert，

每层激活动态数量的expert


### MoLE


训练时专家输入改为id，推理时将专家重参数化

为查表的形式


### MoE-APEX


端侧MoE

