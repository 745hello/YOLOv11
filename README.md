# YOLOv11

## ULCF 消融实验结构

已在以下目录提供可直接使用的消融模型配置：

- `/home/runner/work/yolov11/yolov11/yolov11/ultralytics/cfg/models/11/ablation`

分组如下：

- G0: Baseline
- G1: Baseline + DCAF
- G2: Baseline + FDSG
- G3: Baseline + DetectGLR
- G4: Baseline + DCAF + FDSG + DetectGLR
- G5: Baseline + DCAF + FDSG
- G6: Baseline + DCAF + DetectGLR
- G7: Baseline + FDSG + DetectGLR

结构敏感性分组如下：

- S1: 通道保守配置（160/320/640）
- S2: 通道激进配置（224/384/768）
- S3: FDSG level 映射替代（2/3/4）
- S4: DCAF 三分支输入替代

统一实验结构配置：

- `/home/runner/work/yolov11/yolov11/yolov11/ultralytics/cfg/experiments/yolo11-ulcf-ablation.yaml`

该配置定义了：

- 统一对比指标（主指标 mAP50-95）
- 固定非目标变量
- 三阶段预算（快速筛选 / 正式对比 / 报告复核）
- 多随机种子（默认 0/1/2）

## 运行示例

```bash
cd /home/runner/work/yolov11/yolov11/yolov11

yolo task=detect mode=train \
  model=ultralytics/cfg/models/11/ablation/yolo11-ablation-g0-baseline.yaml \
  data=your_data.yaml epochs=300 batch=16 imgsz=640 seed=0 \
  project=runs/ablation name=g0_seed0 save_json=True
```

将 `model` 换成各组配置即可复现实验矩阵。
