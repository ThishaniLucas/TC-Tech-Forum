# -*- coding: utf-8 -*-
db.define_table('Blog_Post',
               Field('Title',requires=IS_NOT_EMPTY()),
               Field('Post','text',requires=IS_NOT_EMPTY()),
               Field('Posted_On','datetime'))
#we have created a database table name call blog_post with 3 columns and a additional ID column(autoincrementing primary key )
#default type of field is 'String'
