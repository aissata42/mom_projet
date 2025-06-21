import nox


@nox.session
def tests(session):
    """Run the test suite."""
    session.install(".[test]")  # installe les dépendances du groupe [test]
    session.run("pytest")
