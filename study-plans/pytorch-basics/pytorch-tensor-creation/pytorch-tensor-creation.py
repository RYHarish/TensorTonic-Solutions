import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    """
    if method == "zeros":
        ans = torch.zeros(shape)
    elif method == "ones":
        ans =torch.ones(shape)
    elif method == "full":
        ans = torch.full(shape, value)
        
    return ans.tolist()