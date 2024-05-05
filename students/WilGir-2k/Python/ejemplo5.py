from sklearn.model_selection import cross_val_score

# Aplicar validacion cruzada
scores = cross_val_score(model, x, y, cv=5)
print('Cross-validated scores:', scores)
print('Mean score:', scores.mean())
