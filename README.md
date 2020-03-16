# Deep Feature Perturbation
**[update 3/15/2020]**

Official implementation of the paper: ["Diversified Arbitrary Style Transfer via Deep Feature Perturbation"](https://arxiv.org/abs/1909.08223) (**CVPR 2020**)

The deep feature perturbation (DFP) operation uses an orthogonal random noise matrix to perturb the deep image feature maps while keeping the original style information unchanged. This operation can be easily integrated into many existing [WCT (whitening and coloring transform)](https://arxiv.org/pdf/1705.08086.pdf)-based methods (e.g., [1. UniversalStyleTransfer](https://github.com/Yijunmaverick/UniversalStyleTransfer), [2. Avatar-Net](https://github.com/LucasSheng/avatar-net), [3. FastPhotoStyle](https://github.com/NVIDIA/FastPhotoStyle)), and empower them to generate diverse results for arbitrary styles. 

![show](https://github.com/EndyWon/Deep-Feature-Perturbation/blob/master/figures/show.jpg)

## An Example (UniversalStyleTransfer + our DFP):

* Step-1: Follow the instructions of [UniversalStyleTransfer](https://github.com/Yijunmaverick/UniversalStyleTransfer) to implement their code.

* Step-2: Put our **test_wct_DFP.lua** in the same folder as their **test_wct.lua**.

* Step-3: (1) For a single pair test:

　　　`th test_wct_DFP.lua -content YourContentPath -style YourStylePath -alpha 0.6 -lambda 0.6`

　　　**-alpha**: stylization strength, 　**-lambda**: diversity strength.
   
　　　(2) For large numbers of pair test:

　　　`th test_wct_DFP.lua -contentDir YourContentDir -styleDir YourStyleDir -alpha 0.6 -lambda 0.6`
      
## Evaluate Diversity:

We evaluate the diversity using two metrics: (1) **Pixel distance** and (2) **[LPIPS](https://arxiv.org/abs/1801.03924) distance**. (Higher means further/more different. Lower means more similar.)

* **Pixel distance**: this distance measures the difference between two images in pixel (RGB) space.

　　Example script to take the average pixel distance between all pairs of images within a directory:

　　`python compute_pixel_dists.py -d YourImageDir`
  
* **LPIPS distance**: [Learned Perceptual Image Patch Similarity (LPIPS)](https://github.com/richzhang/PerceptualSimilarity#1-learned-perceptual-image-patch-similarity-lpips-metric) metric. It computes distance in deep feature space (in our), with linear weights to better match human perceptual judgments.
