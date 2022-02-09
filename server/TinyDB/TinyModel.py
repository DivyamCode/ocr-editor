from tinydb import TinyDB


db = TinyDB("book.json")

class book(db.default_storage_class):
    bookuuid = "uid"
    title =  "title"
    author = "aithor name"
    fullpath = "Path"
    noofpage = int()
    isIndex = bool()
    bookdetail = {"uid":bookuuid , "title":title, "authorname":author,
         "path":fullpath ,"nofpage":noofpage,"index":isIndex}
    db.insert(bookdetail)
