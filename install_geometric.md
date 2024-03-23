# install Python Torch Geometric

# PyTorch Geometric Installation Guide on M1 Mac

PyTorch Geometric (PyG) is a library that extends PyTorch to support graph neural networks. This guide is to help with M1 Macs install PyG and its dependencies efficiently. Since the M1 chip is ARM-based, and thus some of the libraries may require special attention for compatibility. In particular, it is not very straightforward for Anaconda users like me, as Conda packages are currently not available for Windows and M1/M2/M3 macs.

- Date: 23 March 2024
- macOS Sonoma 14.3.1

1. **Install Miniforge for ARM architecture**: Miniforge is a community-driven minimalistic conda installer. It's recommended for M1 Macs as it provides better compatibility with the ARM architecture. It is similar to Anaconda and can coexist with Anaconda.
    
    ```bash
    brew install miniforge
    ```
    
2. **Create a new conda environment**: Once Miniforge is installed, you can create a new conda environment. Open your terminal and run:
    
    ```bash
    conda create --name pyg_env python=3.11.5
    ```
    
    Here, `pyg_env` is the name of the new environment, and `python=3.11.5` specifies the Python version, which can be found by `python --version`.
    
    Then we activate it by
    
    ```bash
    conda activate pyg_env
    ```
    
    Note that in this new environment, there are no JupyterLab for example. One need to install that separately.
    
3. **Install PyTorch**: Before installing PyTorch Geometric, you need to install PyTorch. PyTorch provides instructions for installation on different platforms, including macOS with M1 chips. As of my last update, you should install PyTorch for M1 Macs using the following command. However, it's a good idea to check the official PyTorch website for the most current command:
    
    ```bash
    conda install pytorch torchvision torchaudio -c pytorch
    ```
    
    After the installation, we can check it by running
    
    ```python
    import torch
    print(torch.__version__)
    print("CUDA Available:", torch.cuda.is_available())
    ```
    
4. **Install dependencies of PyTorch Geometric**: After installing PyTorch, you can install the dependencies of Geometric.
    
    ```bash
    pip install torch-scatter torch-sparse torch-cluster torch-spline-conv -f https://data.pyg.org/whl/torch-2.2.1+cpu.html
    ```
    
    Note: Replace **`torch-2.2.1+cpu`** with the version of PyTorch you installed. This is found in the output of the last step. I don’t use CUDA so I will simply choose `cpu.`
    
    After the installation, we can check it by running
    
    ```python
    import torch
    import torch_scatter
    import torch_sparse
    import torch_cluster
    import torch_spline_conv
    
    print("torch version:", torch.__version__)
    print("torch_scatter version:", torch_scatter.__version__)
    print("torch_sparse version:", torch_sparse.__version__)
    print("torch_cluster version:", torch_cluster.__version__)
    print("torch_spline_conv version:", torch_spline_conv.__version__)
    
    # Example tensor of shape [1, 4]
    tensor = torch.tensor([[2, 1, 3, 4]], dtype=torch.float32)
    
    # Correctly reshaping the tensor to [2, 2]
    reshaped_tensor = tensor.view(2, 2)  # or tensor.reshape(2, 2)
    
    print("Reshaped tensor:", reshaped_tensor)
    ```
    
5. **Install PyTorch Geometric**: Finally, you can install PyTorch Geometric. As of my last update, the best approach is to use the following commands, but you should also check the [official installation instructions](https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html) for any updates:
    
    ```python
    pip install torch-geometric
    ```
    
    This can be checked by running
    
    ```python
    import torch_geometric
    print("torch_geometric version:", torch_geometric.__version__)
    
    # Optionally, verify with a simple operation
    from torch_geometric.data import Data
    
    edge_index = torch.tensor([[0, 1], [1, 0]], dtype=torch.long)
    num_nodes = 2
    
    data = Data(edge_index=edge_index, num_nodes=num_nodes)
    print(data)
    ```
