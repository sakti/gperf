docker:
	docker build -t gperf .
run_sleep:
	docker run -it --rm --name gperf gperf -c 'import time; time.sleep(3600)'
run_sh:
	docker exec -it gperf bash
