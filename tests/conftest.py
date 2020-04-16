import pytest


@pytest.mark.asyncio
@pytest.fixture(scope="session")
def enterCredentials():
    print("To run the examples, enter your credentials for the GTI API.")
    gti_user = input("GTI Username: ")
    gti_pass = input("GTI Password: ")
    return gti_user, gti_pass
