from utils import doThing

def test_do_thing_performance(benchmark):
    """Benchmark de la fonction doThing qui est volontairement lente"""
    # On benchmark l'exécution de doThing avec des valeurs dummy
    result = benchmark(doThing, "user_bench", 1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert result is True
