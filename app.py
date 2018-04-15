import docker
import time
import os
import asyncio
import constants
import containers
from os import walk

client = docker.from_env()

# result = containers.startJavaServer(client, '1-mihhb-jwebapp', 'mihhb', '0.1.0')
# print(result)

result = containers.executeCCppBuilderContainer(client, '5-bucumih-cppm', 'Alex')
print(result)


# projectsList = []
#
# for (dirpath, dirnames, filenames) in walk(constants.PATH_TO_PROJECTS):
#      projectsList.extend(dirnames)
#      break
#
# for project in projectsList:
#
#     nameParts = project.split("-")
#     projectNumber, uniqueIdentifier, projectType = nameParts[0], nameParts[1], nameParts[2]
#     passedTests, failedTests = [], []
#
#     for (dirpath, dirnames, filenames) in walk(constants.PATH_TO_ARGUMENTS + "/project-" + projectNumber):
#         nbOfTests = len(filenames)
#         for file in filenames:
#             testNumber = file.split("-")[-1].split(".")[0]
#             testArguments = open(dirpath + "/" + file, 'r').read().rstrip()
#             expectedResult = open(constants.PATH_TO_EXPECTED_RESULTS + "/project-" + projectNumber + "/" + file, 'r').read().rstrip()
#
#             if projectType == 'jar':
#                 result = containers.executeJavaContainer(client, project, projectNumber, uniqueIdentifier, testArguments)
#
#                 if result == expectedResult:
#                     passedTests.append(testNumber)
#                 else:
#                     failedTests.append(testNumber)
#
#             if projectType == 'py':
#                 result = containers.executePythonContainer(client, project, projectNumber, uniqueIdentifier, testArguments)
#
#                 if result == expectedResult:
#                     passedTests.append(testNumber)
#                 else:
#                     failedTests.append(testNumber)
#
#             if projectType == 'cpp':
#                 result = containers.executeCppContainer(client, project, projectNumber, uniqueIdentifier, testArguments)
#
#                 if result == expectedResult:
#                     passedTests.append(testNumber)
#                 else:
#                     failedTests.append(testNumber)
#
#     print('Proiect: ' + project + ' | Passed tests: ' + passedTests.__str__() + ' | Failed tests:' + failedTests.__str__())











