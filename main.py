import models

member1 =models.Memeber('khaled', 16)
member2 =models.Memeber('Yaser', 30)

post1 =models.Post('First post', 'this is the first post')
post2 =models.Post('Second post', 'this is the second  post')
post3 =models.Post('Third post', 'this is the third post')



print ( 'User name: ' + member1.get_name() + '  |   Age: '+ str( member1.get_age() ) )
print ( 'User name: ' + member2.get_name() + '  |   Age: '+ str( member2.get_age() ) )
print ( 'Post 1 title: ' + post1.get_title() + '  |   Content: '+ str( post1.get_body() ) )
print ( 'Post 2 title: ' + post2.get_title() + '  |   Content: '+ str( post2.get_body() ) )
print ( 'Post 3 title: ' + post3.get_title() + '  |   Content: '+ str( post3.get_body() ) )
