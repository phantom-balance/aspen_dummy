"nn_utils.py"

import torch


def save_checkpoint(state, filename=f"MODEL/nn_surrogate.pth.tar"):
    print("__Saving Checkpoint__")
    torch.save(state, filename)


def load_checkpoint(model, optimizer, checkpoint):
    print("__Loading Checkpoint__")
    model.load_state_dict(checkpoint['state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer'])



# def train_(model, loader, criterion, optimizer):
#     for batch_idx, (data, targets) in enumerate(loader):
#         data = data.to(device=device)
#         targets = targets.to(device=device)

#         pred = model(data)
#         loss = criterion(pred, targets)

#         optimizer.zero_grad()
#         loss.backward()

#         optimizer.step()

#     return loss




    