def executeJavaContainer(client, project, projectNumber, uniqueIdentifier, testArguments):
    result = client.containers.run("java-img",
                                   "java -jar /myData/projects/" + project + "/main-"+projectNumber + uniqueIdentifier+".jar "+ testArguments,
                                    volumes = {
                                        '/var/lib/docker/volumes/everythingHappensHere/_data': {'bind': '/myData'}
                                    })
    return result.decode("utf-8").rstrip()

def executePythonContainer(client, project, projectNumber, uniqueIdentifier, testArguments):
    result = client.containers.run("py-img",
                                   "python3 /myData/projects/" + project + "/main-" + projectNumber + uniqueIdentifier + ".py" + testArguments,
                                   volumes={
                                       '/var/lib/docker/volumes/everythingHappensHere/_data': {'bind': '/myData'}
                                   })
    return result.decode("utf-8")

def executeCppContainer(client, project, projectNumber, uniqueIdentifier, testArguments):
    result = client.containers.run("cpp-img",
                                   command='bash -c "g++ -o /myData/projects/' + project + '/output /myData/projects/' + project + '/main-' + projectNumber + uniqueIdentifier + '.cpp '
                                                    '&& /myData/projects/5-mihaib-cpp/output ' + testArguments + '"',
                                   volumes={
                                       '/var/lib/docker/volumes/everythingHappensHere/_data': {'bind': '/myData',
                                                                                               'mode': 'rw'}
                                   })
    return result.decode("utf-8")

def executeCCppBuilderContainer(client, project, testArguments):
    result = client.containers.run("mihaibucur/c-cpp-img",
                                   command='bash -c "cd /myData/projects/' + project +
                                                    ' && make' +
                                                    ' && make ARGS="'+ testArguments + '" run"',
                                   volumes={
                                       '/var/lib/docker/volumes/everythingHappensHere/_data': {'bind': '/myData',
                                                                                               'mode': 'rw'}
                                   })
    return result.decode("utf-8").split("\n")[-1]

def startNodeServer(client, project):
    result = client.containers.run("mihaibucur/node-web-app",
                                   detach=True,
                                   command='bash -c "cd /myData/projects/' + project + ' '
                                                    '&& npm  install '
                                                    '&& npm start"',
                                   volumes={
                                       '/var/lib/docker/volumes/everythingHappensHere/_data': {'bind': '/myData',
                                                                                               'mode': 'rw'}
                                   },
                                   ports={'8080/tcp': 3333}
                                   )
    return result

def startJavaServer(client, project, uniqueIdentifier, version):
    commandStr = 'cd /myData/projects/1-mihhb-jwebapp && mvn install && java -jar target/mihhb-0.1.0.jar'
    result = client.containers.run("mvnserver",
                                   detach=True,
                                   command='bash -c "' + commandStr + '"',
                                   volumes={
                                       '/var/lib/docker/volumes/everythingHappensHere/_data': {'bind': '/myData',
                                                                                               'mode': 'rw'}
                                   },
                                   ports={'8080/tcp': 3389}
                                   )
    return result