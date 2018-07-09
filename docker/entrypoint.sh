#!/bin/sh


run() {
	python src/word_count.py "$@"
}


run_test() {
	py.test
}


open_sh() {
	sh
}


case "$1" in
	"run")
		shift
		run $@
		;;

	"run_test")
		shift
		run_test
		;;

	"open_sh")
		shift
		open_sh
		;;
esac
