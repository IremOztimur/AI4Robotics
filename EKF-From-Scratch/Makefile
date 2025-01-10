clean:
	@rm -rf __pycache__
	@echo "\033[91mCleaned up __pycache__\033[0m"

virtual:
	@if [ ! -d "myenv" ]; then \
		python3.11 -m venv myenv && \
		. myenv/bin/activate && pip install -r requirements.txt && \
		echo "\033[92mCreated virtual environment.\033[0m"; \
	else \
		echo "\033[93mVirtual environment already exists.\033[0m"; \
	fi

install:
	pip install -r requirements.txt
	@echo "\033[92mInstalled all python packages\033[0m"