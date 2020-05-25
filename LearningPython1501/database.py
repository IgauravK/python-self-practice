post_file = 'posts.txt'


def create_post_table():
    with open (post_file, 'w'):
        pass


def add_post(post_id,title,content):
    with open (post_file, 'a') as file:
        file.write(f'{post_id},{title},{content}\n\n')


def get_all_posts():
    with open (post_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'post_id': line[0], 'title': line[1], 'content': line[2]}
        for line in lines
    ]


