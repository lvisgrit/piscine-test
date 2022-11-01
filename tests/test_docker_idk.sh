#!/bin/bash

docker container run --rm -it --read-only --network none --memory 500M --cpus 2.0 --user 1000:1000 --env EXERCISE=foureven --env USERNAME=srueth --env HOME=/jail --env TMPDIR=/jail --workdir /jail --tmpfs /jail:size=100M,noatime,exec,nodev,nosuid,uid=1000,gid=1000,nr_inodes=5k,mode=1700 -v "$(pwd):/jail/student:ro" gritlab-tests
