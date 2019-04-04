from torchtext import data
from torchtext import datasets
from torchtext.vocab import GloVe
import re
import string
import torch

def data_tokenize(input_data):
    input_data = re.sub('<br /><br />' , '',input_data )
    input_data = input_data.translate(string.punctuation)
    input_data = input_data.split(' ')
    return input_data
# Approach 1:
# set up fields
TEXT = data.Field(lower=True, include_lengths=True, batch_first=True ,tokenize= data_tokenize)
LABEL = data.Field(sequential=False)

# make splits for data
train, test = datasets.IMDB.splits(TEXT, LABEL)
# print information about the data
# print('train.fields', train.fields)
# print('len(train)', len(train))
# print('vars(train[0])', vars(train[0]))
# print('vars(train[1]', vars(train[1]))

# build the vocabulary
TEXT.build_vocab(train, vectors=GloVe(name='6B', dim=300) , unk_init = torch.Tensor.normal_)
LABEL.build_vocab(train)

# print vocab information
# print(TEXT.vocab.itos[:100])
# print(LABEL.vocab.stoi)

# make iterator for splits
train_iter, test_iter = data.BucketIterator.splits((train, test),
                                                   batch_size=64,
                                                   device="cpu")

# print batch information
batch = next(iter(train_iter))
# print(batch.text)
# print(batch.label)
