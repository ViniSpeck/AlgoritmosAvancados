# Exemplos de Comandos do Cypher 

```
Match (m:Movie) where m.released > 2000 RETURN m
```

Procura por filmes lançados depois do ano 2000.

```
MATCH (p:Person)-[d:DIRECTED]-(m:Movie) where m.released > 2010 RETURN p,d,m
```

Procura por pessoa que dirigiu filme, onde filme foi lançado após 2010, e retorna a Pessoa, a Relação, e o Filme.

```
MATCH (p:Person) RETURN p
```

Procura por todas as entidades Pessoas.

```
MATCH (p:Person) return p.name, p.born
```

Mostra os nomes e datas de nascimento de todas as Pessoas.

```
Create (p:Person {name: 'John Doe'}) RETURN p
```

Cria e retorna uma Pessoa, cujo nome é John Doe

```
MERGE (p:Person {name: 'John Doe'})
ON MATCH SET p.lastLoggedInAt = timestamp()
ON CREATE SET p.createdAt = timestamp()
Return p
```

Caso John Doe já exista, junta os dois John Does, e atribui à variável lastLoggedInAt o timestamp atual.
Se não, cria um novo John Doe, e atribui o timestamp.

```
MATCH (p:Person), (m:Movie)
WHERE p.name = "Tom Hanks" and m.title = "Cloud Atlas"
CREATE (p)-[w:WATCHED]->(m)
RETURN type(w)
```

Seleciona as pessoas e os filmes, e onde a pessoa se chama Tom Hanks e o filme é "Cloud Atlas", cria a relação que a pessoa assistiu o filme.

```
MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(:Movie)<-[:ACTED_IN]-(p:Person) return p.name
```

Mostra as pessoas que atuaram em filmes em comum com Tom Hanks.
