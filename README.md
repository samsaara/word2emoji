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

#### Demo:
![word2emoji demo](https://cloud.githubusercontent.com/assets/6368653/17326353/1f639136-58b1-11e6-8e09-75f1ce2bb467.gif)


##### ToDo:
Clickable emojis would be 👌🏼.



Enjoy :)

#### References:
1. For awesome tutorial on Flask, check Miguel's blogpost [here](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
2. Uses lightweight [Skeleton](http://getskeleton.com) CSS...

Github Pages [link](https://vaddina.github.io/word2emoji/)


## License:
[MIT](LICENSE)
