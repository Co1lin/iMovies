from movies.models import *

for i in range(2, 9):
    print(i)
    for j in range(1, 3):
        Movie.objects.get(id=i).comment_set.create(
            content=('电影' + str(i) + '的' + '评论' + str(j)),
            author=('评论员' + str(j)),
            date='2020-09-08'
        )