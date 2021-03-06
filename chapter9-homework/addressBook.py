#!/usr/bin/python
# Filename : addressBook.py
import cPickle as p
import os


class Person:
    """
    Person class
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def __str__(self):
        return 'name: %s, email: %s' % (self.name, self.email)


class AddrBook:
    """
    AddBook class
    """
    bookdata = 'bookdata.txt'

    def __init__(self):
        if not os.path.isfile(AddrBook.bookdata):
            print 'file not exist'
            self.book = []
        else:
            f = file(AddrBook.bookdata)
            self.book = p.load(f)
            f.close()

    def add(self,person):
        self.book.append(person)
        self.persistent()

    def show(self):
        if len(self.book) > 1:
            for person in self.book[:-1]:
                print person,
            print self.book[-1]
        elif len(self.book) == 1:
            print self.book[-1]
        else:
            print

    def persistent(self):
        f = file(AddrBook.bookdata, 'w')
        p.dump(self.book, f)
        f.close()


book = AddrBook()
person = Person('jack','jack@tom.com')
print 'person is', person
print 'add before is',
book.show()
book.add(person)
print 'add after is',
book.show()