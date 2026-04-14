# 推测性解码


本页面收集了 推测性解码 相关的论文及其核心思想。


总共 9 篇论文


---


### block-wise parallel


静态预测长度，预测验证重叠

需要再训练


### specinfer


构造token树，重新搞了针对于token

这样就可以一次验证整棵树


### Fast Inference from Transformers via Speculative Decoding


第一篇草稿+验证的推理范式

（之前那个blockwise是并行）


### Medusa


通过倒数第二层（feature层）预测

也用了token树，本质上是一个

blockwise并行 + 草稿验证的融合


### Lookahead


### EAGLE 1


features+shifted tokens预测

树形预测


### SEQUOIA


树形预测结构优化，使

接受数量随预测树大小的指数增长


### Talon


动态控制树宽和树深


### DFVG


GPU和FPGA的异构计算

