![Image](clockwork-logo.png)

Clockwork is a collection of custom nodes for the [Dynamo](http://www.dynamobim.org) visual programming environment. It contains many Revit-related nodes, but also lots of nodes for various other purposes such as list management, mathematical operations, string operations, unit conversions, geometric operations (mainly bounding boxes, meshes, planes, points, surfaces, UVs and vectors) and paneling. Currently it consists of some 370+ nodes of which a large portion was previously published in a number of separate packages. My reasoning is that keeping all nodes in a single package will make updates easier and reduce package dependencies. I had never set out to build so many custom nodes – somehow it just happened.

If you like the package, please vote in support of it in Dynamo's package search tool. 

##Installation
Installation is simple - just use Dynamo's built-in package manager and search for ```Clockwork```. If you have used some of my previous 0.6.3 packages, please remember to uninstall *all* of them (find a complete list [here](https://github.com/CAAD-RWTH/ClockworkForDynamo/wiki/0.6.3-Packages-to-Uninstall)).

##Versions
###Clockwork for Dynamo 0.8.x
There is currently no distinct version of Clockwork for Dynamo 0.8.x yet - in the meantime, most nodes of [Clockwork for Dynamo 0.7.x](#clockwork-for-dynamo-07x) should run smoothly under Dynamo 0.8.x as well. Some nodes may not behave as expected under Dynamo 0.8, e.g. all nodes that get or set any Revit parameters that have a unit data type (like lengths, areas & volumes) will only work correctly if you have your Revit project units set to imperial units. I *am* in the process of creating a separate 0.8.x package that makes use of some non-downward-compatible new functionality available in Dynamo 0.8.x (default data types and values for node inputs) but it will most likely not be finished before fall of 2015. You can check in on my progress [here](https://github.com/CAAD-RWTH/ClockworkForDynamo/tree/master/nodes/0.8.x).
###Clockwork for Dynamo 0.7.x
The current release of Clockwork is version **0.75.47** - you can find more detailed information about this version and previous versions in the [version history](https://github.com/CAAD-RWTH/ClockworkForDynamo/wiki/Version-History). 
###Clockwork for Dynamo 0.6.3
There is also a version for Dynamo 0.6.3 (Clockwork 0.63.3) which I am keeping for historical purposes only - it is not supported any more.

##Renamed, recategorized and deprecated nodes
Migrating from 0.6.3, I recategorized and renamed most of the nodes. These changes are documented in an [excel sheet](https://github.com/CAAD-RWTH/ClockworkForDynamo/raw/master/NodeList.xls) that contains a list of all nodes within the package. Nodes with [pending issues](https://github.com/CAAD-RWTH/ClockworkForDynamo/issues) are highlighted in yellow.
If you are missing a specific node, please consult the [list of deprecated nodes](https://github.com/CAAD-RWTH/ClockworkForDynamo/wiki/Deprecated-Nodes).

##Updates
Since Dynamo's package manager currently does not (yet) have an update notification infrastructure in place, you may want to follow me on [twitter](https://twitter.com/a_dieckmann) for update notifications.

##Known Issues
On this repository you can find a [list of known issues and planned enhancements](https://github.com/CAAD-RWTH/ClockworkForDynamo/issues). Should you find that one of the nodes in this package does not work (or could work better with improved functionality), please let me know by creating a new issue in that section. Also, if you happen to come across a built-in node that does exactly the same as one of the Clockwork nodes, please let me know so I can remove that particular node from the package - I am not trying to duplicate existing functionality.

##Material on this repository

This repository contains the following:
- Directory [package_samples](package_samples) contains simple examples for most of the nodes in Clockwork. I use them for occasional testing, but they should also help explain how to use each node. I have started to migrate all the samples to 0.7.x, but this process is not yet complete. If you cannot find a sample for a particular node, have a look at the 0.6.3 samples instead (they are, however, sorted according to their previous packages).
- Directory [workflow_samples](workflow_samples) contains some sample workflows that I have published online somewhere before. I have also started to include some of the examples that I use for teaching Dynamo as well as some material presented at conferences. Almost all of these are available for Dynamo 0.7.x (as well as 0.6.3).
- Directory [nodes](nodes) is the actual repository of the custom nodes that I use for versioning nodes in between publishing package updates to Dynamo's package manager - which means you will sometimes find nodes in here that haven't made it onto the package manager yet.
- Directory [issues](issues) contains sample files for issues raised on the [Dynamo GitHub site](https://github.com/DynamoDS/Dynamo).

##Contributors
- [Andreas Dieckmann](https://github.com/andydandy74) [package maintainer]
- [Fabian Ritter](https://github.com/redinkinc) [contributor]
- [Konrad Sobon](https://github.com/ksobon) [contributor]

If you're interested in contributing to Clockwork, just submit a [pull request](https://github.com/CAAD-RWTH/ClockworkForDynamo/pulls).
