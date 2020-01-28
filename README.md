# nuitka-cython-test
Test installing a package including Cython extension, and then compile a script with Nuitka using that package.

This use a Docker container for:
- Reproducible test setup
- Trying different python/package versions quickly

If you need to experiment within the container, do:
`docker run -it --rm --entrypoint /bin/bash axelvoitier/nuitka-cython-test`
