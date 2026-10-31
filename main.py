"""Basic PyTorch sanity check for the alphazero-lab environment."""

import numpy as np
import torch


def main() -> None:
    # Pick the best available device: Apple Silicon (MPS), CUDA, or CPU.
    if torch.backends.mps.is_available():
        device = torch.device("mps")
    elif torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    print(f"PyTorch version: {torch.__version__}")
    print(f"NumPy version:   {np.__version__}")
    print(f"Using device:    {device}")

    # Tiny tensor operation: build two tensors and matrix-multiply them.
    a = torch.arange(6, dtype=torch.float32, device=device).reshape(2, 3)
    b = torch.ones(3, 2, device=device)
    c = a @ b

    print("\na =\n", a)
    print("\nb =\n", b)
    print("\na @ b =\n", c)


if __name__ == "__main__":
    main()
