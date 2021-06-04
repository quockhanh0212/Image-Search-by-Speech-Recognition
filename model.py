import os 
import torch
from base_model import LitVoice
import librosa
import numpy as np
import torch.nn.functional as F
from collections import Counter

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class RecognitionModel:
    def __init__(self, checkpoint_path='voice_recognition_cnn_tv.pth'):
        ckpt = torch.load(checkpoint_path, map_location=device)
        self.model = LitVoice()
        self.model.load_state_dict(ckpt['state_dict'])

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
        outs = self.model(mfccs)
        outs = F.log_softmax(outs, dim=1)
        _, preds = torch.max(outs, dim=1)
        return self.nb_2_label(preds)


model = RecognitionModel()
# paths = os.listdir('D:/Desktop/Document/Nam3/Ki2/Xử lý tiếng nói/prj/ml-class-master/videos/cnn-audio/all/com')
# preds_list = []
# for path in paths:
#     pred = model.predict(['D:/Desktop/Document/Nam3/Ki2/Xử lý tiếng nói/prj/ml-class-master/videos/cnn-audio/all/com/' + path])[0]
#     preds_list.append(pred)
#
# print(preds_list)

pred = model.predict(['com.wav'])[0]
print(pred)
