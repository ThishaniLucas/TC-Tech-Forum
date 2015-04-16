# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def index():
    db.Blog_Post.Posted_On.default = request.now
    db.Blog_Post.Posted_On.writable = False
    db.Blog_Post.Posted_On.readable = True
    form = SQLFORM(db.Blog_Post).process()
    if form.accepted:
        redirect(URL('read'))
    return locals()

def read():
    rows = db(db.Blog_Post).select()
    return locals()

def viewPost():
    po = db.Blog_Post(request.args(0,cast=int))
    return locals()

@auth.requires_membership('Founder')
def manage():
    grid = SQLFORM.grid(db.Blog_Post)
    return locals()
