import models

member1 =models.Memeber('khaled', 16)
member2 =models.Memeber('Yaser', 30)

post1 =models.Post('First post', 'this is the first post')
post2 =models.Post('Second post', 'this is the second  post')
post3 =models.Post('Third post', 'this is the third post')



print ( 'User name: ' + member1.name + '  |   Age: '+ str( member1.age ) )
print ( 'User name: ' + member2.name + '  |   Age: '+ str( member2.age ) )
print ( 'Post 1 title: ' + post1.title + '  |   Content: '+ str( post1.body ) )
print ( 'Post 2 title: ' + post2.title + '  |   Content: '+ str( post2.body ) )
print ( 'Post 3 title: ' + post3.title + '  |   Content: '+ str( post3.body ) )
