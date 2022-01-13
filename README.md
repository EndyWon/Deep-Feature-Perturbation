# Deep Feature Perturbation
**[update 3/20/2020]**

Official implementation of the paper: ["Diversified Arbitrary Style Transfer via Deep Feature Perturbation"](https://arxiv.org/abs/1909.08223) (**CVPR 2020**)

The deep feature perturbation (DFP) operation uses an orthogonal random noise matrix to perturb the deep image feature maps while keeping the original style information unchanged. This operation can be easily integrated into many existing [WCT (whitening and coloring transform)](https://arxiv.org/pdf/1705.08086.pdf)-based methods (e.g., [1. UniversalStyleTransfer (NIPS17)](https://github.com/Yijunmaverick/UniversalStyleTransfer), [2. Avatar-Net (CVPR18)](https://github.com/LucasSheng/avatar-net), [3. FastPhotoStyle (ECCV18)](https://github.com/NVIDIA/FastPhotoStyle)), and empower them to generate diverse results for arbitrary styles. 

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

We evaluate diversity using two metrics: (1) **Pixel distance** and (2) **[LPIPS](https://arxiv.org/abs/1801.03924) distance**. 

(**Higher means further/more different. Lower means more similar.**)

The data (6 content images and 6 style images) we used for evaluation can be found in **"evaluation_data"** directory. See **Section 5.3** in our [paper](https://arxiv.org/abs/1909.08223) for more details about the evaluation.

* **Pixel distance**: this distance measures the difference between two images in pixel (RGB) space.

　　Example script to take the average Pixel distance between all pairs of images within a directory:

　　`python compute_pixel_dists.py -d YourImageDir`
  
* **LPIPS distance**: [Learned Perceptual Image Patch Similarity (LPIPS)](https://github.com/richzhang/PerceptualSimilarity) metric. It computes distance in deep feature space, with linear weights to better match human perceptual judgments.

　　Step-1: Follow the instructions of [Richard Zhang](https://github.com/richzhang/PerceptualSimilarity) to implement their code.
  
　　Step-2: Use the script to take the average LPIPS distance between all pairs of images within a directory (see more from their [repository](https://github.com/richzhang/PerceptualSimilarity)):
        
　　`python compute_dists_pair.py -d imgs/ex_dir_pair -o imgs/example_dists_pair.txt --use_gpu`
     
## Comparison Results: 

We incorporate our DFP into [UniversalStyleTransfer](https://github.com/Yijunmaverick/UniversalStyleTransfer), [Avatar-Net](https://github.com/LucasSheng/avatar-net), [FastPhotoStyle](https://github.com/NVIDIA/FastPhotoStyle), respectively, and compare them with other two diversified style transfer methods: [ImprovedTextureNets (CVPR17)](https://github.com/DmitryUlyanov/texture_nets/tree/diversity) and [MultiTextureSynthesis (CVPR17)](https://github.com/Yijunmaverick/MultiTextureSynthesis).

| Method | ImprovedTextureNets | MultiTextureSynthesis | UniversalStyleTransfer<br> + our DFP | AvatarNet<br> + our DFP | FastPhotoStyle<br> + our DFP |
| :---:  | :---:       | :---: | :---: | :---:    | :---:         |
| **Pixel_Dist** | 0.077 | 0.080 | **0.162** | **0.102** | **0.091** |
| **LPIPS_Dist** | 0.163 | 0.175 | **0.431** | **0.264** | **0.203** |
 
![comparison](https://github.com/EndyWon/Deep-Feature-Perturbation/blob/master/figures/comparison.jpg)

## Citation:

If you find this code useful for your research, please cite the paper:

Zhizhong Wang, Lei Zhao, Haibo Chen, Lihong Qiu, Qihang Mo, Sihuan Lin, Wei Xing and Dongming Lu, "Diversified Arbitrary Style Transfer via Deep Feature Perturbation", In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2020. [[Arxiv](https://arxiv.org/abs/1909.08223)]

```
@inproceedings{wang2020diversified,
  title={Diversified arbitrary style transfer via deep feature perturbation},
  author={Wang, Zhizhong and Zhao, Lei and Chen, Haibo and Qiu, Lihong and Mo, Qihang and Lin, Sihuan and Xing, Wei and Lu, Dongming},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages={7789--7798},
  year={2020}
}
```

## Acknowledgement:

This project is based on existing WCT-based style transfer methods, including [UniversalStyleTransfer](https://github.com/Yijunmaverick/UniversalStyleTransfer), [Avatar-Net](https://github.com/LucasSheng/avatar-net), [FastPhotoStyle](https://github.com/NVIDIA/FastPhotoStyle).
