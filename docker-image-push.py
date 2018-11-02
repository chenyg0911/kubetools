# !/usr/bin/python
# -*- coding: UTF-8 -*-

import docker

registry_server = 'registry.orientsoft.cn'
catalog = 'kube'
client = docker.from_env()
newtag = ''
image_list = client.images.list()
for image in image_list:
    tag = image.tags[0]
    splited = tag.rsplit('/',1)
    if len(splited) == 1:
        newtag = '/'.join([registry_server,catalog,splited[0]])
    else:
        newtag = '/'.join([registry_server,catalog,splited[1]])

    image.tag(newtag)

    # push to target register
    for line in client.images.push(newtag, stream=True):
        print(line)

    # delete new tag, restore local docker image env
    client.images.remove(newtag)

client.close()