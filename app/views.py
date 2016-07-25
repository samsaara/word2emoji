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
valid_ems = []
for i in range(len(ems)):
    try:
        if len(model[ems[i]]):
            valid_ems.append(ems[i])
    except:
        pass
valid_ems = np.array(valid_ems)
print ('total {} valid emojis found...'.format(len(valid_ems)))


def scores(word, top_n=10):
    res = []
    for i in range(len(ems)):
        try:
            res.append((ems[i], model.similarity(ems[i], word)))
        except:
            continue

    res = np.array(res, dtype=[('emoji', np.dtype(('U', 10))), ('cosine_similarity', 'f')])
    res['cosine_similarity'] = np.round(res['cosine_similarity'], decimals=3)

    return np.sort(res, order='cosine_similarity')[::-1][:top_n]


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
                            valid='True' if results.shape[0] else 'False')
