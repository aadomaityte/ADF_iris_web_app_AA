# This will test the model is actually predicting the right species

from calc import predict_species


def test_setosa():
    sepal_length = 5.1
    sepal_width = 3.5
    petal_length = 1.4
    petal_width = 0.2

    final_species = predict_species(sepal_length,sepal_width,petal_length,petal_width)
    assert final_species == 0