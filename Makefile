build:
	python3 scripts/build-all.py

install:
	pip3 install -r requirements.txt

clean:
	rm -rf ./scripts/builds/arm64/build ./scripts/builds/arm64/dist ./scripts/builds/x86/build ./scripts/builds/x86/dist

test:
	pytest