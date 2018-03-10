import models
import stores


member1 =models.Memeber('khaled', 16)
member2 =models.Memeber('Yaser', 30)

post1 =models.Post('First post', 'this is the first post')
post2 =models.Post('Second post', 'this is the second  post')
post3 =models.Post('Third post', 'this is the third post')

memberstore =stores.MemberStore()
memberstore.add(member1)
memberstore.add(member2)

print str(memberstore.get_all)

poststore =stores.PostStore()
poststore.add(post1)
poststore.add(post2)
poststore.add(post3)

print str(poststore.get_all)
