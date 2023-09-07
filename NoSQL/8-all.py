#!/usr/bin/env python3
""" commented module """

def list_all(mongo_collection):
    """ commented function """
    documents = []

    cursor = mongo_collection.find({})

    if cursor.count() > 0:
        for document in cursor:
            documents.append(document)

    return documents
