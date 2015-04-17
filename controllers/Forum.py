# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def index():
    form = SQLFORM(db.Blog_Post).process()
    if form.accepted:
        session.flash = 'Posted'
        redirect(URL('read'))
    return locals()

def read():
    rows = db(db.Blog_Post).select()#can use orderby=db.Blog_Post.Title.upper() , put this inside select
    return locals()

def viewPost():
    po = db.Blog_Post(request.args(0,cast=int))
    return locals()

@auth.requires_membership('Founder')
def manage():
    grid = SQLFORM.grid(db.Blog_Post)
    return locals()
