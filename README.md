![Image](clockwork-logo.png)

Clockwork is a collection of custom nodes for the [Dynamo](http://www.dynamobim.org) visual programming environment which can be downloaded using the package search feature inside Dynamo or, alternatively, from Dynamo's [package manager](http://www.dynamopackages.com). It contains many Revit-related nodes, but also lots of nodes for various other purposes such as list management, mathematical operations, string operations, unit conversions, geometric operations (mainly bounding boxes, meshes, planes, points, surfaces, UVs and vectors) and paneling. Currently it consists of some 330+ nodes of which a large portion was previously published in a number of separate packages. My reasoning is that keeping all nodes in a single package will make updates easier and reduce package dependencies. I had never set out to build so many custom nodes – somehow it just happened.

If you use Clockwork, please remember to uninstall *all* of my previous packages (see [list below](#packages-to-uninstall)).

If you like the package, please vote in support of it in Dynamo's package search tool. Should you find that one of the nodes in this package does not work (or could work better with improved functionality), please let me know by creating a new [issue](https://github.com/CAAD-RWTH/ClockworkForDynamo/issues). Also, if you happen to come across a built-in node that does exactly the same as one of the Clockwork nodes, please let me know so I can remove that particular node from the package - I am not trying to duplicate existing functionality.

Since Dynamo's package manager currently does not (yet) have an update notification infrastructure in place, you may want to follow me on [twitter](https://twitter.com/a_dieckmann) for update notifications.

#Version history

The latest release of Clockwork is version 0.75.17 - you can find more detailed information about this version and previous versions in the [version history](VersionHistory.md). There is also a version for Dynamo 0.6.3 (Clockwork 0.63.3) which I am keeping for historical purposes only - it is not supported any more.

#Material on this repository#

This repository contains the following:

Directory [package_samples](package_samples) contains simple examples for most of the nodes in Clockwork. I use them for occasional testing, but they should also help explain how to use each node. I have started to migrate all the samples to 0.7.x, but this process is not yet complete. If you cannot find a sample for a particular node, have a look at the 0.6.3 samples instead (they are, however, sorted according to their previous packages).

Directory [workflow_samples](workflow_samples) contains some sample workflows that I have published online somewhere before. I have also started to include some of the examples that I use for teaching Dynamo as well as some material presented at conferences. All of these are available for Dynamo 0.7.x (as well as 0.6.3).

Directory [nodes](nodes) is the actual repository of the custom nodes that I use for versioning nodes in between publishing package updates to Dynamo's package manager - which means you will sometimes find nodes in here that haven't made it onto the package manager yet.

Directory [issues](issues) contains sample files for issues raised on the [Dynamo GitHub site](https://github.com/DynamoDS/Dynamo).

#State of migration#

Migrating from 0.6.3, I recategorized and renamed most of the nodes. These changes are documented in an [excel sheet](https://github.com/CAAD-RWTH/ClockworkForDynamo/raw/master/NodeList.xls) that contains a list of all nodes within the package. This list is colour-coded in order to reflect the state of each node:
- ```GREEN```: Works
- ```YELLOW```: Buggy in 0.7.x
- ```PURPLE```: Needs review
- ```RED```: Deprecated in 0.7.x
- ```GREY```: Not yet migrated or published

I am currently using the official 0.7.5 build as well as recent daily builds of Dynamo 0.7.x for testing. Note that nodes known to be buggy in the latest stable build of Dynamo 0.7.x may not be included in the package until they (or the respective bugs in Dynamo that are causing them to fail) are fixed.

#Packages to uninstall#
If you have installed Clockwork or are planning to do so, you should uninstall *all* of my previous packages (that is if you had those installed at all, of course). As a rule of thumb, uninstall everything that is organized in the ```CAAD_RWTH``` category in the node browser. Here's a complete list of all (recently) deprecated packages:
- Accumulate List
- Almost Zero
- Alphabetical Sequence
- Altitude And Azimuth From Vector
- Angle Between Vectors
- Angle Bisector
- Angle By Angle Sum
- Binary To Decimal
- Buckyball
- Central Projection On Face
- Central Projection On Plane
- Convex Hull 2D
- Correct Normal Orientation
- Count Sequences Of True Or False
- Count True And False
- Create Placeholder Sheets
- CSV To List
- Curve Array
- Custom Rounding
- Dispatch
- Drop Last Row And Column From UV Field
- Elements From And To IDs
- Equal List Lengths
- Evaluate Divided Surface Grid Nodes
- Exterior Angle
- Family To Type And Back
- Foundation Stuff
- Get And Set Family Type
- Get And Set Name
- Get Bounding Box
- Get Current Revit Document Path
- Get Directory From File Path
- Get Element By Face
- Get Element Location
- Get Faces From Solid
- Get Highest And Lowest From List
- Get Third XYZ Axis
- Group List Of Lists By Key
- Has Out-Of-Plane XYZs
- Hosted Object Stuff
- Increment Or Decrement By 1
- Intersects For Divided Surfaces
- Invert And Mirror Normalized values
- Is Empty
- Is Multiple
- Is Odd Number
- Is Point Inside Polygon
- Is Related To Mass
- Law Of Cosines
- Law Of Sines
- LibG Vector Components
- Lines Through Points (Closed Loop)
- List Not Empty
- Mappable Conditions
- Match List With Key Values
- Material Stuff
- Mesh Stuff
- Move XYZs from Plane To Plane
- Normalization
- Parameter Exists
- Parse Solar Radiation CSV
- Phasing Stuff
- Plane By Reference Or Sketch Plane
- Plane From First 3 XYZs
- Plane From Planar Face
- Plane Properties
- Plane-Vector Intersection
- Project Stuff
- Pythagorean Theorem
- Recursive Boolean Difference
- Regular Expressions
- Remove Duplicates From List
- Replace Substring
- Return List Or Single Value
- Revit API Helpers
- Revit App Version Info
- Roof And Floor Stuff
- Room Stuff
- Select By Category
- Sequence With Leading Zeros
- Similar
- Simple Patterning
- Solve Triangle By XYZs
- Sort List Of Lists
- Standard Colours
- Standard Normals
- Subcategory Stuff
- Sublist Helpers
- Swap UV
- Switch
- Topo Stuff
- Transform Curve Loop
- True And False For Any And All
- Turn Into List
- Unit Conversion
- UV Components
- Vector And Plane Are Parallel
- Vector Is In Plane
- Vector-Vector Intersection
- Vectors Are Orthogonal
- Vectors Are Parallel
- View Stuff
- Wall Stuff
- XYZ Axis From Vector
- XYZ Grid From Face
