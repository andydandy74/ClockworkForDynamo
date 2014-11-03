![Image](clockwork-logo.png)

Clockwork is a collection of custom nodes for the [Dynamo](http://www.dynamobim.org) visual programming environment which can be downloaded from Dynamo's [package manager](http://www.dynamopackages.com). It contains many Revit-related nodes, but also lots of nodes for various other purposes such as list management, vector operations and paneling. Currently it consists of some 200+ nodes that were previously published in a number of separate packages. My reasoning is that keeping all nodes in a single package will make updates easier and reduce package dependencies. I had never set out to build so many custom nodes – somehow it just happened.

If you use Clockwork please remember to uninstall all of my previous packages (see [list below](#packages-to-uninstall)).

Should you find that one of the nodes in this package does not work (or could work better with improved functionality), please let me know by creating a new [issue](https://github.com/CAAD-RWTH/ClockworkForDynamo/issues). Also, if you happen to come across a built-in node that does exactly the same as one of the Clockwork nodes, please let me know so I can remove that particular node from the package.

Since Dynamo's package manager currently does not (yet) have an update notification infrastructure in place, you may want to follow me on twitter ([twitter](https://twitter.com/a_dieckmann)) for update notifications.

#State of migration#

At least for a while, I will maintain two versions this package (one for Dynamo 0.6.3 and one for Dynamo 0.7.x). As soon as 0.7.x supports all (or most) of my 0.6.3 workflows, I will abandon the 0.6.3 branch. Migrating from 0.6.3, I also recategorized and renamed most of the nodes. These changes are documented in an [excel sheet](NodeList.xls) that contains a list of all nodes within the package. This list is colour-coded in order to reflect the state of each node:
- ```GREEN```: Works in 0.7.x
- ```YELLOW```: Still buggy in 0.7.x / needs review / not yet migrated
- ```RED```: Deprecated in 0.7.x

I am currently using the offical 0.6.3 build as well as recent daily builds of Dynamo 0.7.x for testing. Note that nodes known to be buggy in the latest daily builds of Dynamo 0.7.x will not be included in the package until they (or the respective bugs in Dynamo that are causing them to fail) are fixed.

#Material on this repository#

This repository contains the following:

Directory [package_samples](package_samples) contains simple examples for most of the nodes in Clockwork. I use them for occasional testing, but they should also help explain how to use each node. The samples are currently still sorted according to their previous package and limited to 0.6.3 files. I plan to correct that in the future by organizing them according to their respective categories in the node browser and also add 0.7.x versions of the sample files.

Directory [workflow_samples](workflow_samples) contains some sample workflows that I have published online somewhere before. I have also started to include some of the examples that I use for teaching Dynamo. All of these are currently still 0.6.3 files and will be migrated as 0.7.x stability improves and time permits.

Directory [nodes](nodes) is the actual repository of the custom nodes. Particularly the 0.7.x subdirectory may contain nodes that have not been published to the package manager yet.

Directory [issues](issues) contains sample files for issues raised on the [Dynamo GitHub site](https://github.com/DynamoDS/Dynamo).

#Packages to uninstall#
If you have installed Clockwork or are planning to do so, you should uninstall all of my previous packages (that is if you had those installed at all, of course). As a rule of thumb, uninstall everything that is organized in the ```CAAD_RWTH``` category in the node browser. Here's a complete list of all (recently) deprecated packages:
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
