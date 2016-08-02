from flask import render_template, request
from app import app

from sklearn import metrics
from gensim.models import Word2Vec
import numpy as np
import os

import logging
log = logging.getLogger()

# Download the w2v model from here: https://mega.nz/#F!4VZFGIAa!uGx0JoqTr3KcN1bIwt1LzA
# Insert the path to the donwloaded w2v model (" .bin ") here.
MODEL_PATH = './data/w2v_norwegian_twitter_model.bin'
assert os.path.exists(MODEL_PATH), 'Word2Vec model file not found... please point it to the right location...'

FULL_EMOJIS_PATH='./data/emojis.npy'
MODEL_VARIANCE = 0.25

model = Word2Vec.load_word2vec_format(MODEL_PATH, binary=True)
ems = np.load(FULL_EMOJIS_PATH)

# Not all emojis can have a word vector. Some of them are rarely / never used...
# So collect only the valid ones.
valid_ems = np.array([x for x in ems if x in model.vocab.keys()])
log.info('total {} valid emojis found...'.format(len(valid_ems)))

vecs = np.zeros((len(valid_ems), model.syn0.shape[1]))
for i in range(len(valid_ems)):
    vecs[i] = model[valid_ems[i]]


def scores(words, top_n=10):
    """ couple emojis with their cosine similarities and return 'top_n' of total """

    # strip skin tones before looking for its vector
    words = ''.join([x for x in words if ord(x) not in range(127995, 128000)])
    wsplit = words.split()

    if not len(wsplit):
        log.info('empty')
        return []

    elif len(words.split()) > 1:
        log.info('multiple words entered... taking only 1st one... please enter only word')
        words = words[0]

    if words in model.vocab.keys():
        vec = model[words].reshape(1, -1)
    else:
        log.info('word not found in vocabulary...')
        return []

    res = metrics.pairwise.cosine_similarity(vecs, vec).ravel()
    ids = res.argsort()[::-1][:top_n]

    vals = list(zip(valid_ems[ids], np.round(res[ids], 3)))

    return vals


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    valid = False
    results = None
    emj = None
    search_string = None

    if request.method == 'POST':
        search_string = request.form['search_string'].strip().lower()
        results = scores(search_string)
        valid = True if len(results) else False

    return render_template('index.html', title='Search', search_string=search_string, valid=valid, res=results,
                            emj=np.random.choice(valid_ems))
