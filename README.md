# Deep Feature Perturbation
**[update 3/15/2020]**

Official implementation of the paper: ["Diversified Arbitrary Style Transfer via Deep Feature Perturbation"](https://arxiv.org/abs/1909.08223) (**CVPR 2020**)

The deep feature perturbation (DFP) operation uses an orthogonal random noise matrix to perturb the deep image feature maps while keeping the original style information unchanged. This operation can be easily integrated into many existing [WCT (whitening and coloring transform)](https://arxiv.org/pdf/1705.08086.pdf)-based methods (e.g., [1. UniversalStyleTransfer](https://github.com/Yijunmaverick/UniversalStyleTransfer), [2. Avatar-Net](https://github.com/LucasSheng/avatar-net), [3. FastPhotoStyle](https://github.com/NVIDIA/FastPhotoStyle)), and empower them to generate diverse results for arbitrary styles. 

![show](https://github.com/EndyWon/Deep-Feature-Perturbation/blob/master/figures/show.png)

### Environment Required:
