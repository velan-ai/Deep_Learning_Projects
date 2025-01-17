# fMRI Image Autoencoder with Enhanced Decoder Efficiency

This project develops an autoencoder to process functional MRI (fMRI) images with a novel approach to optimize training efficiency. By segmenting the decoder into **left** and **right** parts, the model aims to achieve better training time efficiency while preserving reconstruction accuracy.

## Project Description

fMRI datasets are high-dimensional, requiring significant computational resources to process. This autoencoder project tackles this challenge by:

1. **Encoder**: Compressing high-dimensional fMRI images into compact latent representations.
2. **Segmented Decoder**: Reconstructing the original image using a segmented decoder architecture, where the left and right parts independently reconstruct respective portions of the image.

This segmentation approach distributes the reconstruction workload, improving efficiency and reducing overall training time.

The dataset includes:
- **Actual fMRI images**: High-dimensional input images.
- **Reduced fMRI images**: Low-dimensional representations for training the model.

## Features

- **Segmented Decoder Architecture**: Left and right decoders handle respective parts of the image reconstruction.
- **Efficiency Optimization**: Reduces computational requirements and training time.
- **Dataset Compatibility**: Works with standard fMRI datasets.
- **Performance Evaluation**: Measures reconstruction accuracy and training efficiency.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- TensorFlow / PyTorch (depending on your implementation)
- Numpy
- Matplotlib
- Other dependencies in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd fmri-autoencoder
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Dataset Preparation

1. Prepare the dataset with this structure:
   ```
   data/
   ├── actual_images/
   └── reduced_images/
   ```
2. Place high-dimensional fMRI images in `actual_images` and the reduced images in `reduced_images`.

### Running the Autoencoder

1. Train the autoencoder:
   ```bash
   python train.py --data_dir data/ --epochs <num_epochs> --batch_size <batch_size>
   ```
2. Evaluate the model:
   ```bash
   python evaluate.py --model_path models/autoencoder_segmented.pth --data_dir data/
   ```

### Results

Training and evaluation outputs, including loss curves and reconstructed images, will be saved in the `results/` directory.

## Project Structure

```
fmri-autoencoder/
├── data/                   # Dataset directory
├── models/                 # Saved models
├── results/                # Evaluation and visualization outputs
├── train.py                # Training script
├── evaluate.py             # Evaluation script
├── autoencoder.py          # Model definition (including segmented decoder)
├── utils.py                # Helper functions
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Future Work

- Explore advanced segmentation techniques for more efficient decoders.
- Test various fMRI datasets to evaluate model generalization.
- Incorporate techniques like data augmentation or transfer learning for enhanced performance.

## Contributors

- **Velan** - Initial design and implementation.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
