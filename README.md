# nuitka-cython-test
Test installing a package including Cython extension, and then compile a script with Nuitka using that package.

This use a Docker container for:
- Reproducible test setup
- Trying different python/package/code variations quickly and cleanly

Run:
- `make build` to build the container
- `make run` to run it and check it works

If you need to experiment within the container, do:
`docker run -it --rm --entrypoint /bin/bash axelvoitier/nuitka-cython-test`
