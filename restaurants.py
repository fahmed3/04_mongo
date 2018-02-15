import pymongo

connection = pymongo.MongoClient('homer.stuy.edu')

db = connection['test']
collection = db['restaurants']


def borough(b):
    borough = collection.find({'borough' : b})
    for i in borough:
        print i

#borough("Brooklyn")
        
def zip(z):
    zip = collection.find({'address.zipcode' : z} )
    for i in zip:
        print i

#zipGrade("11209")

def zipGrade(z, grade):
    zip = collection.find({'address.zipcode' : z, "grades.grade" : grade})
    for i in zip:
        print i

#zipGrade("11209", "A")
        
def zipScore(z, score):
    zip = collection.find({'address.zipcode' : z, "grades.score" : {'$lt' : score}})
    for i in zip:
        print i

#zipScore("11209", 13)

def cuisine(c):
    cuisine = collection.find({'cuisine': c})
    for i in cuisine:
        print i

#cuisine('Mexican')       
