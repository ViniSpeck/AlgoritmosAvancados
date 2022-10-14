:server connect

# Testing
```
Match (m:Movie) where m.released > 2000 RETURN m
```
```
MATCH (p:Person)-[d:DIRECTED]-(m:Movie) where m.released > 2010 RETURN p,d,m
```
```
MATCH (p:Person) RETURN p limit 20
```
```
MATCH (p:Person) return p.name, p.born
```
```
Create (p:Person {name: 'John Doe'}) RETURN p
```
```
MERGE (p:Person {name: 'John Doe'})<br/>
ON MATCH SET p.lastLoggedInAt = timestamp()<br/>
ON CREATE SET p.createdAt = timestamp()<br/>
Return p<br/>
```
```
MATCH (p:Person), (m:Movie)<br/>
WHERE p.name = "Tom Hanks" and m.title = "Cloud Atlas"<br/>
CREATE (p)-[w:WATCHED]->(m)<br/>
RETURN type(w)<br/>
```
`
MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(:Movie)<-[:ACTED_IN]-(p:Person) return p.name
`
