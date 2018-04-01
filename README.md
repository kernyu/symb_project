# Symbolic Methods Project
collaboration between Nenad Macesic and Kernyu Park

## Tackling Antibiotic Resistance (aka AMR) Using Ontology Learning
Aiming at an ontology-based approach to tackle antibiotic resistance.

## Method(s)
- Ontology Learning process (semi-automated)
  - Topic-modeling methods using tf-idf weighting of terms
  - annotation of biomedical texts using Metamap
  - network analysis (clustering and community detection)


## Tasks

1. obtain MEDLINE corpus of abstracts and MeSH terms

2. process abstracts using tf-idf weighting of terms and constrain to an adjacency matrix of co-occurrences between all terms occurring in all abstract texts (*obtain "tokens", or "terms"*)

3. map to UMLS using Metamap to identify concepts in the term cloud (*obtain "concepts"*)

4. combine with matrix of MeSH terms to identify hierarchical as well as modifier relationships between terms (*define relationships*)

5. expert validation of the established concepts and their relationships

6. construct an ontology (*ontology generation*)

7. expert validation of the obtained ontology for further improvement
