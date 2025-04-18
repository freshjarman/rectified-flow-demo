import matplotlib.pyplot as plt
import torch

if __name__ == '__main__':

    # 画Loss曲线看收敛情况
    # 读取pth文件，获得loss_list
    # checkpoint = torch.load('./checkpoints/v1.2-reflow-cfg/miniunet_19.pth')
    checkpoint = torch.load('./checkpoints/v1.1-cfg/miniunet_49.pth')
    loss_list = checkpoint['loss_list']

    # 画图
    plt.plot(loss_list)
    plt.xlabel('Iteration')
    plt.ylabel('Loss')
    plt.title('Loss Curve')
    plt.tight_layout()
    plt.show()
