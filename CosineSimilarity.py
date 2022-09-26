#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.metrics.pairwise import cosine_similarity


# Vectors
vec_a = [1, 0, 0, 1, 0]
vec_b = [1, 0, 1, 1, 0]

# Dot and norm
dot = sum(a*b for a, b in zip(vec_a, vec_b))

norm_a = sum(a*a for a in vec_a) ** 0.5
norm_b = sum(b*b for b in vec_b) ** 0.5

print(norm_a*norm_b)
print(dot)


# Cosine similarity
cos_sim = dot / (norm_a*norm_b)

# Results
print('My version:', cos_sim)
print('Scikit-Learn:', cosine_similarity([vec_a], [vec_b]))

