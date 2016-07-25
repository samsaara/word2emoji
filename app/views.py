from flask import render_template, redirect
from app import app
from .forms import SearchForm

from gensim.models import Word2Vec
import numpy as np
import os


# Download the w2v model from here: https://mega.nz/#F!4VZFGIAa!uGx0JoqTr3KcN1bIwt1LzA
# Insert the path to the donwloaded w2v model (" .bin ") here.
MODEL_PATH = './data/w2v_norwegian_twitter_model.bin'
FULL_EMOJIS_PATH='./data/emojis.npy'

assert os.path.exists(MODEL_PATH), 'Word2Vec model file not found... please point it to the right location...'

model = Word2Vec.load_word2vec_format(MODEL_PATH, binary=True)
ems = np.load(FULL_EMOJIS_PATH)


# Not all emojis can have a vector. Some of them might are rarely / never used...
# So collect the valid ones.
valid_ems = np.array([x for x in ems if x in model.vocab.keys()])
print ('total {} valid emojis found...'.format(len(valid_ems)))

def scores(word, top_n=10):
    # strip skin tones before looking for its vector
    word = ''.join([x for x in word if ord(x) not in range(127995, 128000)])
    if word in model.vocab.keys():
        res = np.empty(len(valid_ems), dtype=[('emoji', np.dtype(('U', 10))), ('cosine_similarity', 'f')])
        for i in range(len(res)):
            res[i] = (valid_ems[i], model.similarity(word, valid_ems[i]))
        res['cosine_similarity'] = np.round(res['cosine_similarity'], decimals=3)

        return np.sort(res, order='cosine_similarity')[::-1][:top_n]
    else:
        return []


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect('/search/{}'.format(form.search_word.data))

    return render_template('index.html', title='Home', form=form) #, word=word_field)


@app.route('/search/<keyword>')
def search(keyword):
    results = scores(keyword.strip().lower(), top_n=10)
    return render_template('search.html', keyword=keyword, res=results, title='search', emj=np.random.choice(valid_ems),
                            valid='True' if len(results) else 'False')
