import torch
from torch.nn import functional as F
from torch import nn
import pytorch_lightning as pl
import librosa
import numpy as np

class LitVoice(pl.LightningModule):

    def __init__(self, n_classes=5, lr=1e-3):
        super().__init__()

        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 16, kernel_size=3, stride=1, padding=1)
        self.linear1 = nn.Linear(16*5*10, 64)
        self.linear2 = nn.Linear(64, n_classes)
        

        self.lr = lr

        self.labels_str2nb = {'can ho': 0,
                              'canh sat': 1,
                              'com': 2,
                              'hoc sinh': 3,
                              'nguoi': 4}
        self.labels_nb2str = {0: 'can ho',
                              1: 'canh sat',
                              2: 'com',
                              3: 'hoc sinh',
                              4: 'nguoi'}

    def forward(self, x):

        batch_size, channels, width, height = x.size()

        x = self.conv1(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=2, stride=2)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=2, stride=2)
        x = torch.flatten(x).view(batch_size, -1)
        x = self.linear1(x)
        x = F.relu(x)
        x = self.linear2(x)
        
        return x
    
    def wav2mfcc(self, path, n_mfcc=20, max_len=40):
        wave, sr = librosa.load(path, mono=True, sr=None)
        wave = np.asfortranarray(wave[::3])
        mfcc = librosa.feature.mfcc(wave, sr=16000, n_mfcc=n_mfcc)

        # If maximum length exceeds mfcc lengths then pad the remaining ones
        if (max_len > mfcc.shape[1]):
            pad_width = max_len - mfcc.shape[1]
            mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')

        # Else cutoff the remaining parts
        else:
            mfcc = mfcc[:, :max_len]
    
        return mfcc 
    
    def prepare_inference_input(self, paths):
        mfccs = [self.wav2mfcc(path) for path in paths]
        mfccs = [mfcc[..., np.newaxis] for mfcc in mfccs]
        return torch.tensor(mfccs).permute(0, 3, 1, 2)
    
    def nb_2_label(self, nbs):
        return [self.labels_nb2str[nb] for nb in nbs.tolist()]
    
    def predict(self, paths):
        mfccs = self.prepare_inference_input(paths)
        outs = self(mfccs)
        outs = F.log_softmax(outs, dim=1)
        _, preds = torch.max(outs, dim=1)
        return self.nb_2_label(preds)