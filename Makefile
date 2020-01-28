build:
	docker build -t axelvoitier/nuitka-cython-test .

run:
	docker run -it --rm axelvoitier/nuitka-cython-test
