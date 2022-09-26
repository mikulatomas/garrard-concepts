# garrard-concepts
Exemplars by features data from [1], typicality ratings were additionaly gathered since are not avaliable publicly.

## Python wrapper
For easier manipulation, you can download data as Python wrapper:

```bash
pip3 install git+https://github.com/mikulatomas/garrard-concepts.git
```

## Example

```python
import garrard_concepts as gc

data = gc.GarrardConcepts()

# typicality ratings for birds
data.exemplar_judgements.typicality_ratings[dc.Category.BIRD]

# exemplar based features for birds
data.features[dc.FeatureType.EXEMPLAR].category[dc.Category.BIRD]
```

## Original dataset
[1] Garrard, Peter, et al. "Prototypicality, distinctiveness, and intercorrelation: Analyses of the semantic attributes of living and nonliving concepts." Cognitive neuropsychology 18.2 (2001): 125-174.
