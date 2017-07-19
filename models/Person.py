from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom, db)

config.DATABASE_URL = 'bolt://neo4j:123456@172.17.0.3:7687'

class Person(StructuredNode):
    name = StringProperty()
    age = IntegerProperty()
    def getFriends(self, id):
        query = "match (p:Person)-[r:friend]->(f:Person) where id(f)=%s return distinct p" % id
        results, meta = db.cypher_query(query)
        print(query)
        return [self.inflate(row[0]) for row in results]
    def add(self, name, age):
        query = "create (p:Person{name:'%s', age:%s}) return p" % (name, age)
        results, meta = db.cypher_query(query)
        return results
    def detail(self, id):
        query = "match (p:Person) where id(p)=%s return p" % (id)
        results, meta = db.cypher_query(query)
        return [self.inflate(row[0]) for row in results][0]