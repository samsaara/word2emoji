# word2emoji
Get closest related emojis for any given word / emoji.  😍 - Works best for Norwegian 🇳🇴 language.

Based on a [Word2Vec](https://code.google.com/p/word2vec/) model trained on Norwegian twitter data.

It's a Flask web app that you can run comfortably in your browser.

### How To:
1. Create a [virtual environment](https://docs.python.org/3/library/venv.html)
2. Do ``` pip install -r requirements.txt ```
3. Download the word2vec embeddings from this Mega link [here](https://mega.nz/#F!4VZFGIAa!uGx0JoqTr3KcN1bIwt1LzA) (800 MB)
4. Place it in the ```data``` directory.
5. run ``` python run.py ```

#### Example:
Here's one when searched for ``` KFC ```

![example_kfc](https://cloud.githubusercontent.com/assets/6368653/17087784/056c6ca8-5212-11e6-892d-59b2512153d1.jpg)

Enjoy :)

#### References:
For awesome tutorial on Flask, check Miguel's blogpost [here](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Github Pages [link](https://vaddina.github.io/word2emoji/)


## License:
[MIT](LICENSE)
