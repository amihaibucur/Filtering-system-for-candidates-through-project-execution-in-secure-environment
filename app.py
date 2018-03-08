import docker
from os import walk

client = docker.from_env()

PATH_TO_PROJECTS = '/var/lib/docker/volumes/everythingHappensHere/_data/projects'
PATH_TO_ARGUMENTS = '/var/lib/docker/volumes/everythingHappensHere/_data/arguments'
PATH_TO_EXPECTED_RESULTS = '/var/lib/docker/volumes/everythingHappensHere/_data/expectedResults'

projectsList = []

for (dirpath, dirnames, filenames) in walk(PATH_TO_PROJECTS):
     projectsList.extend(dirnames)
     break

for project in projectsList:

    nameParts = project.split("-")
    projectNumber, uniqueIdentifier, projectType = nameParts[0], nameParts[1], nameParts[2]
    passedTests, failedTests = [], []

    for (dirpath, dirnames, filenames) in walk(PATH_TO_ARGUMENTS + "/project-" + projectNumber):
        nbOfTests = len(filenames)
        for file in filenames:
            testNumber = file.split("-")[-1].split(".")[0]
            testArguments = open(dirpath + "/" + file, 'r').read()
            expectedResult = open(PATH_TO_EXPECTED_RESULTS + "/project-" + projectNumber + "/" + file, 'r').read()

            if projectType == 'jar':
                result = client.containers.run("java-img",
                                               "java -jar /myData/projects/" + project + "/main-"+projectNumber + uniqueIdentifier+".jar "+ testArguments,
                                               volumes = {
                                                 '/var/lib/docker/volumes/everythingHappensHere/_data': {'bind': '/myData'}
                                               }
                                              )


                if result == expectedResult:
                    passedTests.append(testNumber)
                else:
                    failedTests.append(testNumber)

            if projectType == 'py':
                result = client.containers.run("py-img",
                                      "python3 /myData/projects/" + project +"/main-" + projectNumber + uniqueIdentifier + ".py" + testArguments,
                                      volumes = {
                                          '/var/lib/docker/volumes/everythingHappensHere/_data': {'bind': '/myData'}
                                      }
                                    )


                if result == expectedResult:
                    passedTests.append(testNumber)
                else:
                    failedTests.append(testNumber)

            if projectType == 'cpp':
                result = client.containers.run("cpp-img",
                                      command='bash -c "g++ -o /myData/projects/' + project + '/output /myData/projects/' + project+ '/main-' + projectNumber + uniqueIdentifier +'.cpp '
                                              '&& /myData/projects/5-mihaib-cpp/output ' + testArguments +'"',
                                      volumes = {
                                          '/var/lib/docker/volumes/everythingHappensHere/_data': {'bind': '/myData', 'mode': 'rw'}
                                      }
                                    )


                if result == expectedResult.rstrip():
                    passedTests.append(testNumber)
                else:
                    failedTests.append(testNumber)

    print 'Proiect: ' + project + ' | Teste trecute: ' + passedTests.__str__() + ' | Teste picate' + failedTests.__str__()











