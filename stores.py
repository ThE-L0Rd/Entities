class MemberStore:

    members = []

    list_id = 1

    def add(self, member):
        member.id = MemberStore.list_id

        MemberStore.members.append(member)

        MemberStore.list_id += 1

    def get_all(self):
        return MemberStore.members

    def get_by_id(self, id):
        all_members = self.get_all()

        return all_members[(int(id)-1)]

    def entity_exists(self, member):

        result = True

        for m in MemberStore.members :
           if m == member :
               return result

        return False

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

class PostStore:

    posts = []

    def add(self, post):
        PostStore.posts.append(post)

    def get_all(self):
        return posts
