class MemberStore:

    members = []

    def add(self, member):
        MemberStore.members.append(member)

    def get_all(self):
        return members

class PostStore:

    posts = []

    def add(self, post):
        PostStore.posts.append(post)

    def get_all(self):
        return posts
