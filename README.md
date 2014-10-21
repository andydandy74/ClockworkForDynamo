![Image](clockwork-logo.png)

#Clockwork for Dynamo#

Clockwork is a collection of custom nodes for the [Dynamo](http://www.dynamobim.org) visual programming environment which can be downloaded from Dynamo's [package manager](http://www.dynamopackages.com). Currently it consists of some 200+ nodes that were previously published in a number of separate packages. My reasoning is that keeping all nodes in a single package will make updates easier and reduce package dependencies. I had never set out to build so many custom nodes – somehow it just happened (most of them are by-products of my research and teaching activities).

#State of migration#

At least for some time, I will maintain two versions this package (one for Dynamo 0.6.3 and one for Dynamo 0.7.x). As soon as 0.7.x supports all my 0.6.3 workflows, I will abandon the 0.6.3 branch. Migrating from 0.6.3, I also recategorized and renamed most of the nodes. These changes are documented in an excel sheet [here](NodeList.xls). This list also includes information as to which nodes where deprecated during migration and which ones are still buggy or haven't been migrated yet. Note that nodes known to be buggy have not been included in the package.

I am currently using Dynamo 0.6.3 and 0.7.2 to test nodes, so some buggy nodes might very well be running under more recent daily builds.

#Material on this repository#

This repository contains the following:

Directory [package_samples](https://github.com/CAAD-RWTH/DynamoSamples/tree/master/package_samples) contains simple examples for most of the nodes in Clockwork. I use them for occasional testing, but they should also help explain how to use each node. The samples are currently still sorted according to their previous package and limited to 0.6.3 files. I plan to correct that in the future and also add 0.7.x versions of the sample files.

Directory [workflow_samples](https://github.com/CAAD-RWTH/DynamoSamples/tree/master/workflow_samples) contains some sample workflows that I have published online somewhere before. I have also started to include some of the examples that I use for teaching Dynamo. All of these are currently still 0.6.3 files and will be migrated as 0.7.x stability improves.
