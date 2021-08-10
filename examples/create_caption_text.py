import torch
#import matplotlib.pyplot as plt
import numpy as np 
import argparse
import pickle 
import os
import cv2
import textwrap
import datetime
import locale
import numpy as np
from torchvision import transforms 
from build_vocab import Vocabulary
from model import EncoderCNN, DecoderRNN
from PIL import Image

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def create_caption_text_str_list(image_data):
    # Image preprocessing
    transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406),
                             (0.229, 0.224, 0.225))])
    
    # Load vocabulary wrapper
    vocab_path = 'data/vocab.pkl'
    encoder_path = 'models/encoder-5-3000.pkl'
    decoder_path = 'models/decoder-5-3000.pkl'
    embed_size = 256
    hidden_size = 512
    num_layers = 1
    
    with open(vocab_path, 'rb') as f:
        vocab = pickle.load(f)

    # Build models
    encoder = EncoderCNN(embed_size).eval()  # eval mode (batchnorm uses moving mean/variance)
    decoder = DecoderRNN(embed_size, hidden_size, len(vocab), num_layers)
    encoder = encoder.to(device)
    decoder = decoder.to(device)

    # Load the trained model parameters
    encoder.load_state_dict(torch.load(encoder_path))
    decoder.load_state_dict(torch.load(decoder_path))

    # Prepare an image
    #image = Image.open(image_path).convert('RGB')
    image = Image.fromarray(image_data)
    image = image.resize([224, 224], Image.LANCZOS)
    image = transform(image).unsqueeze(0)
    #image = load_image(args.image, transform)
    image_tensor = image.to(device)
    
    # Generate an caption from the image
    feature = encoder(image_tensor)
    sampled_ids = decoder.sample(feature)
    sampled_ids = sampled_ids[0].cpu().numpy()          # (1, max_seq_length) -> (max_seq_length)
    
    # Convert word_ids to words
    sampled_caption = []
    for word_id in sampled_ids:
        word = vocab.idx2word[word_id]
        sampled_caption.append(word)
        if word == '<end>':
            break
    sentence = ' '.join(sampled_caption)
    sentence = sentence.replace("<start>", "")
    sentence = sentence.replace("<end>", "")
    
    # Print out the image and the generated caption
    #print(sentence)
    caption_text_wrap_list = textwrap.wrap(str(sentence), 40)
    
    return caption_text_wrap_list

#args.models
#parser.add_argument('--encoder_path', type=str, default='models/encoder-5-3000.pkl', help='path for trained encoder')
#parser.add_argument('--decoder_path', type=str, default='models/decoder-5-3000.pkl', help='path for trained decoder')
#parser.add_argument('--vocab_path', type=str, default='data/vocab.pkl', help='path for vocabulary wrapper')
    
# Model parameters (should be same as paramters in train.py)
#parser.add_argument('--embed_size', type=int , default=256, help='dimension of word embedding vectors')
#parser.add_argument('--hidden_size', type=int , default=512, help='dimension of lstm hidden states')
#parser.add_argument('--num_layers', type=int , default=1, help='number of layers in lstm')

