# Serving


## Meta Info


论文数量: 5

更新时间: 2026-04-14


## Papers

### Scaling LLM Test-Time Compute with Mobile NPU onSmartphones(Eurosys26) \[[Paper](https://arxiv.org/abs/2509.23324)] \[[Code](https://github.com/haozixu/llama.cpp-npu)] 

**核心思想**
* 利用Test-Time Scaling方法（如beam search），提高模型能力的同时，提高NPU利用率，因为
decode阶段Query只有一个token，对NPU的Matrix Multiplication Unit利用率低。
* 设计了tile-based的量化策略，也是针对NPU硬件特点的优化
* 打表优化softmax和反量化
---