import nox

@nox.session
def tests(session):
    session.install("-e", ".")
    session.install("pytest", "uncertainties")
    session.run("pytest")
