import subprocess, sys

# Commands
COMPOSE_POSTS = "../../../wrk2/wrk -D exp -t {threads} -c {conns} -d {durr} -L -s ./wrk2/scripts/social-network/compose-post.lua http://localhost:8080/wrk2-api/post/compose -R {reqs}"

def commObjGen(threads: int, conns: int, dur: int, reqs: int):
    return {
        "threads": threads,
        "conns": conns,
        "durr": dur,
        "reqs": reqs
    }

def commandGen(obj) -> str:
    return COMPOSE_POSTS.format_map(obj)

def runProcess(command):
    subprocess.run(command, shell = True, executable="/bin/bash")

def start():
    runProcess(commandGen(commObjGen(4, 12, 60, 1000)))

if __name__ == "__main__":
    start()