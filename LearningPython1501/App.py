from flask import Flask
from flask import render_template, request, redirect, url_for
import database

app = Flask(__name__)
posts = database.get_all_posts()

posts1 = { i : posts[i] for i in range(0, len(posts) ) }

'''posts = {
    0: {
        'post_id': 0,
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}'''


@app.route('/')
def home():
    return render_template('home.html', posts1=posts1)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts1.get((post_id))
    if not post:
        return render_template('404.html', message=f'A post with id {post_id} was not found.')
    #return f"Post {post['title']}, content:\n\n{post['content']}"
    #return render_template('post.html', post=posts.get(post_id))
    return render_template('post.html', post=post)

'''@app.route('/post/form')
def form():
    return render_template('create.html')

@app.route('/post/create', methods =['POST'])
def create():
    title = request.form.get('title')
    content = request.form.get('content')
    post_id = len(posts)
    posts[post_id] = {'id':post_id, 'title': title, 'content': content}
    return redirect(url_for('post', post_id=post_id))'''

@app.route('/post/create', methods =['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts1)
        database.add_post(post_id, title, content)
        #posts[post_id] = {'id':post_id, 'title': title, 'content': content}
        return redirect(url_for('post', post_id=post_id))
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
